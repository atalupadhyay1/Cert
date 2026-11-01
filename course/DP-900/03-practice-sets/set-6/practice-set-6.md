# Microsoft Exam DP-900: Microsoft Azure Data Fundamentals — Full-Length Mock Exam 6

**Theme:** Global Logistics & Clean Energy Grid — Data Roles, MySQL Flexible Server, Lifecycle Policies, Fabric Lakehouse & DAX KPIs  
**Credential:** `Microsoft Certified: Azure Data Fundamentals` *(Beginner / Fundamentals · **no prerequisite** · **never expires**)*  
**Study guide baseline:** `July 21, 2026` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `75 minutes` (`45 sec/question`, matching live 45-minute / 60-question pace; `45 minutes` optional speed drill · **closed-book**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn documentation — not affiliated with or endorsed by Microsoft Corporation. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Describe core data concepts (25–30% official weight · 28 questions)

### 1. NordGrid Logistics stores shipping container tariffs in a relational table with typed `OriginPort`, `DestinationPort`, `TEURateUSD`, and `ValidFromDate` columns across every row. Which data representation is this?

- **A.** Apache Avro row-based binary format with JSON schema
- **B.** Structured data
- **C.** Semi-structured data
- **D.** Unstructured data

### 2. Wind-farm asset registries record turbine serial numbers, hub heights in meters, and commissioning dates in strictly typed SQL table columns. How is this dataset classified?

- **A.** Graph database (vertices and directed edges)
- **B.** Unstructured data
- **C.** JavaScript Object Notation (JSON) document format
- **D.** Structured data

### 3. Customs EDI-to-API gateways emit `{}` shipment manifests where refrigerated containers include nested `reeferSetPointC` objects while dry containers include `stackingLimitKg` keys without sharing a fixed table grid. Which two items apply? Select two.

- **A.** JavaScript Object Notation (JSON) document format
- **B.** Page blobs in Azure Blob Storage
- **C.** Unstructured data
- **D.** Semi-structured data
- **E.** Structured data

### 4. Solar inverter gateways transmit XML telemetry packets containing self-describing `<Inverter>`, `<MPPTString>`, and optional `<FaultCode>` tags that vary across inverter brands. These XML packets represent ____.

- **A.** Semi-structured data
- **B.** Unstructured data
- **C.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **D.** Structured data

### 5. NordGrid's vessel AIS tracking bus serializes millions of compact binary position events prefixed by a JSON schema header for downstream Kafka and Event Hubs consumers. Which data format is used?

- **A.** Apache Avro row-based binary format with JSON schema
- **B.** Page blobs in Azure Blob Storage
- **C.** Bar or column chart (comparing discrete categorical values across items)
- **D.** Delimited text format (CSV or TSV)

### 6. Port crane cameras upload container-damage `.jpg` photos, turbine blade drone inspection `.mp4` videos, and VHF harbor pilot `.wav` audio clips into Azure Storage. Together, these files are ____.

- **A.** Semi-structured data
- **B.** Apache Parquet columnar storage format
- **C.** Structured data
- **D.** Unstructured data

### 7. Scanned paper bills of lading (`.pdf`) and signed customs clearance stamps (`.png`) are archived in cloud blob containers. How is this data categorized?

- **A.** Unstructured data
- **B.** Structured data
- **C.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **D.** Composite key (multi-column key)

### 8. NordGrid's energy-forecasting team runs analytical scans reading only `WindSpeedMS` and `MegawattOutput` across a 95-column, 18-billion-row historical SCADA archive. Which two compressed columnar file formats avoid scanning the other 93 columns? Select two.

- **A.** Apache Parquet columnar storage format
- **B.** Optimized Row Columnar (ORC) stripe format
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** Delimited text format (CSV or TSV)
- **E.** Page blobs in Azure Blob Storage

### 9. A regional freight broker exports a 600-row port holiday calendar as plain UTF-8 text where fields are separated by commas and opened in any text editor. Which file format is this?

- **A.** Apache Parquet columnar storage format
- **B.** Optimized Row Columnar (ORC) stripe format
- **C.** Apache Avro row-based binary format with JSON schema
- **D.** Delimited text format (CSV or TSV)

### 10. A smart-grid REST API returns nested substation status payloads (`{"substation": "S12", "breakers": [{"id": 1, "closed": true}]}`) to operator web consoles. Which text file/payload format is used?

- **A.** First Normal Form (1NF — atomic values and no repeating column groups)
- **B.** Delimited text format (CSV or TSV)
- **C.** JavaScript Object Notation (JSON) document format
- **D.** Page blobs in Azure Blob Storage

### 11. NordGrid selects two non-relational stores: one simple store looking up customs broker API keys solely by `ClientKeyID`, and one wide-column store ingesting millions of smart-meter readings grouped into `voltage` and `watt_hour` column families. Which two database categories match? Select two.

- **A.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **B.** Column-family (wide-column) database
- **C.** Delimited text format (CSV or TSV)
- **D.** Database view (saved virtual `SELECT` query)
- **E.** Key-value non-relational store

### 12. Supply-chain planners model ports, rail yards, and warehouses as vertices connected by `SHIPPING_LANE` and `CUSTOMS_CORRIDOR` edges to compute resilient rerouting paths when a canal closes. Which database type fits best?

- **A.** Append blobs in Azure Blob Storage
- **B.** Graph database (vertices and directed edges)
- **C.** Delimited text format (CSV or TSV)
- **D.** Key-value non-relational store

### 13. Hazardous-cargo declarations carry deeply nested safety sheets, UN class arrays, and emergency contacts that vary per chemical shipment, queried across nested JSON fields. Which non-relational store model fits?

- **A.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **B.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **C.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **D.** Document database

### 14. NordGrid is designing its Azure architecture from live freight booking transactions through global carbon-intensity Power BI scorecards. Which four-step Azure service flow places each workload properly?

- **A.** Capture OLTP writes directly in Archive Blob tier → Run live checkout queries in Power BI Desktop → Copy rows to Azure Files SMB → Normalize into Azure Table storage
- **B.** Land raw checkout clicks in Paginated Reports → Transform via SMB file locks → Commit ACID transactions in Azure Blob Cold tier → Query via Gremlin graph vertices
- **C.** Serve live checkout writes in Power BI Service → Export dashboards to CSV → Load CSVs into Azure SQL Database → Archive active rows to Azure Queue storage
- **D.** Capture OLTP writes in Azure SQL Database → Extract changes via Data Factory pipeline → Land Parquet files in ADLS Gen2 / OneLake → Serve star-schema visuals in Power BI

### 15. NordGrid adopts Microsoft Fabric and wants a single tenant-wide SaaS data lake that stores Lakehouse and Warehouse Delta Parquet files automatically while linking existing ADLS Gen2 buckets via Shortcuts. Which datastore is this?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Microsoft OneLake (single tenant-wide SaaS data lake built into Microsoft Fabric)
- **C.** Store 20 GB CAD engineering drawings inside single Azure Queue storage messages
- **D.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)

### 16. Legacy maritime weather-routing software on vessel-ops Windows VMs requires reading GRIB forecast files from a shared SMB network drive (`\\maritime\grib\`). Which Azure datastore provides managed SMB cloud shares?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

### 17. When two freight forwarders vie for the final refrigerated slot on a vessel, booking the slot and issuing the container booking reference must succeed or roll back together, and concurrent bookings must not corrupt slot counts. Which three concepts describe this system? Select three.

- **A.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **B.** Online Analytical Processing (OLAP) workload
- **C.** Atomicity (all-or-nothing transaction unit)
- **D.** Online Transaction Processing (OLTP) workload
- **E.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **F.** Isolation (concurrent transactions do not interfere)

### 18. Once NordGrid's grid-dispatch database returns `COMMIT` on a substation breaker switching order, that committed record remains safely recorded even if the host VM restarts unexpectedly two seconds later. Which ACID property guarantees this?

- **A.** Apache Parquet columnar storage format
- **B.** Durability (committed writes survive restarts or crashes)
- **C.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **D.** Online Analytical Processing (OLAP) workload

### 19. Database `CHECK` and foreign-key constraints on `VesselVoyages` guarantee `LoadedContainers <= MaxVesselCapacity` before and after every transaction. Which ACID property preserves valid schema and business-rule states?

- **A.** Consistency (valid schema and constraint state)
- **B.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)
- **C.** Denormalize the live checkout table with five years of historical aggregates and disable ACID transaction locks
- **D.** Cool access tier (online, 30-day minimum retention for infrequently accessed data)

### 20. NordGrid's sustainability team aggregates six years of voyage fuel burn, TEU-miles, and `CO2` emissions across `FactVoyages` joined directly to `DimVessel`, `DimPort`, and `DimDate`. Which two concepts characterize this system? Select two.

- **A.** Atomicity (all-or-nothing transaction unit)
- **B.** Online Analytical Processing (OLAP) workload
- **C.** Online Transaction Processing (OLTP) workload
- **D.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **E.** Page blobs in Azure Blob Storage

### 21. Grid economists run multi-year seasonal peak-demand aggregations across 3 billion historical smart-meter intervals without impacting live SCADA dispatch writes. Which workload type is this?

- **A.** Online Analytical Processing (OLAP) workload
- **B.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **C.** Online Transaction Processing (OLTP) workload
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)

### 22. In NordGrid's logistics warehouse, `FactShipments` joins to `DimPort`, which normalizes into `DimCountry`, which normalizes into `DimTradeRegion`. What schema pattern does this normalized dimension chain represent?

- **A.** First Normal Form (1NF — atomic values and no repeating column groups)
- **B.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **C.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **D.** Append blobs in Azure Blob Storage

### 23. Proposed solution: NordGrid assigns one specialist to configure Azure SQL transparent data encryption, manage database firewall and Entra role permissions, verify 35-day backup restores, and tune OLTP index fragmentation — classifying that specialist as a ____. Is that role assignment accurate?

- **A.** Data analyst
- **B.** Database administrator (DBA)
- **C.** Line chart (tracking continuous trends and changes over ordered time intervals)
- **D.** Data engineer

