# Microsoft Exam DP-900: Microsoft Azure Data Fundamentals — Full-Length Mock Exam 5

**Theme:** Digital Banking & Fraud Risk Operations — ACID Guarantees, 3NF, Elastic Pools/VMs, Cosmos Consistency & Azure Databricks  
**Credential:** `Microsoft Certified: Azure Data Fundamentals` *(Beginner / Fundamentals · **no prerequisite** · **never expires**)*  
**Study guide baseline:** `July 21, 2026` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `75 minutes` (`45 sec/question`, matching live 45-minute / 60-question pace; `45 minutes` optional speed drill · **closed-book**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn documentation — not affiliated with or endorsed by Microsoft Corporation. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Describe core data concepts (25–30% official weight · 28 questions)

### 1. CrestVault Digital Bank stores wire-transfer ledger rows in a SQL table with typed `TransferID`, `SenderIBAN`, `ReceiverIBAN`, and `AmountUSD` columns enforced across every entry. Which data representation is this?

- **A.** Unstructured data
- **B.** Semi-structured data
- **C.** Apache Avro row-based binary format with JSON schema
- **D.** Structured data

### 2. Treasury analysts maintain sovereign bond coupon schedules inside fixed tabular columns governed by `DATE`, `DECIMAL(18,4)`, and `CHAR(3)` currency types. How is this data classified?

- **A.** Unstructured data
- **B.** JavaScript Object Notation (JSON) document format
- **C.** Graph database (vertices and directed edges)
- **D.** Structured data

### 3. Open-banking payment webhooks send ISO-style `{}` payloads where domestic ACH transfers carry `routingNumber` keys and international SWIFT transfers carry nested `correspondentBanks[]` arrays without a fixed column grid. Which two items apply? Select two.

- **A.** Semi-structured data
- **B.** Structured data
- **C.** Page blobs in Azure Blob Storage
- **D.** Unstructured data
- **E.** JavaScript Object Notation (JSON) document format

### 4. Credit-bureau responses arrive as hierarchical XML documents with self-describing `<Tradeline>` and optional `<PublicRecord>` tags that vary per applicant. XML documents are an example of ____.

- **A.** Semi-structured data
- **B.** Structured data
- **C.** Unstructured data
- **D.** Clustered index (defines physical leaf-level sort order; maximum one per table)

### 5. CrestVault's card-authorization bus serializes millions of compact binary swipe records prefixed by an embedded JSON schema so fraud consumers handle schema evolution cleanly. Which data format is used?

- **A.** Line chart (tracking continuous trends and changes over ordered time intervals)
- **B.** Apache Avro row-based binary format with JSON schema
- **C.** Page blobs in Azure Blob Storage
- **D.** Delimited text format (CSV or TSV)

### 6. KYC onboarding workflows archive passport selfie `.jpg` photos, video-verification `.mp4` clips, and recorded compliance disclosure `.wav` audio files in Blob containers. Together, these assets are ____.

- **A.** Apache Parquet columnar storage format
- **B.** Semi-structured data
- **C.** Unstructured data
- **D.** Structured data

### 7. Scanned wet-signature mortgage deed `.pdf` bundles and notarized affidavit `.tiff` images are stored in cloud object storage. Which data classification applies to these files?

- **A.** Unstructured data
- **B.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **C.** Composite key (multi-column key)
- **D.** Structured data

### 8. CrestVault's regulatory team exports a 300-row interest-rate table as comma-separated plain text for external auditors, while risk quants store 15 billion historical trade ticks in compressed columnar files for fast Spark scans. Which two file formats match these two scenarios? Select two.

- **A.** Apache Parquet columnar storage format
- **B.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **C.** Delimited text format (CSV or TSV)
- **D.** Page blobs in Azure Blob Storage
- **E.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)

### 9. A Basel capital-adequacy query reads only `CounterpartyRating` and `ExposureEAD` out of a 110-column portfolio dataset in OneLake. Storing the dataset in ____ skips reading the other 108 columns from disk.

- **A.** JavaScript Object Notation (JSON) document format
- **B.** Append blobs in Azure Blob Storage
- **C.** Delimited text format (CSV or TSV)
- **D.** Apache Parquet columnar storage format

### 10. A legacy risk cluster running Apache Hive queries compressed columnar stripes with stripe-level min/max indexes over ten years of loan-servicing snapshots. Which file format matches this layout?

- **A.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **B.** Optimized Row Columnar (ORC) stripe format
- **C.** Page blobs in Azure Blob Storage
- **D.** Delimited text format (CSV or TSV)

### 11. CrestVault's financial-crime unit models accounts, devices, and IP addresses as vertices connected by `SENT_FUNDS` and `SHARED_DEVICE` edges to uncover mule rings, while storing flexible JSON dispute dossiers in an indexed collection. Which two database categories fit? Select two.

- **A.** Graph database (vertices and directed edges)
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Document database
- **D.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **E.** Delimited text format (CSV or TSV)

### 12. A mobile-banking login service caches encrypted OAuth nonce tokens looked up solely by `NonceKey` with sub-millisecond latency and zero table joins. Which non-relational store category is ideal?

- **A.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **B.** Graph database (vertices and directed edges)
- **C.** Key-value non-relational store
- **D.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)

### 13. An algorithmic market-data feed writes millions of order-book ticks per second grouped into `bid_depth` and `ask_depth` column families keyed by `TickerSymbol` and timestamp. Which non-relational category matches?

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Column-family (wide-column) database
- **C.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)
- **D.** Database view (saved virtual `SELECT` query)

### 14. CrestVault is designing its cloud data estate from live checking-account debit/credit postings through board-level net-interest-margin dashboards. Which four-step Azure service flow is sound?

- **A.** Land raw checkout clicks in Paginated Reports → Transform via SMB file locks → Commit ACID transactions in Azure Blob Cold tier → Query via Gremlin graph vertices
- **B.** Capture OLTP writes directly in Archive Blob tier → Run live checkout queries in Power BI Desktop → Copy rows to Azure Files SMB → Normalize into Azure Table storage
- **C.** Capture OLTP writes in Azure SQL Database → Extract changes via Data Factory pipeline → Land Parquet files in ADLS Gen2 / OneLake → Serve star-schema visuals in Power BI
- **D.** Serve live checkout writes in Power BI Service → Export dashboards to CSV → Load CSVs into Azure SQL Database → Archive active rows to Azure Queue storage

### 15. Proposed solution: For a greenfield savings-account microservice requiring strict relational constraints, foreign keys, and ACID multi-row transfers without OS management, the architect selects ____. Does this Azure PaaS datastore fit?

- **A.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

### 16. CrestVault's global travel-card app serves cardholders in London, Singapore, and New York needing `<10 ms` JSON profile reads/writes and automatic multi-region replication. Which Azure database capability meets this need?

- **A.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Cold access tier (online, 90-day minimum retention for rarely accessed data)
- **D.** Azure Cosmos DB turnkey global distribution with multi-region writes and <10 ms SLAs

### 17. When transferring `$500` from Checking to Savings, debiting Checking and crediting Savings must execute all-or-nothing, `CheckingBalance >= 0` constraints must hold, and once confirmed the transfer must survive an immediate server power failure. Which three ACID properties are described? Select three.

- **A.** Online Analytical Processing (OLAP) workload
- **B.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **C.** Durability (committed writes survive restarts or crashes)
- **D.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **E.** Consistency (valid schema and constraint state)
- **F.** Atomicity (all-or-nothing transaction unit)

### 18. Two ATMs attempt to withdraw `$300` simultaneously from an account holding `$400`; transaction locking/versioning prevents both ATMs from reading the initial `$400` concurrently and overdrawing the account. Which ACID property enforces this?

- **A.** Apache Parquet columnar storage format
- **B.** Online Analytical Processing (OLAP) workload
- **C.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **D.** Isolation (concurrent transactions do not interfere)

### 19. Proposed solution: Core card-clearing engines process 15,000 normalized `INSERT` and `UPDATE` ledger transactions per second with millisecond response times, so the architect classifies card clearing as an ____ rather than OLAP. Is this accurate?

- **A.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **B.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **C.** Online Transaction Processing (OLTP) workload
- **D.** Online Analytical Processing (OLAP) workload

### 20. CrestVault's CFO team queries 8 years of historical loan originations, defaults, and net spreads across `FactLoanBalances` joined in one hop to `DimBranch`, `DimProduct`, and `DimCalendar`. Which two concepts describe this system? Select two.

- **A.** Online Transaction Processing (OLTP) workload
- **B.** Online Analytical Processing (OLAP) workload
- **C.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **D.** Page blobs in Azure Blob Storage
- **E.** Isolation (concurrent transactions do not interfere)

### 21. Risk actuaries run quarterly stress-test aggregations scanning 900 million historical mortgage payment rows in a warehouse isolated from live teller terminals. Which workload category is this?

- **A.** Online Analytical Processing (OLAP) workload
- **B.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **C.** Online Transaction Processing (OLTP) workload
- **D.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)

### 22. In CrestVault's treasury warehouse, `FactTrades` joins to `DimInstrument`, which normalizes into `DimAssetSubClass`, which normalizes into `DimAssetClass`. What dimensional schema pattern is this?

- **A.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **B.** Append blobs in Azure Blob Storage
- **C.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **D.** First Normal Form (1NF — atomic values and no repeating column groups)

### 23. At CrestVault, which data professional configures Always Encrypted / TDE, manages Microsoft Entra SQL roles, tests geo-failover drills, and tunes slow OLTP query plans on core banking servers?

- **A.** Database administrator (DBA)
- **B.** Data analyst
- **C.** Data engineer
- **D.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)

### 24. Regulators ask CrestVault to prove it can restore a corrupted operational loan database to `14:22:00 UTC` from automated transaction-log backups. Which specialist executes and certifies this point-in-time restore?

