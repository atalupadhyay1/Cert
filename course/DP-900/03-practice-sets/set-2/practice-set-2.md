# Microsoft Exam DP-900: Microsoft Azure Data Fundamentals — Full-Length Mock Exam 2

**Theme:** Healthcare Clinical & Patient Telemetry — Normalization, SQL Managed Instance, Blob Tiers, Fabric RTI & Paginated Reports  
**Credential:** `Microsoft Certified: Azure Data Fundamentals` *(Beginner / Fundamentals · **no prerequisite** · **never expires**)*  
**Study guide baseline:** `July 21, 2026` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `75 minutes` (`45 sec/question`, matching live 45-minute / 60-question pace; `45 minutes` optional speed drill · **closed-book**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn documentation — not affiliated with or endorsed by Microsoft Corporation. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Describe core data concepts (25–30% official weight · 28 questions)

### 1. CarePulse Hospitals stores patient appointment bookings in a database table with strictly typed `AppointmentID`, `PatientMRN`, `ClinicCode`, and `ScheduledUTC` columns where every row conforms to the identical schema. This appointment table contains ____.

- **A.** Optimized Row Columnar (ORC) stripe format
- **B.** Structured data
- **C.** Unstructured data
- **D.** Semi-structured data

### 2. A hospital pharmacy tracks controlled medication lot numbers, expiration dates, and tablet counts inside fixed SQL columns enforced by `NOT NULL` and `DATE` data types. Which data representation category applies?

- **A.** Graph database (vertices and directed edges)
- **B.** Unstructured data
- **C.** Structured data
- **D.** JavaScript Object Notation (JSON) document format

### 3. Bedside infusion pumps emit FHIR observation documents where cardiac pumps include nested `bolusRate` arrays and insulin pumps include `basalUnits` keys without sharing a rigid relational column list. Which two items describe these payloads? Select two.

- **A.** Unstructured data
- **B.** Semi-structured data
- **C.** Page blobs in Azure Blob Storage
- **D.** Structured data
- **E.** JavaScript Object Notation (JSON) document format

### 4. An external diagnostics lab sends HL7 XML results containing hierarchical `<Patient>`, `<Order>`, and repeating `<Observation>` tags whose optional child elements vary by lab panel. XML with self-describing tags is ____.

- **A.** Structured data
- **B.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **C.** Unstructured data
- **D.** Semi-structured data

### 5. CarePulse's telemetry gateway serializes wearable ECG event rows in a compact binary format that embeds a JSON schema definition in the file header for downstream Spark consumers. Which file format is this?

- **A.** Delimited text format (CSV or TSV)
- **B.** Page blobs in Azure Blob Storage
- **C.** Apache Avro row-based binary format with JSON schema
- **D.** Bar or column chart (comparing discrete categorical values across items)

### 6. Radiology departments archive chest X-ray `.dcm` bitmaps, endoscopic procedure `.mp4` videos, and dictated physician `.mp3` voice notes in Azure Storage. What kind of data are these clinical media files?

- **A.** Structured data
- **B.** Semi-structured data
- **C.** Unstructured data
- **D.** Apache Parquet columnar storage format

### 7. Scanned handwritten patient consent `.tiff` forms and pathology slide `.png` photographs are uploaded from outpatient clinics into cloud object containers. Which data classification describes these files?

- **A.** Structured data
- **B.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **C.** Unstructured data
- **D.** Composite key (multi-column key)

### 8. CarePulse exchanges small 500-row clinic directory lists with state regulators as human-readable comma-delimited text, while storing 12 billion de-identified lab results in OneLake using compressed columnar files for fast analytics. Which two file formats match these two uses? Select two.

- **A.** Apache Parquet columnar storage format
- **B.** Page blobs in Azure Blob Storage
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** Delimited text format (CSV or TSV)
- **E.** Clustered index (defines physical leaf-level sort order; maximum one per table)

### 9. A clinical population-health query scans only `DiagnosisCode` and `LengthOfStay` across a 90-column, 6-terabyte hospital admissions dataset. Storing the dataset in ____ lets Spark skip reading the other 88 columns completely.

- **A.** JavaScript Object Notation (JSON) document format
- **B.** Append blobs in Azure Blob Storage
- **C.** Delimited text format (CSV or TSV)
- **D.** Apache Parquet columnar storage format

### 10. A legacy healthcare research cluster running Apache Hive stores de-identified claims history in compressed columnar stripes with built-in stripe footer indexes. Which file format is used?

- **A.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **B.** Optimized Row Columnar (ORC) stripe format
- **C.** Page blobs in Azure Blob Storage
- **D.** Delimited text format (CSV or TSV)

### 11. CarePulse needs one non-relational store to index variable nested JSON patient intake questionnaires and a second store to map infectious-disease contact tracing across patients, rooms, and staff (`EXPOSED_TO` edges). Which two database types fit? Select two.

- **A.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Document database
- **D.** Graph database (vertices and directed edges)
- **E.** Delimited text format (CSV or TSV)

### 12. A patient portal microservice looks up temporary SMS verification codes exclusively by `PatientPhoneHash` with sub-millisecond reads and zero relational joins. Which non-relational store model is simplest and fastest here?

- **A.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **B.** Graph database (vertices and directed edges)
- **C.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **D.** Key-value non-relational store

### 13. An ICU telemetry platform ingests continuous vital-sign streams keyed by `DeviceID` with separate `vitals_hr`, `vitals_spo2`, and `alarm_state` column families for high write throughput. Which database category matches this model?

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Column-family (wide-column) database
- **C.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)
- **D.** Database view (saved virtual `SELECT` query)

### 14. CarePulse is designing a cloud data flow from live outpatient billing check-ins through de-identified population analytics in Power BI. Which four-step Azure datastore sequence is architecturally sound?

- **A.** Serve live checkout writes in Power BI Service → Export dashboards to CSV → Load CSVs into Azure SQL Database → Archive active rows to Azure Queue storage
- **B.** Capture OLTP writes directly in Archive Blob tier → Run live checkout queries in Power BI Desktop → Copy rows to Azure Files SMB → Normalize into Azure Table storage
- **C.** Land raw checkout clicks in Paginated Reports → Transform via SMB file locks → Commit ACID transactions in Azure Blob Cold tier → Query via Gremlin graph vertices
- **D.** Capture OLTP writes in Azure SQL Database → Extract changes via Data Factory pipeline → Land Parquet files in ADLS Gen2 / OneLake → Serve star-schema visuals in Power BI

### 15. A legacy PACS medical viewer application on clinic workstations requires mounting a shared `\\clinicshare\templates` network drive over `SMB 3.0`. Which Azure datastore provides managed cloud file shares for this requirement?

- **A.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Store 20 GB CAD engineering drawings inside single Azure Queue storage messages

### 16. CarePulse operates a global telemedicine triage app across North America, Europe, and Asia that requires `<10 ms` JSON document reads and writes with turnkey multi-region replication. Which Azure database capability satisfies this requirement?

- **A.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **B.** Azure Cosmos DB turnkey global distribution with multi-region writes and <10 ms SLAs
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 17. When a hospital pharmacist dispenses a prescription, the system decrements vial stock and records the patient administration in one database transaction that rolls back completely on error and enforces `StockOnHand >= 0`. Which three concepts apply? Select three.

- **A.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **B.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **C.** Atomicity (all-or-nothing transaction unit)
- **D.** Online Analytical Processing (OLAP) workload
- **E.** Consistency (valid schema and constraint state)
- **F.** Online Transaction Processing (OLTP) workload

### 18. Two scheduling clerks simultaneously try to book the last open 09:30 MRI slot; database row locking ensures one clerk completes the booking first rather than both clerks seeing an uncommitted slot state. Which ACID property protects concurrent transactions here?

- **A.** Online Analytical Processing (OLAP) workload
- **B.** Isolation (concurrent transactions do not interfere)
- **C.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **D.** Apache Parquet columnar storage format

### 19. Milliseconds after CarePulse's database confirms `COMMIT` on an emergency allergy alert entry, an unexpected host power fault triggers failover, yet the committed allergy record remains intact upon recovery. Which ACID guarantee ensured this?

- **A.** Durability (committed writes survive restarts or crashes)
- **B.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)
- **C.** Line chart (tracking continuous trends and changes over ordered time intervals)
- **D.** Cool access tier (online, 30-day minimum retention for infrequently accessed data)

### 20. CarePulse's clinical quality team runs monthly read-heavy aggregations across 7 years of inpatient discharges where `DimDiagnosis` normalizes into `DimICDChapter` and `DimClinicalSpecialty`. Which two concepts describe this reporting workload and schema? Select two.

- **A.** Page blobs in Azure Blob Storage
- **B.** Atomicity (all-or-nothing transaction unit)
- **C.** Online Analytical Processing (OLAP) workload
- **D.** Online Transaction Processing (OLTP) workload
- **E.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)

### 21. Proposed solution: Hospital executives want 10-year readmission trend calculations across 200 million historical stays; to protect live EHR response times, the architect offloads those heavy aggregations from the OLTP database to a dedicated ____ store. What completes the architecture?

- **A.** Online Transaction Processing (OLTP) workload
- **B.** Append blobs in Azure Blob Storage
- **C.** Online Analytical Processing (OLAP) workload
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)

### 22. In CarePulse's analytics warehouse, `FactEncounters` holds numeric `ChargeAmount` and `WaitMinutes` alongside foreign keys to flat `DimPatient`, `DimProvider`, and `DimFacility` tables. Which analytical schema design is this?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** First Normal Form (1NF — atomic values and no repeating column groups)
- **C.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **D.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)

### 23. At CarePulse, which data professional manages Transparent Data Encryption (`TDE`), configures Azure SQL Managed Instance failover groups, audits `GRANT`/`DENY` role memberships, and validates 35-day point-in-time backup restores?

- **A.** Data engineer
- **B.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)
- **C.** Database administrator (DBA)
- **D.** Data analyst

### 24. Live EHR queries slow down after a schema patch, so a specialist inspects wait statistics and rebuilds fragmented nonclustered indexes on Azure SQL Managed Instance. Which role performs operational database tuning?

