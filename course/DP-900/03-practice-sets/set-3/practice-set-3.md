# Microsoft Exam DP-900: Microsoft Azure Data Fundamentals — Full-Length Mock Exam 3

**Theme:** Smart City Transit & Municipal Services — SQL Joins/Views, PostgreSQL Flexible Server, Azure Files, Stream Windows & Maps  
**Credential:** `Microsoft Certified: Azure Data Fundamentals` *(Beginner / Fundamentals · **no prerequisite** · **never expires**)*  
**Study guide baseline:** `July 21, 2026` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `75 minutes` (`45 sec/question`, matching live 45-minute / 60-question pace; `45 minutes` optional speed drill · **closed-book**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn documentation — not affiliated with or endorsed by Microsoft Corporation. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Describe core data concepts (25–30% official weight · 28 questions)

### 1. MetroPulse Transit stores municipal bus fare schedules in a SQL table with typed `RouteNumber`, `ZoneCode`, `PeakFareDecimal`, and `EffectiveDate` columns across every row. Which data representation is this?

- **A.** Semi-structured data
- **B.** Apache Avro row-based binary format with JSON schema
- **C.** Unstructured data
- **D.** Structured data

### 2. City property-tax assessors record parcel IDs, assessed valuations, and square footage inside fixed tabular columns governed by integer and numeric database types. How is this dataset classified?

- **A.** Structured data
- **B.** Graph database (vertices and directed edges)
- **C.** Unstructured data
- **D.** JavaScript Object Notation (JSON) document format

### 3. Smart traffic-signal controllers emit status messages where pedestrian crosswalk nodes include `pushButtonCount` arrays while highway ramp meters include `queueSensorMeters` keys inside nested `{}` objects. Which two items describe these messages? Select two.

- **A.** Unstructured data
- **B.** Semi-structured data
- **C.** Page blobs in Azure Blob Storage
- **D.** Structured data
- **E.** JavaScript Object Notation (JSON) document format

### 4. Public-works 311 APIs exchange service requests using hierarchical key-value tags where tree-trimming tickets carry optional `canopyHeight` tags and pothole tickets carry `laneNumber` tags without a fixed column matrix. This payload style is ____.

- **A.** Unstructured data
- **B.** Structured data
- **C.** Semi-structured data
- **D.** Clustered index (defines physical leaf-level sort order; maximum one per table)

### 5. MetroPulse's real-time bus arrival REST feed publishes nested `route`, `vehicle`, and `stopPredictions[]` arrays directly to commuter smartphone apps. Which standard text format represents these nested objects and arrays?

- **A.** JavaScript Object Notation (JSON) document format
- **B.** Page blobs in Azure Blob Storage
- **C.** Delimited text format (CSV or TSV)
- **D.** Second Normal Form (2NF — full functional dependency on the entire composite key)

### 6. Transit safety teams retain dashcam `.mp4` incident clips, dispatch radio `.ogg` audio logs, and bridge inspection drone `.jpg` photos in cloud storage. Together, these files are ____.

- **A.** Unstructured data
- **B.** Structured data
- **C.** Apache Parquet columnar storage format
- **D.** Semi-structured data

### 7. Historic city council meeting `.pdf` scans and public-hearing `.wav` recordings are archived in an Azure Blob container. Which data category describes these binary assets?

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Composite key (multi-column key)
- **C.** Structured data
- **D.** Unstructured data

### 8. MetroPulse's data lake uses two binary file formats: Format 1 is row-oriented with a JSON header ideal for high-speed bus GPS event streaming; Format 2 is columnar with predicate pushdown ideal for scanning 3 columns across 8 billion historical ridership rows. Which two formats are Format 1 and Format 2? Select two.

- **A.** Apache Avro row-based binary format with JSON schema
- **B.** Apache Parquet columnar storage format
- **C.** Page blobs in Azure Blob Storage
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **E.** Clustered index (defines physical leaf-level sort order; maximum one per table)

### 9. A city clerk exports a 1,200-row bicycle-rack inventory where values on each line are separated by commas and opened directly in spreadsheet software with zero binary encoding. Which file format was exported?

- **A.** Apache Avro row-based binary format with JSON schema
- **B.** Apache Parquet columnar storage format
- **C.** Delimited text format (CSV or TSV)
- **D.** Optimized Row Columnar (ORC) stripe format

### 10. A regional transportation authority runs Hive batch queries over multi-terabyte toll histories stored in compressed columnar stripes with embedded min/max stripe indexes. Which file format is described?

- **A.** Delimited text format (CSV or TSV)
- **B.** Append blobs in Azure Blob Storage
- **C.** JavaScript Object Notation (JSON) document format
- **D.** Optimized Row Columnar (ORC) stripe format

### 11. MetroPulse evaluates two non-relational models: one modeling subway stations as vertices and rail segments as weighted transfer edges to compute shortest multi-line routes, and another looking up active transit-card balances purely by `CardUID`. Which two database types fit? Select two.

- **A.** Key-value non-relational store
- **B.** Graph database (vertices and directed edges)
- **C.** Delimited text format (CSV or TSV)
- **D.** Database view (saved virtual `SELECT` query)
- **E.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

### 12. City building-permit applications vary widely between solar-panel installs, food trucks, and high-rise cranes, so IT stores each application as an indexed self-contained JSON document. Which database category is this?

- **A.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **B.** Delimited text format (CSV or TSV)
- **C.** Document database
- **D.** Line chart (tracking continuous trends and changes over ordered time intervals)

### 13. Roadway weather stations stream millones of pavement temperature, salinity, and wind-gust measurements grouped into wide column families keyed by `SensorCorridor` and timestamp. Which non-relational store category matches?

- **A.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **B.** Column-family (wide-column) database
- **C.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **D.** Database view (saved virtual `SELECT` query)

### 14. MetroPulse wants an Azure reference flow from live fare-gate tap deductions through multi-year ridership dashboards for city planners. Which four-step Azure service sequence fits best?

- **A.** Serve live checkout writes in Power BI Service → Export dashboards to CSV → Load CSVs into Azure SQL Database → Archive active rows to Azure Queue storage
- **B.** Land raw checkout clicks in Paginated Reports → Transform via SMB file locks → Commit ACID transactions in Azure Blob Cold tier → Query via Gremlin graph vertices
- **C.** Capture OLTP writes directly in Archive Blob tier → Run live checkout queries in Power BI Desktop → Copy rows to Azure Files SMB → Normalize into Azure Table storage
- **D.** Capture OLTP writes in Azure SQL Database → Extract changes via Data Factory pipeline → Land Parquet files in ADLS Gen2 / OneLake → Serve star-schema visuals in Power BI

### 15. Proposed solution: A municipal engineer proposes storing 20 GB CAD bridge blueprints inside Azure Queue storage messages; the lead architect rejects this and stores the blueprints in ____ instead. What completes the correction?

- **A.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **B.** Store 20 GB CAD engineering drawings inside single Azure Queue storage messages
- **C.** Block blobs in Azure Blob Storage
- **D.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)

### 16. City GIS developers need a managed PaaS relational database supporting open-source spatial polygon geometry queries (`PostGIS`) and `PL/pgSQL` routines for zoning maps. Which Azure service fits?

- **A.** Azure Database for PostgreSQL — Flexible Server
- **B.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **C.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 17. When a commuter taps a smart transit card at a turnstile, deducting `$2.75` and logging the gate entry must succeed or fail together, card balance rules (`Balance >= 0`) must hold, and two simultaneous taps cannot read an uncommitted mid-update balance. Which three ACID properties are described? Select three.

- **A.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **B.** Consistency (valid schema and constraint state)
- **C.** Online Analytical Processing (OLAP) workload
- **D.** Isolation (concurrent transactions do not interfere)
- **E.** Cold access tier (online, 90-day minimum retention for rarely accessed data)
- **F.** Atomicity (all-or-nothing transaction unit)

### 18. Parking-meter payment APIs process thousands of concurrent 1-second session starts, extensions, and receipts per minute against normalized operational tables. This workload is an ____.

- **A.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **B.** Online Analytical Processing (OLAP) workload
- **C.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **D.** Online Transaction Processing (OLTP) workload

### 19. Once a resident receives confirmation receipt `#TX-88412` for an online water-bill payment, the committed payment record survives even if the primary database node suffers a sudden kernel panic 10 milliseconds later. Which ACID property guarantees this?

- **A.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)
- **B.** Denormalize the live checkout table with five years of historical aggregates and disable ACID transaction locks
- **C.** Durability (committed writes survive restarts or crashes)
- **D.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)

### 20. MetroPulse's urban planning warehouse aggregates 10 years of bus ridership, weather, and fuel-cost metrics across `FactTrips` joined in one hop to `DimRoute`, `DimCalendar`, and `DimDepot`. Which two concepts apply? Select two.

- **A.** Append blobs in Azure Blob Storage
- **B.** Online Transaction Processing (OLTP) workload
- **C.** Online Analytical Processing (OLAP) workload
- **D.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **E.** Isolation (concurrent transactions do not interfere)

### 21. Budget analysts run complex quarterly variance queries scanning 600 million historical toll-gantry passages without touching live lane-controller databases. Which data workload type is this?

- **A.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **B.** Online Transaction Processing (OLTP) workload
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** Online Analytical Processing (OLAP) workload

### 22. In the city budget warehouse, `FactExpenditures` joins to `DimCostCenter`, which normalizes into `DimDivision`, which normalizes into `DimAgency`. Normalizing dimension tables into multi-step hierarchies produces a ____.

- **A.** First Normal Form (1NF — atomic values and no repeating column groups)
- **B.** Page blobs in Azure Blob Storage
- **C.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **D.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)

### 23. Which municipal IT specialist configures Azure SQL firewall rules, manages Microsoft Entra admin logins, monitors deadlocks, and verifies geo-redundant backup retention across utility billing databases?