- **A.** Database administrator (DBA)
- **B.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **C.** Data analyst
- **D.** Data engineer

### 25. CrestVault is building a unified credit-risk analytics platform spanning Azure SQL, Microsoft Fabric Lakehouse, and Power BI. Which four-step sequence assigns duties properly across DBA, data engineer, and data analyst?

- **A.** DBA provisions & secures operational Azure SQL → Data engineer builds ELT pipelines into Fabric Lakehouse → Data engineer curates Gold star-schema tables → Data analyst models DAX KPIs & publishes Power BI reports
- **B.** Data analyst configures SQL Server failover clusters → DBA authors Spark ELT notebooks in Databricks → Data engineer designs executive Power BI visuals → DBA schedules workspace app audiences
- **C.** Data engineer grants T-SQL row permissions on OLTP → Data analyst provisions Azure VNet private endpoints → DBA builds Power Query Dataflows Gen2 → Data analyst runs point-in-time DB restores
- **D.** DBA designs executive KPI scorecards → Data analyst writes Spark Structured Streaming checkpoints → Data engineer tunes OLTP clustered indexes → DBA publishes paginated sales packs

### 26. Who authors PySpark notebooks and Fabric Data Factory pipelines to ingest raw SWIFT messages, standardize currency ISO codes, and write validated Silver and Gold Delta tables?

- **A.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **B.** Database administrator (DBA)
- **C.** Data engineer
- **D.** Data analyst

### 27. CrestVault's retail banking VP wants an interactive branch profitability Power BI report featuring DAX `Net Interest Margin %` measures and regional cohort visuals. Which role builds this report?

- **A.** Data engineer
- **B.** Data analyst
- **C.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **D.** Database administrator (DBA)

### 28. Connecting Power BI Desktop to Gold delinquency tables, a specialist models `30/60/90+ Days Past Due` DAX metrics and designs visual drill-downs for credit officers. This specialist works as a ____.

- **A.** Database administrator (DBA)
- **B.** Data engineer
- **C.** Data analyst
- **D.** Append blobs in Azure Blob Storage

---

## Domain 2 — Identify considerations for relational data on Azure (20–25% official weight · 24 questions)

### 29. In CrestVault's relational ledger, `Accounts.AccountID` uniquely identifies each account without `NULL`s, and `LedgerEntries.AccountID` references `Accounts.AccountID` so entries cannot post to nonexistent accounts. Which two constraints are used? Select two.

- **A.** Unstructured data
- **B.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **C.** Primary key constraint
- **D.** Foreign key constraint
- **E.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)

### 30. In a `JointAccountHolders` junction table linking `AccountID` and `CustomerID`, the pair `(AccountID, CustomerID)` together uniquely identifies each ownership link. This multi-column identifier is a ____.

- **A.** Page blobs in Azure Blob Storage
- **B.** Apache Avro row-based binary format with JSON schema
- **C.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **D.** Composite key (multi-column key)

### 31. Which relational database constraint prevents deleting a `Branches` row while active `Loans` rows still reference that `BranchCode`?

- **A.** Waterfall chart (sequential positive/negative variance steps) or Funnel chart (linear stage conversion drop-off)
- **B.** Foreign key constraint
- **C.** First Normal Form (1NF — atomic values and no repeating column groups)
- **D.** Append blobs in Azure Blob Storage

### 32. Why can a relational table have many `UNIQUE` constraints if needed, yet every primary identifier designated as the table's ____ automatically forbids `NULL` values and serves as the default parent target for foreign keys?

- **A.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **B.** Primary key constraint
- **C.** Cool access tier (online, 30-day minimum retention for infrequently accessed data)
- **D.** Foreign key constraint

### 33. CrestVault's commercial lending team wants to refactor an unnormalized spreadsheet containing multi-valued collateral lists and duplicated branch-manager phone numbers into a 3NF relational database. Which four-step sequence is valid?

- **A.** Cluster-index raw JSON blobs → Delete primary keys on parent tables → Copy supplier city into every invoice item (2NF) → Combine product names into pipe-delimited strings (3NF)
- **B.** Create foreign keys on unsplit multi-value columns → Denormalize all lookup tables into one wide sheet → Remove partial dependencies (2NF) → Split atomic columns into repeating groups (1NF)
- **C.** Remove transitive non-key dependencies (3NF) → Merge comma-separated phone lists into one column → Delete all primary keys to speed inserts → Duplicate customer addresses across every order line
- **D.** Split repeating groups into atomic columns (1NF) → Assign a unique primary key → Move partial composite-key dependencies to parent tables (2NF) → Extract transitive non-key dependencies into lookup tables (3NF)

### 34. A `LoanApplications` staging table stores `CoBorrowerNames` as `'Alice Chen, Marco Diaz'` in one column and includes `Phone1` and `Phone2` columns. Splitting those into atomic single-valued cells and child rows achieves ____.

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **C.** First Normal Form (1NF — atomic values and no repeating column groups)
- **D.** Star schema (central numeric fact table joined directly to denormalized dimension tables)

### 35. In a 1NF `PortfolioHoldings` table keyed by `(PortfolioID, SecurityISIN)`, column `IssuerName` depends solely on `SecurityISIN`. Moving `IssuerName` to a `Securities` parent table satisfies ____.

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **C.** First Normal Form (1NF — atomic values and no repeating column groups)
- **D.** Second Normal Form (2NF — full functional dependency on the entire composite key)

### 36. In a 2NF `Cards` table keyed by `CardNumber`, non-key column `CardTierCode` (`PLATINUM`) determines `AnnualFeeUSD` (`$495`). Moving `CardTierCode -> AnnualFeeUSD` into a `CardTiers` lookup table eliminates update anomalies and achieves ____.

- **A.** First Normal Form (1NF — atomic values and no repeating column groups)
- **B.** Apache Parquet columnar storage format
- **C.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **D.** Second Normal Form (2NF — full functional dependency on the entire composite key)

### 37. An audit log captures three SQL statements on CrestVault's database: `CREATE TABLE WireHolds (...)`, `INSERT INTO WireHolds VALUES (...)`, and `REVOKE INSERT ON WireHolds FROM InternRole`. Which three SQL categories are used? Select three.

- **A.** Page blobs in Azure Blob Storage
- **B.** Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- **C.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **D.** JavaScript Object Notation (JSON) document format
- **E.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **F.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)

### 38. A fraud analyst writes `SELECT AccountID, COUNT(*) FROM CardSwipes ____ Country <> 'US' GROUP BY AccountID ____ COUNT(*) >= 10;`. Which pair of SQL clauses filters pre-grouped foreign swipes first and grouped counts `>= 10` second?

- **A.** Place `SUM()` or `COUNT(*)` aggregate predicates directly inside the SQL `WHERE` clause before `GROUP BY`
- **B.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **C.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **D.** `WHERE` filters rows before grouping; `HAVING` filters aggregated groups after `GROUP BY`

### 39. CrestVault wants a compliance query listing **every** wealth-management client from `Clients` alongside any `SuspiciousActivityReports` filed, returning `NULL` report columns for the 99.8% of clients with zero filings. Which join is required?

- **A.** Use DML `SELECT` and `INSERT` statements to grant or revoke user login permissions on schemas
- **B.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **C.** `LEFT OUTER JOIN` preserving all left-table rows with `NULL` when right-table matches are absent
- **D.** `INNER JOIN` matching related keys present in both tables

### 40. Proposed solution: To adhere to least-privilege banking rules, the DBA executes `GRANT SELECT ON vw_MaskedBalances TO AuditTeam` and `DENY SELECT ON RawCards TO AuditTeam`, categorizing both commands as ____. What completes this statement?

- **A.** Use DML `SELECT` and `INSERT` statements to grant or revoke user login permissions on schemas
- **B.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **C.** Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)

### 41. CrestVault exposes `vw_TellerAccountSummary` to hide full tax-ID numbers behind a virtual `SELECT` query, and requires wire apps to invoke `EXEC usp_SubmitWire` so AML checks and ledger debits run inside precompiled server SQL. Which two database objects are used? Select two.

- **A.** Stored procedure (parameterized precompiled SQL routine)
- **B.** Optimized Row Columnar (ORC) stripe format
- **C.** Database view (saved virtual `SELECT` query)
- **D.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **E.** Append blobs in Azure Blob Storage

### 42. On `LedgerEntries`, defining a ____ on `EntrySequenceID` stores the table's actual leaf data pages sorted physically by `EntrySequenceID`, which is why only one such index can exist per table.

- **A.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **B.** Create four separate clustered indexes on the same relational table to sort rows four ways physically
- **C.** Database view (saved virtual `SELECT` query)
- **D.** Nonclustered index (separate B-tree structure with row locators; multiple allowed per table)

### 43. Fraud investigators query `LedgerEntries` (clustered on `EntrySequenceID`) by `MerchantMCC` and `CardHash`. Creating ____ structures on those columns adds separate B-tree lookup structures pointing back to the base rows.

- **A.** Nonclustered index (separate B-tree structure with row locators; multiple allowed per table)
- **B.** Create four separate clustered indexes on the same relational table to sort rows four ways physically
- **C.** Stored procedure (parameterized precompiled SQL routine)
- **D.** Clustered index (defines physical leaf-level sort order; maximum one per table)

### 44. Why does querying a standard SQL ____ always reflect the latest committed balances in `Accounts` without requiring scheduled refresh jobs?

- **A.** Database view (saved virtual `SELECT` query)
- **B.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **C.** Page blobs in Azure Blob Storage
- **D.** Stored procedure (parameterized precompiled SQL routine)

### 45. CrestVault plans to migrate 22 on-premises SQL Server core-banking databases to Azure SQL PaaS. Which four-step workflow follows current Microsoft migration guidance?

