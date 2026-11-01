# Microsoft Exam DP-300: Administering Microsoft Azure SQL Solutions — Full-Length Mock Exam 1

Exam DP-300 (Omnichannel E-Commerce, Hyperscale Read-Scale, and Hybrid Azure Arc Retail) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint & Credential Notice:** Aligned to the official **October 27, 2026** DP-300 study guide (`Microsoft Certified: Azure Database Administrator Associate`). Associate-level certification with **no prerequisite exam required**, free online annual renewal on Microsoft Learn, split-screen `learn.microsoft.com` access during non-lab exam sections, and hands-on coverage across **T-SQL**, **Azure PowerShell**, **Azure CLI**, **Bicep**, and **KQL**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` T-SQL/PowerShell/CLI/Bicep/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Azure SQL case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area T-SQL/CLI dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn Azure SQL and SQL Server documentation — never recalled live items or copied Microsoft sample case studies.

## Questions

### 1. A retail ERP vendor requires SQL Server 2019 CU28 pinned to a specific build, a third-party Windows kernel COM+ tax module installed on the host OS, and co-hosted SSRS reports on the same machine. Which Azure SQL deployment option meets all three requirements?

Domain: Plan and implement data platform resources

- A. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- B. SQL Server on Azure Virtual Machines (`Ebdsv5` series) with full OS and engine version control
- C. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas
- D. Azure SQL Database vCore Elastic Pool with per-database min and max vCore limits

### 2. A checkout platform team runs ephemeral pull-request integration tests in GitHub Actions on Ubuntu runners and configures memory limits on RHEL 9 SQL hosts using `sudo /opt/mssql/bin/____ set memory.memorylimitmb 32768`. Which deployment approach fits this workflow?

Domain: Plan and implement data platform resources

- A. SQL Server on Linux configured via `mssql-conf` or Linux container images for consistent CI/CD dev-test parity
- B. SQL Server enabled by Azure Arc (`Microsoft.AzureArcData/sqlServerInstances`)
- C. Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica
- D. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas

### 3. You are automating network prerequisites before provisioning a new Azure SQL Managed Instance inside `vnet-retail-eastus`. Which two virtual network configurations are mandatory? Select two.

Domain: Plan and implement data platform resources

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Authenticate applications and users exclusively with Microsoft Entra ID identities, service principals, or workspace roles
- C. Associate a User-Defined Route (`UDR`) table (`0.0.0.0/0` -> `Internet` for management plane) and required NSG rules with the SQL MI subnet
- D. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- E. Create a dedicated VNet subnet (`/28` or larger) with no other cloud resources and delegate it to `Microsoft.Sql/managedInstances`

### 4. A merchandising squad provisions a new `SQL database` item inside a Microsoft Fabric workspace for a promotional catalog app. Which two platform behaviors apply automatically? Select two.

Domain: Plan and implement data platform resources

- A. Configure SQL Server password logins (`CREATE LOGIN ... WITH PASSWORD`) and T-SQL `BACKUP DATABASE ... TO DISK` inside SQL database in Microsoft Fabric
- B. Authenticate applications and users exclusively with Microsoft Entra ID identities, service principals, or workspace roles
- C. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- D. Query automatically replicated OneLake Delta Parquet tables and the read-only SQL analytics endpoint from Spark and Direct Lake
- E. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 5. An e-commerce `OrderEvents` table holds 24 monthly partitions on `EventDateUTC`. At midnight on the first of each month, you must open a new future partition and archive the oldest month with zero blocking `DELETE` locks. Which four-step sequence should you execute?

Domain: Plan and implement data platform resources

- A. ALTER TABLE ... SWITCH oldest partition directly to Azure Blob Storage → SPLIT partition function → Rebuild entire table offline → MERGE all boundaries
- B. SPLIT partition function for incoming future boundary → Create empty staging table on same filegroup with matching schema/indexes → ALTER TABLE ... SWITCH oldest partition to staging → Archive staging data & MERGE retired boundary
- C. Create staging table without matching CHECK constraints → SWITCH partition across two separate Azure SQL Databases → MERGE future boundary → Truncate production table
- D. MERGE oldest partition boundary first → Run row-by-row DELETE on 80M rows → Create unindexed staging table on a different filegroup → SPLIT partition function

### 6. A global marketplace splits 60 million loyalty accounts across 24 independent Azure SQL Databases keyed by discrete `CountryCode` values, requiring `.NET` checkout APIs to route connections via `OpenConnectionForKey("JP")` in `____`. Which architecture should you implement?

Domain: Plan and implement data platform resources

- A. Horizontal sharding using the Elastic Database Client Library (`ShardMapManager` with `ListShardMap` or `RangeShardMap`)
- B. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- C. Table partitioning using `CREATE PARTITION FUNCTION ... AS RANGE RIGHT` with aligned indexes and `ALTER TABLE ... SWITCH`
- D. Evaluate `sp_estimate_data_compression_savings` and apply `ROW`, `PAGE`, or `COLUMNSTORE_ARCHIVE` compression per partition

### 7. You deploy eight Windows Server 2022 VMs running SQL Server 2022 from a custom golden image and must enable Azure Hybrid Benefit license switching and Sunday 02:00 maintenance patching via `Set-AzVMSqlServerExtension` (`____` mode). What should you configure?

Domain: Plan and implement data platform resources

- A. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- B. SQL IaaS Agent Extension in Full management mode paired with Azure Update Manager / Automated Patching
- C. Azure SQL Database vCore Elastic Pool with per-database min and max vCore limits
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 8. An inventory service hosts 210 databases on a single Azure SQL Managed Instance and needs 45,000 IOPS without over-allocating 16 TB of unused disk capacity or paying for Business Critical vCores. Which offering meets this requirement?

Domain: Plan and implement data platform resources

- A. Azure SQL Managed Instance (Next-gen General Purpose) with decoupled IOPS and storage sliders
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- D. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica

### 9. You are configuring storage on an `E32bds_v5` Azure VM hosting a 4 TB retail ERP database (`OrderData.mdf`, `OrderLog.ldf`, and `tempdb`). Which disk caching and placement layout follows Microsoft best practices?

Domain: Plan and implement data platform resources

- A. No — transaction log managed disks on SQL Server Azure VMs must use host caching `None`, never `ReadOnly` or `ReadWrite`
- B. Premium SSD v2 / striped Premium SSD with `ReadOnly` host caching for data disks, `None` for log disks, and `tempdb` on local NVMe
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching

### 10. A DBA experiences `WRITELOG` latency on a SQL Server Azure VM. Proposed solution: Change the Azure managed disk hosting `Checkout.ldf` to `ReadWrite` host caching (`--caching ____`). Does the solution meet the goal?

Domain: Plan and implement data platform resources

- A. No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases
- B. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- C. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- D. No — transaction log managed disks on SQL Server Azure VMs must use host caching `None`, never `ReadOnly` or `ReadWrite`

### 11. You need to migrate a 900 GB on-premises SQL Server 2022 order fulfillment database to Azure SQL Managed Instance with under three minutes of cutover downtime using Managed Instance link. Which four-step sequence should you follow?

Domain: Plan and implement data platform resources

- A. Export live `.bacpac` via SqlPackage without database copy → Establish VNet peering on UDP 1434 → Restore `.bacpac` onto SQL MI → Enable Availability Groups on SQL Server
- B. Take SQL Server offline immediately → Copy raw `.mdf`/`.ldf` files to Azure Files SMB → Attach `.mdf` files directly on SQL Managed Instance → Start distributed AG seeding
- C. Create Managed Instance link & seed distributed AG → Enable Availability Groups & master key on SQL Server → Execute planned cutover to SQL MI → Establish VNet/IPsec network peering on TCP 5022
- D. Enable Availability Groups & master key on SQL Server → Establish VNet/IPsec network peering on TCP 5022 → Create Managed Instance link & seed distributed AG → Validate sync state and execute planned cutover to SQL MI

### 12. You initiate an online Database Move of `CatalogDB` between two Azure SQL Managed Instances in peered VNets. Seeding finishes and the portal status shows `Ready for completion`. Which operational rule governs completing this move?

Domain: Plan and implement data platform resources

- A. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- B. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- C. Log Replay Service (`LRS`) streaming Full, Differential, and Tail-Log backups from Azure Blob Storage into SQL Managed Instance
- D. Online Azure SQL Managed Instance Database Move / Copy (`TCP 5022` & `11000–11999`, 24-hour manual completion window)

### 13. Your retail security policy mandates disabling `sa` and all SQL password logins on logical server `sql-kestrel-prod` via `az sql server ad-only-auth ____`. Which configuration enforces this requirement?

Domain: Implement a secure environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- D. Enable Microsoft Entra-only authentication (`azuread_authentication_only`) on the logical SQL server or SQL Managed Instance

### 14. A Node.js checkout API runs on Azure App Service with a System-Assigned Managed Identity `app-checkout-mi` and connects passwordlessly to Azure SQL Database. Which T-SQL statement grants database access: `CREATE USER [app-checkout-mi] FROM ____;`?

Domain: Implement a secure environment

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or `Entra Kerberos`)
- C. Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`)
- D. Remap orphaned database users (`ALTER USER [u] WITH LOGIN = [u]`) and inspect explicit `DENY` permissions via `sys.database_permissions`

### 15. Legacy warehouse desktop thick clients require integrated Windows Kerberos authentication against Azure SQL Managed Instance, and IT refuses to deploy customer-managed AD Domain Controllers in Azure. Which authentication architecture should you configure?

Domain: Implement a secure environment

- A. Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or `Entra Kerberos`)
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database

### 16. You manage a Failover Group spanning East US and West US 2. Which principal type ensures newly hired analysts in Entra group `SG-Retail-Analysts` can sign in immediately after regional failover without syncing SIDs in `master`?

Domain: Implement a secure environment

- A. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- B. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- C. Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`)
- D. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 17. A junior operations engineer needs to query `sys.dm_exec_requests` and `sys.dm_os_wait_stats` across every database on an Azure SQL logical server without reading any customer rows. Which server-level role should you assign: `ALTER SERVER ROLE ____ ADD MEMBER [ops_eng];`?

Domain: Implement a secure environment

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- C. Built-in granular server-level roles (`##MS_ServerStateReader##`, `##MS_DefinitionReader##`) or `GRANT VIEW DATABASE PERFORMANCE STATE`
- D. Row-Level Security (`CREATE SECURITY POLICY`) binding a `SCHEMABINDING` inline TVF as both `FILTER PREDICATE` and `BLOCK PREDICATE`

### 18. Returns clerks must execute `Sales.usp_IssueRefund` to insert rows into `Sales.RefundLedger`, yet clerks must never run ad-hoc `INSERT` or `SELECT` statements directly against `Sales.RefundLedger`. Which permission design follows least privilege?

Domain: Implement a secure environment

- A. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Stored procedure encapsulation using schema ownership chaining, `EXECUTE AS OWNER`, or certificate module signing

### 19. Analysts with ad-hoc `SELECT` access on `Customers` must be prevented from deducing executive salaries via `WHERE Salary > 250000`. Proposed solution: Apply `ALTER TABLE Customers ALTER COLUMN Salary ADD MASKED WITH (FUNCTION = 'default()')` only. Does the solution meet the goal?

Domain: Implement a secure environment

- A. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- B. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- C. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- D. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server

### 20. After restoring `PromoDB.bak` onto a new SQL Server 2022 VM, SQL user `promo_svc` fails login mapping, and user `auditor1` in `db_datareader` receives Msg 229 `SELECT permission was denied` on `Sales.Payouts`. How should you resolve both issues?

Domain: Implement a secure environment

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Enable Microsoft Entra-only authentication (`azuread_authentication_only`) on the logical SQL server or SQL Managed Instance
- C. Remap orphaned database users (`ALTER USER [u] WITH LOGIN = [u]`) and inspect explicit `DENY` permissions via `sys.database_permissions`
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 21. Compliance requires configuring Customer-Managed Key (`CMK`) Transparent Data Encryption on `sql-kestrel-prod` using Azure Key Vault. Which four-step sequence must you follow?

Domain: Implement a secure environment

- A. Enable Soft Delete & Purge Protection on Key Vault → Assign Managed Identity to SQL server → Grant Key Vault Crypto Service Encryption User (`get`/`wrapKey`/`unwrapKey`) → Set server TDE protector to Key Vault key
- B. Create symmetric key inside tempdb → Grant db_datareader in Key Vault → Set database compatibility level to 100 → Restart Azure SQL Database service
- C. Set server TDE protector to Key Vault key → Disable Soft Delete and Purge Protection on Key Vault → Assign Managed Identity after encryption starts → Export DEK plaintext to Blob storage
- D. Upload plaintext `.pfx` directly to Azure Table storage → Grant anonymous public read on container → Point TDE protector to Table URL → Disable TLS 1.2

### 22. You are troubleshooting why `Set-AzSqlServerTransparentDataEncryptionProtector` rejects an Azure Key Vault key URI for TDE. Which two Key Vault configurations must be verified? Select two.

Domain: Implement a secure environment

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- D. Enable both `Soft Delete` and `Purge Protection` on the Azure Key Vault or Managed HSM storing the TDE protector key
- E. Grant the SQL server Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) on the Key Vault

### 23. An on-premises SQL Server app without Always Encrypted client drivers must encrypt `GiftCardPin` inside T-SQL using `OPEN SYMMETRIC KEY PinKey DECRYPTION BY CERTIFICATE PinCert; SELECT ____(Key_GUID('PinKey'), @pin)` while enforcing encrypted network transit. Which configuration applies?

Domain: Implement a secure environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Column-level encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey`) plus `Minimal TLS version = 1.2`
- C. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 24. A fulfillment partner connects from static IP `198.51.100.24` to `OrdersDB`, which replicates to a DR server in another region. Proposed solution: Run `EXEC sp_set_firewall_rule` in `master` on the primary server only and expect the rule to fail over automatically. Does the solution meet the goal?

Domain: Implement a secure environment

- A. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- B. No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases
- C. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- D. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server

### 25. You need to perform in-place encryption and enable `ORDER BY` range queries on a `BirthDate` column in Azure SQL Database using Always Encrypted with VBS enclaves. Which two steps are required? Select two.

Domain: Implement a secure environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Enable `Column Encryption Setting=Enabled` and pass the `Enclave Attestation Url` (or VBS zero-attestation setting) in client drivers
- C. Configure `ReadOnly` Azure host caching on Premium SSD data disks hosting `.mdf` and `.ndf` database files
- D. Provision a Column Master Key in Key Vault and create a Column Encryption Key with `ENCLAVE_COMPUTATIONS` enabled
- E. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 26. After creating a Private Endpoint for `sql-velvetloom.database.windows.net`, an external host on the internet can still reach port 1433 and VNet pods still resolve the public IP. Which two remediation steps must you take? Select two.

Domain: Implement a secure environment

- A. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- B. Switch eligible hybrid SQL Server instances to hourly Azure Arc pay-as-you-go billing instead of upfront core licenses
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Link Private DNS Zone `privatelink.database.windows.net` (or forward on-premises DNS) to resolve `<server>.database.windows.net` to the private IP
- E. Set `Public network access = Disabled` (`publicNetworkAccess: Disabled`) on the logical SQL server so internet connections are rejected

### 27. PCI-DSS auditors require every query touching credit-card expiration columns to emit sensitivity labels inside Log Analytics audit records. You run `ADD ____ CLASSIFICATION TO Sales.Cards.ExpDate WITH (LABEL = 'Confidential', INFORMATION_TYPE = 'Credit Card')`. What completes this setup?

Domain: Implement a secure environment

- A. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- B. Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history
- C. SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 28. You enable server-level Azure SQL Auditing writing to an Azure Storage Account for seven-year archival without credential-expiry failures after storage key rotation. Which configuration best protects those audit logs?

Domain: Implement a secure environment

- A. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- B. SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history

### 29. A mobile catalog cache polls Azure SQL Database every two minutes needing only the primary keys of products inserted, updated, or deleted since `@last_sync_version` via `FROM ____(CHANGES Production.Products, @last_sync_version) AS CT` with minimal log overhead. Which feature should you enable?

Domain: Implement a secure environment

- A. Enable Change Data Capture (`CDC`) on DTU `Basic`/`S0–S2` databases or expect Change Tracking (`CT`) to retain every intermediate `UPDATE` value
- B. Azure SQL Ledger (`LEDGER = ON` append-only or updatable tables) storing SHA-256 database digests in Azure Confidential Ledger and verifying via `sp_verify_database_ledger`
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history

### 30. Call-center reps querying `Customers.Email` should see `aXXX@XXXX.com` while fraud supervisors in role `FraudLeads` see full email addresses without changing `SELECT Email FROM Customers`. Which T-SQL mask and permission achieve this: `MASKED WITH (FUNCTION = '____')` plus `GRANT UNMASK TO [FraudLeads]`?

Domain: Implement a secure environment

- A. Transparent Data Encryption (TDE) with a Customer-Managed Key (`CMK`) in Azure Key Vault (`Soft Delete` + `Purge Protection`)
- B. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- C. Row-Level Security (`CREATE SECURITY POLICY`) binding a `SCHEMABINDING` inline TVF as both `FILTER PREDICATE` and `BLOCK PREDICATE`
- D. Always Encrypted with VBS or Intel SGX secure enclaves (`ALLOW_ENCLAVE_COMPUTATIONS` + `Column Encryption Setting=Enabled`)

### 31. You are deploying Row-Level Security on `Support.Tickets` for a pooled Node.js middle tier that passes `CountryIso` per HTTP request. Which four-step implementation sequence follows Microsoft security best practices?

Domain: Implement a secure environment

- A. Apply `ADD MASKED WITH (FUNCTION = 'default()')` on `TenantId` → Create `AFTER INSERT` trigger → Grant `UNMASK` to shared app login → Expect row filtering
- B. Create dedicated `Security` schema → Create `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT(N'TenantId')` → Create `SECURITY POLICY` with `FILTER` & `BLOCK` predicates (`STATE = ON`) → Set read-only `sp_set_session_context` on connect
- C. Create `SECURITY POLICY` with `STATE = ON` first → Create multi-statement TVF without `SCHEMABINDING` → Grant tenants `ALTER ANY SECURITY POLICY` → Store `TenantId` in a global temp table
- D. Create non-schema-bound scalar UDF → Attach UDF to `sys.sp_set_firewall_rule` → Enable Change Tracking → Set `SESSION_CONTEXT` with `@read_only = 0` so users can switch tenants

### 32. Before Black Friday, you need 14 days of 15-second historical averages for CPU, data I/O, and transaction log write percentages on a single Azure SQL Database via `SELECT avg_cpu_percent, avg_log_write_percent FROM sys.____`. Which DMV provides this built-in baseline?

Domain: Monitor, configure, and optimize database resources

- A. Azure Monitor metrics paired with `sys.dm_db_resource_stats` (single DB) or `sys.server_resource_stats` (SQL MI) for 15-second CPU, data I/O, log write, and memory baselines
- B. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 33. During a flash sale, `avg_data_io_percent` hits 98% and top wait type `PAGEIOLATCH_SH` accounts for 74% of total wait time while `avg_cpu_percent` is 22%. What does `PAGEIOLATCH_SH` indicate?

Domain: Monitor, configure, and optimize database resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 34. You stream Azure SQL Database telemetry to Log Analytics and write a KQL query: `AzureDiagnostics | where Category == "____" | where TimeGenerated > ago(1h)` to inspect automated root-cause anomaly JSON payloads. Which Diagnostic Settings category must be enabled?

Domain: Monitor, configure, and optimize database resources

- A. Azure Monitor Diagnostic Settings streaming `SQLInsights`, `QueryStoreRuntimeStatistics`, `Errors`, and `Blocks` to a Log Analytics workspace (`KQL`)
- B. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server

### 35. Operations wants to deploy `database watcher` to collect centralized KQL performance telemetry across 25 retail Azure SQL Databases and two Elastic Pools. Which four-step setup sequence is required?

Domain: Monitor, configure, and optimize database resources

- A. Create database watcher targeting Azure Cosmos DB for Gremlin → Store metrics in Azure Table storage → Authenticate via anonymous public SAS → Query dashboards via Gremlin
- B. Provision Azure Data Explorer or Fabric Eventhouse store → Create database watcher with Managed Identity → Add SQL targets & grant `VIEW SERVER PERFORMANCE STATE` + ingest roles → Start watcher & open portal dashboards
- C. Install third-party kernel drivers inside Azure SQL Database PaaS OS → Configure SMB share on domain controller → Export `.trc` files via `sp_trace_create` → Query via MDX
- D. Start database watcher before selecting data store or SQL targets → Grant `sysadmin` via blank-password `sa` login → Store time-series telemetry in Azure Queue Storage → Enable SQL Profiler trace

### 36. You configure role-based access for an Azure SQL `database watcher` Managed Identity (noting Microsoft's planned transition to Database Hub in Fabric before April 30, 2027). Which two permissions must you grant? Select two.

Domain: Monitor, configure, and optimize database resources

- A. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- B. Grant the database watcher Managed Identity `VIEW SERVER PERFORMANCE STATE` (or `VIEW DATABASE PERFORMANCE STATE`) on SQL targets
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Grant the database watcher Managed Identity database `Admin` / ingest permissions on the Azure Data Explorer or Fabric Eventhouse store
- E. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script

### 37. You must capture persistent Extended Events `.xel` trace files for queries exceeding 5 seconds on a single Azure SQL Database so traces survive engine failovers. Which two actions are required? Select two.

Domain: Monitor, configure, and optimize database resources

- A. Define `CREATE EVENT SESSION ... ON DATABASE ADD TARGET package0.event_file(SET filename = N'https://...xel')` and start the session
- B. Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE` with `rwl` permissions) for the Azure Blob container
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Enable both `Soft Delete` and `Purge Protection` on the Azure Key Vault or Managed HSM storing the TDE protector key
- E. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7

### 38. How does T-SQL Extended Events DDL differ between a single Azure SQL Database and an Azure SQL Managed Instance when creating an event session: `CREATE EVENT SESSION [SlowRpc] ON ____`?

Domain: Monitor, configure, and optimize database resources

- A. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- B. Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`)
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Extended Events (`CREATE EVENT SESSION ... ON DATABASE` in SQL DB or `ON SERVER` in SQL MI/VMs) writing to an `event_file` target in Azure Blob Storage

### 39. After a promotional skew, `usp_GetCartItems` jumps from 4 ms to 1,900 ms. You cannot deploy code changes until next week. Which four-step Query Store workflow safely restores 4 ms latency?

Domain: Monitor, configure, and optimize database resources

- A. Restart SQL Server production instance during peak traffic → Rebuild every index with `ONLINE = OFF` → Enable `AUTO_CLOSE = ON` → Check Query Store
- B. Confirm Query Store is `READ_WRITE` with wait capture → Compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`) → Force prior plan via `sp_query_store_force_plan` → Monitor `force_failure_count` & latency
- C. Run `ALTER DATABASE ... SET QUERY_STORE CLEAR ALL` first → Inspect Regressed Queries history → Force new regressed plan ID → Set `OPERATION_MODE = OFF`
- D. Set Query Store `OPERATION_MODE = READ_ONLY` → Modify `sys.query_store_plan` system catalog via `UPDATE` → Run `DBCC FREEPROCCACHE` every minute → Disable statistics

### 40. Two checkout procedures (`usp_ReserveStock` and `usp_ApplyCoupon`) frequently fail with Error 1205 (`deadlock victim`). In `sys.event_log`, `____` events show one procedure locks `Inventory` then `Coupons` while the other locks `Coupons` then `Inventory`. How do you fix this permanently?

Domain: Monitor, configure, and optimize database resources

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- C. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- D. Capture `xml_deadlock_report` via Extended Events or `sys.event_log`, align table modification order across transactions, and add covering indexes

### 41. You need to identify the active lead blocker session holding uncommitted locks while 45 checkout sessions queue up. Which DMVs should you join on `session_id` and `blocking_session_id`?

Domain: Monitor, configure, and optimize database resources

- A. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- B. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- C. Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 42. A reporting batch fills `tempdb` on Azure SQL Database. Which DMV breaks down `user_object_reserved_page_count`, `internal_object_reserved_page_count`, and `version_store_reserved_page_count` per session via `SELECT * FROM sys.____`?

Domain: Monitor, configure, and optimize database resources

- A. Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 43. A high-frequency query `SELECT OrderId, TotalAmt FROM Orders WHERE YEAR(OrderDate) = 2026 AND CustomerPhone = N'5550199'` scans 90M rows because `CustomerPhone` is `VARCHAR(20)` and `OrderDate` is wrapped in `YEAR()`. How should you optimize it?

Domain: Monitor, configure, and optimize database resources

- A. Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions
- B. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- C. Replace set-based `JOIN` queries with nested `FAST_FORWARD` T-SQL cursors calling multi-statement table-valued functions per row under compat `100`
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 44. Ninety-eight percent of rows in `Shipments` have `IsArchived = 1`, while live picking queries filter `WHERE IsArchived = 0 AND WarehouseId = @wid`. Which space-efficient index structure accelerates live picking without indexing archived rows?

Domain: Monitor, configure, and optimize database resources

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions

### 45. An Actual Execution Plan displays a yellow exclamation warning triangle on a `Hash Match (Inner Join)` operator and shows Estimated Number of Rows = `1` versus Actual Number of Rows = `4,800,000`. What runtime penalty is occurring?

Domain: Monitor, configure, and optimize database resources

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`)
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 46. Which built-in Azure SQL capability continuously compares current database query execution wait times against a rolling 7-day baseline and emits automated root-cause diagnostics (`MaxDOP`, missing index, locking, memory pressure)?

Domain: Monitor, configure, and optimize database resources

- A. Transparent Data Encryption (TDE) with a Customer-Managed Key (`CMK`) in Azure Key Vault (`Soft Delete` + `Purge Protection`)
- B. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- C. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- D. Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`)

### 47. You are designing a low-impact weekly maintenance standard for a 3 TB 24x7 retail OLTP database. Which three practices minimize locking, compilation stalls, and I/O overhead? Select three.

Domain: Monitor, configure, and optimize database resources

- A. Run `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON, MAX_DURATION = 90 MINUTES)` for heavily fragmented (`>30%`) indexes
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Run `DBCC CHECKDB WITH PHYSICAL_ONLY` during off-peak windows or offload full `DBCC CHECKDB` onto a restored backup replica
- D. Enable `AUTO_UPDATE_STATISTICS_ASYNC = ON` and schedule targeted `UPDATE STATISTICS` jobs so user queries do not stall waiting on sampling
- E. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- F. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon

### 48. A 500 GB index has 48% fragmentation, and your nightly maintenance window is 60 minutes. Proposed solution: Run `ALTER INDEX PK_Orders ON Sales.Orders REBUILD WITH (ONLINE = ON, ____ = ON, MAX_DURATION = 60 MINUTES)` and run `ALTER INDEX ... RESUME` the next night. Does the solution meet the goal?

Domain: Monitor, configure, and optimize database resources

- A. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- B. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- C. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- D. No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases

### 49. A small e-commerce DBA team wants Azure SQL Database to automatically revert query plan regressions whenever CPU gain exceeds threshold and automatically remove unused duplicate nonclustered indexes (`DROP_INDEX = ON`). Which feature should they enable?

