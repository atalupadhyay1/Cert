# Microsoft Exam DP-900: Microsoft Azure Data Fundamentals — Full-Length Mock Exam 4

**Theme:** Connected Manufacturing & Industrial IoT — Parquet/Avro, Indexes, ADLS Gen2, Table Storage, Cassandra/Gremlin & Eventhouse  
**Credential:** `Microsoft Certified: Azure Data Fundamentals` *(Beginner / Fundamentals · **no prerequisite** · **never expires**)*  
**Study guide baseline:** `July 21, 2026` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `75 minutes` (`45 sec/question`, matching live 45-minute / 60-question pace; `45 minutes` optional speed drill · **closed-book**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn documentation — not affiliated with or endorsed by Microsoft Corporation. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Describe core data concepts (25–30% official weight · 28 questions)

### 1. ForgeWorks Manufacturing records CNC bill-of-materials rows in a relational table with strictly typed `PartID`, `AlloyCode`, `ToleranceMicrons`, and `UnitCost` columns across every part. Which data representation is this?

- **A.** Semi-structured data
- **B.** Unstructured data
- **C.** Structured data
- **D.** Apache Avro row-based binary format with JSON schema

### 2. Plant quality inspectors log shift calibration readings into a fixed SQL table where every entry has mandatory `GaugeID`, `CalibratedAt`, and `DeviationMM` numeric fields. How is this dataset categorized?

- **A.** JavaScript Object Notation (JSON) document format
- **B.** Unstructured data
- **C.** Graph database (vertices and directed edges)
- **D.** Structured data

### 3. Robotic weld cells publish compact binary event records prefixed by an embedded JSON schema header, while assembly PLCs emit nested JSON diagnostic documents whose keys vary by robot model. Which two items belong to this flexible schema-embedded / hierarchical world? Select two.

- **A.** Semi-structured data
- **B.** Page blobs in Azure Blob Storage
- **C.** Unstructured data
- **D.** Structured data
- **E.** Apache Avro row-based binary format with JSON schema

### 4. Industrial OPC-UA gateways emit XML and JSON equipment manifests containing self-describing tags and nested sensor arrays that differ between stamping presses and paint ovens. These manifests are ____.

- **A.** Structured data
- **B.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **C.** Semi-structured data
- **D.** Unstructured data

### 5. A smart-factory twin API returns nested machine state objects (`{"cellId": "C14", "spindles": [{"rpm": 8200}, {"rpm": 8190}]}`) over HTTPS. Which text format encodes these nested objects and arrays?

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Page blobs in Azure Blob Storage
- **C.** JavaScript Object Notation (JSON) document format
- **D.** Delimited text format (CSV or TSV)

### 6. Quality-assurance cameras capture high-speed weld-seam `.bmp` images, acoustic bearing `.wav` recordings, and safety training `.mp4` videos stored in Blob containers. Which data type describes these assets?

- **A.** Semi-structured data
- **B.** Structured data
- **C.** Apache Parquet columnar storage format
- **D.** Unstructured data

### 7. Scanned supplier mill-test certificate `.pdf` files and handwritten maintenance logbook `.jpg` photos are uploaded from six factories to Azure Storage. How is this data classified?

- **A.** Structured data
- **B.** First Normal Form (1NF — atomic values and no repeating column groups)
- **C.** Composite key (multi-column key)
- **D.** Unstructured data

### 8. ForgeWorks stores 20 billion historical vibration rows in its lakehouse and wants columnar compression so analytical queries calculating `AVG(VibrationRMS)` skip 60 unused metadata columns. Which two file formats store data in compressed columnar layouts? Select two.

- **A.** Page blobs in Azure Blob Storage
- **B.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **C.** Apache Parquet columnar storage format
- **D.** Delimited text format (CSV or TSV)
- **E.** Optimized Row Columnar (ORC) stripe format

### 9. Why do ForgeWorks Kafka and Event Hubs producers serialize high-velocity PLC telemetry using ____ rather than verbose plain-text CSV when downstream Spark consumers require compact binary rows and graceful schema evolution?

- **A.** Apache Avro row-based binary format with JSON schema
- **B.** Page blobs in Azure Blob Storage
- **C.** Delimited text format (CSV or TSV)
- **D.** Bar or column chart (comparing discrete categorical values across items)

### 10. An industrial fastener vendor exports a flat 400-line price table as plain UTF-8 text separated by commas with no embedded data types or nested arrays. Which file format is this?

- **A.** Apache Avro row-based binary format with JSON schema
- **B.** Apache Parquet columnar storage format
- **C.** Delimited text format (CSV or TSV)
- **D.** Optimized Row Columnar (ORC) stripe format

### 11. ForgeWorks chooses two specialized non-relational databases: one wide-column store to ingest 500,000 sensor writes per second grouped into `thermal` and `torque` column families, and one vertex/edge store to trace multi-tier sub-assembly supplier dependencies during a recall. Which two database categories match? Select two.

- **A.** Delimited text format (CSV or TSV)
- **B.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **C.** Column-family (wide-column) database
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **E.** Graph database (vertices and directed edges)

### 12. A shop-floor badge reader service looks up operator shift tokens exclusively by `BadgeHash` in under 2 milliseconds with zero relational joins or nested document queries. Which non-relational store model fits best?

- **A.** Graph database (vertices and directed edges)
- **B.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **C.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **D.** Key-value non-relational store

### 13. Each custom turbine order has a unique nested specification sheet (`bladePitch`, `coatingLayers[]`, `testBenchConfig`) queried across nested JSON properties. Which non-relational database model fits best?

- **A.** Database view (saved virtual `SELECT` query)
- **B.** Document database
- **C.** Line chart (tracking continuous trends and changes over ordered time intervals)
- **D.** Third Normal Form (3NF — no transitive dependencies between non-key columns)

### 14. ForgeWorks is architecting its cloud estate from live ERP work-order releases through global OEE (`Overall Equipment Effectiveness`) dashboards. Which four-step Azure service flow places each workload properly?

- **A.** Capture OLTP writes in Azure SQL Database → Extract changes via Data Factory pipeline → Land Parquet files in ADLS Gen2 / OneLake → Serve star-schema visuals in Power BI
- **B.** Capture OLTP writes directly in Archive Blob tier → Run live checkout queries in Power BI Desktop → Copy rows to Azure Files SMB → Normalize into Azure Table storage
- **C.** Land raw checkout clicks in Paginated Reports → Transform via SMB file locks → Commit ACID transactions in Azure Blob Cold tier → Query via Gremlin graph vertices
- **D.** Serve live checkout writes in Power BI Service → Export dashboards to CSV → Load CSVs into Azure SQL Database → Archive active rows to Azure Queue storage

### 15. ForgeWorks needs a petabyte-scale cloud lake store with POSIX directory ACLs and hierarchical folders to land raw Parquet and Avro telemetry for Databricks and Synapse jobs. Which Azure storage capability is purpose-built for this?

- **A.** Azure Data Lake Storage Gen2 (Blob Storage with Hierarchical Namespace enabled)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

### 16. To store 90 million lightweight firmware-version status records keyed simply by `PlantCode` (`PartitionKey`) and `ControllerSerial` (`RowKey`) at minimal monthly cost, which Azure Storage service fits?

- **A.** Store 20 GB CAD engineering drawings inside single Azure Queue storage messages
- **B.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **C.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 17. ForgeWorks' warehouse barcoding app processes live inventory picks (`UPDATE BinStock`), shields concurrent forklift scans from reading uncommitted counts, and guarantees committed picks survive a power outage. Which three concepts describe these requirements? Select three.

- **A.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **B.** Online Transaction Processing (OLTP) workload
- **C.** Isolation (concurrent transactions do not interfere)
- **D.** Durability (committed writes survive restarts or crashes)
- **E.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **F.** Online Analytical Processing (OLAP) workload

### 18. When releasing a work order, reserving raw steel coils and creating the production batch must execute as a single indivisible unit: if coil reservation fails, the batch header rolls back automatically. Which ACID property is this?

- **A.** Apache Parquet columnar storage format
- **B.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **C.** Atomicity (all-or-nothing transaction unit)
- **D.** Online Analytical Processing (OLAP) workload

### 19. Database `CHECK (ScrapQty >= 0)` and foreign-key constraints ensure no production transaction can leave the database in a rule-violating state. Which ACID property describes preserving all defined data-integrity rules across transactions?

- **A.** Cool access tier (online, 30-day minimum retention for infrequently accessed data)
- **B.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)
- **C.** Denormalize the live checkout table with five years of historical aggregates and disable ACID transaction locks
- **D.** Consistency (valid schema and constraint state)

### 20. ForgeWorks' plant controllers analyze five years of scrap rates, cycle times, and energy kWh per unit across `FactProductionRuns` joined in a single hop to `DimMachine`, `DimShift`, and `DimPart`. Which two concepts apply? Select two.

- **A.** Online Transaction Processing (OLTP) workload
- **B.** Page blobs in Azure Blob Storage
- **C.** Online Analytical Processing (OLAP) workload
- **D.** Atomicity (all-or-nothing transaction unit)
- **E.** Star schema (central numeric fact table joined directly to denormalized dimension tables)

### 21. Proposed solution: To protect shop-floor latency, ForgeWorks offloads multi-year supplier defect `GROUP BY` scans away from the live MES production database into a dedicated ____ warehouse. Why is this workload separation recommended?

- **A.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **B.** Online Analytical Processing (OLAP) workload
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** Online Transaction Processing (OLTP) workload

### 22. In ForgeWorks' analytical warehouse, `FactMaintenance` joins to `DimAsset`, which normalizes into `DimMachineModel`, which normalizes into `DimOEMVendor`. What schema pattern does this normalized dimension chain form?

- **A.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **B.** Append blobs in Azure Blob Storage
- **C.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **D.** First Normal Form (1NF — atomic values and no repeating column groups)

### 23. At ForgeWorks, which specialist configures Azure SQL geo-replication, applies Transparent Data Encryption (`TDE`), manages login permissions, and tunes OLTP query execution plans for the MES database?