- **A.** Assess SQL Server readiness and SKU sizing in Azure Migrate → Select Azure SQL Database or Managed Instance → Provision target with Entra auth and TLS firewall rules → Migrate schema/data and cut over connection strings
- **B.** Point production apps to an empty Azure SQL server → Open firewall `0.0.0.0-255.255.255.255` to the public internet → Assess SQL Agent blockers after cutover → Export tables manually as JPEG screenshots
- **C.** Disable TLS encryption on SQL Server → Copy `.mdf` files directly into Azure Table storage → Provision Azure SQL Database Basic tier for cross-DB SQL Agent jobs → Run Azure Migrate discovery
- **D.** Convert relational tables into Azure Queue messages → Provision SQL Managed Instance without VNet planning → Run compatibility assessment last → Remove all primary keys before cutover

### 46. CrestVault hosts two distinct SQL workloads on Azure: (1) 250 independent credit-union single databases in PaaS sharing a pooled vCore budget across staggered peak hours; (2) a legacy check-imaging app requiring Windows Server 2019 OS registry access and SQL Server 2017 IaaS control. Which two offerings match? Select two.

- **A.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **B.** Run the retired standalone Data Migration Assistant (DMA) desktop tool as Microsoft’s current cloud sizing service
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Azure SQL Database Elastic Pool (shared eDTU or vCore compute across multi-tenant DBs)
- **E.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 47. A treasury settlement database uses SQL Server Agent multi-step schedules, Service Broker queues, and cross-database three-part queries, and leadership wants managed PaaS with automated patching and backups. Which Azure SQL service fits?

- **A.** Use a single Azure SQL Database to run native SQL Server Agent jobs and cross-database three-part queries
- **B.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **C.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 48. CrestVault's quarterly regulatory stress-test SQL database runs heavy simulations for three days per quarter and sits completely idle the other 87 days. Which Azure SQL Database compute tier auto-scales vCores when active and auto-pauses compute when idle?

- **A.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **B.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **C.** Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)
- **D.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)

### 49. To eliminate hardcoded SQL connection passwords across 60 banking microservices, CrestVault authenticates App Service and AKS workloads to Azure SQL using managed identities backed by ____.

- **A.** Delimited text format (CSV or TSV)
- **B.** Cold access tier (online, 90-day minimum retention for rarely accessed data)
- **C.** Microsoft Entra ID centralized authentication with MFA and passwordless managed identities
- **D.** Run the retired standalone Data Migration Assistant (DMA) desktop tool as Microsoft’s current cloud sizing service

### 50. CrestVault's quantitative FX pricing service uses PostgreSQL custom composite types, `PL/pgSQL` functions, and `pgAdmin`, and requires managed Azure PaaS with built-in zone-redundant high availability. Which service fits?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **C.** Azure Database for MySQL — Flexible Server
- **D.** Azure Database for PostgreSQL — Flexible Server

### 51. CrestVault's financial-literacy blog runs on a `LAMP` (`Linux, Apache, MySQL, PHP`) stack and needs a managed Azure PaaS relational service with automated backups and up to 35-day point-in-time restore. Which service fits?

- **A.** Azure Database for PostgreSQL — Flexible Server
- **B.** Azure Database for MySQL — Flexible Server
- **C.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **D.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)

### 52. Which open-source Azure PaaS relational service is classified as an **object-relational** database supporting custom data types, geometric objects, `PL/pgSQL`, and Query Store metrics in `azure_sys`?

- **A.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **B.** Azure Database for PostgreSQL — Flexible Server
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

---

## Domain 3 — Describe considerations for working with non-relational data on Azure (15–20% official weight · 20 questions)

### 53. Monthly PDF bank statements are downloaded heavily for 30 days, occasionally up to day 90, rarely through month 12, and retained 7 years for SEC/banking compliance. Which four-step Blob Storage lifecycle sequence minimizes storage cost?

- **A.** Ingest active operational files directly into Archive tier → Serve millisecond web downloads from Archive without rehydration → Move 90-day files to Hot tier → Delete storage account container metadata
- **B.** Ingest active files into Hot access tier → Transition 30-day infrequent blobs to Cool tier → Move 90-day rarely read blobs to Cold tier → Transition 365-day compliance blobs to offline Archive tier (rehydrating when needed)
- **C.** Write unstructured video files into Azure Table `RowKey` cells → Age rows from Cool to Hot after 180 days → Convert Page blobs into SQL views → Rehydrate Cool blobs for 12 hours before reading
- **D.** Mount Archive blobs as an SMB network drive → Stream live append logs into Page blobs in Cold tier → Transition 1-year compliance archives to Hot tier → Rehydrate Hot blobs before every read

### 54. CrestVault archives 2 PB of 6-year-old check-front `.tiff` images that have a 7-year legal hold and are almost never read (12-hour retrieval is acceptable). Which blob type and access tier combination minimizes cost? Select two.

- **A.** Page blobs in Azure Blob Storage
- **B.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **C.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **D.** Block blobs in Azure Blob Storage
- **E.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 55. Immutable SWIFT gateway wire logs are written sequentially by appending new blocks solely to the end of daily log blobs without modifying earlier entries. Which Azure Blob type is optimized for this?

- **A.** Store active operational files directly in Azure Blob Archive tier for immediate millisecond web reads
- **B.** Append blobs in Azure Blob Storage
- **C.** Page blobs in Azure Blob Storage
- **D.** Block blobs in Azure Blob Storage

### 56. CrestVault's risk data lake requires POSIX access-control lists (`ACLs`) on subdirectories and atomic directory rename operations for Spark Parquet jobs on Azure Storage. Which feature provides this?

- **A.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **B.** Page blobs in Azure Blob Storage
- **C.** Azure Data Lake Storage Gen2 (Blob Storage with Hierarchical Namespace enabled)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 57. Mobile banking app icons, active promo banners, and intraday FX rate JSON files are read thousands of times per second and overwritten every minute. Which Azure Blob access tier provides the lowest read/write transaction cost?

- **A.** Hot access tier (highest storage rate, lowest read/write access cost)
- **B.** Store active operational files directly in Azure Blob Archive tier for immediate millisecond web reads
- **C.** Cold access tier (online, 90-day minimum retention for rarely accessed data)
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 58. CrestVault's mortgage underwriting offices use legacy Windows apps mapped to `\\corpfiles\underwriting` over `SMB 3.0` and want local branch Windows Server caching with automatic cloud tiering of closed loan folders. Which two Azure services fit? Select two.

- **A.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **B.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **C.** Append blobs in Azure Blob Storage
- **D.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **E.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 59. A Linux risk-simulation grid mounts a shared `NFS 4.1` directory across 32 compute nodes to read shared yield-curve config files concurrently. Which Azure Storage service provides managed `NFS 4.1` file shares?

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Block blobs in Azure Blob Storage
- **C.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 60. Which Azure service synchronizes multiple on-premises Windows Server file shares with a central Azure Files share while keeping recently accessed files cached locally at branch offices?

- **A.** Azure Data Lake Storage Gen2 (Blob Storage with Hierarchical Namespace enabled)
- **B.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **C.** Azure Stream Analytics (serverless SQL-like stream processing engine with windowing functions)
- **D.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)

### 61. CrestVault stores 150 million ATM heartbeat status records keyed by `RegionCode` (`PartitionKey`) and `AtmTerminalID` (`RowKey`) in a low-cost schemaless key-value store within an Azure Storage account. Which service is this?

- **A.** Enforce server-side foreign keys and multi-table SQL `INNER JOIN` queries inside Azure Table storage
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 62. When CrestVault's `PartitionKey`/`RowKey` card-token lookup service requires multi-region active-active writes, automatic secondary indexing, and `<10 ms` latency SLAs, which offering upgrades Azure Table storage cleanly?

- **A.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **B.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Page blobs in Azure Blob Storage

### 63. Proposed solution: An engineer proposes running server-side `JOIN` queries across three tables in Azure Table storage to reconcile ledger balances; the architect declines because ____ supports key-value lookups by `PartitionKey`/`RowKey` without server-side joins or foreign keys. Which service is described?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Enforce server-side foreign keys and multi-table SQL `INNER JOIN` queries inside Azure Table storage
- **C.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **D.** Clustered index (defines physical leaf-level sort order; maximum one per table)

### 64. Compare the two ends of Azure Cosmos DB's five-level consistency spectrum: which level guarantees **linearizable reads of the latest committed write**, and which level offers the **lowest latency/RU cost with no ordering guarantee**? Select two.

- **A.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **B.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **C.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **E.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)

### 65. When a CrestVault customer updates spending-alert thresholds in the mobile app backed by Cosmos DB, which **default** consistency level guarantees that customer's app session immediately reads back its own updated thresholds?

- **A.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **B.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating
- **C.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)
- **D.** Session consistency (default level guaranteeing read-your-own-writes and monotonic reads per client session)

### 66. CrestVault deploys a sporadic internal compliance bot on Azure Cosmos DB and selects **Serverless** mode so it pays strictly for the ____ consumed by actual database reads and writes with zero minimum hourly charge.

- **A.** Bar or column chart (comparing discrete categorical values across items)
- **B.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **C.** Page blobs in Azure Blob Storage
- **D.** Request Units (RUs) normalized compute/IO currency (Provisioned, Autoscale, or Serverless)

### 67. Why does CrestVault select Azure Cosmos DB for its global cardholder session store across Zurich, São Paulo, Virginia, and Tokyo?

- **A.** Azure Cosmos DB turnkey global distribution with multi-region writes and <10 ms SLAs
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **D.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)

### 68. CrestVault is deploying a new JSON payment-dispute microservice on Azure Cosmos DB partitioned by `/accountId`. Which four-step sequence follows Cosmos DB best practices?

