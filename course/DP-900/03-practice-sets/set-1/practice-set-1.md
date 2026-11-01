# Microsoft Exam DP-900: Microsoft Azure Data Fundamentals — Full-Length Mock Exam 1

**Theme:** Omnichannel Retail & E-Commerce — Data Formats, OLTP/OLAP, Azure SQL, Cosmos DB NoSQL, OneLake & Power BI  
**Credential:** `Microsoft Certified: Azure Data Fundamentals` *(Beginner / Fundamentals · **no prerequisite** · **never expires**)*  
**Study guide baseline:** `July 21, 2026` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `75 minutes` (`45 sec/question`, matching live 45-minute / 60-question pace; `45 minutes` optional speed drill · **closed-book**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn documentation — not affiliated with or endorsed by Microsoft Corporation. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Describe core data concepts (25–30% official weight · 28 questions)

### 1. VeloMart Retail stores inventory SKU numbers, unit prices, and warehouse quantities in fixed columns with strict data types where every product row follows the exact same table layout. This dataset is an example of ____.

- **A.** Structured data
- **B.** Semi-structured data
- **C.** Unstructured data
- **D.** Apache Avro row-based binary format with JSON schema

### 2. An e-commerce finance controller exports monthly tax ledger entries into relational tables where every record has mandatory `OrderID`, `TaxRate`, and `TaxAmount` columns. Which data classification describes this storage layout?

- **A.** Graph database (vertices and directed edges)
- **B.** Structured data
- **C.** Unstructured data
- **D.** Semi-structured data

### 3. A marketplace catalog allows footwear listings to carry nested `shoeSize` and `soleMaterial` attributes while electronics listings carry `voltage` and `warrantyMonths` in the same collection without altering a table schema. Which two items characterize this representation? Select two.

- **A.** Semi-structured data
- **B.** Unstructured data
- **C.** Structured data
- **D.** JavaScript Object Notation (JSON) document format
- **E.** Page blobs in Azure Blob Storage

### 4. Web checkout webhooks deliver order payloads containing nested customer shipping objects and variable-length coupon arrays enclosed in curly braces `{}` and key names. These webhook payloads represent ____.

- **A.** Structured data
- **B.** Semi-structured data
- **C.** Unstructured data
- **D.** Clustered index (defines physical leaf-level sort order; maximum one per table)

### 5. A mobile shopping cart API exchanges hierarchical product reviews containing nested author metadata and variable tag arrays between browser clients and cloud microservices. Which representation format is standard for this payload?

- **A.** Page blobs in Azure Blob Storage
- **B.** JavaScript Object Notation (JSON) document format
- **C.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **D.** Delimited text format (CSV or TSV)

### 6. A luxury apparel brand stores studio photoshoot `.jpg` images, fitting-room `.mp4` promo clips, and customer support call `.wav` recordings in cloud object storage. Together, these media assets are classified as ____.

- **A.** Semi-structured data
- **B.** Unstructured data
- **C.** Structured data
- **D.** Apache Parquet columnar storage format

### 7. Store security cameras upload continuous night-shift `.mp4` footage and scanned signed delivery `.pdf` receipts to an Azure storage container. How is this data categorized?

- **A.** First Normal Form (1NF — atomic values and no repeating column groups)
- **B.** Structured data
- **C.** Composite key (multi-column key)
- **D.** Unstructured data

### 8. VeloMart's analytics team queries 4 billion historical order lines but typically reads only 3 of the table's 85 columns (`Region`, `Category`, `NetSales`). Which two file formats store data column-by-column with compression to minimize scanned bytes? Select two.

- **A.** JavaScript Object Notation (JSON) document format
- **B.** Append blobs in Azure Blob Storage
- **C.** Apache Parquet columnar storage format
- **D.** Delimited text format (CSV or TSV)
- **E.** Optimized Row Columnar (ORC) stripe format

### 9. A boutique supplier emails a plain-text price sheet where the first line lists header names separated by commas and each subsequent line represents one flat item row with no nested arrays or embedded data types. This file uses the ____.

- **A.** Optimized Row Columnar (ORC) stripe format
- **B.** Apache Parquet columnar storage format
- **C.** Apache Avro row-based binary format with JSON schema
- **D.** Delimited text format (CSV or TSV)

### 10. A retail clickstream producer serializes compact binary event rows prefixed by a JSON schema header so downstream consumers can evolve fields safely over time. Which data file format matches this design?

- **A.** Apache Avro row-based binary format with JSON schema
- **B.** Line chart (tracking continuous trends and changes over ordered time intervals)
- **C.** Page blobs in Azure Blob Storage
- **D.** Delimited text format (CSV or TSV)

### 11. A flash-sale engineering team evaluates non-relational database models: one to cache shopping-cart tokens looked up purely by `SessionID`, and another to query rich product catalogs across nested JSON attributes. Which two non-relational store types fit these workloads? Select two.

- **A.** Key-value non-relational store
- **B.** Document database
- **C.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **E.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

### 12. VeloMart's merchandising team models shoppers, products, and shared payment cards as nodes connected by `PURCHASED` and `SHARED_CARD` edges to uncover multi-hop referral and fraud rings. Which database type is purpose-built for this traversal?

- **A.** Graph database (vertices and directed edges)
- **B.** Delimited text format (CSV or TSV)
- **C.** Key-value non-relational store
- **D.** Append blobs in Azure Blob Storage

### 13. An inventory sensor platform writes millions of wide time-stamped aisle beacon readings keyed by store row and column families such as `temperature` and `footfall`. Which non-relational database category organizes columns into families for high-throughput writes?

- **A.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)
- **B.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **C.** Database view (saved virtual `SELECT` query)
- **D.** Column-family (wide-column) database

### 14. VeloMart is designing an end-to-end Azure architecture from live point-of-sale checkout through enterprise executive reporting. Which four-step sequence places each workload on the appropriate Azure service?

- **A.** Land raw checkout clicks in Paginated Reports → Transform via SMB file locks → Commit ACID transactions in Azure Blob Cold tier → Query via Gremlin graph vertices
- **B.** Serve live checkout writes in Power BI Service → Export dashboards to CSV → Load CSVs into Azure SQL Database → Archive active rows to Azure Queue storage
- **C.** Capture OLTP writes in Azure SQL Database → Extract changes via Data Factory pipeline → Land Parquet files in ADLS Gen2 / OneLake → Serve star-schema visuals in Power BI
- **D.** Capture OLTP writes directly in Archive Blob tier → Run live checkout queries in Power BI Desktop → Copy rows to Azure Files SMB → Normalize into Azure Table storage

### 15. Proposed solution: To process live e-commerce credit-card orders requiring relational foreign keys and ACID transactions without managing OS patches, the architect provisions Azure SQL Database. Does this meet the goal?

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 16. VeloMart needs a low-cost Azure datastore to host 90 TB of high-resolution product `.png` photos and downloadable `.pdf` user manuals served over HTTPS. Which Azure storage option fits best?

- **A.** Block blobs in Azure Blob Storage
- **B.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** Store 20 GB CAD engineering drawings inside single Azure Queue storage messages

### 17. When a shopper redeems gift-card credit during checkout, the database must ensure debiting the gift card and creating the paid order either both succeed or both roll back, concurrent checkouts cannot read half-updated balances, and committed orders survive a server reboot. Which three ACID guarantees are described? Select three.

- **A.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **B.** Atomicity (all-or-nothing transaction unit)
- **C.** Treemap (or pie/donut chart for small category counts) showing part-to-whole proportions
- **D.** Isolation (concurrent transactions do not interfere)
- **E.** Durability (committed writes survive restarts or crashes)
- **F.** Online Analytical Processing (OLAP) workload

### 18. Point-of-sale registers across 600 VeloMart stores execute thousands of millisecond `INSERT` and `UPDATE` statements per minute against normalized `Orders` and `Inventory` tables. This operational pattern is an ____.

- **A.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **B.** Online Analytical Processing (OLAP) workload
- **C.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **D.** Online Transaction Processing (OLTP) workload

### 19. Proposed solution: To double checkout speed during holiday sales, an engineer proposes denormalizing five years of historical aggregates into the live `Orders` table and disabling ACID transaction locks; instead, the lead architect keeps normalized tables where constraints ensure `InventoryQty >= 0` before and after every commit. Which ACID property enforces valid rule-compliant states across every transaction?

- **A.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **B.** Consistency (valid schema and constraint state)
- **C.** Denormalize the live checkout table with five years of historical aggregates and disable ACID transaction locks
- **D.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)

### 20. VeloMart's quarterly planning system aggregates three years of regional revenue, returns, and gross margin across denormalized `FactSales` and `DimStore` tables using read-heavy queries. Which two concepts characterize this system? Select two.

- **A.** Online Transaction Processing (OLTP) workload
- **B.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **C.** Page blobs in Azure Blob Storage
- **D.** Isolation (concurrent transactions do not interfere)
- **E.** Online Analytical Processing (OLAP) workload

### 21. Merchandising executives run ad-hoc multi-year year-over-year basket size comparisons that scan millions of historical rows without modifying live store inventory. Which workload category is this?

- **A.** Online Analytical Processing (OLAP) workload
- **B.** Online Transaction Processing (OLTP) workload
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)

### 22. In VeloMart's analytical model, a central `FactOrderLines` table storing numeric `Quantity` and `NetAmount` joins in a single hop to `DimDate`, `DimProduct`, and `DimCustomer`. This analytical table layout is a ____.

- **A.** Append blobs in Azure Blob Storage
- **B.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Third Normal Form (3NF — no transitive dependencies between non-key columns)

### 23. At VeloMart, one specialist configures Azure SQL geo-redundant backups, tests point-in-time recovery, enforces least-privilege database roles, and tunes slow OLTP index plans. Which data professional role owns these operational duties?

- **A.** Data analyst
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Data engineer
- **D.** Database administrator (DBA)

### 24. After an accidental bulk delete on a staging relational database, who is responsible for executing a point-in-time restore (`PITR`) and tightening `GRANT`/`REVOKE` permissions on the server?

- **A.** Database administrator (DBA)
- **B.** Data analyst
- **C.** Data engineer
- **D.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)

### 25. VeloMart is onboarding a DBA, a data engineer, and a data analyst for a new Microsoft Fabric and Azure SQL initiative. Which sequence accurately reflects how responsibilities flow across the three roles?

- **A.** Data engineer grants T-SQL row permissions on OLTP → Data analyst provisions Azure VNet private endpoints → DBA builds Power Query Dataflows Gen2 → Data analyst runs point-in-time DB restores
- **B.** DBA designs executive KPI scorecards → Data analyst writes Spark Structured Streaming checkpoints → Data engineer tunes OLTP clustered indexes → DBA publishes paginated sales packs
- **C.** DBA provisions & secures operational Azure SQL → Data engineer builds ELT pipelines into Fabric Lakehouse → Data engineer curates Gold star-schema tables → Data analyst models DAX KPIs & publishes Power BI reports
- **D.** Data analyst configures SQL Server failover clusters → DBA authors Spark ELT notebooks in Databricks → Data engineer designs executive Power BI visuals → DBA schedules workspace app audiences