- **A.** Data analyst
- **B.** Data engineer
- **C.** Database administrator (DBA)
- **D.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)

### 25. CarePulse is launching a hospital readmission analytics program spanning Azure SQL, Microsoft Fabric Lakehouse, and Power BI. Which four-step workflow assigns each stage to the right data professional role?

- **A.** DBA provisions & secures operational Azure SQL → Data engineer builds ELT pipelines into Fabric Lakehouse → Data engineer curates Gold star-schema tables → Data analyst models DAX KPIs & publishes Power BI reports
- **B.** Data analyst configures SQL Server failover clusters → DBA authors Spark ELT notebooks in Databricks → Data engineer designs executive Power BI visuals → DBA schedules workspace app audiences
- **C.** DBA designs executive KPI scorecards → Data analyst writes Spark Structured Streaming checkpoints → Data engineer tunes OLTP clustered indexes → DBA publishes paginated sales packs
- **D.** Data engineer grants T-SQL row permissions on OLTP → Data analyst provisions Azure VNet private endpoints → DBA builds Power Query Dataflows Gen2 → Data analyst runs point-in-time DB restores

### 26. Who builds automated Fabric pipelines and PySpark notebooks to ingest nightly HL7 feeds, standardize ICD-10 diagnosis codes, and write partitioned Silver and Gold Delta tables?

- **A.** Database administrator (DBA)
- **B.** Data engineer
- **C.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **D.** Data analyst

### 27. CarePulse's chief nursing officer needs an interactive emergency-department wait-time scorecard with DAX measures and drill-down visuals by shift and triage acuity. Which role designs and publishes this Power BI report?

- **A.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **B.** Data engineer
- **C.** Database administrator (DBA)
- **D.** Data analyst

### 28. A hospital quality specialist connects Power BI Desktop to Gold star-schema tables, creates a `30-Day Readmission Rate %` measure, and configures visual slicers for department heads. Which data role does this work represent?

- **A.** Database administrator (DBA)
- **B.** Data engineer
- **C.** Data analyst
- **D.** Append blobs in Azure Blob Storage

---

## Domain 2 — Identify considerations for relational data on Azure (20–25% official weight · 24 questions)

### 29. In CarePulse's relational database, `Patients` uses single-column `PatientID` to uniquely identify every patient, whereas `PatientAllergies` uses the pair `(PatientID, AllergenCode)` together to ensure the same allergen isn't recorded twice for one patient. Which two key types are used? Select two.

- **A.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **B.** Primary key constraint
- **C.** Unstructured data
- **D.** Composite key (multi-column key)
- **E.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 30. In the `LabOrders` table, column `OrderingPhysicianID` references `Physicians.PhysicianID` so the database rejects any lab order referencing an invalid doctor ID. `OrderingPhysicianID` is a ____.

- **A.** Primary key constraint
- **B.** Apache Avro row-based binary format with JSON schema
- **C.** Foreign key constraint
- **D.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)

### 31. In a relational table, every row represents a single entity instance (tuple) and every column enforces a consistent domain data type such as `INT`, `NVARCHAR(50)`, or `DATETIME2`. What data representation does a relational table implement?

- **A.** Structured data
- **B.** Semi-structured data
- **C.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **D.** Unstructured data

### 32. Proposed solution: A developer proposes allowing `NULL` inside `Clinics.ClinicID` even though `ClinicID` is designated as the table's primary key; the DBA explains that relational engines automatically reject `NULL` in a ____. What completes the explanation?

- **A.** Hot access tier (highest storage rate, lowest read/write access cost)
- **B.** Primary key constraint
- **C.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **D.** Foreign key constraint

### 33. CarePulse is redesigning a flat intake spreadsheet containing multi-valued medication cells and duplicated insurance-carrier addresses into a clean 3NF relational schema. Which four-step normalization sequence is valid?

- **A.** Remove transitive non-key dependencies (3NF) → Merge comma-separated phone lists into one column → Delete all primary keys to speed inserts → Duplicate customer addresses across every order line
- **B.** Split repeating groups into atomic columns (1NF) → Assign a unique primary key → Move partial composite-key dependencies to parent tables (2NF) → Extract transitive non-key dependencies into lookup tables (3NF)
- **C.** Create foreign keys on unsplit multi-value columns → Denormalize all lookup tables into one wide sheet → Remove partial dependencies (2NF) → Split atomic columns into repeating groups (1NF)
- **D.** Cluster-index raw JSON blobs → Delete primary keys on parent tables → Copy supplier city into every invoice item (2NF) → Combine product names into pipe-delimited strings (3NF)

### 34. An `Appointments` staging table has columns `Symptom1`, `Symptom2`, and `Symptom3` plus a `PhoneNumbers` column storing `'555-0101, 555-0199'`. Refactoring into atomic single-valued columns and a child rows table satisfies ____.

- **A.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **B.** First Normal Form (1NF — atomic values and no repeating column groups)
- **C.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **D.** Third Normal Form (3NF — no transitive dependencies between non-key columns)

### 35. A 1NF `PrescriptionItems` table uses composite primary key `(PrescriptionID, DrugNDC)` and includes `DrugGenericName`, which depends solely on `DrugNDC`. Moving `DrugGenericName` into a `Drugs` table achieves ____.

- **A.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **B.** First Normal Form (1NF — atomic values and no repeating column groups)
- **C.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **D.** Star schema (central numeric fact table joined directly to denormalized dimension tables)

### 36. In a 2NF `Wards` table keyed by `WardID`, non-key column `BuildingCode` determines `BuildingAddress`. Moving `BuildingCode -> BuildingAddress` into a `Buildings` lookup table prevents update anomalies and achieves ____.

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Apache Parquet columnar storage format
- **C.** First Normal Form (1NF — atomic values and no repeating column groups)
- **D.** Second Normal Form (2NF — full functional dependency on the entire composite key)

### 37. Match CarePulse's governance audit: `ALTER TABLE Patients ADD PreferredLanguage NVARCHAR(20)` modifies schema, `SELECT MRN, BirthDate FROM Patients WHERE ClinicID = 4` reads rows, and `REVOKE UPDATE ON Patients FROM TempClerks` removes permissions. Which three SQL subsets appear here? Select three.

- **A.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **B.** Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- **C.** JavaScript Object Notation (JSON) document format
- **D.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **E.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **F.** Page blobs in Azure Blob Storage

### 38. CarePulse wants a query returning **only** patients who have at least one matching row in `Admissions`, excluding patients who have never been admitted. Which SQL join clause produces this result?

- **A.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **B.** `INNER JOIN` matching related keys present in both tables
- **C.** Place `SUM()` or `COUNT(*)` aggregate predicates directly inside the SQL `WHERE` clause before `GROUP BY`
- **D.** `LEFT OUTER JOIN` preserving all left-table rows with `NULL` when right-table matches are absent

### 39. Proposed solution: A clinical analyst writes `SELECT ClinicID, COUNT(*) FROM Visits WHERE COUNT(*) > 50 GROUP BY ClinicID;` and receives a SQL syntax error; to fix it, the aggregate filter `COUNT(*) > 50` must move out of `WHERE` into `HAVING`. Why did `WHERE` fail?

- **A.** Place `SUM()` or `COUNT(*)` aggregate predicates directly inside the SQL `WHERE` clause before `GROUP BY`
- **B.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **C.** `WHERE` filters rows before grouping; `HAVING` filters aggregated groups after `GROUP BY`
- **D.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)

### 40. To ensure outpatient receptionists can read `Appointments` but are explicitly blocked from reading `PsychiatryNotes`, the DBA executes `GRANT SELECT` and `DENY SELECT` statements. Which SQL subset do `GRANT`, `REVOKE`, and `DENY` belong to?

- **A.** Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- **B.** Use DML `SELECT` and `INSERT` statements to grant or revoke user login permissions on schemas
- **C.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)

### 41. CarePulse wants two relational database objects: a virtual `SELECT` projection (`vw_PublicProviderDirectory`) hiding clinician home addresses, and a precompiled parameterized routine (`usp_DischargePatient`) updating bed status and billing atomically. Which two objects should be created? Select two.

- **A.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **B.** Database view (saved virtual `SELECT` query)
- **C.** Apache Parquet columnar storage format
- **D.** Stored procedure (parameterized precompiled SQL routine)
- **E.** Append blobs in Azure Blob Storage

### 42. When CarePulse defines a primary key on `LabResults.ResultID` in Azure SQL, SQL Server creates an index by default that physically orders the table's leaf data pages by `ResultID`. This index is a ____.

- **A.** Database view (saved virtual `SELECT` query)
- **B.** Create four separate clustered indexes on the same relational table to sort rows four ways physically
- **C.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **D.** Nonclustered index (separate B-tree structure with row locators; multiple allowed per table)

### 43. Clinicians frequently search `Patients` by `LastName`, `BirthDate`, and `InsuranceMemberID`, even though `Patients` is already clustered on `PatientID`. Which database object speeds up all three search patterns on the same table?

- **A.** Stored procedure (parameterized precompiled SQL routine)
- **B.** Nonclustered index (separate B-tree structure with row locators; multiple allowed per table)
- **C.** Create four separate clustered indexes on the same relational table to sort rows four ways physically
- **D.** Clustered index (defines physical leaf-level sort order; maximum one per table)

### 44. A clinical reporting analyst runs `SELECT * FROM vw_ActiveInpatients WHERE Ward = 'ICU'`. If `vw_ActiveInpatients` stores only a query definition and zero duplicated row pages on disk, `vw_ActiveInpatients` is a standard ____.

- **A.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Page blobs in Azure Blob Storage
- **D.** Database view (saved virtual `SELECT` query)

### 45. CarePulse wants to migrate 14 on-premises SQL Server clinical databases to Azure SQL while checking compatibility blockers and right-sizing compute first. Which four-step migration sequence is current?