- **A.** Create a container without a partition key → Switch the existing account between Cassandra, Gremlin, and NoSQL APIs daily → Enforce 3NF foreign-key joins across containers → Store 500 MB MP4 blobs inside single JSON items
- **B.** Provision an Azure Files SMB share → Enable Strong consistency across 5 multi-write regions simultaneously → Omit databases and write JSON straight to subscription tags → Query vertices using `SMB2` locks
- **C.** Install OS patches on Cosmos DB virtual machines → Format NTFS volumes for JSON items → Assign a constant single-value partition key to all 100 million documents → Query exclusively with T-SQL stored procedures
- **D.** Create a Cosmos DB account choosing the target API → Create a database and container with a high-cardinality partition key → Configure RU/s or serverless and consistency → Insert items and run partition-scoped queries

### 69. CrestVault's anti-money-laundering (`AML`) engine models bank accounts, shell companies, and devices as vertices and wire transfers as directed edges to detect circular layering rings. Which Azure Cosmos DB API fits?

- **A.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **B.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **C.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 70. A greenfield Java Spring microservice stores JSON cardholder notifications in Cosmos DB and queries them with `SELECT c.alertId, c.severity FROM c WHERE c.accountId = 'A771'`. Which Cosmos DB API is used?

- **A.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **B.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **C.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating
- **D.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)

### 71. CrestVault acquires a fintech wealth-robo-advisor whose Node.js backend stores BSON client portfolios via MongoDB drivers and wants managed Cosmos DB global replication via connection-string cutover. Which API fits?

- **A.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **B.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **C.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **D.** Azure Cosmos DB for MongoDB (wire-protocol compatibility for BSON document apps)

### 72. A market-surveillance ticker store written with Apache Cassandra `CQL` drivers needs managed multi-region Azure PaaS hosting without rewriting `CQL` statements. Which Cosmos DB API should be provisioned?

- **A.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **B.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating
- **C.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

---

## Domain 4 — Describe an analytics workload on Azure (25–30% official weight · 28 questions)

### 73. CrestVault consolidates core banking, card, and treasury feeds into Microsoft Fabric OneLake using a medallion architecture. Which four-step workflow implements ELT?

- **A.** Build Power BI visuals directly against uncleaned CSV attachments → Delete raw source history immediately → Normalize Gold tables into 3NF OLTP row stores → Export final aggregates back into email inboxes
- **B.** Publish Gold star schema before ingesting source data → Run OLTP checkout locks inside Power BI Mobile → Overwrite source ERP primary keys during read → Store Parquet files in DNS TXT records
- **C.** Extract source data via Data Factory pipeline → Land raw files into OneLake / ADLS Gen2 (Bronze) → Cleanse and conform Delta tables via Spark or SQL (Silver) → Model star-schema fact/dimension tables (Gold) for BI
- **D.** Transform terabytes on the client laptop in Notepad → Upload screenshots to Archive Blob tier → Query offline blobs live with DAX → Store fact tables inside Azure Queue messages

### 74. Proposed solution: PCI-DSS scope rules forbid raw 16-digit Primary Account Numbers (`PAN`) from ever landing in analytical cloud storage, so CrestVault tokenizes `PAN` fields inside an intermediate pipeline stage **before** writing rows into the warehouse — an example of ____. Is this classification right?

- **A.** Extract, Transform, and Load (ETL) pattern
- **B.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)
- **C.** Extract, Load, and Transform (ELT) pattern
- **D.** Page blobs in Azure Blob Storage

### 75. Which Microsoft cloud data-integration service provides 90+ connectors, Copy activity pipelines, and Power Query Dataflows Gen2 to orchestrate nightly banking batch loads?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Azure Data Factory / Fabric Data Factory pipelines and Dataflows Gen2
- **C.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **D.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)

### 76. CrestVault stores governed analytical tables as open **Delta Lake** Parquet files in OneLake (`FactCardSpend`) surrounded by single-hop `DimMerchant`, `DimCardholder`, and `DimDate` tables. Which two analytical concepts combine here? Select two.

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **C.** Data lakehouse (Delta Lake ACID transactions and SQL/Spark queries directly over open Parquet files)
- **D.** Append blobs in Azure Blob Storage
- **E.** Online Transaction Processing (OLTP) workload

### 77. When `DimBranch` in CrestVault's analytical warehouse is normalized into `DimBranch -> DimDistrict -> DimDivision`, the warehouse model follows a ____.

- **A.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **B.** Key-value non-relational store
- **C.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 78. In Microsoft Fabric, **Shortcuts** let CrestVault's Lakehouse reference existing ADLS Gen2 Parquet risk folders virtually in ____ without copying or duplicating bytes across storage accounts.

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Page blobs in Azure Blob Storage
- **C.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **D.** Microsoft OneLake (single tenant-wide SaaS data lake built into Microsoft Fabric)

### 79. CrestVault's cloud architecture standards approve three enterprise analytics services on Azure: unified SaaS analytics atop OneLake, collaborative Apache Spark + ML notebooks with Unity Catalog, and PaaS serverless/dedicated SQL + Spark pools in Synapse Studio. Which three services are these? Select three.

- **A.** Azure Synapse Analytics (serverless SQL pools, dedicated MPP SQL pools, and Spark pools)
- **B.** Microsoft Fabric (unified SaaS analytics platform atop OneLake)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **E.** Azure Databricks (collaborative Apache Spark analytics, Delta Lake, and ML platform)
- **F.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 80. CrestVault's quantitative fraud-modeling team trains gradient-boosted Spark ML pipelines over 80 TB of historical card features in collaborative Python/Scala notebooks with MLflow tracking. Which Azure service is tailored for this?

- **A.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **B.** Azure Databricks (collaborative Apache Spark analytics, Delta Lake, and ML platform)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

### 81. Risk analysts run ad-hoc T-SQL queries directly over raw Parquet files in ADLS Gen2 without provisioning warehouse clusters by using a **serverless SQL pool** inside ____.

- **A.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **B.** Azure Synapse Analytics (serverless SQL pools, dedicated MPP SQL pools, and Spark pools)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)

### 82. An acquired brokerage firm relies on custom Apache HBase and Hadoop MapReduce risk jobs and wants managed open-source Hadoop/HBase clusters on Azure during transition. Which service fits?

- **A.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **B.** Azure HDInsight (managed open-source Hadoop, Hive, HBase, Kafka, and Spark clusters)
- **C.** Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)
- **D.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)

### 83. CrestVault scores every incoming contactless card tap against velocity-fraud rules in under 150 milliseconds while the shopper stands at the terminal. Processing unbounded events continuously in flight is ____.

- **A.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **B.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **C.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 84. On the 1st business day of each month, CrestVault calculates monthly savings interest accruals across 12 million accounts and generates statement summaries. This scheduled job over bounded monthly balances is ____.

- **A.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **B.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)
- **C.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **D.** Session window (variable-length activity bursts closed after a quiet timeout gap)

### 85. A velocity-fraud rule triggers an alert whenever a single card executes **more than 4 transactions within any rolling 90-second span**, evaluating immediately as swipes enter or age out of the 90-second window. Which window type fits?

- **A.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **B.** Apache Parquet columnar storage format
- **C.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **D.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)

### 86. Every 10 seconds, CrestVault's payment gateway emits the 1-minute rolling decline percentage across Visa/Mastercard rails (a 60-second window advancing every 10 seconds). Which overlapping scheduled window function is this?

- **A.** Optimized Row Columnar (ORC) stripe format
- **B.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **C.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **D.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)

### 87. CrestVault ingests 400,000 payment authorization events per second into a partitioned Azure event broker and runs serverless SQL-like window queries joining live swipes against a `HighRiskCountries` reference file. Which two Azure services pair together? Select two.

- **A.** Azure Stream Analytics (serverless SQL-like stream processing engine with windowing functions)
- **B.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **E.** Azure Event Hubs (high-throughput partitioned event ingestion broker with Kafka support)

### 88. In Microsoft Fabric, CrestVault captures live ATM telemetry via **Eventstream**, stores billions of indexed events in an **Eventhouse** `KQL` database, visualizes live ops tiles, and fires cash-low alerts via **Activator**. Which Fabric workload is this?

- **A.** Cold access tier (online, 90-day minimum retention for rarely accessed data)
- **B.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **C.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **D.** Microsoft Fabric Real-Time Intelligence (Eventstream, Eventhouse KQL database, Real-Time Dashboards, and Activator)

### 89. Data engineers in Azure Databricks consume Kafka payment streams as unbounded DataFrames using checkpointed `readStream` / `writeStream` logic into Delta tables. Which streaming engine is used?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **C.** Apache Spark Structured Streaming (fault-tolerant DataFrame/SQL stream processing in Databricks and Fabric)
- **D.** Database view (saved virtual `SELECT` query)

### 90. CrestVault's treasury monitor totals wire volume in strict non-overlapping 5-minute buckets (`09:00–09:05`, `09:05–09:10`) so every wire is counted in exactly one 5-minute interval. Which window function is used?

- **A.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **B.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **C.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **D.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)

### 91. CrestVault's BI team wants to shape warehouse tables, author DAX risk metrics, pin a CRO executive dashboard, and distribute a governed read-only App to 200 risk officers. Which four-step Power BI sequence applies?

- **A.** Shape source data with Power Query in Power BI Desktop → Relate star-schema tables, write DAX, and build report pages → Publish model and report to Power BI Service → Pin dashboard tiles, schedule refresh, and share an App
- **B.** Pin dashboard tiles in Power BI Desktop offline → Write Power Query M transformations inside Power BI Mobile → Store semantic models on SMB floppy shares → Require every executive viewer to edit DAX in Desktop
- **C.** Design `.rdl` pixel-perfect invoices in Azure Stream Analytics → Publish directly to unmanaged personal OneDrive as an OLTP database → Disable table relationships → Share via anonymous firewall port `1433`
- **D.** Author multi-report dashboards inside Power BI Mobile → Export `.pbix` files to Azure Table storage → Schedule dataset refresh inside Windows Notepad → Email raw database passwords to report viewers