### 26. Which data professional designs fault-tolerant Data Factory pipelines and Spark notebooks that ingest raw store logs, deduplicate malformed JSON events, and load Delta tables in OneLake?

- **A.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **B.** Database administrator (DBA)
- **C.** Data engineer
- **D.** Data analyst

### 27. VeloMart's merchandising director wants interactive Power BI visuals, seasonal sell-through KPIs, and DAX margin measures built over curated warehouse tables to guide markdown decisions. Which role delivers these artifacts?

- **A.** Database administrator (DBA)
- **B.** Data engineer
- **C.** Data analyst
- **D.** Azure Migrate (discovery, readiness assessment, and SKU right-sizing for SQL Server)

### 28. Working in Power BI Desktop, a team member connects to curated Gold tables, defines a `Gross Margin %` DAX measure, and publishes an executive category scorecard. This specialist is acting as a ____.

- **A.** Page blobs in Azure Blob Storage
- **B.** Data engineer
- **C.** Database administrator (DBA)
- **D.** Data analyst

---

## Domain 2 — Identify considerations for relational data on Azure (20–25% official weight · 24 questions)

### 29. In VeloMart's relational schema, `Customers.CustomerID` uniquely identifies each shopper with no `NULL` values, and `Orders.CustomerID` references `Customers.CustomerID` so no order can point to a nonexistent shopper. Which two relational constraints are used? Select two.

- **A.** Unstructured data
- **B.** Primary key constraint
- **C.** Append blobs in Azure Blob Storage
- **D.** Foreign key constraint
- **E.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)

### 30. An `OrderItems` junction table has no single-column surrogate ID; instead, the combination of `(OrderID, ProductID)` uniquely identifies each line item. Together, `(OrderID, ProductID)` forms a ____.

- **A.** Append blobs in Azure Blob Storage
- **B.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **C.** Unstructured data
- **D.** Composite key (multi-column key)

### 31. When an application attempts to delete a `Suppliers` row that still has linked rows in `Products`, the relational engine blocks the delete to prevent orphaned product records. Which constraint enforces this rule?

- **A.** First Normal Form (1NF — atomic values and no repeating column groups)
- **B.** Line chart (tracking continuous trends and changes over ordered time intervals)
- **C.** Foreign key constraint
- **D.** Page blobs in Azure Blob Storage

### 32. Every table in a normalized relational database should include a constraint that guarantees row uniqueness and rejects `NULL` entries on its identifier column(s). This constraint is a ____.

- **A.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **B.** Cool access tier (online, 30-day minimum retention for infrequently accessed data)
- **C.** Primary key constraint
- **D.** Apache Avro row-based binary format with JSON schema

### 33. A junior developer hands you an unnormalized spreadsheet of retail orders containing comma-separated SKU lists and repeated customer city/postal attributes. Which four-step sequence normalizes the schema through Third Normal Form (3NF)?

- **A.** Create foreign keys on unsplit multi-value columns → Denormalize all lookup tables into one wide sheet → Remove partial dependencies (2NF) → Split atomic columns into repeating groups (1NF)
- **B.** Cluster-index raw JSON blobs → Delete primary keys on parent tables → Copy supplier city into every invoice item (2NF) → Combine product names into pipe-delimited strings (3NF)
- **C.** Remove transitive non-key dependencies (3NF) → Merge comma-separated phone lists into one column → Delete all primary keys to speed inserts → Duplicate customer addresses across every order line
- **D.** Split repeating groups into atomic columns (1NF) → Assign a unique primary key → Move partial composite-key dependencies to parent tables (2NF) → Extract transitive non-key dependencies into lookup tables (3NF)

### 34. A `Promotions` table stores `ApplicableTags` as `'Summer,Clearance,VIP'` inside a single text cell and includes `CouponCode1`, `CouponCode2`, and `CouponCode3` columns. Splitting these into atomic cells and child rows achieves ____.

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **C.** First Normal Form (1NF — atomic values and no repeating column groups)
- **D.** Second Normal Form (2NF — full functional dependency on the entire composite key)

### 35. In a 1NF `OrderLines` table keyed by `(OrderID, ProductID)`, column `ProductName` depends only on `ProductID` rather than the whole composite key. Moving `ProductName` to a `Products` table satisfies ____.

- **A.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **B.** First Normal Form (1NF — atomic values and no repeating column groups)
- **C.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **D.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)

### 36. In a 2NF `Stores` table keyed by `StoreID`, column `PostalCode` determines `CityName`, causing `CityName` to depend transitively on `StoreID` via `PostalCode`. Extracting `PostalCode -> CityName` into a separate table achieves ____.

- **A.** First Normal Form (1NF — atomic values and no repeating column groups)
- **B.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **C.** Second Normal Form (2NF — full functional dependency on the entire composite key)
- **D.** Unstructured data

### 37. A retail SQL script runs `CREATE TABLE Returns (...)`, then `INSERT INTO Returns VALUES (...)`, and finally `GRANT SELECT ON Returns TO MerchAnalysts`. Which three SQL statement categories are exercised in this script? Select three.

- **A.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **B.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **C.** Hot access tier (highest storage rate, lowest read/write access cost)
- **D.** Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- **E.** Apache Parquet columnar storage format
- **F.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)

### 38. An analyst writes `SELECT StoreID, SUM(TotalDue) FROM Orders ____ OrderYear = 2026 GROUP BY StoreID ____ SUM(TotalDue) > 100000;`. Which pair of SQL clauses correctly completes the pre-grouping row filter and post-grouping aggregate filter?

- **A.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **B.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **C.** Place `SUM()` or `COUNT(*)` aggregate predicates directly inside the SQL `WHERE` clause before `GROUP BY`
- **D.** `WHERE` filters rows before grouping; `HAVING` filters aggregated groups after `GROUP BY`

### 39. VeloMart wants a report listing **every** registered customer from the `Customers` left table alongside their `Orders` if any exist, showing `NULL` order columns for shoppers who have never placed an order. Which join operator is required?

- **A.** Use DML `SELECT` and `INSERT` statements to grant or revoke user login permissions on schemas
- **B.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **C.** `INNER JOIN` matching related keys present in both tables
- **D.** `LEFT OUTER JOIN` preserving all left-table rows with `NULL` when right-table matches are absent

### 40. Proposed solution: A store developer needs to modify the price of SKU `BK-402` from `$29.99` to `$24.99` in the `Products` table and remove discontinued test rows using `UPDATE` and `DELETE`, classifying both commands under Data Manipulation Language (DML). Is this classification accurate?

- **A.** Use DML `SELECT` and `INSERT` statements to grant or revoke user login permissions on schemas
- **B.** Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- **C.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **D.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)

### 41. VeloMart's `Orders` table stores rows physically sorted on disk by `OrderID` and also needs fast lookups by `CustomerEmail` and `OrderDate` without rearranging the physical table. Which two index types work together here? Select two.

- **A.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **B.** Database view (saved virtual `SELECT` query)
- **C.** Nonclustered index (separate B-tree structure with row locators; multiple allowed per table)
- **D.** Append blobs in Azure Blob Storage
- **E.** Clustered index (defines physical leaf-level sort order; maximum one per table)

### 42. To let merchandising interns query `StoreSalesSummary` without exposing raw cost columns or repeating a 5-table `JOIN`, a DBA saves a named virtual `SELECT` query in the database that stores no separate copy of the rows. This database object is a ____.

- **A.** Stored procedure (parameterized precompiled SQL routine)
- **B.** Create four separate clustered indexes on the same relational table to sort rows four ways physically
- **C.** Database view (saved virtual `SELECT` query)
- **D.** Clustered index (defines physical leaf-level sort order; maximum one per table)

### 43. Checkout services call `EXEC usp_PlaceOrder @CustomerID = 42, @Sku = 'SHOE-9'` to execute parameterized validation, inventory decrement, and order insertion logic precompiled inside SQL Server. Which database object is `usp_PlaceOrder`?

- **A.** Delimited text format (CSV or TSV)
- **B.** Stored procedure (parameterized precompiled SQL routine)
- **C.** Database view (saved virtual `SELECT` query)
- **D.** Nonclustered index (separate B-tree structure with row locators; multiple allowed per table)

### 44. Proposed solution: A junior developer tries to create four clustered indexes on `Products` (`SKU`, `CategoryID`, `BrandID`, `UnitPrice`), fails with an engine error, and instead creates one ____ on `ProductID` plus three nonclustered indexes. What completes this fix?

- **A.** Database view (saved virtual `SELECT` query)
- **B.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **C.** Create four separate clustered indexes on the same relational table to sort rows four ways physically
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 45. VeloMart plans to retire an on-premises SQL Server 2019 cluster and move its retail databases to managed Azure SQL PaaS. Which four-step workflow follows Microsoft's current migration guidance?

- **A.** Convert relational tables into Azure Queue messages → Provision SQL Managed Instance without VNet planning → Run compatibility assessment last → Remove all primary keys before cutover
- **B.** Point production apps to an empty Azure SQL server → Open firewall `0.0.0.0-255.255.255.255` to the public internet → Assess SQL Agent blockers after cutover → Export tables manually as JPEG screenshots
- **C.** Assess SQL Server readiness and SKU sizing in Azure Migrate → Select Azure SQL Database or Managed Instance → Provision target with Entra auth and TLS firewall rules → Migrate schema/data and cut over connection strings
- **D.** Disable TLS encryption on SQL Server → Copy `.mdf` files directly into Azure Table storage → Provision Azure SQL Database Basic tier for cross-DB SQL Agent jobs → Run Azure Migrate discovery

### 46. VeloMart builds two cloud apps on Azure SQL Database: a SaaS portal with 180 single-tenant franchise databases whose busy hours rarely overlap, and a seasonal pop-up promo database that sits idle 20 hours a day and should auto-pause compute. Which two Azure SQL Database options match these needs? Select two.

- **A.** Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)
- **B.** Azure SQL Database Elastic Pool (shared eDTU or vCore compute across multi-tenant DBs)
- **C.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **D.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **E.** Use a single Azure SQL Database to run native SQL Server Agent jobs and cross-database three-part queries

### 47. VeloMart is migrating an ERP database that relies heavily on SQL Server Agent jobs, cross-database three-part queries, and native `.bak` restores, and management wants fully managed PaaS with no OS patching. Which Azure SQL offering fits best?

- **A.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **B.** Use a single Azure SQL Database to run native SQL Server Agent jobs and cross-database three-part queries
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)

### 48. A legacy warehouse management package requires Windows Server registry access, a pinned SQL Server 2016 engine build, and third-party OS-level backup agents on the database host. Which deployment option is required?

- **A.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **B.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)
- **C.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **D.** Azure Database for MySQL — Flexible Server

### 49. Instead of embedding static SQL passwords in web-app configuration files, VeloMart configures passwordless managed identities and MFA-backed admin logins against Azure SQL Database using ____.

- **A.** Microsoft Entra ID centralized authentication with MFA and passwordless managed identities
- **B.** Run the retired standalone Data Migration Assistant (DMA) desktop tool as Microsoft’s current cloud sizing service
- **C.** Cold access tier (online, 90-day minimum retention for rarely accessed data)
- **D.** Delimited text format (CSV or TSV)