- **A.** Database administrator (DBA)
- **B.** Data engineer
- **C.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)
- **D.** Data analyst

### 24. When a runaway ERP batch session blocks shop-floor transactions, who investigates active lock waits, resolves blocking sessions, and adjusts index maintenance schedules on the database server?

- **A.** Data engineer
- **B.** Data analyst
- **C.** Database administrator (DBA)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

### 25. ForgeWorks is deploying an enterprise manufacturing lakehouse across Azure SQL, Microsoft Fabric, and Power BI. Which four-step workflow reflects proper role ownership across DBA, data engineer, and data analyst?

- **A.** Data analyst configures SQL Server failover clusters → DBA authors Spark ELT notebooks in Databricks → Data engineer designs executive Power BI visuals → DBA schedules workspace app audiences
- **B.** Data engineer grants T-SQL row permissions on OLTP → Data analyst provisions Azure VNet private endpoints → DBA builds Power Query Dataflows Gen2 → Data analyst runs point-in-time DB restores
- **C.** DBA designs executive KPI scorecards → Data analyst writes Spark Structured Streaming checkpoints → Data engineer tunes OLTP clustered indexes → DBA publishes paginated sales packs
- **D.** DBA provisions & secures operational Azure SQL → Data engineer builds ELT pipelines into Fabric Lakehouse → Data engineer curates Gold star-schema tables → Data analyst models DAX KPIs & publishes Power BI reports

### 26. Which data professional authors PySpark notebooks and Data Factory pipelines that ingest raw OPC-UA Parquet drops, standardize engineering units (`psi` to `kPa`), and populate Gold Delta tables?

- **A.** Database administrator (DBA)
- **B.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **C.** Data analyst
- **D.** Data engineer

### 27. Plant managers want an interactive OEE Power BI scorecard breaking down `Availability x Performance x Quality` with drill-through visuals by assembly line and shift. Which role designs this semantic model and report?

- **A.** Azure Migrate (discovery, readiness assessment, and SKU right-sizing for SQL Server)
- **B.** Data analyst
- **C.** Database administrator (DBA)
- **D.** Data engineer

### 28. Connecting to curated Gold manufacturing tables, a specialist builds scrap-pareto bar visuals and `First Pass Yield %` DAX measures to brief quality executives. This specialist serves as a ____.

- **A.** Data analyst
- **B.** Database administrator (DBA)
- **C.** Page blobs in Azure Blob Storage
- **D.** Data engineer

---

## Domain 2 — Identify considerations for relational data on Azure (20–25% official weight · 24 questions)

### 29. In ForgeWorks' relational database, `WorkOrderParts` uses `(WorkOrderID, PartID)` together as its unique row identifier, while `PartID` also references `Parts.PartID` to prevent invalid part numbers. Which two relational key concepts are applied? Select two.

- **A.** Append blobs in Azure Blob Storage
- **B.** Unstructured data
- **C.** Foreign key constraint
- **D.** Composite key (multi-column key)
- **E.** Session window (variable-length activity bursts closed after a quiet timeout gap)

### 30. In the `Machines` table, `MachineID` uniquely identifies every press on the shop floor and rejects `NULL` or duplicate values. `MachineID` is enforced by a ____.

- **A.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **B.** Foreign key constraint
- **C.** Primary key constraint
- **D.** Apache Avro row-based binary format with JSON schema

### 31. Proposed solution: A plant developer wants the database engine itself — without relying solely on UI code — to block inserting a `WorkOrders` row whose `LineID` does not exist in `AssemblyLines`; the DBA adds a ____ constraint from `WorkOrders.LineID` to `AssemblyLines.LineID`. What completes this solution?

- **A.** First Normal Form (1NF — atomic values and no repeating column groups)
- **B.** Page blobs in Azure Blob Storage
- **C.** Foreign key constraint
- **D.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)

### 32. Why are relational tables able to enforce consistent arithmetic (`SUM(ScrapCount)`) and date comparisons across millions of rows without per-row type parsing?

- **A.** Structured data
- **B.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **C.** Semi-structured data
- **D.** Unstructured data

### 33. ForgeWorks inherits a legacy spreadsheet of tooling inspections containing comma-separated defect codes and repeated supplier city/state columns. Which four-step workflow normalizes the tables through 3NF?

- **A.** Split repeating groups into atomic columns (1NF) → Assign a unique primary key → Move partial composite-key dependencies to parent tables (2NF) → Extract transitive non-key dependencies into lookup tables (3NF)
- **B.** Create foreign keys on unsplit multi-value columns → Denormalize all lookup tables into one wide sheet → Remove partial dependencies (2NF) → Split atomic columns into repeating groups (1NF)
- **C.** Cluster-index raw JSON blobs → Delete primary keys on parent tables → Copy supplier city into every invoice item (2NF) → Combine product names into pipe-delimited strings (3NF)
- **D.** Remove transitive non-key dependencies (3NF) → Merge comma-separated phone lists into one column → Delete all primary keys to speed inserts → Duplicate customer addresses across every order line

### 34. A `MachineCertifications` table contains columns `Cert1`, `Cert2`, `Cert3`, and `Cert4` for operator badges. Replacing those repeating columns with atomic child rows in an `OperatorCertifications` table satisfies ____.

- **A.** First Normal Form (1NF — atomic values and no repeating column groups)
- **B.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **C.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **D.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)

### 35. In a 1NF `BillOfMaterials` table keyed by `(AssemblyID, ComponentID)`, column `ComponentWeightGrams` depends only on `ComponentID`. Moving `ComponentWeightGrams` to `Components` achieves ____.

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** First Normal Form (1NF — atomic values and no repeating column groups)
- **C.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **D.** Second Normal Form (2NF — full functional dependency on the entire composite key)

### 36. In a 2NF `Plants` table keyed by `PlantID`, non-key column `CountryISO` determines `CountryCurrencyCode`. Moving `CountryISO -> CountryCurrencyCode` into a `Countries` table eliminates update anomalies and satisfies ____.

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Optimized Row Columnar (ORC) stripe format
- **C.** First Normal Form (1NF — atomic values and no repeating column groups)
- **D.** Second Normal Form (2NF — full functional dependency on the entire composite key)

### 37. Classify three SQL commands executed during a MES release: `CREATE INDEX ix_Lot ON Lots(LotCode)` (1), `DELETE FROM StagingLots WHERE Processed = 1` (2), and `DENY DELETE ON Lots TO ShiftViewers` (3). Which three SQL categories are represented? Select three.

- **A.** Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- **B.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **E.** Apache Parquet columnar storage format
- **F.** Cold access tier (online, 90-day minimum retention for rarely accessed data)

### 38. ForgeWorks wants a list of **all** 240 factory machines from the left `Machines` table together with any `DowntimeEvents` logged today, showing `NULL` downtime columns for machines that ran with zero downtime. Which SQL join is required?

- **A.** Use DML `SELECT` and `INSERT` statements to grant or revoke user login permissions on schemas
- **B.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **C.** `LEFT OUTER JOIN` preserving all left-table rows with `NULL` when right-table matches are absent
- **D.** `INNER JOIN` matching related keys present in both tables

### 39. To return assembly lines that produced more than 5,000 units **considering only** `Shift = 'Day'` rows, an analyst writes `SELECT LineID, SUM(Units) FROM Runs ____ Shift = 'Day' GROUP BY LineID ____ SUM(Units) > 5000;`. Which clauses fill the two blanks?

- **A.** `WHERE` filters rows before grouping; `HAVING` filters aggregated groups after `GROUP BY`
- **B.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** Place `SUM()` or `COUNT(*)` aggregate predicates directly inside the SQL `WHERE` clause before `GROUP BY`

### 40. When a database engineer executes `ALTER TABLE Sensors ADD MaxThreshold DECIMAL(10,2) NOT NULL DEFAULT 100.0`, which SQL statement category is used?

- **A.** Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- **B.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** Use DML `SELECT` and `INSERT` statements to grant or revoke user login permissions on schemas

### 41. Proposed solution: On `ProductionLots` (200 million rows), the DBA defines one ____ on `LotID` to control physical row sort order on disk and adds two ____ structures on `PartNumber` and `CompletionDate` for fast secondary lookups. Which two index types are used? Select two.

- **A.** Append blobs in Azure Blob Storage
- **B.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **C.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **D.** Nonclustered index (separate B-tree structure with row locators; multiple allowed per table)
- **E.** Database view (saved virtual `SELECT` query)

### 42. ForgeWorks creates `vw_VendorShipments` (`CREATE VIEW vw_VendorShipments AS SELECT ...`) joining `PurchaseOrders`, `Vendors`, and `Receipts` while omitting internal unit-margin columns. What does `vw_VendorShipments` store in the database?

- **A.** Page blobs in Azure Blob Storage
- **B.** Database view (saved virtual `SELECT` query)
- **C.** Create four separate clustered indexes on the same relational table to sort rows four ways physically
- **D.** Stored procedure (parameterized precompiled SQL routine)

### 43. Shop-floor PLC gateways call `EXEC usp_RecordScrap @LineID = 7, @ReasonCode = 'WELD', @Qty = 3` so validation, scrap insertion, and inventory adjustment execute as precompiled server-side SQL logic. What object is `usp_RecordScrap`?

- **A.** Stored procedure (parameterized precompiled SQL routine)
- **B.** Nonclustered index (separate B-tree structure with row locators; multiple allowed per table)
- **C.** Apache Avro row-based binary format with JSON schema
- **D.** Database view (saved virtual `SELECT` query)

### 44. Why does adding a targeted ____ on `SerialNumber` dramatically speed up `SELECT * FROM Units WHERE SerialNumber = 'SN-992814'` on a 50-million-row table already clustered by `ManufactureDate`?

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Create four separate clustered indexes on the same relational table to sort rows four ways physically
- **C.** Nonclustered index (separate B-tree structure with row locators; multiple allowed per table)
- **D.** Database view (saved virtual `SELECT` query)

### 45. ForgeWorks plans to migrate eight on-premises SQL Server MES databases into Azure SQL PaaS with zero surprise compatibility failures. Which four-step sequence follows current Microsoft guidance?