### 24. When a customs-clearance relational database approaches storage limits and suffers lock waits, which data professional scales the Azure SQL compute tier, resolves blocking locks, and validates failover readiness?

- **A.** Database administrator (DBA)
- **B.** Data analyst
- **C.** Data engineer
- **D.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)

### 25. NordGrid is launching a fleet decarbonization analytics hub across Azure SQL, Microsoft Fabric Lakehouse, and Power BI. Which four-step workflow reflects proper responsibilities across DBA, data engineer, and data analyst?

- **A.** DBA designs executive KPI scorecards → Data analyst writes Spark Structured Streaming checkpoints → Data engineer tunes OLTP clustered indexes → DBA publishes paginated sales packs
- **B.** Data engineer grants T-SQL row permissions on OLTP → Data analyst provisions Azure VNet private endpoints → DBA builds Power Query Dataflows Gen2 → Data analyst runs point-in-time DB restores
- **C.** Data analyst configures SQL Server failover clusters → DBA authors Spark ELT notebooks in Databricks → Data engineer designs executive Power BI visuals → DBA schedules workspace app audiences
- **D.** DBA provisions & secures operational Azure SQL → Data engineer builds ELT pipelines into Fabric Lakehouse → Data engineer curates Gold star-schema tables → Data analyst models DAX KPIs & publishes Power BI reports

### 26. Which specialist builds scheduled Data Factory pipelines and Spark Structured Streaming jobs that ingest vessel telemetry, cleanse GPS outliers, and populate Gold Delta tables in OneLake?

- **A.** Data analyst
- **B.** Data engineer
- **C.** Database administrator (DBA)
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)

### 27. NordGrid's VP of Fleet Operations requests an interactive Power BI dashboard tracking `Grams CO2 per Ton-Km` DAX KPIs, port dwell-time visuals, and route slicers. Which role authors this Power BI solution?

- **A.** Data engineer
- **B.** Database administrator (DBA)
- **C.** Data analyst
- **D.** Azure Migrate (discovery, readiness assessment, and SKU right-sizing for SQL Server)

### 28. Using Power BI Desktop over curated Gold grid-generation tables, a team member authors `Capacity Factor %` DAX measures and wind-vs-solar visual comparisons for executives. This team member is acting as a ____.

- **A.** Data engineer
- **B.** Database administrator (DBA)
- **C.** Data analyst
- **D.** Page blobs in Azure Blob Storage

---

## Domain 2 — Identify considerations for relational data on Azure (20–25% official weight · 24 questions)

### 29. In NordGrid's relational schema, `Containers.ContainerISO` uniquely identifies each shipping box, while `VoyageManifests` uses `(VoyageID, ContainerISO)` together to uniquely identify a box loaded on a specific voyage. Which two key types are used? Select two.

- **A.** Composite key (multi-column key)
- **B.** Append blobs in Azure Blob Storage
- **C.** Primary key constraint
- **D.** Unstructured data
- **E.** Session window (variable-length activity bursts closed after a quiet timeout gap)

### 30. In `VoyageManifests`, column `VoyageID` references `Voyages.VoyageID` so the database blocks adding manifest rows for nonexistent voyages. Which relational constraint enforces this referential integrity?

- **A.** Foreign key constraint
- **B.** Apache Avro row-based binary format with JSON schema
- **C.** Primary key constraint
- **D.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)

### 31. In a relational table, why can't a clerk accidentally type `'Pending'` into a `DepartureUTC DATETIME2 NOT NULL` column?

- **A.** Structured data
- **B.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **C.** Unstructured data
- **D.** Semi-structured data

### 32. Every normalized operational table defines a ____ to guarantee no two rows share the same identifier and no identifier cell contains `NULL`.

- **A.** Primary key constraint
- **B.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **C.** Cold access tier (online, 90-day minimum retention for rarely accessed data)
- **D.** Foreign key constraint

### 33. NordGrid inherits an unnormalized spreadsheet of wind-turbine work orders containing comma-separated technician names and repeated substation street addresses. Which four-step workflow normalizes the schema to 3NF?

- **A.** Cluster-index raw JSON blobs → Delete primary keys on parent tables → Copy supplier city into every invoice item (2NF) → Combine product names into pipe-delimited strings (3NF)
- **B.** Create foreign keys on unsplit multi-value columns → Denormalize all lookup tables into one wide sheet → Remove partial dependencies (2NF) → Split atomic columns into repeating groups (1NF)
- **C.** Remove transitive non-key dependencies (3NF) → Merge comma-separated phone lists into one column → Delete all primary keys to speed inserts → Duplicate customer addresses across every order line
- **D.** Split repeating groups into atomic columns (1NF) → Assign a unique primary key → Move partial composite-key dependencies to parent tables (2NF) → Extract transitive non-key dependencies into lookup tables (3NF)

### 34. A `Shipments` staging table stores `SealNumbers` as `'SL-11, SL-12, SL-13'` in one text cell. Decomposing each seal number into atomic single-valued rows satisfies ____.

- **A.** First Normal Form (1NF — atomic values and no repeating column groups)
- **B.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **C.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **D.** Third Normal Form (3NF — no transitive dependencies between non-key columns)

### 35. In a 1NF `CharterLegs` table keyed by `(CharterID, LegNumber)`, column `VesselFlagCountry` depends on `CharterID` alone rather than `(CharterID, LegNumber)`. Moving `VesselFlagCountry` to `Charters` satisfies ____.

- **A.** First Normal Form (1NF — atomic values and no repeating column groups)
- **B.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **C.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **D.** Second Normal Form (2NF — full functional dependency on the entire composite key)

### 36. In a 2NF `Substations` table keyed by `SubstationID`, non-key column `GridZoneCode` determines `RegulatorName`. Extracting `GridZoneCode -> RegulatorName` into a `GridZones` table prevents update anomalies and satisfies ____.

- **A.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **B.** Optimized Row Columnar (ORC) stripe format
- **C.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **D.** First Normal Form (1NF — atomic values and no repeating column groups)

### 37. During a port database release, scripts execute `ALTER TABLE Berths ADD MaxDraftMeters DECIMAL(5,2)`, `UPDATE Berths SET MaxDraftMeters = 16.5 WHERE BerthID = 4`, and `GRANT SELECT ON Berths TO HarborPilots`. Which three SQL subsets are used? Select three.

- **A.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **B.** Apache Parquet columnar storage format
- **C.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **E.** Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- **F.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)

### 38. NordGrid runs `SELECT v.VesselName, c.CharterDate FROM Vessels v ____ Charters c ON v.VesselID = c.VesselID` to return **only** vessels that have at least one charter contract, excluding unchartered vessels. Which join clause fits?

- **A.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **B.** `LEFT OUTER JOIN` preserving all left-table rows with `NULL` when right-table matches are absent
- **C.** `INNER JOIN` matching related keys present in both tables
- **D.** Use DML `SELECT` and `INSERT` statements to grant or revoke user login permissions on schemas

### 39. Proposed solution: To list origin ports that shipped more than `10,000` refrigerated containers in `2026`, an analyst writes `SELECT OriginPort, SUM(TEU) FROM Bookings WHERE CargoType = 'Reefer' AND BookingYear = 2026 GROUP BY OriginPort HAVING SUM(TEU) > 10000;`. Does this place row and aggregate filters in the valid SQL clauses?

- **A.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **B.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **C.** `WHERE` filters rows before grouping; `HAVING` filters aggregated groups after `GROUP BY`
- **D.** Place `SUM()` or `COUNT(*)` aggregate predicates directly inside the SQL `WHERE` clause before `GROUP BY`

### 40. When a yard gate system logs a truck arrival via `INSERT INTO GateMoves (TruckPlate, ArrivedUTC) VALUES ('TX-4910', SYSUTCDATETIME())`, which SQL subset is `INSERT INTO` part of?

- **A.** Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- **B.** Use DML `SELECT` and `INSERT` statements to grant or revoke user login permissions on schemas
- **C.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)

### 41. NordGrid's `SmartMeterReads` table physically orders rows on disk by `ReadID` via one index and maintains fast secondary lookup structures on `MeterSerial` and `SubstationID` via additional indexes. Which two index types are used? Select two.

- **A.** Nonclustered index (separate B-tree structure with row locators; multiple allowed per table)
- **B.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **C.** Append blobs in Azure Blob Storage
- **D.** Database view (saved virtual `SELECT` query)
- **E.** Session window (variable-length activity bursts closed after a quiet timeout gap)

### 42. Port gate kiosks invoke `EXEC usp_ReleaseContainer @ContainerISO = 'MSCU1234567', @CustomsPin = '8841'` so customs verification, hold checks, and gate-pass creation execute inside precompiled server SQL. `usp_ReleaseContainer` is a ____.

- **A.** Database view (saved virtual `SELECT` query)
- **B.** Nonclustered index (separate B-tree structure with row locators; multiple allowed per table)
- **C.** Stored procedure (parameterized precompiled SQL routine)
- **D.** Delimited text format (CSV or TSV)

### 43. To give freight partners a simplified virtual table (`vw_ActiveVesselETAs`) joining `Voyages`, `Vessels`, and `Ports` without exposing internal fuel-cost columns, the DBA creates a ____.

- **A.** Database view (saved virtual `SELECT` query)
- **B.** Stored procedure (parameterized precompiled SQL routine)
- **C.** Create four separate clustered indexes on the same relational table to sort rows four ways physically
- **D.** Page blobs in Azure Blob Storage

### 44. How many ____ structures can be defined on a single relational SQL table at one time, given that leaf pages are stored in that index's physical sort order?

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Database view (saved virtual `SELECT` query)
- **C.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **D.** Create four separate clustered indexes on the same relational table to sort rows four ways physically

### 45. NordGrid is retiring an on-premises datacenter in Rotterdam and moving 18 SQL Server logistics databases to Azure SQL PaaS. Which four-step migration sequence follows Microsoft's current guidance?