### 92. Federal bank examiners require a formatted 180-page PDF **Loan Exception Register** printing every flagged loan row with fixed page headers, footers, and exact pagination (`.rdl`). Which Power BI tool builds this?

- **A.** Azure Stream Analytics (serverless SQL-like stream processing engine with windowing functions)
- **B.** Microsoft Power BI Service (cloud SaaS portal for workspaces, dashboards, scheduled refresh, and Apps)
- **C.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

### 93. Proposed solution: A risk analyst wants executives to receive automated morning email subscriptions and view a single dashboard pinning tiles from three separate `.pbix` reports, so the analyst publishes the reports and builds the dashboard in ____. Does this use the right Power BI component?

- **A.** Microsoft Power BI Service (cloud SaaS portal for workspaces, dashboards, scheduled refresh, and Apps)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Create multi-report pinned dashboards directly inside Power BI Desktop offline
- **D.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)

### 94. In Power BI Desktop, an analyst links `DimBranch` and `DimDate` (`1`) to `FactDeposits` (`*`), hides surrogate integer keys, and writes `Loan-to-Deposit Ratio := DIVIDE([TotalLoans], [TotalDeposits])`. Which two modeling concepts are applied? Select two.

- **A.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **B.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Power BI semantic model (relationships, DAX measures, hierarchies, and Import/DirectQuery/Direct Lake storage)
- **E.** Append blobs in Azure Blob Storage

### 95. Why must CrestVault calculate `Net Charge-Off Rate %` as a ____ rather than summing or averaging precalculated row-level percentages when executives filter by product, vintage, or state?

- **A.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **B.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **C.** Page blobs in Azure Blob Storage
- **D.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)

### 96. Configuring a `Region -> District -> Branch` drill-down hierarchy and setting **Row-Level Security (RLS)** filter roles so branch managers only see their own region's deposits are done on the ____.

- **A.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **B.** Power BI semantic model (relationships, DAX measures, hierarchies, and Import/DirectQuery/Direct Lake storage)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)

### 97. Structuring CrestVault's Power BI model with `FactTransactions` at the center and `DimAccount`, `DimDate`, and `DimChannel` radiating outward in `1:*` relationships implements a ____.

- **A.** Key-value non-relational store
- **B.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **C.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **D.** Append blobs in Azure Blob Storage

### 98. CrestVault's CFO wants one chart bridging `Q1 Operating Profit ($120M)` through positive `Fee Growth (+$18M)`, negative `Credit Provisions (-$9M)`, and negative `Tech Opex (-$6M)` to `Q2 Operating Profit ($123M)`. Which Power BI visual is built for sequential variance bridges?

- **A.** Page blobs in Azure Blob Storage
- **B.** First Normal Form (1NF — atomic values and no repeating column groups)
- **C.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)
- **D.** Waterfall chart (sequential positive/negative variance steps) or Funnel chart (linear stage conversion drop-off)

### 99. Treasury analysts want to plot daily 10-year Treasury yield vs. CrestVault's mortgage rate continuously over 730 trading days to visualize rate trajectory over time. Which Power BI visual fits best?

- **A.** Append blobs in Azure Blob Storage
- **B.** Treemap (or pie/donut chart for small category counts) showing part-to-whole proportions
- **C.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)
- **D.** Line chart (tracking continuous trends and changes over ordered time intervals)

### 100. A retail deposit summary tile shows how total deposits break down into exactly **four** product slices (`Checking`, `Savings`, `CDs`, `Money Market`) as percentages of `100%`. Which Power BI visual class displays simple part-to-whole proportions?

- **A.** Line chart (tracking continuous trends and changes over ordered time intervals)
- **B.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)
- **C.** Treemap (or pie/donut chart for small category counts) showing part-to-whole proportions
- **D.** Apache Parquet columnar storage format

---

## Answer Key and Explanations

### Question 1 — `D` (Describe core data concepts)