- **A.** Waterfall chart (sequential positive/negative variance steps) or Funnel chart (linear stage conversion drop-off)
- **B.** Database administrator (DBA)
- **C.** Data analyst
- **D.** Data engineer

### 24. Before a Hurricane readiness drill, who executes a test restore of the city's 911 CAD relational database to a secondary Azure region and validates recovery time objectives (`RTO`)?

- **A.** Database administrator (DBA)
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Data engineer
- **D.** Data analyst

### 25. MetroPulse is standing up a citywide open-data analytics hub across Azure SQL, Microsoft Fabric, and Power BI. Which four-step sequence reflects clean role boundaries among DBA, data engineer, and data analyst?

- **A.** Data analyst configures SQL Server failover clusters → DBA authors Spark ELT notebooks in Databricks → Data engineer designs executive Power BI visuals → DBA schedules workspace app audiences
- **B.** DBA provisions & secures operational Azure SQL → Data engineer builds ELT pipelines into Fabric Lakehouse → Data engineer curates Gold star-schema tables → Data analyst models DAX KPIs & publishes Power BI reports
- **C.** Data engineer grants T-SQL row permissions on OLTP → Data analyst provisions Azure VNet private endpoints → DBA builds Power Query Dataflows Gen2 → Data analyst runs point-in-time DB restores
- **D.** DBA designs executive KPI scorecards → Data analyst writes Spark Structured Streaming checkpoints → Data engineer tunes OLTP clustered indexes → DBA publishes paginated sales packs

### 26. Which specialist builds resilient Eventstream and Spark pipelines that ingest raw bus GPS pings, impute missing stop coordinates, and write partitioned Delta Lake tables into OneLake?

- **A.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **B.** Data engineer
- **C.** Database administrator (DBA)
- **D.** Data analyst

### 27. The transit commissioner asks for an interactive on-time performance Power BI report showing route reliability DAX KPIs and neighborhood equity visuals. Which data professional builds this deliverable?

- **A.** Data engineer
- **B.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **C.** Database administrator (DBA)
- **D.** Data analyst

### 28. Working with curated Gold ridership tables, a staff member builds drill-down `Year -> Month -> Day` visuals and DAX `Cost per Passenger Mile` measures in Power BI Desktop. This staff member fulfills the ____ role.

- **A.** Database administrator (DBA)
- **B.** Page blobs in Azure Blob Storage
- **C.** Data engineer
- **D.** Data analyst

---

## Domain 2 — Identify considerations for relational data on Azure (20–25% official weight · 24 questions)

### 29. In MetroPulse's fleet schema, `Buses.BusVIN` uniquely identifies each vehicle without `NULL`s, and `MaintenanceLogs.BusVIN` references `Buses.BusVIN` so logs can only be recorded for valid fleet vehicles. Which two relational constraints are applied? Select two.

- **A.** Foreign key constraint
- **B.** Primary key constraint
- **C.** Page blobs in Azure Blob Storage
- **D.** Unstructured data
- **E.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)

### 30. In a `RouteStops` table mapping which stops appear in what sequence along each bus route, neither `RouteID` nor `StopSequenceNumber` is unique alone, so `(RouteID, StopSequenceNumber)` together form the table's ____.

- **A.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **B.** Apache Avro row-based binary format with JSON schema
- **C.** Composite key (multi-column key)
- **D.** Cold access tier (online, 90-day minimum retention for rarely accessed data)

### 31. Which relational constraint prevents a clerk from inserting `DepotID = 99` into `BusAssignments` when `DepotID = 99` does not exist in the parent `Depots` table?

- **A.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)
- **B.** First Normal Form (1NF — atomic values and no repeating column groups)
- **C.** Foreign key constraint
- **D.** Append blobs in Azure Blob Storage

### 32. In a relational database management system (`RDBMS`), entities are stored as tables (relations) in which rows represent instances and columns enforce typed attributes. What category of data does an RDBMS manage natively?

- **A.** Unstructured data
- **B.** Semi-structured data
- **C.** Structured data
- **D.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)

### 33. City fleet mechanics track parts orders in a flat sheet containing comma-separated part numbers and duplicated vendor street addresses on every row. Which four-step sequence normalizes this design to 3NF?

- **A.** Cluster-index raw JSON blobs → Delete primary keys on parent tables → Copy supplier city into every invoice item (2NF) → Combine product names into pipe-delimited strings (3NF)
- **B.** Split repeating groups into atomic columns (1NF) → Assign a unique primary key → Move partial composite-key dependencies to parent tables (2NF) → Extract transitive non-key dependencies into lookup tables (3NF)
- **C.** Create foreign keys on unsplit multi-value columns → Denormalize all lookup tables into one wide sheet → Remove partial dependencies (2NF) → Split atomic columns into repeating groups (1NF)
- **D.** Remove transitive non-key dependencies (3NF) → Merge comma-separated phone lists into one column → Delete all primary keys to speed inserts → Duplicate customer addresses across every order line

### 34. A `Citations` table stores `ViolationCodes` as `'P102; P204; P310'` inside a single string column. Decomposing each violation code into atomic scalar values across separate rows brings the table into ____.

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **C.** First Normal Form (1NF — atomic values and no repeating column groups)
- **D.** Star schema (central numeric fact table joined directly to denormalized dimension tables)

### 35. In a 1NF `ShiftAssignments` table keyed by `(DriverID, ShiftDate)`, column `DriverLicenseClass` depends only on `DriverID` rather than `(DriverID, ShiftDate)`. Moving `DriverLicenseClass` to `Drivers` achieves ____.

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Unstructured data
- **C.** First Normal Form (1NF — atomic values and no repeating column groups)
- **D.** Second Normal Form (2NF — full functional dependency on the entire composite key)

### 36. Why does MetroPulse normalize its operational utility-billing schema to ____ by moving `ZipCode -> MunicipalityName` out of `ServiceAddresses` into a `PostalZones` lookup table?

- **A.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **B.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **C.** First Normal Form (1NF — atomic values and no repeating column groups)
- **D.** Append blobs in Azure Blob Storage

### 37. During a transit database deployment, an engineer runs `ALTER TABLE FareZones ADD ZoneLabel NVARCHAR(30)`, `UPDATE FareZones SET Price = 3.00 WHERE Zone = 2`, and `GRANT EXECUTE ON usp_IssuePass TO KioskApp`. Which three SQL language categories are used? Select three.

- **A.** Optimized Row Columnar (ORC) stripe format
- **B.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **C.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **E.** Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- **F.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)

### 38. Proposed solution: A junior admin claims `GRANT` and `REVOKE` are Data Manipulation Language (`DML`) statements; the senior DBA corrects them, noting `GRANT`/`REVOKE` are `DCL` whereas `SELECT`, `INSERT`, `UPDATE`, and `DELETE` constitute ____. What completes the correction?

- **A.** Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- **B.** Use DML `SELECT` and `INSERT` statements to grant or revoke user login permissions on schemas
- **C.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)

### 39. An auditor writes `SELECT p.PermitNo, i.InspectionDate FROM Permits p ____ Inspections i ON p.PermitID = i.PermitID` so permits that have **not yet** had any inspection are excluded from the output. Which join operator fits?

- **A.** `LEFT OUTER JOIN` preserving all left-table rows with `NULL` when right-table matches are absent
- **B.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **C.** Place `SUM()` or `COUNT(*)` aggregate predicates directly inside the SQL `WHERE` clause before `GROUP BY`
- **D.** `INNER JOIN` matching related keys present in both tables

### 40. Which SQL statement subset includes `CREATE TABLE`, `ALTER TABLE`, and `DROP` schema commands for defining, altering, and removing relational objects without inserting row data?

- **A.** Place `SUM()` or `COUNT(*)` aggregate predicates directly inside the SQL `WHERE` clause before `GROUP BY`
- **B.** Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- **C.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)

### 41. MetroPulse's `TollTransactions` table physically orders rows on disk by `TransactionID` and exposes `EXEC usp_PostToll @Plate, @GantryID, @Amount` so lane controllers invoke precompiled T-SQL logic. Which two database objects are used? Select two.

- **A.** Apache Parquet columnar storage format
- **B.** Stored procedure (parameterized precompiled SQL routine)
- **C.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **D.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **E.** Append blobs in Azure Blob Storage

### 42. Clerks search the `Permits` table (already clustered on `PermitID`) by `ApplicantLastName` and `ParcelNumber`. Adding a ____ on `(ApplicantLastName, ParcelNumber)` accelerates lookups via a separate B-tree without altering physical table order.

- **A.** Database view (saved virtual `SELECT` query)
- **B.** Nonclustered index (separate B-tree structure with row locators; multiple allowed per table)
- **C.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **D.** Create four separate clustered indexes on the same relational table to sort rows four ways physically

### 43. To publish open-data 311 request statistics while masking caller phone numbers and email columns from the underlying `ServiceTickets` table, the DBA creates `vw_Public311Tickets`. What type of database object is `vw_Public311Tickets`?

- **A.** Stored procedure (parameterized precompiled SQL routine)
- **B.** Database view (saved virtual `SELECT` query)
- **C.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **D.** Page blobs in Azure Blob Storage

### 44. Instead of letting kiosk apps run ad-hoc `UPDATE` and `INSERT` statements directly against base tables, the DBA grants `EXECUTE` permission only on parameterized ____ routines while denying direct table writes.

- **A.** Delimited text format (CSV or TSV)
- **B.** Database view (saved virtual `SELECT` query)
- **C.** Stored procedure (parameterized precompiled SQL routine)
- **D.** Cold access tier (online, 90-day minimum retention for rarely accessed data)

### 45. The city controller is migrating on-premises SQL Server tax and payroll databases to Azure SQL PaaS. Which four-step workflow aligns with current Microsoft migration best practices?