- **A.** Convert relational tables into Azure Queue messages → Provision SQL Managed Instance without VNet planning → Run compatibility assessment last → Remove all primary keys before cutover
- **B.** Assess SQL Server readiness and SKU sizing in Azure Migrate → Select Azure SQL Database or Managed Instance → Provision target with Entra auth and TLS firewall rules → Migrate schema/data and cut over connection strings
- **C.** Disable TLS encryption on SQL Server → Copy `.mdf` files directly into Azure Table storage → Provision Azure SQL Database Basic tier for cross-DB SQL Agent jobs → Run Azure Migrate discovery
- **D.** Point production apps to an empty Azure SQL server → Open firewall `0.0.0.0-255.255.255.255` to the public internet → Assess SQL Agent blockers after cutover → Export tables manually as JPEG screenshots

### 46. NordGrid maps two PaaS relational targets: Target A is a cloud-native container-tracking API needing a single serverless PaaS database; Target B is a legacy fleet-payroll system needing SQL Server Agent jobs and cross-database queries without OS patching. Which two Azure SQL PaaS services match A and B? Select two.

- **A.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **D.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **E.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)

### 47. NordGrid provides isolated single-tenant Azure SQL Databases for 110 regional port agents across 18 time zones whose daytime peaks never coincide. Placing those 110 databases into an ____ shares vCore capacity cost-effectively.

- **A.** Use a single Azure SQL Database to run native SQL Server Agent jobs and cross-database three-part queries
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Azure SQL Database Elastic Pool (shared eDTU or vCore compute across multi-tenant DBs)
- **D.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)

### 48. A grid-stability SCADA package requires Windows Server 2022 OS-level COM drivers, a pinned SQL Server 2019 CU build, and local disk access for a vendor dongle service. Which Azure deployment model is required?

- **A.** Azure Database for MySQL — Flexible Server
- **B.** Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)
- **C.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **D.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)

### 49. Proposed solution: Instead of using the retired Data Migration Assistant (`DMA`), NordGrid's cloud team runs discovery, compatibility assessment, and Azure SQL SKU right-sizing in ____. Does this align with current Microsoft Learn guidance?

- **A.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **B.** Run the retired standalone Data Migration Assistant (DMA) desktop tool as Microsoft’s current cloud sizing service
- **C.** Azure Migrate (discovery, readiness assessment, and SKU right-sizing for SQL Server)
- **D.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)

### 50. NordGrid's customer shipment-booking portal runs on a `LAMP` (`Linux, Apache, MySQL, PHP`) stack and IT wants managed PaaS hosting with automatic failover, TLS security, and up to 35-day point-in-time restore. Which Azure service fits?

- **A.** Azure Database for MySQL — Flexible Server
- **B.** Azure Database for PostgreSQL — Flexible Server
- **C.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **D.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)

### 51. Grid GIS engineers store high-voltage transmission corridors using PostgreSQL spatial geometry types, custom extensions, and `PL/pgSQL` functions on managed Azure PaaS monitored via `pgAdmin`. Which service are they using?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **C.** Azure Database for PostgreSQL — Flexible Server
- **D.** Azure Database for MySQL — Flexible Server

### 52. Developers pause compute on their staging MySQL database over weekends to cut cloud spend while retaining automatic storage backups on Azure PaaS. Which deployment option of Azure Database for MySQL supports stop/start cost controls?

- **A.** Azure Stream Analytics (serverless SQL-like stream processing engine with windowing functions)
- **B.** Azure Database for MySQL — Flexible Server
- **C.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **D.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)

---

## Domain 3 — Describe considerations for working with non-relational data on Azure (15–20% official weight · 20 questions)

### 53. Customs X-ray container scans are queried actively for 30 days, occasionally to day 90, rarely through month 12, and archived 7 years for border-security audits. Which four-step Blob Storage lifecycle flow minimizes storage spend?

- **A.** Write unstructured video files into Azure Table `RowKey` cells → Age rows from Cool to Hot after 180 days → Convert Page blobs into SQL views → Rehydrate Cool blobs for 12 hours before reading
- **B.** Ingest active files into Hot access tier → Transition 30-day infrequent blobs to Cool tier → Move 90-day rarely read blobs to Cold tier → Transition 365-day compliance blobs to offline Archive tier (rehydrating when needed)
- **C.** Mount Archive blobs as an SMB network drive → Stream live append logs into Page blobs in Cold tier → Transition 1-year compliance archives to Hot tier → Rehydrate Hot blobs before every read
- **D.** Ingest active operational files directly into Archive tier → Serve millisecond web downloads from Archive without rehydration → Move 90-day files to Hot tier → Delete storage account container metadata

### 54. NordGrid compares two **online** Azure Blob cost-saving tiers that require **no multi-hour rehydration** before reading: Tier 1 has a 30-day minimum retention for infrequent reads, and Tier 2 has a 90-day minimum retention with even lower storage cost for rare reads. Which two tiers are Tier 1 and Tier 2? Select two.

- **A.** Cold access tier (online, 90-day minimum retention for rarely accessed data)
- **B.** Page blobs in Azure Blob Storage
- **C.** Cool access tier (online, 30-day minimum retention for infrequently accessed data)
- **D.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **E.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 55. NordGrid uploads 500 GB of satellite weather `.nc` files and Parquet exports in parallel chunks for analytical processing in Azure Storage. Which Azure Blob type stores discrete files and analytics objects up to ~190.7 TiB?

- **A.** Page blobs in Azure Blob Storage
- **B.** Block blobs in Azure Blob Storage
- **C.** Append blobs in Azure Blob Storage
- **D.** Store active operational files directly in Azure Blob Archive tier for immediate millisecond web reads

### 56. Enabling ____ (`Hierarchical Namespace`) on an Azure Blob Storage account lets Spark and Data Factory jobs execute atomic directory renames and enforce fine-grained POSIX ACLs on folders.

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Azure Data Lake Storage Gen2 (Blob Storage with Hierarchical Namespace enabled)
- **C.** Page blobs in Azure Blob Storage
- **D.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)

### 57. Before a compliance officer can read a 4-year-old bill-of-lading PDF stored in the offline ____, the blob must first be rehydrated (copied or tier-changed) to the Hot or Cool tier.

- **A.** Cool access tier (online, 30-day minimum retention for infrequently accessed data)
- **B.** Hot access tier (highest storage rate, lowest read/write access cost)
- **C.** Store active operational files directly in Azure Blob Archive tier for immediate millisecond web reads
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 58. NordGrid's port offices mount shared `SMB 3.0` tariff folders in Azure while local terminal Windows Servers cache active manifests on LAN disks and cloud-tier older manifests automatically. Which two Azure services combine here? Select two.

- **A.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **D.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **E.** Block blobs in Azure Blob Storage

### 59. An offshore wind-simulation Linux cluster mounts a shared cloud file system concurrently across 24 worker VMs using `NFS 4.1`. Which Azure Storage service provides managed `NFS 4.1` shares?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Append blobs in Azure Blob Storage
- **D.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)

### 60. Proposed solution: When a remote port office suffers high WAN latency opening shared `.xlsx` stowage plans from Azure Files, IT installs ____ on the port's local Windows Server so active files open at local LAN speed while staying synced with Azure Files. Does this meet the goal?

- **A.** Apache Spark Structured Streaming (fault-tolerant DataFrame/SQL stream processing in Databricks and Fabric)
- **B.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **C.** Azure Data Lake Storage Gen2 (Blob Storage with Hierarchical Namespace enabled)
- **D.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)

### 61. NordGrid stores 300 million reefer-plug voltage check entities keyed by `PortCode` (`PartitionKey`) and `PlugID` (`RowKey`) in a low-cost schemaless key-value store inside Azure Storage. Which service is used?

- **A.** Enforce server-side foreign keys and multi-table SQL `INNER JOIN` queries inside Azure Table storage
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 62. In Azure Table storage, entities that share the same ____ are stored together in the same logical partition, while `RowKey` uniquely identifies each entity inside that partition.

- **A.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **B.** Enforce server-side foreign keys and multi-table SQL `INNER JOIN` queries inside Azure Table storage
- **C.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 63. NordGrid's global `PartitionKey`/`RowKey` container-seal lookup service outgrows standard Azure Table storage and now needs multi-region writes across Rotterdam, Singapore, and Los Angeles with `<10 ms` SLAs and secondary indexes. Which service upgrades it seamlessly?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Page blobs in Azure Blob Storage
- **C.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)

### 64. NordGrid runs a global shipment-tracking API on Azure Cosmos DB replicated across five continents with multi-region writes, `<10 ms` latency SLAs, and Autoscale capacity billed in normalized request units. Which two Cosmos DB capabilities are highlighted? Select two.

- **A.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **B.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **C.** Request Units (RUs) normalized compute/IO currency (Provisioned, Autoscale, or Serverless)
- **D.** Azure Cosmos DB turnkey global distribution with multi-region writes and <10 ms SLAs
- **E.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 65. When a customs broker submits a clearance update in NordGrid's portal backed by Cosmos DB, which **default** consistency level ensures that broker's session immediately reads its own submitted update in order?

- **A.** Session consistency (default level guaranteeing read-your-own-writes and monotonic reads per client session)
- **B.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)
- **C.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating
- **D.** Strong consistency (linearizable reads guaranteed to return the latest committed write)

### 66. A high-voltage grid-interlock state table in single-write-region Cosmos DB cannot tolerate any regional reader seeing stale breaker status; linearizable latest-write reads are mandatory. Which consistency level is required?

- **A.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)
- **B.** Session consistency (default level guaranteeing read-your-own-writes and monotonic reads per client session)
- **C.** Apache Avro row-based binary format with JSON schema
- **D.** Strong consistency (linearizable reads guaranteed to return the latest committed write)

### 67. Public ocean-buoy wave-height map pins stored in Cosmos DB tolerate a few seconds of cross-region convergence delay in exchange for the lowest RU consumption and fastest writes. Which consistency level fits best?

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **C.** Isolation (concurrent transactions do not interfere)
- **D.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)