Domain: Monitor, configure, and optimize database resources

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`)
- C. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 50. Ad-hoc merchandisers run heavy `SELECT` queries on a single Azure SQL Database (`GP_Gen5_16`). Proposed solution: Run `CREATE RESOURCE POOL PoolAdHoc WITH (MAX_CPU_PERCENT = 20)` and `ALTER RESOURCE GOVERNOR RECONFIGURE` inside that single Azure SQL Database. Does the solution meet the goal?

Domain: Monitor, configure, and optimize database resources

- A. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- B. No — transaction log managed disks on SQL Server Azure VMs must use host caching `None`, never `ReadOnly` or `ReadWrite`
- C. No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases
- D. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement

### 51. On an Azure SQL Managed Instance hosting 40 databases, only `LegacyCatalogDB` suffers parallel `CXPACKET` waits and needs `MAXDOP = 2` via `ALTER DATABASE ____ CONFIGURATION SET MAXDOP = 2;` without changing the other 39 databases. What should you run?

Domain: Monitor, configure, and optimize database resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Use `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`, `OPTIMIZED_PLAN_FORCING`) per database
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 52. After upgrading `CheckoutDB` to compatibility level `160`, a parameterized search query serving both 2-row boutique brands and 15M-row flagship brands stops regressing without `OPTION (RECOMPILE)`. Which Intelligent Query Processing feature explains this improvement?

Domain: Monitor, configure, and optimize database resources

- A. Replace set-based `JOIN` queries with nested `FAST_FORWARD` T-SQL cursors calling multi-statement table-valued functions per row under compat `100`
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Enable compatibility level `160` Intelligent Query Processing (`Parameter Sensitive Plan` optimization, `Memory Grant Feedback` persistence, `Scalar UDF Inlining`, `DOP Feedback`)

### 53. On a SQL Server 2022 Azure VM, a non-`sysadmin` ETL developer owns a SQL Server Agent job with a PowerShell step that uploads CSV manifests. How do you grant only the required Windows account permissions to that job step?

Domain: Configure and manage automation of tasks

- A. SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- D. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 54. You must email `dba-oncall@kestrelcart.com` immediately whenever a fatal storage checksum Error `824` or Severity `20` error occurs on an Azure SQL Managed Instance. Which native automation components should you configure?

Domain: Configure and manage automation of tasks

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators

### 55. You are hardening SQL Server Agent governance on 10 retail SQL Server 2022 VMs so job owners never receive `sysadmin` and hardware/storage faults page on-call DBAs automatically. Which two configurations should you deploy? Select two.

Domain: Configure and manage automation of tasks

- A. Configure Database Mail, define an Agent Operator, and create SQL Server Agent Alerts for Severity `19–25` and Errors `823`, `824`, and `825`
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Create a Windows/SQL Credential and map it to a SQL Server Agent Subsystem Proxy (`CmdExec` / `PowerShell`) instead of granting `sysadmin`
- E. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 56. After migrating from SQL Server on-premises to Azure SQL Managed Instance, an old SQL Agent job step that calls an OS `CmdExec` batch script accessing `C:\Drops\parse.exe` fails. Why does this step fail on SQL Managed Instance?

Domain: Configure and manage automation of tasks

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries
- C. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- D. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 57. A nightly SQL Server Agent index job reports failed status, and you need step-level error messages and run durations via T-SQL: `SELECT message, run_status, run_duration FROM msdb.dbo.____ ORDER BY instance_id DESC`. Which system table do you query?

Domain: Configure and manage automation of tasks

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries
- C. Transparent Data Encryption (TDE) with a Customer-Managed Key (`CMK`) in Azure Key Vault (`Soft Delete` + `Purge Protection`)
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 58. You author a Bicep module deploying `Microsoft.Sql/servers` and must ensure `administratorLoginPassword` never appears in Git or ARM deployment logs by decorating the parameter with `@____()` and referencing Key Vault. Which decorator is required?

Domain: Configure and manage automation of tasks

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`
- C. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 59. Before merging a pull request that modifies production Elastic Pool Bicep templates, your CI workflow runs `az deployment group ____ --resource-group rg-sql-prod --template-file main.bicep` to verify no database resources will be recreated or deleted. Which subcommand runs this preview?

Domain: Configure and manage automation of tasks

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`

### 60. A DevOps script scales `OrdersDB` to `GP_Gen5_16` before flash sales using Azure PowerShell: `____ -ResourceGroupName "rg-kestrel" -ServerName "sql-kestrel" -DatabaseName "OrdersDB" -VCore 16`. Which cmdlet updates an existing database?

Domain: Configure and manage automation of tasks

- A. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- B. Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`)
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 61. You are scripting Linux bash automation with Azure CLI to provision a Zone Redundant Hyperscale database: `az sql db ____ -g rg-kestrel -s sql-kestrel -n CartDB --edition Hyperscale --capacity 8 --zone-redundant true`. Which CLI verb completes the command?

Domain: Configure and manage automation of tasks

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`)

### 62. An ARM template deploying an Azure SQL Managed Instance fails immediately with `SubnetNotValidForSqlManagedInstance`. Which subnet misconfiguration causes this deployment error?

Domain: Configure and manage automation of tasks

- A. Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules
- B. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 63. A Bicep deployment to `eastus2` fails with `SubscriptionIsOverQuotaForSku` and outputs a `CorrelationId` GUID. How do you retrieve nested inner error details via PowerShell and resolve the failure?

Domain: Configure and manage automation of tasks

- A. Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 64. You are building a new Azure SQL Elastic Job Agent from scratch to execute nightly partition management across 35 regional Azure SQL Databases using Managed Identity. Which four-step setup sequence is required?

Domain: Configure and manage automation of tasks

- A. Enable SQL Server Agent inside single Azure SQL Database → Create linked servers to 480 tenant DBs → Loop synchronously inside a scalar UDF → Grant `CONTROL SERVER` to `guest`
- B. Create Elastic Job Agent on Basic tier DB → Run `jobs.sp_add_job` before creating Target Group → Authenticate across servers with Windows NTLM local accounts → Schedule via `msdb.dbo.sp_add_job`
- C. Create S1+ Job Database & Elastic Job Agent with UAMI → Create contained UAMI user on target DBs with needed permissions → Define Target Group (`jobs.sp_add_target_group_member`) → Add T-SQL steps & schedule (`jobs.sp_add_job`)
- D. Provision Elastic Job Agent inside Azure Blob Storage → Store plaintext admin password in Git repo → Add Cosmos DB containers to Target Group → Trigger via `DBCC SHRINKDATABASE`

### 65. Every night at 23:00 UTC you want to scale an Elastic Pool down from 32 vCores to 8 vCores and scale it back up at 06:00 UTC without running any VM or storing credentials. Which Azure service and identity pattern fits best?

Domain: Configure and manage automation of tasks

- A. Azure Automation PowerShell / Python runbooks (or Azure Functions / Logic Apps) using a System-Assigned Managed Identity on a recurring schedule
- B. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 66. You need an event-driven low-code workflow that posts a formatted Adaptive Card to Microsoft Teams and opens a ServiceNow ticket whenever an Azure Monitor webhook fires for a blocked Azure SQL Database. Which service integrates natively as the Action Group target?

Domain: Configure and manage automation of tasks

- A. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Azure Automation PowerShell / Python runbooks (or Azure Functions / Logic Apps) using a System-Assigned Managed Identity on a recurring schedule
- D. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server

### 67. Three target databases failed during last night's Elastic Job run. Which catalog view inside the Elastic Job database shows per-target `lifecycle`, `last_message`, and exception stack traces: `SELECT target_database_name, lifecycle, last_message FROM ____.job_executions`?

Domain: Configure and manage automation of tasks

- A. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Configure Azure Monitor Metric / Log Alert rules routed to Action Groups and query `jobs.job_executions` in the Elastic Job database to diagnose step failures

### 68. KestrelCart's SLA specifies zero data loss (`RPO = 0`) if a single datacenter Availability Zone loses power, plus cross-region DR with `RPO <= 5 seconds` and `RTO <= 1 hour` if an entire Azure region goes dark. Which architecture meets both SLAs?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG
- B. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- C. Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`)
- D. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled

### 69. A non-critical internal archive database has a tight budget and tolerates up to `1 hour` of data loss (`RPO = 1h`) and up to `12 hours` of recovery time (`RTO = 12h`) during a regional catastrophe without paying for a live secondary replica. Which DR mechanism fits best?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`)
- B. Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica
- C. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas
- D. Always Encrypted with VBS or Intel SGX secure enclaves (`ALLOW_ENCLAVE_COMPUTATIONS` + `Column Encryption Setting=Enabled`)

### 70. A retail chain runs SQL Server 2022 Enterprise on-premises and wants a warm cloud DR replica in Azure SQL Managed Instance that allows online planned failover to Azure during hurricane warnings AND online failback to on-premises afterward. Which feature supports this?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Expect online bidirectional planned failback from Azure SQL Managed Instance directly back to on-premises SQL Server 2016 without downtime
- B. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- C. Hybrid DR using Managed Instance link with bidirectional online failover between SQL Server 2022 and Azure SQL Managed Instance
- D. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 71. How does built-in intra-region High Availability differ architecturally between Business Critical and General Purpose tiers in Azure SQL Database / SQL Managed Instance?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica
- B. Azure SQL Managed Instance (Next-gen General Purpose) with decoupled IOPS and storage sliders
- C. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- D. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica

### 72. Compliance auditors require a quarterly zero-data-loss regional DR drill for three coupled e-commerce databases without manually editing microservice connection strings. Which four-step Failover Group workflow satisfies this requirement?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Execute unplanned `AllowDataLoss` forced failover during peak checkout → Create secondary logical SQL server afterward → Hardcode regional server names in app connection strings → Skip firewall rules on secondary
- B. Create Failover Group between two servers in the exact same datacenter rack → Add `tempdb` and `master` to Failover Group → Point OLTP writes to `.secondary.database.windows.net` → Disable Geo-Replication
- C. Export nightly `.bacpac` to local laptop → Delete production database to test restore → Manually edit 50 microservice connection strings → Re-enable TDE after 6 hours
- D. Provision secondary SQL server with matching firewall/Private Link & Entra admin → Create Failover Group with coupled DBs → Point apps to `<fog>.database.windows.net` & `.secondary` → Run planned `Switch-AzSqlDatabaseFailoverGroup` drill

### 73. During a scheduled DR readiness drill on a Failover Group, why must you invoke a **planned** failover (`Switch-AzSqlDatabaseFailoverGroup` without `-AllowDataLoss`) rather than a forced unplanned failover?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Non-disruptive DR readiness drill executing a planned zero-data-loss Failover Group switch (`Switch-AzSqlDatabaseFailoverGroup`), validating app listeners, and failing back
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 74. A QA lead needs a one-time `.bak` export of a database on Azure SQL Managed Instance to restore onto a dev container. Proposed solution: Run `BACKUP DATABASE [Catalog] TO URL = 'https://.../Catalog.bak'` without `WITH ____` and expect automated differential backups to remain unaffected. Does the solution meet the goal?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- B. No — taking an ad-hoc non-`COPY_ONLY` full backup resets the differential base and breaks downstream differential restores
- C. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- D. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server

### 75. You manage 14 SQL Server 2022 Azure VMs and want centralized Recovery Services Vault management with automated Full, Differential, and 15-minute Transaction Log backups plus `Auto-protection` for newly created databases. Which service should you deploy?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- B. Use `BACKUP DATABASE ... WITH COPY_ONLY` for ad-hoc exports on SQL MI / AGs, and Azure Backup Recovery Services Vault SQL-aware policies (`15-min` log RPO) on SQL VMs
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access

### 76. At 14:17 UTC an engineer accidentally drops table `Promotions` in production Azure SQL Database `CartDB` (14-day PITR). How does Point-in-Time Restore (`Restore-AzSqlDatabase -UsePointInTimeRestore -PointInTime "2026-11-01T14:16:00Z"`) behave?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Set Short-Term PITR retention to `3,650` days (`10 years`) and grant developers Subscription Contributor to prevent backup deletion
- B. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- C. Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback
- D. Long-Term Retention (`LTR`) weekly/monthly/yearly backups up to `10 years` protected by a locked time-based immutable (`WORM`) policy and `RA-GRS` / `ZRS` backup storage

### 77. A bulk price-update batch modifies 65 million rows in Azure SQL Database and is killed after 40 minutes. Instead of taking 40 minutes to undo log records, rollback finishes in under two seconds. Which built-in engine recovery technology makes this possible?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 78. Financial tax regulators mandate retaining monthly Azure SQL Database backups for 7 years and guaranteeing that even a compromised Subscription Owner cannot delete those backups early. Which two configurations are required? Select two.

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Set Short-Term PITR retention to `3,650` days (`10 years`) and grant developers Subscription Contributor to prevent backup deletion
- D. Enable and lock time-based immutability (`WORM`) on the LTR backup policy so nobody can shorten retention or delete compliance backups early
- E. Configure an Azure SQL Long-Term Retention (`LTR`) policy (`WeeklyRetention`, `MonthlyRetention`, `YearlyRetention`, `WeekOfYear`) up to 10 years

### 79. When provisioning a new Azure SQL Database in a region with Availability Zones, you want automated PITR and LTR backups replicated synchronously across zones AND asynchronously to a paired geo-region (`--backup-storage-redundancy ____`). Which redundancy option should you specify?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Set Short-Term PITR retention to `3,650` days (`10 years`) and grant developers Subscription Contributor to prevent backup deletion
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Long-Term Retention (`LTR`) weekly/monthly/yearly backups up to `10 years` protected by a locked time-based immutable (`WORM`) policy and `RA-GRS` / `ZRS` backup storage

### 80. You need to back up a 5.4 TB on-premises/VM SQL Server 2022 database directly to Azure Blob Storage over ExpressRoute using T-SQL `BACKUP DATABASE`. Which two actions are required to exceed the 1 TB single-page-blob ceiling? Select two.

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Stripe `BACKUP DATABASE` across multiple `TO URL = 'https://...bak'` block blob targets with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- D. Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access
- E. Create a SQL Server `CREDENTIAL` (`IDENTITY = 'Managed Identity'` or `'SHARED ACCESS SIGNATURE'`) matching the Azure Blob container URL

### 81. You write `CREATE CREDENTIAL [https://stbackups.blob.core.windows.net/sqlbak] WITH IDENTITY = '____', SECRET = 'sv=2022-11-02&ss=b...';` on SQL Server 2022 (making sure no leading `?` appears in `SECRET`). Which `IDENTITY` string enables SAS-authenticated Blob backups?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- B. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- C. Striped T-SQL `BACKUP DATABASE ... TO URL = ...` across up to 64 block blobs (`MAXTRANSFERSIZE`, `COMPRESSION`) authenticated via `Managed Identity` or `SHARED ACCESS SIGNATURE` Credential
- D. Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access

### 82. You configure an Azure SQL Database Failover Group `fog-kestrel` across East US and West US 2 with automatic failover enabled, while avoiding hair-trigger lossy failovers during 3-minute network blips. Which two settings should you apply? Select two.

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- C. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- D. Configure `ReadWriteFailoverPolicy = Automatic` with `GracePeriodWithDataLossHours >= 1` so transient blips do not trigger premature lossy failover
- E. Connect OLTP write traffic to `<fog>.database.windows.net` and read-only analytics to `<fog>.secondary.database.windows.net`

### 83. A global retail catalog database needs **four** readable secondary replicas distributed across Europe, Asia, South America, and Australia simultaneously. Why must you use Active Geo-Replication instead of a single Failover Group alone?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Long-Term Retention (`LTR`) weekly/monthly/yearly backups up to `10 years` protected by a locked time-based immutable (`WORM`) policy and `RA-GRS` / `ZRS` backup storage
- B. Failover Groups for automatic multi-database failover behind stable `<fog>.database.windows.net` / `.secondary` listeners vs Active Geo-Replication for up to 4 readable secondaries
- C. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- D. Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`)

### 84. You deploy a 2-node Always On Availability Group on SQL Server 2022 Azure VMs across two subnets without deploying an Azure Internal Load Balancer, and you set `____=True` in client connection strings for rapid DNS reconnection. Which listener and client setting pair achieves this?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`
- B. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG
- C. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- D. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)

### 85. Which lightweight quorum witness is recommended by Microsoft for a 2-node Windows Server Failover Cluster (`WSFC`) hosting an Always On Availability Group in a single Azure region across Availability Zones?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`
- B. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG
- C. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 86. A legacy retail warehouse WMS application requires whole-instance failover (`msdb` jobs, server logins, linked servers) and refuses Always On Availability Group listeners. How can you deploy a 2-node Always On Failover Cluster Instance (`FCI`) across Availability Zones on Azure VMs?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- B. Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`)
- C. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas
- D. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching

### 87. A franchise server maintains a warm DR copy on a secondary SQL Server Standard Edition VM via T-SQL Log Shipping, and analysts want to run read-only queries between 15-minute `.trn` restores using `RESTORE LOG ... WITH ____`. Which recovery clause allows read access between log restores?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- B. Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`)
- C. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 88. Alerts report rising recovery point lag on an Always On Availability Group secondary VM. Querying `sys.dm_hadr_database_replica_states` shows `log_send_queue_size = 12 KB` while `redo_queue_size = 18,400,000 KB`. What is the root cause?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- D. Query `sys.dm_hadr_database_replica_states` (`synchronization_state_desc`, `log_send_queue_size`, `redo_queue_size`) and `sys.dm_geo_replication_link_status`, plus verify NSG probe port `59999`

---

## Case study — BrambleBox Stores

BrambleBox Stores operates 320 SQL Server 2022 instances on Windows and Linux servers across regional distribution warehouses outside Azure. Leadership wants a single Azure portal inventory, automated SQL Best Practices Assessments, centralized Microsoft Entra authentication, and hourly pay-as-you-go billing.

The next 3 questions refer to **BrambleBox Stores**. Read the scenario brief once, then answer each item independently.

### 89. You onboard all 320 warehouse SQL Server 2022 instances to Azure Arc. Which three management and licensing capabilities become available from the Azure control plane? Select three.

Domain: Plan and implement data platform resources

- A. Switch eligible hybrid SQL Server instances to hourly Azure Arc pay-as-you-go billing instead of upfront core licenses
- B. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- C. Configure SQL Server password logins (`CREATE LOGIN ... WITH PASSWORD`) and T-SQL `BACKUP DATABASE ... TO DISK` inside SQL database in Microsoft Fabric
- D. Query fleet-wide SQL Server version, edition, and backup status across hybrid servers via Azure Resource Graph Explorer
- E. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- F. Enable automated SQL Best Practices Assessments and Microsoft Defender for SQL via the Azure Arc SQL Server extension

### 90. Regional warehouse servers must remain in on-premises racks for local scanner sub-millisecond latency while using Microsoft Entra authentication on SQL Server 2022. Which hybrid service enables Microsoft Entra authentication on those non-Azure hosts?

Domain: Plan and implement data platform resources

- A. SQL Server enabled by Azure Arc (`Microsoft.AzureArcData/sqlServerInstances`)
- B. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- C. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- D. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled

### 91. Leadership decides to migrate 12 back-office SQL Server 2016 instances into Azure SQL PaaS and wants automated feature-blocker detection plus performance-based vCore SKU sizing. Which modern Microsoft toolset should you run?

Domain: Plan and implement data platform resources

- A. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- B. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Azure Migrate (`Azure SQL` assessment) and the Azure SQL Migration extension for Azure Data Studio / VS Code

---

## Case study — HarborPick Fulfillment

HarborPick Fulfillment runs high-concurrency warehouse picking on Azure SQL Database. After a nightly batch skews inventory counts, a critical stored procedure regresses to a slow nested-loops plan, reader sessions wait behind `LCK_M_S` writer locks, and schema maintenance must run across 35 regional databases.

The next 3 questions refer to **HarborPick Fulfillment**. Read the scenario brief once, then answer each item independently.

### 92. Which two built-in Query Store stored procedures let you immediately stabilize the regressed warehouse-picking query without modifying or redeploying application code? Select two.

Domain: Monitor, configure, and optimize database resources

- A. Execute `sys.sp_query_store_set_hints @query_id, N'OPTION (RECOMPILE)'` (or `MAXDOP` / memory grant hints) without redeploying code
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- E. Execute `sys.sp_query_store_force_plan @query_id, @plan_id` to pin the historical low-latency execution plan immediately

### 93. Which database concurrency features eliminate `LCK_M_S` reader waits behind writers and replace thousands of row locks with a single Transaction ID (`TID`) lock without permitting dirty reads?

Domain: Monitor, configure, and optimize database resources

- A. Read Committed Snapshot Isolation (`READ_COMMITTED_SNAPSHOT = ON`) combined with Optimized Locking (`TID` locking + Lock After Qualification `LAQ`)
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 94. You must roll out DDL schema updates and index maintenance across all 35 regional Azure SQL Databases passwordlessly, automatically including new regional databases added later. Which two Elastic Job configurations should you use? Select two.

Domain: Configure and manage automation of tasks

- A. Add logical SQL servers or Elastic Pools (`include` / `exclude` members) to an Elastic Job Target Group so new tenant DBs inherit jobs automatically
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Assign a User-Assigned Managed Identity to the Elastic Job Agent and create a contained `FROM EXTERNAL PROVIDER` user on target databases
- D. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- E. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

---

## Case study — KestrelCart Commerce

KestrelCart Commerce runs a 14 TB multi-region order database in Azure SQL Database experiencing rapid seasonal growth, bursty BI read traffic from three analytics teams that must be compute-isolated from OLTP checkouts, and 18 non-production staging databases that sit idle every night and weekend.

The next 3 questions refer to **KestrelCart Commerce**. Read the scenario brief once, then answer each item independently.

### 95. Which Azure SQL Database service tier and read-scale feature should you recommend for the 14 TB primary order database so three analytics teams get isolated vCore compute over shared storage?

Domain: Plan and implement data platform resources

- A. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- B. SQL Server on Azure Virtual Machines (`Ebdsv5` series) with full OS and engine version control
- C. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas
- D. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica

### 96. Which Azure SQL Database compute configuration minimizes compute cost for the 18 non-production staging databases that sit completely idle every night and weekend?

Domain: Plan and implement data platform resources

- A. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- B. Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica
- C. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- D. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas

### 97. You partition `OrderHistory` monthly on `OrderTimestamp DATETIME2` using `CREATE PARTITION FUNCTION pf_Month (DATETIME2) AS RANGE ____ FOR VALUES ('2026-01-01', '2026-02-01')` so midnight `'2026-01-01 00:00:00'` rows land in January's partition. Which strategy applies?

Domain: Plan and implement data platform resources

- A. Table partitioning using `CREATE PARTITION FUNCTION ... AS RANGE RIGHT` with aligned indexes and `ALTER TABLE ... SWITCH`
- B. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- C. Horizontal sharding using the Elastic Database Client Library (`ShardMapManager` with `ListShardMap` or `RangeShardMap`)
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

---

## Case study — VelvetLoom Checkout

VelvetLoom Checkout stores payment tokens and customer SSNs in Azure SQL Database. Fraud investigators must run `LIKE` suffix searches on encrypted SSNs without DBAs ever seeing plaintext keys or values, all public internet access must be blocked, and regional support reps may view only their own country rows.

The next 3 questions refer to **VelvetLoom Checkout**. Read the scenario brief once, then answer each item independently.

### 98. Which encryption technology lets fraud investigators run `WHERE SSN LIKE '%-4821'` while guaranteeing DBAs never access plaintext SSNs or Column Master Keys?

Domain: Implement a secure environment

- A. Always Encrypted (`Randomized` for maximum security with zero equality leakage; `Deterministic` only when `=` joins or `GROUP BY` are required)
- B. Transparent Data Encryption (TDE) with a Customer-Managed Key (`CMK`) in Azure Key Vault (`Soft Delete` + `Purge Protection`)
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Always Encrypted with VBS or Intel SGX secure enclaves (`ALLOW_ENCLAVE_COMPUTATIONS` + `Column Encryption Setting=Enabled`)

### 99. Which network configuration blocks all public internet access to the Azure SQL Database and routes payment microservice traffic exclusively over a private VNet IP?

Domain: Implement a secure environment

- A. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Azure Private Endpoint (`Microsoft.Network/privateEndpoints`) paired with `privatelink.database.windows.net` Private DNS and `publicNetworkAccess = Disabled`
- D. Virtual Network Service Endpoints (`Microsoft.Sql`) with outbound storage firewall rules, or dedicated `/28+` delegated subnet for SQL MI

### 100. Regional support reps must query and update only rows matching their assigned `CountryIso` and be blocked from inserting rows for other countries. Which three Row-Level Security components should you implement? Select three.

Domain: Implement a secure environment

- A. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- B. Add a `FILTER PREDICATE` in `CREATE SECURITY POLICY` to hide non-matching rows silently from `SELECT`, `UPDATE`, and `DELETE`
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Create an inline table-valued function `WITH SCHEMABINDING` evaluating `SESSION_CONTEXT()` or `DATABASE_PRINCIPAL_ID()`
- E. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- F. Add `AFTER INSERT` and `AFTER UPDATE` / `BEFORE UPDATE` `BLOCK PREDICATE` clauses in `CREATE SECURITY POLICY` (`STATE = ON`)

---

## Answer key and explanations

### Question 1 — B