- **A.** Convert relational tables into Azure Queue messages → Provision SQL Managed Instance without VNet planning → Run compatibility assessment last → Remove all primary keys before cutover
- **B.** Point production apps to an empty Azure SQL server → Open firewall `0.0.0.0-255.255.255.255` to the public internet → Assess SQL Agent blockers after cutover → Export tables manually as JPEG screenshots
- **C.** Disable TLS encryption on SQL Server → Copy `.mdf` files directly into Azure Table storage → Provision Azure SQL Database Basic tier for cross-DB SQL Agent jobs → Run Azure Migrate discovery
- **D.** Assess SQL Server readiness and SKU sizing in Azure Migrate → Select Azure SQL Database or Managed Instance → Provision target with Entra auth and TLS firewall rules → Migrate schema/data and cut over connection strings

### 46. MetroPulse builds a greenfield citizen parking app needing a fully managed single PaaS SQL database with zero OS management and passwordless managed-identity connections governed by Conditional Access. Which two Azure capabilities combine here? Select two.

- **A.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **B.** Microsoft Entra ID centralized authentication with MFA and passwordless managed identities
- **C.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **D.** Run the retired standalone Data Migration Assistant (DMA) desktop tool as Microsoft’s current cloud sizing service
- **E.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 47. Proposed solution: A city developer provisions a single Azure SQL Database expecting to run native SQL Server Agent multi-step schedules and cross-database three-part queries; when those instance features are unavailable, the architect migrates to ____ to retain managed PaaS with instance-level compatibility. What completes the fix?

- **A.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **D.** Use a single Azure SQL Database to run native SQL Server Agent jobs and cross-database three-part queries

### 48. A regional municipal consortium hosts 60 separate town clerk databases on Azure SQL Database; each town spikes only during its monthly tax deadline on different days. Which deployment option shares compute cost-efficiently across all 60 databases?

- **A.** Azure SQL Database Elastic Pool (shared eDTU or vCore compute across multi-tenant DBs)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **D.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)

### 49. City court software requires SQL Server 2017 Reporting Services (`SSRS`) installed on the exact same Windows Server OS volume as the database engine plus custom kernel filter drivers. Which Azure option meets this requirement?

- **A.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **B.** Azure Database for PostgreSQL — Flexible Server
- **C.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **D.** Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)

### 50. MetroPulse's transit-routing engine relies on PostgreSQL geometric data types (`POLYGON`, `LINESTRING`), custom extensions, and `PL/pgSQL` procedures, and wants built-in high availability without patching Linux VMs. Which Azure service fits?

- **A.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **B.** Azure Database for PostgreSQL — Flexible Server
- **C.** Azure Database for MySQL — Flexible Server
- **D.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)

### 51. The city parks department runs a public event calendar built on Drupal (`Linux + Apache + MySQL + PHP`) and wants managed PaaS with automated backups and up to 35-day point-in-time restore. Which Azure database service fits?

- **A.** Azure Database for MySQL — Flexible Server
- **B.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **C.** Azure Database for PostgreSQL — Flexible Server
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 52. During winter off-season weeks, parks developers stop compute on their non-production open-source LAMP relational server in Azure to save money while keeping TLS enforcement and server parameter tuning. Which Flexible Server PaaS offering are they using?

- **A.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **B.** Azure Stream Analytics (serverless SQL-like stream processing engine with windowing functions)
- **C.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **D.** Azure Database for MySQL — Flexible Server

---

## Domain 3 — Describe considerations for working with non-relational data on Azure (15–20% official weight · 20 questions)

### 53. Body-worn parking enforcement videos are reviewed heavily for 30 days during ticket appeals, occasionally to day 90, rarely to day 365, and retained offline for 5 years per municipal records law. Which four-step Blob lifecycle flow fits?

- **A.** Ingest active operational files directly into Archive tier → Serve millisecond web downloads from Archive without rehydration → Move 90-day files to Hot tier → Delete storage account container metadata
- **B.** Mount Archive blobs as an SMB network drive → Stream live append logs into Page blobs in Cold tier → Transition 1-year compliance archives to Hot tier → Rehydrate Hot blobs before every read
- **C.** Write unstructured video files into Azure Table `RowKey` cells → Age rows from Cool to Hot after 180 days → Convert Page blobs into SQL views → Rehydrate Cool blobs for 12 hours before reading
- **D.** Ingest active files into Hot access tier → Transition 30-day infrequent blobs to Cool tier → Move 90-day rarely read blobs to Cold tier → Transition 365-day compliance blobs to offline Archive tier (rehydrating when needed)

### 54. MetroPulse stores two types of objects in Azure Blob Storage: 50 MB drone aerial `.jpg` orthophotos uploaded in parallel blocks, and continuous turnstile security audit logs where new lines are only appended to the end. Which two blob types match? Select two.

- **A.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **B.** Append blobs in Azure Blob Storage
- **C.** Block blobs in Azure Blob Storage
- **D.** Page blobs in Azure Blob Storage
- **E.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 55. Proposed solution: Monthly PDF water bills are downloaded frequently for the first week and then accessed very rarely over the next 45 days, yet residents expect instant millisecond downloads without waiting hours for rehydration, so IT moves week-old bills to the ____. Which Blob tier balances lower storage cost over >=30 days with immediate online reads?

- **A.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **B.** Hot access tier (highest storage rate, lowest read/write access cost)
- **C.** Cool access tier (online, 30-day minimum retention for infrequently accessed data)
- **D.** Store active operational files directly in Azure Blob Archive tier for immediate millisecond web reads

### 56. To run Apache Spark analytics over transit Parquet partitions with true directory hierarchies, POSIX file/folder permissions, and atomic directory renames, which feature must be enabled on the Azure Blob Storage account?

- **A.** Azure Data Lake Storage Gen2 (Blob Storage with Hierarchical Namespace enabled)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Page blobs in Azure Blob Storage
- **D.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)

### 57. MetroPulse's citywide Microsoft Fabric workspace stores Lakehouse and Warehouse tables automatically in Delta Parquet format inside a single tenant-wide SaaS storage layer dubbed the "OneDrive for data." What is this storage layer called?

- **A.** Page blobs in Azure Blob Storage
- **B.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **C.** Microsoft OneLake (single tenant-wide SaaS data lake built into Microsoft Fabric)
- **D.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)

### 58. City engineering offices mount shared `SMB 3.0` project folders in the cloud and deploy a caching agent on depot Windows Servers so large CAD drawings open at LAN speed while cold files tier to Azure. Which two services provide this? Select two.

- **A.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)
- **B.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **E.** Append blobs in Azure Blob Storage

### 59. A municipal Linux weather-modeling cluster requires a shared POSIX-compliant network volume mounted concurrently across 16 nodes via `NFS 4.1`. Which Azure Storage service provides managed `NFS 4.1` shares?

- **A.** Block blobs in Azure Blob Storage
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)

### 60. When lifting-and-shifting an on-premises Windows file server so legacy clerk macros continue opening `Z:\Forms\PermitTemplate.dotx` via standard SMB file shares, which Azure Storage service replaces the file server?

- **A.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **B.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Store 20 GB CAD engineering drawings inside single Azure Queue storage messages

### 61. MetroPulse records 120 million smart streetlamp status entities (`DistrictCode` + `PoleID`) containing flexible properties (`wattage`, `dimLevel`, `bulbModel`) in a low-cost Azure Storage key-value service without SQL joins. Which service is this?

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Star schema (central numeric fact table joined directly to denormalized dimension tables)

### 62. In Azure Table storage, queries that filter on both `PartitionKey` and ____ execute the fastest single-entity point lookup without scanning an entire partition or table.

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Enforce server-side foreign keys and multi-table SQL `INNER JOIN` queries inside Azure Table storage
- **C.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **D.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)

### 63. When a `PartitionKey`/`RowKey` emergency siren registry needs automatic secondary indexing on non-key attributes plus multi-region active-active failover with `<10 ms` latency SLAs, which service replaces basic Azure Table storage with minimal SDK changes?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Page blobs in Azure Blob Storage
- **D.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)

### 64. A global commuter weather-widget backend on Azure Cosmos DB wants consumption-based billing measured in normalized request operations and chooses the consistency level with the **lowest RU cost and latency** because brief regional differences in temperature readings are harmless. Which two Cosmos DB concepts apply? Select two.

- **A.** Request Units (RUs) normalized compute/IO currency (Provisioned, Autoscale, or Serverless)
- **B.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **C.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **E.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)

### 65. Which Azure database service replicates non-relational containers turnkey across any number of Azure regions via global region selection and supports multi-region writes with `<10 ms` 99th-percentile read/write SLAs?

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **C.** Azure Cosmos DB turnkey global distribution with multi-region writes and <10 ms SLAs
- **D.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)

### 66. A commuter updates their favorite bus routes in the MetroPulse app backed by Azure Cosmos DB; which **default** consistency level guarantees that same commuter's app session immediately reads back their updated favorites in order?

- **A.** Session consistency (default level guaranteeing read-your-own-writes and monotonic reads per client session)
- **B.** Hot access tier (highest storage rate, lowest read/write access cost)
- **C.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)
- **D.** Strong consistency (linearizable reads guaranteed to return the latest committed write)

### 67. A municipal election precinct tally board stored in single-write-region Azure Cosmos DB requires guaranteed linearizable reads so no reader ever sees an older uncommitted or stale precinct count. Which consistency level is required?

- **A.** Session consistency (default level guaranteeing read-your-own-writes and monotonic reads per client session)
- **B.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **C.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)
- **D.** Delimited text format (CSV or TSV)

### 68. MetroPulse's cloud team is building a JSON scooter-share telemetry backend on Azure Cosmos DB. Which four-step sequence follows official Cosmos DB provisioning and partitioning practices?