- **A.** Point production apps to an empty Azure SQL server → Open firewall `0.0.0.0-255.255.255.255` to the public internet → Assess SQL Agent blockers after cutover → Export tables manually as JPEG screenshots
- **B.** Assess SQL Server readiness and SKU sizing in Azure Migrate → Select Azure SQL Database or Managed Instance → Provision target with Entra auth and TLS firewall rules → Migrate schema/data and cut over connection strings
- **C.** Convert relational tables into Azure Queue messages → Provision SQL Managed Instance without VNet planning → Run compatibility assessment last → Remove all primary keys before cutover
- **D.** Disable TLS encryption on SQL Server → Copy `.mdf` files directly into Azure Table storage → Provision Azure SQL Database Basic tier for cross-DB SQL Agent jobs → Run Azure Migrate discovery

### 46. CarePulse classifies two legacy SQL Server workloads: Workload A needs fully managed PaaS with SQL Server Agent and cross-database queries; Workload B requires Windows Server OS access to run a pinned SQL Server 2014 build alongside a legacy HL7 COM+ service on the same VM. Which two Azure SQL offerings match A and B? Select two.

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **C.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **D.** Cool access tier (online, 30-day minimum retention for infrequently accessed data)
- **E.** Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)

### 47. A clinical research team runs statistical SQL models only on Tuesday afternoons; during the remaining 160 hours per week the database has zero connections and should automatically pause compute billing so only storage is charged. Which Azure SQL SKU provides auto-pause?

- **A.** Use a single Azure SQL Database to run native SQL Server Agent jobs and cross-database three-part queries
- **B.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **C.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **D.** Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)

### 48. CarePulse hosts 95 separate outpatient clinic databases in Azure SQL Database where urban clinics peak in the morning and urgent-care clinics peak late evening. Grouping them into an ____ lets them share a fixed vCore budget cost-effectively.

- **A.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **B.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Azure SQL Database Elastic Pool (shared eDTU or vCore compute across multi-tenant DBs)

### 49. Proposed solution: An engineer suggests downloading the retired standalone Data Migration Assistant (`DMA`) for cloud SKU sizing; the lead DBA replaces it with ____ to assess SQL Server readiness and right-size Azure SQL targets. Which service completes the update?

- **A.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **B.** Run the retired standalone Data Migration Assistant (DMA) desktop tool as Microsoft’s current cloud sizing service
- **C.** Azure Migrate (discovery, readiness assessment, and SKU right-sizing for SQL Server)
- **D.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)

### 50. A genomics research team uses PostgreSQL extensions, custom composite types, and `PL/pgSQL` functions and wants managed Azure PaaS with built-in high availability and automated backups. Which Azure database service fits?

- **A.** Azure Database for MySQL — Flexible Server
- **B.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **C.** Azure Database for PostgreSQL — Flexible Server
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 51. CarePulse's patient education portal runs WordPress (`PHP` + `MySQL`) and IT wants to eliminate Linux VM patching while keeping native MySQL Community compatibility and cost-optimization stop/start controls. Which Azure service fits best?

- **A.** Azure Database for MySQL — Flexible Server
- **B.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **C.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **D.** Azure Database for PostgreSQL — Flexible Server

### 52. Clinicians' analytics DBAs connect `pgAdmin` to an Azure PaaS relational server while Microsoft automatically manages underlying host patching and server-level physical backups. Which service are they administering?

- **A.** Azure Database for PostgreSQL — Flexible Server
- **B.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

---

## Domain 3 — Describe considerations for working with non-relational data on Azure (15–20% official weight · 20 questions)

### 53. CarePulse retains diagnostic imaging studies online for immediate physician review during the first 30 days, occasional follow-up to 90 days, rare reference to 365 days, and mandatory 10-year HIPAA archival thereafter. Which four-step Blob Storage tier sequence fits?

- **A.** Ingest active files into Hot access tier → Transition 30-day infrequent blobs to Cool tier → Move 90-day rarely read blobs to Cold tier → Transition 365-day compliance blobs to offline Archive tier (rehydrating when needed)
- **B.** Mount Archive blobs as an SMB network drive → Stream live append logs into Page blobs in Cold tier → Transition 1-year compliance archives to Hot tier → Rehydrate Hot blobs before every read
- **C.** Write unstructured video files into Azure Table `RowKey` cells → Age rows from Cool to Hot after 180 days → Convert Page blobs into SQL views → Rehydrate Cool blobs for 12 hours before reading
- **D.** Ingest active operational files directly into Archive tier → Serve millisecond web downloads from Archive without rehydration → Move 90-day files to Hot tier → Delete storage account container metadata

### 54. Compare the two extremes of Azure Blob Storage access tiers: which tier has the **lowest read/transaction cost** for actively accessed files, and which offline tier has the **lowest GB/month storage price** for >=180-day compliance archives? Select two.

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **C.** Hot access tier (highest storage rate, lowest read/write access cost)
- **D.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **E.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 55. CarePulse's data lake team enables **Hierarchical Namespace** on an Azure Storage account so Spark jobs can perform atomic folder renames (`/raw/2026/07` -> `/processed/2026/07`) and enforce POSIX directory ACLs. Which capability was enabled?

- **A.** Azure Data Lake Storage Gen2 (Blob Storage with Hierarchical Namespace enabled)
- **B.** Page blobs in Azure Blob Storage
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)

### 56. Outpatient discharge summaries older than 90 days are read less than once a quarter, yet emergency physicians require immediate millisecond online access whenever a returning patient arrives (no multi-hour rehydration delay). Which Blob tier offers lower storage cost than Cool while remaining online?

- **A.** Store active operational files directly in Azure Blob Archive tier for immediate millisecond web reads
- **B.** Cold access tier (online, 90-day minimum retention for rarely accessed data)
- **C.** Hot access tier (highest storage rate, lowest read/write access cost)
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 57. In Microsoft Fabric, CarePulse creates a single tenant-wide logical data lake that links existing ADLS Gen2 medical-research folders via zero-copy **Shortcuts** without duplicating Parquet files. This built-in Fabric storage layer is ____.

- **A.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **B.** Page blobs in Azure Blob Storage
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Microsoft OneLake (single tenant-wide SaaS data lake built into Microsoft Fabric)

### 58. CarePulse's pathology labs run Linux microscope appliances mounting `NFS 4.1` shares alongside branch Windows servers syncing local SMB folders to Azure with cloud tiering. Which two Azure services satisfy both needs? Select two.

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **C.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **D.** Block blobs in Azure Blob Storage
- **E.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)

### 59. Hospital transcription software expects a POSIX/SMB shared directory tree where multiple Windows and macOS transcriptionists lock and edit `.docx` drafts concurrently via OS mount points. Which Azure Storage service should IT deploy?

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Append blobs in Azure Blob Storage
- **C.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 60. When CarePulse enables cloud tiering in ____, only recently opened radiology templates remain cached on the local clinic Windows Server volume while older files become pointer stubs fetched seamlessly from Azure Files on demand.

- **A.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **B.** Azure Stream Analytics (serverless SQL-like stream processing engine with windowing functions)
- **C.** Azure Data Lake Storage Gen2 (Blob Storage with Hierarchical Namespace enabled)
- **D.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)

### 61. CarePulse tracks 50 million disposable BLE asset-tracker pings where every entity stores `HospitalWing` as `PartitionKey`, `BeaconID` as `RowKey`, and variable sensor properties without a fixed column schema. Which Azure Storage service fits this low-cost key-value pattern?

- **A.** Apache Parquet columnar storage format
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 62. In Azure Table storage, grouping related entities with the same ____ ensures they are co-located in the same logical partition for efficient single-partition range scans ordered by `RowKey`.

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Enforce server-side foreign keys and multi-table SQL `INNER JOIN` queries inside Azure Table storage
- **C.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **D.** Star schema (central numeric fact table joined directly to denormalized dimension tables)

### 63. Proposed solution: A hospital alert directory built on Azure Table storage now needs sub-10 ms read/write SLAs, automatic secondary property indexes, and multi-region failover while keeping its `PartitionKey`/`RowKey` data model; the architect migrates it to ____. What completes this solution?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **C.** Append blobs in Azure Blob Storage
- **D.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)

### 64. A multinational clinical-trial diary app on Azure Cosmos DB needs multi-region writes across Sydney, London, and Chicago so trial participants experience `<10 ms` writes and immediately read back their own submitted symptom entries in order. Which two Cosmos DB features apply? Select two.

- **A.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **B.** Azure Cosmos DB turnkey global distribution with multi-region writes and <10 ms SLAs
- **C.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **E.** Session consistency (default level guaranteeing read-your-own-writes and monotonic reads per client session)

### 65. In Azure Cosmos DB, a 1 KB point read by ID + partition key consumes `1` normalized unit combining CPU, memory, and IOPS, whereas complex cross-partition queries consume more units. What is this billing unit called?

- **A.** Page blobs in Azure Blob Storage
- **B.** Waterfall chart (sequential positive/negative variance steps) or Funnel chart (linear stage conversion drop-off)
- **C.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **D.** Request Units (RUs) normalized compute/IO currency (Provisioned, Autoscale, or Serverless)

### 66. CarePulse's controlled-narcotics vault log on single-write-region Cosmos DB requires that every hospital pharmacy reader globally is guaranteed to see the absolute latest committed dispense event with zero stale reads. Which consistency level is required?

- **A.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)
- **B.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **C.** Session consistency (default level guaranteeing read-your-own-writes and monotonic reads per client session)
- **D.** Apache Avro row-based binary format with JSON schema

### 67. Which Azure non-relational database service offers financially backed `99.999%` read and write availability SLAs when configured across multiple Azure regions?

- **A.** Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **D.** Azure Cosmos DB turnkey global distribution with multi-region writes and <10 ms SLAs

### 68. CarePulse's engineering team is provisioning an Azure Cosmos DB container for FHIR JSON patient observations keyed by `/patientId`. Which four-step workflow follows Cosmos DB architecture rules?

- **A.** Create a Cosmos DB account choosing the target API → Create a database and container with a high-cardinality partition key → Configure RU/s or serverless and consistency → Insert items and run partition-scoped queries
- **B.** Install OS patches on Cosmos DB virtual machines → Format NTFS volumes for JSON items → Assign a constant single-value partition key to all 100 million documents → Query exclusively with T-SQL stored procedures
- **C.** Create a container without a partition key → Switch the existing account between Cassandra, Gremlin, and NoSQL APIs daily → Enforce 3NF foreign-key joins across containers → Store 500 MB MP4 blobs inside single JSON items
- **D.** Provision an Azure Files SMB share → Enable Strong consistency across 5 multi-write regions simultaneously → Omit databases and write JSON straight to subscription tags → Query vertices using `SMB2` locks