### 50. VeloMart's store-locator microservice relies on open-source object-relational custom types, `PL/pgSQL` stored procedures, geometric spatial queries, and `pgAdmin` monitoring without managing Linux VMs. Which Azure PaaS database service should the team provision?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Azure Database for MySQL — Flexible Server
- **C.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **D.** Azure Database for PostgreSQL — Flexible Server

### 51. VeloMart runs a customer community blog built on a Linux, Apache, MySQL, and PHP (`LAMP`) stack and wants a managed PaaS relational backend with automatic backups up to 35 days of point-in-time restore. Which Azure service matches without rewriting SQL queries?

- **A.** Azure Database for MySQL — Flexible Server
- **B.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **C.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **D.** Azure Database for PostgreSQL — Flexible Server

### 52. In Azure Database for PostgreSQL — Flexible Server, enabling Query Store records query execution telemetry inside a system database named `azure_sys` (`query_store.qs_view`). Which open-source Azure PaaS service provides this built-in tuning feature?

- **A.** Use a single Azure SQL Database to run native SQL Server Agent jobs and cross-database three-part queries
- **B.** Azure Database for PostgreSQL — Flexible Server
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

---

## Domain 3 — Describe considerations for working with non-relational data on Azure (15–20% official weight · 20 questions)

### 53. VeloMart ingests daily digital receipt PDFs that customers view frequently during the first month, occasionally through day 90, rarely through year one, and retain seven years for tax audits. Which four-step Blob Storage lifecycle flow minimizes storage cost?

- **A.** Write unstructured video files into Azure Table `RowKey` cells → Age rows from Cool to Hot after 180 days → Convert Page blobs into SQL views → Rehydrate Cool blobs for 12 hours before reading
- **B.** Ingest active operational files directly into Archive tier → Serve millisecond web downloads from Archive without rehydration → Move 90-day files to Hot tier → Delete storage account container metadata
- **C.** Ingest active files into Hot access tier → Transition 30-day infrequent blobs to Cool tier → Move 90-day rarely read blobs to Cold tier → Transition 365-day compliance blobs to offline Archive tier (rehydrating when needed)
- **D.** Mount Archive blobs as an SMB network drive → Stream live append logs into Page blobs in Cold tier → Transition 1-year compliance archives to Hot tier → Rehydrate Hot blobs before every read

### 54. VeloMart's analytics architects evaluate lake storage foundations: one Azure Storage capability that adds POSIX folder ACLs and atomic directory renames on top of Blob Storage, and one tenant-wide SaaS data lake built into Microsoft Fabric with zero-copy Shortcuts. Which two technologies match? Select two.

- **A.** Microsoft OneLake (single tenant-wide SaaS data lake built into Microsoft Fabric)
- **B.** Azure Data Lake Storage Gen2 (Blob Storage with Hierarchical Namespace enabled)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Page blobs in Azure Blob Storage
- **E.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)

### 55. A checkout gateway continuously writes immutable audit lines to the end of hourly log objects where existing bytes must never be modified in place. Which Azure Blob type is optimized specifically for this pattern?

- **A.** Page blobs in Azure Blob Storage
- **B.** Store active operational files directly in Azure Blob Archive tier for immediate millisecond web reads
- **C.** Append blobs in Azure Blob Storage
- **D.** Block blobs in Azure Blob Storage

### 56. VeloMart runs legacy IaaS virtual machines that require random 512-byte read/write disk access for `.vhd` operating-system and data volumes up to 8 TiB. Which Azure Blob type backs these disks?

- **A.** Append blobs in Azure Blob Storage
- **B.** Page blobs in Azure Blob Storage
- **C.** Block blobs in Azure Blob Storage
- **D.** Delimited text format (CSV or TSV)

### 57. Proposed solution: To store 400 TB of 5-year-old warehouse CCTV footage at the lowest possible monthly GB price when regulators allow 12–24 hours notice before viewing a clip, the admin moves the blobs to the ____ and rehydrates clips to Hot or Cool only when requested. Which tier completes this solution?

- **A.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **B.** Store active operational files directly in Azure Blob Archive tier for immediate millisecond web reads
- **C.** Cool access tier (online, 30-day minimum retention for infrequently accessed data)
- **D.** Hot access tier (highest storage rate, lowest read/write access cost)

### 58. VeloMart's store design CAD team needs a cloud share mountable concurrently over `SMB 3.0` on Windows workstations and `NFS 4.1` on Linux render nodes, plus local caching on a branch Windows Server that tiers older files to the cloud. Which two Azure services work together? Select two.

- **A.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **B.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **E.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)

### 59. A legacy back-office billing executable reads configuration `.ini` files from a mapped network drive path (`\\fileserver\billing\`) using standard OS file locks. Which Azure Storage service lets VeloMart lift-and-shift this shared drive without changing application code?

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **D.** Block blobs in Azure Blob Storage

### 60. Regional distribution centers suffer slow WAN links when opening large print labels from cloud shares, so IT deploys an agent on local Windows Server 2022 boxes to cache active files locally while syncing with Azure Files. This capability is ____.

- **A.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **B.** Append blobs in Azure Blob Storage
- **C.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **D.** Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)

### 61. VeloMart stores 80 million lightweight IoT shelf-tag battery status entities keyed by `StoreID` and `TagMAC`, needing low-cost key-value point lookups with no foreign keys or table joins. In ____, those two keys map to `PartitionKey` and `RowKey`.

- **A.** Enforce server-side foreign keys and multi-table SQL `INNER JOIN` queries inside Azure Table storage
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)

### 62. Proposed solution: A developer chooses Azure Table storage expecting the storage service to enforce server-side foreign keys and execute multi-table SQL `INNER JOIN` queries; the architect rejects that assumption because Azure Table storage indexes entities solely on `PartitionKey` and `RowKey` without server-side joins. Which service's true behavior did the architect describe?

- **A.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **B.** Enforce server-side foreign keys and multi-table SQL `INNER JOIN` queries inside Azure Table storage
- **C.** Clustered index (defines physical leaf-level sort order; maximum one per table)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 63. VeloMart's `PartitionKey`/`RowKey` loyalty lookup app outgrows standard Azure Table storage because it now requires turnkey multi-region active-active writes, automatic secondary indexes, and single-digit millisecond latency SLAs without rewriting Table SDK calls. Which offering upgrades it cleanly?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **C.** Data Definition Language (`CREATE`, `ALTER`, `DROP`)
- **D.** Page blobs in Azure Blob Storage

### 64. VeloMart launches a global mobile shopping cart serving Tokyo, Frankfurt, and Virginia shoppers simultaneously with `<10 ms` read/write SLAs, multi-region writes, and autoscale capacity billed in normalized compute/IO request currency. Which two Azure Cosmos DB capabilities power this? Select two.

- **A.** Azure Cosmos DB turnkey global distribution with multi-region writes and <10 ms SLAs
- **B.** Request Units (RUs) normalized compute/IO currency (Provisioned, Autoscale, or Serverless)
- **C.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **D.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **E.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)

### 65. When a logged-in VeloMart shopper adds sneakers to their cart, that shopper must immediately read their own updated cart in order, without paying the latency penalty of global linearizable Strong consistency. Cosmos DB's default ____ level guarantees this.

- **A.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **B.** Session consistency (default level guaranteeing read-your-own-writes and monotonic reads per client session)
- **C.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)
- **D.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating

### 66. A gift-card settlement microservice on Azure Cosmos DB cannot tolerate any regional replica returning a slightly stale balance; every read must be guaranteed to return the latest committed write globally. Which consistency level enforces linearizable reads?

- **A.** Session consistency (default level guaranteeing read-your-own-writes and monotonic reads per client session)
- **B.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)
- **C.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **D.** Cool access tier (online, 30-day minimum retention for infrequently accessed data)

### 67. A product star-rating counter widget in Azure Cosmos DB prioritizes the lowest possible read/write latency and RU cost, and temporary out-of-order review counts across continents are completely acceptable. Which consistency level fits best?

- **A.** Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)
- **B.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **C.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **D.** Isolation (concurrent transactions do not interfere)

### 68. VeloMart is deploying a greenfield JSON product catalog on Azure Cosmos DB. Which four-step workflow follows best practices from account creation through querying?

- **A.** Provision an Azure Files SMB share → Enable Strong consistency across 5 multi-write regions simultaneously → Omit databases and write JSON straight to subscription tags → Query vertices using `SMB2` locks
- **B.** Create a Cosmos DB account choosing the target API → Create a database and container with a high-cardinality partition key → Configure RU/s or serverless and consistency → Insert items and run partition-scoped queries
- **C.** Install OS patches on Cosmos DB virtual machines → Format NTFS volumes for JSON items → Assign a constant single-value partition key to all 100 million documents → Query exclusively with T-SQL stored procedures
- **D.** Create a container without a partition key → Switch the existing account between Cassandra, Gremlin, and NoSQL APIs daily → Enforce 3NF foreign-key joins across containers → Store 500 MB MP4 blobs inside single JSON items

### 69. A greenfield .NET retail microservice stores native JSON order documents in Azure Cosmos DB and queries nested arrays using `SELECT c.orderId, c.total FROM c WHERE c.storeId = 'S104'`. Which Cosmos DB API is used?

- **A.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **B.** Azure Cosmos DB for MongoDB (wire-protocol compatibility for BSON document apps)
- **C.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **D.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)

### 70. VeloMart acquires a boutique marketplace whose Node.js backend uses Mongoose drivers and BSON documents, and wants to lift-and-shift to Azure Cosmos DB merely by updating the connection string. Which Cosmos DB API should be selected at account creation?

- **A.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)
- **B.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating
- **C.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **D.** Azure Cosmos DB for MongoDB (wire-protocol compatibility for BSON document apps)

### 71. To generate real-time `"Shoppers who bought X also co-purchased Y"` recommendations across millions of shopper and item vertices connected by weighted edges, which Azure Cosmos DB API should VeloMart choose?

- **A.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)
- **B.** Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)

### 72. Proposed solution: An acquired logistics tracker writes wide-column shipment checkpoints using Cassandra Query Language (`CQL`); instead of trying to switch an existing NoSQL account's API in place, the engineer creates a dedicated ____ account. Which API completes the solution?

- **A.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **B.** Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)
- **C.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **D.** Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating

---

## Domain 4 — Describe an analytics workload on Azure (25–30% official weight · 28 questions)

### 73. VeloMart's data engineering team is implementing a modern medallion lakehouse pipeline in Microsoft Fabric for 40 retail source systems. Which four-step sequence implements the ELT Bronze-Silver-Gold pattern?