- **A.** Provision an Azure Files SMB share → Enable Strong consistency across 5 multi-write regions simultaneously → Omit databases and write JSON straight to subscription tags → Query vertices using `SMB2` locks
- **B.** Create a container without a partition key → Switch the existing account between Cassandra, Gremlin, and NoSQL APIs daily → Enforce 3NF foreign-key joins across containers → Store 500 MB MP4 blobs inside single JSON items
- **C.** Install OS patches on Cosmos DB virtual machines → Format NTFS volumes for JSON items → Assign a constant single-value partition key to all 100 million documents → Query exclusively with T-SQL stored procedures
- **D.** Create a Cosmos DB account choosing the target API → Create a database and container with a high-cardinality partition key → Configure RU/s or serverless and consistency → Insert items and run partition-scoped queries

### 69. Transit planners model intersections, rail hubs, and bike docks as vertices connected by `TRAVEL_TIME` and `TRANSFER_PENALTY` edges to run multi-hop intermodal graph traversals. Which Azure Cosmos DB API is built for this?

- **A.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **B.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)

### 70. MetroPulse writes a brand-new TypeScript service storing flexible JSON 311 tickets in Cosmos DB and querying them with `SELECT c.ticketId, c.ward FROM c WHERE c.status = 'Open'`. Which native API is recommended for new JSON document workloads?

- **A.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **B.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **C.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **D.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating

### 71. A smart-highway contractor's toll-tag reader platform already uses Apache Cassandra `CQL` keyspaces and column-family tables, and wants managed PaaS in Azure without rewriting `CQL` queries. Which Cosmos DB API fits?

- **A.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **B.** Azure Cosmos DB for MongoDB (wire-protocol compatibility for BSON document apps)
- **C.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **D.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)

### 72. Proposed solution: A city open-data app written against MongoDB BSON drivers must move to Azure Cosmos DB; rather than attempting to change an existing NoSQL account's API in place, IT provisions a new ____ account and updates the app's connection string. What completes this solution?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Azure Cosmos DB for MongoDB (wire-protocol compatibility for BSON document apps)
- **D.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating

---

## Domain 4 — Describe an analytics workload on Azure (25–30% official weight · 28 questions)

### 73. MetroPulse ingests farebox, weather, and schedule feeds into a Microsoft Fabric Lakehouse. Which four-step sequence implements a clean Bronze -> Silver -> Gold ELT pipeline?

- **A.** Build Power BI visuals directly against uncleaned CSV attachments → Delete raw source history immediately → Normalize Gold tables into 3NF OLTP row stores → Export final aggregates back into email inboxes
- **B.** Publish Gold star schema before ingesting source data → Run OLTP checkout locks inside Power BI Mobile → Overwrite source ERP primary keys during read → Store Parquet files in DNS TXT records
- **C.** Extract source data via Data Factory pipeline → Land raw files into OneLake / ADLS Gen2 (Bronze) → Cleanse and conform Delta tables via Spark or SQL (Silver) → Model star-schema fact/dimension tables (Gold) for BI
- **D.** Transform terabytes on the client laptop in Notepad → Upload screenshots to Archive Blob tier → Query offline blobs live with DAX → Store fact tables inside Azure Queue messages

### 74. In modern cloud data warehousing, why do teams frequently prefer ____ over legacy pre-load ETL when ingesting high-volume municipal sensor logs into OneLake or Azure Synapse?

- **A.** Extract, Load, and Transform (ELT) pattern
- **B.** Online Transaction Processing (OLTP) workload
- **C.** Append blobs in Azure Blob Storage
- **D.** Extract, Transform, and Load (ETL) pattern

### 75. MetroPulse configures a scheduled cloud pipeline that copies nightly parking-citation tables from an on-premises SQL Server, transforms codes visually with Power Query Dataflows Gen2, and triggers a notebook refresh. Which service orchestrates this?

- **A.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **B.** Azure Data Factory / Fabric Data Factory pipelines and Dataflows Gen2
- **C.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 76. MetroPulse stores curated ridership history in open Delta Parquet files supporting ACID transactions and organizes tables into `FactBoardings` surrounded by `DimStop`, `DimRoute`, and `DimTime`. Which two analytical store concepts are combined? Select two.

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Online Transaction Processing (OLTP) workload
- **C.** Data lakehouse (Delta Lake ACID transactions and SQL/Spark queries directly over open Parquet files)
- **D.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **E.** Page blobs in Azure Blob Storage

### 77. In MetroPulse's transit warehouse, `DimRoute` contains `RouteID`, `RouteName`, `ServiceType`, and `CorridorName` in one denormalized table joined directly to `FactBoardings`. Why are dimension tables intentionally denormalized in a ____?

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **C.** Key-value non-relational store
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 78. When `DimStop` in an analytical warehouse is split into `DimStop -> DimNeighborhood -> DimBorough` to normalize geographic hierarchy attributes, the warehouse schema becomes a ____.

- **A.** Append blobs in Azure Blob Storage
- **B.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **C.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **D.** Star schema (central numeric fact table joined directly to denormalized dimension tables)

### 79. Which three Microsoft cloud platforms provide distributed Apache Spark engines capable of transforming multi-terabyte Parquet / Delta Lake datasets for large-scale analytics? Select three.

- **A.** Microsoft Fabric (unified SaaS analytics platform atop OneLake)
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Azure Synapse Analytics (serverless SQL pools, dedicated MPP SQL pools, and Spark pools)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **E.** Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)
- **F.** Azure Databricks (collaborative Apache Spark analytics, Delta Lake, and ML platform)

### 80. City data teams want one SaaS workspace experience uniting Data Factory pipelines, Lakehouse Spark notebooks, T-SQL Data Warehouse, Real-Time Intelligence, and Power BI over OneLake without managing separate Azure resource groups. Which platform fits?

- **A.** Microsoft Fabric (unified SaaS analytics platform atop OneLake)
- **B.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **C.** Azure HDInsight (managed open-source Hadoop, Hive, HBase, Kafka, and Spark clusters)
- **D.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)

### 81. A municipal analytics team uses Synapse Studio to run **serverless SQL pool** queries directly over raw CSV and Parquet files in ADLS Gen2 before loading curated aggregates into a **dedicated SQL pool**. Which Azure service provides both SQL pool flavors?

- **A.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Azure Synapse Analytics (serverless SQL pools, dedicated MPP SQL pools, and Spark pools)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 82. A regional atmospheric agency needs managed Azure clusters running open-source Apache Kafka and Apache HBase exactly as configured in their on-premises Hadoop ecosystem. Which Azure service hosts managed Hadoop/HBase/Kafka clusters?

- **A.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **B.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **C.** Azure HDInsight (managed open-source Hadoop, Hive, HBase, Kafka, and Spark clusters)
- **D.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)

### 83. MetroPulse's highway gantry job counts vehicle passages in contiguous, non-overlapping 1-minute windows (`08:00–08:01`, `08:01–08:02`, `08:02–08:03`) for congestion toll pricing. Which windowing function is this?

- **A.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **B.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **C.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **D.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)

### 84. Every 30 seconds, a bridge wind-speed stream job computes the maximum gust recorded over the last 2 minutes (`Tumbling` would not overlap, whereas this 2-minute window advances every 30 seconds). Which windowing function is used?

- **A.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **B.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **C.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **D.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)

### 85. Subway tunnel flood sensors evaluate water-level telemetry continuously as packets arrive so pump relays and dispatch alarms trigger within 1 second of a threshold breach. This pattern is ____.

- **A.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **B.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **C.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **D.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)

### 86. Every quarter, the transit authority compiles 90 days of completed maintenance work orders to submit federal grant compliance tables. Processing bounded quarterly records on a fixed schedule is ____.

- **A.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **B.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **C.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **D.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)

### 87. MetroPulse ingests 100,000 connected-bus GPS pings per second through an Azure partitioned Kafka-compatible event broker and routes live streams into Microsoft Fabric's Eventstream, Eventhouse KQL database, and Real-Time Dashboards. Which two Microsoft cloud offerings are combined? Select two.

- **A.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **B.** Azure Event Hubs (high-throughput partitioned event ingestion broker with Kafka support)
- **C.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **E.** Microsoft Fabric Real-Time Intelligence (Eventstream, Eventhouse KQL database, Real-Time Dashboards, and Activator)

### 88. A traffic engineer writes a declarative SQL-like query joining live Event Hubs loop-detector speed events against a static `RoadSegments` reference JSON file in Blob Storage and outputting alerts to Power BI. Which serverless Azure service runs this job?

- **A.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **B.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Azure Stream Analytics (serverless SQL-like stream processing engine with windowing functions)

### 89. In Microsoft Fabric or Azure Databricks, which streaming framework lets engineers apply the exact same PySpark DataFrame/SQL transformations to unbounded live telemetry streams using write-ahead checkpoints?

- **A.** Apache Spark Structured Streaming (fault-tolerant DataFrame/SQL stream processing in Databricks and Fabric)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Database view (saved virtual `SELECT` query)
- **D.** Cold access tier (online, 90-day minimum retention for rarely accessed data)

### 90. A municipal EV-charging stream groups plug-in power telemetry per charger into dynamic active charging bursts that close once 5 minutes pass with zero power-draw events. Which window type captures variable-length activity sessions?

- **A.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **B.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **C.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **D.** Optimized Row Columnar (ORC) stripe format

### 91. MetroPulse's transparency team wants to ingest transit punctuality tables, model DAX KPIs, pin a mayor's transit dashboard, and publish a read-only civic App to 80 agency leads. Which four-step Power BI workflow is correct?

- **A.** Design `.rdl` pixel-perfect invoices in Azure Stream Analytics → Publish directly to unmanaged personal OneDrive as an OLTP database → Disable table relationships → Share via anonymous firewall port `1433`
- **B.** Author multi-report dashboards inside Power BI Mobile → Export `.pbix` files to Azure Table storage → Schedule dataset refresh inside Windows Notepad → Email raw database passwords to report viewers
- **C.** Pin dashboard tiles in Power BI Desktop offline → Write Power Query M transformations inside Power BI Mobile → Store semantic models on SMB floppy shares → Require every executive viewer to edit DAX in Desktop
- **D.** Shape source data with Power Query in Power BI Desktop → Relate star-schema tables, write DAX, and build report pages → Publish model and report to Power BI Service → Pin dashboard tiles, schedule refresh, and share an App