- **A.** Disable TLS encryption on SQL Server → Copy `.mdf` files directly into Azure Table storage → Provision Azure SQL Database Basic tier for cross-DB SQL Agent jobs → Run Azure Migrate discovery
- **B.** Assess SQL Server readiness and SKU sizing in Azure Migrate → Select Azure SQL Database or Managed Instance → Provision target with Entra auth and TLS firewall rules → Migrate schema/data and cut over connection strings
- **C.** Convert relational tables into Azure Queue messages → Provision SQL Managed Instance without VNet planning → Run compatibility assessment last → Remove all primary keys before cutover
- **D.** Point production apps to an empty Azure SQL server → Open firewall `0.0.0.0-255.255.255.255` to the public internet → Assess SQL Agent blockers after cutover → Export tables manually as JPEG screenshots

### 46. ForgeWorks provisions two Azure PaaS SQL targets: Target 1 hosts a digital-twin sandbox used 6 hours per week that should auto-pause compute when idle; Target 2 hosts a plant ERP requiring SQL Server Agent jobs and cross-database queries without OS patching. Which two offerings match? Select two.

- **A.** Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)
- **B.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **C.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **E.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 47. An industrial historian vendor certifies its software **only** on SQL Server 2019 running on Windows Server 2022 with direct DCOM access to a local C++ service on the database VM. Which Azure option is required?

- **A.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **B.** Azure Database for PostgreSQL — Flexible Server
- **C.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **D.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)

### 48. ForgeWorks provides dedicated single-tenant Azure SQL Databases for 140 global OEM suppliers whose portal traffic peaks in different time zones around the clock. Which model shares vCores across all 140 databases economically?

- **A.** Use a single Azure SQL Database to run native SQL Server Agent jobs and cross-database three-part queries
- **B.** Azure SQL Database Elastic Pool (shared eDTU or vCore compute across multi-tenant DBs)
- **C.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 49. Which Microsoft service discovers on-premises SQL Server estates, flags PaaS feature blockers, and produces performance-based SKU sizing recommendations for Azure SQL Database, Managed Instance, and Azure VMs?

- **A.** Azure Migrate (discovery, readiness assessment, and SKU right-sizing for SQL Server)
- **B.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **C.** Run the retired standalone Data Migration Assistant (DMA) desktop tool as Microsoft’s current cloud sizing service
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

### 50. ForgeWorks' robotics calibration platform uses PostgreSQL custom array/composite types, `PL/pgSQL` stored functions, and `pgAdmin` diagnostics, and wants managed Azure PaaS with built-in HA. Which service fits?

- **A.** Azure Database for MySQL — Flexible Server
- **B.** Azure Database for PostgreSQL — Flexible Server
- **C.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 51. A supplier documentation portal runs on a classic `LAMP` (`Linux, Apache, MySQL, PHP`) stack and needs a managed Azure PaaS relational backend with automated backups up to 35 days. Which service should IT provision?

- **A.** Azure Database for PostgreSQL — Flexible Server
- **B.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **C.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **D.** Azure Database for MySQL — Flexible Server

### 52. To tune slow calibration queries on Azure Database for PostgreSQL — Flexible Server, a DBA enables Query Store and queries execution statistics recorded in `query_store.qs_view` inside the system database named ____.

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **C.** Use a single Azure SQL Database to run native SQL Server Agent jobs and cross-database three-part queries
- **D.** Azure Database for PostgreSQL — Flexible Server

---

## Domain 3 — Describe considerations for working with non-relational data on Azure (15–20% official weight · 20 questions)

### 53. X-ray weld inspection images are checked daily during month one, occasionally up to day 90, rarely up to year one, and kept 10 years for aerospace audit compliance. Which four-step Blob lifecycle sequence minimizes cost?

- **A.** Write unstructured video files into Azure Table `RowKey` cells → Age rows from Cool to Hot after 180 days → Convert Page blobs into SQL views → Rehydrate Cool blobs for 12 hours before reading
- **B.** Mount Archive blobs as an SMB network drive → Stream live append logs into Page blobs in Cold tier → Transition 1-year compliance archives to Hot tier → Rehydrate Hot blobs before every read
- **C.** Ingest active files into Hot access tier → Transition 30-day infrequent blobs to Cool tier → Move 90-day rarely read blobs to Cold tier → Transition 365-day compliance blobs to offline Archive tier (rehydrating when needed)
- **D.** Ingest active operational files directly into Archive tier → Serve millisecond web downloads from Archive without rehydration → Move 90-day files to Hot tier → Delete storage account container metadata

### 54. ForgeWorks configures an Azure Storage account with Hierarchical Namespace enabled for Spark Parquet folders and sets a lifecycle rule moving 95-day-old quality PDFs to the lowest-cost **online** tier (90-day minimum retention, instant reads). Which two capabilities are used? Select two.

- **A.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **B.** Azure Data Lake Storage Gen2 (Blob Storage with Hierarchical Namespace enabled)
- **C.** Cold access tier (online, 90-day minimum retention for rarely accessed data)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **E.** Page blobs in Azure Blob Storage

### 55. Which Azure Blob type organizes storage as an array of 512-byte pages optimized for random byte-offset reads and writes backing Azure IaaS virtual machine disks?

- **A.** Page blobs in Azure Blob Storage
- **B.** Block blobs in Azure Blob Storage
- **C.** Append blobs in Azure Blob Storage
- **D.** Delimited text format (CSV or TSV)

### 56. Shop-floor safety PLCs write tamper-evident event lines strictly to the end of daily log blobs where in-place block updates are prohibited. Which Azure Blob type is purpose-built for this?

- **A.** Append blobs in Azure Blob Storage
- **B.** Store active operational files directly in Azure Blob Archive tier for immediate millisecond web reads
- **C.** Page blobs in Azure Blob Storage
- **D.** Block blobs in Azure Blob Storage

### 57. Proposed solution: An engineer places active CNC G-code programs needed every 5 minutes by shop-floor machines into the Azure Blob Archive tier expecting immediate millisecond downloads; why does this fail, and what defines the ____?

- **A.** Cool access tier (online, 30-day minimum retention for infrequently accessed data)
- **B.** Store active operational files directly in Azure Blob Archive tier for immediate millisecond web reads
- **C.** Hot access tier (highest storage rate, lowest read/write access cost)
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 58. ForgeWorks' firmware build farm mounts shared `NFS 4.1` volumes on Linux runners while plant Windows file servers replicate local SMB tool-drawing folders to Azure and tier old revisions to the cloud. Which two services handle this? Select two.

- **A.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Block blobs in Azure Blob Storage
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **E.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)

### 59. Legacy CNC post-processor software on Windows workstations requires opening shared tooling libraries via an SMB UNC path (`\\cncshare\postproc\`) using Kerberos/SMB authentication. Which Azure Storage service supports this natively?

- **A.** Append blobs in Azure Blob Storage
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)

### 60. When a plant's local Windows Server disk fills up, which service's **cloud tiering** policy converts rarely opened CAD assemblies into lightweight NTFS reparse pointers while keeping the full files safely in Azure Files?

- **A.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **B.** Apache Spark Structured Streaming (fault-tolerant DataFrame/SQL stream processing in Databricks and Fabric)
- **C.** Azure Data Lake Storage Gen2 (Blob Storage with Hierarchical Namespace enabled)
- **D.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)

### 61. ForgeWorks stores 200 million tool-wear counter records indexed by `FactoryID` (`PartitionKey`) and `SpindleSerial` (`RowKey`) where newer spindles include extra `coatingTemp` properties without altering older rows. Which Azure Storage service fits?

- **A.** Enforce server-side foreign keys and multi-table SQL `INNER JOIN` queries inside Azure Table storage
- **B.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 62. Proposed solution: When ForgeWorks expands its `PartitionKey`/`RowKey` spindle registry globally across Munich, Detroit, and Osaka plants and needs `<10 ms` multi-region writes plus automatic secondary property indexes, the team migrates from basic Azure Table storage to ____. Does this upgrade meet the requirements with minimal SDK changes?

- **A.** Page blobs in Azure Blob Storage
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **D.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)

### 63. Why must every entity inside an ____ table include `PartitionKey` and `RowKey` system properties (alongside system `Timestamp`)?

- **A.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **B.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Enforce server-side foreign keys and multi-table SQL `INNER JOIN` queries inside Azure Table storage

### 64. ForgeWorks runs a global aerospace part-serial lock registry on Azure Cosmos DB replicated across multiple continents; aerospace safety rules require linearizable reads so no two plants ever read a stale serial-allocation state. Which two Cosmos DB concepts apply? Select two.

- **A.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **B.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **C.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **D.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **E.** Azure Cosmos DB turnkey global distribution with multi-region writes and <10 ms SLAs

### 65. ForgeWorks configures an Azure Cosmos DB container with **Autoscale** max `4,000` units so throughput scales automatically between `400` and `4,000` units based on real-time factory shift load. What unit is being scaled?

- **A.** Line chart (tracking continuous trends and changes over ordered time intervals)
- **B.** Request Units (RUs) normalized compute/IO currency (Provisioned, Autoscale, or Serverless)
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** Append blobs in Azure Blob Storage

### 66. Which default Azure Cosmos DB consistency level balances performance and accuracy for shop-floor tablet apps by guaranteeing each operator tablet reads its own submitted quality checks immediately in order?

- **A.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating
- **B.** Session consistency (default level guaranteeing read-your-own-writes and monotonic reads per client session)
- **C.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **D.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)

### 67. Ambient warehouse humidity widgets read from globally replicated Cosmos DB containers where temporary 1-second replica lag is irrelevant and minimizing RU cost is the top priority. Which consistency level fits?

- **A.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)
- **B.** Atomicity (all-or-nothing transaction unit)
- **C.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **D.** Third Normal Form (3NF — no transitive dependencies between non-key columns)

### 68. ForgeWorks is creating a greenfield Azure Cosmos DB store for digital-twin JSON machine configurations partitioned by `/machineId`. Which four-step workflow is valid?