### 68. NordGrid is provisioning a new Azure Cosmos DB JSON container for smart-meter outage events partitioned by `/feederId`. Which four-step workflow follows official Cosmos DB design rules?

- **A.** Create a container without a partition key → Switch the existing account between Cassandra, Gremlin, and NoSQL APIs daily → Enforce 3NF foreign-key joins across containers → Store 500 MB MP4 blobs inside single JSON items
- **B.** Create a Cosmos DB account choosing the target API → Create a database and container with a high-cardinality partition key → Configure RU/s or serverless and consistency → Insert items and run partition-scoped queries
- **C.** Provision an Azure Files SMB share → Enable Strong consistency across 5 multi-write regions simultaneously → Omit databases and write JSON straight to subscription tags → Query vertices using `SMB2` locks
- **D.** Install OS patches on Cosmos DB virtual machines → Format NTFS volumes for JSON items → Assign a constant single-value partition key to all 100 million documents → Query exclusively with T-SQL stored procedures

### 69. NordGrid builds a new Go microservice storing flexible JSON customs manifests in Cosmos DB and querying them with `SELECT c.bolNumber, c.port FROM c WHERE c.port = 'NLRTM'`. Which Cosmos DB API is used?

- **A.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **B.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **C.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating
- **D.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)

### 70. Grid engineers model substations, transformers, and feeders as vertices connected by `ENERGIZES` edges to trace downstream outage blast radius in real time via graph traversals. Which Cosmos DB API fits?

- **A.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **B.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **C.** Block blobs in Azure Blob Storage
- **D.** Azure Cosmos DB for MongoDB (wire-protocol compatibility for BSON document apps)

### 71. NordGrid's acquired wind-turbine OEM streams wide-column SCADA logs using Apache Cassandra `CQL` drivers and wants managed multi-region PaaS in Azure without changing `CQL` queries. Which Cosmos DB API fits?

- **A.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **B.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **C.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **D.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)

### 72. A freight-forwarding subsidiary's Python app stores BSON booking quotes using `PyMongo` drivers and wants to migrate to Azure Cosmos DB purely by updating its connection string to a newly created ____ account. What completes this migration?

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Azure Cosmos DB for MongoDB (wire-protocol compatibility for BSON document apps)
- **C.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **D.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating

---

## Domain 4 — Describe an analytics workload on Azure (25–30% official weight · 28 questions)

### 73. NordGrid ingests ERP bookings, AIS vessel feeds, and SCADA logs into a Microsoft Fabric Lakehouse. Which four-step sequence implements the medallion ELT pattern?

- **A.** Extract source data via Data Factory pipeline → Land raw files into OneLake / ADLS Gen2 (Bronze) → Cleanse and conform Delta tables via Spark or SQL (Silver) → Model star-schema fact/dimension tables (Gold) for BI
- **B.** Build Power BI visuals directly against uncleaned CSV attachments → Delete raw source history immediately → Normalize Gold tables into 3NF OLTP row stores → Export final aggregates back into email inboxes
- **C.** Transform terabytes on the client laptop in Notepad → Upload screenshots to Archive Blob tier → Query offline blobs live with DAX → Store fact tables inside Azure Queue messages
- **D.** Publish Gold star schema before ingesting source data → Run OLTP checkout locks inside Power BI Mobile → Overwrite source ERP primary keys during read → Store Parquet files in DNS TXT records

### 74. NordGrid extracts raw JSON weather feeds, lands them directly into OneLake Bronze folders unchanged, and runs distributed Fabric Spark notebooks to flatten and type-cast columns into Silver Delta tables. Which pattern is this?

- **A.** Page blobs in Azure Blob Storage
- **B.** Extract, Load, and Transform (ELT) pattern
- **C.** Extract, Transform, and Load (ETL) pattern
- **D.** Online Transaction Processing (OLTP) workload

### 75. Which Microsoft cloud service provides code-free **Copy activity** pipelines for 90+ sources alongside visual Power Query **Dataflows Gen2** transformations to schedule nightly logistics data loads?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **C.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **D.** Azure Data Factory / Fabric Data Factory pipelines and Dataflows Gen2

### 76. NordGrid stores curated energy tables in OneLake as ACID **Delta Lake** Parquet files (`FactGenerationMWh`) joined directly in one hop to `DimTurbine`, `DimWindFarm`, and `DimTime`. Which two analytical concepts are combined? Select two.

- **A.** Data lakehouse (Delta Lake ACID transactions and SQL/Spark queries directly over open Parquet files)
- **B.** Key-value non-relational store
- **C.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **D.** Append blobs in Azure Blob Storage
- **E.** Online Transaction Processing (OLTP) workload

### 77. In a dimensional warehouse ____, why do `DimVessel` and `DimPort` store human-readable descriptive text attributes while `FactVoyages` stores surrogate keys and numeric measures (`FuelTons`, `DelayMinutes`)?

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **C.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 78. Which modern analytical store design avoids keeping separate siloed data lakes and relational warehouses by providing ACID transactions, schema enforcement, and SQL/Spark access directly over open Parquet files?

- **A.** First Normal Form (1NF — atomic values and no repeating column groups)
- **B.** Data lakehouse (Delta Lake ACID transactions and SQL/Spark queries directly over open Parquet files)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 79. NordGrid reviews Microsoft cloud services for big-data analytics: (1) unified SaaS analytics atop OneLake, (2) collaborative Apache Spark + ML platform with Unity Catalog, and (3) managed open-source Hadoop/Hive/Kafka clusters. Which three services are these? Select three.

- **A.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Azure Databricks (collaborative Apache Spark analytics, Delta Lake, and ML platform)
- **D.** Azure HDInsight (managed open-source Hadoop, Hive, HBase, Kafka, and Spark clusters)
- **E.** Microsoft Fabric (unified SaaS analytics platform atop OneLake)
- **F.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)

### 80. NordGrid wants data engineers using Spark Lakehouses, SQL developers using T-SQL Warehouses, real-time operators using KQL Eventhouses, and BI analysts using Power BI Direct Lake to work in one SaaS platform over OneLake. Which platform is this?

- **A.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Microsoft Fabric (unified SaaS analytics platform atop OneLake)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 81. Which Azure PaaS analytics service lets engineers explore raw ADLS Gen2 Parquet files via on-demand **serverless SQL pools** and run enterprise MPP warehousing in **dedicated SQL pools** within Synapse Studio?

- **A.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Azure Synapse Analytics (serverless SQL pools, dedicated MPP SQL pools, and Spark pools)
- **D.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)

### 82. NordGrid's weather-routing data scientists train vessel fuel-optimization models over 100 TB of ocean-current Parquet files using collaborative PySpark notebooks, Delta Lake, and MLflow on Azure. Which service fits best?

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Azure Databricks (collaborative Apache Spark analytics, Delta Lake, and ML platform)
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 83. European electricity markets settle grid generation in strict contiguous, non-overlapping 15-minute settlement periods (`12:00–12:15`, `12:15–12:30`) where every meter reading belongs to one period. Which streaming window is this?

- **A.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **B.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **C.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **D.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)

### 84. Every 2 minutes, NordGrid's wind-ramp monitor calculates average megawatt output across the preceding 10-minute span so adjacent 10-minute windows overlap by 8 minutes. Which windowing function is used?

- **A.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **B.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **C.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **D.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)

### 85. Port crane telemetry groups container-hoist movements into dynamic active loading bursts per crane that close automatically once the crane sits idle for 10 minutes with no hoist events. Which window type is this?

- **A.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **B.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **C.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **D.** Apache Parquet columnar storage format

### 86. Every January, NordGrid processes all completed voyages from the prior calendar year to file annual IMO maritime carbon-intensity reports. Processing bounded annual history on a schedule is ____.

- **A.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **B.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **C.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **D.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)

### 87. NordGrid deploys two real-time grid analytics workloads: Workload 1 uses Microsoft Fabric **Eventstream**, **Eventhouse** `KQL` databases, and **Activator** alerts; Workload 2 runs checkpointed PySpark `readStream` DataFrames merging telemetry into Delta Lake. Which two technologies match? Select two.

- **A.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **B.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **C.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **D.** Apache Spark Structured Streaming (fault-tolerant DataFrame/SQL stream processing in Databricks and Fabric)
- **E.** Microsoft Fabric Real-Time Intelligence (Eventstream, Eventhouse KQL database, Real-Time Dashboards, and Activator)

### 88. NordGrid streams 300,000 smart-inverter telemetry packets per second from regional concentrators into a partitioned Azure event broker supporting both AMQP and Apache Kafka producers. Which Azure ingestion service is this?

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Database view (saved virtual `SELECT` query)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Azure Event Hubs (high-throughput partitioned event ingestion broker with Kafka support)

### 89. An engineer writes a serverless SQL-like stream query (`SELECT SubstationId, MIN(FrequencyHz) ... GROUP BY SubstationId, SlidingWindow(second, 10)`) reading from Event Hubs and triggering grid under-frequency alerts. Which Azure service executes this query?

- **A.** Azure Stream Analytics (serverless SQL-like stream processing engine with windowing functions)
- **B.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **C.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **D.** Cold access tier (online, 90-day minimum retention for rarely accessed data)

### 90. Evaluating transformer oil-gas sensor readings continuously within milliseconds of arrival to trip a protective relay before catastrophic failure is an example of ____.

- **A.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **B.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **C.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **D.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)

### 91. NordGrid's analytics team wants to connect to Gold warehouse tables, author DAX sustainability KPIs, pin a boardroom executive dashboard, and distribute a governed App to 150 port managers. Which four-step Power BI sequence fits?

- **A.** Shape source data with Power Query in Power BI Desktop → Relate star-schema tables, write DAX, and build report pages → Publish model and report to Power BI Service → Pin dashboard tiles, schedule refresh, and share an App
- **B.** Author multi-report dashboards inside Power BI Mobile → Export `.pbix` files to Azure Table storage → Schedule dataset refresh inside Windows Notepad → Email raw database passwords to report viewers
- **C.** Pin dashboard tiles in Power BI Desktop offline → Write Power Query M transformations inside Power BI Mobile → Store semantic models on SMB floppy shares → Require every executive viewer to edit DAX in Desktop
- **D.** Design `.rdl` pixel-perfect invoices in Azure Stream Analytics → Publish directly to unmanaged personal OneDrive as an OLTP database → Disable table relationships → Share via anonymous firewall port `1433`