### 92. Where in the Power BI ecosystem do team members collaborate in shared cloud **workspaces**, configure **scheduled semantic-model refreshes** via an on-premises data gateway, and pin cross-report **dashboards**?

- **A.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **B.** Microsoft Power BI Service (cloud SaaS portal for workspaces, dashboards, scheduled refresh, and Apps)
- **C.** Create multi-report pinned dashboards directly inside Power BI Desktop offline
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 93. City payroll must generate 4,500 formatted multi-page PDF pension statements with exact page breaks, repeating column headers, and row-by-row contribution tables. Which Power BI tool builds `.rdl` paginated reports for this purpose?

- **A.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **B.** Apache Spark Structured Streaming (fault-tolerant DataFrame/SQL stream processing in Databricks and Fabric)
- **C.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **D.** Microsoft Power BI Service (cloud SaaS portal for workspaces, dashboards, scheduled refresh, and Apps)

### 94. In Power BI Desktop, a transit analyst relates `DimRoute` (`1`) to `FactTrips` (`*`), builds a `Borough -> Neighborhood -> Stop` drill hierarchy, and authors `On-Time % := DIVIDE([OnTimeTrips], [TotalTrips])`. Which two Power BI modeling capabilities are used? Select two.

- **A.** Append blobs in Azure Blob Storage
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **D.** Power BI semantic model (relationships, DAX measures, hierarchies, and Import/DirectQuery/Direct Lake storage)
- **E.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)

### 95. Proposed solution: A report creator imports five disconnected flat CSVs into Power BI Desktop without defining table relationships, causing slicers on `RouteName` to fail to filter `FactRidership`; to fix filter propagation, the analyst defines `1:*` relationships inside the ____. What completes the fix?

- **A.** Page blobs in Azure Blob Storage
- **B.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** Power BI semantic model (relationships, DAX measures, hierarchies, and Import/DirectQuery/Direct Lake storage)

### 96. When a city councilor clicks `Borough = Queens` on a Power BI slicer, `Avg Speed MPH` immediately recalculates solely over Queens bus trips without storing pre-aggregated combinations on disk. `Avg Speed MPH` is implemented as a ____.

- **A.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **B.** Apache Avro row-based binary format with JSON schema
- **C.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **D.** Clustered index (defines physical leaf-level sort order; maximum one per table)

### 97. In a Power BI semantic model, placing descriptive filter fields (`RouteColor`, `DepotName`, `HolidayFlag`) in dimension tables and numeric values (`PassengerCount`, `FareCollected`) in a central fact table implements a ____.

- **A.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **B.** Graph database (vertices and directed edges)
- **C.** Append blobs in Azure Blob Storage
- **D.** Third Normal Form (3NF — no transitive dependencies between non-key columns)

### 98. MetroPulse planners want to plot 1,400 bike-share stations by `Latitude` and `Longitude` across city streets, sizing bubbles by `AvailableBikes` and coloring by `Utilization %`. Which Power BI visual type is designed for geospatial coordinates?

- **A.** Matrix visual (cross-tabbed rows/columns with stepped drill-down subtotals) or Azure Map (geospatial coordinates)
- **B.** Treemap (or pie/donut chart for small category counts) showing part-to-whole proportions
- **C.** Apache Parquet columnar storage format
- **D.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)

### 99. The city budget director wants a chart showing the FY25 surplus starting balance, positive tax-revenue bars, negative overtime/snow-removal variance bars, and the resulting FY26 ending balance. Which Power BI chart shows cumulative sequential positive and negative contributions?

- **A.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **B.** Waterfall chart (sequential positive/negative variance steps) or Funnel chart (linear stage conversion drop-off)
- **C.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)
- **D.** Page blobs in Azure Blob Storage

### 100. A transit summary report needs to display the proportional share of total trips across 22 bus depots nested inside 5 boroughs using space-filling nested rectangles. Which Power BI visual represents hierarchical part-to-whole proportions cleanly?

- **A.** Line chart (tracking continuous trends and changes over ordered time intervals)
- **B.** Treemap (or pie/donut chart for small category counts) showing part-to-whole proportions
- **C.** Append blobs in Azure Blob Storage
- **D.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)

---

## Answer Key and Explanations

### Question 1 — `D` (Describe core data concepts)