- **A.** Build Power BI visuals directly against uncleaned CSV attachments → Delete raw source history immediately → Normalize Gold tables into 3NF OLTP row stores → Export final aggregates back into email inboxes
- **B.** Transform terabytes on the client laptop in Notepad → Upload screenshots to Archive Blob tier → Query offline blobs live with DAX → Store fact tables inside Azure Queue messages
- **C.** Extract source data via Data Factory pipeline → Land raw files into OneLake / ADLS Gen2 (Bronze) → Cleanse and conform Delta tables via Spark or SQL (Silver) → Model star-schema fact/dimension tables (Gold) for BI
- **D.** Publish Gold star schema before ingesting source data → Run OLTP checkout locks inside Power BI Mobile → Overwrite source ERP primary keys during read → Store Parquet files in DNS TXT records

### 74. Rather than transforming multi-terabyte web clickstreams on a middle-tier server before storage, VeloMart loads raw JSON files straight into OneLake and uses distributed Spark pools to transform them in place. This ingestion pattern is ____.

- **A.** Extract, Load, and Transform (ELT) pattern
- **B.** Extract, Transform, and Load (ETL) pattern
- **C.** Page blobs in Azure Blob Storage
- **D.** Online Transaction Processing (OLTP) workload

### 75. VeloMart needs a cloud orchestration service with 90+ built-in connectors, scheduled and event-driven Copy pipelines, and visual Power Query Dataflows Gen2 to move nightly ERP tables into lakehouse storage. Which service provides these capabilities?

- **A.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **B.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **C.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **D.** Azure Data Factory / Fabric Data Factory pipelines and Dataflows Gen2

### 76. VeloMart wants a single analytical storage pattern that brings ACID transactions and SQL queries directly over open Delta Parquet files in OneLake, organized into `FactSales` and single-hop `DimProduct` / `DimDate` tables for fast BI. Which two concepts combine here? Select two.

- **A.** Page blobs in Azure Blob Storage
- **B.** Data lakehouse (Delta Lake ACID transactions and SQL/Spark queries directly over open Parquet files)
- **C.** Star schema (central numeric fact table joined directly to denormalized dimension tables)
- **D.** Online Transaction Processing (OLTP) workload
- **E.** Third Normal Form (3NF — no transitive dependencies between non-key columns)

### 77. In VeloMart's merchandising warehouse, `FactSales` links to `DimProduct`, which normalizes `SubcategoryID` into `DimSubcategory`, which in turn links to `DimDepartment`. Normalizing dimension hierarchies into chained sub-tables forms a ____.

- **A.** Key-value non-relational store
- **B.** Append blobs in Azure Blob Storage
- **C.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **D.** Star schema (central numeric fact table joined directly to denormalized dimension tables)

### 78. Which analytical data store architecture eliminates maintaining separate raw data lakes and proprietary relational warehouses by supporting ACID transactions, schema enforcement, and time travel directly over open Delta Lake Parquet files?

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **C.** First Normal Form (1NF — atomic values and no repeating column groups)
- **D.** Data lakehouse (Delta Lake ACID transactions and SQL/Spark queries directly over open Parquet files)

### 79. VeloMart's architecture board compares Microsoft cloud services for petabyte-scale enterprise analytics: a unified SaaS platform built on OneLake, a collaborative Apache Spark and ML platform with Unity Catalog, and an Azure PaaS studio combining serverless/dedicated SQL pools with Spark pools. Which three services are being compared? Select three.

- **A.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **B.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **C.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **D.** Azure Synapse Analytics (serverless SQL pools, dedicated MPP SQL pools, and Spark pools)
- **E.** Microsoft Fabric (unified SaaS analytics platform atop OneLake)
- **F.** Azure Databricks (collaborative Apache Spark analytics, Delta Lake, and ML platform)

### 80. VeloMart wants an end-to-end SaaS analytics platform where Data Factory, Spark Data Engineering, T-SQL Data Warehouse, Real-Time Intelligence, and Power BI Direct Lake all share a single tenant-wide OneLake without copying files between services. Which platform delivers this?

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Microsoft Fabric (unified SaaS analytics platform atop OneLake)
- **C.** SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)
- **D.** Azure HDInsight (managed open-source Hadoop, Hive, HBase, Kafka, and Spark clusters)

### 81. Data scientists and data engineers at VeloMart collaborate in shared Python, Scala, and SQL notebooks on auto-scaling Apache Spark clusters optimized for Delta Lake and machine-learning experiment tracking. Which Azure service is tailored for this workflow?

- **A.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **B.** Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Azure Databricks (collaborative Apache Spark analytics, Delta Lake, and ML platform)

### 82. An acquired retail subsidiary runs legacy on-premises Apache Hadoop MapReduce, Hive, and HBase jobs and needs managed open-source cluster hosting on Azure to lift-and-shift those exact frameworks. Which Azure service fits?

- **A.** Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)
- **B.** Azure HDInsight (managed open-source Hadoop, Hive, HBase, Kafka, and Spark clusters)
- **C.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **D.** Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)

### 83. Every Sunday at 02:00 UTC, VeloMart aggregates the prior week's settled store receipts to generate vendor rebate statements. Processing a bounded collection of accumulated records on a schedule is ____.

- **A.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)
- **B.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)
- **C.** Strong consistency (linearizable reads guaranteed to return the latest committed write)
- **D.** Batch data processing (scheduled execution over bounded collections of accumulated records)

### 84. VeloMart evaluates checkout card swipes within 200 milliseconds of arrival so stolen cards are declined before the payment terminal prints a receipt. Evaluating unbounded events continuously in motion is ____.

- **A.** Stream data processing (continuous low-latency evaluation of unbounded events in motion)
- **B.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **C.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **D.** Third Normal Form (3NF — no transitive dependencies between non-key columns)

### 85. VeloMart's live ops screen computes total orders placed in non-overlapping, back-to-back 5-minute intervals (`10:00–10:05`, `10:05–10:10`, `10:10–10:15`) where each checkout belongs to exactly one window. Which windowing function is used?

- **A.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **B.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **C.** Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)
- **D.** Session window (variable-length activity bursts closed after a quiet timeout gap)

### 86. Every 1 minute, VeloMart calculates the moving average checkout latency over the preceding 5-minute window so adjacent 5-minute windows overlap by 4 minutes. Which stream window type schedules overlapping fixed-length intervals?

- **A.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **B.** Session window (variable-length activity bursts closed after a quiet timeout gap)
- **C.** Batch data processing (scheduled execution over bounded collections of accumulated records)
- **D.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)

### 87. VeloMart streams 250,000 web clickstream telemetry events per second into a partitioned cloud event broker (compatible with Kafka producers) and runs a serverless SQL-like windowed query to flag checkout abandonment spikes in real time. Which two Azure services pair together here? Select two.

- **A.** Azure Event Hubs (high-throughput partitioned event ingestion broker with Kafka support)
- **B.** Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)
- **C.** Azure Stream Analytics (serverless SQL-like stream processing engine with windowing functions)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **E.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)

### 88. Inside Microsoft Fabric, VeloMart routes live store kiosk events with **Eventstream**, indexes billions of time-series logs for sub-second KQL queries in an **Eventhouse**, displays live tiles, and triggers automated restock alerts via **Activator**. Which Fabric workload provides these components?

- **A.** Microsoft Fabric Real-Time Intelligence (Eventstream, Eventhouse KQL database, Real-Time Dashboards, and Activator)
- **B.** Azure SQL Database (fully managed single-database or elastic-pool PaaS)
- **C.** Cold access tier (online, 90-day minimum retention for rarely accessed data)
- **D.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)

### 89. Data engineers in Azure Databricks process live inventory Kafka streams as an unbounded DataFrame using Python/SQL APIs with fault-tolerant checkpointing into Delta Lake tables. Which streaming engine are they using?

- **A.** Apache Spark Structured Streaming (fault-tolerant DataFrame/SQL stream processing in Databricks and Fabric)
- **B.** Database view (saved virtual `SELECT` query)
- **C.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **D.** Batch data processing (scheduled execution over bounded collections of accumulated records)

### 90. VeloMart groups a shopper's mobile app taps into variable-length browsing bursts that close automatically once the user stops tapping for 3 minutes of inactivity. Which streaming window groups activity bursts separated by quiet gaps?

- **A.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **B.** Apache Parquet columnar storage format
- **C.** Tumbling window (fixed-size, contiguous, non-overlapping time intervals)
- **D.** Session window (variable-length activity bursts closed after a quiet timeout gap)

### 91. VeloMart's BI team wants to transform raw warehouse tables, model DAX measures, pin an executive summary dashboard, and distribute governed read-only access to 400 store managers. Which four-step Power BI workflow is accurate?

- **A.** Pin dashboard tiles in Power BI Desktop offline → Write Power Query M transformations inside Power BI Mobile → Store semantic models on SMB floppy shares → Require every executive viewer to edit DAX in Desktop
- **B.** Author multi-report dashboards inside Power BI Mobile → Export `.pbix` files to Azure Table storage → Schedule dataset refresh inside Windows Notepad → Email raw database passwords to report viewers
- **C.** Shape source data with Power Query in Power BI Desktop → Relate star-schema tables, write DAX, and build report pages → Publish model and report to Power BI Service → Pin dashboard tiles, schedule refresh, and share an App
- **D.** Design `.rdl` pixel-perfect invoices in Azure Stream Analytics → Publish directly to unmanaged personal OneDrive as an OLTP database → Disable table relationships → Share via anonymous firewall port `1433`

### 92. Proposed solution: A store analyst tries to create a single-canvas multi-report dashboard with pinned visual tiles offline inside Power BI Desktop; a senior BI lead explains that multi-report pinned dashboards can only be created in ____. What completes the correction?

- **A.** Microsoft Power BI Service (cloud SaaS portal for workspaces, dashboards, scheduled refresh, and Apps)
- **B.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **C.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **D.** Create multi-report pinned dashboards directly inside Power BI Desktop offline

### 93. VeloMart's accounting department needs pixel-perfect, multi-page PDF vendor remittance invoices that print every line item across 30 pages with fixed page headers and footers (`.rdl` format). Which Power BI tool is designed for this?

- **A.** Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)
- **B.** Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)
- **C.** Microsoft Power BI Service (cloud SaaS portal for workspaces, dashboards, scheduled refresh, and Apps)
- **D.** Azure Stream Analytics (serverless SQL-like stream processing engine with windowing functions)

### 94. In Power BI, VeloMart defines `1:*` relationships from `DimDate` and `DimStore` to `FactSales`, hides surrogate integer keys from report viewers, and writes `YoY Revenue %` so it recalculates dynamically whenever a user slices by region or quarter. Which two Power BI modeling elements are described? Select two.

- **A.** Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)
- **B.** Append blobs in Azure Blob Storage
- **C.** Data Control Language (`GRANT`, `REVOKE`, `DENY`)
- **D.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **E.** Power BI semantic model (relationships, DAX measures, hierarchies, and Import/DirectQuery/Direct Lake storage)

### 95. Unlike a calculated column whose values are materialized row-by-row during dataset refresh, `Total Margin := SUM(FactSales[Margin])` uses zero extra column RAM and recalculates on the fly as report slicers change. `Total Margin` is a ____.

- **A.** DAX measure (dynamic aggregation evaluated at query time in the current report filter context)
- **B.** Delimited text format (CSV or TSV)
- **C.** Hot access tier (highest storage rate, lowest read/write access cost)
- **D.** Clustered index (defines physical leaf-level sort order; maximum one per table)