### 92. Proposed solution: Before publishing to the cloud, an analyst uses Power Query Editor to clean port codes, defines `1:*` star-schema relationships, authors DAX measures, and designs interactive report pages locally in ____. Is this the right authoring tool?

- **A.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **B.** Create multi-report pinned dashboards directly inside Power BI Desktop offline
- **C.** Microsoft Power BI Service (cloud SaaS portal for workspaces, dashboards, scheduled refresh, and Apps)
- **D.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)

### 93. Customs authorities require printed multi-page **Dangerous Goods Cargo Manifests** with fixed page headers, exact margins, and every container row rendered across 25 PDF pages without scrollbars. Which Power BI tool creates `.rdl` paginated reports?

- **A.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **B.** Azure Event Hubs (high-throughput partitioned event ingestion broker with Kafka support)
- **C.** Microsoft Power BI Service (cloud SaaS portal for workspaces, dashboards, scheduled refresh, and Apps)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

### 94. In Power BI, NordGrid relates `DimPort` and `DimVessel` (`1`) to `FactVoyages` (`*`), builds a `Continent -> Country -> Port` hierarchy, and defines `Fleet Utilization % := DIVIDE([LoadedTEU], [CapacityTEU])`. Which two Power BI modeling elements are used? Select two.

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Power BI semantic model (relationships, DAX measures, hierarchies, and Import/DirectQuery/Direct Lake storage)
- **C.** Append blobs in Azure Blob Storage
- **D.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **E.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)

### 95. When a port director slices a report by `TradeLane = Transpacific` and `Quarter = Q4`, `On-Schedule Arrival %` dynamically recomputes from the underlying voyage rows rather than reading a static stored column. `On-Schedule Arrival %` is a ____.

- **A.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **B.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **C.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **D.** Page blobs in Azure Blob Storage

### 96. In Microsoft Fabric and Power BI, configuring **Direct Lake** or **Import** storage mode, relationship cross-filter direction, and default number formatting happens inside the ____.

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **C.** Power BI semantic model (relationships, DAX measures, hierarchies, and Import/DirectQuery/Direct Lake storage)
- **D.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)

### 97. Proposed solution: To eliminate ambiguous filter paths and slow multi-hop OLTP joins in Power BI, NordGrid reshapes 14 normalized ERP tables into `FactFreightCost` surrounded by `DimCarrier`, `DimLane`, and `DimDate` — a ____. Does this follow Microsoft's Power BI modeling guidance?

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Append blobs in Azure Blob Storage
- **C.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **D.** Key-value non-relational store

### 98. NordGrid's control room wants to plot 800 cargo vessels and offshore wind farms by live `Latitude` and `Longitude` on an interactive world map colored by `WeatherAlertLevel`. Which Power BI visual class fits best?

- **A.** Optimized Row Columnar (ORC) stripe format
- **B.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)
- **C.** Treemap (or pie/donut chart for small category counts) showing part-to-whole proportions
- **D.** Matrix visual (cross-tabbed rows/columns with stepped drill-down subtotals) or Azure Map (geospatial coordinates)

### 99. A port operations manager wants to compare average crane moves per hour side by side across 14 container terminals sorted from highest to lowest productivity. Which Power BI visual compares discrete categories most clearly?

- **A.** Bar or column chart (comparing discrete categorical values across items)
- **B.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)
- **C.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **D.** Apache Avro row-based binary format with JSON schema

### 100. On NordGrid's sustainability dashboard, the board wants one headline tile displaying `Renewable Generation Share (74.6%)`, monthly trend background, and green status against the `72.0%` annual target. Which Power BI visual is designed for this?

- **A.** Apache Parquet columnar storage format
- **B.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)
- **C.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **D.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)

---

## Answer Key and Explanations

### Question 1 — `B` (Describe core data concepts)