Correct answer: D (is correct). Uniform rows organized into predefined typed relational columns represent structured data. [Skill 1.1: Describe the features of structured data | Source: Explore core data concepts — Identify data formats (structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **B:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **C:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.

### Question 2 — `A` (Describe core data concepts)

Correct answer: A (is correct). Datasets adhering to a fixed tabular row-and-column schema with strict data types are structured data. [Skill 1.1: Describe the features of structured data | Source: Explore core data concepts — Identify data formats (structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **B:** Incorrect. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **C:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Incorrect. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.

### Question 3 — `B, E` (Describe core data concepts)

Correct answers: B and E (are correct). Nested `{}` key-value objects with variable per-device fields are semi-structured JSON payloads. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **B:** Correct. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **E:** Correct. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.

### Question 4 — `C` (Describe core data concepts)

Correct answer: C (is correct). Self-describing hierarchical tags and flexible attributes without a rigid relational table schema define semi-structured data. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **B:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **C:** Correct. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **D:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.

### Question 5 — `A` (Describe core data concepts)

Correct answer: A (is correct). JSON is the standard lightweight text format for hierarchical key-value pairs and arrays in REST feeds. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Correct. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **D:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.

### Question 6 — `A` (Describe core data concepts)

Correct answer: A (is correct). Raw video, audio, and image files have no internal row or tag schema and are unstructured data. [Skill 1.3: Describe the features of unstructured data | Source: Explore core data concepts — Identify data formats (unstructured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Correct. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **B:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **C:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **D:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.

### Question 7 — `D` (Describe core data concepts)

Correct answer: D (is correct). Scanned PDFs and audio recordings lack a tabular or key-value structure and are unstructured data. [Skill 1.3: Describe the features of unstructured data | Source: Explore core data concepts — Identify data formats (unstructured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. A composite key combines two or more columns (such as `OrderID` + `ProductID`) to uniquely identify rows in a junction or line-item table.
- **C:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **D:** Correct. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.

### Question 8 — `A, B` (Describe core data concepts)

Correct answers: A and B (are correct). Apache Avro is row-based binary with a JSON schema for streaming, and Apache Parquet is compressed columnar storage for analytical scans. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Correct. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **B:** Correct. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **E:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.

### Question 9 — `C` (Describe core data concepts)

Correct answer: C (is correct). Comma-separated plain-text rows without binary compression or nested hierarchy use the delimited CSV format. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **B:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **C:** Correct. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **D:** Incorrect. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.

### Question 10 — `D` (Describe core data concepts)

Correct answer: D (is correct). Optimized Row Columnar (ORC) stores data in compressed columnar stripes with built-in stripe indexes. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Incorrect. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **D:** Correct. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.

### Question 11 — `A, B` (Describe core data concepts)

Correct answers: A and B (are correct). Graph databases traverse station vertices and route edges, while key-value stores deliver fast single-key balance lookups. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Correct. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.
- **B:** Correct. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **C:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **D:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **E:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 12 — `C` (Describe core data concepts)

Correct answer: C (is correct). Document databases store and index self-contained JSON/BSON documents with flexible per-entity schemas. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **B:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **C:** Correct. A document database stores self-contained JSON/BSON documents indexed across nested attributes so each entity can evolve fields without schema migrations.
- **D:** Incorrect. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.

### Question 13 — `B` (Describe core data concepts)

Correct answer: B (is correct). Column-family (wide-column) databases organize related attributes into column families under partition/row keys for high write volume. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **B:** Correct. A column-family database groups related columns into families keyed by row and partition keys (such as Apache Cassandra or HBase) for massive write throughput.
- **C:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **D:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.

### Question 14 — `D` (Describe core data concepts)

Correct answer: D (is correct). Live ACID fare deductions commit in Azure SQL Database, Data Factory extracts history to ADLS Gen2 / OneLake Parquet, and Power BI visuals query star schemas. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Incorrect. Power BI Service is a read-optimized BI platform rather than a transactional database, and Queue storage buffers small messages rather than archiving relational rows.
- **B:** Incorrect. Paginated reports render formatted output rather than ingesting transactions, and Blob Cold tier does not execute multi-row ACID relational transactions.
- **C:** Incorrect. Archive blobs are offline and unreadable for live OLTP writes, Power BI Desktop is an authoring tool rather than an OLTP engine, and Table storage is schemaless key-value.
- **D:** Correct. Operational transactions commit in an ACID relational store first, pipelines land history in columnar lake storage, and analytical models serve BI reports without taxing OLTP.

### Question 15 — `C` (Describe core data concepts)

Correct answer: C (is correct). Queue messages cap at 64 KB for work items, whereas Block blobs in Azure Blob Storage store multi-gigabyte binary CAD files. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **B:** Incorrect. Azure Queue storage holds small asynchronous work messages (up to 64 KB per message), not multi-gigabyte binary files.
- **C:** Correct. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.
- **D:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.

### Question 16 — `A` (Describe core data concepts)

Correct answer: A (is correct). Azure Database for PostgreSQL — Flexible Server supports PostGIS spatial extensions and `PL/pgSQL` as managed PaaS. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Correct. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **B:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **C:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 17 — `B, D, F` (Describe core data concepts)

Correct answers: B, D, and F (are correct). All-or-nothing execution is Atomicity, enforcing valid rule states is Consistency, and shielding concurrent in-flight transactions is Isolation. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **B:** Correct. Consistency ensures a transaction transitions the database only from one valid rule-compliant state (keys, check constraints, types) to another.
- **C:** Incorrect. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **D:** Correct. Isolation prevents concurrent in-flight transactions from reading uncommitted intermediate edits or overwriting each other unpredictably via locking or row versioning.
- **E:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.
- **F:** Correct. Atomicity guarantees that every statement in a transaction either succeeds together or rolls back completely if any step fails, preventing half-completed transfers.

### Question 18 — `D` (Describe core data concepts)

Correct answer: D (is correct). High-volume, low-latency row inserts and updates with ACID integrity define an OLTP transactional workload. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **B:** Incorrect. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **C:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **D:** Correct. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.

### Question 19 — `C` (Describe core data concepts)

Correct answer: C (is correct). Durability ensures committed transactions are persisted to non-volatile logs/storage and survive crashes. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.
- **B:** Incorrect. Denormalized historical scans belong in an OLAP store; live checkout requires normalized OLTP tables with ACID guarantees to prevent lost or corrupted orders.
- **C:** Correct. Durability guarantees that once a transaction commits, its changes are persisted to non-volatile transaction logs/storage and survive power loss or crash recovery.
- **D:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.

### Question 20 — `C, D` (Describe core data concepts)

Correct answers: C and D (are correct). Multi-year read-intensive historical aggregation is an OLAP workload, and a central fact table with single-hop dimensions is a star schema. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **C:** Correct. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **D:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **E:** Incorrect. Isolation prevents concurrent in-flight transactions from reading uncommitted intermediate edits or overwriting each other unpredictably via locking or row versioning.

### Question 21 — `D` (Describe core data concepts)

Correct answer: D (is correct). Read-heavy historical scans isolated from live transactional operations characterize an OLAP workload. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **B:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **C:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Correct. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.

### Question 22 — `D` (Describe core data concepts)

Correct answer: D (is correct). Normalizing dimension tables into chained parent lookup tables around a fact table defines a snowflake schema. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **D:** Correct. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.

### Question 23 — `B` (Describe core data concepts)

Correct answer: B (is correct). Database security, firewall/access control, deadlock monitoring, and backup/recovery governance belong to the DBA. [Skill 1.9: Describe responsibilities for database administrators | Source: Explore data roles and services — Database administrator responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. Waterfall charts break down cumulative gains and losses between a starting and ending total, while Funnel charts track progressive drop-off across sequential pipeline stages.
- **B:** Correct. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **C:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **D:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.

### Question 24 — `A` (Describe core data concepts)

Correct answer: A (is correct). Disaster-recovery failover drills and database restore verification are responsibilities of the database administrator (DBA). [Skill 1.9: Describe responsibilities for database administrators | Source: Explore data roles and services — Database administrator responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Correct. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **B:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **D:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.

### Question 25 — `B` (Describe core data concepts)

Correct answer: B (is correct). The DBA secures operational SQL, the data engineer builds ELT pipelines and Gold star tables, and the data analyst authors DAX KPIs and Power BI reports. [Skill 1.10: Describe responsibilities for data engineers | Source: Explore data roles and services — Data engineer responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. Cluster HA belongs to the DBA, Spark ELT pipelines belong to the data engineer, and visual storytelling/app distribution belongs to the data analyst.
- **B:** Correct. DBAs govern operational database engines, data engineers build ingestion/transformation pipelines into curated analytical stores, and data analysts model KPIs and visual reports.
- **C:** Incorrect. Operational DB security and PITR restores are DBA duties, network/pipeline plumbing belongs to infra/data engineering, and analysts focus on semantic models and visuals.
- **D:** Incorrect. KPI scorecards and sales packs are data analyst outputs, whereas Spark streaming pipelines belong to data engineers and OLTP index maintenance belongs to DBAs.

### Question 26 — `B` (Describe core data concepts)

Correct answer: B (is correct). Data engineers design, build, and maintain streaming and batch ingestion/transformation pipelines into analytical stores. [Skill 1.10: Describe responsibilities for data engineers | Source: Explore data roles and services — Data engineer responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **B:** Correct. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **C:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **D:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.

### Question 27 — `D` (Describe core data concepts)

Correct answer: D (is correct). Data analysts model semantic metrics and craft visual Power BI reports and dashboards for business and civic leaders. [Skill 1.11: Describe responsibilities for data analysts | Source: Explore data roles and services — Data analyst responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **B:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **C:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **D:** Correct. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.

### Question 28 — `D` (Describe core data concepts)

Correct answer: D (is correct). Authoring DAX business measures and interactive visual stories over curated data defines the data analyst role. [Skill 1.11: Describe responsibilities for data analysts | Source: Explore data roles and services — Data analyst responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **D:** Correct. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.

### Question 29 — `A, B` (Identify considerations for relational data on Azure)

Correct answers: A and B (are correct). `BusVIN` on `Buses` is a primary key, and `BusVIN` on `MaintenanceLogs` is a foreign key enforcing referential integrity. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Correct. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.
- **B:** Correct. A primary key uniquely identifies each row in a relational table and implicitly forbids `NULL` and duplicate key values.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **E:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.

### Question 30 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). A key formed by combining two or more columns to guarantee row uniqueness is a composite key. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **B:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **C:** Correct. A composite key combines two or more columns (such as `OrderID` + `ProductID`) to uniquely identify rows in a junction or line-item table.
- **D:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.

### Question 31 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). A foreign key constraint validates that every non-null child reference matches an existing parent key value. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.
- **B:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **C:** Correct. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 32 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Relational tables of typed columns and uniform rows manage structured data. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **B:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **C:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **D:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.

### Question 33 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). 1NF splits multi-value cells into atomic columns with a primary key, 2NF removes partial composite-key dependencies, and 3NF removes transitive non-key dependencies. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. Copying supplier attributes into invoice items creates transitive redundancy, and pipe-delimited multi-value strings violate 1NF.
- **B:** Correct. Normalization progresses sequentially: 1NF enforces atomic values and row uniqueness, 2NF removes partial dependencies on composite keys, and 3NF eliminates transitive non-key dependencies.
- **C:** Incorrect. Foreign keys require atomic primary keys first, and 1NF eliminates repeating groups rather than creating them.
- **D:** Incorrect. You cannot achieve 3NF before 1NF/2NF, comma-separated lists violate 1NF atomicity, and duplicating addresses reintroduces update anomalies.

### Question 34 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Eliminating multi-valued attributes and repeating column groups satisfies First Normal Form (1NF). [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **C:** Correct. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **D:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.

### Question 35 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Removing partial functional dependencies on a subset of a composite primary key achieves Second Normal Form (2NF). [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **C:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **D:** Correct. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.

### Question 36 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Third Normal Form (3NF) removes transitive non-key dependencies, eliminating redundant text storage and preventing update/delete anomalies. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **B:** Correct. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **C:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 37 — `B, E, F` (Identify considerations for relational data on Azure)

Correct answers: B, E, and F (are correct). `ALTER TABLE` is DDL, `UPDATE` is DML, and `GRANT EXECUTE` is DCL. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.
- **B:** Correct. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **C:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **D:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **E:** Correct. DML statements query, add, modify, or delete row data stored inside relational tables.
- **F:** Correct. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.

### Question 38 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Data Manipulation Language (DML) comprises `SELECT`, `INSERT`, `UPDATE`, and `DELETE` for querying and modifying row data. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Correct. DML statements query, add, modify, or delete row data stored inside relational tables.
- **B:** Incorrect. Granting and revoking security permissions belongs to DCL (`GRANT`, `REVOKE`, `DENY`), not DML.
- **C:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **D:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.

### Question 39 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). An `INNER JOIN` returns only rows with matching keys in both `Permits` and `Inspections`. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. `LEFT OUTER JOIN` keeps every row from the left table (for example, all customers) and fills `NULL` for right-table columns when no related order exists.
- **B:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **C:** Incorrect. SQL `WHERE` evaluates individual pre-grouped rows and rejects aggregate functions; group-level aggregate filters belong in the `HAVING` clause.
- **D:** Correct. `INNER JOIN` returns only row pairs whose join predicate matches in both the left and right tables, excluding unmatched rows.

### Question 40 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Data Definition Language (DDL) creates, alters, and removes schema objects such as tables, views, and indexes. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. SQL `WHERE` evaluates individual pre-grouped rows and rejects aggregate functions; group-level aggregate filters belong in the `HAVING` clause.
- **B:** Incorrect. DML statements query, add, modify, or delete row data stored inside relational tables.
- **C:** Correct. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **D:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.

### Question 41 — `B, C` (Identify considerations for relational data on Azure)

Correct answers: B and C (are correct). A clustered index dictates physical table row order, and a stored procedure runs parameterized server-side SQL routines. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **B:** Correct. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.
- **C:** Correct. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **D:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **E:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 42 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). A nonclustered index maintains a separate sorted key structure with row locators pointing back to the base table. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **B:** Correct. A nonclustered index maintains a separate sorted key structure pointing back to the base table rows, accelerating selective lookups on non-primary search columns.
- **C:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **D:** Incorrect. Because a clustered index dictates the single physical leaf-level storage order of the table’s rows, a table can have at most one clustered index (plus multiple nonclustered indexes).

### Question 43 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). A database view is a virtual table defined by a saved `SELECT` query that can project safe columns while hiding sensitive fields. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.
- **B:** Correct. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **C:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 44 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Stored procedures encapsulate business logic and allow fine-grained `EXECUTE` permissions without granting direct table write access. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **B:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **C:** Correct. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.
- **D:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.

### Question 45 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Assess compatibility and SKU sizing in Azure Migrate first, select Azure SQL Database or Managed Instance, provision with Entra/TLS security, and migrate data before cutover. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Queue storage is not a relational migration vehicle, SQL Managed Instance requires VNet subnet sizing upfront, and removing primary keys corrupts relational integrity.
- **B:** Incorrect. Cutting over before data migration breaks production, opening all public IPs violates security, and assessments must run before selecting the target SKU.
- **C:** Incorrect. Azure Table storage cannot mount `.mdf` database files, and single Azure SQL Database does not host SQL Server Agent or cross-database instance queries.
- **D:** Correct. Azure Migrate discovers workloads, flags compatibility blockers, and recommends right-sized Azure SQL targets before secure provisioning, data sync, and connection cutover.

### Question 46 — `B, C` (Identify considerations for relational data on Azure)

Correct answers: B and C (are correct). Azure SQL Database provides single-DB managed PaaS, and Microsoft Entra ID provides managed-identity passwordless auth and Conditional Access. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **B:** Correct. Microsoft Entra ID (formerly Azure AD) centralizes identity governance, conditional access, MFA, and passwordless managed-identity connections to Azure data services.
- **C:** Correct. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **D:** Incorrect. Microsoft retired Data Migration Assistant (DMA) in July 2025; Azure Migrate and the Azure SQL Migration extension handle SQL discovery, assessment, and right-sizing.
- **E:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 47 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Azure SQL Managed Instance supports SQL Server Agent and cross-database queries inside a fully managed PaaS instance. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Correct. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **D:** Incorrect. Single Azure SQL Database is database-scoped and does not include SQL Server Agent or cross-database instance queries; those require SQL Managed Instance or SQL Server on Azure VMs.

### Question 48 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). An Azure SQL Database Elastic Pool allocates shared eDTU or vCore compute across multiple databases with staggered peak loads. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Correct. An Elastic Pool shares a pool of compute resources across multiple single databases that have unpredictable, staggered usage spikes to optimize cost.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **D:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.

### Question 49 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). SQL Server on Azure Virtual Machines (IaaS) provides full OS control, legacy engine versions, and co-hosted SSRS/host agents. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Correct. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **B:** Incorrect. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **C:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **D:** Incorrect. The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.

### Question 50 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting spatial geometry, extensions, and `PL/pgSQL`. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **B:** Correct. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **C:** Incorrect. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.
- **D:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.

### Question 51 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Azure Database for MySQL — Flexible Server delivers managed PaaS MySQL Community Edition with HA and up to 35-day PITR. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Correct. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.
- **B:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **C:** Incorrect. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 52 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Azure Database for MySQL — Flexible Server supports stop/start cost optimization, TLS connection security, and customizable server parameters. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **B:** Incorrect. Azure Stream Analytics runs declarative Stream Analytics Query Language (`SELECT ... GROUP BY TumblingWindow(...)`) jobs joining live streams with reference data into sinks.
- **C:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **D:** Correct. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.

### Question 53 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Blobs start in Hot, age to Cool after 30 days, move to Cold after 90 days, and archive offline in Archive tier for multi-year retention. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Archive tier is offline and cannot serve direct reads until rehydrated to Hot or Cool, which takes hours.
- **B:** Incorrect. Blob tiers are object storage rather than SMB shares, Archive rather than Hot minimizes 1-year retention storage cost, and Hot blobs require no rehydration.
- **C:** Incorrect. Table storage entities hold small key-value properties rather than large video files, and Cool/Cold tiers remain online with immediate millisecond read access.
- **D:** Correct. Lifecycle management policies automatically age blobs from lowest-read-cost Hot through Cool and Cold down to lowest-storage-cost offline Archive.

### Question 54 — `B, C` (Describe considerations for working with non-relational data on Azure)

Correct answers: B and C (are correct). Block blobs store discrete media files via parallel block uploads, while Append blobs optimize end-of-blob log appends. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **B:** Correct. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Correct. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **E:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 55 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). The Cool access tier lowers storage cost for data kept at least 30 days while remaining online with millisecond read latency. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **B:** Incorrect. The Hot tier is online storage optimized for data that is accessed or modified frequently, carrying the lowest transaction/read cost.
- **C:** Correct. The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.
- **D:** Incorrect. Archive tier blobs are stored offline and cannot be read directly until rehydrated to Hot or Cool, which takes hours.

### Question 56 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Azure Data Lake Storage (ADLS) Gen2 is enabled via the Hierarchical Namespace setting on an Azure Storage account. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Correct. ADLS Gen2 adds a true POSIX-ACL directory hierarchy and atomic folder rename/delete operations atop Azure Blob Storage for big-data analytics engines.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.

### Question 57 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Microsoft OneLake is the single, unified tenant-wide SaaS data lake built into Microsoft Fabric. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **C:** Correct. OneLake is Microsoft Fabric’s unified ADLS Gen2-compatible logical data lake that stores Delta Parquet data once and shares it via zero-copy Shortcuts across workloads.
- **D:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.

### Question 58 — `B, C` (Describe considerations for working with non-relational data on Azure)

Correct answers: B and C (are correct). Azure Files hosts managed SMB/NFS shares, and Azure File Sync caches active files on Windows Servers with cloud tiering. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
- **B:** Correct. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **C:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **E:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 59 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Files Premium shares support managed `NFS 4.1` as well as `SMB 3.0` network mounts. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.
- **B:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.

### Question 60 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Azure Files provides cloud SMB file shares mountable to drive letters (`Z:`) on Windows clients and servers. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **B:** Incorrect. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **C:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Incorrect. Azure Queue storage holds small asynchronous work messages (up to 64 KB per message), not multi-gigabyte binary files.

### Question 61 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Azure Table storage stores schemaless key-value entities indexed by `PartitionKey` (`DistrictCode`) and `RowKey` (`PoleID`). [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **C:** Correct. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.

### Question 62 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Specifying both `PartitionKey` and `RowKey` resolves directly to a single entity in Azure Table storage. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Correct. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. Azure Table storage is a schemaless key-value store indexed only by `PartitionKey` and `RowKey` with no foreign keys or server-side table joins.
- **C:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **D:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.

### Question 63 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Azure Cosmos DB for Table adds global distribution, automatic secondary indexes, and <10 ms SLAs to the Table `PartitionKey`/`RowKey` API. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Correct. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.

### Question 64 — `A, E` (Describe considerations for working with non-relational data on Azure)

Correct answers: A and E (are correct). Operations are measured in Request Units (RUs, including Serverless/Autoscale), and Eventual consistency delivers the lowest latency and RU cost. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Correct. Cosmos DB measures CPU, memory, and IOPS per database operation in Request Units (RUs), billed via Provisioned/Autoscale RU/s or consumption-based Serverless.
- **B:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **C:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **D:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **E:** Correct. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.

### Question 65 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Azure Cosmos DB provides turnkey multi-region global distribution and financially backed single-digit millisecond latency SLAs. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **C:** Correct. Azure Cosmos DB replicates data transparently across selected Azure regions with financially backed 99.999% availability and single-digit millisecond read/write latency.
- **D:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.

### Question 66 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Session consistency is Cosmos DB's default setting and guarantees monotonic read-your-own-writes within a client session. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Correct. Session consistency is Cosmos DB’s default level, balancing low latency and throughput while guaranteeing each user session immediately sees its own writes in order.
- **B:** Incorrect. The Hot tier is online storage optimized for data that is accessed or modified frequently, carrying the lowest transaction/read cost.
- **C:** Incorrect. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.
- **D:** Incorrect. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.

### Question 67 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Strong consistency guarantees linearizable reads of the latest committed write. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. Session consistency is Cosmos DB’s default level, balancing low latency and throughput while guaranteeing each user session immediately sees its own writes in order.
- **B:** Correct. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **C:** Incorrect. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 68 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Choose the API at account creation, create a database and container with a high-cardinality partition key, configure RU/s or serverless + consistency, and issue partition-scoped queries. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB sits under an account -> database -> container -> item hierarchy, not SMB shares or subscription tags.
- **B:** Incorrect. Every Cosmos DB container requires a partition key, the API is fixed per account, Cosmos DB does not enforce cross-container foreign keys, and item size is capped at 2 MB.
- **C:** Incorrect. Cosmos DB is fully managed PaaS with no OS patching, a single-value partition key creates a 20 GB logical-partition bottleneck, and triggers/sprocs use JavaScript rather than T-SQL.
- **D:** Correct. API selection happens at account creation, partition key design happens at container creation to distribute storage/RU evenly, and partition-scoped queries avoid cross-partition fan-out.

### Question 69 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Cosmos DB for Apache Gremlin stores property-graph vertices and edges queried via Gremlin traversals. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **B:** Correct. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.

### Question 70 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Azure Cosmos DB for NoSQL is the native JSON document API supporting SQL query expressions. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Correct. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **B:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **C:** Incorrect. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **D:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.

### Question 71 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Azure Cosmos DB for Apache Cassandra provides wire-protocol compatibility for CQL column-family workloads. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Correct. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **B:** Incorrect. Cosmos DB for MongoDB lets existing MongoDB drivers and tools store BSON documents in Cosmos DB simply by updating the connection string.
- **C:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **D:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.

### Question 72 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Because APIs are immutable after account creation, existing MongoDB BSON apps connect to a dedicated Azure Cosmos DB for MongoDB account. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Correct. Cosmos DB for MongoDB lets existing MongoDB drivers and tools store BSON documents in Cosmos DB simply by updating the connection string.
- **D:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.

### Question 73 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Data Factory lands raw files into OneLake Bronze, Spark/SQL cleanses Silver Delta tables, and curated Gold star schemas feed BI. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Incorrect. Skipping cleansing degrades report accuracy, deleting raw Bronze files prevents replayability, and Gold analytical layers favor denormalized star schemas over 3NF.
- **B:** Incorrect. Analytical ingestion is read-only against operational sources and builds Bronze -> Silver -> Gold sequentially.
- **C:** Correct. Modern ELT lands raw data in scalable lake storage first, then leverages cloud compute to cleanse Silver tables and publish Gold star schemas for analytics.
- **D:** Incorrect. ELT executes transformations in scalable cloud engines rather than client laptops, and Archive blobs/Queues cannot back live BI queries.

### Question 74 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). ELT lands raw data rapidly into cheap lake storage and harnesses elastic distributed Spark/SQL cloud compute to transform data at scale in place. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Correct. ELT extracts raw source data, loads it directly into scalable lake/warehouse storage, and runs distributed cloud compute (Spark or SQL) to cleanse and model in place.
- **B:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **C:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **D:** Incorrect. ETL transforms, scrubs, or redacts sensitive fields in an intermediate processing engine prior to loading only the conformed structure into the target analytical store.

### Question 75 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Azure Data Factory (and Data Factory in Microsoft Fabric) orchestrates Copy pipelines, Dataflows Gen2, and downstream notebook activities. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **B:** Correct. Data Factory orchestrates code-free data movement (90+ connectors via Copy activity) and visual Power Query transformations (Dataflows Gen2) or Spark/Mapping Data Flows.
- **C:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 76 — `C, D` (Describe an analytics workload on Azure)

Correct answers: C and D (are correct). Delta Lake ACID tables over Parquet implement a data lakehouse, and `FactBoardings` with single-hop dimensions implements a star schema. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **C:** Correct. A lakehouse combines the low-cost open file flexibility of a data lake with ACID transactions, schema enforcement, and SQL warehouse performance via Delta Lake tables.
- **D:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **E:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 77 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Star schemas denormalize dimensions to minimize multi-table joins and deliver fast, intuitive slicing and grouping in BI queries. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **C:** Incorrect. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 78 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Splitting dimension hierarchies into normalized sub-dimension tables turns a star schema into a snowflake schema. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Correct. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **C:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **D:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.

### Question 79 — `A, C, F` (Describe an analytics workload on Azure)

Correct answers: A, C, and F (are correct). Microsoft Fabric, Azure Synapse Analytics, and Azure Databricks all include managed Apache Spark compute for large-scale lake analytics. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Correct. Microsoft Fabric unifies Data Factory, Data Engineering, Data Warehouse, Data Science, Real-Time Intelligence, and Power BI in one SaaS workspace sharing OneLake Delta tables.
- **B:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Correct. Azure Synapse Analytics integrates serverless SQL on-demand lake querying, dedicated MPP SQL warehousing, Apache Spark pools, and Synapse Pipelines in Synapse Studio.
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **E:** Incorrect. The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.
- **F:** Correct. Azure Databricks provides managed Apache Spark clusters, collaborative Python/SQL/Scala/R notebooks, Unity Catalog governance, and Delta Lake processing on Azure.

### Question 80 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Microsoft Fabric is Microsoft's unified SaaS analytics platform built atop OneLake. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Correct. Microsoft Fabric unifies Data Factory, Data Engineering, Data Warehouse, Data Science, Real-Time Intelligence, and Power BI in one SaaS workspace sharing OneLake Delta tables.
- **B:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **C:** Incorrect. Azure HDInsight provisions managed clusters of open-source Apache big-data frameworks when lift-and-shift Hadoop/Hive/HBase/Kafka compatibility is required.
- **D:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.

### Question 81 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Azure Synapse Analytics offers both serverless SQL pools for lake exploration and dedicated MPP SQL pools for enterprise warehousing. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Correct. Azure Synapse Analytics integrates serverless SQL on-demand lake querying, dedicated MPP SQL warehousing, Apache Spark pools, and Synapse Pipelines in Synapse Studio.
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 82 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Azure HDInsight deploys managed cloud clusters for open-source Hadoop, Hive, HBase, Kafka, and Spark workloads. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **B:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **C:** Correct. Azure HDInsight provisions managed clusters of open-source Apache big-data frameworks when lift-and-shift Hadoop/Hive/HBase/Kafka compatibility is required.
- **D:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.

### Question 83 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Fixed-length, contiguous, non-overlapping time slices where each event falls into exactly one slice define a tumbling window. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **B:** Correct. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **C:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **D:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.

### Question 84 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). A hopping window advances a fixed-size window forward by a shorter hop interval, creating scheduled overlapping windows. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **B:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **C:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **D:** Correct. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.

### Question 85 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Continuous real-time processing of unbounded event streams for immediate action is stream processing. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **B:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **C:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **D:** Correct. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.

### Question 86 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Scheduled processing over bounded sets of accumulated historical data is batch processing. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **B:** Correct. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **C:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **D:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.

### Question 87 — `B, E` (Describe an analytics workload on Azure)

Correct answers: B and E (are correct). Azure Event Hubs buffers partitioned telemetry streams, and Microsoft Fabric Real-Time Intelligence provides Eventstream, Eventhouse KQL, and Real-Time Dashboards. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **B:** Correct. Azure Event Hubs ingests millions of telemetry events per second into partitioned append logs (supporting native AMQP/HTTPS and Apache Kafka producers) for downstream stream consumers.
- **C:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **D:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **E:** Correct. Fabric Real-Time Intelligence ingests and routes events via Eventstream, indexes high-volume telemetry in Eventhouse KQL databases, visualizes live tiles, and triggers Activator alerts.

### Question 88 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Azure Stream Analytics joins live event streams with static reference data using declarative SQL-like window queries. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **B:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Correct. Azure Stream Analytics runs declarative Stream Analytics Query Language (`SELECT ... GROUP BY TumblingWindow(...)`) jobs joining live streams with reference data into sinks.

### Question 89 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Apache Spark Structured Streaming processes continuous streams via Spark DataFrame/SQL APIs with fault-tolerant checkpoints. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Correct. Spark Structured Streaming treats a live event stream as an unbounded table processed via familiar Spark SQL/DataFrame APIs with checkpointed exactly-once guarantees.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **D:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.

### Question 90 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). A session window groups events until a specified quiet timeout elapses without new events. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **B:** Correct. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **C:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **D:** Incorrect. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.

### Question 91 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Shape/model and author report pages in Power BI Desktop, publish to a Power BI Service workspace, pin dashboard tiles and schedule refresh in the Service, and distribute a Power BI App. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Incorrect. Paginated `.rdl` reports are authored in Power BI Report Builder, Stream Analytics processes event streams, and port `1433` is SQL Server TDS rather than BI sharing.
- **B:** Incorrect. Dashboards are created in Power BI Service rather than Power BI Mobile, and dataset refresh plus secure sharing are managed in Power BI Service workspaces.
- **C:** Incorrect. Dashboards exist only in Power BI Service (not Power BI Desktop), Power BI Mobile is for consumption, and viewers consume shared Apps/reports in browser or mobile.
- **D:** Correct. Power BI Desktop handles Power Query prep, semantic modeling, and report design, while Power BI Service hosts scheduled refresh, multi-report dashboards, and governed App distribution.

### Question 92 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Shared workspaces, gateway-backed scheduled refresh, dashboards, and Apps are capabilities of the cloud Power BI Service. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **B:** Correct. Power BI Service (`app.powerbi.com` / Fabric) hosts published semantic models and reports, pins cross-report dashboard tiles, schedules gateway refreshes, and distributes governed Apps.
- **C:** Incorrect. Dashboards with pinned tiles across multiple reports are a cloud-only feature of Power BI Service, not Power BI Desktop.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 93 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Power BI Report Builder creates pixel-perfect paginated (`.rdl`) reports optimized for multi-page PDF output and printing. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Correct. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **B:** Incorrect. Spark Structured Streaming treats a live event stream as an unbounded table processed via familiar Spark SQL/DataFrame APIs with checkpointed exactly-once guarantees.
- **C:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **D:** Incorrect. Power BI Service (`app.powerbi.com` / Fabric) hosts published semantic models and reports, pins cross-report dashboard tiles, schedules gateway refreshes, and distributes governed Apps.

### Question 94 — `C, D` (Describe an analytics workload on Azure)

Correct answers: C and D (are correct). Relationships and drill-down hierarchies live in the Power BI semantic model, and `DIVIDE(...)` defines a dynamic DAX measure. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Correct. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **D:** Correct. A Power BI semantic model defines `1:*` star-schema relationships, reusable DAX measures, drill-down hierarchies, and column metadata consumed across reports.
- **E:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.

### Question 95 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Table relationships and filter propagation directions are defined in the Power BI semantic model. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **C:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Correct. A Power BI semantic model defines `1:*` star-schema relationships, reusable DAX measures, drill-down hierarchies, and column metadata consumed across reports.

### Question 96 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). DAX measures dynamically evaluate aggregations within the current slicer and visual filter context at query time. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Correct. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **B:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **C:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **D:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.

### Question 97 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Separating filter/grouping dimensions from numeric fact tables implements a star schema. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **B:** Incorrect. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **C:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **D:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.

### Question 98 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). An Azure Map (or Filled Map) plots geospatial coordinates and regional boundaries interactively on a map canvas. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Correct. A Matrix aggregates measures across both row and column hierarchies like a pivot table, whereas Azure/Filled Maps plot spatial latitude/longitude or regional boundaries.
- **B:** Incorrect. Pie/donut charts show part-to-whole shares for a few slices, while treemaps use nested rectangles to display proportional composition across larger hierarchical categories.
- **C:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **D:** Incorrect. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.

### Question 99 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). A Waterfall chart illustrates how sequential positive and negative values bridge a starting total to an ending total. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **B:** Correct. Waterfall charts break down cumulative gains and losses between a starting and ending total, while Funnel charts track progressive drop-off across sequential pipeline stages.
- **C:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 100 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). A Treemap displays hierarchical part-to-whole proportions as nested colored rectangles sized by measure value. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Incorrect. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.
- **B:** Correct. Pie/donut charts show part-to-whole shares for a few slices, while treemaps use nested rectangles to display proportional composition across larger hierarchical categories.
- **C:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **D:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