### 96. To let store managers drill smoothly from `Year -> Quarter -> Month -> Date` on any visual and ensure filters flow cleanly from `DimProduct` (`1`) to `FactSales` (`*`), where does the analyst configure hierarchies and relationship cardinality?

- **A.** Apache Avro row-based binary format with JSON schema
- **B.** Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)
- **C.** Power BI semantic model (relationships, DAX measures, hierarchies, and Import/DirectQuery/Direct Lake storage)
- **D.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)

### 97. Microsoft's official Power BI modeling guidance recommends organizing semantic models with dimension tables for filtering/grouping and fact tables for numeric summarization rather than a single wide flat file or deeply normalized 3NF OLTP chains. Which schema design is recommended?

- **A.** Append blobs in Azure Blob Storage
- **B.** Key-value non-relational store
- **C.** Third Normal Form (3NF — no transitive dependencies between non-key columns)
- **D.** Star schema (central numeric fact table joined directly to denormalized dimension tables)

### 98. VeloMart's VP of E-Commerce wants to visualize daily website conversion rate continuously across all 365 days of the past year to spot holiday trends and seasonal dips. Which Power BI visual is most appropriate?

- **A.** Line chart (tracking continuous trends and changes over ordered time intervals)
- **B.** Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)
- **C.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)
- **D.** Treemap (or pie/donut chart for small category counts) showing part-to-whole proportions

### 99. A regional manager wants to compare total Q3 revenue side by side across 12 discrete product categories ranked from highest to lowest. Which Power BI visual provides the clearest categorical comparison?

- **A.** Bar or column chart (comparing discrete categorical values across items)
- **B.** Line chart (tracking continuous trends and changes over ordered time intervals)
- **C.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)
- **D.** Page blobs in Azure Blob Storage

### 100. On an executive summary dashboard tile, the CEO wants one prominent visual showing current month-to-date net sales (`$14.2M`), the trend line across days of the month, and green/red status against the `$15.0M` monthly target. Which Power BI visual is built specifically for this?

- **A.** Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)
- **B.** KPI visual or Card (highlighting a single headline metric or progress toward a target goal)
- **C.** Apache Avro row-based binary format with JSON schema
- **D.** Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)

---

## Answer Key and Explanations

### Question 1 — `A` (Describe core data concepts)