Correct answer: D (is correct). Rows conforming to a fixed relational table schema of typed columns represent structured data. [Skill 1.1: Describe the features of structured data | Source: Explore core data concepts — Identify data formats (structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **B:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **C:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **D:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.

### Question 2 — `D` (Describe core data concepts)

Correct answer: D (is correct). Tabular rows with predefined column names and strict data types are structured data. [Skill 1.1: Describe the features of structured data | Source: Explore core data concepts — Identify data formats (structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **B:** Incorrect. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **C:** Incorrect. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **D:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.

### Question 3 — `A, E` (Describe core data concepts)

Correct answers: A and E (are correct). Nested `{}` objects with variable per-transfer attributes represent semi-structured JSON data. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Correct. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **B:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **E:** Correct. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.

### Question 4 — `A` (Describe core data concepts)

Correct answer: A (is correct). Self-describing hierarchical tags without a rigid tabular column layout define semi-structured data. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Correct. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **B:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **C:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.

### Question 5 — `B` (Describe core data concepts)

Correct answer: B (is correct). Apache Avro pairs compact binary row serialization with a JSON header schema for high-speed financial event buses and schema evolution. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.
- **B:** Correct. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 6 — `C` (Describe core data concepts)

Correct answer: C (is correct). Raw binary images, video clips, and audio recordings lack an internal field schema and are unstructured data. [Skill 1.3: Describe the features of unstructured data | Source: Explore core data concepts — Identify data formats (unstructured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **B:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **C:** Correct. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.

### Question 7 — `A` (Describe core data concepts)

Correct answer: A (is correct). Scanned PDFs and TIFF images lack a tabular or key-tag schema and are classified as unstructured data. [Skill 1.3: Describe the features of unstructured data | Source: Explore core data concepts — Identify data formats (unstructured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Correct. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **B:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **C:** Incorrect. A composite key combines two or more columns (such as `OrderID` + `ProductID`) to uniquely identify rows in a junction or line-item table.
- **D:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.

### Question 8 — `A, C` (Describe core data concepts)

Correct answers: A and C (are correct). CSV provides simple flat comma-separated text, while Apache Parquet provides compressed columnar storage for analytical queries. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Correct. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **B:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **C:** Correct. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **E:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.

### Question 9 — `D` (Describe core data concepts)

Correct answer: D (is correct). Apache Parquet's columnar layout and column chunk metadata allow engines to project only needed columns and skip irrelevant data. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Incorrect. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **D:** Correct. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.

### Question 10 — `B` (Describe core data concepts)

Correct answer: B (is correct). Optimized Row Columnar (ORC) organizes data into compressed stripes with built-in lightweight indexes for Hive and batch analytics. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Incorrect. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **B:** Correct. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 11 — `A, C` (Describe core data concepts)

Correct answers: A and C (are correct). Graph databases execute multi-hop vertex/edge traversals for fraud rings, and document databases index nested JSON dossiers. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Correct. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **B:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Correct. A document database stores self-contained JSON/BSON documents indexed across nested attributes so each entity can evolve fields without schema migrations.
- **D:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **E:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 12 — `C` (Describe core data concepts)

Correct answer: C (is correct). Key-value stores map unique keys directly to values for fast single-key point lookups. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **B:** Incorrect. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **C:** Correct. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.
- **D:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.

### Question 13 — `B` (Describe core data concepts)

Correct answer: B (is correct). Column-family (wide-column) databases group related columns into families under partition/row keys for high-throughput writes. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Correct. A column-family database groups related columns into families keyed by row and partition keys (such as Apache Cassandra or HBase) for massive write throughput.
- **C:** Incorrect. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.
- **D:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.

### Question 14 — `C` (Describe core data concepts)

Correct answer: C (is correct). Live ACID ledger postings run in Azure SQL Database, Data Factory extracts history to ADLS Gen2 / OneLake Parquet, and Power BI visuals query star schemas. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Incorrect. Paginated reports render formatted output rather than ingesting transactions, and Blob Cold tier does not execute multi-row ACID relational transactions.
- **B:** Incorrect. Archive blobs are offline and unreadable for live OLTP writes, Power BI Desktop is an authoring tool rather than an OLTP engine, and Table storage is schemaless key-value.
- **C:** Correct. Operational transactions commit in an ACID relational store first, pipelines land history in columnar lake storage, and analytical models serve BI reports without taxing OLTP.
- **D:** Incorrect. Power BI Service is a read-optimized BI platform rather than a transactional database, and Queue storage buffers small messages rather than archiving relational rows.

### Question 15 — `A` (Describe core data concepts)

Correct answer: A (is correct). Azure SQL Database provides managed PaaS relational tables with ACID transactions, foreign keys, and built-in high availability. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Correct. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 16 — `D` (Describe core data concepts)

Correct answer: D (is correct). Azure Cosmos DB provides turnkey multi-region global distribution and financially backed `<10 ms` latency SLAs. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.
- **D:** Correct. Azure Cosmos DB replicates data transparently across selected Azure regions with financially backed 99.999% availability and single-digit millisecond read/write latency.

### Question 17 — `C, E, F` (Describe core data concepts)

Correct answers: C, E, and F (are correct). All-or-nothing execution is Atomicity, valid constraint adherence is Consistency, and crash persistence after commit is Durability. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **B:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **C:** Correct. Durability guarantees that once a transaction commits, its changes are persisted to non-volatile transaction logs/storage and survive power loss or crash recovery.
- **D:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **E:** Correct. Consistency ensures a transaction transitions the database only from one valid rule-compliant state (keys, check constraints, types) to another.
- **F:** Correct. Atomicity guarantees that every statement in a transaction either succeeds together or rolls back completely if any step fails, preventing half-completed transfers.

### Question 18 — `D` (Describe core data concepts)

Correct answer: D (is correct). Isolation prevents concurrent in-flight transactions from interfering or reading uncommitted intermediate states. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **B:** Incorrect. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **C:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **D:** Correct. Isolation prevents concurrent in-flight transactions from reading uncommitted intermediate edits or overwriting each other unpredictably via locking or row versioning.

### Question 19 — `C` (Describe core data concepts)

Correct answer: C (is correct). High-concurrency, short, ACID-protected row writes against normalized tables define an OLTP transactional workload. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **B:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **C:** Correct. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **D:** Incorrect. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.

### Question 20 — `B, C` (Describe core data concepts)

Correct answers: B and C (are correct). Historical read-intensive aggregation is an OLAP workload, and a central fact table surrounded by flat dimensions is a star schema. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **B:** Correct. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **C:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **E:** Incorrect. Isolation prevents concurrent in-flight transactions from reading uncommitted intermediate edits or overwriting each other unpredictably via locking or row versioning.

### Question 21 — `A` (Describe core data concepts)

Correct answer: A (is correct). Read-heavy historical aggregations separated from live operational transactions define an OLAP workload. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Correct. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **B:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **C:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **D:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.

### Question 22 — `A` (Describe core data concepts)

Correct answer: A (is correct). Normalizing dimension hierarchies into chained parent lookup tables around a fact table creates a snowflake schema. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Correct. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **D:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).

### Question 23 — `A` (Describe core data concepts)

Correct answer: A (is correct). Securing database servers, managing HA/DR and backups, and tuning operational queries belong to the DBA. [Skill 1.9: Describe responsibilities for database administrators | Source: Explore data roles and services — Database administrator responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Correct. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **B:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **C:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **D:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.

### Question 24 — `A` (Describe core data concepts)

Correct answer: A (is correct). Backup governance and point-in-time recovery (`PITR`) execution are core responsibilities of the database administrator (DBA). [Skill 1.9: Describe responsibilities for database administrators | Source: Explore data roles and services — Database administrator responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Correct. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **B:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **C:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **D:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.

### Question 25 — `A` (Describe core data concepts)

Correct answer: A (is correct). The DBA governs operational SQL, the data engineer builds ELT pipelines and Gold star tables in Fabric, and the data analyst authors DAX KPIs and Power BI reports. [Skill 1.10: Describe responsibilities for data engineers | Source: Explore data roles and services — Data engineer responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Correct. DBAs govern operational database engines, data engineers build ingestion/transformation pipelines into curated analytical stores, and data analysts model KPIs and visual reports.
- **B:** Incorrect. Cluster HA belongs to the DBA, Spark ELT pipelines belong to the data engineer, and visual storytelling/app distribution belongs to the data analyst.
- **C:** Incorrect. Operational DB security and PITR restores are DBA duties, network/pipeline plumbing belongs to infra/data engineering, and analysts focus on semantic models and visuals.
- **D:** Incorrect. KPI scorecards and sales packs are data analyst outputs, whereas Spark streaming pipelines belong to data engineers and OLTP index maintenance belongs to DBAs.

### Question 26 — `C` (Describe core data concepts)

Correct answer: C (is correct). Designing and maintaining batch/streaming ingestion and transformation pipelines into analytical stores is the data engineer's role. [Skill 1.10: Describe responsibilities for data engineers | Source: Explore data roles and services — Data engineer responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **B:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **C:** Correct. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **D:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.

### Question 27 — `B` (Describe core data concepts)

Correct answer: B (is correct). Data analysts create semantic DAX calculations and interactive Power BI visuals to answer business questions. [Skill 1.11: Describe responsibilities for data analysts | Source: Explore data roles and services — Data analyst responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **B:** Correct. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **C:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **D:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.

### Question 28 — `C` (Describe core data concepts)

Correct answer: C (is correct). Modeling KPIs and building interactive visual reports over curated warehouse tables defines the data analyst role. [Skill 1.11: Describe responsibilities for data analysts | Source: Explore data roles and services — Data analyst responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **B:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **C:** Correct. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 29 — `C, D` (Identify considerations for relational data on Azure)

Correct answers: C and D (are correct). `AccountID` on `Accounts` is a primary key, and `AccountID` on `LedgerEntries` is a foreign key enforcing referential integrity. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **B:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **C:** Correct. A primary key uniquely identifies each row in a relational table and implicitly forbids `NULL` and duplicate key values.
- **D:** Correct. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.
- **E:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.

### Question 30 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). A key composed of two or more columns to uniquely identify rows is a composite key. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **C:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **D:** Correct. A composite key combines two or more columns (such as `OrderID` + `ProductID`) to uniquely identify rows in a junction or line-item table.

### Question 31 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). A foreign key constraint enforces referential integrity between child (`Loans`) and parent (`Branches`) tables. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. Waterfall charts break down cumulative gains and losses between a starting and ending total, while Funnel charts track progressive drop-off across sequential pipeline stages.
- **B:** Correct. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.
- **C:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 32 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). A primary key uniquely identifies every tuple in a table and strictly disallows `NULL` values. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **B:** Correct. A primary key uniquely identifies each row in a relational table and implicitly forbids `NULL` and duplicate key values.
- **C:** Incorrect. The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.
- **D:** Incorrect. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.

### Question 33 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). 1NF enforces atomic cells and a primary key, 2NF removes partial composite-key dependencies, and 3NF removes transitive non-key dependencies. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. Copying supplier attributes into invoice items creates transitive redundancy, and pipe-delimited multi-value strings violate 1NF.
- **B:** Incorrect. Foreign keys require atomic primary keys first, and 1NF eliminates repeating groups rather than creating them.
- **C:** Incorrect. You cannot achieve 3NF before 1NF/2NF, comma-separated lists violate 1NF atomicity, and duplicating addresses reintroduces update anomalies.
- **D:** Correct. Normalization progresses sequentially: 1NF enforces atomic values and row uniqueness, 2NF removes partial dependencies on composite keys, and 3NF eliminates transitive non-key dependencies.

### Question 34 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). First Normal Form (1NF) requires atomic scalar values per cell and removes repeating column groups. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **C:** Correct. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **D:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.

### Question 35 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Extracting `IssuerName` so no non-key attribute depends on only one column of `(PortfolioID, SecurityISIN)` satisfies Second Normal Form (2NF). [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **C:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **D:** Correct. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.

### Question 36 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Third Normal Form (3NF) removes transitive dependencies where one non-key column determines another non-key column. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **B:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **C:** Correct. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **D:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.

### Question 37 — `B, E, F` (Identify considerations for relational data on Azure)

Correct answers: B, E, and F (are correct). `CREATE TABLE` is DDL, `INSERT INTO` is DML, and `REVOKE` is DCL. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Correct. DML statements query, add, modify, or delete row data stored inside relational tables.
- **C:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **D:** Incorrect. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **E:** Correct. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **F:** Correct. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.

### Question 38 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). In SQL, `WHERE` filters individual rows before `GROUP BY`, and `HAVING` filters aggregated groups after `GROUP BY`. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. SQL `WHERE` evaluates individual pre-grouped rows and rejects aggregate functions; group-level aggregate filters belong in the `HAVING` clause.
- **B:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **C:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **D:** Correct. `WHERE` predicates evaluate individual source rows prior to aggregation, whereas `HAVING` filters grouped summary results such as `HAVING COUNT(*) > 5`.

### Question 39 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). A `LEFT OUTER JOIN` preserves all rows from the left `Clients` table and fills `NULL` when no right-table match exists. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. Granting and revoking security permissions belongs to DCL (`GRANT`, `REVOKE`, `DENY`), not DML.
- **B:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **C:** Correct. `LEFT OUTER JOIN` keeps every row from the left table (for example, all customers) and fills `NULL` for right-table columns when no related order exists.
- **D:** Incorrect. `INNER JOIN` returns only row pairs whose join predicate matches in both the left and right tables, excluding unmatched rows.

### Question 40 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Permission management commands (`GRANT`, `REVOKE`, `DENY`) belong to Data Control Language (DCL). [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. Granting and revoking security permissions belongs to DCL (`GRANT`, `REVOKE`, `DENY`), not DML.
- **B:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **C:** Incorrect. DML statements query, add, modify, or delete row data stored inside relational tables.
- **D:** Correct. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.

### Question 41 — `A, C` (Identify considerations for relational data on Azure)

Correct answers: A and C (are correct). A view provides a virtual `SELECT` projection masking columns, and a stored procedure runs parameterized server-side SQL routines. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Correct. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.
- **B:** Incorrect. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.
- **C:** Correct. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **D:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **E:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 42 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). A clustered index determines the single physical leaf-level sort order of rows in a table. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Correct. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **B:** Incorrect. Because a clustered index dictates the single physical leaf-level storage order of the table’s rows, a table can have at most one clustered index (plus multiple nonclustered indexes).
- **C:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **D:** Incorrect. A nonclustered index maintains a separate sorted key structure pointing back to the base table rows, accelerating selective lookups on non-primary search columns.

### Question 43 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Nonclustered indexes store separate sorted key structures with row locators so multiple search paths can coexist on one table. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Correct. A nonclustered index maintains a separate sorted key structure pointing back to the base table rows, accelerating selective lookups on non-primary search columns.
- **B:** Incorrect. Because a clustered index dictates the single physical leaf-level storage order of the table’s rows, a table can have at most one clustered index (plus multiple nonclustered indexes).
- **C:** Incorrect. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.
- **D:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.

### Question 44 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). A standard view stores only its `SELECT` query definition and reads the live underlying base tables dynamically at query time. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Correct. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **B:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.

### Question 45 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Discover and assess SQL compatibility/SKUs in Azure Migrate, select Azure SQL Database or Managed Instance, provision with Entra/TLS security, and migrate data before cutover. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Correct. Azure Migrate discovers workloads, flags compatibility blockers, and recommends right-sized Azure SQL targets before secure provisioning, data sync, and connection cutover.
- **B:** Incorrect. Cutting over before data migration breaks production, opening all public IPs violates security, and assessments must run before selecting the target SKU.
- **C:** Incorrect. Azure Table storage cannot mount `.mdf` database files, and single Azure SQL Database does not host SQL Server Agent or cross-database instance queries.
- **D:** Incorrect. Queue storage is not a relational migration vehicle, SQL Managed Instance requires VNet subnet sizing upfront, and removing primary keys corrupts relational integrity.

### Question 46 — `A, D` (Identify considerations for relational data on Azure)

Correct answers: A and D (are correct). Azure SQL Database Elastic Pools share PaaS compute across multi-tenant DBs, while SQL Server on Azure VMs provides full IaaS OS and engine version control. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Correct. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **B:** Incorrect. Microsoft retired Data Migration Assistant (DMA) in July 2025; Azure Migrate and the Azure SQL Migration extension handle SQL discovery, assessment, and right-sizing.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Correct. An Elastic Pool shares a pool of compute resources across multiple single databases that have unpredictable, staggered usage spikes to optimize cost.
- **E:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 47 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Azure SQL Managed Instance provides near-100% SQL Server instance compatibility (SQL Agent, Service Broker, cross-DB queries) as managed PaaS. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Single Azure SQL Database is database-scoped and does not include SQL Server Agent or cross-database instance queries; those require SQL Managed Instance or SQL Server on Azure VMs.
- **B:** Correct. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **C:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 48 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Azure SQL Database Serverless automatically scales compute and auto-pauses during inactive periods so only storage is billed. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **B:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **C:** Correct. The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.
- **D:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.

### Question 49 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Microsoft Entra ID supports passwordless managed-identity authentication, MFA, and Conditional Access for Azure SQL. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **B:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.
- **C:** Correct. Microsoft Entra ID (formerly Azure AD) centralizes identity governance, conditional access, MFA, and passwordless managed-identity connections to Azure data services.
- **D:** Incorrect. Microsoft retired Data Migration Assistant (DMA) in July 2025; Azure Migrate and the Azure SQL Migration extension handle SQL discovery, assessment, and right-sizing.

### Question 50 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Azure Database for PostgreSQL — Flexible Server provides managed PaaS PostgreSQL with `PL/pgSQL`, extensions, `pgAdmin`, and HA. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **C:** Incorrect. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.
- **D:** Correct. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.

### Question 51 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Azure Database for MySQL — Flexible Server delivers managed MySQL Community Edition PaaS with built-in HA and up to 35-day PITR. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Incorrect. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **B:** Correct. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.
- **C:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **D:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.

### Question 52 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Azure Database for PostgreSQL — Flexible Server is an object-relational PaaS engine with `PL/pgSQL` and `azure_sys` Query Store telemetry. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **B:** Correct. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 53 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Lifecycle policies transition blobs from Hot -> Cool (>=30d) -> Cold (>=90d) -> offline Archive (>=180d, rehydrating on audit request). [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Archive tier is offline and cannot serve direct reads until rehydrated to Hot or Cool, which takes hours.
- **B:** Correct. Lifecycle management policies automatically age blobs from lowest-read-cost Hot through Cool and Cold down to lowest-storage-cost offline Archive.
- **C:** Incorrect. Table storage entities hold small key-value properties rather than large video files, and Cool/Cold tiers remain online with immediate millisecond read access.
- **D:** Incorrect. Blob tiers are object storage rather than SMB shares, Archive rather than Hot minimizes 1-year retention storage cost, and Hot blobs require no rehydration.

### Question 54 — `C, D` (Describe considerations for working with non-relational data on Azure)

Correct answers: C and D (are correct). Discrete `.tiff` image files are stored as Block blobs, and the offline Archive tier minimizes monthly per-GB cost for >=180-day retention. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **C:** Correct. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **D:** Correct. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.
- **E:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 55 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Append blobs optimize block append operations strictly at the end of a blob for audit and diagnostic logs. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Archive tier blobs are stored offline and cannot be read directly until rehydrated to Hot or Cool, which takes hours.
- **B:** Correct. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.

### Question 56 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Azure Data Lake Storage (ADLS) Gen2 adds a Hierarchical Namespace, POSIX ACLs, and atomic directory operations to Blob Storage. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Correct. ADLS Gen2 adds a true POSIX-ACL directory hierarchy and atomic folder rename/delete operations atop Azure Blob Storage for big-data analytics engines.
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 57 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). The Hot access tier is optimized for frequently read and modified objects, offering the lowest access/transaction fees. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Correct. The Hot tier is online storage optimized for data that is accessed or modified frequently, carrying the lowest transaction/read cost.
- **B:** Incorrect. Archive tier blobs are stored offline and cannot be read directly until rehydrated to Hot or Cool, which takes hours.
- **C:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.
- **D:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 58 — `D, E` (Describe considerations for working with non-relational data on Azure)

Correct answers: D and E (are correct). Azure Files provides managed SMB 3.0 shares, and Azure File Sync caches hot files on branch Windows Servers while tiering cold files to Azure. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **B:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **C:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **D:** Correct. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **E:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 59 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Azure Files supports managed `NFS 4.1` as well as `SMB 3.0` shared volumes. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.
- **C:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 60 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure File Sync replicates Windows Server folders with Azure Files and supports local caching plus cloud tiering. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Incorrect. ADLS Gen2 adds a true POSIX-ACL directory hierarchy and atomic folder rename/delete operations atop Azure Blob Storage for big-data analytics engines.
- **B:** Correct. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **C:** Incorrect. Azure Stream Analytics runs declarative Stream Analytics Query Language (`SELECT ... GROUP BY TumblingWindow(...)`) jobs joining live streams with reference data into sinks.
- **D:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.

### Question 61 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Table storage stores schemaless key-value property bags indexed by `PartitionKey` and `RowKey`. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. Azure Table storage is a schemaless key-value store indexed only by `PartitionKey` and `RowKey` with no foreign keys or server-side table joins.
- **B:** Correct. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 62 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Cosmos DB for Table preserves the `PartitionKey`/`RowKey` SDK model while adding turnkey global distribution, secondary indexes, and <10 ms SLAs. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **B:** Correct. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 63 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Azure Table storage is a schemaless key-value store with no server-side joins or foreign-key constraints. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Correct. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. Azure Table storage is a schemaless key-value store indexed only by `PartitionKey` and `RowKey` with no foreign keys or server-side table joins.
- **C:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **D:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.

### Question 64 — `B, E` (Describe considerations for working with non-relational data on Azure)

Correct answers: B and E (are correct). Strong consistency sits at the strictest end (linearizable latest write), and Eventual consistency sits at the most relaxed, lowest-RU end. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **B:** Correct. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **C:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **E:** Correct. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.

### Question 65 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Session consistency is Cosmos DB's default level and guarantees monotonic read-your-own-writes per client session. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **B:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.
- **C:** Incorrect. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.
- **D:** Correct. Session consistency is Cosmos DB’s default level, balancing low latency and throughput while guaranteeing each user session immediately sees its own writes in order.

### Question 66 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Cosmos DB Serverless bills purely per Request Unit (RU) consumed by executed operations plus storage. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. Bar and column charts use aligned bar lengths to compare magnitudes accurately across discrete categories such as product lines or regions.
- **B:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Correct. Cosmos DB measures CPU, memory, and IOPS per database operation in Request Units (RUs), billed via Provisioned/Autoscale RU/s or consumption-based Serverless.

### Question 67 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Cosmos DB offers turnkey multi-region replication, multi-region writes, `99.999%` availability SLAs, and `<10 ms` read/write latency. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Correct. Azure Cosmos DB replicates data transparently across selected Azure regions with financially backed 99.999% availability and single-digit millisecond read/write latency.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **D:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.

### Question 68 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Select the API at account creation, create the database and `/accountId` container, configure RU/s or serverless + consistency, and run partition-scoped queries. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Every Cosmos DB container requires a partition key, the API is fixed per account, Cosmos DB does not enforce cross-container foreign keys, and item size is capped at 2 MB.
- **B:** Incorrect. Cosmos DB sits under an account -> database -> container -> item hierarchy, not SMB shares or subscription tags.
- **C:** Incorrect. Cosmos DB is fully managed PaaS with no OS patching, a single-value partition key creates a 20 GB logical-partition bottleneck, and triggers/sprocs use JavaScript rather than T-SQL.
- **D:** Correct. API selection happens at account creation, partition key design happens at container creation to distribute storage/RU evenly, and partition-scoped queries avoid cross-partition fan-out.

### Question 69 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Cosmos DB for Apache Gremlin models accounts and entities as vertices connected by directed wire-transfer edges for AML ring traversals. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Correct. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **B:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **C:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 70 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Azure Cosmos DB for NoSQL is the native JSON document API queried with SQL `SELECT` syntax. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **B:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **C:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.
- **D:** Correct. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.

### Question 71 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Azure Cosmos DB for MongoDB provides wire-protocol compatibility for BSON MongoDB applications. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **B:** Incorrect. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **C:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **D:** Correct. Cosmos DB for MongoDB lets existing MongoDB drivers and tools store BSON documents in Cosmos DB simply by updating the connection string.

### Question 72 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Azure Cosmos DB for Apache Cassandra provides managed wire compatibility for CQL wide-column workloads. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **B:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.
- **C:** Correct. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 73 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Data Factory lands raw files into OneLake Bronze, Spark/SQL cleanses Silver Delta tables, and curated Gold star schemas power BI. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Incorrect. Skipping cleansing degrades report accuracy, deleting raw Bronze files prevents replayability, and Gold analytical layers favor denormalized star schemas over 3NF.
- **B:** Incorrect. Analytical ingestion is read-only against operational sources and builds Bronze -> Silver -> Gold sequentially.
- **C:** Correct. Modern ELT lands raw data in scalable lake storage first, then leverages cloud compute to cleanse Silver tables and publish Gold star schemas for analytics.
- **D:** Incorrect. ELT executes transformations in scalable cloud engines rather than client laptops, and Archive blobs/Queues cannot back live BI queries.

### Question 74 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Yes — scrubbing or tokenizing sensitive fields before loading the analytical store follows Extract, Transform, and Load (ETL). [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Correct. ETL transforms, scrubs, or redacts sensitive fields in an intermediate processing engine prior to loading only the conformed structure into the target analytical store.
- **B:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.
- **C:** Incorrect. ELT extracts raw source data, loads it directly into scalable lake/warehouse storage, and runs distributed cloud compute (Spark or SQL) to cleanse and model in place.
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 75 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Azure Data Factory (and Data Factory in Microsoft Fabric) orchestrates connector-based Copy pipelines and Dataflows Gen2. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Correct. Data Factory orchestrates code-free data movement (90+ connectors via Copy activity) and visual Power Query transformations (Dataflows Gen2) or Spark/Mapping Data Flows.
- **C:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **D:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.

### Question 76 — `B, C` (Describe an analytics workload on Azure)

Correct answers: B and C (are correct). Delta Lake ACID tables over open Parquet implement a data lakehouse, and single-hop dimensions around a fact table form a star schema. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **C:** Correct. A lakehouse combines the low-cost open file flexibility of a data lake with ACID transactions, schema enforcement, and SQL warehouse performance via Delta Lake tables.
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **E:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.

### Question 77 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Normalizing dimension tables into multi-level parent lookup tables around a fact table defines a snowflake schema. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Correct. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **B:** Incorrect. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.
- **C:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 78 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Microsoft OneLake is Fabric's unified tenant-wide data lake supporting zero-copy Shortcuts across ADLS Gen2 and external lakes. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **D:** Correct. OneLake is Microsoft Fabric’s unified ADLS Gen2-compatible logical data lake that stores Delta Parquet data once and shares it via zero-copy Shortcuts across workloads.

### Question 79 — `A, B, E` (Describe an analytics workload on Azure)

Correct answers: A, B, and E (are correct). Microsoft Fabric, Azure Databricks, and Azure Synapse Analytics are those three enterprise analytics platforms. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Correct. Azure Synapse Analytics integrates serverless SQL on-demand lake querying, dedicated MPP SQL warehousing, Apache Spark pools, and Synapse Pipelines in Synapse Studio.
- **B:** Correct. Microsoft Fabric unifies Data Factory, Data Engineering, Data Warehouse, Data Science, Real-Time Intelligence, and Power BI in one SaaS workspace sharing OneLake Delta tables.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **E:** Correct. Azure Databricks provides managed Apache Spark clusters, collaborative Python/SQL/Scala/R notebooks, Unity Catalog governance, and Delta Lake processing on Azure.
- **F:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 80 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Azure Databricks provides managed collaborative Apache Spark clusters, Delta Lake optimization, Unity Catalog, and MLflow. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **B:** Correct. Azure Databricks provides managed Apache Spark clusters, collaborative Python/SQL/Scala/R notebooks, Unity Catalog governance, and Delta Lake processing on Azure.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 81 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Azure Synapse Analytics includes serverless SQL pools for pay-per-query T-SQL exploration over data lake files alongside dedicated MPP SQL pools. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **B:** Correct. Azure Synapse Analytics integrates serverless SQL on-demand lake querying, dedicated MPP SQL warehousing, Apache Spark pools, and Synapse Pipelines in Synapse Studio.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.

### Question 82 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Azure HDInsight provisions managed clusters of open-source Hadoop, Hive, HBase, Kafka, and Spark frameworks. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **B:** Correct. Azure HDInsight provisions managed clusters of open-source Apache big-data frameworks when lift-and-shift Hadoop/Hive/HBase/Kafka compatibility is required.
- **C:** Incorrect. The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.
- **D:** Incorrect. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.

### Question 83 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Evaluating continuous unbounded events in real time with sub-second latency defines stream processing. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **B:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **C:** Correct. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.
- **D:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 84 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Processing bounded collections of accumulated records on a schedule defines batch processing. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **B:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.
- **C:** Correct. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **D:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).

### Question 85 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). A sliding window evaluates a rolling fixed lookback duration whenever events enter or leave the window. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **B:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **C:** Correct. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **D:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.

### Question 86 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). A hopping window schedules fixed-size windows that step forward by a shorter hop interval, producing overlapping windows. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.
- **B:** Correct. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **C:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **D:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.

### Question 87 — `A, E` (Describe an analytics workload on Azure)

Correct answers: A and E (are correct). Azure Event Hubs buffers high-throughput partitioned streams, and Azure Stream Analytics runs serverless SQL-like stream queries with reference-data joins. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Correct. Azure Stream Analytics runs declarative Stream Analytics Query Language (`SELECT ... GROUP BY TumblingWindow(...)`) jobs joining live streams with reference data into sinks.
- **B:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **E:** Correct. Azure Event Hubs ingests millions of telemetry events per second into partitioned append logs (supporting native AMQP/HTTPS and Apache Kafka producers) for downstream stream consumers.

### Question 88 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Microsoft Fabric Real-Time Intelligence unites Eventstream, Eventhouse (KQL databases), Real-Time Dashboards, and Activator. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.
- **B:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **C:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **D:** Correct. Fabric Real-Time Intelligence ingests and routes events via Eventstream, indexes high-volume telemetry in Eventhouse KQL databases, visualizes live tiles, and triggers Activator alerts.

### Question 89 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Apache Spark Structured Streaming processes continuous streams via Spark SQL/DataFrame APIs with fault-tolerant checkpointing. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **C:** Correct. Spark Structured Streaming treats a live event stream as an unbounded table processed via familiar Spark SQL/DataFrame APIs with checkpointed exactly-once guarantees.
- **D:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.

### Question 90 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Fixed-size, contiguous, non-overlapping intervals where each event belongs to one bucket define a tumbling window. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **B:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **C:** Correct. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **D:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.

### Question 91 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Risk analysts prep and model in Power BI Desktop, publish to a workspace in Power BI Service, pin CRO dashboard tiles and schedule refresh, and distribute a governed App. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Correct. Power BI Desktop handles Power Query prep, semantic modeling, and report design, while Power BI Service hosts scheduled refresh, multi-report dashboards, and governed App distribution.
- **B:** Incorrect. Dashboards exist only in Power BI Service (not Power BI Desktop), Power BI Mobile is for consumption, and viewers consume shared Apps/reports in browser or mobile.
- **C:** Incorrect. Paginated `.rdl` reports are authored in Power BI Report Builder, Stream Analytics processes event streams, and port `1433` is SQL Server TDS rather than BI sharing.
- **D:** Incorrect. Dashboards are created in Power BI Service rather than Power BI Mobile, and dataset refresh plus secure sharing are managed in Power BI Service workspaces.

### Question 92 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Power BI Report Builder authors pixel-perfect paginated (`.rdl`) reports designed for multi-page PDF output and printing. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Incorrect. Azure Stream Analytics runs declarative Stream Analytics Query Language (`SELECT ... GROUP BY TumblingWindow(...)`) jobs joining live streams with reference data into sinks.
- **B:** Incorrect. Power BI Service (`app.powerbi.com` / Fabric) hosts published semantic models and reports, pins cross-report dashboard tiles, schedules gateway refreshes, and distributes governed Apps.
- **C:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **D:** Correct. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 93 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Yes — cross-report pinned dashboards, subscriptions, scheduled refresh, and Apps are cloud features of the Power BI Service. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Correct. Power BI Service (`app.powerbi.com` / Fabric) hosts published semantic models and reports, pins cross-report dashboard tiles, schedules gateway refreshes, and distributes governed Apps.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. Dashboards with pinned tiles across multiple reports are a cloud-only feature of Power BI Service, not Power BI Desktop.
- **D:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.

### Question 94 — `A, D` (Describe an analytics workload on Azure)

Correct answers: A and D (are correct). `1:*` relationships and hidden keys belong to the Power BI semantic model, while `DIVIDE(...)` defines a dynamic DAX measure. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Correct. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **B:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Correct. A Power BI semantic model defines `1:*` star-schema relationships, reusable DAX measures, drill-down hierarchies, and column metadata consumed across reports.
- **E:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 95 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). A DAX measure dynamically divides filtered charge-offs by filtered average loan balances inside the active report filter context. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **B:** Correct. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.

### Question 96 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Hierarchies, relationships, and Row-Level Security roles are defined in the Power BI semantic model (and role members assigned in Power BI Service). [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **B:** Correct. A Power BI semantic model defines `1:*` star-schema relationships, reusable DAX measures, drill-down hierarchies, and column metadata consumed across reports.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.

### Question 97 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). A central fact table surrounded by single-hop `1:*` dimension tables implements a star schema. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.
- **B:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **C:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 98 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). A Waterfall chart shows cumulative positive and negative steps bridging a starting value to an ending total. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **C:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
- **D:** Correct. Waterfall charts break down cumulative gains and losses between a starting and ending total, while Funnel charts track progressive drop-off across sequential pipeline stages.

### Question 99 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). A line chart best displays continuous time-series trends over ordered dates. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Incorrect. Pie/donut charts show part-to-whole shares for a few slices, while treemaps use nested rectangles to display proportional composition across larger hierarchical categories.
- **C:** Incorrect. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.
- **D:** Correct. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.

### Question 100 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). A donut/pie chart (for a few slices) or Treemap displays part-to-whole proportional shares of a total. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Incorrect. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.
- **B:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
- **C:** Correct. Pie/donut charts show part-to-whole shares for a few slices, while treemaps use nested rectangles to display proportional composition across larger hierarchical categories.
- **D:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