- **A.** Install OS patches on Cosmos DB virtual machines → Format NTFS volumes for JSON items → Assign a constant single-value partition key to all 100 million documents → Query exclusively with T-SQL stored procedures
- **B.** Create a container without a partition key → Switch the existing account between Cassandra, Gremlin, and NoSQL APIs daily → Enforce 3NF foreign-key joins across containers → Store 500 MB MP4 blobs inside single JSON items
- **C.** Create a Cosmos DB account choosing the target API → Create a database and container with a high-cardinality partition key → Configure RU/s or serverless and consistency → Insert items and run partition-scoped queries
- **D.** Provision an Azure Files SMB share → Enable Strong consistency across 5 multi-write regions simultaneously → Omit databases and write JSON straight to subscription tags → Query vertices using `SMB2` locks

### 69. ForgeWorks' vibration-monitoring platform already writes wide-column time-series rows using Apache Cassandra `CQL` drivers and wants zero-maintenance Azure PaaS hosting. Which Cosmos DB API should be selected?

- **A.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **B.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)

### 70. During an avionics batch recall, quality engineers traverse `RawIngot -> ForgedBillet -> MachinedShaft -> SubAssembly -> AircraftTail` relationships stored as vertices and directed edges in Cosmos DB. Which API powers this graph traversal?

- **A.** Azure Cosmos DB for MongoDB (wire-protocol compatibility for BSON document apps)
- **B.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **C.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **D.** Block blobs in Azure Blob Storage

### 71. A new Rust microservice stores flexible JSON torque-wrench calibration certificates in Cosmos DB and queries nested JSON arrays with `SELECT * FROM c WHERE ARRAY_CONTAINS(c.flags, 'RECHECK')`. Which Cosmos DB API is used?

- **A.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **B.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **C.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **D.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating

### 72. An acquired 3D-printing lab stores BSON print-job manifests via the official MongoDB Go driver and wants turnkey Azure Cosmos DB geo-replication without changing application query code. Which API fits?

- **A.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **B.** Azure Cosmos DB for MongoDB (wire-protocol compatibility for BSON document apps)
- **C.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

---

## Domain 4 — Describe an analytics workload on Azure (25–30% official weight · 28 questions)

### 73. ForgeWorks consolidates MES, ERP, and OPC-UA telemetry into Microsoft Fabric OneLake using a medallion architecture. Which four-step sequence implements ELT across Bronze, Silver, and Gold layers?

- **A.** Extract source data via Data Factory pipeline → Land raw files into OneLake / ADLS Gen2 (Bronze) → Cleanse and conform Delta tables via Spark or SQL (Silver) → Model star-schema fact/dimension tables (Gold) for BI
- **B.** Build Power BI visuals directly against uncleaned CSV attachments → Delete raw source history immediately → Normalize Gold tables into 3NF OLTP row stores → Export final aggregates back into email inboxes
- **C.** Publish Gold star schema before ingesting source data → Run OLTP checkout locks inside Power BI Mobile → Overwrite source ERP primary keys during read → Store Parquet files in DNS TXT records
- **D.** Transform terabytes on the client laptop in Notepad → Upload screenshots to Archive Blob tier → Query offline blobs live with DAX → Store fact tables inside Azure Queue messages

### 74. ForgeWorks builds scheduled orchestration pipelines that copy nightly SAP material tables via a Self-Hosted Integration Runtime, run visual Power Query Dataflows Gen2 transformations, and trigger Spark notebooks. Which service provides this?

- **A.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Azure Data Factory / Fabric Data Factory pipelines and Dataflows Gen2
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

### 75. Export-controlled defense tolerances (`ITAR` fields) must be stripped and anonymized inside an on-premises staging engine **before** any file is ever written to the cloud analytical store. Which ingestion pattern is required?

- **A.** Page blobs in Azure Blob Storage
- **B.** Extract, Transform, and Load (ETL) pattern
- **C.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)
- **D.** Extract, Load, and Transform (ELT) pattern

### 76. ForgeWorks stores analytical tables as ACID **Delta Lake** Parquet files in OneLake (`FactScrap`), while normalizing `DimPart -> DimPartFamily -> DimCommodityGroup`. Which two analytical data-store concepts are present? Select two.

- **A.** Online Transaction Processing (OLTP) workload
- **B.** Data lakehouse (Delta Lake ACID transactions and SQL/Spark queries directly over open Parquet files)
- **C.** Key-value non-relational store
- **D.** Append blobs in Azure Blob Storage
- **E.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)

### 77. In ForgeWorks' OEE warehouse, `FactOEE` contains numeric `RunMinutes`, `PlannedMinutes`, and `GoodUnits`, surrounded by single-hop `DimDate`, `DimMachine`, and `DimOperator` tables. Which schema design is this?

- **A.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **B.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **C.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 78. Why does Microsoft Fabric's Lakehouse store managed tables in the open **Delta Lake** (`Parquet` + `_delta_log`) format inside OneLake?

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Data lakehouse (Delta Lake ACID transactions and SQL/Spark queries directly over open Parquet files)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Second Normal Form (2NF — full functional dependency on the entire composite key)

### 79. ForgeWorks compares three cloud analytics services: (1) Microsoft Fabric SaaS over OneLake, (2) Azure Databricks collaborative Spark + ML, and (3) Azure Synapse Analytics serverless/dedicated SQL + Spark pools. Which three services are these? Select three.

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Azure Synapse Analytics (serverless SQL pools, dedicated MPP SQL pools, and Spark pools)
- **C.** Microsoft Fabric (unified SaaS analytics platform atop OneLake)
- **D.** Azure Databricks (collaborative Apache Spark analytics, Delta Lake, and ML platform)
- **E.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **F.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 80. In ____, a T-SQL **Data Warehouse** and a Spark **Lakehouse** sit side by side in the same SaaS workspace and can run cross-database T-SQL joins over OneLake Delta tables with zero data movement.

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Microsoft Fabric (unified SaaS analytics platform atop OneLake)
- **C.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **D.** Azure HDInsight (managed open-source Hadoop, Hive, HBase, Kafka, and Spark clusters)

### 81. ForgeWorks' predictive-maintenance data scientists train anomaly models on 50 TB of spindle vibration spectrograms using distributed PySpark, Delta Live Tables, and MLflow in collaborative notebooks. Which Azure service fits best?

- **A.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Azure Databricks (collaborative Apache Spark analytics, Delta Lake, and ML platform)
- **D.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)

### 82. A legacy steel-mill acquisition runs custom Java MapReduce and Apache Hive scripts built for on-premises Hadoop clusters and wants managed open-source Hadoop/Hive clusters in Azure. Which service matches?

- **A.** Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)
- **B.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **C.** Azure HDInsight (managed open-source Hadoop, Hive, HBase, Kafka, and Spark clusters)
- **D.** Cool access tier (online, 30-day minimum retention for infrequently accessed data)

### 83. A spindle-overheat rule triggers an alert the instant the average bearing temperature over the **preceding 30 seconds** exceeds `95°C`, evaluating only when telemetry events enter or age out of that 30-second window. Which window type is this?

- **A.** Optimized Row Columnar (ORC) stripe format
- **B.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **C.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **D.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)

### 84. ForgeWorks calculates non-overlapping 10-minute energy kWh totals (`06:00–06:10`, `06:10–06:20`) across plant substations so utility charges never double-count an event across adjacent windows. Which window function fits?

- **A.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **B.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **C.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **D.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)

### 85. At `23:55` each night, ForgeWorks reconciles completed shift production counts against ERP raw-material consumption for daily accounting close. This scheduled bounded job is ____.

- **A.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **B.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)
- **C.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **D.** Batch data processing (scheduled execution over bounded collections of accumulated records)

### 86. Laser-cutter optical sensors inspect every cut edge continuously in flight and halt the gantry within 80 milliseconds if plasma drift is detected. This sub-second continuous pattern is ____.

- **A.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **B.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)
- **C.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **D.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)

### 87. ForgeWorks evaluates two Microsoft real-time analytics engines: Engine A ingests OPC-UA streams via Fabric **Eventstream** into an **Eventhouse** `KQL` database with **Activator** rules; Engine B runs standalone serverless Azure SQL-like temporal window jobs from Event Hubs. Which two offerings are Engine A and Engine B? Select two.

- **A.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Microsoft Fabric Real-Time Intelligence (Eventstream, Eventhouse KQL database, Real-Time Dashboards, and Activator)
- **D.** Azure Stream Analytics (serverless SQL-like stream processing engine with windowing functions)
- **E.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 88. Proposed solution: Plant reliability engineers want to store 5 billion timestamped PLC log events in Microsoft Fabric, query anomalies interactively in milliseconds with **KQL**, display live shop-floor tiles, and trigger Teams alerts automatically via **Activator** — all inside ____. What completes this solution?

- **A.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **B.** Cold access tier (online, 90-day minimum retention for rarely accessed data)
- **C.** Microsoft Fabric Real-Time Intelligence (Eventstream, Eventhouse KQL database, Real-Time Dashboards, and Activator)
- **D.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)

### 89. Which Azure service acts as a partitioned cloud telemetry ingestion buffer capable of receiving millions of factory IoT / Kafka events per second and replaying retained partitions to multiple downstream stream processors?

- **A.** Database view (saved virtual `SELECT` query)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Azure Event Hubs (high-throughput partitioned event ingestion broker with Kafka support)

### 90. Data engineers in Microsoft Fabric write a PySpark job using `spark.readStream` and `writeStream` with checkpoint directories to continuously merge live IoT defect events into a Lakehouse Delta table. Which streaming engine is used?

- **A.** Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)
- **B.** First Normal Form (1NF — atomic values and no repeating column groups)
- **C.** Delimited text format (CSV or TSV)
- **D.** Apache Spark Structured Streaming (fault-tolerant DataFrame/SQL stream processing in Databricks and Fabric)

### 91. ForgeWorks' BI team wants to transform plant quality tables, author DAX OEE measures, pin a cross-plant executive dashboard, and distribute governed access to 120 plant supervisors. Which four-step Power BI sequence is valid?