### 69. CarePulse builds a new cloud-native FHIR service storing JSON clinical notes and querying them via `SELECT * FROM c WHERE c.patientId = 'P908' AND c.type = 'Vitals'`. Which Azure Cosmos DB API should be chosen?

- **A.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **B.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **C.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **D.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)

### 70. An epidemiology team models hospitals, wards, clinicians, and patients as vertices with time-stamped `TREATED_BY` and `SHARED_ROOM` edges to trace multi-hop pathogen transmission paths. Which Azure Cosmos DB API fits?

- **A.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **B.** Azure Cosmos DB for MongoDB (wire-protocol compatibility for BSON document apps)
- **C.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **D.** Block blobs in Azure Blob Storage

### 71. CarePulse's mobile wellness subsidiary already runs a Python PyMongo application storing BSON workout documents and wants managed global replication on Azure without rewriting driver calls. Which Cosmos DB API fits?

- **A.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **B.** Azure Cosmos DB for MongoDB (wire-protocol compatibility for BSON document apps)
- **C.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **D.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)

### 72. A wearable pacemaker vendor streams wide-column telemetry tables written with Apache Cassandra CQL drivers and wants zero node-repair administration on Azure. Which Cosmos DB API should they provision?

- **A.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **D.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating

---

## Domain 4 — Describe an analytics workload on Azure (25–30% official weight · 28 questions)

### 73. CarePulse consolidates EHR, lab, and pharmacy extracts into a Microsoft Fabric Lakehouse using a medallion architecture. Which four-step sequence represents the ELT pipeline?

- **A.** Extract source data via Data Factory pipeline → Land raw files into OneLake / ADLS Gen2 (Bronze) → Cleanse and conform Delta tables via Spark or SQL (Silver) → Model star-schema fact/dimension tables (Gold) for BI
- **B.** Transform terabytes on the client laptop in Notepad → Upload screenshots to Archive Blob tier → Query offline blobs live with DAX → Store fact tables inside Azure Queue messages
- **C.** Publish Gold star schema before ingesting source data → Run OLTP checkout locks inside Power BI Mobile → Overwrite source ERP primary keys during read → Store Parquet files in DNS TXT records
- **D.** Build Power BI visuals directly against uncleaned CSV attachments → Delete raw source history immediately → Normalize Gold tables into 3NF OLTP row stores → Export final aggregates back into email inboxes

### 74. Because strict clinical privacy policy forbids raw patient Social Security numbers from ever landing in analytical lake storage, CarePulse hashes and strips PII inside an intermediate transformation stage **before** writing records into the warehouse. Which pattern is this?

- **A.** Extract, Load, and Transform (ELT) pattern
- **B.** Extract, Transform, and Load (ETL) pattern
- **C.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)
- **D.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)

### 75. CarePulse schedules nightly pipelines that pull on-premises EHR tables over a Self-Hosted Integration Runtime via Copy activity and visually cleanse lookup codes in Dataflows Gen2. Which orchestration service runs these pipelines?

- **A.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **B.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Azure Data Factory / Fabric Data Factory pipelines and Dataflows Gen2

### 76. CarePulse's BI architects compare two dimensional warehouse modeling styles around `FactAdmissions`: Style A joins `FactAdmissions` directly to flat `DimProcedure` and `DimDate` tables; Style B normalizes `DimProcedure` into `DimProcedureGroup` and `DimClinicalDomain`. Which two schemas are Style A and Style B? Select two.

- **A.** Key-value non-relational store
- **B.** Append blobs in Azure Blob Storage
- **C.** Isolation (concurrent transactions do not interfere)
- **D.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **E.** Star schema (central numeric fact table joined directly to denormalized dimension tables)

### 77. CarePulse stores de-identified clinical datasets as open **Delta Lake** Parquet files in OneLake while running ACID `MERGE` updates and T-SQL queries directly over those files without copying them into a separate proprietary warehouse. This store architecture is a ____.

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Data lakehouse (Delta Lake ACID transactions and SQL/Spark queries directly over open Parquet files)

### 78. In dimensional modeling, numeric additive measurements such as `BilledAmount` and `ProcedureMinutes` belong in the central fact table, while descriptive filtering attributes (`PhysicianSpecialty`, `HospitalRegion`) belong in surrounding dimension tables of a ____.

- **A.** Page blobs in Azure Blob Storage
- **B.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **C.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **D.** Graph database (vertices and directed edges)

### 79. Match three large-scale Azure analytics platforms: (1) unified SaaS analytics over OneLake, (2) collaborative Apache Spark + ML platform co-engineered with Databricks, and (3) managed open-source Hadoop/Hive/HBase cluster service for lift-and-shift workloads. Which three services match? Select three.

- **A.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **B.** Microsoft Fabric (unified SaaS analytics platform atop OneLake)
- **C.** Azure HDInsight (managed open-source Hadoop, Hive, HBase, Kafka, and Spark clusters)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **E.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **F.** Azure Databricks (collaborative Apache Spark analytics, Delta Lake, and ML platform)

### 80. CarePulse's analytics team uses **serverless SQL pools** to run ad-hoc T-SQL `OPENROWSET` queries directly over Parquet files in ADLS Gen2 alongside **dedicated SQL pools** for MPP warehousing inside Synapse Studio. Which Azure service are they using?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Azure Synapse Analytics (serverless SQL pools, dedicated MPP SQL pools, and Spark pools)
- **C.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **D.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)

### 81. Which Microsoft SaaS analytics platform includes **Direct Lake** mode so Power BI semantic models read Delta Parquet tables straight from OneLake memory without slow DirectQuery translations or scheduled Import copies?

- **A.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Microsoft Fabric (unified SaaS analytics platform atop OneLake)
- **D.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)

### 82. CarePulse's biostatistics team trains survival-analysis ML models and runs PySpark jobs over petabytes of genomics Parquet files using managed Spark clusters and Unity Catalog governance in Azure. Which service fits best?

- **A.** Azure Databricks (collaborative Apache Spark analytics, Delta Lake, and ML platform)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 83. ICU bedside monitors evaluate patient oxygen saturation (`SpO2`) readings continuously every second so nurses receive hypoxia alerts within 500 milliseconds when `SpO2 < 88%`. This workload requires ____.

- **A.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **B.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **C.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)
- **D.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)

### 84. At the close of each calendar month, CarePulse compiles all finalized insurance claims into state DRG reimbursement submissions. Processing bounded monthly claim sets on a schedule is ____.

- **A.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **B.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **C.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **D.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)

### 85. An ICU stream job raises an alert whenever a patient's average heart rate over **any** rolling 60-second lookback exceeds 140 bpm, evaluating the window specifically as new heartbeats enter or expire from the 60-second span. Which window function matches this?

- **A.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **B.** Apache Parquet columnar storage format
- **C.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **D.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)

### 86. CarePulse records non-overlapping 15-minute emergency-room arrival counts (`00:00–00:15`, `00:15–00:30`, `00:30–00:45`) so every triage check-in is counted in one and only one 15-minute bucket. Which window type is this?

- **A.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **B.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **C.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **D.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)

### 87. CarePulse evaluates two Microsoft cloud options for real-time vitals analytics: Option 1 uses Eventstream, Eventhouse KQL databases, and Activator alerts in Microsoft Fabric; Option 2 uses checkpointed PySpark unbounded DataFrames writing to Delta Lake. Which two technologies are these? Select two.

- **A.** Apache Spark Structured Streaming (fault-tolerant DataFrame/SQL stream processing in Databricks and Fabric)
- **B.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **C.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **D.** Microsoft Fabric Real-Time Intelligence (Eventstream, Eventhouse KQL database, Real-Time Dashboards, and Activator)
- **E.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 88. An engineer writes `SELECT DeviceId, AVG(HeartRate) INTO AlertSink FROM VitalsHub TIMESTAMP BY EventTime GROUP BY DeviceId, TumblingWindow(second, 30)` in a serverless Azure PaaS job with zero cluster management. Which Azure service executes this SQL-like streaming query?

- **A.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **B.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **C.** Azure Stream Analytics (serverless SQL-like stream processing engine with windowing functions)
- **D.** Cold access tier (online, 90-day minimum retention for rarely accessed data)

### 89. Before stream processors analyze telemetry from 80,000 hospital IoT infusion pumps, CarePulse needs a partitioned cloud event ingestion front door capable of buffering millions of events per second for multiple consumer groups. Which Azure service acts as this event broker?

- **A.** Database view (saved virtual `SELECT` query)
- **B.** Azure Event Hubs (high-throughput partitioned event ingestion broker with Kafka support)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 90. In Microsoft Fabric Real-Time Intelligence, high-volume streaming telemetry and log events are stored and indexed inside an **Eventhouse** database queried with `KQL` (Kusto Query Language). Which Fabric workload hosts Eventstream, Eventhouse, and Activator?

- **A.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **B.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **C.** Microsoft Fabric Real-Time Intelligence (Eventstream, Eventhouse KQL database, Real-Time Dashboards, and Activator)
- **D.** Delimited text format (CSV or TSV)

### 91. CarePulse's analytics team wants to prepare clinical quality tables, author interactive report pages, assemble a cross-report executive dashboard, and distribute read-only access to hospital directors. Which four-step Power BI sequence is valid?

- **A.** Author multi-report dashboards inside Power BI Mobile → Export `.pbix` files to Azure Table storage → Schedule dataset refresh inside Windows Notepad → Email raw database passwords to report viewers
- **B.** Shape source data with Power Query in Power BI Desktop → Relate star-schema tables, write DAX, and build report pages → Publish model and report to Power BI Service → Pin dashboard tiles, schedule refresh, and share an App
- **C.** Design `.rdl` pixel-perfect invoices in Azure Stream Analytics → Publish directly to unmanaged personal OneDrive as an OLTP database → Disable table relationships → Share via anonymous firewall port `1433`
- **D.** Pin dashboard tiles in Power BI Desktop offline → Write Power Query M transformations inside Power BI Mobile → Store semantic models on SMB floppy shares → Require every executive viewer to edit DAX in Desktop