Correct answer: B (is correct). Container tariff rows stored in fixed, strictly typed SQL table columns represent structured data. [Skill 1.1: Describe the features of structured data | Source: Explore core data concepts — Identify data formats (structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **B:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **C:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **D:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.

### Question 2 — `D` (Describe core data concepts)

Correct answer: D (is correct). Fixed tabular schemas with predefined column names and enforced data types are structured data. [Skill 1.1: Describe the features of structured data | Source: Explore core data concepts — Identify data formats (structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **B:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **C:** Incorrect. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **D:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.

### Question 3 — `A, D` (Describe core data concepts)

Correct answers: A and D (are correct). Variable per-container fields inside nested `{}` key-value objects represent semi-structured JSON data. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Correct. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Correct. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **E:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.

### Question 4 — `A` (Describe core data concepts)

Correct answer: A (is correct). Hierarchical self-describing tags without a fixed tabular column matrix define semi-structured data. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Correct. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **B:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **C:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **D:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.

### Question 5 — `A` (Describe core data concepts)

Correct answer: A (is correct). Apache Avro combines compact row-based binary serialization with an embedded JSON schema header. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Correct. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Incorrect. Bar and column charts use aligned bar lengths to compare magnitudes accurately across discrete categories such as product lines or regions.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 6 — `D` (Describe core data concepts)

Correct answer: D (is correct). Raw photos, videos, and audio files lack a predefined row or key-tag schema and are unstructured data. [Skill 1.3: Describe the features of unstructured data | Source: Explore core data concepts — Identify data formats (unstructured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **B:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **C:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **D:** Correct. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.

### Question 7 — `A` (Describe core data concepts)

Correct answer: A (is correct). Scanned PDF documents and PNG images are raw binary files classified as unstructured data. [Skill 1.3: Describe the features of unstructured data | Source: Explore core data concepts — Identify data formats (unstructured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Correct. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **B:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **C:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **D:** Incorrect. A composite key combines two or more columns (such as `OrderID` + `ProductID`) to uniquely identify rows in a junction or line-item table.

### Question 8 — `A, B` (Describe core data concepts)

Correct answers: A and B (are correct). Apache Parquet and ORC store data in compressed columnar chunks/stripes, enabling selective column projection in analytics. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Correct. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **B:** Correct. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.
- **C:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **E:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 9 — `D` (Describe core data concepts)

Correct answer: D (is correct). Comma-separated plain-text rows represent the delimited CSV format. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **B:** Incorrect. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.
- **C:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **D:** Correct. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 10 — `C` (Describe core data concepts)

Correct answer: C (is correct). JSON encodes hierarchical key-value pairs and nested arrays across REST APIs. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **B:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **C:** Correct. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 11 — `B, E` (Describe core data concepts)

Correct answers: B and E (are correct). Key-value stores handle rapid single-key lookups, while column-family stores scale wide-column time-series writes. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **B:** Correct. A column-family database groups related columns into families keyed by row and partition keys (such as Apache Cassandra or HBase) for massive write throughput.
- **C:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **D:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **E:** Correct. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.

### Question 12 — `B` (Describe core data concepts)

Correct answer: B (is correct). Graph databases store vertices and edges to run fast multi-hop network and route traversals. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Correct. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **C:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **D:** Incorrect. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.

### Question 13 — `D` (Describe core data concepts)

Correct answer: D (is correct). Document databases store and index self-contained JSON/BSON documents with flexible nested schemas. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **B:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **C:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **D:** Correct. A document database stores self-contained JSON/BSON documents indexed across nested attributes so each entity can evolve fields without schema migrations.

### Question 14 — `D` (Describe core data concepts)

Correct answer: D (is correct). Live ACID bookings commit in Azure SQL Database, Data Factory extracts history to ADLS Gen2 / OneLake Parquet, and Power BI visuals query star schemas. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Incorrect. Archive blobs are offline and unreadable for live OLTP writes, Power BI Desktop is an authoring tool rather than an OLTP engine, and Table storage is schemaless key-value.
- **B:** Incorrect. Paginated reports render formatted output rather than ingesting transactions, and Blob Cold tier does not execute multi-row ACID relational transactions.
- **C:** Incorrect. Power BI Service is a read-optimized BI platform rather than a transactional database, and Queue storage buffers small messages rather than archiving relational rows.
- **D:** Correct. Operational transactions commit in an ACID relational store first, pipelines land history in columnar lake storage, and analytical models serve BI reports without taxing OLTP.

### Question 15 — `B` (Describe core data concepts)

Correct answer: B (is correct). Microsoft OneLake is Fabric's unified tenant-wide SaaS data lake supporting Delta Parquet and zero-copy Shortcuts. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Correct. OneLake is Microsoft Fabric’s unified ADLS Gen2-compatible logical data lake that stores Delta Parquet data once and shares it via zero-copy Shortcuts across workloads.
- **C:** Incorrect. Azure Queue storage holds small asynchronous work messages (up to 64 KB per message), not multi-gigabyte binary files.
- **D:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.

### Question 16 — `B` (Describe core data concepts)

Correct answer: B (is correct). Azure Files provides managed SMB 3.0 and NFS 4.1 cloud file shares mountable via standard UNC paths. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 17 — `C, D, F` (Describe core data concepts)

Correct answers: C, D, and F (are correct). Live booking reservation is an OLTP workload relying on ACID Atomicity (all-or-nothing rollback) and Isolation (concurrent transaction safety). [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **B:** Incorrect. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **C:** Correct. Atomicity guarantees that every statement in a transaction either succeeds together or rolls back completely if any step fails, preventing half-completed transfers.
- **D:** Correct. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **E:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **F:** Correct. Isolation prevents concurrent in-flight transactions from reading uncommitted intermediate edits or overwriting each other unpredictably via locking or row versioning.

### Question 18 — `B` (Describe core data concepts)

Correct answer: B (is correct). Durability guarantees committed transactions are persisted to non-volatile logs/storage and survive crashes. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **B:** Correct. Durability guarantees that once a transaction commits, its changes are persisted to non-volatile transaction logs/storage and survive power loss or crash recovery.
- **C:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **D:** Incorrect. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.

### Question 19 — `A` (Describe core data concepts)

Correct answer: A (is correct). Consistency ensures every transaction transitions the database from one valid constraint-compliant state to another. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Correct. Consistency ensures a transaction transitions the database only from one valid rule-compliant state (keys, check constraints, types) to another.
- **B:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.
- **C:** Incorrect. Denormalized historical scans belong in an OLAP store; live checkout requires normalized OLTP tables with ACID guarantees to prevent lost or corrupted orders.
- **D:** Incorrect. The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.

### Question 20 — `B, D` (Describe core data concepts)

Correct answers: B and D (are correct). Multi-year historical aggregation is an OLAP workload, and a central numeric fact table with single-hop dimensions is a star schema. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Incorrect. Atomicity guarantees that every statement in a transaction either succeeds together or rolls back completely if any step fails, preventing half-completed transfers.
- **B:** Correct. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **C:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **D:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **E:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 21 — `A` (Describe core data concepts)

Correct answer: A (is correct). Read-intensive historical aggregations isolated from live operational transactions define an OLAP workload. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Correct. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **B:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **C:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **D:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.

### Question 22 — `C` (Describe core data concepts)

Correct answer: C (is correct). Normalizing dimension hierarchies into chained parent lookup tables around a fact table defines a snowflake schema. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **B:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **C:** Correct. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 23 — `B` (Describe core data concepts)

Correct answer: B (is correct). Yes — operational database security, HA/DR backup recovery, and query/index maintenance are core DBA duties. [Skill 1.9: Describe responsibilities for database administrators | Source: Explore data roles and services — Database administrator responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **B:** Correct. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **C:** Incorrect. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.
- **D:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.

### Question 24 — `A` (Describe core data concepts)

Correct answer: A (is correct). Capacity scaling, lock resolution, and HA failover governance on database engines belong to the database administrator (DBA). [Skill 1.9: Describe responsibilities for database administrators | Source: Explore data roles and services — Database administrator responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Correct. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **B:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **C:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **D:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.

### Question 25 — `D` (Describe core data concepts)

Correct answer: D (is correct). The DBA secures operational SQL, the data engineer builds ELT pipelines and Gold star tables in Fabric, and the data analyst models DAX KPIs and Power BI visuals. [Skill 1.10: Describe responsibilities for data engineers | Source: Explore data roles and services — Data engineer responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. KPI scorecards and sales packs are data analyst outputs, whereas Spark streaming pipelines belong to data engineers and OLTP index maintenance belongs to DBAs.
- **B:** Incorrect. Operational DB security and PITR restores are DBA duties, network/pipeline plumbing belongs to infra/data engineering, and analysts focus on semantic models and visuals.
- **C:** Incorrect. Cluster HA belongs to the DBA, Spark ELT pipelines belong to the data engineer, and visual storytelling/app distribution belongs to the data analyst.
- **D:** Correct. DBAs govern operational database engines, data engineers build ingestion/transformation pipelines into curated analytical stores, and data analysts model KPIs and visual reports.

### Question 26 — `B` (Describe core data concepts)

Correct answer: B (is correct). Data engineers design, build, and monitor batch and streaming ingestion/transformation pipelines into analytical stores. [Skill 1.10: Describe responsibilities for data engineers | Source: Explore data roles and services — Data engineer responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **B:** Correct. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **C:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **D:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.

### Question 27 — `C` (Describe core data concepts)

Correct answer: C (is correct). Data analysts model semantic metrics and design interactive Power BI reports and dashboards for business stakeholders. [Skill 1.11: Describe responsibilities for data analysts | Source: Explore data roles and services — Data analyst responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **B:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **C:** Correct. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **D:** Incorrect. Azure Migrate discovers on-premises SQL Server instances, evaluates feature compatibility blockers, and recommends right-sized Azure SQL targets (replacing retired DMA).

### Question 28 — `C` (Describe core data concepts)

Correct answer: C (is correct). Building semantic KPI calculations and visual analytical reports defines the data analyst role. [Skill 1.11: Describe responsibilities for data analysts | Source: Explore data roles and services — Data analyst responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **B:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **C:** Correct. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 29 — `A, C` (Identify considerations for relational data on Azure)

Correct answers: A and C (are correct). `ContainerISO` is a single-column primary key, and `(VoyageID, ContainerISO)` is a multi-column composite key. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Correct. A composite key combines two or more columns (such as `OrderID` + `ProductID`) to uniquely identify rows in a junction or line-item table.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Correct. A primary key uniquely identifies each row in a relational table and implicitly forbids `NULL` and duplicate key values.
- **D:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **E:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).

### Question 30 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). A foreign key constraint ensures every child reference matches a valid primary/unique key in the parent table. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Correct. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.
- **B:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **C:** Incorrect. A primary key uniquely identifies each row in a relational table and implicitly forbids `NULL` and duplicate key values.
- **D:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.

### Question 31 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Relational tables enforce structured schemas with strict column data types and nullability constraints on every row. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **B:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **C:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.

### Question 32 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). A primary key constraint enforces row uniqueness and `NOT NULL` across the table. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Correct. A primary key uniquely identifies each row in a relational table and implicitly forbids `NULL` and duplicate key values.
- **B:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **C:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.
- **D:** Incorrect. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.

### Question 33 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Turbine work-order normalization starts with 1NF atomic columns and a primary key, then 2NF full composite-key dependency, and finally 3NF lookup extraction. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. Copying supplier attributes into invoice items creates transitive redundancy, and pipe-delimited multi-value strings violate 1NF.
- **B:** Incorrect. Foreign keys require atomic primary keys first, and 1NF eliminates repeating groups rather than creating them.
- **C:** Incorrect. You cannot achieve 3NF before 1NF/2NF, comma-separated lists violate 1NF atomicity, and duplicating addresses reintroduces update anomalies.
- **D:** Correct. Normalization progresses sequentially: 1NF enforces atomic values and row uniqueness, 2NF removes partial dependencies on composite keys, and 3NF eliminates transitive non-key dependencies.

### Question 34 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). First Normal Form (1NF) requires every cell to hold a single atomic value with no repeating groups. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Correct. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **B:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **C:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **D:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.

### Question 35 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Removing partial functional dependencies on part of a composite primary key achieves Second Normal Form (2NF). [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **B:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **C:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **D:** Correct. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.

### Question 36 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Third Normal Form (3NF) eliminates transitive dependencies between non-key attributes. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **B:** Incorrect. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.
- **C:** Correct. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **D:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).

### Question 37 — `D, E, F` (Identify considerations for relational data on Azure)

Correct answers: D, E, and F (are correct). `ALTER TABLE` is DDL, `UPDATE` is DML, and `GRANT` is DCL. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **B:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **C:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **D:** Correct. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **E:** Correct. DML statements query, add, modify, or delete row data stored inside relational tables.
- **F:** Correct. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.

### Question 38 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). An `INNER JOIN` returns only rows whose join keys match in both tables. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **B:** Incorrect. `LEFT OUTER JOIN` keeps every row from the left table (for example, all customers) and fills `NULL` for right-table columns when no related order exists.
- **C:** Correct. `INNER JOIN` returns only row pairs whose join predicate matches in both the left and right tables, excluding unmatched rows.
- **D:** Incorrect. Granting and revoking security permissions belongs to DCL (`GRANT`, `REVOKE`, `DENY`), not DML.

### Question 39 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Yes — `WHERE` filters individual rows (`CargoType`, `BookingYear`) before `GROUP BY`, while `HAVING` filters grouped `SUM(TEU)` aggregates (`____` pattern rule). [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **B:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **C:** Correct. `WHERE` predicates evaluate individual source rows prior to aggregation, whereas `HAVING` filters grouped summary results such as `HAVING COUNT(*) > 5`.
- **D:** Incorrect. SQL `WHERE` evaluates individual pre-grouped rows and rejects aggregate functions; group-level aggregate filters belong in the `HAVING` clause.

### Question 40 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Adding, modifying, deleting, and querying table rows (`INSERT`, `UPDATE`, `DELETE`, `SELECT`) belong to Data Manipulation Language (DML). [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Correct. DML statements query, add, modify, or delete row data stored inside relational tables.
- **B:** Incorrect. Granting and revoking security permissions belongs to DCL (`GRANT`, `REVOKE`, `DENY`), not DML.
- **C:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **D:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.

### Question 41 — `A, B` (Identify considerations for relational data on Azure)

Correct answers: A and B (are correct). One clustered index governs physical row storage order, and multiple nonclustered indexes support secondary key lookups. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Correct. A nonclustered index maintains a separate sorted key structure pointing back to the base table rows, accelerating selective lookups on non-primary search columns.
- **B:** Correct. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **C:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **D:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **E:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).

### Question 42 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). A stored procedure encapsulates parameterized SQL statements and business logic executed via `EXEC` on the server. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **B:** Incorrect. A nonclustered index maintains a separate sorted key structure pointing back to the base table rows, accelerating selective lookups on non-primary search columns.
- **C:** Correct. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 43 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). A database view encapsulates a saved `SELECT` query as a virtual table that hides underlying join complexity and sensitive columns. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Correct. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **B:** Incorrect. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.
- **C:** Incorrect. Because a clustered index dictates the single physical leaf-level storage order of the table’s rows, a table can have at most one clustered index (plus multiple nonclustered indexes).
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 44 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). At most one clustered index can exist per table because table rows can only be physically sorted on disk in one order. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **C:** Correct. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **D:** Incorrect. Because a clustered index dictates the single physical leaf-level storage order of the table’s rows, a table can have at most one clustered index (plus multiple nonclustered indexes).

### Question 45 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Assess readiness and SKU sizing in Azure Migrate first, choose Azure SQL Database or Managed Instance, provision with Entra/TLS security, and migrate data before cutover. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Queue storage is not a relational migration vehicle, SQL Managed Instance requires VNet subnet sizing upfront, and removing primary keys corrupts relational integrity.
- **B:** Correct. Azure Migrate discovers workloads, flags compatibility blockers, and recommends right-sized Azure SQL targets before secure provisioning, data sync, and connection cutover.
- **C:** Incorrect. Azure Table storage cannot mount `.mdf` database files, and single Azure SQL Database does not host SQL Server Agent or cross-database instance queries.
- **D:** Incorrect. Cutting over before data migration breaks production, opening all public IPs violates security, and assessments must run before selecting the target SKU.

### Question 46 — `A, E` (Identify considerations for relational data on Azure)

Correct answers: A and E (are correct). Azure SQL Database suits cloud-native single/serverless DBs, and Azure SQL Managed Instance provides PaaS SQL Agent and cross-database compatibility. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Correct. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **D:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **E:** Correct. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.

### Question 47 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). An Azure SQL Database Elastic Pool shares compute resources across multiple databases with staggered demand spikes. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Single Azure SQL Database is database-scoped and does not include SQL Server Agent or cross-database instance queries; those require SQL Managed Instance or SQL Server on Azure VMs.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Correct. An Elastic Pool shares a pool of compute resources across multiple single databases that have unpredictable, staggered usage spikes to optimize cost.
- **D:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.

### Question 48 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). SQL Server on Azure Virtual Machines (IaaS) provides full control over the guest OS, exact SQL Server version, and host-level drivers. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.
- **B:** Incorrect. The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.
- **C:** Correct. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **D:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.

### Question 49 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Yes — Azure Migrate (and the Azure SQL Migration extension) replaced retired DMA for SQL Server discovery, readiness, and SKU sizing. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **B:** Incorrect. Microsoft retired Data Migration Assistant (DMA) in July 2025; Azure Migrate and the Azure SQL Migration extension handle SQL discovery, assessment, and right-sizing.
- **C:** Correct. Azure Migrate discovers on-premises SQL Server instances, evaluates feature compatibility blockers, and recommends right-sized Azure SQL targets (replacing retired DMA).
- **D:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.

### Question 50 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Azure Database for MySQL — Flexible Server hosts LAMP shipment portals on managed MySQL Community Edition PaaS with HA, TLS, and up to 35-day PITR. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Correct. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.
- **B:** Incorrect. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **C:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **D:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.

### Question 51 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Azure Database for PostgreSQL — Flexible Server supports object-relational custom/spatial types, extensions, `PL/pgSQL`, and `pgAdmin`. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **C:** Correct. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **D:** Incorrect. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.

### Question 52 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Azure Database for MySQL — Flexible Server provides stop/start compute controls, granular server parameters, and 12-month Azure free-account eligibility. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Incorrect. Azure Stream Analytics runs declarative Stream Analytics Query Language (`SELECT ... GROUP BY TumblingWindow(...)`) jobs joining live streams with reference data into sinks.
- **B:** Correct. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.
- **C:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **D:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.

### Question 53 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Lifecycle rules age blobs automatically from Hot -> Cool (>=30d) -> Cold (>=90d) -> offline Archive (>=180d, rehydrating when audited). [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Table storage entities hold small key-value properties rather than large video files, and Cool/Cold tiers remain online with immediate millisecond read access.
- **B:** Correct. Lifecycle management policies automatically age blobs from lowest-read-cost Hot through Cool and Cold down to lowest-storage-cost offline Archive.
- **C:** Incorrect. Blob tiers are object storage rather than SMB shares, Archive rather than Hot minimizes 1-year retention storage cost, and Hot blobs require no rehydration.
- **D:** Incorrect. Archive tier is offline and cannot serve direct reads until rehydrated to Hot or Cool, which takes hours.

### Question 54 — `A, C` (Describe considerations for working with non-relational data on Azure)

Correct answers: A and C (are correct). Cool tier (30-day minimum) and Cold tier (90-day minimum) both keep blobs online with immediate millisecond access at progressively lower storage rates. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Correct. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Correct. The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.
- **D:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **E:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 55 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Block blobs store discrete files, media, and big-data objects uploaded as independent blocks. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Correct. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.
- **C:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **D:** Incorrect. Archive tier blobs are stored offline and cannot be read directly until rehydrated to Hot or Cool, which takes hours.

### Question 56 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Data Lake Storage (ADLS) Gen2 adds true hierarchical folder operations and POSIX ACLs atop Azure Blob Storage. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Correct. ADLS Gen2 adds a true POSIX-ACL directory hierarchy and atomic folder rename/delete operations atop Azure Blob Storage for big-data analytics engines.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.

### Question 57 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Blobs in the offline Archive tier cannot be read directly until rehydrated to an online tier (Hot or Cool). [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.
- **B:** Incorrect. The Hot tier is online storage optimized for data that is accessed or modified frequently, carrying the lowest transaction/read cost.
- **C:** Incorrect. Archive tier blobs are stored offline and cannot be read directly until rehydrated to Hot or Cool, which takes hours.
- **D:** Correct. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 58 — `A, B` (Describe considerations for working with non-relational data on Azure)

Correct answers: A and B (are correct). Azure Files provides managed SMB/NFS cloud shares, and Azure File Sync caches active files on Windows Servers with cloud tiering. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Correct. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **B:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **D:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **E:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.

### Question 59 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Files supports both `SMB 3.0` and `NFS 4.1` managed cloud file shares. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **D:** Incorrect. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.

### Question 60 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Yes — Azure File Sync caches active Azure Files shares locally on Windows Servers and syncs changes bi-directionally. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Incorrect. Spark Structured Streaming treats a live event stream as an unbounded table processed via familiar Spark SQL/DataFrame APIs with checkpointed exactly-once guarantees.
- **B:** Correct. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **C:** Incorrect. ADLS Gen2 adds a true POSIX-ACL directory hierarchy and atomic folder rename/delete operations atop Azure Blob Storage for big-data analytics engines.
- **D:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.

### Question 61 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Table storage stores schemaless property-bag entities indexed by `PartitionKey` and `RowKey`. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. Azure Table storage is a schemaless key-value store indexed only by `PartitionKey` and `RowKey` with no foreign keys or server-side table joins.
- **B:** Correct. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 62 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). `PartitionKey` defines logical partition placement for scale-out, and `RowKey` provides unique ordering within that partition. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **B:** Incorrect. Azure Table storage is a schemaless key-value store indexed only by `PartitionKey` and `RowKey` with no foreign keys or server-side table joins.
- **C:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **D:** Correct. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 63 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Azure Cosmos DB for Table preserves the Table SDK data model while adding global distribution, secondary indexing, and millisecond SLAs. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Correct. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **D:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.

### Question 64 — `C, D` (Describe considerations for working with non-relational data on Azure)

Correct answers: C and D (are correct). Turnkey multi-region global distribution with `<10 ms` SLAs and Request Unit (`RU/s`) autoscale throughput are core Cosmos DB capabilities. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **B:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **C:** Correct. Cosmos DB measures CPU, memory, and IOPS per database operation in Request Units (RUs), billed via Provisioned/Autoscale RU/s or consumption-based Serverless.
- **D:** Correct. Azure Cosmos DB replicates data transparently across selected Azure regions with financially backed 99.999% availability and single-digit millisecond read/write latency.
- **E:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 65 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Cosmos DB defaults to Session consistency so each customs broker session immediately sees its own committed updates in monotonic order. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Correct. Session consistency is Cosmos DB’s default level, balancing low latency and throughput while guaranteeing each user session immediately sees its own writes in order.
- **B:** Incorrect. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.
- **C:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.
- **D:** Incorrect. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.

### Question 66 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Strong consistency guarantees linearizable reads returning the latest globally committed write. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.
- **B:** Incorrect. Session consistency is Cosmos DB’s default level, balancing low latency and throughput while guaranteeing each user session immediately sees its own writes in order.
- **C:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **D:** Correct. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.

### Question 67 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Eventual consistency provides the lowest RU cost and write latency when temporary replica convergence lag is acceptable. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **C:** Incorrect. Isolation prevents concurrent in-flight transactions from reading uncommitted intermediate edits or overwriting each other unpredictably via locking or row versioning.
- **D:** Correct. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.

### Question 68 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Choose the API at account creation, create the database and `/feederId` container, set RU/s or serverless + consistency, and run partition-scoped queries. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Every Cosmos DB container requires a partition key, the API is fixed per account, Cosmos DB does not enforce cross-container foreign keys, and item size is capped at 2 MB.
- **B:** Correct. API selection happens at account creation, partition key design happens at container creation to distribute storage/RU evenly, and partition-scoped queries avoid cross-partition fan-out.
- **C:** Incorrect. Cosmos DB sits under an account -> database -> container -> item hierarchy, not SMB shares or subscription tags.
- **D:** Incorrect. Cosmos DB is fully managed PaaS with no OS patching, a single-value partition key creates a 20 GB logical-partition bottleneck, and triggers/sprocs use JavaScript rather than T-SQL.

### Question 69 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Azure Cosmos DB for NoSQL is Microsoft's native JSON document API queried with SQL `SELECT` syntax. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **B:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **C:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.
- **D:** Correct. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.

### Question 70 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Cosmos DB for Apache Gremlin models property-graph vertices and directed edges traversed with Gremlin queries. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **B:** Correct. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **C:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.
- **D:** Incorrect. Cosmos DB for MongoDB lets existing MongoDB drivers and tools store BSON documents in Cosmos DB simply by updating the connection string.

### Question 71 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Cosmos DB for Apache Cassandra provides wire compatibility for CQL wide-column applications. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **B:** Correct. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **C:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **D:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.

### Question 72 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Cosmos DB for MongoDB provides wire-protocol compatibility so existing BSON MongoDB apps migrate via connection string. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Correct. Cosmos DB for MongoDB lets existing MongoDB drivers and tools store BSON documents in Cosmos DB simply by updating the connection string.
- **C:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **D:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.

### Question 73 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Pipelines land raw logistics/SCADA files in OneLake Bronze, Spark/SQL cleanses Silver Delta tables, and Gold star-schema tables feed BI. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Correct. Modern ELT lands raw data in scalable lake storage first, then leverages cloud compute to cleanse Silver tables and publish Gold star schemas for analytics.
- **B:** Incorrect. Skipping cleansing degrades report accuracy, deleting raw Bronze files prevents replayability, and Gold analytical layers favor denormalized star schemas over 3NF.
- **C:** Incorrect. ELT executes transformations in scalable cloud engines rather than client laptops, and Archive blobs/Queues cannot back live BI queries.
- **D:** Incorrect. Analytical ingestion is read-only against operational sources and builds Bronze -> Silver -> Gold sequentially.

### Question 74 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Loading raw data into scalable lake storage first and transforming in place with cloud compute defines ELT. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Correct. ELT extracts raw source data, loads it directly into scalable lake/warehouse storage, and runs distributed cloud compute (Spark or SQL) to cleanse and model in place.
- **C:** Incorrect. ETL transforms, scrubs, or redacts sensitive fields in an intermediate processing engine prior to loading only the conformed structure into the target analytical store.
- **D:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.

### Question 75 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Azure Data Factory (and Data Factory in Microsoft Fabric) orchestrates Copy pipelines and Dataflows Gen2. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **C:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **D:** Correct. Data Factory orchestrates code-free data movement (90+ connectors via Copy activity) and visual Power Query transformations (Dataflows Gen2) or Spark/Mapping Data Flows.

### Question 76 — `A, C` (Describe an analytics workload on Azure)

Correct answers: A and C (are correct). Delta Lake ACID tables over open Parquet implement a data lakehouse, and single-hop dimensions around `FactGenerationMWh` form a star schema. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Correct. A lakehouse combines the low-cost open file flexibility of a data lake with ACID transactions, schema enforcement, and SQL warehouse performance via Delta Lake tables.
- **B:** Incorrect. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.
- **C:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **E:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.

### Question 77 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Star schemas place descriptive filter/group attributes in dimensions and additive numeric measurements in the central fact table for fast BI aggregations. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **C:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 78 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). A data lakehouse combines data-lake file openness and scale with data-warehouse ACID reliability and SQL performance. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **B:** Correct. A lakehouse combines the low-cost open file flexibility of a data lake with ACID transactions, schema enforcement, and SQL warehouse performance via Delta Lake tables.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 79 — `C, D, E` (Describe an analytics workload on Azure)

Correct answers: C, D, and E (are correct). Microsoft Fabric, Azure Databricks, and Azure HDInsight match those three large-scale analytics offerings. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Correct. Azure Databricks provides managed Apache Spark clusters, collaborative Python/SQL/Scala/R notebooks, Unity Catalog governance, and Delta Lake processing on Azure.
- **D:** Correct. Azure HDInsight provisions managed clusters of open-source Apache big-data frameworks when lift-and-shift Hadoop/Hive/HBase/Kafka compatibility is required.
- **E:** Correct. Microsoft Fabric unifies Data Factory, Data Engineering, Data Warehouse, Data Science, Real-Time Intelligence, and Power BI in one SaaS workspace sharing OneLake Delta tables.
- **F:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.

### Question 80 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Microsoft Fabric unifies Lakehouse, Warehouse, Data Factory, Real-Time Intelligence, and Power BI over OneLake. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Correct. Microsoft Fabric unifies Data Factory, Data Engineering, Data Warehouse, Data Science, Real-Time Intelligence, and Power BI in one SaaS workspace sharing OneLake Delta tables.
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 81 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Azure Synapse Analytics combines serverless SQL pools, dedicated MPP SQL pools, Apache Spark pools, and pipelines. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Correct. Azure Synapse Analytics integrates serverless SQL on-demand lake querying, dedicated MPP SQL warehousing, Apache Spark pools, and Synapse Pipelines in Synapse Studio.
- **D:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.

### Question 82 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Azure Databricks provides managed Apache Spark clusters, collaborative notebooks, Delta Lake optimization, and MLflow. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Correct. Azure Databricks provides managed Apache Spark clusters, collaborative Python/SQL/Scala/R notebooks, Unity Catalog governance, and Delta Lake processing on Azure.
- **D:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 83 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). A tumbling window divides time into fixed-size, contiguous, non-overlapping intervals. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **B:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **C:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **D:** Correct. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.

### Question 84 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). A hopping window advances a fixed-duration window forward by a shorter hop interval, creating scheduled overlapping windows. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Correct. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **B:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **C:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **D:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.

### Question 85 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). A session window groups activity bursts dynamically and closes after a configured inactivity gap elapses. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **B:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **C:** Correct. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **D:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.

### Question 86 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Scheduled processing over bounded sets of accumulated historical records defines batch processing. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Correct. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **B:** Incorrect. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **C:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **D:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.

### Question 87 — `D, E` (Describe an analytics workload on Azure)

Correct answers: D and E (are correct). Workload 1 is Microsoft Fabric Real-Time Intelligence, and Workload 2 is Apache Spark Structured Streaming. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **B:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **C:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **D:** Correct. Spark Structured Streaming treats a live event stream as an unbounded table processed via familiar Spark SQL/DataFrame APIs with checkpointed exactly-once guarantees.
- **E:** Correct. Fabric Real-Time Intelligence ingests and routes events via Eventstream, indexes high-volume telemetry in Eventhouse KQL databases, visualizes live tiles, and triggers Activator alerts.

### Question 88 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Azure Event Hubs ingests hundreds of thousands of partitioned inverter packets per second over AMQP and Kafka endpoints for downstream analytics. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Correct. Azure Event Hubs ingests millions of telemetry events per second into partitioned append logs (supporting native AMQP/HTTPS and Apache Kafka producers) for downstream stream consumers.

### Question 89 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Azure Stream Analytics runs serverless SQL-like streaming queries with built-in windowing functions. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Correct. Azure Stream Analytics runs declarative Stream Analytics Query Language (`SELECT ... GROUP BY TumblingWindow(...)`) jobs joining live streams with reference data into sinks.
- **B:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **C:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **D:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.

### Question 90 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Continuous low-latency evaluation of unbounded event streams in motion defines stream processing. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **B:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **C:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **D:** Correct. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.

### Question 91 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Analysts shape Gold tables and author DAX reports in Power BI Desktop, publish to Power BI Service, pin boardroom dashboard tiles with scheduled refresh, and share an App. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Correct. Power BI Desktop handles Power Query prep, semantic modeling, and report design, while Power BI Service hosts scheduled refresh, multi-report dashboards, and governed App distribution.
- **B:** Incorrect. Dashboards are created in Power BI Service rather than Power BI Mobile, and dataset refresh plus secure sharing are managed in Power BI Service workspaces.
- **C:** Incorrect. Dashboards exist only in Power BI Service (not Power BI Desktop), Power BI Mobile is for consumption, and viewers consume shared Apps/reports in browser or mobile.
- **D:** Incorrect. Paginated `.rdl` reports are authored in Power BI Report Builder, Stream Analytics processes event streams, and port `1433` is SQL Server TDS rather than BI sharing.

### Question 92 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Yes — Power BI Desktop is the local authoring tool for Power Query data prep, semantic modeling, DAX, and interactive `.pbix` report design. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **B:** Incorrect. Dashboards with pinned tiles across multiple reports are a cloud-only feature of Power BI Service, not Power BI Desktop.
- **C:** Incorrect. Power BI Service (`app.powerbi.com` / Fabric) hosts published semantic models and reports, pins cross-report dashboard tiles, schedules gateway refreshes, and distributes governed Apps.
- **D:** Correct. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.

### Question 93 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Power BI Report Builder creates fixed-layout paginated (`.rdl`) reports built for multi-page printing and exact PDF pagination. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **B:** Incorrect. Azure Event Hubs ingests millions of telemetry events per second into partitioned append logs (supporting native AMQP/HTTPS and Apache Kafka producers) for downstream stream consumers.
- **C:** Incorrect. Power BI Service (`app.powerbi.com` / Fabric) hosts published semantic models and reports, pins cross-report dashboard tiles, schedules gateway refreshes, and distributes governed Apps.
- **D:** Correct. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 94 — `B, D` (Describe an analytics workload on Azure)

Correct answers: B and D (are correct). `1:*` relationships and hierarchies live in the Power BI semantic model, and `Fleet Utilization %` is a dynamic DAX measure. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Correct. A Power BI semantic model defines `1:*` star-schema relationships, reusable DAX measures, drill-down hierarchies, and column metadata consumed across reports.
- **C:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **D:** Correct. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **E:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.

### Question 95 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). A DAX measure evaluates aggregations dynamically at query time within the active report filter context. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Correct. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **B:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **C:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 96 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Storage modes, relationships, hierarchies, and column formatting are governed in the Power BI semantic model. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **C:** Correct. A Power BI semantic model defines `1:*` star-schema relationships, reusable DAX measures, drill-down hierarchies, and column metadata consumed across reports.
- **D:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.

### Question 97 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Yes — Microsoft Learn recommends star-schema modeling (`1:*` dimensions filtering fact tables) for clarity, accuracy, and performance in Power BI. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **D:** Incorrect. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.

### Question 98 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). An Azure Map visual plots latitude/longitude geospatial coordinates interactively with bubble size and color encoding. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Incorrect. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.
- **B:** Incorrect. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.
- **C:** Incorrect. Pie/donut charts show part-to-whole shares for a few slices, while treemaps use nested rectangles to display proportional composition across larger hierarchical categories.
- **D:** Correct. A Matrix aggregates measures across both row and column hierarchies like a pivot table, whereas Azure/Filled Maps plot spatial latitude/longitude or regional boundaries.

### Question 99 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). A bar or column chart compares values cleanly across discrete categories using aligned bar lengths. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Correct. Bar and column charts use aligned bar lengths to compare magnitudes accurately across discrete categories such as product lines or regions.
- **B:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
- **C:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **D:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.

### Question 100 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). A KPI visual displays a headline indicator metric with its trend axis and status against a target goal. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **B:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
- **C:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **D:** Correct. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.