- **A.** Pin dashboard tiles in Power BI Desktop offline → Write Power Query M transformations inside Power BI Mobile → Store semantic models on SMB floppy shares → Require every executive viewer to edit DAX in Desktop
- **B.** Author multi-report dashboards inside Power BI Mobile → Export `.pbix` files to Azure Table storage → Schedule dataset refresh inside Windows Notepad → Email raw database passwords to report viewers
- **C.** Design `.rdl` pixel-perfect invoices in Azure Stream Analytics → Publish directly to unmanaged personal OneDrive as an OLTP database → Disable table relationships → Share via anonymous firewall port `1433`
- **D.** Shape source data with Power Query in Power BI Desktop → Relate star-schema tables, write DAX, and build report pages → Publish model and report to Power BI Service → Pin dashboard tiles, schedule refresh, and share an App

### 92. Where do ForgeWorks analysts use **Power Query Editor** to unpivot sensor columns, configure star-schema relationships in **Model view**, and author multi-page `.pbix` interactive reports before publishing to the cloud?

- **A.** Microsoft Power BI Service (cloud SaaS portal for workspaces, dashboards, scheduled refresh, and Apps)
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Create multi-report pinned dashboards directly inside Power BI Desktop offline
- **D.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)

### 93. Aerospace customers require a shipped paper/PDF **Certificate of Conformance** listing all 600 lot-traceability measurements across multiple fixed-margin pages without scrollbars. Which Power BI authoring tool produces `.rdl` paginated reports?

- **A.** Microsoft Power BI Service (cloud SaaS portal for workspaces, dashboards, scheduled refresh, and Apps)
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Azure Event Hubs (high-throughput partitioned event ingestion broker with Kafka support)
- **D.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)

### 94. In Power BI, ForgeWorks configures `1:*` relationships between `DimMachine` and `FactOEE`, defines a `Plant -> Area -> Cell -> Machine` drill hierarchy, and creates `Scrap % := DIVIDE(SUM(FactOEE[ScrapUnits]), SUM(FactOEE[TotalUnits]))`. Which two concepts are used? Select two.

- **A.** Power BI semantic model (relationships, DAX measures, hierarchies, and Import/DirectQuery/Direct Lake storage)
- **B.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **E.** Append blobs in Azure Blob Storage

### 95. Why does `OEE %` defined as a ____ recalculate accurately when a plant manager slices by `Shift = Night` or `Plant = Stuttgart`, whereas a precomputed static row column averaged across unequal shift sizes would be mathematically wrong?

- **A.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **B.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** Page blobs in Azure Blob Storage

### 96. In Power BI, hiding technical surrogate keys (`MachineKey`, `DateKey`) from Report view while keeping them active on `1:*` relationships is configured inside the ____.

- **A.** Power BI semantic model (relationships, DAX measures, hierarchies, and Import/DirectQuery/Direct Lake storage)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **D.** Session window (variable-length activity bursts closed after a quiet timeout gap)

### 97. When designing a Power BI semantic model over manufacturing data, organizing lookup attributes into `DimPart`, `DimPlant`, and `DimDate` around numeric `FactProduction` follows the recommended ____ design.

- **A.** Append blobs in Azure Blob Storage
- **B.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **C.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **D.** Key-value non-relational store

### 98. A quality engineer wants to rank the top 10 scrap reason codes (`Porosity`, `Burr`, `Misalignment`, etc.) from highest to lowest total scrapped units in Q2. Which Power BI visual compares discrete categories clearest?

- **A.** Bar or column chart (comparing discrete categorical values across items)
- **B.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **C.** Apache Avro row-based binary format with JSON schema
- **D.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)

### 99. ForgeWorks' metallurgist wants to plot `FurnaceTempCelsius` (X-axis) against `TensileStrengthMPa` (Y-axis) across 2,000 alloy heats to inspect correlation and identify outlier batches. Which Power BI visual is ideal?

- **A.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)
- **B.** Page blobs in Azure Blob Storage
- **C.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)
- **D.** Treemap (or pie/donut chart for small category counts) showing part-to-whole proportions

### 100. On the factory lobby TV dashboard, plant leadership wants a single bold visual displaying today's `First Pass Yield (98.4%)`, daily trend sparkline, and green status against the `98.0%` plant target. Which Power BI visual fits best?

- **A.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **B.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)
- **C.** Apache Parquet columnar storage format
- **D.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)

---

## Answer Key and Explanations

### Question 1 — `C` (Describe core data concepts)