### 92. Which free Windows authoring tool do CarePulse data analysts use locally to connect to data sources via Power Query, define `1:*` star-schema relationships, write DAX measures, and save `.pbix` multi-page interactive reports?

- **A.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **B.** Create multi-report pinned dashboards directly inside Power BI Desktop offline
- **C.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **D.** Microsoft Power BI Service (cloud SaaS portal for workspaces, dashboards, scheduled refresh, and Apps)

### 93. Proposed solution: State health auditors require printed multi-page patient billing statements where a 400-row itemized table expands cleanly across 14 PDF pages with exact margins; instead of using a scrolling Power BI Desktop visual, the analyst builds a paginated `.rdl` report in ____. What completes this solution?

- **A.** Microsoft Power BI Service (cloud SaaS portal for workspaces, dashboards, scheduled refresh, and Apps)
- **B.** Azure Event Hubs (high-throughput partitioned event ingestion broker with Kafka support)
- **C.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

### 94. In Power BI Desktop's Model view, an analyst connects `DimDepartment`, `DimCalendar`, and `DimDiagnosis` via single-direction `1:*` relationships to `FactVisits` and creates a `Year -> Quarter -> Month` hierarchy. Which two Power BI modeling concepts are applied? Select two.

- **A.** Power BI semantic model (relationships, DAX measures, hierarchies, and Import/DirectQuery/Direct Lake storage)
- **B.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **C.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **D.** Append blobs in Azure Blob Storage
- **E.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 95. CarePulse defines `Bed Occupancy % := DIVIDE(SUM(FactCensus[OccupiedBeds]), SUM(FactCensus[StaffedBeds]))` so the ratio recalculates accurately whether sliced by hospital, wing, or date. Why must this ratio be authored as a ____ rather than a precalculated row column?

- **A.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **B.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **C.** Page blobs in Azure Blob Storage
- **D.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)

### 96. To prevent report consumers from accidentally summing `PatientID` or `ClinicZipCode` on charts, an analyst sets **Summarization = Don't summarize** and hides foreign-key columns inside the ____.

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **C.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **D.** Power BI semantic model (relationships, DAX measures, hierarchies, and Import/DirectQuery/Direct Lake storage)

### 97. Which formula language is used inside Power BI semantic models to define dynamic aggregations such as `CALCULATE`, `SUM`, `AVERAGE`, and year-over-year time-intelligence metrics?

- **A.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **B.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **C.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **D.** Apache Avro row-based binary format with JSON schema

### 98. CarePulse's emergency medical director wants to plot `TriageWaitMinutes` on the X-axis against `PatientSatisfactionScore` on the Y-axis across 180 clinics (with bubble size = `AnnualVisits`) to see whether longer waits correlate with lower scores and spot outlier clinics. Which Power BI visual fits best?

- **A.** Treemap (or pie/donut chart for small category counts) showing part-to-whole proportions
- **B.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)
- **C.** Append blobs in Azure Blob Storage
- **D.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)

### 99. Hospital finance wants a cross-tabulated visual showing `HospitalRegion -> Facility` down the rows, `FiscalYear -> Quarter` across the columns, and stepped drill-down subtotals for `NetPatientRevenue`. Which Power BI visual provides two-axis pivot cross-tabulation?

- **A.** Matrix visual (cross-tabbed rows/columns with stepped drill-down subtotals) or Azure Map (geospatial coordinates)
- **B.** Apache Parquet columnar storage format
- **C.** Line chart (tracking continuous trends and changes over ordered time intervals)
- **D.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)

### 100. CarePulse's oncology trial team wants to visualize progressive participant drop-off across five sequential screening stages (`Referred -> Screened -> Eligible -> Consented -> Enrolled`). Which Power BI chart displays linear stage-by-stage conversion and drop-off?

- **A.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)
- **B.** Waterfall chart (sequential positive/negative variance steps) or Funnel chart (linear stage conversion drop-off)
- **C.** Page blobs in Azure Blob Storage
- **D.** First Normal Form (1NF — atomic values and no repeating column groups)

---

## Answer Key and Explanations

### Question 1 — `B` (Describe core data concepts)