Correct answer: A (is correct). Fixed rows and typed columns adhering to a uniform tabular schema define structured data. [Skill 1.1: Describe the features of structured data | Source: Explore core data concepts — Identify data formats (structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **B:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **C:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.

### Question 2 — `B` (Describe core data concepts)

Correct answer: B (is correct). Relational tables with predefined column names and enforced types represent structured data. [Skill 1.1: Describe the features of structured data | Source: Explore core data concepts — Identify data formats (structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **B:** Correct. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **C:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.

### Question 3 — `A, D` (Describe core data concepts)

Correct answers: A and D (are correct). Variable per-item attributes organized via hierarchical key-value tags and arrays characterize semi-structured JSON documents. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Correct. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **B:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **C:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **D:** Correct. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **E:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 4 — `B` (Describe core data concepts)

Correct answer: B (is correct). Self-describing hierarchical tags and nested key-value pairs without a fixed relational table schema represent semi-structured data. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **B:** Correct. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **C:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.

### Question 5 — `B` (Describe core data concepts)

Correct answer: B (is correct). JSON represents hierarchical key-value pairs and arrays natively across web APIs and document stores. [Skill 1.2: Describe the features of semi-structured data | Source: Explore core data concepts — Identify data formats (semi-structured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Correct. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **C:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 6 — `B` (Describe core data concepts)

Correct answer: B (is correct). Raw binary media files such as JPEG photos, MP4 videos, and WAV audio lack an internal field schema and are unstructured data. [Skill 1.3: Describe the features of unstructured data | Source: Explore core data concepts — Identify data formats (unstructured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.
- **B:** Correct. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **C:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **D:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.

### Question 7 — `D` (Describe core data concepts)

Correct answer: D (is correct). Video streams and scanned PDF blobs have no predefined row-or-tag schema and are classified as unstructured data. [Skill 1.3: Describe the features of unstructured data | Source: Explore core data concepts — Identify data formats (unstructured data) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)]

- **A:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **B:** Incorrect. Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.
- **C:** Incorrect. A composite key combines two or more columns (such as `OrderID` + `ProductID`) to uniquely identify rows in a junction or line-item table.
- **D:** Correct. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.

### Question 8 — `C, E` (Describe core data concepts)

Correct answers: C and E (are correct). Apache Parquet and ORC are compressed columnar file formats that allow analytical engines to read only requested columns. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Incorrect. JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Correct. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **E:** Correct. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.

### Question 9 — `D` (Describe core data concepts)

Correct answer: D (is correct). Plain-text rows whose fields are separated by commas or tabs with optional header text use the delimited CSV/TSV format. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Incorrect. ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.
- **B:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **C:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **D:** Correct. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 10 — `A` (Describe core data concepts)

Correct answer: A (is correct). Apache Avro pairs a JSON schema header with compact row-oriented binary records, making it ideal for streaming and schema evolution. [Skill 1.4: Describe common formats for data files | Source: Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)]

- **A:** Correct. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **B:** Incorrect. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 11 — `A, B` (Describe core data concepts)

Correct answers: A and B (are correct). Key-value stores excel at fast single-key session lookups, while document databases index nested JSON attributes for flexible catalog queries. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Correct. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.
- **B:** Correct. A document database stores self-contained JSON/BSON documents indexed across nested attributes so each entity can evolve fields without schema migrations.
- **C:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **D:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **E:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 12 — `A` (Describe core data concepts)

Correct answer: A (is correct). Graph databases store vertices and directed edges to execute fast multi-hop relationship traversals. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Correct. A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.
- **B:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **C:** Incorrect. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.

### Question 13 — `D` (Describe core data concepts)

Correct answer: D (is correct). Column-family (wide-column) databases group related columns into families keyed by row/partition keys for massive write scale. [Skill 1.5: Describe features of common data stores including databases | Source: Explore core data concepts — Explore databases (relational and non-relational stores) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)]

- **A:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
- **B:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **C:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **D:** Correct. A column-family database groups related columns into families keyed by row and partition keys (such as Apache Cassandra or HBase) for massive write throughput.

### Question 14 — `C` (Describe core data concepts)

Correct answer: C (is correct). Live ACID checkouts belong in Azure SQL Database, Data Factory extracts history into ADLS Gen2 / OneLake Parquet files, and Power BI serves star-schema visuals. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Incorrect. Paginated reports render formatted output rather than ingesting transactions, and Blob Cold tier does not execute multi-row ACID relational transactions.
- **B:** Incorrect. Power BI Service is a read-optimized BI platform rather than a transactional database, and Queue storage buffers small messages rather than archiving relational rows.
- **C:** Correct. Operational transactions commit in an ACID relational store first, pipelines land history in columnar lake storage, and analytical models serve BI reports without taxing OLTP.
- **D:** Incorrect. Archive blobs are offline and unreadable for live OLTP writes, Power BI Desktop is an authoring tool rather than an OLTP engine, and Table storage is schemaless key-value.

### Question 15 — `C` (Describe core data concepts)

Correct answer: C (is correct). Azure SQL Database is a managed PaaS relational engine providing ACID transactions, foreign keys, and zero OS patch overhead. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Correct. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **D:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 16 — `A` (Describe core data concepts)

Correct answer: A (is correct). Block blobs in Azure Blob Storage store massive volumes of unstructured images and PDFs cost-effectively over HTTPS. [Skill 1.6: Identify Azure datastores for common use cases | Source: Explore data roles and services — Identify Azure data services (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)]

- **A:** Correct. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.
- **B:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **C:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Incorrect. Azure Queue storage holds small asynchronous work messages (up to 64 KB per message), not multi-gigabyte binary files.

### Question 17 — `B, D, E` (Describe core data concepts)

Correct answers: B, D, and E (are correct). All-or-nothing execution is Atomicity, shielding concurrent in-flight edits is Isolation, and persisting committed writes across crashes is Durability. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **B:** Correct. Atomicity guarantees that every statement in a transaction either succeeds together or rolls back completely if any step fails, preventing half-completed transfers.
- **C:** Incorrect. Pie/donut charts show part-to-whole shares for a few slices, while treemaps use nested rectangles to display proportional composition across larger hierarchical categories.
- **D:** Correct. Isolation prevents concurrent in-flight transactions from reading uncommitted intermediate edits or overwriting each other unpredictably via locking or row versioning.
- **E:** Correct. Durability guarantees that once a transaction commits, its changes are persisted to non-volatile transaction logs/storage and survive power loss or crash recovery.
- **F:** Incorrect. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.

### Question 18 — `D` (Describe core data concepts)

Correct answer: D (is correct). High-concurrency, low-latency row reads and writes against normalized tables with ACID guarantees define an OLTP workload. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **B:** Incorrect. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **C:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **D:** Correct. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.

### Question 19 — `B` (Describe core data concepts)

Correct answer: B (is correct). Consistency guarantees every transaction moves the database only from one valid constraint-compliant state to another. [Skill 1.7: Describe features of transactional workloads | Source: Explore core data concepts — Explore transactional data processing (OLTP and ACID) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)]

- **A:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **B:** Correct. Consistency ensures a transaction transitions the database only from one valid rule-compliant state (keys, check constraints, types) to another.
- **C:** Incorrect. Denormalized historical scans belong in an OLAP store; live checkout requires normalized OLTP tables with ACID guarantees to prevent lost or corrupted orders.
- **D:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.

### Question 20 — `B, E` (Describe core data concepts)

Correct answers: B and E (are correct). Read-intensive historical aggregations over denormalized fact and dimension tables define an OLAP star-schema workload. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **B:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. Isolation prevents concurrent in-flight transactions from reading uncommitted intermediate edits or overwriting each other unpredictably via locking or row versioning.
- **E:** Correct. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.

### Question 21 — `A` (Describe core data concepts)

Correct answer: A (is correct). Read-heavy historical aggregation and trend analysis separated from live operational writes is an OLAP workload. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Correct. OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.
- **B:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **C:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.

### Question 22 — `B` (Describe core data concepts)

Correct answer: B (is correct). A central quantitative fact table surrounded by single-hop denormalized dimension tables forms a star schema. [Skill 1.8: Describe features of analytical workloads | Source: Explore core data concepts — Explore analytical data processing (OLAP) (https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)]

- **A:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.

### Question 23 — `D` (Describe core data concepts)

Correct answer: D (is correct). Provisioning, securing, backing up, restoring, and performance-tuning database servers are core DBA responsibilities. [Skill 1.9: Describe responsibilities for database administrators | Source: Explore data roles and services — Database administrator responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **B:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **D:** Correct. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.

### Question 24 — `A` (Describe core data concepts)

Correct answer: A (is correct). Backup recovery and database security permission governance belong to the database administrator (DBA). [Skill 1.9: Describe responsibilities for database administrators | Source: Explore data roles and services — Database administrator responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Correct. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **B:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **C:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **D:** Incorrect. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.

### Question 25 — `C` (Describe core data concepts)

Correct answer: C (is correct). The DBA secures operational SQL, the data engineer builds ELT pipelines and curates Gold star tables, and the data analyst authors DAX KPIs and Power BI visuals. [Skill 1.10: Describe responsibilities for data engineers | Source: Explore data roles and services — Data engineer responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. Operational DB security and PITR restores are DBA duties, network/pipeline plumbing belongs to infra/data engineering, and analysts focus on semantic models and visuals.
- **B:** Incorrect. KPI scorecards and sales packs are data analyst outputs, whereas Spark streaming pipelines belong to data engineers and OLTP index maintenance belongs to DBAs.
- **C:** Correct. DBAs govern operational database engines, data engineers build ingestion/transformation pipelines into curated analytical stores, and data analysts model KPIs and visual reports.
- **D:** Incorrect. Cluster HA belongs to the DBA, Spark ELT pipelines belong to the data engineer, and visual storytelling/app distribution belongs to the data analyst.

### Question 26 — `C` (Describe core data concepts)

Correct answer: C (is correct). Designing and operating batch/streaming ingestion and cleansing pipelines into lakehouse stores is the data engineer's role. [Skill 1.10: Describe responsibilities for data engineers | Source: Explore data roles and services — Data engineer responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **B:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **C:** Correct. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **D:** Incorrect. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.

### Question 27 — `C` (Describe core data concepts)

Correct answer: C (is correct). Data analysts model semantic relationships/DAX measures and design interactive reports and dashboards for business stakeholders. [Skill 1.11: Describe responsibilities for data analysts | Source: Explore data roles and services — Data analyst responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **B:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **C:** Correct. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.
- **D:** Incorrect. Azure Migrate discovers on-premises SQL Server instances, evaluates feature compatibility blockers, and recommends right-sized Azure SQL targets (replacing retired DMA).

### Question 28 — `D` (Describe core data concepts)

Correct answer: D (is correct). Building semantic calculations and visual business scorecards from curated data is the responsibility of a data analyst. [Skill 1.11: Describe responsibilities for data analysts | Source: Explore data roles and services — Data analyst responsibilities (https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Incorrect. A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.
- **C:** Incorrect. A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.
- **D:** Correct. A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.

### Question 29 — `B, D` (Identify considerations for relational data on Azure)

Correct answers: B and D (are correct). A primary key uniquely identifies parent rows without NULLs, and a foreign key enforces referential integrity from child to parent rows. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **B:** Correct. A primary key uniquely identifies each row in a relational table and implicitly forbids `NULL` and duplicate key values.
- **C:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **D:** Correct. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.
- **E:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.

### Question 30 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Combining two or more columns to uniquely identify a row in a table defines a composite key. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **C:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.
- **D:** Correct. A composite key combines two or more columns (such as `OrderID` + `ProductID`) to uniquely identify rows in a junction or line-item table.

### Question 31 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). A foreign key constraint enforces referential integrity between child and parent tables, preventing orphaned child rows. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **B:** Incorrect. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.
- **C:** Correct. A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 32 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). A primary key uniquely identifies every row in a table and disallows NULL values. [Skill 2.1: Identify features of relational data | Source: Explore fundamental relational data concepts — Understand relational data (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)]

- **A:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **B:** Incorrect. The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.
- **C:** Correct. A primary key uniquely identifies each row in a relational table and implicitly forbids `NULL` and duplicate key values.
- **D:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.

### Question 33 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Normalization moves from 1NF atomic columns and a primary key, to 2NF removing partial composite-key dependencies, to 3NF removing transitive non-key dependencies. [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. Foreign keys require atomic primary keys first, and 1NF eliminates repeating groups rather than creating them.
- **B:** Incorrect. Copying supplier attributes into invoice items creates transitive redundancy, and pipe-delimited multi-value strings violate 1NF.
- **C:** Incorrect. You cannot achieve 3NF before 1NF/2NF, comma-separated lists violate 1NF atomicity, and duplicating addresses reintroduces update anomalies.
- **D:** Correct. Normalization progresses sequentially: 1NF enforces atomic values and row uniqueness, 2NF removes partial dependencies on composite keys, and 3NF eliminates transitive non-key dependencies.

### Question 34 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Eliminating multi-valued cells and repeating column groups so every attribute holds one atomic value satisfies First Normal Form (1NF). [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **C:** Correct. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **D:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.

### Question 35 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Removing partial dependencies on a subset of a composite primary key brings a 1NF table into Second Normal Form (2NF). [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **B:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **C:** Correct. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **D:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.

### Question 36 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Eliminating transitive dependencies between non-key columns brings a 2NF table into Third Normal Form (3NF). [Skill 2.2: Describe normalization and why it is used | Source: Explore fundamental relational data concepts — Understand normalization (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)]

- **A:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **B:** Correct. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **C:** Incorrect. 2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.
- **D:** Incorrect. Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.

### Question 37 — `B, D, F` (Identify considerations for relational data on Azure)

Correct answers: B, D, and F (are correct). `CREATE TABLE` is DDL, `INSERT INTO` is DML, and `GRANT SELECT` is DCL. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **B:** Correct. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **C:** Incorrect. The Hot tier is online storage optimized for data that is accessed or modified frequently, carrying the lowest transaction/read cost.
- **D:** Correct. DML statements query, add, modify, or delete row data stored inside relational tables.
- **E:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **F:** Correct. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.

### Question 38 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). In SQL, `WHERE` filters individual rows before `GROUP BY`, whereas `HAVING` filters aggregated group totals after `GROUP BY`. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **B:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **C:** Incorrect. SQL `WHERE` evaluates individual pre-grouped rows and rejects aggregate functions; group-level aggregate filters belong in the `HAVING` clause.
- **D:** Correct. `WHERE` predicates evaluate individual source rows prior to aggregation, whereas `HAVING` filters grouped summary results such as `HAVING COUNT(*) > 5`.

### Question 39 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). A `LEFT OUTER JOIN` returns all rows from the left table and populates `NULL` where no matching right-table row exists. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. Granting and revoking security permissions belongs to DCL (`GRANT`, `REVOKE`, `DENY`), not DML.
- **B:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **C:** Incorrect. `INNER JOIN` returns only row pairs whose join predicate matches in both the left and right tables, excluding unmatched rows.
- **D:** Correct. `LEFT OUTER JOIN` keeps every row from the left table (for example, all customers) and fills `NULL` for right-table columns when no related order exists.

### Question 40 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Yes — `SELECT`, `INSERT`, `UPDATE`, and `DELETE` are the core DML commands that read and modify row data. [Skill 2.3: Identify common structured query language (SQL) statements | Source: Explore fundamental relational data concepts — Explore SQL statements (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)]

- **A:** Incorrect. Granting and revoking security permissions belongs to DCL (`GRANT`, `REVOKE`, `DENY`), not DML.
- **B:** Correct. DML statements query, add, modify, or delete row data stored inside relational tables.
- **C:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **D:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.

### Question 41 — `C, E` (Identify considerations for relational data on Azure)

Correct answers: C and E (are correct). A single clustered index defines physical row order (`OrderID`), while multiple nonclustered indexes maintain separate B-trees with pointers for additional search columns. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **B:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **C:** Correct. A nonclustered index maintains a separate sorted key structure pointing back to the base table rows, accelerating selective lookups on non-primary search columns.
- **D:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **E:** Correct. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.

### Question 42 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). A standard database view is a saved virtual `SELECT` query that abstracts joins and restricts column visibility without duplicating row storage. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.
- **B:** Incorrect. Because a clustered index dictates the single physical leaf-level storage order of the table’s rows, a table can have at most one clustered index (plus multiple nonclustered indexes).
- **C:** Correct. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **D:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.

### Question 43 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). A stored procedure encapsulates parameterized SQL statements and procedural logic executed via `EXEC` on the server. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **B:** Correct. A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.
- **C:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **D:** Incorrect. A nonclustered index maintains a separate sorted key structure pointing back to the base table rows, accelerating selective lookups on non-primary search columns.

### Question 44 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Because a clustered index controls the single physical storage sort order of table rows, each table can have at most one clustered index. [Skill 2.4: Identify common database objects | Source: Explore fundamental relational data concepts — Describe database objects (https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)]

- **A:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **B:** Correct. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **C:** Incorrect. Because a clustered index dictates the single physical leaf-level storage order of the table’s rows, a table can have at most one clustered index (plus multiple nonclustered indexes).
- **D:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 45 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). Azure Migrate assesses compatibility and right-sizes SKUs first, followed by secure Microsoft Entra/TLS target provisioning, schema/data sync, and connection cutover. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Queue storage is not a relational migration vehicle, SQL Managed Instance requires VNet subnet sizing upfront, and removing primary keys corrupts relational integrity.
- **B:** Incorrect. Cutting over before data migration breaks production, opening all public IPs violates security, and assessments must run before selecting the target SKU.
- **C:** Correct. Azure Migrate discovers workloads, flags compatibility blockers, and recommends right-sized Azure SQL targets before secure provisioning, data sync, and connection cutover.
- **D:** Incorrect. Azure Table storage cannot mount `.mdf` database files, and single Azure SQL Database does not host SQL Server Agent or cross-database instance queries.

### Question 46 — `A, B` (Identify considerations for relational data on Azure)

Correct answers: A and B (are correct). Elastic Pools share compute across many multi-tenant DBs with staggered spikes, while Serverless auto-scales and auto-pauses idle single databases. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Correct. The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.
- **B:** Correct. An Elastic Pool shares a pool of compute resources across multiple single databases that have unpredictable, staggered usage spikes to optimize cost.
- **C:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **D:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **E:** Incorrect. Single Azure SQL Database is database-scoped and does not include SQL Server Agent or cross-database instance queries; those require SQL Managed Instance or SQL Server on Azure VMs.

### Question 47 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Azure SQL Managed Instance delivers near-100% instance-scoped SQL Server compatibility (including SQL Agent and cross-DB queries) as managed PaaS. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **B:** Incorrect. Single Azure SQL Database is database-scoped and does not include SQL Server Agent or cross-database instance queries; those require SQL Managed Instance or SQL Server on Azure VMs.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Correct. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.

### Question 48 — `C` (Identify considerations for relational data on Azure)

Correct answer: C (is correct). SQL Server on Azure Virtual Machines (IaaS) grants full control over the guest OS, exact SQL Server version, and host-level agents. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **B:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.
- **C:** Correct. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **D:** Incorrect. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.

### Question 49 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Microsoft Entra ID centralizes cloud identity, MFA, conditional access, and passwordless managed-identity authentication for Azure SQL. [Skill 2.5: Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | Source: Explore relational database services in Azure — Describe Azure SQL services and capabilities (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql)]

- **A:** Correct. Microsoft Entra ID (formerly Azure AD) centralizes identity governance, conditional access, MFA, and passwordless managed-identity connections to Azure data services.
- **B:** Incorrect. Microsoft retired Data Migration Assistant (DMA) in July 2025; Azure Migrate and the Azure SQL Migration extension handle SQL discovery, assessment, and right-sizing.
- **C:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 50 — `D` (Identify considerations for relational data on Azure)

Correct answer: D (is correct). Azure Database for PostgreSQL — Flexible Server is Microsoft's managed PaaS offering supporting `PL/pgSQL`, spatial/custom extensions, and `pgAdmin`. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.
- **C:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **D:** Correct. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.

### Question 51 — `A` (Identify considerations for relational data on Azure)

Correct answer: A (is correct). Azure Database for MySQL — Flexible Server provides managed MySQL Community Edition PaaS with built-in HA and up to 35-day PITR for LAMP apps. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Correct. Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.
- **B:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **C:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **D:** Incorrect. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.

### Question 52 — `B` (Identify considerations for relational data on Azure)

Correct answer: B (is correct). Azure Database for PostgreSQL — Flexible Server stores Query Store performance telemetry inside its `azure_sys` database. [Skill 2.6: Identify Azure database services for open-source database systems | Source: Explore relational database services in Azure — Describe Azure services for open-source databases (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source)]

- **A:** Incorrect. Single Azure SQL Database is database-scoped and does not include SQL Server Agent or cross-database instance queries; those require SQL Managed Instance or SQL Server on Azure VMs.
- **B:** Correct. Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 53 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Lifecycle policies age blobs from online Hot (active) -> Cool (>=30d) -> Cold (>=90d) -> offline Archive (>=180d, rehydrated only on audit demand). [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Table storage entities hold small key-value properties rather than large video files, and Cool/Cold tiers remain online with immediate millisecond read access.
- **B:** Incorrect. Archive tier is offline and cannot serve direct reads until rehydrated to Hot or Cool, which takes hours.
- **C:** Correct. Lifecycle management policies automatically age blobs from lowest-read-cost Hot through Cool and Cold down to lowest-storage-cost offline Archive.
- **D:** Incorrect. Blob tiers are object storage rather than SMB shares, Archive rather than Hot minimizes 1-year retention storage cost, and Hot blobs require no rehydration.

### Question 54 — `A, B` (Describe considerations for working with non-relational data on Azure)

Correct answers: A and B (are correct). ADLS Gen2 adds a hierarchical namespace to Azure Blob Storage, and Microsoft OneLake is Fabric's unified tenant-wide SaaS data lake. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Correct. OneLake is Microsoft Fabric’s unified ADLS Gen2-compatible logical data lake that stores Delta Parquet data once and shares it via zero-copy Shortcuts across workloads.
- **B:** Correct. ADLS Gen2 adds a true POSIX-ACL directory hierarchy and atomic folder rename/delete operations atop Azure Blob Storage for big-data analytics engines.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **E:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.

### Question 55 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Append blobs optimize block append operations strictly at the end of a blob for logging scenarios. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Incorrect. Archive tier blobs are stored offline and cannot be read directly until rehydrated to Hot or Cool, which takes hours.
- **C:** Correct. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **D:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.

### Question 56 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Page blobs provide random-access 512-byte pages up to 8 TiB and back Azure VM OS and data disks. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Correct. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **C:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.
- **D:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.

### Question 57 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). The offline Archive tier delivers the lowest storage cost for data retained >=180 days when multi-hour rehydration latency is acceptable. [Skill 3.1: Describe features of Azure Blob storage | Source: Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)]

- **A:** Correct. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **B:** Incorrect. Archive tier blobs are stored offline and cannot be read directly until rehydrated to Hot or Cool, which takes hours.
- **C:** Incorrect. The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.
- **D:** Incorrect. The Hot tier is online storage optimized for data that is accessed or modified frequently, carrying the lowest transaction/read cost.

### Question 58 — `B, D` (Describe considerations for working with non-relational data on Azure)

Correct answers: B and D (are correct). Azure Files provides managed SMB/NFS cloud shares, and Azure File Sync caches hot files on local Windows Servers while cloud-tiering cold files. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **B:** Correct. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **E:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.

### Question 59 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Azure Files exposes fully managed SMB 3.0 network file shares mountable via UNC paths (`\\...`) across VMs and on-premises hosts. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Correct. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **D:** Incorrect. Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.

### Question 60 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Azure File Sync replicates and caches Azure Files shares onto local Windows Servers with optional cloud tiering. [Skill 3.2: Describe features of Azure Files | Source: Explore Azure Storage for nonrelational data — Explore Azure Files (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)]

- **A:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Correct. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **D:** Incorrect. SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.

### Question 61 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Azure Table storage is a low-cost schemaless key-value store where every entity is uniquely indexed by `PartitionKey` + `RowKey`. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. Azure Table storage is a schemaless key-value store indexed only by `PartitionKey` and `RowKey` with no foreign keys or server-side table joins.
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Correct. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.

### Question 62 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Azure Table storage stores denormalized key-value entities indexed only on `PartitionKey` and `RowKey` with no joins or foreign keys. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **B:** Incorrect. Azure Table storage is a schemaless key-value store indexed only by `PartitionKey` and `RowKey` with no foreign keys or server-side table joins.
- **C:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.
- **D:** Correct. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 63 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Cosmos DB for Table preserves the `PartitionKey`/`RowKey` Table SDK model while adding global distribution, secondary indexing, and millisecond SLAs. [Skill 3.3: Describe features of Azure Table storage | Source: Explore Azure Storage for nonrelational data — Explore Azure Tables (https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Correct. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **C:** Incorrect. DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 64 — `A, B` (Describe considerations for working with non-relational data on Azure)

Correct answers: A and B (are correct). Cosmos DB provides turnkey global distribution with multi-region writes/<10 ms SLAs and bills operations in Request Units (RUs). [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Correct. Azure Cosmos DB replicates data transparently across selected Azure regions with financially backed 99.999% availability and single-digit millisecond read/write latency.
- **B:** Correct. Cosmos DB measures CPU, memory, and IOPS per database operation in Request Units (RUs), billed via Provisioned/Autoscale RU/s or consumption-based Serverless.
- **C:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **D:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **E:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.

### Question 65 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Session consistency is Cosmos DB's default level and guarantees monotonic read-your-own-writes within each client session at low RU cost. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **B:** Correct. Session consistency is Cosmos DB’s default level, balancing low latency and throughput while guaranteeing each user session immediately sees its own writes in order.
- **C:** Incorrect. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.
- **D:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.

### Question 66 — `C` (Describe considerations for working with non-relational data on Azure)

Correct answer: C (is correct). Strong consistency guarantees linearizable reads of the most recent committed write across readers. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Incorrect. Session consistency is Cosmos DB’s default level, balancing low latency and throughput while guaranteeing each user session immediately sees its own writes in order.
- **B:** Incorrect. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.
- **C:** Correct. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **D:** Incorrect. The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.

### Question 67 — `A` (Describe considerations for working with non-relational data on Azure)

Correct answer: A (is correct). Eventual consistency offers the lowest latency and RU consumption when replicas may converge asynchronously without ordering guarantees. [Skill 3.4: Identify use cases for Azure Cosmos DB | Source: Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db)]

- **A:** Correct. Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.
- **B:** Incorrect. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **C:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **D:** Incorrect. Isolation prevents concurrent in-flight transactions from reading uncommitted intermediate edits or overwriting each other unpredictably via locking or row versioning.

### Question 68 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). You select the API when creating the Cosmos DB account, define database + container with a high-cardinality partition key, set RU/s or serverless + consistency, and run partition-scoped queries. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB sits under an account -> database -> container -> item hierarchy, not SMB shares or subscription tags.
- **B:** Correct. API selection happens at account creation, partition key design happens at container creation to distribute storage/RU evenly, and partition-scoped queries avoid cross-partition fan-out.
- **C:** Incorrect. Cosmos DB is fully managed PaaS with no OS patching, a single-value partition key creates a 20 GB logical-partition bottleneck, and triggers/sprocs use JavaScript rather than T-SQL.
- **D:** Incorrect. Every Cosmos DB container requires a partition key, the API is fixed per account, Cosmos DB does not enforce cross-container foreign keys, and item size is capped at 2 MB.

### Question 69 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Azure Cosmos DB for NoSQL is the native JSON document API queried using familiar SQL `SELECT` syntax. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **B:** Incorrect. Cosmos DB for MongoDB lets existing MongoDB drivers and tools store BSON documents in Cosmos DB simply by updating the connection string.
- **C:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **D:** Correct. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.

### Question 70 — `D` (Describe considerations for working with non-relational data on Azure)

Correct answer: D (is correct). Azure Cosmos DB for MongoDB provides wire-protocol compatibility so existing MongoDB BSON apps connect via connection-string update. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.
- **B:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.
- **C:** Incorrect. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **D:** Correct. Cosmos DB for MongoDB lets existing MongoDB drivers and tools store BSON documents in Cosmos DB simply by updating the connection string.

### Question 71 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Azure Cosmos DB for Apache Gremlin stores property-graph vertices and edges queried via Gremlin graph traversals. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.
- **B:** Correct. Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Incorrect. Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.

### Question 72 — `B` (Describe considerations for working with non-relational data on Azure)

Correct answer: B (is correct). Because a Cosmos DB account's API is fixed at creation, CQL wide-column apps require provisioning an Azure Cosmos DB for Apache Cassandra account. [Skill 3.5: Describe Azure Cosmos DB APIs | Source: Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs (https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis)]

- **A:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **B:** Correct. Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.
- **C:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **D:** Incorrect. The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.

### Question 73 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). ELT lands raw extracts into OneLake Bronze first, cleanses/conforms Delta tables in Silver via Spark/SQL, and publishes Gold star schemas for BI. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Incorrect. Skipping cleansing degrades report accuracy, deleting raw Bronze files prevents replayability, and Gold analytical layers favor denormalized star schemas over 3NF.
- **B:** Incorrect. ELT executes transformations in scalable cloud engines rather than client laptops, and Archive blobs/Queues cannot back live BI queries.
- **C:** Correct. Modern ELT lands raw data in scalable lake storage first, then leverages cloud compute to cleanse Silver tables and publish Gold star schemas for analytics.
- **D:** Incorrect. Analytical ingestion is read-only against operational sources and builds Bronze -> Silver -> Gold sequentially.

### Question 74 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Loading raw data into target cloud lake/warehouse storage first and transforming in place with scalable cloud compute defines ELT. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Correct. ELT extracts raw source data, loads it directly into scalable lake/warehouse storage, and runs distributed cloud compute (Spark or SQL) to cleanse and model in place.
- **B:** Incorrect. ETL transforms, scrubs, or redacts sensitive fields in an intermediate processing engine prior to loading only the conformed structure into the target analytical store.
- **C:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **D:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.

### Question 75 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Azure Data Factory (and Data Factory in Microsoft Fabric) provides connector-rich Copy pipelines and visual Dataflows Gen2 orchestration. [Skill 4.1: Describe considerations for data ingestion and processing | Source: Explore fundamentals of large-scale analytics — Explore data ingestion pipelines (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)]

- **A:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **B:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **C:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **D:** Correct. Data Factory orchestrates code-free data movement (90+ connectors via Copy activity) and visual Power Query transformations (Dataflows Gen2) or Spark/Mapping Data Flows.

### Question 76 — `B, C` (Describe an analytics workload on Azure)

Correct answers: B and C (are correct). A data lakehouse layers Delta Lake ACID/SQL capabilities onto open Parquet lake storage, and a star schema models fact and dimension tables for BI. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.
- **B:** Correct. A lakehouse combines the low-cost open file flexibility of a data lake with ACID transactions, schema enforcement, and SQL warehouse performance via Delta Lake tables.
- **C:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.
- **D:** Incorrect. OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.
- **E:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.

### Question 77 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). When a star schema's dimension tables are normalized into multi-table hierarchies, the resulting design is a snowflake schema. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Correct. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **D:** Incorrect. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.

### Question 78 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). A data lakehouse unifies data lake file openness with data warehouse ACID transactions and SQL query performance via Delta Lake. [Skill 4.2: Describe options for analytical data stores | Source: Explore fundamentals of large-scale analytics — Explore analytical data stores (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **C:** Incorrect. 1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).
- **D:** Correct. A lakehouse combines the low-cost open file flexibility of a data lake with ACID transactions, schema enforcement, and SQL warehouse performance via Delta Lake tables.

### Question 79 — `D, E, F` (Describe an analytics workload on Azure)

Correct answers: D, E, and F (are correct). Microsoft Fabric (unified OneLake SaaS), Azure Databricks (collaborative Spark/Delta), and Azure Synapse Analytics (SQL + Spark pools) are Microsoft's flagship large-scale analytics platforms. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **B:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **C:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **D:** Correct. Azure Synapse Analytics integrates serverless SQL on-demand lake querying, dedicated MPP SQL warehousing, Apache Spark pools, and Synapse Pipelines in Synapse Studio.
- **E:** Correct. Microsoft Fabric unifies Data Factory, Data Engineering, Data Warehouse, Data Science, Real-Time Intelligence, and Power BI in one SaaS workspace sharing OneLake Delta tables.
- **F:** Correct. Azure Databricks provides managed Apache Spark clusters, collaborative Python/SQL/Scala/R notebooks, Unity Catalog governance, and Delta Lake processing on Azure.

### Question 80 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Microsoft Fabric unifies ingestion, lakehouse/warehouse engineering, real-time analytics, and Power BI in one SaaS experience over OneLake. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Correct. Microsoft Fabric unifies Data Factory, Data Engineering, Data Warehouse, Data Science, Real-Time Intelligence, and Power BI in one SaaS workspace sharing OneLake Delta tables.
- **C:** Incorrect. SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.
- **D:** Incorrect. Azure HDInsight provisions managed clusters of open-source Apache big-data frameworks when lift-and-shift Hadoop/Hive/HBase/Kafka compatibility is required.

### Question 81 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Azure Databricks provides managed collaborative Apache Spark clusters, multi-language notebooks, Delta Lake optimization, and ML workflows. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **B:** Incorrect. Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Correct. Azure Databricks provides managed Apache Spark clusters, collaborative Python/SQL/Scala/R notebooks, Unity Catalog governance, and Delta Lake processing on Azure.

### Question 82 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). Azure HDInsight provisions managed cloud clusters for open-source Hadoop, Hive, HBase, Kafka, and Spark workloads. [Skill 4.3: Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | Source: Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric (https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)]

- **A:** Incorrect. The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.
- **B:** Correct. Azure HDInsight provisions managed clusters of open-source Apache big-data frameworks when lift-and-shift Hadoop/Hive/HBase/Kafka compatibility is required.
- **C:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **D:** Incorrect. Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.

### Question 83 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Batch processing executes scheduled jobs over bounded sets of accumulated historical records. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
- **B:** Incorrect. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.
- **C:** Incorrect. Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.
- **D:** Correct. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.

### Question 84 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Stream processing analyzes continuous unbounded events in real time with sub-second or millisecond latency. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Correct. Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.
- **B:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **C:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **D:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.

### Question 85 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). A tumbling window slices time into fixed-size, contiguous, non-overlapping intervals with each event counted once. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **B:** Correct. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **C:** Incorrect. A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.
- **D:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).

### Question 86 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). A hopping window jumps forward by a hop interval shorter than the window duration, producing scheduled overlapping windows. [Skill 4.4: Describe the difference between batch and streaming data | Source: Explore fundamentals of real-time analytics — Understand batch and stream processing (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream)]

- **A:** Correct. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **B:** Incorrect. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).
- **C:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.
- **D:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.

### Question 87 — `A, C` (Describe an analytics workload on Azure)

Correct answers: A and C (are correct). Azure Event Hubs ingests millions of partitioned events per second, and Azure Stream Analytics processes them via serverless SQL window queries. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Correct. Azure Event Hubs ingests millions of telemetry events per second into partitioned append logs (supporting native AMQP/HTTPS and Apache Kafka producers) for downstream stream consumers.
- **B:** Incorrect. The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.
- **C:** Correct. Azure Stream Analytics runs declarative Stream Analytics Query Language (`SELECT ... GROUP BY TumblingWindow(...)`) jobs joining live streams with reference data into sinks.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **E:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.

### Question 88 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Microsoft Fabric Real-Time Intelligence combines Eventstream, Eventhouse (KQL databases), Real-Time Dashboards, and Activator. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Correct. Fabric Real-Time Intelligence ingests and routes events via Eventstream, indexes high-volume telemetry in Eventhouse KQL databases, visualizes live tiles, and triggers Activator alerts.
- **B:** Incorrect. Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.
- **C:** Incorrect. The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.
- **D:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.

### Question 89 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Apache Spark Structured Streaming processes continuous streams as unbounded tables using Spark SQL/DataFrame APIs and checkpoints. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Correct. Spark Structured Streaming treats a live event stream as an unbounded table processed via familiar Spark SQL/DataFrame APIs with checkpointed exactly-once guarantees.
- **B:** Incorrect. A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.
- **C:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **D:** Incorrect. Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.

### Question 90 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). A session window dynamically groups events arriving within a timeout gap and closes once inactivity exceeds that threshold. [Skill 4.5: Identify Microsoft cloud services for real-time analytics | Source: Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming (https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence)]

- **A:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **B:** Incorrect. Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.
- **C:** Incorrect. A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.
- **D:** Correct. A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).

### Question 91 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Analysts shape/model and build reports in Power BI Desktop, publish to a Power BI Service workspace, pin dashboard tiles and schedule refresh in the Service, and share a Power BI App. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Incorrect. Dashboards exist only in Power BI Service (not Power BI Desktop), Power BI Mobile is for consumption, and viewers consume shared Apps/reports in browser or mobile.
- **B:** Incorrect. Dashboards are created in Power BI Service rather than Power BI Mobile, and dataset refresh plus secure sharing are managed in Power BI Service workspaces.
- **C:** Correct. Power BI Desktop handles Power Query prep, semantic modeling, and report design, while Power BI Service hosts scheduled refresh, multi-report dashboards, and governed App distribution.
- **D:** Incorrect. Paginated `.rdl` reports are authored in Power BI Report Builder, Stream Analytics processes event streams, and port `1433` is SQL Server TDS rather than BI sharing.

### Question 92 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Dashboards composed of pinned tiles from one or more reports are an exclusive cloud capability of the Power BI Service, not Power BI Desktop. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Correct. Power BI Service (`app.powerbi.com` / Fabric) hosts published semantic models and reports, pins cross-report dashboard tiles, schedules gateway refreshes, and distributes governed Apps.
- **B:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **C:** Incorrect. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **D:** Incorrect. Dashboards with pinned tiles across multiple reports are a cloud-only feature of Power BI Service, not Power BI Desktop.

### Question 93 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). Power BI Report Builder authors fixed-layout paginated (`.rdl`) reports built for multi-page printing and complete table listings. [Skill 4.6: Identify the capabilities of Power BI | Source: Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities (https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)]

- **A:** Correct. Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.
- **B:** Incorrect. Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.
- **C:** Incorrect. Power BI Service (`app.powerbi.com` / Fabric) hosts published semantic models and reports, pins cross-report dashboard tiles, schedules gateway refreshes, and distributes governed Apps.
- **D:** Incorrect. Azure Stream Analytics runs declarative Stream Analytics Query Language (`SELECT ... GROUP BY TumblingWindow(...)`) jobs joining live streams with reference data into sinks.

### Question 94 — `D, E` (Describe an analytics workload on Azure)

Correct answers: D and E (are correct). A Power BI semantic model defines relationships and field visibility, while a DAX measure evaluates dynamically within the active report filter context. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.
- **B:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **C:** Incorrect. DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.
- **D:** Correct. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **E:** Correct. A Power BI semantic model defines `1:*` star-schema relationships, reusable DAX measures, drill-down hierarchies, and column metadata consumed across reports.

### Question 95 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). A DAX measure computes aggregations dynamically at query time according to report slicers and visual filter context. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Correct. Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.
- **B:** Incorrect. CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.
- **C:** Incorrect. The Hot tier is online storage optimized for data that is accessed or modified frequently, carrying the lowest transaction/read cost.
- **D:** Incorrect. A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.

### Question 96 — `C` (Describe an analytics workload on Azure)

Correct answer: C (is correct). Hierarchies, `1:*` star-schema relationships, and storage modes (Import, DirectQuery, Direct Lake) are configured in the Power BI semantic model. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **B:** Incorrect. A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.
- **C:** Correct. A Power BI semantic model defines `1:*` star-schema relationships, reusable DAX measures, drill-down hierarchies, and column metadata consumed across reports.
- **D:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).

### Question 97 — `D` (Describe an analytics workload on Azure)

Correct answer: D (is correct). Power BI semantic models perform and read best when structured as a star schema of dimension and fact tables. [Skill 4.7: Describe features of data models in Power BI | Source: Design semantic models and star schemas in Power BI (https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)]

- **A:** Incorrect. Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.
- **B:** Incorrect. A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.
- **C:** Incorrect. 3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.
- **D:** Correct. A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.

### Question 98 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). A line chart best displays continuous trends and directional changes over ordered time intervals. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Correct. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.
- **B:** Incorrect. Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).
- **C:** Incorrect. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.
- **D:** Incorrect. Pie/donut charts show part-to-whole shares for a few slices, while treemaps use nested rectangles to display proportional composition across larger hierarchical categories.

### Question 99 — `A` (Describe an analytics workload on Azure)

Correct answer: A (is correct). A bar or column chart uses aligned bar lengths to compare discrete category totals clearly and accurately. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Correct. Bar and column charts use aligned bar lengths to compare magnitudes accurately across discrete categories such as product lines or regions.
- **B:** Incorrect. Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.
- **C:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
- **D:** Incorrect. Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.

### Question 100 — `B` (Describe an analytics workload on Azure)

Correct answer: B (is correct). A KPI visual pairs a headline indicator metric with a trend axis and progress/variance against a defined target goal. [Skill 4.8: Identify appropriate visualizations for data | Source: Visualization types in Power BI (https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)]

- **A:** Incorrect. A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.
- **B:** Correct. A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.
- **C:** Incorrect. Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.
- **D:** Incorrect. Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.