Correct answer: C (is correct). Uniform rows adhering to fixed, typed relational columns represent structured data. [Skill 1.1: Describe the features of structured data | Source: Explore core data concepts — Identify data formats (structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **B:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **C:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **D:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.

### Question 2 — `D` (Describe core data concepts)

Correct answer: D (is correct). Fixed tabular schemas with enforced column types and uniform records are structured data. [Skill 1.1: Describe the features of structured data | Source: Explore core data concepts — Identify data formats (structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **B:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **C:** Incorrect. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **D:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.

### Question 3 — `A, E` (Describe core data concepts)

Correct answers: A and E (are correct). Nested variable-field JSON documents represent semi-structured data, and Apache Avro pairs a JSON schema header with serialized binary records. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Correct. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **E:** Correct. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.

### Question 4 — `C` (Describe core data concepts)

Correct answer: C (is correct). Hierarchical self-describing XML and JSON documents without a rigid relational table grid are semi-structured data. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **B:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **C:** Correct. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **D:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.

### Question 5 — `C` (Describe core data concepts)

Correct answer: C (is correct). JSON represents hierarchical key-value objects and arrays natively across web and IoT APIs. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Correct. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 6 — `D` (Describe core data concepts)

Correct answer: D (is correct). Images, audio files, and videos lack a predefined tabular or key-tag structure and are unstructured data. [Skill 1.3: Describe the features of unstructured data | Source: Explore core data concepts — Identify data formats (unstructured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **B:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **C:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **D:** Correct. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.

### Question 7 — `D` (Describe core data concepts)

Correct answer: D (is correct). Scanned PDFs and JPEG photographs are raw binary blobs classified as unstructured data. [Skill 1.3: Describe the features of unstructured data | Source: Explore core data concepts — Identify data formats (unstructured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **B:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **C:** Incorrect. A composite key combines two or more columns (such as `OrderID` + `ProductID`) to uniquely identify rows in a junction or line-item table.
- **D:** Correct. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.

### Question 8 — `C, E` (Describe core data concepts)

Correct answers: C and E (are correct). Apache Parquet and ORC organize data in compressed columnar layouts optimized for selective analytical reads. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **C:** Correct. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **E:** Correct. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.

### Question 9 — `A` (Describe core data concepts)

Correct answer: A (is correct). Apache Avro combines compact binary row serialization with an embedded JSON schema supporting schema evolution across streaming pipelines. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Correct. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **D:** Incorrect. Bar and column charts use aligned bar lengths to compare magnitudes accurately across discrete categories such as product lines or regions.

### Question 10 — `C` (Describe core data concepts)

Correct answer: C (is correct). Plain-text rows separated by commas (or tabs) represent the delimited CSV/TSV file format. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **B:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **C:** Correct. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **D:** Incorrect. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.

### Question 11 — `C, E` (Describe core data concepts)

Correct answers: C and E (are correct). Column-family databases handle massive partitioned wide-column writes, and graph databases traverse multi-hop component dependency edges. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **B:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **C:** Correct. A column-family database groups related columns into families keyed by row and partition keys (such as Apache Cassandra or HBase) for massive write throughput.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **E:** Correct. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.

### Question 12 — `D` (Describe core data concepts)

Correct answer: D (is correct). Key-value databases map unique keys directly to values for fast point lookups and horizontal partitioning. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **B:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **C:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **D:** Correct. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.

### Question 13 — `B` (Describe core data concepts)

Correct answer: B (is correct). Document databases store and index self-contained JSON/BSON documents with flexible nested attributes. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **B:** Correct. A document database stores self-contained JSON/BSON documents indexed across nested attributes so each entity can evolve fields without schema migrations.
- **C:** Incorrect. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.
- **D:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.

### Question 14 — `A` (Describe core data concepts)

Correct answer: A (is correct). Live ACID ERP orders commit in Azure SQL Database, Data Factory extracts history into ADLS Gen2 / OneLake Parquet, and Power BI visuals query star schemas. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Correct. Operational transactions commit in an ACID relational store first, pipelines land history in columnar lake storage, and analytical models serve BI reports without taxing OLTP.
- **B:** Incorrect. Archive blobs are offline and unreadable for live OLTP writes, Power BI Desktop is an authoring tool rather than an OLTP engine, and Table storage is schemaless key-value.
- **C:** Incorrect. Paginated reports render formatted output rather than ingesting transactions, and Blob Cold tier does not execute multi-row ACID relational transactions.
- **D:** Incorrect. Power BI Service is a read-optimized BI platform rather than a transactional database, and Queue storage buffers small messages rather than archiving relational rows.

### Question 15 — `A` (Describe core data concepts)

Correct answer: A (is correct). Azure Data Lake Storage (ADLS) Gen2 adds hierarchical directory namespaces and POSIX ACLs atop Azure Blob Storage for big-data analytics. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Correct. ADLS Gen2 adds a true POSIX-ACL directory hierarchy and atomic folder rename/delete operations atop Azure Blob Storage for big-data analytics engines.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 16 — `D` (Describe core data concepts)

Correct answer: D (is correct). Azure Table storage provides low-cost schemaless key-value storage indexed by `PartitionKey` and `RowKey`. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Incorrect. Azure Queue storage holds small asynchronous work messages (up to 64 KB per message), not multi-gigabyte binary files.
- **B:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **C:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **D:** Correct. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 17 — `B, C, D` (Describe core data concepts)

Correct answers: B, C, and D (are correct). Live barcode inventory updates are an OLTP workload relying on ACID Isolation (concurrent scan safety) and Durability (crash persistence). [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **B:** Correct. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **C:** Correct. Isolation prevents concurrent in-flight transactions from reading uncommitted intermediate edits or overwriting each other unpredictably via locking or row versioning.
- **D:** Correct. Durability guarantees that once a transaction commits, its changes are persisted to non-volatile transaction logs/storage and survive power loss or crash recovery.
- **E:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **F:** Incorrect. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.

### Question 18 — `C` (Describe core data concepts)

Correct answer: C (is correct). Atomicity ensures all statements inside a transaction succeed together or roll back completely as one unit. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **B:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **C:** Correct. Atomicity guarantees that every statement in a transaction either succeeds together or rolls back completely if any step fails, preventing half-completed transfers.
- **D:** Incorrect. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.

### Question 19 — `D` (Describe core data concepts)

Correct answer: D (is correct). Consistency guarantees every transaction brings the database from one valid constraint-satisfying state to another. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.
- **B:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.
- **C:** Incorrect. Denormalized historical scans belong in an OLAP store; live checkout requires normalized OLTP tables with ACID guarantees to prevent lost or corrupted orders.
- **D:** Correct. Consistency ensures a transaction transitions the database only from one valid rule-compliant state (keys, check constraints, types) to another.

### Question 20 — `C, E` (Describe core data concepts)

Correct answers: C and E (are correct). Multi-year historical aggregation is an OLAP workload, and a central numeric fact table surrounded by flat dimensions is a star schema. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Correct. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **D:** Incorrect. Atomicity guarantees that every statement in a transaction either succeeds together or rolls back completely if any step fails, preventing half-completed transfers.
- **E:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.

### Question 21 — `B` (Describe core data concepts)

Correct answer: B (is correct). Separating read-heavy OLAP analytical scans from live OLTP MES databases prevents lock contention and protects shop-floor latency. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **B:** Correct. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **C:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.

### Question 22 — `A` (Describe core data concepts)

Correct answer: A (is correct). Normalizing dimension hierarchies into multiple linked sub-dimension tables creates a snowflake schema. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Correct. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **D:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).

### Question 23 — `A` (Describe core data concepts)

Correct answer: A (is correct). Operational database security, HA/DR replication, backup recovery, and query/index tuning are core DBA responsibilities. [Skill 1.9: Describe responsibilities for database administrators | Source: Explore data roles and services — Database administrator responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Correct. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **B:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **C:** Incorrect. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.
- **D:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.

### Question 24 — `C` (Describe core data concepts)

Correct answer: C (is correct). Monitoring live database engine health, lock contention, and index maintenance belongs to the database administrator (DBA). [Skill 1.9: Describe responsibilities for database administrators | Source: Explore data roles and services — Database administrator responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **B:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **C:** Correct. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 25 — `D` (Describe core data concepts)

Correct answer: D (is correct). The DBA governs operational SQL, the data engineer builds ELT pipelines and curates Gold star tables, and the data analyst authors DAX KPIs and Power BI visuals. [Skill 1.10: Describe responsibilities for data engineers | Source: Explore data roles and services — Data engineer responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. Cluster HA belongs to the DBA, Spark ELT pipelines belong to the data engineer, and visual storytelling/app distribution belongs to the data analyst.
- **B:** Incorrect. Operational DB security and PITR restores are DBA duties, network/pipeline plumbing belongs to infra/data engineering, and analysts focus on semantic models and visuals.
- **C:** Incorrect. KPI scorecards and sales packs are data analyst outputs, whereas Spark streaming pipelines belong to data engineers and OLTP index maintenance belongs to DBAs.
- **D:** Correct. DBAs govern operational database engines, data engineers build ingestion/transformation pipelines into curated analytical stores, and data analysts model KPIs and visual reports.

### Question 26 — `D` (Describe core data concepts)

Correct answer: D (is correct). Building data ingestion, unit standardization, and lakehouse transformation pipelines is the role of the data engineer. [Skill 1.10: Describe responsibilities for data engineers | Source: Explore data roles and services — Data engineer responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **B:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **C:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **D:** Correct. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.

### Question 27 — `B` (Describe core data concepts)

Correct answer: B (is correct). Data analysts build business DAX measures, semantic models, and interactive Power BI reports for stakeholders. [Skill 1.11: Describe responsibilities for data analysts | Source: Explore data roles and services — Data analyst responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. Azure Migrate discovers on-premises SQL Server instances, evaluates feature compatibility blockers, and recommends right-sized Azure SQL targets (replacing retired DMA).
- **B:** Correct. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **C:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **D:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.

### Question 28 — `A` (Describe core data concepts)

Correct answer: A (is correct). Exploring curated data and authoring visual KPI reports for decision-makers defines the data analyst role. [Skill 1.11: Describe responsibilities for data analysts | Source: Explore data roles and services — Data analyst responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Correct. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **B:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.

### Question 29 — `C, D` (Identify considerations for relational data on Azure)

Correct answers: C and D (are correct). `(WorkOrderID, PartID)` is a composite key, and `PartID` referencing `Parts.PartID` is a foreign key. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **C:** Correct. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.
- **D:** Correct. A composite key combines two or more columns (such as `OrderID` + `ProductID`) to uniquely identify rows in a junction or line-item table.
- **E:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).

### Question 30 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). A primary key constraint guarantees uniqueness and `NOT NULL` across every row of a relational table. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **B:** Incorrect. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.
- **C:** Correct. A primary key uniquely identifies each row in a relational table and implicitly forbids `NULL` and duplicate key values.
- **D:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.

### Question 31 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). A foreign key constraint enforces referential integrity inside the relational database engine. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Correct. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.
- **D:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.

### Question 32 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Relational tables store structured data where every value in a column conforms to the column's declared data type. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **B:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **C:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **D:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.

### Question 33 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). 1NF enforces atomic cells and a primary key, 2NF extracts partial composite-key dependencies, and 3NF removes transitive non-key dependencies. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Correct. Normalization progresses sequentially: 1NF enforces atomic values and row uniqueness, 2NF removes partial dependencies on composite keys, and 3NF eliminates transitive non-key dependencies.
- **B:** Incorrect. Foreign keys require atomic primary keys first, and 1NF eliminates repeating groups rather than creating them.
- **C:** Incorrect. Copying supplier attributes into invoice items creates transitive redundancy, and pipe-delimited multi-value strings violate 1NF.
- **D:** Incorrect. You cannot achieve 3NF before 1NF/2NF, comma-separated lists violate 1NF atomicity, and duplicating addresses reintroduces update anomalies.

### Question 34 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Eliminating repeating column groups and multi-valued cells brings a table into First Normal Form (1NF). [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Correct. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **B:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **C:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **D:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.

### Question 35 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Second Normal Form (2NF) removes partial dependencies where non-key columns depend on only part of a composite primary key. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **C:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **D:** Correct. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.

### Question 36 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Third Normal Form (3NF) removes transitive dependencies between non-key attributes. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Correct. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.
- **C:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **D:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.

### Question 37 — `A, B, C` (Identify considerations for relational data on Azure)

Correct answers: A, B, and C (are correct). `CREATE INDEX` is DDL, `DELETE` is DML, and `DENY` is DCL. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Correct. DML statements query, add, modify, or delete row data stored inside relational tables.
- **B:** Correct. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **C:** Correct. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **E:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **F:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.

### Question 38 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). A `LEFT OUTER JOIN` returns every row from the left `Machines` table and `NULL` where no matching `DowntimeEvents` row exists. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. Granting and revoking security permissions belongs to DCL (`GRANT`, `REVOKE`, `DENY`), not DML.
- **B:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **C:** Correct. `LEFT OUTER JOIN` keeps every row from the left table (for example, all customers) and fills `NULL` for right-table columns when no related order exists.
- **D:** Incorrect. `INNER JOIN` returns only row pairs whose join predicate matches in both the left and right tables, excluding unmatched rows.

### Question 39 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Row-level `Shift = 'Day'` filtering before aggregation belongs in `WHERE`, while post-grouping `SUM(Units) > 5000` belongs in `HAVING`. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Correct. `WHERE` predicates evaluate individual source rows prior to aggregation, whereas `HAVING` filters grouped summary results such as `HAVING COUNT(*) > 5`.
- **B:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **C:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Incorrect. SQL `WHERE` evaluates individual pre-grouped rows and rejects aggregate functions; group-level aggregate filters belong in the `HAVING` clause.

### Question 40 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Altering table column definitions modifies database schema metadata and belongs to Data Definition Language (DDL). [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. DML statements query, add, modify, or delete row data stored inside relational tables.
- **B:** Correct. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **C:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Incorrect. Granting and revoking security permissions belongs to DCL (`GRANT`, `REVOKE`, `DENY`), not DML.

### Question 41 — `B, D` (Identify considerations for relational data on Azure)

Correct answers: B and D (are correct). Each table supports one clustered index for physical row order and multiple nonclustered indexes for secondary search keys. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Correct. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **C:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **D:** Correct. A nonclustered index maintains a separate sorted key structure pointing back to the base table rows, accelerating selective lookups on non-primary search columns.
- **E:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.

### Question 42 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). A standard view stores only the `SELECT` query metadata and exposes a virtual table over the underlying base tables. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Correct. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **C:** Incorrect. Because a clustered index dictates the single physical leaf-level storage order of the table’s rows, a table can have at most one clustered index (plus multiple nonclustered indexes).
- **D:** Incorrect. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.

### Question 43 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). A stored procedure is a named, parameterized routine of SQL statements stored and executed inside the database engine. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Correct. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.
- **B:** Incorrect. A nonclustered index maintains a separate sorted key structure pointing back to the base table rows, accelerating selective lookups on non-primary search columns.
- **C:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **D:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.

### Question 44 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Without a nonclustered index on `SerialNumber`, the engine would scan `ManufactureDate`-ordered pages; the nonclustered B-tree jumps straight to the matching row locator. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. Because a clustered index dictates the single physical leaf-level storage order of the table’s rows, a table can have at most one clustered index (plus multiple nonclustered indexes).
- **C:** Correct. A nonclustered index maintains a separate sorted key structure pointing back to the base table rows, accelerating selective lookups on non-primary search columns.
- **D:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.

### Question 45 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Assess compatibility and SKU sizing in Azure Migrate, choose Azure SQL Database or Managed Instance, provision with Entra/TLS security, and migrate data before cutover. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Azure Table storage cannot mount `.mdf` database files, and single Azure SQL Database does not host SQL Server Agent or cross-database instance queries.
- **B:** Correct. Azure Migrate discovers workloads, flags compatibility blockers, and recommends right-sized Azure SQL targets before secure provisioning, data sync, and connection cutover.
- **C:** Incorrect. Queue storage is not a relational migration vehicle, SQL Managed Instance requires VNet subnet sizing upfront, and removing primary keys corrupts relational integrity.
- **D:** Incorrect. Cutting over before data migration breaks production, opening all public IPs violates security, and assessments must run before selecting the target SKU.

### Question 46 — `A, C` (Identify considerations for relational data on Azure)

Correct answers: A and C (are correct). Azure SQL Database Serverless auto-pauses idle single databases, and Azure SQL Managed Instance provides PaaS SQL Agent and cross-database compatibility. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Correct. The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.
- **B:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **C:** Correct. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **E:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 47 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). SQL Server on Azure Virtual Machines (IaaS) gives full control over Windows Server, exact SQL builds, and co-located host services. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **B:** Incorrect. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **C:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **D:** Correct. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.

### Question 48 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). An Azure SQL Database Elastic Pool shares compute capacity across many databases with non-overlapping usage spikes. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Single Azure SQL Database is database-scoped and does not include SQL Server Agent or cross-database instance queries; those require SQL Managed Instance or SQL Server on Azure VMs.
- **B:** Correct. An Elastic Pool shares a pool of compute resources across multiple single databases that have unpredictable, staggered usage spikes to optimize cost.
- **C:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 49 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Azure Migrate provides SQL Server discovery, readiness assessments, and cloud SKU right-sizing (replacing retired DMA). [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Correct. Azure Migrate discovers on-premises SQL Server instances, evaluates feature compatibility blockers, and recommends right-sized Azure SQL targets (replacing retired DMA).
- **B:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **C:** Incorrect. Microsoft retired Data Migration Assistant (DMA) in July 2025; Azure Migrate and the Azure SQL Migration extension handle SQL discovery, assessment, and right-sizing.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 50 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Azure Database for PostgreSQL — Flexible Server delivers managed PaaS PostgreSQL with custom types, extensions, `PL/pgSQL`, and HA. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Incorrect. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.
- **B:** Correct. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **C:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 51 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Azure Database for MySQL — Flexible Server provides managed MySQL Community Edition PaaS with automated backups and up to 35-day PITR. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Incorrect. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **B:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **C:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **D:** Correct. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.

### Question 52 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Azure Database for PostgreSQL — Flexible Server stores Query Store metrics in the `azure_sys` database (`query_store.qs_view`). [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **C:** Incorrect. Single Azure SQL Database is database-scoped and does not include SQL Server Agent or cross-database instance queries; those require SQL Managed Instance or SQL Server on Azure VMs.
- **D:** Correct. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.

### Question 53 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Lifecycle management transitions blobs from Hot -> Cool (>=30d) -> Cold (>=90d) -> offline Archive (>=180d, rehydrating when audited). [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Table storage entities hold small key-value properties rather than large video files, and Cool/Cold tiers remain online with immediate millisecond read access.
- **B:** Incorrect. Blob tiers are object storage rather than SMB shares, Archive rather than Hot minimizes 1-year retention storage cost, and Hot blobs require no rehydration.
- **C:** Correct. Lifecycle management policies automatically age blobs from lowest-read-cost Hot through Cool and Cold down to lowest-storage-cost offline Archive.
- **D:** Incorrect. Archive tier is offline and cannot serve direct reads until rehydrated to Hot or Cool, which takes hours.

### Question 54 — `B, C` (Describe considerations for working with non-relational data on Azure)

Correct answers: B and C (are correct). ADLS Gen2 provides the Hierarchical Namespace for Spark analytics, and the Cold tier provides 90-day minimum online low-cost storage. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **B:** Correct. ADLS Gen2 adds a true POSIX-ACL directory hierarchy and atomic folder rename/delete operations atop Azure Blob Storage for big-data analytics engines.
- **C:** Correct. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **E:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 55 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Page blobs support random 512-byte page read/write operations up to 8 TiB for VM disks. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Correct. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.
- **C:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 56 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Append blobs optimize appending new blocks solely at the end of the blob for logging workloads. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Correct. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Incorrect. Archive tier blobs are stored offline and cannot be read directly until rehydrated to Hot or Cool, which takes hours.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.

### Question 57 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Archive tier blobs are offline and unreadable until rehydrated for hours to Hot or Cool; Archive is strictly for >=180-day cold retention. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.
- **B:** Incorrect. Archive tier blobs are stored offline and cannot be read directly until rehydrated to Hot or Cool, which takes hours.
- **C:** Incorrect. The Hot tier is online storage optimized for data that is accessed or modified frequently, carrying the lowest transaction/read cost.
- **D:** Correct. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 58 — `B, E` (Describe considerations for working with non-relational data on Azure)

Correct answers: B and E (are correct). Azure Files provides managed SMB 3.0 and NFS 4.1 cloud shares, and Azure File Sync caches/tiers Windows Server folders with Azure Files. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **B:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **E:** Correct. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.

### Question 59 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Files exposes managed SMB 3.0 cloud shares accessible via standard UNC paths and Windows drive mappings. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.

### Question 60 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Azure File Sync's cloud tiering frees local Windows Server disk space while streaming tiered files seamlessly from Azure Files on open. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **B:** Incorrect. Spark Structured Streaming treats a live event stream as an unbounded table processed via familiar Spark SQL/DataFrame APIs with checkpointed exactly-once guarantees.
- **C:** Incorrect. ADLS Gen2 adds a true POSIX-ACL directory hierarchy and atomic folder rename/delete operations atop Azure Blob Storage for big-data analytics engines.
- **D:** Correct. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.

### Question 61 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Azure Table storage stores schemaless key-value property bags indexed by composite `PartitionKey` + `RowKey`. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. Azure Table storage is a schemaless key-value store indexed only by `PartitionKey` and `RowKey` with no foreign keys or server-side table joins.
- **B:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **C:** Correct. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 62 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Azure Cosmos DB for Table keeps the Table SDK `PartitionKey`/`RowKey` model while adding multi-region writes, secondary indexes, and <10 ms SLAs. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Correct. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **D:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.

### Question 63 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). In Azure Table storage, `PartitionKey` controls scale-out partition placement and `RowKey` uniquely identifies and sorts each entity within that partition. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **B:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **C:** Correct. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. Azure Table storage is a schemaless key-value store indexed only by `PartitionKey` and `RowKey` with no foreign keys or server-side table joins.

### Question 64 — `D, E` (Describe considerations for working with non-relational data on Azure)

Correct answers: D and E (are correct). Cosmos DB provides turnkey multi-region global distribution, and Strong consistency guarantees linearizable reads of the latest committed write. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **B:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **C:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **D:** Correct. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **E:** Correct. Azure Cosmos DB replicates data transparently across selected Azure regions with financially backed 99.999% availability and single-digit millisecond read/write latency.

### Question 65 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Cosmos DB provisions and autoscales throughput in Request Units per second (`RU/s`). [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.
- **B:** Correct. Cosmos DB measures CPU, memory, and IOPS per database operation in Request Units (RUs), billed via Provisioned/Autoscale RU/s or consumption-based Serverless.
- **C:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 66 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Session consistency is Cosmos DB's default level, guaranteeing monotonic read-your-own-writes per client session. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.
- **B:** Correct. Session consistency is Cosmos DB’s default level, balancing low latency and throughput while guaranteeing each user session immediately sees its own writes in order.
- **C:** Incorrect. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **D:** Incorrect. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.

### Question 67 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Eventual consistency provides the lowest RU cost and read/write latency when temporary replica convergence lag is acceptable. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Correct. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.
- **B:** Incorrect. Atomicity guarantees that every statement in a transaction either succeeds together or rolls back completely if any step fails, preventing half-completed transfers.
- **C:** Incorrect. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **D:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.

### Question 68 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Choose the API at account creation, create the database and `/machineId` container, set RU/s or serverless + consistency, and execute partition-scoped queries. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB is fully managed PaaS with no OS patching, a single-value partition key creates a 20 GB logical-partition bottleneck, and triggers/sprocs use JavaScript rather than T-SQL.
- **B:** Incorrect. Every Cosmos DB container requires a partition key, the API is fixed per account, Cosmos DB does not enforce cross-container foreign keys, and item size is capped at 2 MB.
- **C:** Correct. API selection happens at account creation, partition key design happens at container creation to distribute storage/RU evenly, and partition-scoped queries avoid cross-partition fan-out.
- **D:** Incorrect. Cosmos DB sits under an account -> database -> container -> item hierarchy, not SMB shares or subscription tags.

### Question 69 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Azure Cosmos DB for Apache Cassandra provides wire-compatible managed hosting for CQL wide-column workloads. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **B:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Correct. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.

### Question 70 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Cosmos DB for Apache Gremlin models vertices and edges queried via Gremlin graph traversals. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB for MongoDB lets existing MongoDB drivers and tools store BSON documents in Cosmos DB simply by updating the connection string.
- **B:** Correct. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **C:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **D:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.

### Question 71 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Azure Cosmos DB for NoSQL is the native JSON document API supporting rich SQL query functions like `ARRAY_CONTAINS`. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **B:** Incorrect. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **C:** Correct. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **D:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.

### Question 72 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Cosmos DB for MongoDB supports the MongoDB wire protocol for BSON document applications. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **B:** Correct. Cosmos DB for MongoDB lets existing MongoDB drivers and tools store BSON documents in Cosmos DB simply by updating the connection string.
- **C:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 73 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Data Factory lands raw files into OneLake Bronze, Spark/SQL cleanses Silver Delta tables, and curated Gold star schemas serve BI. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Correct. Modern ELT lands raw data in scalable lake storage first, then leverages cloud compute to cleanse Silver tables and publish Gold star schemas for analytics.
- **B:** Incorrect. Skipping cleansing degrades report accuracy, deleting raw Bronze files prevents replayability, and Gold analytical layers favor denormalized star schemas over 3NF.
- **C:** Incorrect. Analytical ingestion is read-only against operational sources and builds Bronze -> Silver -> Gold sequentially.
- **D:** Incorrect. ELT executes transformations in scalable cloud engines rather than client laptops, and Archive blobs/Queues cannot back live BI queries.

### Question 74 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Azure Data Factory / Fabric Data Factory provides Copy pipelines, Integration Runtimes, and Dataflows Gen2 orchestration. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Correct. Data Factory orchestrates code-free data movement (90+ connectors via Copy activity) and visual Power Query transformations (Dataflows Gen2) or Spark/Mapping Data Flows.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 75 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Transforming and redacting sensitive attributes before loading the target analytical store follows the ETL pattern. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Correct. ETL transforms, scrubs, or redacts sensitive fields in an intermediate processing engine prior to loading only the conformed structure into the target analytical store.
- **C:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.
- **D:** Incorrect. ELT extracts raw source data, loads it directly into scalable lake/warehouse storage, and runs distributed cloud compute (Spark or SQL) to cleanse and model in place.

### Question 76 — `B, E` (Describe an analytics workload on Azure)

Correct answers: B and E (are correct). Delta Lake ACID tables on open Parquet implement a data lakehouse, and normalized sub-dimension chains implement a snowflake schema. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **B:** Correct. A lakehouse combines the low-cost open file flexibility of a data lake with ACID transactions, schema enforcement, and SQL warehouse performance via Delta Lake tables.
- **C:** Incorrect. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **E:** Correct. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.

### Question 77 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). A central numeric fact table joined directly to single-hop denormalized dimension tables is a star schema. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **B:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **C:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 78 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Delta Lake adds ACID transactions, schema enforcement, and versioned time travel over open columnar Parquet files so both Spark and T-SQL engines share one copy. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Correct. A lakehouse combines the low-cost open file flexibility of a data lake with ACID transactions, schema enforcement, and SQL warehouse performance via Delta Lake tables.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.

### Question 79 — `B, C, D` (Describe an analytics workload on Azure)

Correct answers: B, C, and D (are correct). Microsoft Fabric, Azure Databricks, and Azure Synapse Analytics are Microsoft's primary cloud platforms for large-scale analytics. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Correct. Azure Synapse Analytics integrates serverless SQL on-demand lake querying, dedicated MPP SQL warehousing, Apache Spark pools, and Synapse Pipelines in Synapse Studio.
- **C:** Correct. Microsoft Fabric unifies Data Factory, Data Engineering, Data Warehouse, Data Science, Real-Time Intelligence, and Power BI in one SaaS workspace sharing OneLake Delta tables.
- **D:** Correct. Azure Databricks provides managed Apache Spark clusters, collaborative Python/SQL/Scala/R notebooks, Unity Catalog governance, and Delta Lake processing on Azure.
- **E:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **F:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 80 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Microsoft Fabric stores both Warehouse and Lakehouse tables natively as Delta Parquet in OneLake, enabling zero-copy cross-item SQL queries. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Correct. Microsoft Fabric unifies Data Factory, Data Engineering, Data Warehouse, Data Science, Real-Time Intelligence, and Power BI in one SaaS workspace sharing OneLake Delta tables.
- **C:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **D:** Incorrect. Azure HDInsight provisions managed clusters of open-source Apache big-data frameworks when lift-and-shift Hadoop/Hive/HBase/Kafka compatibility is required.

### Question 81 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Azure Databricks provides collaborative Apache Spark clusters, Delta Live Tables, Unity Catalog, and MLflow for big-data engineering and ML. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **B:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Correct. Azure Databricks provides managed Apache Spark clusters, collaborative Python/SQL/Scala/R notebooks, Unity Catalog governance, and Delta Lake processing on Azure.
- **D:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.

### Question 82 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Azure HDInsight provides managed cloud clusters for open-source Hadoop, Hive, HBase, Kafka, and Spark workloads. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.
- **B:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **C:** Correct. Azure HDInsight provisions managed clusters of open-source Apache big-data frameworks when lift-and-shift Hadoop/Hive/HBase/Kafka compatibility is required.
- **D:** Incorrect. The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.

### Question 83 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). A sliding window evaluates a rolling fixed lookback duration specifically when events enter or exit the window. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.
- **B:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **C:** Correct. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **D:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.

### Question 84 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). A tumbling window divides time into contiguous, fixed-size, non-overlapping intervals where each event belongs to exactly one window. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **B:** Correct. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **C:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **D:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.

### Question 85 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Processing accumulated bounded datasets on a recurring schedule is batch processing. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **B:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.
- **C:** Incorrect. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **D:** Correct. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.

### Question 86 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Analyzing unbounded events continuously in motion for immediate action is stream processing. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **B:** Correct. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.
- **C:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **D:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.

### Question 87 — `C, D` (Describe an analytics workload on Azure)

Correct answers: C and D (are correct). Engine A is Microsoft Fabric Real-Time Intelligence, and Engine B is Azure Stream Analytics. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **B:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Correct. Fabric Real-Time Intelligence ingests and routes events via Eventstream, indexes high-volume telemetry in Eventhouse KQL databases, visualizes live tiles, and triggers Activator alerts.
- **D:** Correct. Azure Stream Analytics runs declarative Stream Analytics Query Language (`SELECT ... GROUP BY TumblingWindow(...)`) jobs joining live streams with reference data into sinks.
- **E:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 88 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Fabric Real-Time Intelligence unites Eventstream ingestion, Eventhouse KQL log analytics, Real-Time Dashboards, and Activator alerts for factory telemetry. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **B:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.
- **C:** Correct. Fabric Real-Time Intelligence ingests and routes events via Eventstream, indexes high-volume telemetry in Eventhouse KQL databases, visualizes live tiles, and triggers Activator alerts.
- **D:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.

### Question 89 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Azure Event Hubs is Azure's high-throughput partitioned event streaming broker with native AMQP and Kafka endpoints. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Correct. Azure Event Hubs ingests millions of telemetry events per second into partitioned append logs (supporting native AMQP/HTTPS and Apache Kafka producers) for downstream stream consumers.

### Question 90 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Apache Spark Structured Streaming processes continuous streams via `readStream`/`writeStream` DataFrame APIs and checkpoints. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.
- **B:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **C:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **D:** Correct. Spark Structured Streaming treats a live event stream as an unbounded table processed via familiar Spark SQL/DataFrame APIs with checkpointed exactly-once guarantees.

### Question 91 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Shape/model and build reports in Power BI Desktop, publish to a Power BI Service workspace, pin dashboard tiles and schedule refresh in the Service, and share a Power BI App. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Incorrect. Dashboards exist only in Power BI Service (not Power BI Desktop), Power BI Mobile is for consumption, and viewers consume shared Apps/reports in browser or mobile.
- **B:** Incorrect. Dashboards are created in Power BI Service rather than Power BI Mobile, and dataset refresh plus secure sharing are managed in Power BI Service workspaces.
- **C:** Incorrect. Paginated `.rdl` reports are authored in Power BI Report Builder, Stream Analytics processes event streams, and port `1433` is SQL Server TDS rather than BI sharing.
- **D:** Correct. Power BI Desktop handles Power Query prep, semantic modeling, and report design, while Power BI Service hosts scheduled refresh, multi-report dashboards, and governed App distribution.

### Question 92 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Power BI Desktop combines Power Query Editor, semantic Model view, DAX authoring, and interactive `.pbix` report creation. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Incorrect. Power BI Service (`app.powerbi.com` / Fabric) hosts published semantic models and reports, pins cross-report dashboard tiles, schedules gateway refreshes, and distributes governed Apps.
- **B:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Incorrect. Dashboards with pinned tiles across multiple reports are a cloud-only feature of Power BI Service, not Power BI Desktop.
- **D:** Correct. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.

### Question 93 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Power BI Report Builder authors fixed-layout paginated (`.rdl`) reports built for multi-page PDF export and printing. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Incorrect. Power BI Service (`app.powerbi.com` / Fabric) hosts published semantic models and reports, pins cross-report dashboard tiles, schedules gateway refreshes, and distributes governed Apps.
- **B:** Correct. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Incorrect. Azure Event Hubs ingests millions of telemetry events per second into partitioned append logs (supporting native AMQP/HTTPS and Apache Kafka producers) for downstream stream consumers.
- **D:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.

### Question 94 — `A, B` (Describe an analytics workload on Azure)

Correct answers: A and B (are correct). Relationships and drill-down hierarchies belong to the Power BI semantic model, while `Scrap %` is a dynamic DAX measure. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Correct. A Power BI semantic model defines `1:*` star-schema relationships, reusable DAX measures, drill-down hierarchies, and column metadata consumed across reports.
- **B:** Correct. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **E:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 95 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). A DAX measure computes weighted numerator/denominator aggregations dynamically inside whatever filter context the user selects. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **B:** Correct. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **C:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 96 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Field visibility, formatting, hierarchies, and relationships are managed in the Power BI semantic model. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Correct. A Power BI semantic model defines `1:*` star-schema relationships, reusable DAX measures, drill-down hierarchies, and column metadata consumed across reports.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **D:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).

### Question 97 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Power BI semantic models are optimized for star schemas separating dimension lookup tables from numeric fact tables. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **C:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **D:** Incorrect. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.

### Question 98 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). A bar or column chart clearly compares ranked magnitudes across discrete categories. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Correct. Bar and column charts use aligned bar lengths to compare magnitudes accurately across discrete categories such as product lines or regions.
- **B:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **C:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **D:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.

### Question 99 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). A scatter chart plots two numeric variables on X and Y axes to expose correlation, clusters, and outliers. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Correct. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Incorrect. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.
- **D:** Incorrect. Pie/donut charts show part-to-whole shares for a few slices, while treemaps use nested rectangles to display proportional composition across larger hierarchical categories.

### Question 100 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). A KPI visual displays a primary metric alongside its trend line and variance against a target goal. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **B:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
- **C:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **D:** Correct. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.