Answer: SQL Server on Azure Virtual Machines (`Ebdsv5` series) with full OS and engine version control. SQL Server on Azure Virtual Machines (IaaS) grants full guest OS administrative control for custom Windows COM+ binaries, exact SQL Server CU version pinning, and local SSRS installation. SQL Server on Azure VMs (IaaS) provides full OS access, custom third-party drivers, legacy SQL Server version pinning, SSIS/SSRS/SSAS co-hosting, and `Ebdsv5` high remote storage throughput. Local study-map skill 1.1 (Recommend an Azure SQL Offering (SQL Database, SQL Managed Instance, or SQL Server on Azure VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Compare Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview).

- **A:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: SQL Server on Azure Virtual Machines (IaaS) grants full guest OS administrative control for custom Windows COM+ binaries, exact SQL Server CU version pinning, and local SSRS installation.
- **B:** Correct. SQL Server on Azure VMs (IaaS) provides full OS access, custom third-party drivers, legacy SQL Server version pinning, SSIS/SSRS/SSAS co-hosting, and `Ebdsv5` high remote storage throughput. In this scenario: SQL Server on Azure Virtual Machines (IaaS) grants full guest OS administrative control for custom Windows COM+ binaries, exact SQL Server CU version pinning, and local SSRS installation.
- **C:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: SQL Server on Azure Virtual Machines (IaaS) grants full guest OS administrative control for custom Windows COM+ binaries, exact SQL Server CU version pinning, and local SSRS installation.
- **D:** Incorrect for this requirement. Elastic Pools share a pooled vCore/storage envelope across many multi-tenant databases with staggered peaks while capping per-database max vCores to stop noisy-neighbor starvation. Why the keyed choice wins: SQL Server on Azure Virtual Machines (IaaS) grants full guest OS administrative control for custom Windows COM+ binaries, exact SQL Server CU version pinning, and local SSRS installation.

### Question 2 — A

Answer: SQL Server on Linux configured via `mssql-conf` or Linux container images for consistent CI/CD dev-test parity. SQL Server Linux container images provide fast disposable CI test instances on Ubuntu runners, while `mssql-conf` manages engine memory, network, and HA settings on RHEL Linux SQL hosts. `mssql-conf` configures memory, trace flags, Entra auth, and HA on Linux SQL Server VMs, while official Linux container images spin up fast disposable SQL instances in CI pipelines. Local study-map skill 1.2 (Choose Automated Deployment Methods and Deploy SQL Offerings Across Windows, Linux, and Containers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated deployment options for Azure SQL and SQL Server on Linux/containers (https://learn.microsoft.com/en-us/azure/azure-sql/database/arm-templates-content-guide).

- **A:** Correct. `mssql-conf` configures memory, trace flags, Entra auth, and HA on Linux SQL Server VMs, while official Linux container images spin up fast disposable SQL instances in CI pipelines. In this scenario: SQL Server Linux container images provide fast disposable CI test instances on Ubuntu runners, while `mssql-conf` manages engine memory, network, and HA settings on RHEL Linux SQL hosts.
- **B:** Incorrect for this requirement. Azure Arc projects on-premises and multicloud SQL Server instances into Azure for Resource Graph inventory, automated Best Practices Assessments, Entra auth (SQL 2022+), Defender, and PAYG billing. Why the keyed choice wins: SQL Server Linux container images provide fast disposable CI test instances on Ubuntu runners, while `mssql-conf` manages engine memory, network, and HA settings on RHEL Linux SQL hosts.
- **C:** Incorrect for this requirement. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. Why the keyed choice wins: SQL Server Linux container images provide fast disposable CI test instances on Ubuntu runners, while `mssql-conf` manages engine memory, network, and HA settings on RHEL Linux SQL hosts.
- **D:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: SQL Server Linux container images provide fast disposable CI test instances on Ubuntu runners, while `mssql-conf` manages engine memory, network, and HA settings on RHEL Linux SQL hosts.

### Question 3 — C, E

Answers: Create a dedicated VNet subnet (`/28` or larger) with no other cloud resources and delegate it to `Microsoft.Sql/managedInstances`; Associate a User-Defined Route (`UDR`) table (`0.0.0.0/0` -> `Internet` for management plane) and required NSG rules with the SQL MI subnet. Deploying Azure SQL Managed Instance requires a dedicated empty subnet (`/28` or larger) delegated to `Microsoft.Sql/managedInstances` with an associated UDR route table and NSG. Local study-map skill 1.2 (Choose Automated Deployment Methods and Deploy SQL Offerings Across Windows, Linux, and Containers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated deployment options for Azure SQL and SQL Server on Linux/containers (https://learn.microsoft.com/en-us/azure/azure-sql/database/arm-templates-content-guide).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Deploying Azure SQL Managed Instance requires a dedicated empty subnet (`/28` or larger) delegated to `Microsoft.Sql/managedInstances` with an associated UDR route table and NSG.
- **B:** Incorrect for this requirement. SQL database in Microsoft Fabric relies exclusively on Microsoft Entra authentication and workspace/item permissions rather than SQL logins. Why the keyed choice wins: Deploying Azure SQL Managed Instance requires a dedicated empty subnet (`/28` or larger) delegated to `Microsoft.Sql/managedInstances` with an associated UDR route table and NSG.
- **C:** Correct. SQL Managed Instance requires an explicit route table and NSG bound to its delegated subnet so Azure management traffic is never blackholed by forced tunneling. In this scenario: Deploying Azure SQL Managed Instance requires a dedicated empty subnet (`/28` or larger) delegated to `Microsoft.Sql/managedInstances` with an associated UDR route table and NSG.
- **D:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Deploying Azure SQL Managed Instance requires a dedicated empty subnet (`/28` or larger) delegated to `Microsoft.Sql/managedInstances` with an associated UDR route table and NSG.
- **E:** Correct. Azure SQL Managed Instance requires an exclusive subnet delegated to `Microsoft.Sql/managedInstances` sized for current and future instance vCore/node counts. In this scenario: Deploying Azure SQL Managed Instance requires a dedicated empty subnet (`/28` or larger) delegated to `Microsoft.Sql/managedInstances` with an associated UDR route table and NSG.

### Question 4 — B, D

Answers: Authenticate applications and users exclusively with Microsoft Entra ID identities, service principals, or workspace roles; Query automatically replicated OneLake Delta Parquet tables and the read-only SQL analytics endpoint from Spark and Direct Lake. SQL database in Microsoft Fabric enforces Microsoft Entra-only authentication (no SQL logins) and automatically mirrors operational tables into OneLake as Delta Parquet with a SQL analytics endpoint. Local study-map skill 1.3 (Identify Use Cases for SQL Server Enabled by Azure Arc and SQL Database in Microsoft Fabric), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server enabled by Azure Arc and SQL database in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/database/sql/overview).

- **A:** Incorrect for this requirement. SQL database in Microsoft Fabric enforces Microsoft Entra authentication exclusively (SQL logins are unsupported) and manages backups/OneLake mirroring automatically as SaaS. Why the keyed choice wins: SQL database in Microsoft Fabric enforces Microsoft Entra-only authentication (no SQL logins) and automatically mirrors operational tables into OneLake as Delta Parquet with a SQL analytics endpoint.
- **B:** Correct. SQL database in Microsoft Fabric relies exclusively on Microsoft Entra authentication and workspace/item permissions rather than SQL logins. In this scenario: SQL database in Microsoft Fabric enforces Microsoft Entra-only authentication (no SQL logins) and automatically mirrors operational tables into OneLake as Delta Parquet with a SQL analytics endpoint.
- **C:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: SQL database in Microsoft Fabric enforces Microsoft Entra-only authentication (no SQL logins) and automatically mirrors operational tables into OneLake as Delta Parquet with a SQL analytics endpoint.
- **D:** Correct. In this scenario: SQL database in Microsoft Fabric enforces Microsoft Entra-only authentication (no SQL logins) and automatically mirrors operational tables into OneLake as Delta Parquet with a SQL analytics endpoint.
- **E:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: SQL database in Microsoft Fabric enforces Microsoft Entra-only authentication (no SQL logins) and automatically mirrors operational tables into OneLake as Delta Parquet with a SQL analytics endpoint.

### Question 5 — B

Answer: SPLIT partition function for incoming future boundary → Create empty staging table on same filegroup with matching schema/indexes → ALTER TABLE ... SWITCH oldest partition to staging → Archive staging data & MERGE retired boundary. A sliding-window partition rotation splits the future boundary first, prepares a schema- and filegroup-aligned empty staging table, executes metadata-only `ALTER TABLE ... SWITCH`, and merges the retired boundary. Sliding-window partitioning splits a new empty future range first, performs a metadata-only `ALTER TABLE ... SWITCH` into an aligned staging table, and merges the retired boundary. Local study-map skill 1.4 (Plan for Table Partitioning (`RANGE RIGHT` / `SWITCH`) and Horizontal Database Sharding (`ShardMapManager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Table partitioning and scaling out with Azure SQL Database sharding (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-scale-introduction).

- **A:** Incorrect for this requirement. Incorrect workflow: `ALTER TABLE ... SWITCH` swaps metadata between two tables in the same database/filegroup rather than writing directly to Azure Blob Storage. Why the keyed choice wins: A sliding-window partition rotation splits the future boundary first, prepares a schema- and filegroup-aligned empty staging table, executes metadata-only `ALTER TABLE ... SWITCH`, and merges the retired boundary.
- **B:** Correct. Sliding-window partitioning splits a new empty future range first, performs a metadata-only `ALTER TABLE ... SWITCH` into an aligned staging table, and merges the retired boundary. In this scenario: A sliding-window partition rotation splits the future boundary first, prepares a schema- and filegroup-aligned empty staging table, executes metadata-only `ALTER TABLE ... SWITCH`, and merges the retired boundary.
- **C:** Incorrect for this requirement. Incorrect workflow: `SWITCH` is strictly an intra-database metadata operation requiring identical schema, filegroup alignment, and trusted constraints—never cross-database. Why the keyed choice wins: A sliding-window partition rotation splits the future boundary first, prepares a schema- and filegroup-aligned empty staging table, executes metadata-only `ALTER TABLE ... SWITCH`, and merges the retired boundary.
- **D:** Incorrect for this requirement. Incorrect workflow: row-by-row `DELETE` bloats the transaction log and locks tables, and `SWITCH` fails if the staging table resides on a different filegroup or lacks aligned indexes. Why the keyed choice wins: A sliding-window partition rotation splits the future boundary first, prepares a schema- and filegroup-aligned empty staging table, executes metadata-only `ALTER TABLE ... SWITCH`, and merges the retired boundary.

### Question 6 — A

Answer: Horizontal sharding using the Elastic Database Client Library (`ShardMapManager` with `ListShardMap` or `RangeShardMap`). The Elastic Database Client Library (`ShardMapManager` with a `ListShardMap`) maps discrete `CountryCode` keys directly to individual shard databases for low-latency data-dependent routing. `ListShardMap` maps discrete `TenantId` keys and `RangeShardMap` maps contiguous ID spans to independent Azure SQL Databases, routing data-dependent connections directly from the app tier. Local study-map skill 1.4 (Plan for Table Partitioning (`RANGE RIGHT` / `SWITCH`) and Horizontal Database Sharding (`ShardMapManager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Table partitioning and scaling out with Azure SQL Database sharding (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-scale-introduction).

- **A:** Correct. `ListShardMap` maps discrete `TenantId` keys and `RangeShardMap` maps contiguous ID spans to independent Azure SQL Databases, routing data-dependent connections directly from the app tier. In this scenario: The Elastic Database Client Library (`ShardMapManager` with a `ListShardMap`) maps discrete `CountryCode` keys directly to individual shard databases for low-latency data-dependent routing.
- **B:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: The Elastic Database Client Library (`ShardMapManager` with a `ListShardMap`) maps discrete `CountryCode` keys directly to individual shard databases for low-latency data-dependent routing.
- **C:** Incorrect for this requirement. `RANGE RIGHT` places each upper-boundary date value cleanly as the lower bound of its own monthly/daily partition, enabling metadata-only `SWITCH` archival when indexes are aligned. Why the keyed choice wins: The Elastic Database Client Library (`ShardMapManager` with a `ListShardMap`) maps discrete `CountryCode` keys directly to individual shard databases for low-latency data-dependent routing.
- **D:** Incorrect for this requirement. `sp_estimate_data_compression_savings` models space gains before compressing; `ROW`/`PAGE` shrink OLTP B-trees while `COLUMNSTORE` / `COLUMNSTORE_ARCHIVE` achieves up to 10x analytics compression. Why the keyed choice wins: The Elastic Database Client Library (`ShardMapManager` with a `ListShardMap`) maps discrete `CountryCode` keys directly to individual shard databases for low-latency data-dependent routing.

### Question 7 — B

Answer: SQL IaaS Agent Extension in Full management mode paired with Azure Update Manager / Automated Patching. Registering the VMs with the SQL IaaS Agent Extension in Full mode paired with Automated Patching / Azure Update Manager enables portal license management and scheduled cumulative update windows. The SQL IaaS Agent Extension unlocks portal license conversion (AHB/PAYG), Automated Backup, Automated Patching windows, Key Vault integration, and storage pool management on SQL VMs. Local study-map skill 1.5 (Deploy Hybrid SQL Server Solutions and Manage Patching (`SQL IaaS Agent Extension` & `Azure Update Manager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server IaaS Agent Extension, Automated Patching, and Azure Update Manager (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-agent-extension-manually-register-single-vm).

- **A:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: Registering the VMs with the SQL IaaS Agent Extension in Full mode paired with Automated Patching / Azure Update Manager enables portal license management and scheduled cumulative update windows.
- **B:** Correct. The SQL IaaS Agent Extension unlocks portal license conversion (AHB/PAYG), Automated Backup, Automated Patching windows, Key Vault integration, and storage pool management on SQL VMs. In this scenario: Registering the VMs with the SQL IaaS Agent Extension in Full mode paired with Automated Patching / Azure Update Manager enables portal license management and scheduled cumulative update windows.
- **C:** Incorrect for this requirement. Elastic Pools share a pooled vCore/storage envelope across many multi-tenant databases with staggered peaks while capping per-database max vCores to stop noisy-neighbor starvation. Why the keyed choice wins: Registering the VMs with the SQL IaaS Agent Extension in Full mode paired with Automated Patching / Azure Update Manager enables portal license management and scheduled cumulative update windows.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Registering the VMs with the SQL IaaS Agent Extension in Full mode paired with Automated Patching / Azure Update Manager enables portal license management and scheduled cumulative update windows.

### Question 8 — A

Answer: Azure SQL Managed Instance (Next-gen General Purpose) with decoupled IOPS and storage sliders. Next-gen General Purpose on Azure SQL Managed Instance supports up to 500 databases per instance and decouples IOPS and storage throughput sliders from provisioned vCores and file sizes. SQL Managed Instance provides near-100% SQL Server engine compatibility (cross-DB queries, SQL Agent, CLR, Service Broker), and Next-gen GP scales IOPS independently of storage up to 500 DBs. Local study-map skill 1.7 (Configure Azure SQL Managed Instance for Scale and Performance (`Next-gen GP` Sliders & `Business Critical`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure SQL Managed Instance service tiers and Next-gen General Purpose scaling (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview).

- **A:** Correct. SQL Managed Instance provides near-100% SQL Server engine compatibility (cross-DB queries, SQL Agent, CLR, Service Broker), and Next-gen GP scales IOPS independently of storage up to 500 DBs. In this scenario: Next-gen General Purpose on Azure SQL Managed Instance supports up to 500 databases per instance and decouples IOPS and storage throughput sliders from provisioned vCores and file sizes.
- **B:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Next-gen General Purpose on Azure SQL Managed Instance supports up to 500 databases per instance and decouples IOPS and storage throughput sliders from provisioned vCores and file sizes.
- **C:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: Next-gen General Purpose on Azure SQL Managed Instance supports up to 500 databases per instance and decouples IOPS and storage throughput sliders from provisioned vCores and file sizes.
- **D:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Next-gen General Purpose on Azure SQL Managed Instance supports up to 500 databases per instance and decouples IOPS and storage throughput sliders from provisioned vCores and file sizes.

### Question 9 — B

Answer: Premium SSD v2 / striped Premium SSD with `ReadOnly` host caching for data disks, `None` for log disks, and `tempdb` on local NVMe. Placing `.mdf` data disks on Premium SSD with `ReadOnly` host caching, `.ldf` log disks with `None` host caching, and `tempdb` on local ephemeral NVMe storage maximizes OLTP throughput safely. SQL Server Azure VM best practices use `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` caching on `.ldf` transaction log disks, and ephemeral NVMe/`D:` storage for `tempdb`. Local study-map skill 1.8 (Configure SQL Server on Azure VMs for Scale and Performance (`ReadOnly`/`None` Host Caching, `tempdb` NVMe, `IFI`/`LPIM`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Performance best practices for SQL Server on Azure Virtual Machines (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-checklist).

- **A:** Incorrect for this requirement. SQL Server write-ahead logging performs sequential unbuffered writes; enabling `ReadOnly` or `ReadWrite` host caching on `.ldf` disks degrades throughput or risks corruption. Why the keyed choice wins: Placing `.mdf` data disks on Premium SSD with `ReadOnly` host caching, `.ldf` log disks with `None` host caching, and `tempdb` on local ephemeral NVMe storage maximizes OLTP throughput safely.
- **B:** Correct. SQL Server Azure VM best practices use `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` caching on `.ldf` transaction log disks, and ephemeral NVMe/`D:` storage for `tempdb`. In this scenario: Placing `.mdf` data disks on Premium SSD with `ReadOnly` host caching, `.ldf` log disks with `None` host caching, and `tempdb` on local ephemeral NVMe storage maximizes OLTP throughput safely.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Placing `.mdf` data disks on Premium SSD with `ReadOnly` host caching, `.ldf` log disks with `None` host caching, and `tempdb` on local ephemeral NVMe storage maximizes OLTP throughput safely.
- **D:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Placing `.mdf` data disks on Premium SSD with `ReadOnly` host caching, `.ldf` log disks with `None` host caching, and `tempdb` on local ephemeral NVMe storage maximizes OLTP throughput safely.

### Question 10 — D

Answer: No — transaction log managed disks on SQL Server Azure VMs must use host caching `None`, never `ReadOnly` or `ReadWrite`. Transaction log disks must always use `None` host caching; `ReadWrite` caching on `.ldf` volumes degrades sequential unbuffered write-ahead flushes and risks database corruption on host crash. SQL Server write-ahead logging performs sequential unbuffered writes; enabling `ReadOnly` or `ReadWrite` host caching on `.ldf` disks degrades throughput or risks corruption. Local study-map skill 1.8 (Configure SQL Server on Azure VMs for Scale and Performance (`ReadOnly`/`None` Host Caching, `tempdb` NVMe, `IFI`/`LPIM`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Performance best practices for SQL Server on Azure Virtual Machines (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-checklist).

- **A:** Incorrect for this requirement. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. Why the keyed choice wins: Transaction log disks must always use `None` host caching; `ReadWrite` caching on `.ldf` volumes degrades sequential unbuffered write-ahead flushes and risks database corruption on host crash.
- **B:** Incorrect for this requirement. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Why the keyed choice wins: Transaction log disks must always use `None` host caching; `ReadWrite` caching on `.ldf` volumes degrades sequential unbuffered write-ahead flushes and risks database corruption on host crash.
- **C:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: Transaction log disks must always use `None` host caching; `ReadWrite` caching on `.ldf` volumes degrades sequential unbuffered write-ahead flushes and risks database corruption on host crash.
- **D:** Correct. SQL Server write-ahead logging performs sequential unbuffered writes; enabling `ReadOnly` or `ReadWrite` host caching on `.ldf` disks degrades throughput or risks corruption. In this scenario: Transaction log disks must always use `None` host caching; `ReadWrite` caching on `.ldf` volumes degrades sequential unbuffered write-ahead flushes and risks database corruption on host crash.

### Question 11 — D

Answer: Enable Availability Groups & master key on SQL Server → Establish VNet/IPsec network peering on TCP 5022 → Create Managed Instance link & seed distributed AG → Validate sync state and execute planned cutover to SQL MI. Managed Instance link prepares Availability Groups and a database master key on SQL Server, peers networks over TCP 5022, seeds a distributed AG continuously, and executes a planned near-zero-downtime cutover. Managed Instance link uses a distributed Availability Group over port 5022 to seed and continuously replicate transaction logs online before executing a near-zero-downtime cutover. Local study-map skill 1.11 (Implement Online and Offline Migrations to and Between Azure SQL Services (`MI Link`, `LRS`, `SqlPackage` Copy)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Online and offline SQL migrations with Managed Instance link, Log Replay Service, and SqlPackage (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-feature-overview).

- **A:** Incorrect for this requirement. Incorrect workflow: `.bacpac` logical export/import is neither transactional on a live DB without a copy nor how Managed Instance link distributed AG replication operates. Why the keyed choice wins: Managed Instance link prepares Availability Groups and a database master key on SQL Server, peers networks over TCP 5022, seeds a distributed AG continuously, and executes a planned near-zero-downtime cutover.
- **B:** Incorrect for this requirement. Incorrect workflow: SQL Managed Instance does not support attaching raw `.mdf`/`.ldf` files from SMB shares, and taking SQL Server offline defeats online migration. Why the keyed choice wins: Managed Instance link prepares Availability Groups and a database master key on SQL Server, peers networks over TCP 5022, seeds a distributed AG continuously, and executes a planned near-zero-downtime cutover.
- **C:** Incorrect for this requirement. Incorrect order: distributed AG prerequisites and TCP 5022 network connectivity must be in place before creating and seeding a Managed Instance link. Why the keyed choice wins: Managed Instance link prepares Availability Groups and a database master key on SQL Server, peers networks over TCP 5022, seeds a distributed AG continuously, and executes a planned near-zero-downtime cutover.
- **D:** Correct. Managed Instance link uses a distributed Availability Group over port 5022 to seed and continuously replicate transaction logs online before executing a near-zero-downtime cutover. In this scenario: Managed Instance link prepares Availability Groups and a database master key on SQL Server, peers networks over TCP 5022, seeds a distributed AG continuously, and executes a planned near-zero-downtime cutover.

### Question 12 — D

Answer: Online Azure SQL Managed Instance Database Move / Copy (`TCP 5022` & `11000–11999`, 24-hour manual completion window). Once an online SQL Managed Instance database copy or move reaches `Ready for completion`, TCP 5022/11000–11999 log sync continues for up to 24 hours before auto-canceling if uncompleted. Online MI Database Copy/Move uses Always On seeding across instances/subscriptions; once `Ready for completion`, you have 24 hours to complete (`Move` removes source DB with zero data loss; `Copy` keeps both). Local study-map skill 1.12 (Implement Azure SQL Managed Instance Online Database Copy and Move (`24h` Completion, `TCP 5022`/`11000-11999`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Copy or move a database online across Azure SQL Managed Instances (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/database-copy-move-how-to).

- **A:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: Once an online SQL Managed Instance database copy or move reaches `Ready for completion`, TCP 5022/11000–11999 log sync continues for up to 24 hours before auto-canceling if uncompleted.
- **B:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Once an online SQL Managed Instance database copy or move reaches `Ready for completion`, TCP 5022/11000–11999 log sync continues for up to 24 hours before auto-canceling if uncompleted.
- **C:** Incorrect for this requirement. `Start-AzSqlInstanceDatabaseLogReplay` continuously replays `.bak`/`.trn` files from Blob storage until `Complete-AzSqlInstanceDatabaseLogReplay` restores the final tail-log backup. Why the keyed choice wins: Once an online SQL Managed Instance database copy or move reaches `Ready for completion`, TCP 5022/11000–11999 log sync continues for up to 24 hours before auto-canceling if uncompleted.
- **D:** Correct. Online MI Database Copy/Move uses Always On seeding across instances/subscriptions; once `Ready for completion`, you have 24 hours to complete (`Move` removes source DB with zero data loss; `Copy` keeps both). In this scenario: Once an online SQL Managed Instance database copy or move reaches `Ready for completion`, TCP 5022/11000–11999 log sync continues for up to 24 hours before auto-canceling if uncompleted.

### Question 13 — D

Answer: Enable Microsoft Entra-only authentication (`azuread_authentication_only`) on the logical SQL server or SQL Managed Instance. Enabling Microsoft Entra-only authentication (`az sql server ad-only-auth enable`) blocks every SQL password login and requires centralized Microsoft Entra tokens across the server. Microsoft Entra-only authentication disables legacy SQL Server logins (`sa` and password auth) completely, enforcing centralized MFA, Conditional Access, and token-based Managed Identities. Local study-map skill 2.1 (Configure Microsoft Entra ID and Microsoft Entra-Only Authentication Across SQL DB, SQL MI, and SQL Server), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure and manage Microsoft Entra authentication with Azure SQL and SQL Server (https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Enabling Microsoft Entra-only authentication (`az sql server ad-only-auth enable`) blocks every SQL password login and requires centralized Microsoft Entra tokens across the server.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Enabling Microsoft Entra-only authentication (`az sql server ad-only-auth enable`) blocks every SQL password login and requires centralized Microsoft Entra tokens across the server.
- **C:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Enabling Microsoft Entra-only authentication (`az sql server ad-only-auth enable`) blocks every SQL password login and requires centralized Microsoft Entra tokens across the server.
- **D:** Correct. Microsoft Entra-only authentication disables legacy SQL Server logins (`sa` and password auth) completely, enforcing centralized MFA, Conditional Access, and token-based Managed Identities. In this scenario: Enabling Microsoft Entra-only authentication (`az sql server ad-only-auth enable`) blocks every SQL password login and requires centralized Microsoft Entra tokens across the server.

### Question 14 — C

Answer: Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`). Creating a contained database user `FROM EXTERNAL PROVIDER` maps the App Service Managed Identity directly inside the user database without passwords or `master` logins. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. Local study-map skill 2.1 (Configure Microsoft Entra ID and Microsoft Entra-Only Authentication Across SQL DB, SQL MI, and SQL Server), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure and manage Microsoft Entra authentication with Azure SQL and SQL Server (https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Creating a contained database user `FROM EXTERNAL PROVIDER` maps the App Service Managed Identity directly inside the user database without passwords or `master` logins.
- **B:** Incorrect for this requirement. Microsoft Entra Kerberos issues Kerberos tickets for SQL Managed Instance without requiring customer-managed Active Directory Domain Services domain controllers inside Azure. Why the keyed choice wins: Creating a contained database user `FROM EXTERNAL PROVIDER` maps the App Service Managed Identity directly inside the user database without passwords or `master` logins.
- **C:** Correct. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. In this scenario: Creating a contained database user `FROM EXTERNAL PROVIDER` maps the App Service Managed Identity directly inside the user database without passwords or `master` logins.
- **D:** Incorrect for this requirement. Restoring a `.bak` onto another instance mismatches login SIDs (fixed via `ALTER USER ... WITH LOGIN`), while an explicit table/schema `DENY` always overrides `db_datareader` role `GRANT`s. Why the keyed choice wins: Creating a contained database user `FROM EXTERNAL PROVIDER` maps the App Service Managed Identity directly inside the user database without passwords or `master` logins.

### Question 15 — A

Answer: Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or `Entra Kerberos`). Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos issues Kerberos tickets via an Entra trust without hosting AD DS domain controller VMs in Azure. Microsoft Entra Kerberos issues Kerberos tickets for SQL Managed Instance without requiring customer-managed Active Directory Domain Services domain controllers inside Azure. Local study-map skill 2.2 (Configure Authentication for SQL Server on Azure VMs and SQL MI (`Microsoft Entra Kerberos` & AD Trusts)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos and AD (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/winauth-azuread-overview).

- **A:** Correct. Microsoft Entra Kerberos issues Kerberos tickets for SQL Managed Instance without requiring customer-managed Active Directory Domain Services domain controllers inside Azure. In this scenario: Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos issues Kerberos tickets via an Entra trust without hosting AD DS domain controller VMs in Azure.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos issues Kerberos tickets via an Entra trust without hosting AD DS domain controller VMs in Azure.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos issues Kerberos tickets via an Entra trust without hosting AD DS domain controller VMs in Azure.
- **D:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos issues Kerberos tickets via an Entra trust without hosting AD DS domain controller VMs in Azure.

### Question 16 — C

Answer: Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`). A contained database user mapped to the Microsoft Entra security group (`CREATE USER [SG-Retail-Analysts] FROM EXTERNAL PROVIDER`) lives inside the replicated user database and works seamlessly on any replica. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. Local study-map skill 2.3 (Configure Security Principals and Portable Contained Microsoft Entra Users (`FROM EXTERNAL PROVIDER`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Contained database users and Microsoft Entra security principals in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage).

- **A:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: A contained database user mapped to the Microsoft Entra security group (`CREATE USER [SG-Retail-Analysts] FROM EXTERNAL PROVIDER`) lives inside the replicated user database and works seamlessly on any replica.
- **B:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: A contained database user mapped to the Microsoft Entra security group (`CREATE USER [SG-Retail-Analysts] FROM EXTERNAL PROVIDER`) lives inside the replicated user database and works seamlessly on any replica.
- **C:** Correct. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. In this scenario: A contained database user mapped to the Microsoft Entra security group (`CREATE USER [SG-Retail-Analysts] FROM EXTERNAL PROVIDER`) lives inside the replicated user database and works seamlessly on any replica.
- **D:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: A contained database user mapped to the Microsoft Entra security group (`CREATE USER [SG-Retail-Analysts] FROM EXTERNAL PROVIDER`) lives inside the replicated user database and works seamlessly on any replica.

### Question 17 — C

Answer: Built-in granular server-level roles (`##MS_ServerStateReader##`, `##MS_DefinitionReader##`) or `GRANT VIEW DATABASE PERFORMANCE STATE`. Adding the principal to `##MS_ServerStateReader##` grants server-wide `VIEW SERVER PERFORMANCE STATE` read access to DMVs while withholding user-table `SELECT` privileges. Modern granular server roles and state permissions let monitoring accounts inspect DMVs and metadata without granting `sysadmin`, `db_owner`, or `SELECT` access to user tables. Local study-map skill 2.3 (Configure Security Principals and Portable Contained Microsoft Entra Users (`FROM EXTERNAL PROVIDER`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Contained database users and Microsoft Entra security principals in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Adding the principal to `##MS_ServerStateReader##` grants server-wide `VIEW SERVER PERFORMANCE STATE` read access to DMVs while withholding user-table `SELECT` privileges.
- **B:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Adding the principal to `##MS_ServerStateReader##` grants server-wide `VIEW SERVER PERFORMANCE STATE` read access to DMVs while withholding user-table `SELECT` privileges.
- **C:** Correct. Modern granular server roles and state permissions let monitoring accounts inspect DMVs and metadata without granting `sysadmin`, `db_owner`, or `SELECT` access to user tables. In this scenario: Adding the principal to `##MS_ServerStateReader##` grants server-wide `VIEW SERVER PERFORMANCE STATE` read access to DMVs while withholding user-table `SELECT` privileges.
- **D:** Incorrect for this requirement. RLS transparently filters `SELECT`/`UPDATE`/`DELETE` rows via `FILTER PREDICATE` and blocks unauthorized cross-tenant `INSERT`/`UPDATE` writes via `BLOCK PREDICATE` inside the engine. Why the keyed choice wins: Adding the principal to `##MS_ServerStateReader##` grants server-wide `VIEW SERVER PERFORMANCE STATE` read access to DMVs while withholding user-table `SELECT` privileges.

### Question 18 — D

Answer: Stored procedure encapsulation using schema ownership chaining, `EXECUTE AS OWNER`, or certificate module signing. Keeping `Sales.usp_IssueRefund` and `Sales.RefundLedger` under the same schema owner (ownership chaining) or signing the procedure with a certificate and granting only `EXECUTE` enforces controlled DML without table permissions. Granting `EXECUTE` on a schema-owned or certificate-signed stored procedure lets callers run controlled DML/DDL workflows without direct table-level `SELECT`, `UPDATE`, or `IMPERSONATE` rights. Local study-map skill 2.4 (Apply Least Privilege Using Granular Server/Database Roles, Schema Chaining, `EXECUTE AS`, and T-SQL/GUI Tools), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Permissions hierarchy, server-level roles, and principle of least privilege in SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/security-server-roles).

- **A:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Keeping `Sales.usp_IssueRefund` and `Sales.RefundLedger` under the same schema owner (ownership chaining) or signing the procedure with a certificate and granting only `EXECUTE` enforces controlled DML without table permissions.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Keeping `Sales.usp_IssueRefund` and `Sales.RefundLedger` under the same schema owner (ownership chaining) or signing the procedure with a certificate and granting only `EXECUTE` enforces controlled DML without table permissions.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Keeping `Sales.usp_IssueRefund` and `Sales.RefundLedger` under the same schema owner (ownership chaining) or signing the procedure with a certificate and granting only `EXECUTE` enforces controlled DML without table permissions.
- **D:** Correct. Granting `EXECUTE` on a schema-owned or certificate-signed stored procedure lets callers run controlled DML/DDL workflows without direct table-level `SELECT`, `UPDATE`, or `IMPERSONATE` rights. In this scenario: Keeping `Sales.usp_IssueRefund` and `Sales.RefundLedger` under the same schema owner (ownership chaining) or signing the procedure with a certificate and granting only `EXECUTE` enforces controlled DML without table permissions.

### Question 19 — C

Answer: No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference. Dynamic Data Masking masks output columns only and does not block `WHERE` predicate probing (`Salary > 250000`), so ad-hoc query users can still infer exact values unless RLS or column permissions are used. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Local study-map skill 2.4 (Apply Least Privilege Using Granular Server/Database Roles, Schema Chaining, `EXECUTE AS`, and T-SQL/GUI Tools), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Permissions hierarchy, server-level roles, and principle of least privilege in SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/security-server-roles).

- **A:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: Dynamic Data Masking masks output columns only and does not block `WHERE` predicate probing (`Salary > 250000`), so ad-hoc query users can still infer exact values unless RLS or column permissions are used.
- **B:** Incorrect for this requirement. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Why the keyed choice wins: Dynamic Data Masking masks output columns only and does not block `WHERE` predicate probing (`Salary > 250000`), so ad-hoc query users can still infer exact values unless RLS or column permissions are used.
- **C:** Correct. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. In this scenario: Dynamic Data Masking masks output columns only and does not block `WHERE` predicate probing (`Salary > 250000`), so ad-hoc query users can still infer exact values unless RLS or column permissions are used.
- **D:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: Dynamic Data Masking masks output columns only and does not block `WHERE` predicate probing (`Salary > 250000`), so ad-hoc query users can still infer exact values unless RLS or column permissions are used.

### Question 20 — C

Answer: Remap orphaned database users (`ALTER USER [u] WITH LOGIN = [u]`) and inspect explicit `DENY` permissions via `sys.database_permissions`. Run `ALTER USER [promo_svc] WITH LOGIN = [promo_svc]` to relink the mismatched SID, and inspect `sys.database_permissions` for an explicit `DENY SELECT` on `Sales.Payouts` overriding `db_datareader`. Restoring a `.bak` onto another instance mismatches login SIDs (fixed via `ALTER USER ... WITH LOGIN`), while an explicit table/schema `DENY` always overrides `db_datareader` role `GRANT`s. Local study-map skill 2.5 (Troubleshoot Authentication and Authorization Issues (Orphaned Users `ALTER USER WITH LOGIN` & `DENY` Precedence)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot SQL login, orphaned user, and Microsoft Entra authorization issues (https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/troubleshoot-orphaned-users-sql-server).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Run `ALTER USER [promo_svc] WITH LOGIN = [promo_svc]` to relink the mismatched SID, and inspect `sys.database_permissions` for an explicit `DENY SELECT` on `Sales.Payouts` overriding `db_datareader`.
- **B:** Incorrect for this requirement. Microsoft Entra-only authentication disables legacy SQL Server logins (`sa` and password auth) completely, enforcing centralized MFA, Conditional Access, and token-based Managed Identities. Why the keyed choice wins: Run `ALTER USER [promo_svc] WITH LOGIN = [promo_svc]` to relink the mismatched SID, and inspect `sys.database_permissions` for an explicit `DENY SELECT` on `Sales.Payouts` overriding `db_datareader`.
- **C:** Correct. Restoring a `.bak` onto another instance mismatches login SIDs (fixed via `ALTER USER ... WITH LOGIN`), while an explicit table/schema `DENY` always overrides `db_datareader` role `GRANT`s. In this scenario: Run `ALTER USER [promo_svc] WITH LOGIN = [promo_svc]` to relink the mismatched SID, and inspect `sys.database_permissions` for an explicit `DENY SELECT` on `Sales.Payouts` overriding `db_datareader`.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Run `ALTER USER [promo_svc] WITH LOGIN = [promo_svc]` to relink the mismatched SID, and inspect `sys.database_permissions` for an explicit `DENY SELECT` on `Sales.Payouts` overriding `db_datareader`.

### Question 21 — A

Answer: Enable Soft Delete & Purge Protection on Key Vault → Assign Managed Identity to SQL server → Grant Key Vault Crypto Service Encryption User (`get`/`wrapKey`/`unwrapKey`) → Set server TDE protector to Key Vault key. Azure SQL CMK TDE requires enabling Soft Delete and Purge Protection on Key Vault first, assigning a Managed Identity to the SQL server, granting `get`/`wrapKey`/`unwrapKey` RBAC, and setting the TDE protector. Customer-Managed TDE requires Soft Delete and Purge Protection on Key Vault, a server Managed Identity granted `get`/`wrapKey`/`unwrapKey` permissions, and assigning the Key Vault key as TDE protector. Local study-map skill 2.6 (Implement Transparent Data Encryption (`TDE`) with Service-Managed Keys, Key Vault `CMK`, and VM Cert Backups), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Transparent Data Encryption (TDE) with service-managed and customer-managed keys in Key Vault (https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview).

- **A:** Correct. Customer-Managed TDE requires Soft Delete and Purge Protection on Key Vault, a server Managed Identity granted `get`/`wrapKey`/`unwrapKey` permissions, and assigning the Key Vault key as TDE protector. In this scenario: Azure SQL CMK TDE requires enabling Soft Delete and Purge Protection on Key Vault first, assigning a Managed Identity to the SQL server, granting `get`/`wrapKey`/`unwrapKey` RBAC, and setting the TDE protector.
- **B:** Incorrect for this requirement. Incorrect workflow: TDE CMK wraps the Database Encryption Key via asymmetric RSA keys in Azure Key Vault or Managed HSM, not `tempdb` symmetric keys. Why the keyed choice wins: Azure SQL CMK TDE requires enabling Soft Delete and Purge Protection on Key Vault first, assigning a Managed Identity to the SQL server, granting `get`/`wrapKey`/`unwrapKey` RBAC, and setting the TDE protector.
- **C:** Incorrect for this requirement. Incorrect workflow: Azure SQL refuses Key Vault TDE protectors unless Soft Delete and Purge Protection are enabled and key-wrapping permissions are granted beforehand. Why the keyed choice wins: Azure SQL CMK TDE requires enabling Soft Delete and Purge Protection on Key Vault first, assigning a Managed Identity to the SQL server, granting `get`/`wrapKey`/`unwrapKey` RBAC, and setting the TDE protector.
- **D:** Incorrect for this requirement. Incorrect workflow: Azure SQL CMK TDE integrates exclusively with Azure Key Vault or Azure Key Vault Managed HSM using Managed Identity, never anonymous storage URLs. Why the keyed choice wins: Azure SQL CMK TDE requires enabling Soft Delete and Purge Protection on Key Vault first, assigning a Managed Identity to the SQL server, granting `get`/`wrapKey`/`unwrapKey` RBAC, and setting the TDE protector.

### Question 22 — D, E

Answers: Enable both `Soft Delete` and `Purge Protection` on the Azure Key Vault or Managed HSM storing the TDE protector key; Grant the SQL server Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) on the Key Vault. Key Vault must have both `Soft Delete` and `Purge Protection` enabled, and the SQL server's Managed Identity must hold `get`, `wrapKey`, and `unwrapKey` key permissions. Local study-map skill 2.6 (Implement Transparent Data Encryption (`TDE`) with Service-Managed Keys, Key Vault `CMK`, and VM Cert Backups), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Transparent Data Encryption (TDE) with service-managed and customer-managed keys in Key Vault (https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Key Vault must have both `Soft Delete` and `Purge Protection` enabled, and the SQL server's Managed Identity must hold `get`, `wrapKey`, and `unwrapKey` key permissions.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Key Vault must have both `Soft Delete` and `Purge Protection` enabled, and the SQL server's Managed Identity must hold `get`, `wrapKey`, and `unwrapKey` key permissions.
- **C:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: Key Vault must have both `Soft Delete` and `Purge Protection` enabled, and the SQL server's Managed Identity must hold `get`, `wrapKey`, and `unwrapKey` key permissions.
- **D:** Correct. Azure SQL requires both Soft Delete and Purge Protection on Key Vault so accidental or malicious key deletion can never permanently brick encrypted databases. In this scenario: Key Vault must have both `Soft Delete` and `Purge Protection` enabled, and the SQL server's Managed Identity must hold `get`, `wrapKey`, and `unwrapKey` key permissions.
- **E:** Correct. The logical SQL server or SQL MI Managed Identity requires `get`, `wrapKey`, and `unwrapKey` permissions to wrap and unwrap the Database Encryption Key (`DEK`). In this scenario: Key Vault must have both `Soft Delete` and `Purge Protection` enabled, and the SQL server's Managed Identity must hold `get`, `wrapKey`, and `unwrapKey` key permissions.

### Question 23 — B

Answer: Column-level encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey`) plus `Minimal TLS version = 1.2`. T-SQL cell-level encryption (`EncryptByKey` / `DecryptByKey` backed by a database master key and certificate) encrypts specific columns in engine storage while `Minimal TLS version = 1.2` secures client transit. T-SQL cell-level symmetric key encryption protects specific columns inside the engine while enforcing TLS 1.2+ encrypts all TDS client traffic in transit. Local study-map skill 2.7 (Implement Object/Column-Level Encryption (`Symmetric Keys` / `Certificates`) and Enforce `Minimal TLS 1.2`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Column-level symmetric key encryption and TLS 1.2 in-transit encryption (https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/encrypt-a-column-of-data).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: T-SQL cell-level encryption (`EncryptByKey` / `DecryptByKey` backed by a database master key and certificate) encrypts specific columns in engine storage while `Minimal TLS version = 1.2` secures client transit.
- **B:** Correct. T-SQL cell-level symmetric key encryption protects specific columns inside the engine while enforcing TLS 1.2+ encrypts all TDS client traffic in transit. In this scenario: T-SQL cell-level encryption (`EncryptByKey` / `DecryptByKey` backed by a database master key and certificate) encrypts specific columns in engine storage while `Minimal TLS version = 1.2` secures client transit.
- **C:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: T-SQL cell-level encryption (`EncryptByKey` / `DecryptByKey` backed by a database master key and certificate) encrypts specific columns in engine storage while `Minimal TLS version = 1.2` secures client transit.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: T-SQL cell-level encryption (`EncryptByKey` / `DecryptByKey` backed by a database master key and certificate) encrypts specific columns in engine storage while `Minimal TLS version = 1.2` secures client transit.

### Question 24 — D

Answer: No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server. Server-level firewall rules live in the primary `master` database and do not replicate automatically to secondary logical servers; either mirror server rules on DR or create portable database-level rules via `sp_set_database_firewall_rule`. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Local study-map skill 2.8 (Configure Server-Level (`master`) vs Portable Database-Level IP Firewall Rules (`sp_set_database_firewall_rule`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Server-level and database-level IP firewall rules in Azure SQL Database (https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure).

- **A:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: Server-level firewall rules live in the primary `master` database and do not replicate automatically to secondary logical servers; either mirror server rules on DR or create portable database-level rules via `sp_set_database_firewall_rule`.
- **B:** Incorrect for this requirement. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. Why the keyed choice wins: Server-level firewall rules live in the primary `master` database and do not replicate automatically to secondary logical servers; either mirror server rules on DR or create portable database-level rules via `sp_set_database_firewall_rule`.
- **C:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: Server-level firewall rules live in the primary `master` database and do not replicate automatically to secondary logical servers; either mirror server rules on DR or create portable database-level rules via `sp_set_database_firewall_rule`.
- **D:** Correct. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. In this scenario: Server-level firewall rules live in the primary `master` database and do not replicate automatically to secondary logical servers; either mirror server rules on DR or create portable database-level rules via `sp_set_database_firewall_rule`.

### Question 25 — B, D

Answers: Provision a Column Master Key in Key Vault and create a Column Encryption Key with `ENCLAVE_COMPUTATIONS` enabled; Enable `Column Encryption Setting=Enabled` and pass the `Enclave Attestation Url` (or VBS zero-attestation setting) in client drivers. Enclave-enabled Always Encrypted requires creating a CEK with `ENCLAVE_COMPUTATIONS` backed by a Key Vault CMK and enabling `Column Encryption Setting=Enabled` with enclave attestation in client connection strings. Local study-map skill 2.9 (Implement Always Encrypted (`Deterministic` vs `Randomized`) and Always Encrypted with VBS/SGX Secure Enclaves), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always Encrypted and Always Encrypted with secure enclaves (https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Enclave-enabled Always Encrypted requires creating a CEK with `ENCLAVE_COMPUTATIONS` backed by a Key Vault CMK and enabling `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.
- **B:** Correct. Client drivers must enable Always Encrypted and verify enclave attestation before transmitting CEKs over TLS into the SQL secure enclave. In this scenario: Enclave-enabled Always Encrypted requires creating a CEK with `ENCLAVE_COMPUTATIONS` backed by a Key Vault CMK and enabling `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.
- **C:** Incorrect for this requirement. `ReadOnly` host caching serves random OLTP data-page reads directly from Azure hypervisor RAM/SSD cache without consuming disk IOPS. Why the keyed choice wins: Enclave-enabled Always Encrypted requires creating a CEK with `ENCLAVE_COMPUTATIONS` backed by a Key Vault CMK and enabling `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.
- **D:** Correct. Rich confidential queries (`LIKE`, `<`, `>`, sorting) and in-place encryption require a CEK explicitly marked to permit enclave computations. In this scenario: Enclave-enabled Always Encrypted requires creating a CEK with `ENCLAVE_COMPUTATIONS` backed by a Key Vault CMK and enabling `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.
- **E:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Enclave-enabled Always Encrypted requires creating a CEK with `ENCLAVE_COMPUTATIONS` backed by a Key Vault CMK and enabling `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.

### Question 26 — D, E

Answers: Link Private DNS Zone `privatelink.database.windows.net` (or forward on-premises DNS) to resolve `<server>.database.windows.net` to the private IP; Set `Public network access = Disabled` (`publicNetworkAccess: Disabled`) on the logical SQL server so internet connections are rejected. You must link `privatelink.database.windows.net` Private DNS so VNet clients resolve the private IP and set `Public network access = Disabled` on the logical SQL server to block internet endpoints. Local study-map skill 2.10 (Configure Azure Private Link (`privatelink.database.windows.net`), Service Endpoints, and SQL MI Subnet Security), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure Private Link, Virtual Network service endpoints, and SQL MI VNet security (https://learn.microsoft.com/en-us/azure/azure-sql/database/private-endpoint-overview).

- **A:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: You must link `privatelink.database.windows.net` Private DNS so VNet clients resolve the private IP and set `Public network access = Disabled` on the logical SQL server to block internet endpoints.
- **B:** Incorrect for this requirement. Azure Arc allows variable-workload or seasonal SQL Server hosts outside Azure to be billed hourly through an Azure subscription. Why the keyed choice wins: You must link `privatelink.database.windows.net` Private DNS so VNet clients resolve the private IP and set `Public network access = Disabled` on the logical SQL server to block internet endpoints.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: You must link `privatelink.database.windows.net` Private DNS so VNet clients resolve the private IP and set `Public network access = Disabled` on the logical SQL server to block internet endpoints.
- **D:** Correct. Clients still validate the TLS certificate for `<server>.database.windows.net`, so split-brain DNS must map the canonical FQDN via CNAME to `privatelink.database.windows.net`. In this scenario: You must link `privatelink.database.windows.net` Private DNS so VNet clients resolve the private IP and set `Public network access = Disabled` on the logical SQL server to block internet endpoints.
- **E:** Correct. Creating a Private Endpoint alone leaves the public endpoint reachable unless `Public network access` is explicitly disabled on the server. In this scenario: You must link `privatelink.database.windows.net` Private DNS so VNet clients resolve the private IP and set `Public network access = Disabled` on the logical SQL server to block internet endpoints.

### Question 27 — C

Answer: SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage. Combining `ADD SENSITIVITY CLASSIFICATION` with Azure SQL Auditing to Log Analytics automatically populates `data_sensitivity_information` in `AzureDiagnostics` whenever classified columns are read. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. Local study-map skill 2.11 (Apply SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) and Server/Database Auditing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Data Discovery and Classification and Azure SQL Auditing (https://learn.microsoft.com/en-us/azure/azure-sql/database/auditing-overview).

- **A:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Combining `ADD SENSITIVITY CLASSIFICATION` with Azure SQL Auditing to Log Analytics automatically populates `data_sensitivity_information` in `AzureDiagnostics` whenever classified columns are read.
- **B:** Incorrect for this requirement. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. Why the keyed choice wins: Combining `ADD SENSITIVITY CLASSIFICATION` with Azure SQL Auditing to Log Analytics automatically populates `data_sensitivity_information` in `AzureDiagnostics` whenever classified columns are read.
- **C:** Correct. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. In this scenario: Combining `ADD SENSITIVITY CLASSIFICATION` with Azure SQL Auditing to Log Analytics automatically populates `data_sensitivity_information` in `AzureDiagnostics` whenever classified columns are read.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Combining `ADD SENSITIVITY CLASSIFICATION` with Azure SQL Auditing to Log Analytics automatically populates `data_sensitivity_information` in `AzureDiagnostics` whenever classified columns are read.

### Question 28 — B

Answer: SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage. Authenticating Azure SQL Auditing via Managed Identity (`Storage Blob Data Contributor`) to an immutable Blob container prevents key-rotation outages and protects audit trails from tampering. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. Local study-map skill 2.11 (Apply SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) and Server/Database Auditing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Data Discovery and Classification and Azure SQL Auditing (https://learn.microsoft.com/en-us/azure/azure-sql/database/auditing-overview).

- **A:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Authenticating Azure SQL Auditing via Managed Identity (`Storage Blob Data Contributor`) to an immutable Blob container prevents key-rotation outages and protects audit trails from tampering.
- **B:** Correct. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. In this scenario: Authenticating Azure SQL Auditing via Managed Identity (`Storage Blob Data Contributor`) to an immutable Blob container prevents key-rotation outages and protects audit trails from tampering.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Authenticating Azure SQL Auditing via Managed Identity (`Storage Blob Data Contributor`) to an immutable Blob container prevents key-rotation outages and protects audit trails from tampering.
- **D:** Incorrect for this requirement. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. Why the keyed choice wins: Authenticating Azure SQL Auditing via Managed Identity (`Storage Blob Data Contributor`) to an immutable Blob container prevents key-rotation outages and protects audit trails from tampering.

### Question 29 — D

Answer: Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history. Change Tracking (`CHANGETABLE(CHANGES ...)`) tracks net row changes synchronously with lightweight storage overhead, unlike CDC which archives every intermediate before/after row image. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. Local study-map skill 2.12 (Implement Change Tracking (`CHANGETABLE`) vs Change Data Capture (`CDC`) for Downstream Data Changes), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Track data changes with Change Tracking (CT) and Change Data Capture (CDC) (https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/track-data-changes-sql-server).

- **A:** Incorrect for this requirement. CDC requires `S3+` or `vCore` tiers in Azure SQL Database, and Change Tracking stores only net version numbers/PKs—never intermediate before/after column values. Why the keyed choice wins: Change Tracking (`CHANGETABLE(CHANGES ...)`) tracks net row changes synchronously with lightweight storage overhead, unlike CDC which archives every intermediate before/after row image.
- **B:** Incorrect for this requirement. SQL Ledger chains transactional Merkle-tree hashes into tamper-evident blocks stored externally in Azure Confidential Ledger or WORM Blob storage to prove cryptographic integrity to auditors. Why the keyed choice wins: Change Tracking (`CHANGETABLE(CHANGES ...)`) tracks net row changes synchronously with lightweight storage overhead, unlike CDC which archives every intermediate before/after row image.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Change Tracking (`CHANGETABLE(CHANGES ...)`) tracks net row changes synchronously with lightweight storage overhead, unlike CDC which archives every intermediate before/after row image.
- **D:** Correct. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. In this scenario: Change Tracking (`CHANGETABLE(CHANGES ...)`) tracks net row changes synchronously with lightweight storage overhead, unlike CDC which archives every intermediate before/after row image.

### Question 30 — B

Answer: Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas. Dynamic Data Masking's built-in `email()` function formats addresses as `aXXX@XXXX.com` for standard callers while `GRANT UNMASK TO [FraudLeads]` reveals cleartext to authorized supervisors. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Local study-map skill 2.13 (Implement Dynamic Data Masking (`default`, `email`, `partial`, `random`) and Scoped `UNMASK` Permissions), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Dynamic Data Masking (DDM) in Azure SQL Database, SQL Managed Instance, and SQL Server (https://learn.microsoft.com/en-us/azure/azure-sql/database/dynamic-data-masking-overview).

- **A:** Incorrect for this requirement. BYOK TDE wraps the symmetric Database Encryption Key (`DEK`) with an asymmetric RSA key in Key Vault or Managed HSM so security admins control key rotation and instant revocation. Why the keyed choice wins: Dynamic Data Masking's built-in `email()` function formats addresses as `aXXX@XXXX.com` for standard callers while `GRANT UNMASK TO [FraudLeads]` reveals cleartext to authorized supervisors.
- **B:** Correct. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. In this scenario: Dynamic Data Masking's built-in `email()` function formats addresses as `aXXX@XXXX.com` for standard callers while `GRANT UNMASK TO [FraudLeads]` reveals cleartext to authorized supervisors.
- **C:** Incorrect for this requirement. RLS transparently filters `SELECT`/`UPDATE`/`DELETE` rows via `FILTER PREDICATE` and blocks unauthorized cross-tenant `INSERT`/`UPDATE` writes via `BLOCK PREDICATE` inside the engine. Why the keyed choice wins: Dynamic Data Masking's built-in `email()` function formats addresses as `aXXX@XXXX.com` for standard callers while `GRANT UNMASK TO [FraudLeads]` reveals cleartext to authorized supervisors.
- **D:** Incorrect for this requirement. Secure enclaves delegate column decryption into an isolated memory region inside SQL, unlocking `LIKE`, `<`, `>`, `ORDER BY`, and fast in-place initial encryption without exposing plaintext to DBAs. Why the keyed choice wins: Dynamic Data Masking's built-in `email()` function formats addresses as `aXXX@XXXX.com` for standard callers while `GRANT UNMASK TO [FraudLeads]` reveals cleartext to authorized supervisors.

### Question 31 — B

Answer: Create dedicated `Security` schema → Create `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT(N'TenantId')` → Create `SECURITY POLICY` with `FILTER` & `BLOCK` predicates (`STATE = ON`) → Set read-only `sp_set_session_context` on connect. Create a separate `Security` schema, define a `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT`, bind `FILTER` and `BLOCK` predicates in a `SECURITY POLICY`, and set read-only `sp_set_session_context` on connection open. Best-practice multi-tenant RLS isolates objects in a dedicated schema, uses a schema-bound inline TVF predicate over read-only `SESSION_CONTEXT`, and enforces both `FILTER` and `BLOCK` predicates. Local study-map skill 2.14 (Implement Cryptographic Ledger in Azure SQL (`Azure Confidential Ledger`) and Row-Level Security (`FILTER`/`BLOCK`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Ledger cryptographic tamper-evidence and Row-Level Security (RLS) in Azure SQL (https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-overview).

- **A:** Incorrect for this requirement. Incorrect workflow: Dynamic Data Masking obfuscates column output in result sets and never filters rows or blocks cross-tenant writes. Why the keyed choice wins: Create a separate `Security` schema, define a `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT`, bind `FILTER` and `BLOCK` predicates in a `SECURITY POLICY`, and set read-only `sp_set_session_context` on connection open.
- **B:** Correct. Best-practice multi-tenant RLS isolates objects in a dedicated schema, uses a schema-bound inline TVF predicate over read-only `SESSION_CONTEXT`, and enforces both `FILTER` and `BLOCK` predicates. In this scenario: Create a separate `Security` schema, define a `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT`, bind `FILTER` and `BLOCK` predicates in a `SECURITY POLICY`, and set read-only `sp_set_session_context` on connection open.
- **C:** Incorrect for this requirement. Incorrect workflow: RLS requires an existing `SCHEMABINDING` inline TVF before creating the security policy, and granting `ALTER ANY SECURITY POLICY` lets tenants bypass isolation. Why the keyed choice wins: Create a separate `Security` schema, define a `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT`, bind `FILTER` and `BLOCK` predicates in a `SECURITY POLICY`, and set read-only `sp_set_session_context` on connection open.
- **D:** Incorrect for this requirement. Incorrect workflow: RLS predicates must be schema-bound inline TVFs attached to a `SECURITY POLICY`, and `@read_only = 1` prevents SQL injection from changing `TenantId` mid-session. Why the keyed choice wins: Create a separate `Security` schema, define a `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT`, bind `FILTER` and `BLOCK` predicates in a `SECURITY POLICY`, and set read-only `sp_set_session_context` on connection open.

### Question 32 — A

Answer: Azure Monitor metrics paired with `sys.dm_db_resource_stats` (single DB) or `sys.server_resource_stats` (SQL MI) for 15-second CPU, data I/O, log write, and memory baselines. In Azure SQL Database, `sys.dm_db_resource_stats` captures 15-second resource utilization snapshots retained for 14 days (while `sys.server_resource_stats` provides the equivalent on SQL Managed Instance). `sys.dm_db_resource_stats` retains 14 days of 15-second resource averages (`avg_cpu_percent`, `avg_data_io_percent`, `avg_log_write_percent`) to compare current peaks against normal baselines. Local study-map skill 3.1 (Establish Performance Baselines and Interpret CPU, Memory, Data I/O, Log Write, and `tempdb` Metrics), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL resource utilization and establish performance baselines (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-sql-database-azure-monitor).

- **A:** Correct. `sys.dm_db_resource_stats` retains 14 days of 15-second resource averages (`avg_cpu_percent`, `avg_data_io_percent`, `avg_log_write_percent`) to compare current peaks against normal baselines. In this scenario: In Azure SQL Database, `sys.dm_db_resource_stats` captures 15-second resource utilization snapshots retained for 14 days (while `sys.server_resource_stats` provides the equivalent on SQL Managed Instance).
- **B:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: In Azure SQL Database, `sys.dm_db_resource_stats` captures 15-second resource utilization snapshots retained for 14 days (while `sys.server_resource_stats` provides the equivalent on SQL Managed Instance).
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: In Azure SQL Database, `sys.dm_db_resource_stats` captures 15-second resource utilization snapshots retained for 14 days (while `sys.server_resource_stats` provides the equivalent on SQL Managed Instance).
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: In Azure SQL Database, `sys.dm_db_resource_stats` captures 15-second resource utilization snapshots retained for 14 days (while `sys.server_resource_stats` provides the equivalent on SQL Managed Instance).

### Question 33 — C

Answer: Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`. High `PAGEIOLATCH_SH` waits indicate sessions are stalling while reading data pages from storage into the buffer pool—typically caused by missing indexes, large table scans, or undersized storage IOPS/RAM. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. Local study-map skill 3.1 (Establish Performance Baselines and Interpret CPU, Memory, Data I/O, Log Write, and `tempdb` Metrics), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL resource utilization and establish performance baselines (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-sql-database-azure-monitor).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: High `PAGEIOLATCH_SH` waits indicate sessions are stalling while reading data pages from storage into the buffer pool—typically caused by missing indexes, large table scans, or undersized storage IOPS/RAM.
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: High `PAGEIOLATCH_SH` waits indicate sessions are stalling while reading data pages from storage into the buffer pool—typically caused by missing indexes, large table scans, or undersized storage IOPS/RAM.
- **C:** Correct. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. In this scenario: High `PAGEIOLATCH_SH` waits indicate sessions are stalling while reading data pages from storage into the buffer pool—typically caused by missing indexes, large table scans, or undersized storage IOPS/RAM.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: High `PAGEIOLATCH_SH` waits indicate sessions are stalling while reading data pages from storage into the buffer pool—typically caused by missing indexes, large table scans, or undersized storage IOPS/RAM.

### Question 34 — A

Answer: Azure Monitor Diagnostic Settings streaming `SQLInsights`, `QueryStoreRuntimeStatistics`, `Errors`, and `Blocks` to a Log Analytics workspace (`KQL`). Enabling `SQLInsights` in Azure Monitor Diagnostic Settings exports SQL Intelligent Insights anomaly detections and root-cause JSON records into Log Analytics. Diagnostic Settings export telemetry across hundreds of databases into Log Analytics so DBAs can correlate `SQLInsights`, wait stats, deadlocks, and timeouts via KQL queries and alerts. Local study-map skill 3.2 (Configure Azure Monitor Diagnostic Settings (`SQLInsights`, `AzureDiagnostics` KQL) and Resource Monitoring), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure Monitor diagnostic settings, SQLInsights logs, and metric alerts (https://learn.microsoft.com/en-us/azure/azure-sql/database/metrics-diagnostic-telemetry-logging-streaming-export-configure).

- **A:** Correct. Diagnostic Settings export telemetry across hundreds of databases into Log Analytics so DBAs can correlate `SQLInsights`, wait stats, deadlocks, and timeouts via KQL queries and alerts. In this scenario: Enabling `SQLInsights` in Azure Monitor Diagnostic Settings exports SQL Intelligent Insights anomaly detections and root-cause JSON records into Log Analytics.
- **B:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Enabling `SQLInsights` in Azure Monitor Diagnostic Settings exports SQL Intelligent Insights anomaly detections and root-cause JSON records into Log Analytics.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Enabling `SQLInsights` in Azure Monitor Diagnostic Settings exports SQL Intelligent Insights anomaly detections and root-cause JSON records into Log Analytics.
- **D:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Enabling `SQLInsights` in Azure Monitor Diagnostic Settings exports SQL Intelligent Insights anomaly detections and root-cause JSON records into Log Analytics.

### Question 35 — B

Answer: Provision Azure Data Explorer or Fabric Eventhouse store → Create database watcher with Managed Identity → Add SQL targets & grant `VIEW SERVER PERFORMANCE STATE` + ingest roles → Start watcher & open portal dashboards. Provision an Azure Data Explorer or Fabric Eventhouse KQL store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets plus store ingest roles, and start the watcher. Database watcher streams SQL telemetry into an Azure Data Explorer or Fabric Eventhouse/KQL store using Managed Identity granted least-privilege `VIEW SERVER PERFORMANCE STATE` on SQL targets. Local study-map skill 3.3 (Monitor Workloads Using Database Watcher (ADX / Fabric Eventhouse) and Plan Fabric Database Hub Transition), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL workloads with database watcher and Database Hub in Microsoft Fabric (https://learn.microsoft.com/en-us/azure/azure-sql/database-watcher-overview).

- **A:** Incorrect for this requirement. Incorrect workflow: database watcher monitors Azure SQL Database, Elastic Pools, and SQL Managed Instance and stores telemetry in Azure Data Explorer or Fabric KQL databases. Why the keyed choice wins: Provision an Azure Data Explorer or Fabric Eventhouse KQL store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets plus store ingest roles, and start the watcher.
- **B:** Correct. Database watcher streams SQL telemetry into an Azure Data Explorer or Fabric Eventhouse/KQL store using Managed Identity granted least-privilege `VIEW SERVER PERFORMANCE STATE` on SQL targets. In this scenario: Provision an Azure Data Explorer or Fabric Eventhouse KQL store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets plus store ingest roles, and start the watcher.
- **C:** Incorrect for this requirement. Incorrect workflow: Azure SQL Database PaaS exposes no underlying OS for agents, `sp_trace_create` is deprecated, and database watcher is agentless. Why the keyed choice wins: Provision an Azure Data Explorer or Fabric Eventhouse KQL store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets plus store ingest roles, and start the watcher.
- **D:** Incorrect for this requirement. Incorrect workflow: watcher requires an Azure Data Explorer or Fabric Real-Time Analytics store and SQL targets configured first, and uses least-privilege Managed Identity rather than `sa` or Profiler. Why the keyed choice wins: Provision an Azure Data Explorer or Fabric Eventhouse KQL store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets plus store ingest roles, and start the watcher.

### Question 36 — B, D

Answers: Grant the database watcher Managed Identity `VIEW SERVER PERFORMANCE STATE` (or `VIEW DATABASE PERFORMANCE STATE`) on SQL targets; Grant the database watcher Managed Identity database `Admin` / ingest permissions on the Azure Data Explorer or Fabric Eventhouse store. The watcher's Managed Identity needs `VIEW SERVER PERFORMANCE STATE` on monitored Azure SQL targets and database `Admin`/ingestion permissions on the target Azure Data Explorer or Fabric Eventhouse database. Local study-map skill 3.3 (Monitor Workloads Using Database Watcher (ADX / Fabric Eventhouse) and Plan Fabric Database Hub Transition), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL workloads with database watcher and Database Hub in Microsoft Fabric (https://learn.microsoft.com/en-us/azure/azure-sql/database-watcher-overview).

- **A:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: The watcher's Managed Identity needs `VIEW SERVER PERFORMANCE STATE` on monitored Azure SQL targets and database `Admin`/ingestion permissions on the target Azure Data Explorer or Fabric Eventhouse database.
- **B:** Correct. Database watcher collects DMVs and system catalogs using least-privilege performance-state permissions rather than `sysadmin` or data-read rights. In this scenario: The watcher's Managed Identity needs `VIEW SERVER PERFORMANCE STATE` on monitored Azure SQL targets and database `Admin`/ingestion permissions on the target Azure Data Explorer or Fabric Eventhouse database.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: The watcher's Managed Identity needs `VIEW SERVER PERFORMANCE STATE` on monitored Azure SQL targets and database `Admin`/ingestion permissions on the target Azure Data Explorer or Fabric Eventhouse database.
- **D:** Correct. Database watcher creates tables, retention policies, and ingestion mappings inside the target Azure Data Explorer or Fabric Real-Time Analytics KQL database. In this scenario: The watcher's Managed Identity needs `VIEW SERVER PERFORMANCE STATE` on monitored Azure SQL targets and database `Admin`/ingestion permissions on the target Azure Data Explorer or Fabric Eventhouse database.
- **E:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: The watcher's Managed Identity needs `VIEW SERVER PERFORMANCE STATE` on monitored Azure SQL targets and database `Admin`/ingestion permissions on the target Azure Data Explorer or Fabric Eventhouse database.

### Question 37 — A, B

Answers: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE` with `rwl` permissions) for the Azure Blob container; Define `CREATE EVENT SESSION ... ON DATABASE ADD TARGET package0.event_file(SET filename = N'https://...xel')` and start the session. Persistent Extended Events in Azure SQL Database require a `DATABASE SCOPED CREDENTIAL` (`rwl` rights on Blob Storage) and `CREATE EVENT SESSION ... ON DATABASE` targeting `package0.event_file`. Local study-map skill 3.4 (Monitor Workloads Using Extended Events (`ON DATABASE` vs `ON SERVER` & Persistent Blob `event_file` Targets)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Extended Events in Azure SQL Database and Azure SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/xevent-db-diff-from-svr).

- **A:** Correct. Azure SQL Database scopes Extended Event sessions `ON DATABASE` and streams persistent `.xel` ring-rotated files to the Blob container URL. In this scenario: Persistent Extended Events in Azure SQL Database require a `DATABASE SCOPED CREDENTIAL` (`rwl` rights on Blob Storage) and `CREATE EVENT SESSION ... ON DATABASE` targeting `package0.event_file`.
- **B:** Correct. Extended Events in Azure SQL Database requires a `DATABASE SCOPED CREDENTIAL` with Read, Write, and List rights on the target Blob Storage container. In this scenario: Persistent Extended Events in Azure SQL Database require a `DATABASE SCOPED CREDENTIAL` (`rwl` rights on Blob Storage) and `CREATE EVENT SESSION ... ON DATABASE` targeting `package0.event_file`.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Persistent Extended Events in Azure SQL Database require a `DATABASE SCOPED CREDENTIAL` (`rwl` rights on Blob Storage) and `CREATE EVENT SESSION ... ON DATABASE` targeting `package0.event_file`.
- **D:** Incorrect for this requirement. Azure SQL requires both Soft Delete and Purge Protection on Key Vault so accidental or malicious key deletion can never permanently brick encrypted databases. Why the keyed choice wins: Persistent Extended Events in Azure SQL Database require a `DATABASE SCOPED CREDENTIAL` (`rwl` rights on Blob Storage) and `CREATE EVENT SESSION ... ON DATABASE` targeting `package0.event_file`.
- **E:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Persistent Extended Events in Azure SQL Database require a `DATABASE SCOPED CREDENTIAL` (`rwl` rights on Blob Storage) and `CREATE EVENT SESSION ... ON DATABASE` targeting `package0.event_file`.

### Question 38 — D

Answer: Extended Events (`CREATE EVENT SESSION ... ON DATABASE` in SQL DB or `ON SERVER` in SQL MI/VMs) writing to an `event_file` target in Azure Blob Storage. Single Azure SQL Databases scope Extended Events sessions with `ON DATABASE`, whereas Azure SQL Managed Instance and SQL Server on Azure VMs use server-scoped `ON SERVER` sessions. Unlike ephemeral in-memory `ring_buffer` targets, the `event_file` target persists `.xel` trace files durably in Azure Blob Storage using a database-scoped credential (Managed Identity or SAS). Local study-map skill 3.4 (Monitor Workloads Using Extended Events (`ON DATABASE` vs `ON SERVER` & Persistent Blob `event_file` Targets)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Extended Events in Azure SQL Database and Azure SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/xevent-db-diff-from-svr).

- **A:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Single Azure SQL Databases scope Extended Events sessions with `ON DATABASE`, whereas Azure SQL Managed Instance and SQL Server on Azure VMs use server-scoped `ON SERVER` sessions.
- **B:** Incorrect for this requirement. Automatic Tuning continuously monitors Query Store, automatically forces prior plans when regressions occur, creates validated missing nonclustered indexes, and removes unused duplicate indexes. Why the keyed choice wins: Single Azure SQL Databases scope Extended Events sessions with `ON DATABASE`, whereas Azure SQL Managed Instance and SQL Server on Azure VMs use server-scoped `ON SERVER` sessions.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Single Azure SQL Databases scope Extended Events sessions with `ON DATABASE`, whereas Azure SQL Managed Instance and SQL Server on Azure VMs use server-scoped `ON SERVER` sessions.
- **D:** Correct. Unlike ephemeral in-memory `ring_buffer` targets, the `event_file` target persists `.xel` trace files durably in Azure Blob Storage using a database-scoped credential (Managed Identity or SAS). In this scenario: Single Azure SQL Databases scope Extended Events sessions with `ON DATABASE`, whereas Azure SQL Managed Instance and SQL Server on Azure VMs use server-scoped `ON SERVER` sessions.

### Question 39 — B

Answer: Confirm Query Store is `READ_WRITE` with wait capture → Compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`) → Force prior plan via `sp_query_store_force_plan` → Monitor `force_failure_count` & latency. Confirm Query Store is `READ_WRITE` with wait capture, compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`), force the prior good `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`. Resolving a parameter-sensitive plan regression uses Query Store runtime/wait history to identify the prior known-good `plan_id`, forces it immediately without code changes, and verifies forcing health. Local study-map skill 3.5 (Configure and Monitor Query Store, Force Regressed Plans (`sp_query_store_force_plan`), and Set Query Store Hints), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance by using the Query Store, plan forcing, and Query Store hints (https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store).

- **A:** Incorrect for this requirement. Incorrect workflow: restarting SQL or running offline index rebuilds causes severe production outage and does not prevent parameter-sensitive plan regressions. Why the keyed choice wins: Confirm Query Store is `READ_WRITE` with wait capture, compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`), force the prior good `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`.
- **B:** Correct. Resolving a parameter-sensitive plan regression uses Query Store runtime/wait history to identify the prior known-good `plan_id`, forces it immediately without code changes, and verifies forcing health. In this scenario: Confirm Query Store is `READ_WRITE` with wait capture, compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`), force the prior good `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`.
- **C:** Incorrect for this requirement. Incorrect workflow: purging Query Store erases the historical baseline and prior good plan needed to diagnose and force the healthy execution plan. Why the keyed choice wins: Confirm Query Store is `READ_WRITE` with wait capture, compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`), force the prior good `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`.
- **D:** Incorrect for this requirement. Incorrect workflow: system catalog tables cannot be updated directly and flushing the plan cache every minute spikes CPU compilations across the entire workload. Why the keyed choice wins: Confirm Query Store is `READ_WRITE` with wait capture, compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`), force the prior good `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`.

### Question 40 — D

Answer: Capture `xml_deadlock_report` via Extended Events or `sys.event_log`, align table modification order across transactions, and add covering indexes. Inspecting `database_xml_deadlock_report` / `xml_deadlock_report` graphs and refactoring both procedures to acquire locks on `Inventory` and `Coupons` in identical order with covering indexes eliminates cycle deadlocks. Cycle deadlocks (`Error 1205`) occur when concurrent transactions lock objects in opposite order or scan wide ranges; accessing tables in identical order with narrow index seeks eliminates cycles. Local study-map skill 3.6 (Identify and Resolve Session Blocking (`RCSI`, `Optimized Locking` `TID`/`LAQ`) and Deadlocks (`xml_deadlock_report`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Understand and resolve Azure SQL blocking problems, deadlocks, RCSI, and Optimized Locking (https://learn.microsoft.com/en-us/azure/azure-sql/database/analyze-prevent-deadlocks).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Inspecting `database_xml_deadlock_report` / `xml_deadlock_report` graphs and refactoring both procedures to acquire locks on `Inventory` and `Coupons` in identical order with covering indexes eliminates cycle deadlocks.
- **B:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Inspecting `database_xml_deadlock_report` / `xml_deadlock_report` graphs and refactoring both procedures to acquire locks on `Inventory` and `Coupons` in identical order with covering indexes eliminates cycle deadlocks.
- **C:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Inspecting `database_xml_deadlock_report` / `xml_deadlock_report` graphs and refactoring both procedures to acquire locks on `Inventory` and `Coupons` in identical order with covering indexes eliminates cycle deadlocks.
- **D:** Correct. Cycle deadlocks (`Error 1205`) occur when concurrent transactions lock objects in opposite order or scan wide ranges; accessing tables in identical order with narrow index seeks eliminates cycles. In this scenario: Inspecting `database_xml_deadlock_report` / `xml_deadlock_report` graphs and refactoring both procedures to acquire locks on `Inventory` and `Coupons` in identical order with covering indexes eliminates cycle deadlocks.

### Question 41 — C

Answer: Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`. Joining `sys.dm_exec_requests` (`blocking_session_id`), `sys.dm_exec_sessions`, and `sys.dm_tran_locks` identifies the head blocker session whose `blocking_session_id = 0` while blocking active waiters. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. Local study-map skill 3.7 (Identify Performance Bottlenecks Using Dynamic Management Views (`sys.dm_os_wait_stats`, `sys.dm_exec_requests`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance using Dynamic Management Views (DMVs) and wait statistics (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-with-dmvs).

- **A:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Joining `sys.dm_exec_requests` (`blocking_session_id`), `sys.dm_exec_sessions`, and `sys.dm_tran_locks` identifies the head blocker session whose `blocking_session_id = 0` while blocking active waiters.
- **B:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Joining `sys.dm_exec_requests` (`blocking_session_id`), `sys.dm_exec_sessions`, and `sys.dm_tran_locks` identifies the head blocker session whose `blocking_session_id = 0` while blocking active waiters.
- **C:** Correct. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. In this scenario: Joining `sys.dm_exec_requests` (`blocking_session_id`), `sys.dm_exec_sessions`, and `sys.dm_tran_locks` identifies the head blocker session whose `blocking_session_id = 0` while blocking active waiters.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Joining `sys.dm_exec_requests` (`blocking_session_id`), `sys.dm_exec_sessions`, and `sys.dm_tran_locks` identifies the head blocker session whose `blocking_session_id = 0` while blocking active waiters.

### Question 42 — A

Answer: Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`. `sys.dm_db_tempdb_space_usage` (alongside `sys.dm_db_session_space_usage` and `sys.dm_db_task_space_usage`) pinpoints whether user temp tables, hash/sort spills, or RCSI version stores consume `tempdb`. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. Local study-map skill 3.7 (Identify Performance Bottlenecks Using Dynamic Management Views (`sys.dm_os_wait_stats`, `sys.dm_exec_requests`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance using Dynamic Management Views (DMVs) and wait statistics (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-with-dmvs).

- **A:** Correct. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. In this scenario: `sys.dm_db_tempdb_space_usage` (alongside `sys.dm_db_session_space_usage` and `sys.dm_db_task_space_usage`) pinpoints whether user temp tables, hash/sort spills, or RCSI version stores consume `tempdb`.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `sys.dm_db_tempdb_space_usage` (alongside `sys.dm_db_session_space_usage` and `sys.dm_db_task_space_usage`) pinpoints whether user temp tables, hash/sort spills, or RCSI version stores consume `tempdb`.
- **C:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: `sys.dm_db_tempdb_space_usage` (alongside `sys.dm_db_session_space_usage` and `sys.dm_db_task_space_usage`) pinpoints whether user temp tables, hash/sort spills, or RCSI version stores consume `tempdb`.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: `sys.dm_db_tempdb_space_usage` (alongside `sys.dm_db_session_space_usage` and `sys.dm_db_task_space_usage`) pinpoints whether user temp tables, hash/sort spills, or RCSI version stores consume `tempdb`.

### Question 43 — A

Answer: Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions. Rewrite the date filter as a SARGable range (`OrderDate >= '2026-01-01' AND OrderDate < '2027-01-01'`), match parameter type `VARCHAR(20)` to prevent implicit conversion, and create a covering index with `INCLUDE (TotalAmt)`. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. Local study-map skill 3.8 (Design Covering/Filtered/Columnstore Indexes and Rewrite Non-SARGable or Implicit-Conversion T-SQL Constructs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server and Azure SQL index design guide and SARGable T-SQL tuning (https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide).

- **A:** Correct. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. In this scenario: Rewrite the date filter as a SARGable range (`OrderDate >= '2026-01-01' AND OrderDate < '2027-01-01'`), match parameter type `VARCHAR(20)` to prevent implicit conversion, and create a covering index with `INCLUDE (TotalAmt)`.
- **B:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Rewrite the date filter as a SARGable range (`OrderDate >= '2026-01-01' AND OrderDate < '2027-01-01'`), match parameter type `VARCHAR(20)` to prevent implicit conversion, and create a covering index with `INCLUDE (TotalAmt)`.
- **C:** Incorrect for this requirement. Row-by-row cursors and multi-statement TVFs under legacy compatibility levels execute thousands of iterative context switches and 1-row cardinality guesses. Why the keyed choice wins: Rewrite the date filter as a SARGable range (`OrderDate >= '2026-01-01' AND OrderDate < '2027-01-01'`), match parameter type `VARCHAR(20)` to prevent implicit conversion, and create a covering index with `INCLUDE (TotalAmt)`.
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Rewrite the date filter as a SARGable range (`OrderDate >= '2026-01-01' AND OrderDate < '2027-01-01'`), match parameter type `VARCHAR(20)` to prevent implicit conversion, and create a covering index with `INCLUDE (TotalAmt)`.

### Question 44 — D

Answer: Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions. A filtered nonclustered index (`CREATE NONCLUSTERED INDEX IX_LiveShipments ON Shipments(WarehouseId) INCLUDE (...) WHERE IsArchived = 0`) indexes only active unarchived rows, slashing storage and DML maintenance overhead. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. Local study-map skill 3.8 (Design Covering/Filtered/Columnstore Indexes and Rewrite Non-SARGable or Implicit-Conversion T-SQL Constructs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server and Azure SQL index design guide and SARGable T-SQL tuning (https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: A filtered nonclustered index (`CREATE NONCLUSTERED INDEX IX_LiveShipments ON Shipments(WarehouseId) INCLUDE (...) WHERE IsArchived = 0`) indexes only active unarchived rows, slashing storage and DML maintenance overhead.
- **B:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: A filtered nonclustered index (`CREATE NONCLUSTERED INDEX IX_LiveShipments ON Shipments(WarehouseId) INCLUDE (...) WHERE IsArchived = 0`) indexes only active unarchived rows, slashing storage and DML maintenance overhead.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: A filtered nonclustered index (`CREATE NONCLUSTERED INDEX IX_LiveShipments ON Shipments(WarehouseId) INCLUDE (...) WHERE IsArchived = 0`) indexes only active unarchived rows, slashing storage and DML maintenance overhead.
- **D:** Correct. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. In this scenario: A filtered nonclustered index (`CREATE NONCLUSTERED INDEX IX_LiveShipments ON Shipments(WarehouseId) INCLUDE (...) WHERE IsArchived = 0`) indexes only active unarchived rows, slashing storage and DML maintenance overhead.

### Question 45 — B

Answer: Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`). Severe cardinality underestimation caused SQL to request a tiny memory grant, forcing the `Hash Match` build table to spill intermediate workfiles to `tempdb` disk I/O. Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. Local study-map skill 3.9 (Analyze Execution Plans (`Key Lookup`, `TempDB` Spills, Row Skew) and Monitor via SQL Intelligent Insights), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Execution plans and SQL Intelligent Insights automated performance diagnostics (https://learn.microsoft.com/en-us/azure/azure-sql/database/intelligent-insights-overview).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Severe cardinality underestimation caused SQL to request a tiny memory grant, forcing the `Hash Match` build table to spill intermediate workfiles to `tempdb` disk I/O.
- **B:** Correct. Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. In this scenario: Severe cardinality underestimation caused SQL to request a tiny memory grant, forcing the `Hash Match` build table to spill intermediate workfiles to `tempdb` disk I/O.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Severe cardinality underestimation caused SQL to request a tiny memory grant, forcing the `Hash Match` build table to spill intermediate workfiles to `tempdb` disk I/O.
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Severe cardinality underestimation caused SQL to request a tiny memory grant, forcing the `Hash Match` build table to spill intermediate workfiles to `tempdb` disk I/O.

### Question 46 — D

Answer: Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`). SQL Intelligent Insights analyzes workload execution telemetry against a 7-day rolling baseline and publishes plain-English root-cause diagnostics to Azure portal and `SQLInsights` logs. Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. Local study-map skill 3.9 (Analyze Execution Plans (`Key Lookup`, `TempDB` Spills, Row Skew) and Monitor via SQL Intelligent Insights), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Execution plans and SQL Intelligent Insights automated performance diagnostics (https://learn.microsoft.com/en-us/azure/azure-sql/database/intelligent-insights-overview).

- **A:** Incorrect for this requirement. BYOK TDE wraps the symmetric Database Encryption Key (`DEK`) with an asymmetric RSA key in Key Vault or Managed HSM so security admins control key rotation and instant revocation. Why the keyed choice wins: SQL Intelligent Insights analyzes workload execution telemetry against a 7-day rolling baseline and publishes plain-English root-cause diagnostics to Azure portal and `SQLInsights` logs.
- **B:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: SQL Intelligent Insights analyzes workload execution telemetry against a 7-day rolling baseline and publishes plain-English root-cause diagnostics to Azure portal and `SQLInsights` logs.
- **C:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: SQL Intelligent Insights analyzes workload execution telemetry against a 7-day rolling baseline and publishes plain-English root-cause diagnostics to Azure portal and `SQLInsights` logs.
- **D:** Correct. Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. In this scenario: SQL Intelligent Insights analyzes workload execution telemetry against a 7-day rolling baseline and publishes plain-English root-cause diagnostics to Azure portal and `SQLInsights` logs.

### Question 47 — A, C, D

Answers: Run `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON, MAX_DURATION = 90 MINUTES)` for heavily fragmented (`>30%`) indexes; Enable `AUTO_UPDATE_STATISTICS_ASYNC = ON` and schedule targeted `UPDATE STATISTICS` jobs so user queries do not stall waiting on sampling; Run `DBCC CHECKDB WITH PHYSICAL_ONLY` during off-peak windows or offload full `DBCC CHECKDB` onto a restored backup replica. Resumable online index rebuilds (`ONLINE = ON, RESUMABLE = ON`), asynchronous statistics refreshes (`AUTO_UPDATE_STATISTICS_ASYNC = ON`), and `DBCC CHECKDB WITH PHYSICAL_ONLY` keep 24x7 OLTP workloads responsive. Local study-map skill 3.10 (Implement Fragmentation-Aware Index Rebuilds (`ONLINE`, `RESUMABLE`), Async Statistics, and `DBCC CHECKDB`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Optimize index maintenance, statistics updates, and DBCC CHECKDB integrity checks (https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes).

- **A:** Correct. Resumable online index rebuilds persist progress in place, bound transaction log growth, and automatically pause at `MAX_DURATION` so later windows can `RESUME`. In this scenario: Resumable online index rebuilds (`ONLINE = ON, RESUMABLE = ON`), asynchronous statistics refreshes (`AUTO_UPDATE_STATISTICS_ASYNC = ON`), and `DBCC CHECKDB WITH PHYSICAL_ONLY` keep 24x7 OLTP workloads responsive.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Resumable online index rebuilds (`ONLINE = ON, RESUMABLE = ON`), asynchronous statistics refreshes (`AUTO_UPDATE_STATISTICS_ASYNC = ON`), and `DBCC CHECKDB WITH PHYSICAL_ONLY` keep 24x7 OLTP workloads responsive.
- **C:** Correct. `PHYSICAL_ONLY` checks page checksums, torn pages, and allocation structures at a fraction of full logical `CHECKDB` CPU/memory cost. In this scenario: Resumable online index rebuilds (`ONLINE = ON, RESUMABLE = ON`), asynchronous statistics refreshes (`AUTO_UPDATE_STATISTICS_ASYNC = ON`), and `DBCC CHECKDB WITH PHYSICAL_ONLY` keep 24x7 OLTP workloads responsive.
- **D:** Correct. Asynchronous statistics updates let incoming OLTP queries execute immediately with existing stats while a background thread refreshes stale histograms. In this scenario: Resumable online index rebuilds (`ONLINE = ON, RESUMABLE = ON`), asynchronous statistics refreshes (`AUTO_UPDATE_STATISTICS_ASYNC = ON`), and `DBCC CHECKDB WITH PHYSICAL_ONLY` keep 24x7 OLTP workloads responsive.
- **E:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Resumable online index rebuilds (`ONLINE = ON, RESUMABLE = ON`), asynchronous statistics refreshes (`AUTO_UPDATE_STATISTICS_ASYNC = ON`), and `DBCC CHECKDB WITH PHYSICAL_ONLY` keep 24x7 OLTP workloads responsive.
- **F:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Resumable online index rebuilds (`ONLINE = ON, RESUMABLE = ON`), asynchronous statistics refreshes (`AUTO_UPDATE_STATISTICS_ASYNC = ON`), and `DBCC CHECKDB WITH PHYSICAL_ONLY` keep 24x7 OLTP workloads responsive.

### Question 48 — C

Answer: Yes — the proposed configuration satisfies every stated technical, security, and availability requirement. Yes — `RESUMABLE = ON` with `MAX_DURATION = 60 MINUTES` cleanly pauses an online rebuild at the window boundary while retaining completed work so `RESUME` finishes the next night. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. Local study-map skill 3.10 (Implement Fragmentation-Aware Index Rebuilds (`ONLINE`, `RESUMABLE`), Async Statistics, and `DBCC CHECKDB`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Optimize index maintenance, statistics updates, and DBCC CHECKDB integrity checks (https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes).

- **A:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: Yes — `RESUMABLE = ON` with `MAX_DURATION = 60 MINUTES` cleanly pauses an online rebuild at the window boundary while retaining completed work so `RESUME` finishes the next night.
- **B:** Incorrect for this requirement. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Why the keyed choice wins: Yes — `RESUMABLE = ON` with `MAX_DURATION = 60 MINUTES` cleanly pauses an online rebuild at the window boundary while retaining completed work so `RESUME` finishes the next night.
- **C:** Correct. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. In this scenario: Yes — `RESUMABLE = ON` with `MAX_DURATION = 60 MINUTES` cleanly pauses an online rebuild at the window boundary while retaining completed work so `RESUME` finishes the next night.
- **D:** Incorrect for this requirement. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. Why the keyed choice wins: Yes — `RESUMABLE = ON` with `MAX_DURATION = 60 MINUTES` cleanly pauses an online rebuild at the window boundary while retaining completed work so `RESUME` finishes the next night.

### Question 49 — B

Answer: Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`). Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`) continuously validates and applies self-healing plan and index optimizations. Automatic Tuning continuously monitors Query Store, automatically forces prior plans when regressions occur, creates validated missing nonclustered indexes, and removes unused duplicate indexes. Local study-map skill 3.11 (Configure Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN`, `CREATE_INDEX`, `DROP_INDEX`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automatic tuning in Azure SQL Database and Azure SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-overview).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`) continuously validates and applies self-healing plan and index optimizations.
- **B:** Correct. Automatic Tuning continuously monitors Query Store, automatically forces prior plans when regressions occur, creates validated missing nonclustered indexes, and removes unused duplicate indexes. In this scenario: Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`) continuously validates and applies self-healing plan and index optimizations.
- **C:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`) continuously validates and applies self-healing plan and index optimizations.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`) continuously validates and applies self-healing plan and index optimizations.

### Question 50 — C

Answer: No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases. Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not on single Azure SQL Databases; isolate read workloads on SQL Database via read replicas or Elastic Pools instead. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. Local study-map skill 3.12 (Configure Server Performance Settings (`MAXDOP`, `cost threshold`, `max server memory`) and Resource Governor), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Server configuration options (MAXDOP, memory) and Resource Governor workload isolation (https://learn.microsoft.com/en-us/sql/relational-databases/resource-governor/resource-governor).

- **A:** Incorrect for this requirement. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Why the keyed choice wins: Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not on single Azure SQL Databases; isolate read workloads on SQL Database via read replicas or Elastic Pools instead.
- **B:** Incorrect for this requirement. SQL Server write-ahead logging performs sequential unbuffered writes; enabling `ReadOnly` or `ReadWrite` host caching on `.ldf` disks degrades throughput or risks corruption. Why the keyed choice wins: Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not on single Azure SQL Databases; isolate read workloads on SQL Database via read replicas or Elastic Pools instead.
- **C:** Correct. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. In this scenario: Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not on single Azure SQL Databases; isolate read workloads on SQL Database via read replicas or Elastic Pools instead.
- **D:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not on single Azure SQL Databases; isolate read workloads on SQL Database via read replicas or Elastic Pools instead.

### Question 51 — C

Answer: Use `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`, `OPTIMIZED_PLAN_FORCING`) per database. Executing `ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 2` inside `LegacyCatalogDB` scopes parallelism solely to that database without altering instance-wide `sp_configure` settings. Database-scoped configurations isolate optimizer settings (`MAXDOP`, CE version, parameter sniffing) to a single database without affecting sibling databases on SQL MI/VMs or requiring server access. Local study-map skill 3.13 (Implement `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: ALTER DATABASE SCOPED CONFIGURATION and dynamic compute/storage scaling (https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Executing `ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 2` inside `LegacyCatalogDB` scopes parallelism solely to that database without altering instance-wide `sp_configure` settings.
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Executing `ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 2` inside `LegacyCatalogDB` scopes parallelism solely to that database without altering instance-wide `sp_configure` settings.
- **C:** Correct. Database-scoped configurations isolate optimizer settings (`MAXDOP`, CE version, parameter sniffing) to a single database without affecting sibling databases on SQL MI/VMs or requiring server access. In this scenario: Executing `ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 2` inside `LegacyCatalogDB` scopes parallelism solely to that database without altering instance-wide `sp_configure` settings.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Executing `ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 2` inside `LegacyCatalogDB` scopes parallelism solely to that database without altering instance-wide `sp_configure` settings.

### Question 52 — D

Answer: Enable compatibility level `160` Intelligent Query Processing (`Parameter Sensitive Plan` optimization, `Memory Grant Feedback` persistence, `Scalar UDF Inlining`, `DOP Feedback`). Parameter Sensitive Plan (`PSP`) optimization in compatibility level `160` maintains multiple active dispatcher query plans bucketed by parameter predicate cardinality. SQL 2022 / Azure SQL compat `160` IQP caches multiple active plans per query based on parameter cardinality (`PSP`), right-sizes `tempdb`-spilling memory grants, and inlines scalar T-SQL UDFs. Local study-map skill 3.14 (Identify Use Cases for Intelligent Query Processing (`PSP` Optimization, Memory Grant Feedback, Scalar UDF Inlining)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Intelligent Query Processing (IQP) features in SQL databases (https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing).

- **A:** Incorrect for this requirement. Row-by-row cursors and multi-statement TVFs under legacy compatibility levels execute thousands of iterative context switches and 1-row cardinality guesses. Why the keyed choice wins: Parameter Sensitive Plan (`PSP`) optimization in compatibility level `160` maintains multiple active dispatcher query plans bucketed by parameter predicate cardinality.
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Parameter Sensitive Plan (`PSP`) optimization in compatibility level `160` maintains multiple active dispatcher query plans bucketed by parameter predicate cardinality.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Parameter Sensitive Plan (`PSP`) optimization in compatibility level `160` maintains multiple active dispatcher query plans bucketed by parameter predicate cardinality.
- **D:** Correct. SQL 2022 / Azure SQL compat `160` IQP caches multiple active plans per query based on parameter cardinality (`PSP`), right-sizes `tempdb`-spilling memory grants, and inlines scalar T-SQL UDFs. In this scenario: Parameter Sensitive Plan (`PSP`) optimization in compatibility level `160` maintains multiple active dispatcher query plans bucketed by parameter predicate cardinality.

### Question 53 — A

Answer: SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators. Create a SQL Server Credential mapped to a least-privilege service account, bind it to a SQL Server Agent PowerShell Subsystem Proxy, and select that Proxy in the job step's `Run as` setting. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. Local study-map skill 4.1 (Create and Schedule SQL Server Agent Maintenance Jobs, Proxies, Severity `19–25` Alerts, and Database Mail), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server Agent jobs, schedules, alerts, and Database Mail operators (https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent).

- **A:** Correct. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. In this scenario: Create a SQL Server Credential mapped to a least-privilege service account, bind it to a SQL Server Agent PowerShell Subsystem Proxy, and select that Proxy in the job step's `Run as` setting.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Create a SQL Server Credential mapped to a least-privilege service account, bind it to a SQL Server Agent PowerShell Subsystem Proxy, and select that Proxy in the job step's `Run as` setting.
- **C:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: Create a SQL Server Credential mapped to a least-privilege service account, bind it to a SQL Server Agent PowerShell Subsystem Proxy, and select that Proxy in the job step's `Run as` setting.
- **D:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Create a SQL Server Credential mapped to a least-privilege service account, bind it to a SQL Server Agent PowerShell Subsystem Proxy, and select that Proxy in the job step's `Run as` setting.

### Question 54 — D

Answer: SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators. Configure Database Mail on SQL Managed Instance, register `dba-oncall@kestrelcart.com` as a SQL Server Agent Operator, and create SQL Server Agent Alerts for Error `824` and Severity `19–25`. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. Local study-map skill 4.1 (Create and Schedule SQL Server Agent Maintenance Jobs, Proxies, Severity `19–25` Alerts, and Database Mail), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server Agent jobs, schedules, alerts, and Database Mail operators (https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Configure Database Mail on SQL Managed Instance, register `dba-oncall@kestrelcart.com` as a SQL Server Agent Operator, and create SQL Server Agent Alerts for Error `824` and Severity `19–25`.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Configure Database Mail on SQL Managed Instance, register `dba-oncall@kestrelcart.com` as a SQL Server Agent Operator, and create SQL Server Agent Alerts for Error `824` and Severity `19–25`.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Configure Database Mail on SQL Managed Instance, register `dba-oncall@kestrelcart.com` as a SQL Server Agent Operator, and create SQL Server Agent Alerts for Error `824` and Severity `19–25`.
- **D:** Correct. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. In this scenario: Configure Database Mail on SQL Managed Instance, register `dba-oncall@kestrelcart.com` as a SQL Server Agent Operator, and create SQL Server Agent Alerts for Error `824` and Severity `19–25`.

### Question 55 — A, D

Answers: Create a Windows/SQL Credential and map it to a SQL Server Agent Subsystem Proxy (`CmdExec` / `PowerShell`) instead of granting `sysadmin`; Configure Database Mail, define an Agent Operator, and create SQL Server Agent Alerts for Severity `19–25` and Errors `823`, `824`, and `825`. Map least-privilege Credentials to SQL Server Agent Subsystem Proxies for non-`sysadmin` job steps, and configure Database Mail Operators attached to Severity `19–25` / Error `823–825` Alerts. Local study-map skill 4.1 (Create and Schedule SQL Server Agent Maintenance Jobs, Proxies, Severity `19–25` Alerts, and Database Mail), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server Agent jobs, schedules, alerts, and Database Mail operators (https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent).

- **A:** Correct. Severity `19–25` and I/O errors `823–825` indicate critical resource exhaustion or storage corruption requiring immediate DBA notification. In this scenario: Map least-privilege Credentials to SQL Server Agent Subsystem Proxies for non-`sysadmin` job steps, and configure Database Mail Operators attached to Severity `19–25` / Error `823–825` Alerts.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Map least-privilege Credentials to SQL Server Agent Subsystem Proxies for non-`sysadmin` job steps, and configure Database Mail Operators attached to Severity `19–25` / Error `823–825` Alerts.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Map least-privilege Credentials to SQL Server Agent Subsystem Proxies for non-`sysadmin` job steps, and configure Database Mail Operators attached to Severity `19–25` / Error `823–825` Alerts.
- **D:** Correct. SQL Server Agent proxies let non-`sysadmin` job owners execute external subsystem steps under a scoped least-privilege identity. In this scenario: Map least-privilege Credentials to SQL Server Agent Subsystem Proxies for non-`sysadmin` job steps, and configure Database Mail Operators attached to Severity `19–25` / Error `823–825` Alerts.
- **E:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Map least-privilege Credentials to SQL Server Agent Subsystem Proxies for non-`sysadmin` job steps, and configure Database Mail Operators attached to Severity `19–25` / Error `823–825` Alerts.

### Question 56 — B

Answer: Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries. Azure SQL Managed Instance is a managed PaaS service that restricts underlying host OS filesystem and `CmdExec`/ActiveX subsystem access; refactor file processing into Azure Automation, Functions, or Blob-integrated T-SQL. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. Local study-map skill 4.2 (Troubleshoot SQL Server Agent Job Histories, Credential/Proxy Permissions, and SQL MI Subsystem Boundaries), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot SQL Server Agent jobs, proxies, and SQL Managed Instance Agent differences (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/transact-sql-tsql-differences-sql-server).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Azure SQL Managed Instance is a managed PaaS service that restricts underlying host OS filesystem and `CmdExec`/ActiveX subsystem access; refactor file processing into Azure Automation, Functions, or Blob-integrated T-SQL.
- **B:** Correct. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. In this scenario: Azure SQL Managed Instance is a managed PaaS service that restricts underlying host OS filesystem and `CmdExec`/ActiveX subsystem access; refactor file processing into Azure Automation, Functions, or Blob-integrated T-SQL.
- **C:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: Azure SQL Managed Instance is a managed PaaS service that restricts underlying host OS filesystem and `CmdExec`/ActiveX subsystem access; refactor file processing into Azure Automation, Functions, or Blob-integrated T-SQL.
- **D:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Azure SQL Managed Instance is a managed PaaS service that restricts underlying host OS filesystem and `CmdExec`/ActiveX subsystem access; refactor file processing into Azure Automation, Functions, or Blob-integrated T-SQL.

### Question 57 — B

Answer: Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries. `msdb.dbo.sysjobhistory` (or `msdb.dbo.sp_help_jobhistory`) stores per-step execution status codes, full error text (`step_id > 0`), and `HHMMSS` run durations for SQL Server Agent jobs. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. Local study-map skill 4.2 (Troubleshoot SQL Server Agent Job Histories, Credential/Proxy Permissions, and SQL MI Subsystem Boundaries), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot SQL Server Agent jobs, proxies, and SQL Managed Instance Agent differences (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/transact-sql-tsql-differences-sql-server).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `msdb.dbo.sysjobhistory` (or `msdb.dbo.sp_help_jobhistory`) stores per-step execution status codes, full error text (`step_id > 0`), and `HHMMSS` run durations for SQL Server Agent jobs.
- **B:** Correct. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. In this scenario: `msdb.dbo.sysjobhistory` (or `msdb.dbo.sp_help_jobhistory`) stores per-step execution status codes, full error text (`step_id > 0`), and `HHMMSS` run durations for SQL Server Agent jobs.
- **C:** Incorrect for this requirement. BYOK TDE wraps the symmetric Database Encryption Key (`DEK`) with an asymmetric RSA key in Key Vault or Managed HSM so security admins control key rotation and instant revocation. Why the keyed choice wins: `msdb.dbo.sysjobhistory` (or `msdb.dbo.sp_help_jobhistory`) stores per-step execution status codes, full error text (`step_id > 0`), and `HHMMSS` run durations for SQL Server Agent jobs.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: `msdb.dbo.sysjobhistory` (or `msdb.dbo.sp_help_jobhistory`) stores per-step execution status codes, full error text (`step_id > 0`), and `HHMMSS` run durations for SQL Server Agent jobs.

### Question 58 — B

Answer: Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`. Marking the parameter `@secure()` in Bicep prevents Azure Resource Manager from logging or returning the value, and pairing it with a Key Vault secret reference keeps credentials out of source control. Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. Local study-map skill 4.3 (Automate Idempotent Deployment Using Bicep and ARM Templates with `@secure()` Key Vault References & `what-if`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Deploy Azure SQL resources using Bicep and Azure Resource Manager (ARM) templates (https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-Quickstart-bicep).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Marking the parameter `@secure()` in Bicep prevents Azure Resource Manager from logging or returning the value, and pairing it with a Key Vault secret reference keeps credentials out of source control.
- **B:** Correct. Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. In this scenario: Marking the parameter `@secure()` in Bicep prevents Azure Resource Manager from logging or returning the value, and pairing it with a Key Vault secret reference keeps credentials out of source control.
- **C:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Marking the parameter `@secure()` in Bicep prevents Azure Resource Manager from logging or returning the value, and pairing it with a Key Vault secret reference keeps credentials out of source control.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Marking the parameter `@secure()` in Bicep prevents Azure Resource Manager from logging or returning the value, and pairing it with a Key Vault secret reference keeps credentials out of source control.

### Question 59 — D

Answer: Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`. Running `az deployment group what-if` simulates the ARM deployment against live state and prints color-coded `Create`, `Modify`, `Delete`, and `NoChange` predictions without mutating resources. Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. Local study-map skill 4.3 (Automate Idempotent Deployment Using Bicep and ARM Templates with `@secure()` Key Vault References & `what-if`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Deploy Azure SQL resources using Bicep and Azure Resource Manager (ARM) templates (https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-Quickstart-bicep).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Running `az deployment group what-if` simulates the ARM deployment against live state and prints color-coded `Create`, `Modify`, `Delete`, and `NoChange` predictions without mutating resources.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Running `az deployment group what-if` simulates the ARM deployment against live state and prints color-coded `Create`, `Modify`, `Delete`, and `NoChange` predictions without mutating resources.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Running `az deployment group what-if` simulates the ARM deployment against live state and prints color-coded `Create`, `Modify`, `Delete`, and `NoChange` predictions without mutating resources.
- **D:** Correct. Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. In this scenario: Running `az deployment group what-if` simulates the ARM deployment against live state and prints color-coded `Create`, `Modify`, `Delete`, and `NoChange` predictions without mutating resources.

### Question 60 — B

Answer: Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`). `Set-AzSqlDatabase` modifies compute tier, vCore count, backup redundancy, and HA properties idempotently on an existing Azure SQL Database (`New-AzSqlDatabase` is for initial creation). `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. Local study-map skill 4.4 (Automate Azure SQL Provisioning and Day-2 Management Using Azure PowerShell (`Az.Sql`) and Azure CLI (`az sql`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL management using Azure PowerShell and Azure CLI (https://learn.microsoft.com/en-us/azure/azure-sql/database/scripts/create-and-configure-database-powershell).

- **A:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: `Set-AzSqlDatabase` modifies compute tier, vCore count, backup redundancy, and HA properties idempotently on an existing Azure SQL Database (`New-AzSqlDatabase` is for initial creation).
- **B:** Correct. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. In this scenario: `Set-AzSqlDatabase` modifies compute tier, vCore count, backup redundancy, and HA properties idempotently on an existing Azure SQL Database (`New-AzSqlDatabase` is for initial creation).
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: `Set-AzSqlDatabase` modifies compute tier, vCore count, backup redundancy, and HA properties idempotently on an existing Azure SQL Database (`New-AzSqlDatabase` is for initial creation).
- **D:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: `Set-AzSqlDatabase` modifies compute tier, vCore count, backup redundancy, and HA properties idempotently on an existing Azure SQL Database (`New-AzSqlDatabase` is for initial creation).

### Question 61 — D

Answer: Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`). `az sql db create` provisions a new Azure SQL Database with the specified vCore edition, capacity, and `--zone-redundant` high-availability flag. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. Local study-map skill 4.4 (Automate Azure SQL Provisioning and Day-2 Management Using Azure PowerShell (`Az.Sql`) and Azure CLI (`az sql`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL management using Azure PowerShell and Azure CLI (https://learn.microsoft.com/en-us/azure/azure-sql/database/scripts/create-and-configure-database-powershell).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: `az sql db create` provisions a new Azure SQL Database with the specified vCore edition, capacity, and `--zone-redundant` high-availability flag.
- **B:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: `az sql db create` provisions a new Azure SQL Database with the specified vCore edition, capacity, and `--zone-redundant` high-availability flag.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `az sql db create` provisions a new Azure SQL Database with the specified vCore edition, capacity, and `--zone-redundant` high-availability flag.
- **D:** Correct. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. In this scenario: `az sql db create` provisions a new Azure SQL Database with the specified vCore edition, capacity, and `--zone-redundant` high-availability flag.

### Question 62 — A

Answer: Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules. The target subnet either contains existing NICs/VMs, is smaller than `/28`, or lacks subnet delegation to `Microsoft.Sql/managedInstances` and its required route table/NSG associations. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. Local study-map skill 4.5 (Monitor and Troubleshoot Automated Deployments (`CorrelationId`, Quota, SQL MI Subnet Delegation/UDR/NSG)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot ARM/Bicep template and SQL Managed Instance subnet deployment errors (https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/common-deployment-errors).

- **A:** Correct. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. In this scenario: The target subnet either contains existing NICs/VMs, is smaller than `/28`, or lacks subnet delegation to `Microsoft.Sql/managedInstances` and its required route table/NSG associations.
- **B:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: The target subnet either contains existing NICs/VMs, is smaller than `/28`, or lacks subnet delegation to `Microsoft.Sql/managedInstances` and its required route table/NSG associations.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: The target subnet either contains existing NICs/VMs, is smaller than `/28`, or lacks subnet delegation to `Microsoft.Sql/managedInstances` and its required route table/NSG associations.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: The target subnet either contains existing NICs/VMs, is smaller than `/28`, or lacks subnet delegation to `Microsoft.Sql/managedInstances` and its required route table/NSG associations.

### Question 63 — A

Answer: Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules. Run `Get-AzResourceGroupDeploymentOperation` (or filter Azure Activity Log by `CorrelationId`) to confirm the regional vCore quota ceiling, then submit an Azure SQL regional vCore quota increase or target an approved region. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. Local study-map skill 4.5 (Monitor and Troubleshoot Automated Deployments (`CorrelationId`, Quota, SQL MI Subnet Delegation/UDR/NSG)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot ARM/Bicep template and SQL Managed Instance subnet deployment errors (https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/common-deployment-errors).

- **A:** Correct. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. In this scenario: Run `Get-AzResourceGroupDeploymentOperation` (or filter Azure Activity Log by `CorrelationId`) to confirm the regional vCore quota ceiling, then submit an Azure SQL regional vCore quota increase or target an approved region.
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Run `Get-AzResourceGroupDeploymentOperation` (or filter Azure Activity Log by `CorrelationId`) to confirm the regional vCore quota ceiling, then submit an Azure SQL regional vCore quota increase or target an approved region.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Run `Get-AzResourceGroupDeploymentOperation` (or filter Azure Activity Log by `CorrelationId`) to confirm the regional vCore quota ceiling, then submit an Azure SQL regional vCore quota increase or target an approved region.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Run `Get-AzResourceGroupDeploymentOperation` (or filter Azure Activity Log by `CorrelationId`) to confirm the regional vCore quota ceiling, then submit an Azure SQL regional vCore quota increase or target an approved region.

### Question 64 — C

Answer: Create S1+ Job Database & Elastic Job Agent with UAMI → Create contained UAMI user on target DBs with needed permissions → Define Target Group (`jobs.sp_add_target_group_member`) → Add T-SQL steps & schedule (`jobs.sp_add_job`). Provision an S1+ Job Database and Elastic Job Agent with a UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and add T-SQL steps/schedules (`jobs.sp_add_job`). Modern Elastic Jobs use a dedicated S1+ job database, an Elastic Job Agent assigned a User-Assigned Managed Identity (UAMI) authorized on target databases, a target group, and scheduled T-SQL steps. Local study-map skill 4.6 (Create and Configure Azure SQL Database Elastic Jobs Across Target Groups Using User-Assigned Managed Identity), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Elastic jobs in Azure SQL Database with Managed Identity authentication (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-jobs-overview).

- **A:** Incorrect for this requirement. Incorrect workflow: single Azure SQL Databases do not have SQL Server Agent or cross-DB linked servers in the same way as SQL MI; Elastic Jobs fan out T-SQL asynchronously. Why the keyed choice wins: Provision an S1+ Job Database and Elastic Job Agent with a UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and add T-SQL steps/schedules (`jobs.sp_add_job`).
- **B:** Incorrect for this requirement. Incorrect workflow: Elastic Job databases require S1 or higher, target groups must exist before binding executions, NTLM local accounts are invalid in SQL DB, and `msdb` belongs to SQL Agent. Why the keyed choice wins: Provision an S1+ Job Database and Elastic Job Agent with a UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and add T-SQL steps/schedules (`jobs.sp_add_job`).
- **C:** Correct. Modern Elastic Jobs use a dedicated S1+ job database, an Elastic Job Agent assigned a User-Assigned Managed Identity (UAMI) authorized on target databases, a target group, and scheduled T-SQL steps. In this scenario: Provision an S1+ Job Database and Elastic Job Agent with a UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and add T-SQL steps/schedules (`jobs.sp_add_job`).
- **D:** Incorrect for this requirement. Incorrect workflow: Elastic Job Agents target Azure SQL servers, elastic pools, and databases using Managed Identity—never Cosmos DB containers or hardcoded Git secrets. Why the keyed choice wins: Provision an S1+ Job Database and Elastic Job Agent with a UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and add T-SQL steps/schedules (`jobs.sp_add_job`).

### Question 65 — A

Answer: Azure Automation PowerShell / Python runbooks (or Azure Functions / Logic Apps) using a System-Assigned Managed Identity on a recurring schedule. An Azure Automation PowerShell runbook scheduled at 23:00 and 06:00 UTC authenticating via its System-Assigned Managed Identity (`Connect-AzAccount -Identity`) invokes `Set-AzSqlElasticPool` serverlessly. Azure Automation runbooks authenticate via Managed Identity (`Connect-AzAccount -Identity`) to scale vCores/Elastic Pools on schedule, rotate keys, or orchestrate hybrid maintenance via Hybrid Workers. Local study-map skill 4.7 (Automate Database Maintenance and Scaling Using Azure Automation Runbooks, Logic Apps, and Azure Functions), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL maintenance tasks with Azure Automation, Logic Apps, and Functions (https://learn.microsoft.com/en-us/azure/automation/overview).

- **A:** Correct. Azure Automation runbooks authenticate via Managed Identity (`Connect-AzAccount -Identity`) to scale vCores/Elastic Pools on schedule, rotate keys, or orchestrate hybrid maintenance via Hybrid Workers. In this scenario: An Azure Automation PowerShell runbook scheduled at 23:00 and 06:00 UTC authenticating via its System-Assigned Managed Identity (`Connect-AzAccount -Identity`) invokes `Set-AzSqlElasticPool` serverlessly.
- **B:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: An Azure Automation PowerShell runbook scheduled at 23:00 and 06:00 UTC authenticating via its System-Assigned Managed Identity (`Connect-AzAccount -Identity`) invokes `Set-AzSqlElasticPool` serverlessly.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: An Azure Automation PowerShell runbook scheduled at 23:00 and 06:00 UTC authenticating via its System-Assigned Managed Identity (`Connect-AzAccount -Identity`) invokes `Set-AzSqlElasticPool` serverlessly.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: An Azure Automation PowerShell runbook scheduled at 23:00 and 06:00 UTC authenticating via its System-Assigned Managed Identity (`Connect-AzAccount -Identity`) invokes `Set-AzSqlElasticPool` serverlessly.

### Question 66 — C

Answer: Azure Automation PowerShell / Python runbooks (or Azure Functions / Logic Apps) using a System-Assigned Managed Identity on a recurring schedule. An Azure Logic App triggered by an Azure Monitor Action Group HTTP/Logic App action parses the alert schema and dispatches Teams and ServiceNow connectors without custom infrastructure. Azure Automation runbooks authenticate via Managed Identity (`Connect-AzAccount -Identity`) to scale vCores/Elastic Pools on schedule, rotate keys, or orchestrate hybrid maintenance via Hybrid Workers. Local study-map skill 4.7 (Automate Database Maintenance and Scaling Using Azure Automation Runbooks, Logic Apps, and Azure Functions), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL maintenance tasks with Azure Automation, Logic Apps, and Functions (https://learn.microsoft.com/en-us/azure/automation/overview).

- **A:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: An Azure Logic App triggered by an Azure Monitor Action Group HTTP/Logic App action parses the alert schema and dispatches Teams and ServiceNow connectors without custom infrastructure.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: An Azure Logic App triggered by an Azure Monitor Action Group HTTP/Logic App action parses the alert schema and dispatches Teams and ServiceNow connectors without custom infrastructure.
- **C:** Correct. Azure Automation runbooks authenticate via Managed Identity (`Connect-AzAccount -Identity`) to scale vCores/Elastic Pools on schedule, rotate keys, or orchestrate hybrid maintenance via Hybrid Workers. In this scenario: An Azure Logic App triggered by an Azure Monitor Action Group HTTP/Logic App action parses the alert schema and dispatches Teams and ServiceNow connectors without custom infrastructure.
- **D:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: An Azure Logic App triggered by an Azure Monitor Action Group HTTP/Logic App action parses the alert schema and dispatches Teams and ServiceNow connectors without custom infrastructure.

### Question 67 — D

Answer: Configure Azure Monitor Metric / Log Alert rules routed to Action Groups and query `jobs.job_executions` in the Elastic Job database to diagnose step failures. Querying `jobs.job_executions` inside the Elastic Job database surfaces execution status, retry counts, and detailed T-SQL error messages for every individual target database, while Azure Monitor Action Groups notify operators on `failed` job metric counts. Action Groups dispatch email/SMS/webhook/Logic App notifications when alert thresholds fire, while `jobs.job_executions` exposes per-target error messages, retries, and timeouts for Elastic Jobs. Local study-map skill 4.8 (Configure Azure Monitor Action Group Alerts on Database Tasks and Troubleshoot `jobs.job_executions`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure Azure Monitor alerts and troubleshoot Elastic Jobs and automated runbooks (https://learn.microsoft.com/en-us/azure/azure-sql/database/alerts-insights-configure-portal).

- **A:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Querying `jobs.job_executions` inside the Elastic Job database surfaces execution status, retry counts, and detailed T-SQL error messages for every individual target database, while Azure Monitor Action Groups notify operators on `failed` job metric counts.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Querying `jobs.job_executions` inside the Elastic Job database surfaces execution status, retry counts, and detailed T-SQL error messages for every individual target database, while Azure Monitor Action Groups notify operators on `failed` job metric counts.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Querying `jobs.job_executions` inside the Elastic Job database surfaces execution status, retry counts, and detailed T-SQL error messages for every individual target database, while Azure Monitor Action Groups notify operators on `failed` job metric counts.
- **D:** Correct. Action Groups dispatch email/SMS/webhook/Logic App notifications when alert thresholds fire, while `jobs.job_executions` exposes per-target error messages, retries, and timeouts for Elastic Jobs. In this scenario: Querying `jobs.job_executions` inside the Elastic Job database surfaces execution status, retry counts, and detailed T-SQL error messages for every individual target database, while Azure Monitor Action Groups notify operators on `failed` job metric counts.

### Question 68 — C

Answer: Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`). Enabling `Zone Redundant` HA on Azure SQL Database provides synchronous 3-zone `RPO = 0` intra-region resilience, while pairing it with a cross-region Failover Group delivers the `RPO = 5s` / `RTO = 1h` regional DR SLA. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. Local study-map skill 5.1 (Recommend HA/DR Architectures Based on RPO and RTO (`Zone Redundant`, `Failover Groups`, `Geo-Restore`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Business continuity, RPO/RTO targets, and high availability in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recovery-hadr-overview).

- **A:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: Enabling `Zone Redundant` HA on Azure SQL Database provides synchronous 3-zone `RPO = 0` intra-region resilience, while pairing it with a cross-region Failover Group delivers the `RPO = 5s` / `RTO = 1h` regional DR SLA.
- **B:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Enabling `Zone Redundant` HA on Azure SQL Database provides synchronous 3-zone `RPO = 0` intra-region resilience, while pairing it with a cross-region Failover Group delivers the `RPO = 5s` / `RTO = 1h` regional DR SLA.
- **C:** Correct. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. In this scenario: Enabling `Zone Redundant` HA on Azure SQL Database provides synchronous 3-zone `RPO = 0` intra-region resilience, while pairing it with a cross-region Failover Group delivers the `RPO = 5s` / `RTO = 1h` regional DR SLA.
- **D:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Enabling `Zone Redundant` HA on Azure SQL Database provides synchronous 3-zone `RPO = 0` intra-region resilience, while pairing it with a cross-region Failover Group delivers the `RPO = 5s` / `RTO = 1h` regional DR SLA.

### Question 69 — A

Answer: Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`). Relying on Geo-Restore from default `RA-GRS` automated backups requires zero standby compute spend while meeting `RPO <= 1h` and `RTO <= 12h` recovery targets. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. Local study-map skill 5.1 (Recommend HA/DR Architectures Based on RPO and RTO (`Zone Redundant`, `Failover Groups`, `Geo-Restore`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Business continuity, RPO/RTO targets, and high availability in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recovery-hadr-overview).

- **A:** Correct. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. In this scenario: Relying on Geo-Restore from default `RA-GRS` automated backups requires zero standby compute spend while meeting `RPO <= 1h` and `RTO <= 12h` recovery targets.
- **B:** Incorrect for this requirement. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. Why the keyed choice wins: Relying on Geo-Restore from default `RA-GRS` automated backups requires zero standby compute spend while meeting `RPO <= 1h` and `RTO <= 12h` recovery targets.
- **C:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: Relying on Geo-Restore from default `RA-GRS` automated backups requires zero standby compute spend while meeting `RPO <= 1h` and `RTO <= 12h` recovery targets.
- **D:** Incorrect for this requirement. Secure enclaves delegate column decryption into an isolated memory region inside SQL, unlocking `LIKE`, `<`, `>`, `ORDER BY`, and fast in-place initial encryption without exposing plaintext to DBAs. Why the keyed choice wins: Relying on Geo-Restore from default `RA-GRS` automated backups requires zero standby compute spend while meeting `RPO <= 1h` and `RTO <= 12h` recovery targets.

### Question 70 — C

Answer: Hybrid DR using Managed Instance link with bidirectional online failover between SQL Server 2022 and Azure SQL Managed Instance. Managed Instance link with SQL Server 2022 supports bidirectional online planned failover between on-premises SQL Server 2022 and Azure SQL Managed Instance using a distributed Availability Group. SQL Server 2022 supports two-way online planned failover back and forth with Azure SQL Managed Instance via Managed Instance link (whereas SQL Server 2016–2019 link failover is one-way to Azure). Local study-map skill 5.2 (Evaluate Hybrid HA/DR (`Managed Instance Link` Bidirectional SQL 2022 Failover) and Azure-Specific HA Tiers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Hybrid HA/DR with Managed Instance link and distributed Availability Groups (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-disaster-recovery).

- **A:** Incorrect for this requirement. Managed Instance link online failback from SQL MI to SQL Server requires SQL Server 2022 or later; SQL Server 2016 and 2019 support one-way migration into SQL MI only. Why the keyed choice wins: Managed Instance link with SQL Server 2022 supports bidirectional online planned failover between on-premises SQL Server 2022 and Azure SQL Managed Instance using a distributed Availability Group.
- **B:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: Managed Instance link with SQL Server 2022 supports bidirectional online planned failover between on-premises SQL Server 2022 and Azure SQL Managed Instance using a distributed Availability Group.
- **C:** Correct. SQL Server 2022 supports two-way online planned failover back and forth with Azure SQL Managed Instance via Managed Instance link (whereas SQL Server 2016–2019 link failover is one-way to Azure). In this scenario: Managed Instance link with SQL Server 2022 supports bidirectional online planned failover between on-premises SQL Server 2022 and Azure SQL Managed Instance using a distributed Availability Group.
- **D:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Managed Instance link with SQL Server 2022 supports bidirectional online planned failover between on-premises SQL Server 2022 and Azure SQL Managed Instance using a distributed Availability Group.

### Question 71 — A

Answer: Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica. Business Critical maintains a 4-node Always On availability group quorum with local SSD storage and sub-second replica failover, whereas General Purpose uses stateless compute failing over via Azure Service Fabric over remote redundant storage. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. Local study-map skill 5.2 (Evaluate Hybrid HA/DR (`Managed Instance Link` Bidirectional SQL 2022 Failover) and Azure-Specific HA Tiers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Hybrid HA/DR with Managed Instance link and distributed Availability Groups (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-disaster-recovery).

- **A:** Correct. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. In this scenario: Business Critical maintains a 4-node Always On availability group quorum with local SSD storage and sub-second replica failover, whereas General Purpose uses stateless compute failing over via Azure Service Fabric over remote redundant storage.
- **B:** Incorrect for this requirement. SQL Managed Instance provides near-100% SQL Server engine compatibility (cross-DB queries, SQL Agent, CLR, Service Broker), and Next-gen GP scales IOPS independently of storage up to 500 DBs. Why the keyed choice wins: Business Critical maintains a 4-node Always On availability group quorum with local SSD storage and sub-second replica failover, whereas General Purpose uses stateless compute failing over via Azure Service Fabric over remote redundant storage.
- **C:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Business Critical maintains a 4-node Always On availability group quorum with local SSD storage and sub-second replica failover, whereas General Purpose uses stateless compute failing over via Azure Service Fabric over remote redundant storage.
- **D:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Business Critical maintains a 4-node Always On availability group quorum with local SSD storage and sub-second replica failover, whereas General Purpose uses stateless compute failing over via Azure Service Fabric over remote redundant storage.

### Question 72 — D

Answer: Provision secondary SQL server with matching firewall/Private Link & Entra admin → Create Failover Group with coupled DBs → Point apps to `<fog>.database.windows.net` & `.secondary` → Run planned `Switch-AzSqlDatabaseFailoverGroup` drill. Mirror network/Entra settings on the paired SQL server, group all coupled DBs in a Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and run a planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback. A resilient Failover Group mirrors security/network configs on the secondary server, groups coupled databases under stable read-write and read-only listeners, and validates readiness via planned zero-data-loss failover. Local study-map skill 5.3 (Plan Non-Disruptive HA/DR Failover Drills, Listener Redirection Validation, and Read-Only Secondary Testing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Disaster recovery drills and failover testing for Azure SQL solutions (https://learn.microsoft.com/en-us/azure/azure-sql/database/disaster-recovery-drills).

- **A:** Incorrect for this requirement. Incorrect workflow: forced failover with `AllowDataLoss` risks dropping uncommitted transactions during drills, and hardcoding regional server names breaks automatic client redirection. Why the keyed choice wins: Mirror network/Entra settings on the paired SQL server, group all coupled DBs in a Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and run a planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback.
- **B:** Incorrect for this requirement. Incorrect workflow: Failover Groups span distinct regions, replicate user databases rather than `master`/`tempdb`, and `.secondary.database.windows.net` is strictly read-only. Why the keyed choice wins: Mirror network/Entra settings on the paired SQL server, group all coupled DBs in a Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and run a planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback.
- **C:** Incorrect for this requirement. Incorrect workflow: deleting production databases and manually rewriting connection strings causes hours of avoidable downtime instead of testing non-disruptive Failover Group listener failover. Why the keyed choice wins: Mirror network/Entra settings on the paired SQL server, group all coupled DBs in a Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and run a planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback.
- **D:** Correct. A resilient Failover Group mirrors security/network configs on the secondary server, groups coupled databases under stable read-write and read-only listeners, and validates readiness via planned zero-data-loss failover. In this scenario: Mirror network/Entra settings on the paired SQL server, group all coupled DBs in a Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and run a planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback.

### Question 73 — C

Answer: Non-disruptive DR readiness drill executing a planned zero-data-loss Failover Group switch (`Switch-AzSqlDatabaseFailoverGroup`), validating app listeners, and failing back. A planned failover waits for the secondary replica to harden all remaining primary log records (`RPO = 0`) before swapping roles, whereas `-AllowDataLoss` forces immediate cutover and can discard unsent transactions. Planned failover synchronizes pending log records before switching roles (`RPO = 0`), validating secondary firewall/Entra configs and `<fog>.database.windows.net` DNS redirection safely. Local study-map skill 5.3 (Plan Non-Disruptive HA/DR Failover Drills, Listener Redirection Validation, and Read-Only Secondary Testing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Disaster recovery drills and failover testing for Azure SQL solutions (https://learn.microsoft.com/en-us/azure/azure-sql/database/disaster-recovery-drills).

- **A:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: A planned failover waits for the secondary replica to harden all remaining primary log records (`RPO = 0`) before swapping roles, whereas `-AllowDataLoss` forces immediate cutover and can discard unsent transactions.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: A planned failover waits for the secondary replica to harden all remaining primary log records (`RPO = 0`) before swapping roles, whereas `-AllowDataLoss` forces immediate cutover and can discard unsent transactions.
- **C:** Correct. Planned failover synchronizes pending log records before switching roles (`RPO = 0`), validating secondary firewall/Entra configs and `<fog>.database.windows.net` DNS redirection safely. In this scenario: A planned failover waits for the secondary replica to harden all remaining primary log records (`RPO = 0`) before swapping roles, whereas `-AllowDataLoss` forces immediate cutover and can discard unsent transactions.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: A planned failover waits for the secondary replica to harden all remaining primary log records (`RPO = 0`) before swapping roles, whereas `-AllowDataLoss` forces immediate cutover and can discard unsent transactions.

### Question 74 — B

Answer: No — taking an ad-hoc non-`COPY_ONLY` full backup resets the differential base and breaks downstream differential restores. User-initiated backups on Azure SQL Managed Instance only allow `WITH COPY_ONLY` (and on SQL Server AGs/VMs omitting `COPY_ONLY` resets the differential base LSN and breaks subsequent differential restores). A standard `BACKUP DATABASE` updates the differential base LSN; ad-hoc exports on SQL Managed Instance or Availability Groups must specify `WITH COPY_ONLY` to preserve the backup chain. Local study-map skill 5.4 (Recommend Backup & Restore Strategies (`COPY_ONLY` on MI/AGs and Azure Backup SQL-Aware Policies on VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated backups, COPY_ONLY backups, and Azure Backup for SQL Server in Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-overview).

- **A:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: User-initiated backups on Azure SQL Managed Instance only allow `WITH COPY_ONLY` (and on SQL Server AGs/VMs omitting `COPY_ONLY` resets the differential base LSN and breaks subsequent differential restores).
- **B:** Correct. A standard `BACKUP DATABASE` updates the differential base LSN; ad-hoc exports on SQL Managed Instance or Availability Groups must specify `WITH COPY_ONLY` to preserve the backup chain. In this scenario: User-initiated backups on Azure SQL Managed Instance only allow `WITH COPY_ONLY` (and on SQL Server AGs/VMs omitting `COPY_ONLY` resets the differential base LSN and breaks subsequent differential restores).
- **C:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: User-initiated backups on Azure SQL Managed Instance only allow `WITH COPY_ONLY` (and on SQL Server AGs/VMs omitting `COPY_ONLY` resets the differential base LSN and breaks subsequent differential restores).
- **D:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: User-initiated backups on Azure SQL Managed Instance only allow `WITH COPY_ONLY` (and on SQL Server AGs/VMs omitting `COPY_ONLY` resets the differential base LSN and breaks subsequent differential restores).

### Question 75 — B

Answer: Use `BACKUP DATABASE ... WITH COPY_ONLY` for ad-hoc exports on SQL MI / AGs, and Azure Backup Recovery Services Vault SQL-aware policies (`15-min` log RPO) on SQL VMs. Azure Backup for SQL Server in Azure VMs installs the workload backup extension to orchestrate VSS/VDI SQL-aware backups with up to 15-minute RPO log frequency and automatic DB discovery. `COPY_ONLY` preserves the differential and log backup chain, while Azure Backup for SQL Server in Azure VMs automates application-consistent Full, Differential, and 15-minute Transaction Log backups. Local study-map skill 5.4 (Recommend Backup & Restore Strategies (`COPY_ONLY` on MI/AGs and Azure Backup SQL-Aware Policies on VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated backups, COPY_ONLY backups, and Azure Backup for SQL Server in Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-overview).

- **A:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Azure Backup for SQL Server in Azure VMs installs the workload backup extension to orchestrate VSS/VDI SQL-aware backups with up to 15-minute RPO log frequency and automatic DB discovery.
- **B:** Correct. `COPY_ONLY` preserves the differential and log backup chain, while Azure Backup for SQL Server in Azure VMs automates application-consistent Full, Differential, and 15-minute Transaction Log backups. In this scenario: Azure Backup for SQL Server in Azure VMs installs the workload backup extension to orchestrate VSS/VDI SQL-aware backups with up to 15-minute RPO log frequency and automatic DB discovery.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Azure Backup for SQL Server in Azure VMs installs the workload backup extension to orchestrate VSS/VDI SQL-aware backups with up to 15-minute RPO log frequency and automatic DB discovery.
- **D:** Incorrect for this requirement. A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs. Why the keyed choice wins: Azure Backup for SQL Server in Azure VMs installs the workload backup extension to orchestrate VSS/VDI SQL-aware backups with up to 15-minute RPO log frequency and automatic DB discovery.

### Question 76 — C

Answer: Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback. PITR restores the database to `14:16:00Z` as a brand-new side-by-side database on the same logical server (never overwriting `CartDB` in place), letting you copy `Promotions` back safely or rename databases. Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. Local study-map skill 5.5 (Perform Native Restores, Point-in-Time Restore (`1–35d` PITR), Deleted-DB Restore, and `ADR` Instant Rollback), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Point-in-time restore (PITR), Accelerated Database Recovery (ADR), and deleted DB restore (https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups).

- **A:** Incorrect for this requirement. Short-Term PITR caps at `35` days (`1–35` days); multi-year retention up to `10 years` with WORM deletion lock requires Long-Term Retention (`LTR`) with time-based immutability. Why the keyed choice wins: PITR restores the database to `14:16:00Z` as a brand-new side-by-side database on the same logical server (never overwriting `CartDB` in place), letting you copy `Promotions` back safely or rename databases.
- **B:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: PITR restores the database to `14:16:00Z` as a brand-new side-by-side database on the same logical server (never overwriting `CartDB` in place), letting you copy `Promotions` back safely or rename databases.
- **C:** Correct. Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. In this scenario: PITR restores the database to `14:16:00Z` as a brand-new side-by-side database on the same logical server (never overwriting `CartDB` in place), letting you copy `Promotions` back safely or rename databases.
- **D:** Incorrect for this requirement. LTR retains compliance backups up to 10 years independently of PITR, and locking time-based immutability prevents even Subscription Owners from deleting backups before expiry. Why the keyed choice wins: PITR restores the database to `14:16:00Z` as a brand-new side-by-side database on the same logical server (never overwriting `CartDB` in place), letting you copy `Promotions` back safely or rename databases.

### Question 77 — A

Answer: Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback. Accelerated Database Recovery (`ADR`) maintains a Persistent Version Store (`PVS`) and `sLog` so aborted transactions mark versions aborted instantaneously (`instantaneous transaction rollback`) regardless of batch size. Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. Local study-map skill 5.5 (Perform Native Restores, Point-in-Time Restore (`1–35d` PITR), Deleted-DB Restore, and `ADR` Instant Rollback), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Point-in-time restore (PITR), Accelerated Database Recovery (ADR), and deleted DB restore (https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups).

- **A:** Correct. Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. In this scenario: Accelerated Database Recovery (`ADR`) maintains a Persistent Version Store (`PVS`) and `sLog` so aborted transactions mark versions aborted instantaneously (`instantaneous transaction rollback`) regardless of batch size.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Accelerated Database Recovery (`ADR`) maintains a Persistent Version Store (`PVS`) and `sLog` so aborted transactions mark versions aborted instantaneously (`instantaneous transaction rollback`) regardless of batch size.
- **C:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Accelerated Database Recovery (`ADR`) maintains a Persistent Version Store (`PVS`) and `sLog` so aborted transactions mark versions aborted instantaneously (`instantaneous transaction rollback`) regardless of batch size.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Accelerated Database Recovery (`ADR`) maintains a Persistent Version Store (`PVS`) and `sLog` so aborted transactions mark versions aborted instantaneously (`instantaneous transaction rollback`) regardless of batch size.

### Question 78 — D, E

Answers: Configure an Azure SQL Long-Term Retention (`LTR`) policy (`WeeklyRetention`, `MonthlyRetention`, `YearlyRetention`, `WeekOfYear`) up to 10 years; Enable and lock time-based immutability (`WORM`) on the LTR backup policy so nobody can shorten retention or delete compliance backups early. Configure an Azure SQL Long-Term Retention (`LTR`) policy (`MonthlyRetention = P7Y`) and lock time-based immutability (`WORM`) on the LTR backup policy. Local study-map skill 5.6 (Configure Long-Term Backup Retention (`LTR` up to `10y`), Time-Based Immutable WORM Locks, and Storage Redundancy), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Long-term backup retention (LTR) and time-based immutable WORM backups in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/long-term-retention-overview).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure an Azure SQL Long-Term Retention (`LTR`) policy (`MonthlyRetention = P7Y`) and lock time-based immutability (`WORM`) on the LTR backup policy.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Configure an Azure SQL Long-Term Retention (`LTR`) policy (`MonthlyRetention = P7Y`) and lock time-based immutability (`WORM`) on the LTR backup policy.
- **C:** Incorrect for this requirement. Short-Term PITR caps at `35` days (`1–35` days); multi-year retention up to `10 years` with WORM deletion lock requires Long-Term Retention (`LTR`) with time-based immutability. Why the keyed choice wins: Configure an Azure SQL Long-Term Retention (`LTR`) policy (`MonthlyRetention = P7Y`) and lock time-based immutability (`WORM`) on the LTR backup policy.
- **D:** Correct. Once locked, time-based LTR immutability enforces write-once-read-many protection against ransomware or rogue privileged admins. In this scenario: Configure an Azure SQL Long-Term Retention (`LTR`) policy (`MonthlyRetention = P7Y`) and lock time-based immutability (`WORM`) on the LTR backup policy.
- **E:** Correct. LTR copies full backups into separate geo-redundant/zone-redundant Azure Blob tiers according to ISO-8601 duration policies (e.g., `P7Y`). In this scenario: Configure an Azure SQL Long-Term Retention (`LTR`) policy (`MonthlyRetention = P7Y`) and lock time-based immutability (`WORM`) on the LTR backup policy.

### Question 79 — D

Answer: Long-Term Retention (`LTR`) weekly/monthly/yearly backups up to `10 years` protected by a locked time-based immutable (`WORM`) policy and `RA-GRS` / `ZRS` backup storage. Specifying `GeoZone` (`GZRS` / `RA-GZRS`) replicates backup blobs synchronously across three Availability Zones in the primary region and asynchronously to the paired secondary region. LTR retains compliance backups up to 10 years independently of PITR, and locking time-based immutability prevents even Subscription Owners from deleting backups before expiry. Local study-map skill 5.6 (Configure Long-Term Backup Retention (`LTR` up to `10y`), Time-Based Immutable WORM Locks, and Storage Redundancy), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Long-term backup retention (LTR) and time-based immutable WORM backups in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/long-term-retention-overview).

- **A:** Incorrect for this requirement. Short-Term PITR caps at `35` days (`1–35` days); multi-year retention up to `10 years` with WORM deletion lock requires Long-Term Retention (`LTR`) with time-based immutability. Why the keyed choice wins: Specifying `GeoZone` (`GZRS` / `RA-GZRS`) replicates backup blobs synchronously across three Availability Zones in the primary region and asynchronously to the paired secondary region.
- **B:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Specifying `GeoZone` (`GZRS` / `RA-GZRS`) replicates backup blobs synchronously across three Availability Zones in the primary region and asynchronously to the paired secondary region.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Specifying `GeoZone` (`GZRS` / `RA-GZRS`) replicates backup blobs synchronously across three Availability Zones in the primary region and asynchronously to the paired secondary region.
- **D:** Correct. LTR retains compliance backups up to 10 years independently of PITR, and locking time-based immutability prevents even Subscription Owners from deleting backups before expiry. In this scenario: Specifying `GeoZone` (`GZRS` / `RA-GZRS`) replicates backup blobs synchronously across three Availability Zones in the primary region and asynchronously to the paired secondary region.

### Question 80 — A, E

Answers: Create a SQL Server `CREDENTIAL` (`IDENTITY = 'Managed Identity'` or `'SHARED ACCESS SIGNATURE'`) matching the Azure Blob container URL; Stripe `BACKUP DATABASE` across multiple `TO URL = 'https://...bak'` block blob targets with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`. Create a SQL `CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE`) for the Blob container and stripe `BACKUP DATABASE` across multiple `TO URL = ...` block blob targets with compression. Local study-map skill 5.7 (Back Up to and Restore from Azure Blob Storage URL Using T-SQL Stripes (`TO URL`) and Managed Identity / SAS), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server backup to URL and restore from Azure Blob Storage with Managed Identity or SAS (https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url-azure-blob-storage).

- **A:** Correct. Multiple `URL` targets write to Azure Block Blobs in parallel, scaling single backups up to ~12.8 TB (`64` stripes) with maximum throughput. In this scenario: Create a SQL `CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE`) for the Blob container and stripe `BACKUP DATABASE` across multiple `TO URL = ...` block blob targets with compression.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Create a SQL `CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE`) for the Blob container and stripe `BACKUP DATABASE` across multiple `TO URL = ...` block blob targets with compression.
- **C:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Create a SQL `CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE`) for the Blob container and stripe `BACKUP DATABASE` across multiple `TO URL = ...` block blob targets with compression.
- **D:** Incorrect for this requirement. A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs. Why the keyed choice wins: Create a SQL `CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE`) for the Blob container and stripe `BACKUP DATABASE` across multiple `TO URL = ...` block blob targets with compression.
- **E:** Correct. SQL Server and SQL MI authenticate `BACKUP TO URL` / `RESTORE FROM URL` requests to Azure Storage via a server-level credential. In this scenario: Create a SQL `CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE`) for the Blob container and stripe `BACKUP DATABASE` across multiple `TO URL = ...` block blob targets with compression.

### Question 81 — C

Answer: Striped T-SQL `BACKUP DATABASE ... TO URL = ...` across up to 64 block blobs (`MAXTRANSFERSIZE`, `COMPRESSION`) authenticated via `Managed Identity` or `SHARED ACCESS SIGNATURE` Credential. Using `IDENTITY = 'SHARED ACCESS SIGNATURE'` with the SAS token (stripped of any leading `?`) creates a container-scoped credential enabling `BACKUP TO URL` against Azure Block Blobs. Backing up to multiple URLs creates block blobs supporting up to ~12.8 TB striped backups (`200 GB+` per blob, unlike legacy single-page-blob 1 TB limits) using `CREATE CREDENTIAL`. Local study-map skill 5.7 (Back Up to and Restore from Azure Blob Storage URL Using T-SQL Stripes (`TO URL`) and Managed Identity / SAS), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server backup to URL and restore from Azure Blob Storage with Managed Identity or SAS (https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url-azure-blob-storage).

- **A:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: Using `IDENTITY = 'SHARED ACCESS SIGNATURE'` with the SAS token (stripped of any leading `?`) creates a container-scoped credential enabling `BACKUP TO URL` against Azure Block Blobs.
- **B:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Using `IDENTITY = 'SHARED ACCESS SIGNATURE'` with the SAS token (stripped of any leading `?`) creates a container-scoped credential enabling `BACKUP TO URL` against Azure Block Blobs.
- **C:** Correct. Backing up to multiple URLs creates block blobs supporting up to ~12.8 TB striped backups (`200 GB+` per blob, unlike legacy single-page-blob 1 TB limits) using `CREATE CREDENTIAL`. In this scenario: Using `IDENTITY = 'SHARED ACCESS SIGNATURE'` with the SAS token (stripped of any leading `?`) creates a container-scoped credential enabling `BACKUP TO URL` against Azure Block Blobs.
- **D:** Incorrect for this requirement. A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs. Why the keyed choice wins: Using `IDENTITY = 'SHARED ACCESS SIGNATURE'` with the SAS token (stripped of any leading `?`) creates a container-scoped credential enabling `BACKUP TO URL` against Azure Block Blobs.

### Question 82 — D, E

Answers: Connect OLTP write traffic to `<fog>.database.windows.net` and read-only analytics to `<fog>.secondary.database.windows.net`; Configure `ReadWriteFailoverPolicy = Automatic` with `GracePeriodWithDataLossHours >= 1` so transient blips do not trigger premature lossy failover. Point OLTP apps to `fog-kestrel.database.windows.net` and read-only BI to `fog-kestrel.secondary.database.windows.net`, and set `GracePeriodWithDataLossHours >= 1` alongside `ReadWriteFailoverPolicy = Automatic`. Local study-map skill 5.8 (Configure Failover Groups (`<fog>.database.windows.net`, Grace Period) vs Active Geo-Replication (`4` Replicas)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Failover groups and active geo-replication in Azure SQL Database and SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Point OLTP apps to `fog-kestrel.database.windows.net` and read-only BI to `fog-kestrel.secondary.database.windows.net`, and set `GracePeriodWithDataLossHours >= 1` alongside `ReadWriteFailoverPolicy = Automatic`.
- **B:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: Point OLTP apps to `fog-kestrel.database.windows.net` and read-only BI to `fog-kestrel.secondary.database.windows.net`, and set `GracePeriodWithDataLossHours >= 1` alongside `ReadWriteFailoverPolicy = Automatic`.
- **C:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Point OLTP apps to `fog-kestrel.database.windows.net` and read-only BI to `fog-kestrel.secondary.database.windows.net`, and set `GracePeriodWithDataLossHours >= 1` alongside `ReadWriteFailoverPolicy = Automatic`.
- **D:** Correct. The grace period controls how long Azure waits during an unrecoverable primary region outage before forcing an automatic failover if async log lag remains. In this scenario: Point OLTP apps to `fog-kestrel.database.windows.net` and read-only BI to `fog-kestrel.secondary.database.windows.net`, and set `GracePeriodWithDataLossHours >= 1` alongside `ReadWriteFailoverPolicy = Automatic`.
- **E:** Correct. Failover Group listener endpoints abstract underlying regional server names and automatically redirect read-write and read-only connections after failover. In this scenario: Point OLTP apps to `fog-kestrel.database.windows.net` and read-only BI to `fog-kestrel.secondary.database.windows.net`, and set `GracePeriodWithDataLossHours >= 1` alongside `ReadWriteFailoverPolicy = Automatic`.

### Question 83 — B

Answer: Failover Groups for automatic multi-database failover behind stable `<fog>.database.windows.net` / `.secondary` listeners vs Active Geo-Replication for up to 4 readable secondaries. A Failover Group links one primary logical server to a single secondary partner server (`1` secondary), whereas Active Geo-Replication supports up to `4` concurrent readable secondaries per database (and can coexist with a Failover Group on one secondary). Failover Groups fail over coupled databases together and redirect connection strings automatically (`GracePeriodWithDataLossHours >= 1`), whereas Active Geo-Replication supports up to 4 secondaries per DB without automatic listener redirection. Local study-map skill 5.8 (Configure Failover Groups (`<fog>.database.windows.net`, Grace Period) vs Active Geo-Replication (`4` Replicas)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Failover groups and active geo-replication in Azure SQL Database and SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db).

- **A:** Incorrect for this requirement. LTR retains compliance backups up to 10 years independently of PITR, and locking time-based immutability prevents even Subscription Owners from deleting backups before expiry. Why the keyed choice wins: A Failover Group links one primary logical server to a single secondary partner server (`1` secondary), whereas Active Geo-Replication supports up to `4` concurrent readable secondaries per database (and can coexist with a Failover Group on one secondary).
- **B:** Correct. Failover Groups fail over coupled databases together and redirect connection strings automatically (`GracePeriodWithDataLossHours >= 1`), whereas Active Geo-Replication supports up to 4 secondaries per DB without automatic listener redirection. In this scenario: A Failover Group links one primary logical server to a single secondary partner server (`1` secondary), whereas Active Geo-Replication supports up to `4` concurrent readable secondaries per database (and can coexist with a Failover Group on one secondary).
- **C:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: A Failover Group links one primary logical server to a single secondary partner server (`1` secondary), whereas Active Geo-Replication supports up to `4` concurrent readable secondaries per database (and can coexist with a Failover Group on one secondary).
- **D:** Incorrect for this requirement. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. Why the keyed choice wins: A Failover Group links one primary logical server to a single secondary partner server (`1` secondary), whereas Active Geo-Replication supports up to `4` concurrent readable secondaries per database (and can coexist with a Failover Group on one secondary).

### Question 84 — A

Answer: Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`. A Distributed Network Name (`DNN`) listener registers all replica IPs in DNS without ILB probe delays, and `MultiSubnetFailover=True` makes ADO.NET/ODBC drivers attempt all IPs in parallel. Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). Local study-map skill 5.9 (Configure Always On Availability Groups on SQL MI and Azure VMs (`Cloud Witness`, `DNN`, `ILB` Port `59999`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On availability groups on SQL Server on Azure VMs (Cloud Witness, DNN, ILB) (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/availability-group-overview).

- **A:** Correct. Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). In this scenario: A Distributed Network Name (`DNN`) listener registers all replica IPs in DNS without ILB probe delays, and `MultiSubnetFailover=True` makes ADO.NET/ODBC drivers attempt all IPs in parallel.
- **B:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: A Distributed Network Name (`DNN`) listener registers all replica IPs in DNS without ILB probe delays, and `MultiSubnetFailover=True` makes ADO.NET/ODBC drivers attempt all IPs in parallel.
- **C:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: A Distributed Network Name (`DNN`) listener registers all replica IPs in DNS without ILB probe delays, and `MultiSubnetFailover=True` makes ADO.NET/ODBC drivers attempt all IPs in parallel.
- **D:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: A Distributed Network Name (`DNN`) listener registers all replica IPs in DNS without ILB probe delays, and `MultiSubnetFailover=True` makes ADO.NET/ODBC drivers attempt all IPs in parallel.

### Question 85 — A

Answer: Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`. An Azure Cloud Witness backed by a standard Azure Storage Account provides an arbitrating quorum vote for pennies per month without maintaining or patching a third File Share Witness VM. Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). Local study-map skill 5.9 (Configure Always On Availability Groups on SQL MI and Azure VMs (`Cloud Witness`, `DNN`, `ILB` Port `59999`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On availability groups on SQL Server on Azure VMs (Cloud Witness, DNN, ILB) (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/availability-group-overview).

- **A:** Correct. Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). In this scenario: An Azure Cloud Witness backed by a standard Azure Storage Account provides an arbitrating quorum vote for pennies per month without maintaining or patching a third File Share Witness VM.
- **B:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: An Azure Cloud Witness backed by a standard Azure Storage Account provides an arbitrating quorum vote for pennies per month without maintaining or patching a third File Share Witness VM.
- **C:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: An Azure Cloud Witness backed by a standard Azure Storage Account provides an arbitrating quorum vote for pennies per month without maintaining or patching a third File Share Witness VM.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: An Azure Cloud Witness backed by a standard Azure Storage Account provides an arbitrating quorum vote for pennies per month without maintaining or patching a third File Share Witness VM.

### Question 86 — B

Answer: Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`). Provision `ZRS` Premium SSD Azure Shared Disks (`maxShares = 2`) attached to both SQL Server Azure VMs across Availability Zones to provide SCSI Persistent Reservation shared block storage for the FCI. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. Local study-map skill 5.10 (Configure Always On Failover Cluster Instances (`Azure Shared Disks` `ZRS`) and T-SQL Log Shipping on Azure VMs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On Failover Cluster Instances (Azure Shared Disks) and Log Shipping on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/failover-cluster-instance-overview).

- **A:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: Provision `ZRS` Premium SSD Azure Shared Disks (`maxShares = 2`) attached to both SQL Server Azure VMs across Availability Zones to provide SCSI Persistent Reservation shared block storage for the FCI.
- **B:** Correct. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. In this scenario: Provision `ZRS` Premium SSD Azure Shared Disks (`maxShares = 2`) attached to both SQL Server Azure VMs across Availability Zones to provide SCSI Persistent Reservation shared block storage for the FCI.
- **C:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: Provision `ZRS` Premium SSD Azure Shared Disks (`maxShares = 2`) attached to both SQL Server Azure VMs across Availability Zones to provide SCSI Persistent Reservation shared block storage for the FCI.
- **D:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Provision `ZRS` Premium SSD Azure Shared Disks (`maxShares = 2`) attached to both SQL Server Azure VMs across Availability Zones to provide SCSI Persistent Reservation shared block storage for the FCI.

### Question 87 — B

Answer: Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`). Restoring transaction logs `WITH STANDBY = '...\undo.bak'` rolls uncommitted transactions into an undo file so the warm Log Shipping secondary can accept read-only queries between restore intervals. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. Local study-map skill 5.10 (Configure Always On Failover Cluster Instances (`Azure Shared Disks` `ZRS`) and T-SQL Log Shipping on Azure VMs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On Failover Cluster Instances (Azure Shared Disks) and Log Shipping on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/failover-cluster-instance-overview).

- **A:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Restoring transaction logs `WITH STANDBY = '...\undo.bak'` rolls uncommitted transactions into an undo file so the warm Log Shipping secondary can accept read-only queries between restore intervals.
- **B:** Correct. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. In this scenario: Restoring transaction logs `WITH STANDBY = '...\undo.bak'` rolls uncommitted transactions into an undo file so the warm Log Shipping secondary can accept read-only queries between restore intervals.
- **C:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Restoring transaction logs `WITH STANDBY = '...\undo.bak'` rolls uncommitted transactions into an undo file so the warm Log Shipping secondary can accept read-only queries between restore intervals.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Restoring transaction logs `WITH STANDBY = '...\undo.bak'` rolls uncommitted transactions into an undo file so the warm Log Shipping secondary can accept read-only queries between restore intervals.

### Question 88 — D

Answer: Query `sys.dm_hadr_database_replica_states` (`synchronization_state_desc`, `log_send_queue_size`, `redo_queue_size`) and `sys.dm_geo_replication_link_status`, plus verify NSG probe port `59999`. Near-zero `log_send_queue_size` proves network transport is healthy, while a huge `redo_queue_size` means the secondary replica's redo threads are bottlenecked by slow secondary disk I/O, CPU saturation, or long-running reporting `SCH-S` locks blocking redo. High `log_send_queue_size` indicates network bottlenecks between primary and secondary, high `redo_queue_size` indicates slow redo I/O/CPU or long-running read queries on the secondary, and blocked ILB probe port `59999` breaks AG listener routing. Local study-map skill 5.11 (Monitor and Troubleshoot HA/DR Health (`sys.dm_hadr_database_replica_states`, `redo_queue_size`, `log_send_queue_size`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor and troubleshoot Always On availability groups and geo-replication health (https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/monitor-availability-groups-transact-sql).

- **A:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: Near-zero `log_send_queue_size` proves network transport is healthy, while a huge `redo_queue_size` means the secondary replica's redo threads are bottlenecked by slow secondary disk I/O, CPU saturation, or long-running reporting `SCH-S` locks blocking redo.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Near-zero `log_send_queue_size` proves network transport is healthy, while a huge `redo_queue_size` means the secondary replica's redo threads are bottlenecked by slow secondary disk I/O, CPU saturation, or long-running reporting `SCH-S` locks blocking redo.
- **C:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Near-zero `log_send_queue_size` proves network transport is healthy, while a huge `redo_queue_size` means the secondary replica's redo threads are bottlenecked by slow secondary disk I/O, CPU saturation, or long-running reporting `SCH-S` locks blocking redo.
- **D:** Correct. High `log_send_queue_size` indicates network bottlenecks between primary and secondary, high `redo_queue_size` indicates slow redo I/O/CPU or long-running read queries on the secondary, and blocked ILB probe port `59999` breaks AG listener routing. In this scenario: Near-zero `log_send_queue_size` proves network transport is healthy, while a huge `redo_queue_size` means the secondary replica's redo threads are bottlenecked by slow secondary disk I/O, CPU saturation, or long-running reporting `SCH-S` locks blocking redo.

### Question 89 — A, D, F

Answers: Query fleet-wide SQL Server version, edition, and backup status across hybrid servers via Azure Resource Graph Explorer; Enable automated SQL Best Practices Assessments and Microsoft Defender for SQL via the Azure Arc SQL Server extension; Switch eligible hybrid SQL Server instances to hourly Azure Arc pay-as-you-go billing instead of upfront core licenses. SQL Server enabled by Azure Arc unlocks cross-fleet KQL inventory in Azure Resource Graph, automated SQL Best Practices Assessments with Defender integration, and hourly pay-as-you-go billing. Local study-map skill 1.3 (Identify Use Cases for SQL Server Enabled by Azure Arc and SQL Database in Microsoft Fabric), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server enabled by Azure Arc and SQL database in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/database/sql/overview).

- **A:** Correct. Azure Arc allows variable-workload or seasonal SQL Server hosts outside Azure to be billed hourly through an Azure subscription. In this scenario: SQL Server enabled by Azure Arc unlocks cross-fleet KQL inventory in Azure Resource Graph, automated SQL Best Practices Assessments with Defender integration, and hourly pay-as-you-go billing.
- **B:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: SQL Server enabled by Azure Arc unlocks cross-fleet KQL inventory in Azure Resource Graph, automated SQL Best Practices Assessments with Defender integration, and hourly pay-as-you-go billing.
- **C:** Incorrect for this requirement. SQL database in Microsoft Fabric enforces Microsoft Entra authentication exclusively (SQL logins are unsupported) and manages backups/OneLake mirroring automatically as SaaS. Why the keyed choice wins: SQL Server enabled by Azure Arc unlocks cross-fleet KQL inventory in Azure Resource Graph, automated SQL Best Practices Assessments with Defender integration, and hourly pay-as-you-go billing.
- **D:** Correct. SQL Server enabled by Azure Arc projects on-premises and multicloud instance metadata into Azure Resource Manager for KQL-based Azure Resource Graph inventory queries. In this scenario: SQL Server enabled by Azure Arc unlocks cross-fleet KQL inventory in Azure Resource Graph, automated SQL Best Practices Assessments with Defender integration, and hourly pay-as-you-go billing.
- **E:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: SQL Server enabled by Azure Arc unlocks cross-fleet KQL inventory in Azure Resource Graph, automated SQL Best Practices Assessments with Defender integration, and hourly pay-as-you-go billing.
- **F:** Correct. The Azure Extension for SQL Server runs recurring configuration assessments against Microsoft Support rules and integrates Defender vulnerability/threat detection. In this scenario: SQL Server enabled by Azure Arc unlocks cross-fleet KQL inventory in Azure Resource Graph, automated SQL Best Practices Assessments with Defender integration, and hourly pay-as-you-go billing.

### Question 90 — A

Answer: SQL Server enabled by Azure Arc (`Microsoft.AzureArcData/sqlServerInstances`). SQL Server 2022 enabled by Azure Arc integrates on-premises instances with Microsoft Entra ID via the Azure Extension for SQL Server without migrating compute to Azure. Azure Arc projects on-premises and multicloud SQL Server instances into Azure for Resource Graph inventory, automated Best Practices Assessments, Entra auth (SQL 2022+), Defender, and PAYG billing. Local study-map skill 1.5 (Deploy Hybrid SQL Server Solutions and Manage Patching (`SQL IaaS Agent Extension` & `Azure Update Manager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server IaaS Agent Extension, Automated Patching, and Azure Update Manager (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-agent-extension-manually-register-single-vm).

- **A:** Correct. Azure Arc projects on-premises and multicloud SQL Server instances into Azure for Resource Graph inventory, automated Best Practices Assessments, Entra auth (SQL 2022+), Defender, and PAYG billing. In this scenario: SQL Server 2022 enabled by Azure Arc integrates on-premises instances with Microsoft Entra ID via the Azure Extension for SQL Server without migrating compute to Azure.
- **B:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: SQL Server 2022 enabled by Azure Arc integrates on-premises instances with Microsoft Entra ID via the Azure Extension for SQL Server without migrating compute to Azure.
- **C:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: SQL Server 2022 enabled by Azure Arc integrates on-premises instances with Microsoft Entra ID via the Azure Extension for SQL Server without migrating compute to Azure.
- **D:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: SQL Server 2022 enabled by Azure Arc integrates on-premises instances with Microsoft Entra ID via the Azure Extension for SQL Server without migrating compute to Azure.

### Question 91 — D

Answer: Azure Migrate (`Azure SQL` assessment) and the Azure SQL Migration extension for Azure Data Studio / VS Code. With standalone Data Migration Assistant (DMA) retired in July 2025, Azure Migrate and the Azure SQL Migration extension for Azure Data Studio / VS Code provide readiness assessments and SKU right-sizing. Following Data Migration Assistant (DMA) retirement, Azure Migrate and the Azure SQL Migration extension assess compatibility blockers, feature parity, and performance-based vCore SKU right-sizing. Local study-map skill 1.10 (Evaluate Migration Requirements, Offline vs Online Strategies, and SKU Sizing via Azure Migrate & ADS), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Assess and plan SQL Server migrations using Azure Migrate and Azure SQL Migration extension (https://learn.microsoft.com/en-us/data-migration/sql-server/managed-instance/overview).

- **A:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: With standalone Data Migration Assistant (DMA) retired in July 2025, Azure Migrate and the Azure SQL Migration extension for Azure Data Studio / VS Code provide readiness assessments and SKU right-sizing.
- **B:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: With standalone Data Migration Assistant (DMA) retired in July 2025, Azure Migrate and the Azure SQL Migration extension for Azure Data Studio / VS Code provide readiness assessments and SKU right-sizing.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: With standalone Data Migration Assistant (DMA) retired in July 2025, Azure Migrate and the Azure SQL Migration extension for Azure Data Studio / VS Code provide readiness assessments and SKU right-sizing.
- **D:** Correct. Following Data Migration Assistant (DMA) retirement, Azure Migrate and the Azure SQL Migration extension assess compatibility blockers, feature parity, and performance-based vCore SKU right-sizing. In this scenario: With standalone Data Migration Assistant (DMA) retired in July 2025, Azure Migrate and the Azure SQL Migration extension for Azure Data Studio / VS Code provide readiness assessments and SKU right-sizing.

### Question 92 — A, E

Answers: Execute `sys.sp_query_store_force_plan @query_id, @plan_id` to pin the historical low-latency execution plan immediately; Execute `sys.sp_query_store_set_hints @query_id, N'OPTION (RECOMPILE)'` (or `MAXDOP` / memory grant hints) without redeploying code. `sys.sp_query_store_force_plan` pins a known-good historical execution plan, while `sys.sp_query_store_set_hints` injects query hints such as `OPTION (RECOMPILE)` directly onto a `query_id`. Local study-map skill 3.5 (Configure and Monitor Query Store, Force Regressed Plans (`sp_query_store_force_plan`), and Set Query Store Hints), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance by using the Query Store, plan forcing, and Query Store hints (https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store).

- **A:** Correct. Query Store hints attach `OPTION (...)` query hints directly to a `query_id` in Azure SQL DB, SQL MI, and SQL Server 2022+ when app code cannot be edited. In this scenario: `sys.sp_query_store_force_plan` pins a known-good historical execution plan, while `sys.sp_query_store_set_hints` injects query hints such as `OPTION (RECOMPILE)` directly onto a `query_id`.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `sys.sp_query_store_force_plan` pins a known-good historical execution plan, while `sys.sp_query_store_set_hints` injects query hints such as `OPTION (RECOMPILE)` directly onto a `query_id`.
- **C:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: `sys.sp_query_store_force_plan` pins a known-good historical execution plan, while `sys.sp_query_store_set_hints` injects query hints such as `OPTION (RECOMPILE)` directly onto a `query_id`.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: `sys.sp_query_store_force_plan` pins a known-good historical execution plan, while `sys.sp_query_store_set_hints` injects query hints such as `OPTION (RECOMPILE)` directly onto a `query_id`.
- **E:** Correct. `sp_query_store_force_plan` instructs the optimizer to compile plans matching the forced `plan_id` shape without modifying application T-SQL. In this scenario: `sys.sp_query_store_force_plan` pins a known-good historical execution plan, while `sys.sp_query_store_set_hints` injects query hints such as `OPTION (RECOMPILE)` directly onto a `query_id`.

### Question 93 — A

Answer: Read Committed Snapshot Isolation (`READ_COMMITTED_SNAPSHOT = ON`) combined with Optimized Locking (`TID` locking + Lock After Qualification `LAQ`). Enabling `READ_COMMITTED_SNAPSHOT = ON` (`RCSI`) provides row-versioned non-blocking reads, while Optimized Locking in Azure SQL Database combines `TID` locking with Lock After Qualification (`LAQ`). `RCSI` uses row versioning so readers never block writers (`LCK_M_S`), while Optimized Locking in Azure SQL DB replaces thousands of row/page locks with a single Transaction ID lock and `LAQ`. Local study-map skill 3.6 (Identify and Resolve Session Blocking (`RCSI`, `Optimized Locking` `TID`/`LAQ`) and Deadlocks (`xml_deadlock_report`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Understand and resolve Azure SQL blocking problems, deadlocks, RCSI, and Optimized Locking (https://learn.microsoft.com/en-us/azure/azure-sql/database/analyze-prevent-deadlocks).

- **A:** Correct. `RCSI` uses row versioning so readers never block writers (`LCK_M_S`), while Optimized Locking in Azure SQL DB replaces thousands of row/page locks with a single Transaction ID lock and `LAQ`. In this scenario: Enabling `READ_COMMITTED_SNAPSHOT = ON` (`RCSI`) provides row-versioned non-blocking reads, while Optimized Locking in Azure SQL Database combines `TID` locking with Lock After Qualification (`LAQ`).
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Enabling `READ_COMMITTED_SNAPSHOT = ON` (`RCSI`) provides row-versioned non-blocking reads, while Optimized Locking in Azure SQL Database combines `TID` locking with Lock After Qualification (`LAQ`).
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Enabling `READ_COMMITTED_SNAPSHOT = ON` (`RCSI`) provides row-versioned non-blocking reads, while Optimized Locking in Azure SQL Database combines `TID` locking with Lock After Qualification (`LAQ`).
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Enabling `READ_COMMITTED_SNAPSHOT = ON` (`RCSI`) provides row-versioned non-blocking reads, while Optimized Locking in Azure SQL Database combines `TID` locking with Lock After Qualification (`LAQ`).

### Question 94 — A, C

Answers: Assign a User-Assigned Managed Identity to the Elastic Job Agent and create a contained `FROM EXTERNAL PROVIDER` user on target databases; Add logical SQL servers or Elastic Pools (`include` / `exclude` members) to an Elastic Job Target Group so new tenant DBs inherit jobs automatically. Assign a User-Assigned Managed Identity (`UAMI`) with contained `FROM EXTERNAL PROVIDER` users on target databases, and add the logical SQL servers/Elastic Pools to the Elastic Job Target Group so new DBs inherit jobs automatically. Local study-map skill 4.6 (Create and Configure Azure SQL Database Elastic Jobs Across Target Groups Using User-Assigned Managed Identity), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Elastic jobs in Azure SQL Database with Managed Identity authentication (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-jobs-overview).

- **A:** Correct. Targeting at the server or Elastic Pool level dynamically discovers newly created tenant databases on each job run without editing job definitions. In this scenario: Assign a User-Assigned Managed Identity (`UAMI`) with contained `FROM EXTERNAL PROVIDER` users on target databases, and add the logical SQL servers/Elastic Pools to the Elastic Job Target Group so new DBs inherit jobs automatically.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Assign a User-Assigned Managed Identity (`UAMI`) with contained `FROM EXTERNAL PROVIDER` users on target databases, and add the logical SQL servers/Elastic Pools to the Elastic Job Target Group so new DBs inherit jobs automatically.
- **C:** Correct. Modern Elastic Jobs authenticate across Azure SQL servers and subscriptions using a User-Assigned Managed Identity without managing SQL credential passwords. In this scenario: Assign a User-Assigned Managed Identity (`UAMI`) with contained `FROM EXTERNAL PROVIDER` users on target databases, and add the logical SQL servers/Elastic Pools to the Elastic Job Target Group so new DBs inherit jobs automatically.
- **D:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: Assign a User-Assigned Managed Identity (`UAMI`) with contained `FROM EXTERNAL PROVIDER` users on target databases, and add the logical SQL servers/Elastic Pools to the Elastic Job Target Group so new DBs inherit jobs automatically.
- **E:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Assign a User-Assigned Managed Identity (`UAMI`) with contained `FROM EXTERNAL PROVIDER` users on target databases, and add the logical SQL servers/Elastic Pools to the Elastic Job Target Group so new DBs inherit jobs automatically.

### Question 95 — C

Answer: Azure SQL Database Hyperscale tier with compute-isolated Named Replicas. Hyperscale supports databases up to 100 TB via page servers and attaches Named Replicas with dedicated compute nodes reading the same storage pages without impacting OLTP checkout vCores. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Local study-map skill 1.1 (Recommend an Azure SQL Offering (SQL Database, SQL Managed Instance, or SQL Server on Azure VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Compare Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview).

- **A:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Hyperscale supports databases up to 100 TB via page servers and attaches Named Replicas with dedicated compute nodes reading the same storage pages without impacting OLTP checkout vCores.
- **B:** Incorrect for this requirement. SQL Server on Azure VMs (IaaS) provides full OS access, custom third-party drivers, legacy SQL Server version pinning, SSIS/SSRS/SSAS co-hosting, and `Ebdsv5` high remote storage throughput. Why the keyed choice wins: Hyperscale supports databases up to 100 TB via page servers and attaches Named Replicas with dedicated compute nodes reading the same storage pages without impacting OLTP checkout vCores.
- **C:** Correct. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. In this scenario: Hyperscale supports databases up to 100 TB via page servers and attaches Named Replicas with dedicated compute nodes reading the same storage pages without impacting OLTP checkout vCores.
- **D:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Hyperscale supports databases up to 100 TB via page servers and attaches Named Replicas with dedicated compute nodes reading the same storage pages without impacting OLTP checkout vCores.

### Question 96 — C

Answer: Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled. The vCore Serverless compute tier automatically scales vCores during daytime QA tests and pauses compute billing after the configured auto-pause delay (`>= 1 hour`), billing only storage while paused. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Local study-map skill 1.6 (Configure Azure SQL Database for Scale and Performance (`Serverless`, `Hyperscale` Named Replicas, `Elastic Pools`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure SQL Database vCore, Serverless, Hyperscale, and Elastic Pools (https://learn.microsoft.com/en-us/azure/azure-sql/database/service-tiers-vcore).

- **A:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: The vCore Serverless compute tier automatically scales vCores during daytime QA tests and pauses compute billing after the configured auto-pause delay (`>= 1 hour`), billing only storage while paused.
- **B:** Incorrect for this requirement. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. Why the keyed choice wins: The vCore Serverless compute tier automatically scales vCores during daytime QA tests and pauses compute billing after the configured auto-pause delay (`>= 1 hour`), billing only storage while paused.
- **C:** Correct. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. In this scenario: The vCore Serverless compute tier automatically scales vCores during daytime QA tests and pauses compute billing after the configured auto-pause delay (`>= 1 hour`), billing only storage while paused.
- **D:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: The vCore Serverless compute tier automatically scales vCores during daytime QA tests and pauses compute billing after the configured auto-pause delay (`>= 1 hour`), billing only storage while paused.

### Question 97 — A

Answer: Table partitioning using `CREATE PARTITION FUNCTION ... AS RANGE RIGHT` with aligned indexes and `ALTER TABLE ... SWITCH`. Using `RANGE RIGHT` ensures each boundary timestamp serves as the inclusive lower bound of the new monthly partition, avoiding `23:59:59.9999999` precision bugs and simplifying aligned `SWITCH` archival. `RANGE RIGHT` places each upper-boundary date value cleanly as the lower bound of its own monthly/daily partition, enabling metadata-only `SWITCH` archival when indexes are aligned. Local study-map skill 1.9 (Configure Table Partitioning Alignment and Data Compression (`ROW`, `PAGE`, `COLUMNSTORE`, `COLUMNSTORE_ARCHIVE`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure table partitioning and row/page/columnstore data compression (https://learn.microsoft.com/en-us/sql/relational-databases/data-compression/data-compression).

- **A:** Correct. `RANGE RIGHT` places each upper-boundary date value cleanly as the lower bound of its own monthly/daily partition, enabling metadata-only `SWITCH` archival when indexes are aligned. In this scenario: Using `RANGE RIGHT` ensures each boundary timestamp serves as the inclusive lower bound of the new monthly partition, avoiding `23:59:59.9999999` precision bugs and simplifying aligned `SWITCH` archival.
- **B:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Using `RANGE RIGHT` ensures each boundary timestamp serves as the inclusive lower bound of the new monthly partition, avoiding `23:59:59.9999999` precision bugs and simplifying aligned `SWITCH` archival.
- **C:** Incorrect for this requirement. `ListShardMap` maps discrete `TenantId` keys and `RangeShardMap` maps contiguous ID spans to independent Azure SQL Databases, routing data-dependent connections directly from the app tier. Why the keyed choice wins: Using `RANGE RIGHT` ensures each boundary timestamp serves as the inclusive lower bound of the new monthly partition, avoiding `23:59:59.9999999` precision bugs and simplifying aligned `SWITCH` archival.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Using `RANGE RIGHT` ensures each boundary timestamp serves as the inclusive lower bound of the new monthly partition, avoiding `23:59:59.9999999` precision bugs and simplifying aligned `SWITCH` archival.

### Question 98 — D

Answer: Always Encrypted with VBS or Intel SGX secure enclaves (`ALLOW_ENCLAVE_COMPUTATIONS` + `Column Encryption Setting=Enabled`). Always Encrypted with VBS or SGX secure enclaves (`ALLOW_ENCLAVE_COMPUTATIONS`) evaluates `LIKE` predicates inside an isolated enclave memory region without revealing keys or plaintext to the SQL engine DBA. Secure enclaves delegate column decryption into an isolated memory region inside SQL, unlocking `LIKE`, `<`, `>`, `ORDER BY`, and fast in-place initial encryption without exposing plaintext to DBAs. Local study-map skill 2.9 (Implement Always Encrypted (`Deterministic` vs `Randomized`) and Always Encrypted with VBS/SGX Secure Enclaves), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always Encrypted and Always Encrypted with secure enclaves (https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves).

- **A:** Incorrect for this requirement. Always Encrypted keeps Column Master Keys on trusted clients/Key Vault; `Randomized` produces distinct ciphertexts for identical plaintexts while `Deterministic` enables equality lookups. Why the keyed choice wins: Always Encrypted with VBS or SGX secure enclaves (`ALLOW_ENCLAVE_COMPUTATIONS`) evaluates `LIKE` predicates inside an isolated enclave memory region without revealing keys or plaintext to the SQL engine DBA.
- **B:** Incorrect for this requirement. BYOK TDE wraps the symmetric Database Encryption Key (`DEK`) with an asymmetric RSA key in Key Vault or Managed HSM so security admins control key rotation and instant revocation. Why the keyed choice wins: Always Encrypted with VBS or SGX secure enclaves (`ALLOW_ENCLAVE_COMPUTATIONS`) evaluates `LIKE` predicates inside an isolated enclave memory region without revealing keys or plaintext to the SQL engine DBA.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Always Encrypted with VBS or SGX secure enclaves (`ALLOW_ENCLAVE_COMPUTATIONS`) evaluates `LIKE` predicates inside an isolated enclave memory region without revealing keys or plaintext to the SQL engine DBA.
- **D:** Correct. Secure enclaves delegate column decryption into an isolated memory region inside SQL, unlocking `LIKE`, `<`, `>`, `ORDER BY`, and fast in-place initial encryption without exposing plaintext to DBAs. In this scenario: Always Encrypted with VBS or SGX secure enclaves (`ALLOW_ENCLAVE_COMPUTATIONS`) evaluates `LIKE` predicates inside an isolated enclave memory region without revealing keys or plaintext to the SQL engine DBA.

### Question 99 — C

Answer: Azure Private Endpoint (`Microsoft.Network/privateEndpoints`) paired with `privatelink.database.windows.net` Private DNS and `publicNetworkAccess = Disabled`. Deploying an Azure Private Endpoint integrated with Private DNS zone `privatelink.database.windows.net` and setting `Public network access = Disabled` restricts SQL connectivity strictly to private VNet IPs. Private Link maps the SQL server to a private RFC 1918 IP inside your VNet accessible over VPN/ExpressRoute, blocking public internet exposure and cross-tenant data exfiltration. Local study-map skill 2.10 (Configure Azure Private Link (`privatelink.database.windows.net`), Service Endpoints, and SQL MI Subnet Security), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure Private Link, Virtual Network service endpoints, and SQL MI VNet security (https://learn.microsoft.com/en-us/azure/azure-sql/database/private-endpoint-overview).

- **A:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Deploying an Azure Private Endpoint integrated with Private DNS zone `privatelink.database.windows.net` and setting `Public network access = Disabled` restricts SQL connectivity strictly to private VNet IPs.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Deploying an Azure Private Endpoint integrated with Private DNS zone `privatelink.database.windows.net` and setting `Public network access = Disabled` restricts SQL connectivity strictly to private VNet IPs.
- **C:** Correct. Private Link maps the SQL server to a private RFC 1918 IP inside your VNet accessible over VPN/ExpressRoute, blocking public internet exposure and cross-tenant data exfiltration. In this scenario: Deploying an Azure Private Endpoint integrated with Private DNS zone `privatelink.database.windows.net` and setting `Public network access = Disabled` restricts SQL connectivity strictly to private VNet IPs.
- **D:** Incorrect for this requirement. VNet Service Endpoints restrict Azure SQL public endpoint traffic to a specific VNet subnet without private IPs, whereas SQL Managed Instance deploys directly into a dedicated delegated VNet subnet. Why the keyed choice wins: Deploying an Azure Private Endpoint integrated with Private DNS zone `privatelink.database.windows.net` and setting `Public network access = Disabled` restricts SQL connectivity strictly to private VNet IPs.

### Question 100 — B, D, F

Answers: Create an inline table-valued function `WITH SCHEMABINDING` evaluating `SESSION_CONTEXT()` or `DATABASE_PRINCIPAL_ID()`; Add a `FILTER PREDICATE` in `CREATE SECURITY POLICY` to hide non-matching rows silently from `SELECT`, `UPDATE`, and `DELETE`; Add `AFTER INSERT` and `AFTER UPDATE` / `BEFORE UPDATE` `BLOCK PREDICATE` clauses in `CREATE SECURITY POLICY` (`STATE = ON`). Complete RLS tenant/region isolation combines a `SCHEMABINDING` inline TVF predicate with both a `FILTER PREDICATE` (reads/updates/deletes) and `BLOCK PREDICATE` (inserts/updates) inside an enabled `SECURITY POLICY`. Local study-map skill 2.14 (Implement Cryptographic Ledger in Azure SQL (`Azure Confidential Ledger`) and Row-Level Security (`FILTER`/`BLOCK`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Ledger cryptographic tamper-evidence and Row-Level Security (RLS) in Azure SQL (https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-overview).

- **A:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Complete RLS tenant/region isolation combines a `SCHEMABINDING` inline TVF predicate with both a `FILTER PREDICATE` (reads/updates/deletes) and `BLOCK PREDICATE` (inserts/updates) inside an enabled `SECURITY POLICY`.
- **B:** Correct. `FILTER PREDICATE` injects the security TVF into read, update, and delete operators transparently without changing application `SELECT` statements. In this scenario: Complete RLS tenant/region isolation combines a `SCHEMABINDING` inline TVF predicate with both a `FILTER PREDICATE` (reads/updates/deletes) and `BLOCK PREDICATE` (inserts/updates) inside an enabled `SECURITY POLICY`.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Complete RLS tenant/region isolation combines a `SCHEMABINDING` inline TVF predicate with both a `FILTER PREDICATE` (reads/updates/deletes) and `BLOCK PREDICATE` (inserts/updates) inside an enabled `SECURITY POLICY`.
- **D:** Correct. RLS predicate functions must be inline TVFs bound with `SCHEMABINDING` so underlying columns cannot be altered silently and query plans inline cleanly. In this scenario: Complete RLS tenant/region isolation combines a `SCHEMABINDING` inline TVF predicate with both a `FILTER PREDICATE` (reads/updates/deletes) and `BLOCK PREDICATE` (inserts/updates) inside an enabled `SECURITY POLICY`.
- **E:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Complete RLS tenant/region isolation combines a `SCHEMABINDING` inline TVF predicate with both a `FILTER PREDICATE` (reads/updates/deletes) and `BLOCK PREDICATE` (inserts/updates) inside an enabled `SECURITY POLICY`.
- **F:** Correct. `BLOCK PREDICATE` raises an error if a shared application login attempts to insert or update a row carrying another tenant's identifier. In this scenario: Complete RLS tenant/region isolation combines a `SCHEMABINDING` inline TVF predicate with both a `FILTER PREDICATE` (reads/updates/deletes) and `BLOCK PREDICATE` (inserts/updates) inside an enabled `SECURITY POLICY`.