Correct answer: B (is correct). Rows stored in fixed, typed relational table columns with a uniform schema represent structured data. [Skill 1.1: Describe the features of structured data | Source: Explore core data concepts — Identify data formats (structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.
- **B:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **C:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.

### Question 2 — `C` (Describe core data concepts)

Correct answer: C (is correct). Fixed tabular schemas with enforced column types and uniform row layouts are structured data. [Skill 1.1: Describe the features of structured data | Source: Explore core data concepts — Identify data formats (structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **B:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **C:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **D:** Incorrect. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.

### Question 3 — `B, E` (Describe core data concepts)

Correct answers: B and E (are correct). FHIR documents with self-describing keys and variable nested arrays are semi-structured JSON data. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **B:** Correct. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **E:** Correct. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.

### Question 4 — `D` (Describe core data concepts)

Correct answer: D (is correct). XML documents use self-describing hierarchical tags rather than fixed relational columns and are classified as semi-structured data. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **B:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **C:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Correct. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.

### Question 5 — `C` (Describe core data concepts)

Correct answer: C (is correct). Apache Avro stores compact binary row records alongside an embedded JSON schema header. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Correct. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **D:** Incorrect. Bar and column charts use aligned bar lengths to compare magnitudes accurately across discrete categories such as product lines or regions.

### Question 6 — `C` (Describe core data concepts)

Correct answer: C (is correct). Medical imagery, video, and audio files lack a tabular or key-tag schema and are unstructured data. [Skill 1.3: Describe the features of unstructured data | Source: Explore core data concepts — Identify data formats (unstructured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **B:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **C:** Correct. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.

### Question 7 — `C` (Describe core data concepts)

Correct answer: C (is correct). Raw scanned images (`TIFF`, `PNG`) have no internal structured schema and represent unstructured data. [Skill 1.3: Describe the features of unstructured data | Source: Explore core data concepts — Identify data formats (unstructured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **B:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **C:** Correct. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Incorrect. A composite key combines two or more columns (such as `OrderID` + `ProductID`) to uniquely identify rows in a junction or line-item table.

### Question 8 — `A, D` (Describe core data concepts)

Correct answers: A and D (are correct). CSV suits simple flat human-readable text exchange, whereas Apache Parquet provides compressed columnar storage for large analytical scans. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Correct. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Correct. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **E:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.

### Question 9 — `D` (Describe core data concepts)

Correct answer: D (is correct). Apache Parquet organizes data column-by-column with column statistics, enabling projection and predicate pushdown over wide analytical datasets. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Incorrect. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **D:** Correct. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.

### Question 10 — `B` (Describe core data concepts)

Correct answer: B (is correct). Optimized Row Columnar (ORC) stores data in compressed stripes with lightweight indexes tailored for Hive and batch analytics. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Incorrect. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **B:** Correct. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 11 — `C, D` (Describe core data concepts)

Correct answers: C and D (are correct). A document database indexes nested JSON intake forms, while a graph database models vertices and edges for multi-hop contact-tracing traversals. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **B:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Correct. A document database stores self-contained JSON/BSON documents indexed across nested attributes so each entity can evolve fields without schema migrations.
- **D:** Correct. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **E:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 12 — `D` (Describe core data concepts)

Correct answer: D (is correct). A key-value database maps each unique key directly to its value for rapid single-key lookups without join overhead. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **B:** Incorrect. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **C:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **D:** Correct. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.

### Question 13 — `B` (Describe core data concepts)

Correct answer: B (is correct). A column-family (wide-column) database organizes related columns into families under row/partition keys for massive write scalability. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Correct. A column-family database groups related columns into families keyed by row and partition keys (such as Apache Cassandra or HBase) for massive write throughput.
- **C:** Incorrect. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.
- **D:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.

### Question 14 — `D` (Describe core data concepts)

Correct answer: D (is correct). Live billing check-ins commit in ACID Azure SQL Database, Data Factory extracts history to ADLS Gen2 / OneLake Parquet, and Power BI visuals query star-schema models. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Incorrect. Power BI Service is a read-optimized BI platform rather than a transactional database, and Queue storage buffers small messages rather than archiving relational rows.
- **B:** Incorrect. Archive blobs are offline and unreadable for live OLTP writes, Power BI Desktop is an authoring tool rather than an OLTP engine, and Table storage is schemaless key-value.
- **C:** Incorrect. Paginated reports render formatted output rather than ingesting transactions, and Blob Cold tier does not execute multi-row ACID relational transactions.
- **D:** Correct. Operational transactions commit in an ACID relational store first, pipelines land history in columnar lake storage, and analytical models serve BI reports without taxing OLTP.

### Question 15 — `C` (Describe core data concepts)

Correct answer: C (is correct). Azure Files provides managed SMB 3.0 and NFS 4.1 cloud file shares mountable like traditional network drives. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Incorrect. Azure Queue storage holds small asynchronous work messages (up to 64 KB per message), not multi-gigabyte binary files.

### Question 16 — `B` (Describe core data concepts)

Correct answer: B (is correct). Azure Cosmos DB delivers turnkey global distribution, multi-region writes, and financially backed single-digit millisecond latency SLAs. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **B:** Correct. Azure Cosmos DB replicates data transparently across selected Azure regions with financially backed 99.999% availability and single-digit millisecond read/write latency.
- **C:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 17 — `C, E, F` (Describe core data concepts)

Correct answers: C, E, and F (are correct). Live operational dispensing is an OLTP workload relying on ACID Atomicity (all-or-nothing rollback) and Consistency (valid `StockOnHand >= 0` state). [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **B:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **C:** Correct. Atomicity guarantees that every statement in a transaction either succeeds together or rolls back completely if any step fails, preventing half-completed transfers.
- **D:** Incorrect. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **E:** Correct. Consistency ensures a transaction transitions the database only from one valid rule-compliant state (keys, check constraints, types) to another.
- **F:** Correct. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.

### Question 18 — `B` (Describe core data concepts)

Correct answer: B (is correct). Isolation ensures concurrent transactions execute without exposing uncommitted intermediate states or colliding unpredictably. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **B:** Correct. Isolation prevents concurrent in-flight transactions from reading uncommitted intermediate edits or overwriting each other unpredictably via locking or row versioning.
- **C:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **D:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.

### Question 19 — `A` (Describe core data concepts)

Correct answer: A (is correct). Durability ensures committed transactions are persisted to non-volatile transaction logs/storage and survive crashes or power loss. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Correct. Durability guarantees that once a transaction commits, its changes are persisted to non-volatile transaction logs/storage and survive power loss or crash recovery.
- **B:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.
- **C:** Incorrect. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.
- **D:** Incorrect. The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.

### Question 20 — `C, E` (Describe core data concepts)

Correct answers: C and E (are correct). Multi-year read-heavy aggregations represent an OLAP workload, and normalized multi-level dimension hierarchies form a snowflake schema. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Incorrect. Atomicity guarantees that every statement in a transaction either succeeds together or rolls back completely if any step fails, preventing half-completed transfers.
- **C:** Correct. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **D:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **E:** Correct. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.

### Question 21 — `C` (Describe core data concepts)

Correct answer: C (is correct). Offloading read-intensive historical aggregations away from live transactional tables is the core purpose of an OLAP analytical workload. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Correct. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **D:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.

### Question 22 — `C` (Describe core data concepts)

Correct answer: C (is correct). A central numeric fact table joined directly to denormalized dimension tables is a star schema. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **C:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **D:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.

### Question 23 — `C` (Describe core data concepts)

Correct answer: C (is correct). Database security, encryption, HA failover groups, permissions, and backup/restore validation are core DBA duties. [Skill 1.9: Describe responsibilities for database administrators | Source: Explore data roles and services — Database administrator responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **B:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
- **C:** Correct. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **D:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.

### Question 24 — `C` (Describe core data concepts)

Correct answer: C (is correct). Monitoring operational database health and tuning indexes/query plans belong to the database administrator (DBA). [Skill 1.9: Describe responsibilities for database administrators | Source: Explore data roles and services — Database administrator responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **B:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **C:** Correct. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **D:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.

### Question 25 — `A` (Describe core data concepts)

Correct answer: A (is correct). The DBA governs operational SQL, the data engineer builds ELT pipelines and Gold star schemas in Fabric, and the data analyst models DAX KPIs and Power BI reports. [Skill 1.10: Describe responsibilities for data engineers | Source: Explore data roles and services — Data engineer responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Correct. DBAs govern operational database engines, data engineers build ingestion/transformation pipelines into curated analytical stores, and data analysts model KPIs and visual reports.
- **B:** Incorrect. Cluster HA belongs to the DBA, Spark ELT pipelines belong to the data engineer, and visual storytelling/app distribution belongs to the data analyst.
- **C:** Incorrect. KPI scorecards and sales packs are data analyst outputs, whereas Spark streaming pipelines belong to data engineers and OLTP index maintenance belongs to DBAs.
- **D:** Incorrect. Operational DB security and PITR restores are DBA duties, network/pipeline plumbing belongs to infra/data engineering, and analysts focus on semantic models and visuals.

### Question 26 — `B` (Describe core data concepts)

Correct answer: B (is correct). Building and maintaining automated ingestion, cleansing, and lakehouse transformation pipelines is the responsibility of a data engineer. [Skill 1.10: Describe responsibilities for data engineers | Source: Explore data roles and services — Data engineer responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **B:** Correct. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **C:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **D:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.

### Question 27 — `D` (Describe core data concepts)

Correct answer: D (is correct). Data analysts transform curated semantic models into DAX KPIs, interactive reports, and actionable business visualizations. [Skill 1.11: Describe responsibilities for data analysts | Source: Explore data roles and services — Data analyst responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **B:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **C:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **D:** Correct. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.

### Question 28 — `C` (Describe core data concepts)

Correct answer: C (is correct). Semantic KPI modeling and visual report authoring for clinical leaders are core data analyst tasks. [Skill 1.11: Describe responsibilities for data analysts | Source: Explore data roles and services — Data analyst responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **B:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **C:** Correct. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 29 — `B, D` (Identify considerations for relational data on Azure)

Correct answers: B and D (are correct). `PatientID` is a single-column primary key, and `(PatientID, AllergenCode)` is a multi-column composite key. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **B:** Correct. A primary key uniquely identifies each row in a relational table and implicitly forbids `NULL` and duplicate key values.
- **C:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Correct. A composite key combines two or more columns (such as `OrderID` + `ProductID`) to uniquely identify rows in a junction or line-item table.
- **E:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 30 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). A foreign key enforces referential integrity by requiring values to match an existing primary/unique key in the referenced parent table. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. A primary key uniquely identifies each row in a relational table and implicitly forbids `NULL` and duplicate key values.
- **B:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **C:** Correct. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.
- **D:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.

### Question 31 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Relational tables enforce a strict tabular row-and-typed-column schema, representing structured data. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **B:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **C:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **D:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.

### Question 32 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Primary key columns must uniquely identify every row and therefore implicitly enforce `NOT NULL`. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. The Hot tier is online storage optimized for data that is accessed or modified frequently, carrying the lowest transaction/read cost.
- **B:** Correct. A primary key uniquely identifies each row in a relational table and implicitly forbids `NULL` and duplicate key values.
- **C:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **D:** Incorrect. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.

### Question 33 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). 1NF enforces atomic cells and a primary key, 2NF removes partial dependencies on composite keys, and 3NF removes transitive dependencies among non-key columns. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. You cannot achieve 3NF before 1NF/2NF, comma-separated lists violate 1NF atomicity, and duplicating addresses reintroduces update anomalies.
- **B:** Correct. Normalization progresses sequentially: 1NF enforces atomic values and row uniqueness, 2NF removes partial dependencies on composite keys, and 3NF eliminates transitive non-key dependencies.
- **C:** Incorrect. Foreign keys require atomic primary keys first, and 1NF eliminates repeating groups rather than creating them.
- **D:** Incorrect. Copying supplier attributes into invoice items creates transitive redundancy, and pipe-delimited multi-value strings violate 1NF.

### Question 34 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). First Normal Form (1NF) requires atomic scalar values per cell and eliminates repeating column groups. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **B:** Correct. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **C:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **D:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.

### Question 35 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Second Normal Form (2NF) removes partial dependencies where a non-key column depends on only one part of a composite primary key. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Correct. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **B:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **C:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **D:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.

### Question 36 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Third Normal Form (3NF) ensures non-key attributes depend only on the primary key and removes transitive non-key dependencies. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Correct. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **C:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **D:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.

### Question 37 — `B, D, E` (Identify considerations for relational data on Azure)

Correct answers: B, D, and E (are correct). `ALTER TABLE` is DDL, `SELECT` is DML, and `REVOKE` is DCL. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **B:** Correct. DML statements query, add, modify, or delete row data stored inside relational tables.
- **C:** Incorrect. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **D:** Correct. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **E:** Correct. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **F:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 38 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). An `INNER JOIN` returns rows only when matching join keys exist in both joined tables. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **B:** Correct. `INNER JOIN` returns only row pairs whose join predicate matches in both the left and right tables, excluding unmatched rows.
- **C:** Incorrect. SQL `WHERE` evaluates individual pre-grouped rows and rejects aggregate functions; group-level aggregate filters belong in the `HAVING` clause.
- **D:** Incorrect. `LEFT OUTER JOIN` keeps every row from the left table (for example, all customers) and fills `NULL` for right-table columns when no related order exists.

### Question 39 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). SQL `WHERE` filters individual rows prior to `GROUP BY` and cannot evaluate aggregate functions, whereas `HAVING` filters grouped aggregates. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. SQL `WHERE` evaluates individual pre-grouped rows and rejects aggregate functions; group-level aggregate filters belong in the `HAVING` clause.
- **B:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **C:** Correct. `WHERE` predicates evaluate individual source rows prior to aggregation, whereas `HAVING` filters grouped summary results such as `HAVING COUNT(*) > 5`.
- **D:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.

### Question 40 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Data Control Language (DCL) governs database permissions via `GRANT`, `REVOKE`, and `DENY`. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. DML statements query, add, modify, or delete row data stored inside relational tables.
- **B:** Incorrect. Granting and revoking security permissions belongs to DCL (`GRANT`, `REVOKE`, `DENY`), not DML.
- **C:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **D:** Correct. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.

### Question 41 — `B, D` (Identify considerations for relational data on Azure)

Correct answers: B and D (are correct). A view exposes a saved virtual `SELECT` query hiding sensitive columns, while a stored procedure executes parameterized multi-statement SQL logic on the server. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **B:** Correct. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **C:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **D:** Correct. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.
- **E:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 42 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). In SQL Server and Azure SQL, a primary key creates a clustered index by default (unless another clustered index already exists), ordering rows physically on disk. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **B:** Incorrect. Because a clustered index dictates the single physical leaf-level storage order of the table’s rows, a table can have at most one clustered index (plus multiple nonclustered indexes).
- **C:** Correct. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **D:** Incorrect. A nonclustered index maintains a separate sorted key structure pointing back to the base table rows, accelerating selective lookups on non-primary search columns.

### Question 43 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Multiple nonclustered indexes can be created per table, each storing a sorted B-tree of key values with pointers back to the clustered row. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.
- **B:** Correct. A nonclustered index maintains a separate sorted key structure pointing back to the base table rows, accelerating selective lookups on non-primary search columns.
- **C:** Incorrect. Because a clustered index dictates the single physical leaf-level storage order of the table’s rows, a table can have at most one clustered index (plus multiple nonclustered indexes).
- **D:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.

### Question 44 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). A standard database view stores a query definition in metadata and dynamically reads underlying base tables when queried. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Correct. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.

### Question 45 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Azure Migrate discovers and assesses SQL readiness/SKUs (replacing retired DMA), followed by Entra/TLS target provisioning, data migration, and cutover. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Cutting over before data migration breaks production, opening all public IPs violates security, and assessments must run before selecting the target SKU.
- **B:** Correct. Azure Migrate discovers workloads, flags compatibility blockers, and recommends right-sized Azure SQL targets before secure provisioning, data sync, and connection cutover.
- **C:** Incorrect. Queue storage is not a relational migration vehicle, SQL Managed Instance requires VNet subnet sizing upfront, and removing primary keys corrupts relational integrity.
- **D:** Incorrect. Azure Table storage cannot mount `.mdf` database files, and single Azure SQL Database does not host SQL Server Agent or cross-database instance queries.

### Question 46 — `B, C` (Identify considerations for relational data on Azure)

Correct answers: B and C (are correct). SQL Managed Instance provides managed PaaS with instance-level SQL Agent/cross-DB features, while SQL Server on Azure VMs provides full IaaS OS and legacy version control. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Correct. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **C:** Correct. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **D:** Incorrect. The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.
- **E:** Incorrect. The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.

### Question 47 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Azure SQL Database Serverless automatically scales vCores on demand and auto-pauses during idle windows so only storage is billed. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Single Azure SQL Database is database-scoped and does not include SQL Server Agent or cross-database instance queries; those require SQL Managed Instance or SQL Server on Azure VMs.
- **B:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **C:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **D:** Correct. The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.

### Question 48 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). An Azure SQL Database Elastic Pool shares compute resources across multiple databases with staggered, unpredictable demand spikes. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **B:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Correct. An Elastic Pool shares a pool of compute resources across multiple single databases that have unpredictable, staggered usage spikes to optimize cost.

### Question 49 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Microsoft retired standalone DMA in July 2025; Azure Migrate (with the Azure SQL Migration experience) handles SQL discovery, readiness, and SKU sizing. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **B:** Incorrect. Microsoft retired Data Migration Assistant (DMA) in July 2025; Azure Migrate and the Azure SQL Migration extension handle SQL discovery, assessment, and right-sizing.
- **C:** Correct. Azure Migrate discovers on-premises SQL Server instances, evaluates feature compatibility blockers, and recommends right-sized Azure SQL targets (replacing retired DMA).
- **D:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.

### Question 50 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Azure Database for PostgreSQL — Flexible Server delivers managed PaaS PostgreSQL with extension support, `PL/pgSQL`, HA, and up to 35-day PITR. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Incorrect. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.
- **B:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **C:** Correct. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 51 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Azure Database for MySQL — Flexible Server provides managed PaaS MySQL with granular configuration and stop/start cost controls. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Correct. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.
- **B:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **C:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **D:** Incorrect. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.

### Question 52 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Azure Database for PostgreSQL — Flexible Server supports client tools like `pgAdmin` while Microsoft manages infrastructure patching and backups. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Correct. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **B:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 53 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Lifecycle rules transition blobs from Hot -> Cool (30+ days) -> Cold (90+ days) -> offline Archive (180+ days, rehydrating when requested). [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Correct. Lifecycle management policies automatically age blobs from lowest-read-cost Hot through Cool and Cold down to lowest-storage-cost offline Archive.
- **B:** Incorrect. Blob tiers are object storage rather than SMB shares, Archive rather than Hot minimizes 1-year retention storage cost, and Hot blobs require no rehydration.
- **C:** Incorrect. Table storage entities hold small key-value properties rather than large video files, and Cool/Cold tiers remain online with immediate millisecond read access.
- **D:** Incorrect. Archive tier is offline and cannot serve direct reads until rehydrated to Hot or Cool, which takes hours.

### Question 54 — `C, E` (Describe considerations for working with non-relational data on Azure)

Correct answers: C and E (are correct). Hot tier minimizes read/transaction costs for active data, whereas offline Archive tier minimizes monthly per-GB storage cost for long-term retention. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **C:** Correct. The Hot tier is online storage optimized for data that is accessed or modified frequently, carrying the lowest transaction/read cost.
- **D:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **E:** Correct. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 55 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Enabling Hierarchical Namespace on Azure Blob Storage activates Azure Data Lake Storage (ADLS) Gen2. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Correct. ADLS Gen2 adds a true POSIX-ACL directory hierarchy and atomic folder rename/delete operations atop Azure Blob Storage for big-data analytics engines.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.

### Question 56 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). The Cold access tier has a 90-day minimum retention and lower storage pricing than Cool while keeping blobs online for immediate reads. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Archive tier blobs are stored offline and cannot be read directly until rehydrated to Hot or Cool, which takes hours.
- **B:** Correct. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.
- **C:** Incorrect. The Hot tier is online storage optimized for data that is accessed or modified frequently, carrying the lowest transaction/read cost.
- **D:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 57 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Microsoft OneLake is Fabric's unified tenant-wide SaaS data lake supporting zero-copy Shortcuts across clouds and ADLS Gen2. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Correct. OneLake is Microsoft Fabric’s unified ADLS Gen2-compatible logical data lake that stores Delta Parquet data once and shares it via zero-copy Shortcuts across workloads.

### Question 58 — `A, C` (Describe considerations for working with non-relational data on Azure)

Correct answers: A and C (are correct). Azure Files natively supports both SMB 3.0 and NFS 4.1 cloud file shares, and Azure File Sync syncs/tiers Windows Server folders with Azure Files. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **C:** Correct. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **D:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.
- **E:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.

### Question 59 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Azure Files provides managed cloud file shares mountable concurrently across Windows, Linux, and macOS over SMB. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 60 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Azure File Sync's cloud tiering keeps hot files on local Windows Server disks and tiers cold files into Azure Files transparently. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Correct. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **B:** Incorrect. Azure Stream Analytics runs declarative Stream Analytics Query Language (`SELECT ... GROUP BY TumblingWindow(...)`) jobs joining live streams with reference data into sinks.
- **C:** Incorrect. ADLS Gen2 adds a true POSIX-ACL directory hierarchy and atomic folder rename/delete operations atop Azure Blob Storage for big-data analytics engines.
- **D:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.

### Question 61 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Azure Table storage stores schemaless entities indexed by composite `PartitionKey` + `RowKey` for fast, low-cost point and partition queries. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **D:** Correct. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 62 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). `PartitionKey` groups entities into logical partitions, while `RowKey` uniquely identifies and sorts entities within each partition. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Correct. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. Azure Table storage is a schemaless key-value store indexed only by `PartitionKey` and `RowKey` with no foreign keys or server-side table joins.
- **C:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **D:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.

### Question 63 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Azure Cosmos DB for Table upgrades `PartitionKey`/`RowKey` workloads with turnkey global distribution, secondary indexes, and <10 ms SLAs. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **C:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **D:** Correct. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.

### Question 64 — `B, E` (Describe considerations for working with non-relational data on Azure)

Correct answers: B and E (are correct). Turnkey multi-region global distribution provides local `<10 ms` writes, and Session consistency guarantees read-your-own-writes per participant session. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **B:** Correct. Azure Cosmos DB replicates data transparently across selected Azure regions with financially backed 99.999% availability and single-digit millisecond read/write latency.
- **C:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.
- **D:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **E:** Correct. Session consistency is Cosmos DB’s default level, balancing low latency and throughput while guaranteeing each user session immediately sees its own writes in order.

### Question 65 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Cosmos DB normalizes compute, memory, and IOPS consumption per operation into Request Units (RUs). [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Incorrect. Waterfall charts break down cumulative gains and losses between a starting and ending total, while Funnel charts track progressive drop-off across sequential pipeline stages.
- **C:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **D:** Correct. Cosmos DB measures CPU, memory, and IOPS per database operation in Request Units (RUs), billed via Provisioned/Autoscale RU/s or consumption-based Serverless.

### Question 66 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Strong consistency provides linearizable reads guaranteed to reflect the latest committed write. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.
- **B:** Correct. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **C:** Incorrect. Session consistency is Cosmos DB’s default level, balancing low latency and throughput while guaranteeing each user session immediately sees its own writes in order.
- **D:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.

### Question 67 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Azure Cosmos DB provides 99.999% multi-region read/write availability SLAs alongside `<10 ms` latency guarantees. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **D:** Correct. Azure Cosmos DB replicates data transparently across selected Azure regions with financially backed 99.999% availability and single-digit millisecond read/write latency.

### Question 68 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Select the NoSQL API at account creation, create the database and `/patientId`-partitioned container, configure RU/s or serverless + consistency, and execute partition-scoped queries. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Correct. API selection happens at account creation, partition key design happens at container creation to distribute storage/RU evenly, and partition-scoped queries avoid cross-partition fan-out.
- **B:** Incorrect. Cosmos DB is fully managed PaaS with no OS patching, a single-value partition key creates a 20 GB logical-partition bottleneck, and triggers/sprocs use JavaScript rather than T-SQL.
- **C:** Incorrect. Every Cosmos DB container requires a partition key, the API is fixed per account, Cosmos DB does not enforce cross-container foreign keys, and item size is capped at 2 MB.
- **D:** Incorrect. Cosmos DB sits under an account -> database -> container -> item hierarchy, not SMB shares or subscription tags.

### Question 69 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Azure Cosmos DB for NoSQL stores native JSON documents and supports SQL query syntax over hierarchical properties. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Correct. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **B:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **C:** Incorrect. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **D:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.

### Question 70 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Azure Cosmos DB for Apache Gremlin models property-graph vertices and edges traversed via Gremlin queries. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Correct. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **B:** Incorrect. Cosmos DB for MongoDB lets existing MongoDB drivers and tools store BSON documents in Cosmos DB simply by updating the connection string.
- **C:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **D:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.

### Question 71 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Cosmos DB for MongoDB speaks the MongoDB wire protocol so PyMongo BSON applications migrate via connection string. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **B:** Correct. Cosmos DB for MongoDB lets existing MongoDB drivers and tools store BSON documents in Cosmos DB simply by updating the connection string.
- **C:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **D:** Incorrect. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.

### Question 72 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Azure Cosmos DB for Apache Cassandra provides managed wire-level compatibility for CQL wide-column applications. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Correct. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **D:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.

### Question 73 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Pipelines land raw files into OneLake Bronze, Spark/SQL cleanses and deduplicates Silver Delta tables, and curated Gold star schemas feed BI. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Correct. Modern ELT lands raw data in scalable lake storage first, then leverages cloud compute to cleanse Silver tables and publish Gold star schemas for analytics.
- **B:** Incorrect. ELT executes transformations in scalable cloud engines rather than client laptops, and Archive blobs/Queues cannot back live BI queries.
- **C:** Incorrect. Analytical ingestion is read-only against operational sources and builds Bronze -> Silver -> Gold sequentially.
- **D:** Incorrect. Skipping cleansing degrades report accuracy, deleting raw Bronze files prevents replayability, and Gold analytical layers favor denormalized star schemas over 3NF.

### Question 74 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Transforming and scrubbing sensitive data prior to loading the target analytical store defines Extract, Transform, and Load (ETL). [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Incorrect. ELT extracts raw source data, loads it directly into scalable lake/warehouse storage, and runs distributed cloud compute (Spark or SQL) to cleanse and model in place.
- **B:** Correct. ETL transforms, scrubs, or redacts sensitive fields in an intermediate processing engine prior to loading only the conformed structure into the target analytical store.
- **C:** Incorrect. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.
- **D:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.

### Question 75 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Azure Data Factory / Microsoft Fabric Data Factory orchestrates hybrid Copy pipelines and visual Power Query Dataflows Gen2. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **B:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Correct. Data Factory orchestrates code-free data movement (90+ connectors via Copy activity) and visual Power Query transformations (Dataflows Gen2) or Spark/Mapping Data Flows.

### Question 76 — `D, E` (Describe an analytics workload on Azure)

Correct answers: D and E (are correct). Flat single-hop dimensions around a fact table form a star schema, while normalized multi-table dimension hierarchies form a snowflake schema. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Incorrect. Isolation prevents concurrent in-flight transactions from reading uncommitted intermediate edits or overwriting each other unpredictably via locking or row versioning.
- **D:** Correct. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **E:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.

### Question 77 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). A data lakehouse combines data-lake open file storage with Delta Lake ACID transactions and SQL warehouse querying. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Correct. A lakehouse combines the low-cost open file flexibility of a data lake with ACID transactions, schema enforcement, and SQL warehouse performance via Delta Lake tables.

### Question 78 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Separating numeric measures in a central fact table from descriptive context in surrounding dimension tables defines a star schema. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **C:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **D:** Incorrect. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.

### Question 79 — `B, C, F` (Describe an analytics workload on Azure)

Correct answers: B, C, and F (are correct). Microsoft Fabric, Azure Databricks, and Azure HDInsight represent those three large-scale cloud analytics platforms. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **B:** Correct. Microsoft Fabric unifies Data Factory, Data Engineering, Data Warehouse, Data Science, Real-Time Intelligence, and Power BI in one SaaS workspace sharing OneLake Delta tables.
- **C:** Correct. Azure HDInsight provisions managed clusters of open-source Apache big-data frameworks when lift-and-shift Hadoop/Hive/HBase/Kafka compatibility is required.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **E:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **F:** Correct. Azure Databricks provides managed Apache Spark clusters, collaborative Python/SQL/Scala/R notebooks, Unity Catalog governance, and Delta Lake processing on Azure.

### Question 80 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Azure Synapse Analytics provides both serverless SQL pools for on-demand lake querying and dedicated MPP SQL pools plus Spark pools. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Correct. Azure Synapse Analytics integrates serverless SQL on-demand lake querying, dedicated MPP SQL warehousing, Apache Spark pools, and Synapse Pipelines in Synapse Studio.
- **C:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **D:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.

### Question 81 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Microsoft Fabric unifies OneLake Delta tables with Power BI Direct Lake for warehouse-speed analytics without data duplication. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Correct. Microsoft Fabric unifies Data Factory, Data Engineering, Data Warehouse, Data Science, Real-Time Intelligence, and Power BI in one SaaS workspace sharing OneLake Delta tables.
- **D:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.

### Question 82 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Azure Databricks provides managed Apache Spark clusters, collaborative notebooks, Unity Catalog governance, and MLflow integration. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Correct. Azure Databricks provides managed Apache Spark clusters, collaborative Python/SQL/Scala/R notebooks, Unity Catalog governance, and Delta Lake processing on Azure.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **D:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 83 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Continuous low-latency evaluation of unbounded events in motion to trigger immediate alerts is stream processing. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **B:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **C:** Correct. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.
- **D:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.

### Question 84 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Scheduled processing over bounded sets of accumulated historical records is batch processing. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **B:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **C:** Correct. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **D:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.

### Question 85 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). A sliding window evaluates a fixed lookback duration exclusively at timestamps when events actually enter or leave the window. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **B:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **C:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **D:** Correct. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.

### Question 86 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Contiguous, fixed-duration, non-overlapping time buckets where each event belongs to one bucket define a tumbling window. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **B:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **C:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **D:** Correct. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.

### Question 87 — `A, D` (Describe an analytics workload on Azure)

Correct answers: A and D (are correct). Option 1 is Microsoft Fabric Real-Time Intelligence, and Option 2 is Apache Spark Structured Streaming. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Correct. Spark Structured Streaming treats a live event stream as an unbounded table processed via familiar Spark SQL/DataFrame APIs with checkpointed exactly-once guarantees.
- **B:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **C:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **D:** Correct. Fabric Real-Time Intelligence ingests and routes events via Eventstream, indexes high-volume telemetry in Eventhouse KQL databases, visualizes live tiles, and triggers Activator alerts.
- **E:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 88 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Azure Stream Analytics executes serverless SQL-like stream queries with built-in temporal windowing functions. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **B:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **C:** Correct. Azure Stream Analytics runs declarative Stream Analytics Query Language (`SELECT ... GROUP BY TumblingWindow(...)`) jobs joining live streams with reference data into sinks.
- **D:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.

### Question 89 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Azure Event Hubs is Azure's high-throughput partitioned event ingestion service supporting multiple downstream stream consumers. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **B:** Correct. Azure Event Hubs ingests millions of telemetry events per second into partitioned append logs (supporting native AMQP/HTTPS and Apache Kafka producers) for downstream stream consumers.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 90 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Microsoft Fabric Real-Time Intelligence provides Eventstream, Eventhouse (KQL databases), Real-Time Dashboards, and Activator. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **B:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **C:** Correct. Fabric Real-Time Intelligence ingests and routes events via Eventstream, indexes high-volume telemetry in Eventhouse KQL databases, visualizes live tiles, and triggers Activator alerts.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 91 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Power Query shaping, modeling, and report creation happen in Power BI Desktop; publishing, dashboard tile pinning, scheduled refresh, and App distribution happen in Power BI Service. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Incorrect. Dashboards are created in Power BI Service rather than Power BI Mobile, and dataset refresh plus secure sharing are managed in Power BI Service workspaces.
- **B:** Correct. Power BI Desktop handles Power Query prep, semantic modeling, and report design, while Power BI Service hosts scheduled refresh, multi-report dashboards, and governed App distribution.
- **C:** Incorrect. Paginated `.rdl` reports are authored in Power BI Report Builder, Stream Analytics processes event streams, and port `1433` is SQL Server TDS rather than BI sharing.
- **D:** Incorrect. Dashboards exist only in Power BI Service (not Power BI Desktop), Power BI Mobile is for consumption, and viewers consume shared Apps/reports in browser or mobile.

### Question 92 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Power BI Desktop is the local authoring environment for Power Query transformations, semantic modeling, DAX, and `.pbix` report design. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Correct. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **B:** Incorrect. Dashboards with pinned tiles across multiple reports are a cloud-only feature of Power BI Service, not Power BI Desktop.
- **C:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **D:** Incorrect. Power BI Service (`app.powerbi.com` / Fabric) hosts published semantic models and reports, pins cross-report dashboard tiles, schedules gateway refreshes, and distributes governed Apps.

### Question 93 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Power BI Report Builder creates pixel-perfect paginated (`.rdl`) reports designed to print every table row across multiple pages. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Incorrect. Power BI Service (`app.powerbi.com` / Fabric) hosts published semantic models and reports, pins cross-report dashboard tiles, schedules gateway refreshes, and distributes governed Apps.
- **B:** Incorrect. Azure Event Hubs ingests millions of telemetry events per second into partitioned append logs (supporting native AMQP/HTTPS and Apache Kafka producers) for downstream stream consumers.
- **C:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **D:** Correct. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 94 — `A, B` (Describe an analytics workload on Azure)

Correct answers: A and B (are correct). Configuring `1:*` relationships and drill-down hierarchies in a Power BI semantic model implements a star schema. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Correct. A Power BI semantic model defines `1:*` star-schema relationships, reusable DAX measures, drill-down hierarchies, and column metadata consumed across reports.
- **B:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **C:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **E:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 95 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Ratios of sums (`DIVIDE(SUM(...), SUM(...))`) must evaluate dynamically in the active filter context as a DAX measure rather than averaging row-level percentages. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **B:** Correct. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.

### Question 96 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Column default summarization, formatting, synonyms, and field visibility are governed in the Power BI semantic model. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **C:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **D:** Correct. A Power BI semantic model defines `1:*` star-schema relationships, reusable DAX measures, drill-down hierarchies, and column metadata consumed across reports.

### Question 97 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Data Analysis Expressions (DAX) is Power BI's formula language for dynamic measures, calculated columns, and calculated tables. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Correct. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **B:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **C:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **D:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.

### Question 98 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). A scatter (or bubble) chart plots two numeric measures on X/Y axes (plus optional bubble size) to reveal correlation, clusters, and outliers. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Incorrect. Pie/donut charts show part-to-whole shares for a few slices, while treemaps use nested rectangles to display proportional composition across larger hierarchical categories.
- **B:** Incorrect. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.
- **C:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **D:** Correct. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.

### Question 99 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). A Matrix visual aggregates values across both row and column hierarchies with expandable subtotals like a pivot table. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Correct. A Matrix aggregates measures across both row and column hierarchies like a pivot table, whereas Azure/Filled Maps plot spatial latitude/longitude or regional boundaries.
- **B:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **C:** Incorrect. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.
- **D:** Incorrect. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.

### Question 100 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). A Funnel chart visualizes sequential pipeline stages and progressive conversion/drop-off between stages. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
- **B:** Correct. Waterfall charts break down cumulative gains and losses between a starting and ending total, while Funnel charts track progressive drop-off across sequential pipeline stages.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
