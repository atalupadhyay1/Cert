# Microsoft Exam DP-300: Administering Microsoft Azure SQL Solutions — Full-Length Mock Exam 3

Exam DP-300 (Global FinTech Payments, Confidential Enclaves, and Zero-Data-Loss HA/DR) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint & Credential Notice:** Aligned to the official **October 27, 2026** DP-300 study guide (`Microsoft Certified: Azure Database Administrator Associate`). Associate-level certification with **no prerequisite exam required**, free online annual renewal on Microsoft Learn, split-screen `learn.microsoft.com` access during non-lab exam sections, and hands-on coverage across **T-SQL**, **Azure PowerShell**, **Azure CLI**, **Bicep**, and **KQL**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` T-SQL/PowerShell/CLI/Bicep/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Azure SQL case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area T-SQL/CLI dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn Azure SQL and SQL Server documentation — never recalled live items or copied Microsoft sample case studies.

## Questions

### 1. A wire-transfer settlement engine needs SQL Server Service Broker message queues, cross-database distributed transactions, sub-millisecond local SSD log writes, and one built-in read-only replica for intraday liquidity dashboards. Which offering fits best?

Domain: Plan and implement data platform resources

- A. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- B. Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica
- C. Azure SQL Managed Instance (Next-gen General Purpose) with decoupled IOPS and storage sliders
- D. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica

### 2. A card-authorization audit store in Azure SQL Database is projected to grow from 8 TB to 55 TB over 18 months and requires rapid scaling plus four compute-isolated read replicas for fraud ML scoring. Which tier should you recommend?

Domain: Plan and implement data platform resources

- A. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. SQL Server on Azure Virtual Machines (`Ebdsv5` series) with full OS and engine version control
- D. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica

### 3. Your FinTech network security team locks down `snet-clearing-mi` before deploying an Azure SQL Managed Instance. Which two subnet configurations are mandatory for provisioning to succeed? Select two.

Domain: Plan and implement data platform resources

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Create a dedicated VNet subnet (`/28` or larger) with no other cloud resources and delegate it to `Microsoft.Sql/managedInstances`
- C. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- D. Switch eligible hybrid SQL Server instances to hourly Azure Arc pay-as-you-go billing instead of upfront core licenses
- E. Associate a User-Defined Route (`UDR`) table (`0.0.0.0/0` -> `Internet` for management plane) and required NSG rules with the SQL MI subnet

### 4. Payment microservice developers run local schema migration tests on macOS/Linux laptops via `docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=..." mcr.microsoft.com/mssql/____:2022-latest`. Which official container repository path provides SQL Server 2022 on Linux?

Domain: Plan and implement data platform resources

- A. Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica
- B. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas
- C. SQL Server on Linux configured via `mssql-conf` or Linux container images for consistent CI/CD dev-test parity
- D. SQL Server enabled by Azure Arc (`Microsoft.AzureArcData/sqlServerInstances`)

### 5. A European acquirer operates 45 SQL Server 2022 hosts inside sovereign colocation cages regulated to stay on-premises, and connects them via Azure Arc. Which three capabilities become available? Select three.

Domain: Plan and implement data platform resources

- A. Enable automated SQL Best Practices Assessments and Microsoft Defender for SQL via the Azure Arc SQL Server extension
- B. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- C. Switch eligible hybrid SQL Server instances to hourly Azure Arc pay-as-you-go billing instead of upfront core licenses
- D. Configure SQL Server password logins (`CREATE LOGIN ... WITH PASSWORD`) and T-SQL `BACKUP DATABASE ... TO DISK` inside SQL database in Microsoft Fabric
- E. Query fleet-wide SQL Server version, edition, and backup status across hybrid servers via Azure Resource Graph Explorer
- F. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching

### 6. A `CardAuthorizations` table partitions daily rows on `SettlementDate`. Every night at 00:05 UTC you must create tomorrow's empty partition and swap out the 91-day-old partition for cold archive without blocking live card swipes. Which four-step sequence applies?

Domain: Plan and implement data platform resources

- A. ALTER TABLE ... SWITCH oldest partition directly to Azure Blob Storage → SPLIT partition function → Rebuild entire table offline → MERGE all boundaries
- B. SPLIT partition function for incoming future boundary → Create empty staging table on same filegroup with matching schema/indexes → ALTER TABLE ... SWITCH oldest partition to staging → Archive staging data & MERGE retired boundary
- C. Create staging table without matching CHECK constraints → SWITCH partition across two separate Azure SQL Databases → MERGE future boundary → Truncate production table
- D. MERGE oldest partition boundary first → Run row-by-row DELETE on 80M rows → Create unindexed staging table on a different filegroup → SPLIT partition function

### 7. When querying aggregated fee totals across 32 horizontally sharded FinTech tenant databases in Azure SQL Database without copying data into a warehouse first, which Elastic Database feature fans out a read-only `UNION ALL`-style T-SQL query across the shard map?

Domain: Plan and implement data platform resources

- A. Table partitioning using `CREATE PARTITION FUNCTION ... AS RANGE RIGHT` with aligned indexes and `ALTER TABLE ... SWITCH`
- B. Evaluate `sp_estimate_data_compression_savings` and apply `ROW`, `PAGE`, or `COLUMNSTORE_ARCHIVE` compression per partition
- C. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- D. Horizontal sharding using the Elastic Database Client Library (`ShardMapManager` with `ListShardMap` or `RangeShardMap`)

### 8. A treasury risk team runs SQL Server 2022 Enterprise on Windows Server Azure VMs with Software Assurance and runs `Update-AzSqlVM -ResourceGroupName "rg-fx" -Name "vm-fx01" -LicenseType ____` to slash SQL license compute charges by up to 40%. Which prerequisite extension enables `AHUB` conversion?

Domain: Plan and implement data platform resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. SQL IaaS Agent Extension in Full management mode paired with Azure Update Manager / Automated Patching
- D. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)

### 9. Branch ATM concentrator servers run SQL Server 2022 on Windows Server in bank branches and need centralized Microsoft Purview data governance policies plus Microsoft Entra authentication without moving to Azure VMs. What should you enable?

Domain: Plan and implement data platform resources

- A. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- B. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- C. Azure SQL Database vCore Elastic Pool with per-database min and max vCore limits
- D. SQL Server enabled by Azure Arc (`Microsoft.AzureArcData/sqlServerInstances`)

### 10. A wealth-advisory firm hosts 140 regional client-reporting databases on Azure SQL Database. Tokyo peaks 00:00–06:00 UTC, London peaks 08:00–15:00 UTC, and New York peaks 14:00–21:00 UTC. Which deployment model shares 32 vCores cost-effectively while capping any runaway database at 8 vCores?

Domain: Plan and implement data platform resources

- A. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- B. SQL Server on Azure Virtual Machines (`Ebdsv5` series) with full OS and engine version control
- C. Azure SQL Database vCore Elastic Pool with per-database min and max vCore limits
- D. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica

### 11. A payment reconciliation Azure SQL Managed Instance needs 320 user databases on a 16-vCore General Purpose instance (exceeding classic GP's 100-database ceiling) plus 30,000 provisioned IOPS. Which SQL MI configuration unlocks both?

Domain: Plan and implement data platform resources

- A. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- B. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- C. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- D. Azure SQL Managed Instance (Next-gen General Purpose) with decoupled IOPS and storage sliders

### 12. You audit storage settings on an `E48bds_v5` Azure VM running a high-volume FX matching SQL Server 2022 database. Which two Azure disk host-caching settings must be enforced on data versus transaction log volumes? Select two.

Domain: Plan and implement data platform resources

- A. Configure `ReadOnly` Azure host caching on Premium SSD data disks hosting `.mdf` and `.ndf` database files
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Configure `None` Azure host caching on dedicated managed disks hosting `.ldf` SQL Server transaction log files
- E. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching

### 13. After an Azure VM deallocate/start maintenance event, SQL Server 2022 fails to start because `D:\SQLTempDB` on the ephemeral local NVMe disk disappeared when the ephemeral drive reset. How should you configure `tempdb` on ephemeral NVMe safely?

Domain: Plan and implement data platform resources

- A. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- B. Premium SSD v2 / striped Premium SSD with `ReadOnly` host caching for data disks, `None` for log disks, and `tempdb` on local NVMe
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. No — transaction log managed disks on SQL Server Azure VMs must use host caching `None`, never `ReadOnly` or `ReadWrite`

### 14. A 900 GB `WireAuditArchive` partition has not been modified for three years and is queried twice a quarter during central-bank audits. Applying `ALTER INDEX CCI_WireAudit ON dbo.WireAuditArchive REBUILD PARTITION = 1 WITH (DATA_COMPRESSION = ____)` yields maximum disk savings beyond standard columnstore. Which compression level applies?

Domain: Plan and implement data platform resources

- A. Evaluate `sp_estimate_data_compression_savings` and apply `ROW`, `PAGE`, or `COLUMNSTORE_ARCHIVE` compression per partition
- B. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- C. Replace set-based `JOIN` queries with nested `FAST_FORWARD` T-SQL cursors calling multi-statement table-valued functions per row under compat `100`
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 15. A core-banking ledger on SQL Server 2022 must cut over to Azure SQL Managed Instance during a 90-second Sunday settlement pause using Managed Instance link. Which four-step execution order is required?

Domain: Plan and implement data platform resources

- A. Create Managed Instance link & seed distributed AG → Enable Availability Groups & master key on SQL Server → Execute planned cutover to SQL MI → Establish VNet/IPsec network peering on TCP 5022
- B. Export live `.bacpac` via SqlPackage without database copy → Establish VNet peering on UDP 1434 → Restore `.bacpac` onto SQL MI → Enable Availability Groups on SQL Server
- C. Enable Availability Groups & master key on SQL Server → Establish VNet/IPsec network peering on TCP 5022 → Create Managed Instance link & seed distributed AG → Validate sync state and execute planned cutover to SQL MI
- D. Take SQL Server offline immediately → Copy raw `.mdf`/`.ldf` files to Azure Files SMB → Attach `.mdf` files directly on SQL Managed Instance → Start distributed AG seeding

### 16. When enabling Microsoft Entra-only authentication on an existing Azure SQL logical server via Azure PowerShell (`Enable-AzSqlServerActiveDirectoryOnlyAuthentication`), which prerequisite resource must already be configured on that logical server?

Domain: Implement a secure environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Remap orphaned database users (`ALTER USER [u] WITH LOGIN = [u]`) and inspect explicit `DENY` permissions via `sys.database_permissions`
- D. Enable Microsoft Entra-only authentication (`azuread_authentication_only`) on the logical SQL server or SQL Managed Instance

### 17. Treasury quants run legacy Excel COM add-ins on Entra-joined laptops requiring `Integrated Security=True` Kerberos logins against Azure SQL Managed Instance. Which modern feature provides Kerberos tickets without deploying AD DS domain controllers in Azure?

Domain: Implement a secure environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or `Entra Kerberos`)

### 18. Settlement APIs invoke `Treasury.usp_PostJournal`, which runs dynamic T-SQL `sp_executesql` (breaking standard ownership chaining) against `Treasury.LedgerEntries`. How do you grant `sp_executesql` table access without granting callers direct `INSERT` on `Treasury.LedgerEntries`?

Domain: Implement a secure environment

- A. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- B. Stored procedure encapsulation using schema ownership chaining, `EXECUTE AS OWNER`, or certificate module signing
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 19. A FinTech CI/CD service principal needs to create and remove databases on an Azure SQL logical server without holding `Server Admin` or Azure RBAC `Owner` rights. Which built-in SQL DB server-level role provides database lifecycle management?

Domain: Implement a secure environment

- A. Built-in granular server-level roles (`##MS_ServerStateReader##`, `##MS_DefinitionReader##`) or `GRANT VIEW DATABASE PERFORMANCE STATE`
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 20. On a SQL Server 2022 VM, `EXEC sp_change_users_login` is deprecated. After restoring `ClearingDB.bak`, which modern T-SQL DDL command relinks orphaned database user `[clearing_app]` to server login `[clearing_app]`: `ALTER USER [clearing_app] WITH ____ = [clearing_app];`?

Domain: Implement a secure environment

- A. Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history
- B. Remap orphaned database users (`ALTER USER [u] WITH LOGIN = [u]`) and inspect explicit `DENY` permissions via `sys.database_permissions`
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 21. Regulators mandate configuring Customer-Managed Key (`CMK`) TDE backed by Azure Key Vault Managed HSM on `sql-quarrypay-prod`. Which four-step implementation sequence must you execute?

Domain: Implement a secure environment

- A. Enable Soft Delete & Purge Protection on Key Vault → Assign Managed Identity to SQL server → Grant Key Vault Crypto Service Encryption User (`get`/`wrapKey`/`unwrapKey`) → Set server TDE protector to Key Vault key
- B. Set server TDE protector to Key Vault key → Disable Soft Delete and Purge Protection on Key Vault → Assign Managed Identity after encryption starts → Export DEK plaintext to Blob storage
- C. Create symmetric key inside tempdb → Grant db_datareader in Key Vault → Set database compatibility level to 100 → Restart Azure SQL Database service
- D. Upload plaintext `.pfx` directly to Azure Table storage → Grant anonymous public read on container → Point TDE protector to Table URL → Disable TLS 1.2

### 22. A bank security admin accidentally revokes Key Vault permissions, putting an Azure SQL Database into `Inaccessible` state. Which two Key Vault configurations ensure CMK TDE stays healthy and un-purgeable? Select two.

Domain: Implement a secure environment

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Grant the SQL server Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) on the Key Vault
- D. Enable both `Soft Delete` and `Purge Protection` on the Azure Key Vault or Managed HSM storing the TDE protector key
- E. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script

### 23. Inside a SQL Server 2022 VM database, you protect `SwiftRoutingSecret` using T-SQL cell encryption. What is the correct key hierarchy from top to bottom inside the database before calling `EncryptByKey()`?

Domain: Implement a secure environment

- A. Column-level encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey`) plus `Minimal TLS version = 1.2`
- B. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 24. Which system view inside a user Azure SQL Database lists only the portable database-level IP firewall rules rather than server-wide `master` firewall rules: `SELECT name, start_ip_address, end_ip_address FROM sys.____`?

Domain: Implement a secure environment

- A. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- B. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server

### 25. A sanctions-screening microservice must execute `<`, `>`, and `LIKE` predicates over encrypted wire-beneficiary columns in Azure SQL Database using VBS secure enclaves. Which two configurations are required? Select two.

Domain: Implement a secure environment

- A. Provision a Column Master Key in Key Vault and create a Column Encryption Key with `ENCLAVE_COMPUTATIONS` enabled
- B. Enable `Column Encryption Setting=Enabled` and pass the `Enclave Attestation Url` (or VBS zero-attestation setting) in client drivers
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- E. Configure `None` Azure host caching on dedicated managed disks hosting `.ldf` SQL Server transaction log files

### 26. Without secure enclaves, a compliance architect encrypts two columns with Always Encrypted: `AccountTaxId` (used in `INNER JOIN` and `WHERE AccountTaxId = @tid`) and `WireMemoNotes` (never joined, filtered, or grouped). Which encryption types should you choose?

Domain: Implement a secure environment

- A. Always Encrypted (`Randomized` for maximum security with zero equality leakage; `Deterministic` only when `=` joins or `GROUP BY` are required)
- B. Always Encrypted with VBS or Intel SGX secure enclaves (`ALLOW_ENCLAVE_COMPUTATIONS` + `Column Encryption Setting=Enabled`)
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Transparent Data Encryption (TDE) with a Customer-Managed Key (`CMK`) in Azure Key Vault (`Soft Delete` + `Purge Protection`)

### 27. Payment card network auditors require `sql-aegisvault.database.windows.net` to resolve exclusively to `10.44.2.12` over Private Link and reject all public internet handshakes. Which two steps complete this design? Select two.

Domain: Implement a secure environment

- A. Link Private DNS Zone `privatelink.database.windows.net` (or forward on-premises DNS) to resolve `<server>.database.windows.net` to the private IP
- B. Set `Public network access = Disabled` (`publicNetworkAccess: Disabled`) on the logical SQL server so internet connections are rejected
- C. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- E. Switch eligible hybrid SQL Server instances to hourly Azure Arc pay-as-you-go billing instead of upfront core licenses

### 28. A SQL Managed Instance subnet needs to lock down outbound traffic so malicious T-SQL `BULK INSERT` or `OPENROWSET` calls cannot exfiltrate data to arbitrary external Azure Storage accounts. Proposed solution: Configure Outbound Firewall Rules (`Allowed FQDN list`) on the Azure SQL Managed Instance / logical SQL server restricting outbound connections solely to `stquarrypayprod.blob.core.windows.net`. Does the solution meet the goal?

Domain: Implement a secure environment

- A. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server
- B. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- C. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- D. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference

### 29. On a SQL Managed Instance, you want T-SQL Server Audit (`CREATE SERVER AUDIT ... WHERE ____`) to record `SELECT` statements **only** when executed outside the trusted `[svc_settlement]` service login, cutting log volume by 92%. Which T-SQL Server Audit capability enables this?

Domain: Implement a secure environment

- A. Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history
- B. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage

### 30. When sending Azure SQL Database audit logs to Azure Event Hubs instead of Azure Storage, which downstream scenario benefits most from Event Hubs streaming?

Domain: Implement a secure environment

- A. SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 31. A fraud feature store needs asynchronous log-based capture of every historical balance mutation on `Accounts` in Azure SQL Database (`GP_Gen5_8`), where SQL Server Agent does not exist. How do you enable Change Data Capture on Azure SQL Database?

Domain: Implement a secure environment

- A. Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history
- B. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- C. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- D. Enable Change Data Capture (`CDC`) on DTU `Basic`/`S0–S2` databases or expect Change Tracking (`CT`) to retain every intermediate `UPDATE` value

### 32. In SQL Server 2022 and Azure SQL Database, support analysts need `SELECT` access on `WireTransfers`, where `RoutingCode` is masked yet `FeeAmount` is masked with `random(1, 5)`. You want `FeeAuditors` to see unmasked `FeeAmount` ONLY while keeping `RoutingCode` masked via `GRANT ____ ON WireTransfers(FeeAmount) TO [FeeAuditors];`. Which granular permission works in SQL 2022 / Azure SQL?

Domain: Implement a secure environment

- A. Row-Level Security (`CREATE SECURITY POLICY`) binding a `SCHEMABINDING` inline TVF as both `FILTER PREDICATE` and `BLOCK PREDICATE`
- B. Transparent Data Encryption (TDE) with a Customer-Managed Key (`CMK`) in Azure Key Vault (`Soft Delete` + `Purge Protection`)
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Always Encrypted with VBS or Intel SGX secure enclaves (`ALLOW_ENCLAVE_COMPUTATIONS` + `Column Encryption Setting=Enabled`)

### 33. A correspondent-banking portal pools connections across 60 partner banks stored in `PartnerTrades` (`PartnerBankId`). Which three Row-Level Security constructs guarantee strict read and write isolation per bank? Select three.

Domain: Implement a secure environment

- A. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- B. Add a `FILTER PREDICATE` in `CREATE SECURITY POLICY` to hide non-matching rows silently from `SELECT`, `UPDATE`, and `DELETE`
- C. Truncate or `DELETE` historical rows from an append-only Ledger table (`LEDGER = ON (APPEND_ONLY = ON)`) to purge audit history in place
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- E. Create an inline table-valued function `WITH SCHEMABINDING` evaluating `SESSION_CONTEXT()` or `DATABASE_PRINCIPAL_ID()`
- F. Add `AFTER INSERT` and `AFTER UPDATE` / `BEFORE UPDATE` `BLOCK PREDICATE` clauses in `CREATE SECURITY POLICY` (`STATE = ON`)

### 34. You are rolling out Row-Level Security on `Custody.Positions` so pooled `.NET` API connections scoped via `SESSION_CONTEXT(N'FundId')` cannot read or modify other funds. Which four-step sequence should you follow?

Domain: Implement a secure environment

- A. Create `SECURITY POLICY` with `STATE = ON` first → Create multi-statement TVF without `SCHEMABINDING` → Grant tenants `ALTER ANY SECURITY POLICY` → Store `TenantId` in a global temp table
- B. Create non-schema-bound scalar UDF → Attach UDF to `sys.sp_set_firewall_rule` → Enable Change Tracking → Set `SESSION_CONTEXT` with `@read_only = 0` so users can switch tenants
- C. Apply `ADD MASKED WITH (FUNCTION = 'default()')` on `TenantId` → Create `AFTER INSERT` trigger → Grant `UNMASK` to shared app login → Expect row filtering
- D. Create dedicated `Security` schema → Create `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT(N'TenantId')` → Create `SECURITY POLICY` with `FILTER` & `BLOCK` predicates (`STATE = ON`) → Set read-only `sp_set_session_context` on connect

### 35. You are establishing a pre-cutover baseline on an Azure SQL Database Elastic Pool (`pool-fx-prod`) and need 15-second historical pool-wide CPU, storage, and worker utilization via `SELECT avg_cpu_percent, max_worker_percent FROM sys.____`. Which catalog view in `master` provides Elastic Pool history?

Domain: Monitor, configure, and optimize database resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Azure Monitor metrics paired with `sys.dm_db_resource_stats` (single DB) or `sys.server_resource_stats` (SQL MI) for 15-second CPU, data I/O, log write, and memory baselines
- D. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7

### 36. During European market open, CPU sits at 99% and `SOS_SCHEDULER_YIELD` accounts for 81% of waits in `sys.dm_os_wait_stats` while `PAGEIOLATCH_*` and `WRITELOG` are under 1%. What does `SOS_SCHEDULER_YIELD` signify?

Domain: Monitor, configure, and optimize database resources

- A. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 37. You configure Azure Monitor Diagnostic Settings on `sqlmi-mintbridge` and query Log Analytics for deadlocks and blocked-process counts over 24 hours. Which Log Analytics table receives `SQLInsights` and `Errors` diagnostic records in Resource-Specific vs Azure-Diagnostics mode?

Domain: Monitor, configure, and optimize database resources

- A. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- B. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- C. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- D. Azure Monitor Diagnostic Settings streaming `SQLInsights`, `QueryStoreRuntimeStatistics`, `Errors`, and `Blocks` to a Log Analytics workspace (`KQL`)

### 38. Your FinTech SRE team is deploying `database watcher` across 18 Azure SQL Databases and 4 SQL Managed Instances backed by an Azure Data Explorer cluster. Which four-step sequence completes deployment?

Domain: Monitor, configure, and optimize database resources

- A. Create database watcher targeting Azure Cosmos DB for Gremlin → Store metrics in Azure Table storage → Authenticate via anonymous public SAS → Query dashboards via Gremlin
- B. Install third-party kernel drivers inside Azure SQL Database PaaS OS → Configure SMB share on domain controller → Export `.trc` files via `sp_trace_create` → Query via MDX
- C. Provision Azure Data Explorer or Fabric Eventhouse store → Create database watcher with Managed Identity → Add SQL targets & grant `VIEW SERVER PERFORMANCE STATE` + ingest roles → Start watcher & open portal dashboards
- D. Start database watcher before selecting data store or SQL targets → Grant `sysadmin` via blank-password `sa` login → Store time-series telemetry in Azure Queue Storage → Enable SQL Profiler trace

### 39. Security reviews the access model for `database watcher` monitoring FinTech SQL Managed Instances into Fabric Eventhouse (while noting transition to Database Hub in Fabric before April 30, 2027). Which two role grants are required? Select two.

Domain: Monitor, configure, and optimize database resources

- A. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- B. Grant the database watcher Managed Identity database `Admin` / ingest permissions on the Azure Data Explorer or Fabric Eventhouse store
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Grant the database watcher Managed Identity `VIEW SERVER PERFORMANCE STATE` (or `VIEW DATABASE PERFORMANCE STATE`) on SQL targets
- E. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 40. Compliance requires capturing persistent `.xel` Extended Events traces for failed `sql_batch_completed` executions (`result = Abort`) on an Azure SQL Database. Which two steps are required? Select two.

Domain: Monitor, configure, and optimize database resources

- A. Define `CREATE EVENT SESSION ... ON DATABASE ADD TARGET package0.event_file(SET filename = N'https://...xel')` and start the session
- B. Enable both `Soft Delete` and `Purge Protection` on the Azure Key Vault or Managed HSM storing the TDE protector key
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE` with `rwl` permissions) for the Azure Blob container
- E. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7

### 41. Which T-SQL system function reads `.xel` Extended Events trace files directly from Azure Blob Storage URLs so DBAs can parse captured XML payloads into relational columns: `SELECT event_data FROM sys.____('https://sttraces.blob.core.windows.net/xe/*.xel', NULL, NULL, NULL)`?

Domain: Monitor, configure, and optimize database resources

- A. Extended Events (`CREATE EVENT SESSION ... ON DATABASE` in SQL DB or `ON SERVER` in SQL MI/VMs) writing to an `event_file` target in Azure Blob Storage
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 42. A third-party SWIFT gateway executes a hardcoded T-SQL query suffering severe parameter-sniffing regressions at market close, and vendor terms forbid modifying stored procedures. Which two Query Store procedures let you intervene cleanly? Select two.

Domain: Monitor, configure, and optimize database resources

- A. Execute `sys.sp_query_store_force_plan @query_id, @plan_id` to pin the historical low-latency execution plan immediately
- B. Execute `sys.sp_query_store_set_hints @query_id, N'OPTION (RECOMPILE)'` (or `MAXDOP` / memory grant hints) without redeploying code
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- E. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 43. At 09:30 NY market open, `usp_MatchOrder` jumps from 2 ms to 850 ms after compiling an atypical plan. Which four-step Query Store workflow restores the 2 ms plan immediately without restarting SQL?

Domain: Monitor, configure, and optimize database resources

- A. Run `ALTER DATABASE ... SET QUERY_STORE CLEAR ALL` first → Inspect Regressed Queries history → Force new regressed plan ID → Set `OPERATION_MODE = OFF`
- B. Set Query Store `OPERATION_MODE = READ_ONLY` → Modify `sys.query_store_plan` system catalog via `UPDATE` → Run `DBCC FREEPROCCACHE` every minute → Disable statistics
- C. Restart SQL Server production instance during peak traffic → Rebuild every index with `ONLINE = OFF` → Enable `AUTO_CLOSE = ON` → Check Query Store
- D. Confirm Query Store is `READ_WRITE` with wait capture → Compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`) → Force prior plan via `sp_query_store_force_plan` → Monitor `force_failure_count` & latency

### 44. An `UPDATE Ledger SET Status = 'Settled' WHERE BatchDate = '2026-11-01' AND Desk = 'FX'` statement in Azure SQL Database previously escalated to an exclusive table lock (`LCK_M_X`) after touching 5,000 rows (`ALTER DATABASE LedgerDB SET ____ = ON` enabled by default in SQL DB). How does **Optimized Locking** prevent lock escalation here?

Domain: Monitor, configure, and optimize database resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Read Committed Snapshot Isolation (`READ_COMMITTED_SNAPSHOT = ON`) combined with Optimized Locking (`TID` locking + Lock After Qualification `LAQ`)
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 45. An application team proposes adding `WITH (NOLOCK)` to intraday margin calculation `SELECT` queries to avoid blocking during position updates. Why must a FinTech DBA reject `NOLOCK` and use `RCSI` instead?

Domain: Monitor, configure, and optimize database resources

- A. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Capture `xml_deadlock_report` via Extended Events or `sys.event_log`, align table modification order across transactions, and add covering indexes
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 46. Which DMV tracks real-time page latch contention, row lock waits, and page split counts per table/index partition via `SELECT page_lock_wait_count, page_io_latch_wait_count FROM sys.____(DB_ID(), NULL, NULL, NULL)`?

Domain: Monitor, configure, and optimize database resources

- A. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- B. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`

### 47. You suspect an open forgotten `BEGIN TRAN` session from SSMS is preventing transaction log truncation on `SettlementDB`. Which catalog column in `sys.databases` confirms why the transaction log cannot truncate: `SELECT name, ____ FROM sys.databases`?

Domain: Monitor, configure, and optimize database resources

- A. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- B. Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 48. A payment lookup query `WHERE LEFT(CardToken, 6) = '411122'` scans all 180M rows of `IX_CardToken` even though `CardToken` is the leading index key. Which SARGable rewrite converts the scan into an `Index Seek`?

Domain: Monitor, configure, and optimize database resources

- A. Replace set-based `JOIN` queries with nested `FAST_FORWARD` T-SQL cursors calling multi-statement table-valued functions per row under compat `100`
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions
- D. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon

### 49. Real-time risk dashboards run analytical `SUM(ExposureUSD)` aggregations directly over a live OLTP `OpenPositions` B-tree table (`HTAP`) without slowing millisecond inserts. Which index design accelerates in-place HTAP analytics?

Domain: Monitor, configure, and optimize database resources

- A. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 50. In an Actual Execution Plan, an `Index Seek` on `IX_Trades_AccountId` is paired via a `Nested Loops` join to a `Key Lookup (Clustered)` executing 420,000 times and consuming 89% of query cost. What causes this pattern?

Domain: Monitor, configure, and optimize database resources

- A. Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`)
- B. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Transparent Data Encryption (TDE) with a Customer-Managed Key (`CMK`) in Azure Key Vault (`Soft Delete` + `Purge Protection`)

### 51. You design a global 24x5 FX maintenance policy that must never hold exclusive table locks, stall query compilations on synchronous stats sampling, or saturate IOPS during integrity checks. Which three settings achieve this? Select three.

Domain: Monitor, configure, and optimize database resources

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Run `DBCC CHECKDB WITH PHYSICAL_ONLY` during off-peak windows or offload full `DBCC CHECKDB` onto a restored backup replica
- D. Run `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON, MAX_DURATION = 90 MINUTES)` for heavily fragmented (`>30%`) indexes
- E. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- F. Enable `AUTO_UPDATE_STATISTICS_ASYNC = ON` and schedule targeted `UPDATE STATISTICS` jobs so user queries do not stall waiting on sampling

### 52. An engineer proposes running `DBCC SHRINKDATABASE (SettlementDB, 10)` every night at 02:00 UTC to reclaim free space after partition purges. Why does Microsoft strongly discourage routine `DBCC SHRINKDATABASE`?

Domain: Monitor, configure, and optimize database resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Fragmentation-aware index maintenance (`REORGANIZE` 5–30%, `REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` >30%), `UPDATE STATISTICS`, and `DBCC CHECKDB WITH PHYSICAL_ONLY`
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 53. Where are Azure SQL Database Automatic Tuning settings inherited from by default when you create a new database without specifying explicit per-database `AUTOMATIC_TUNING` overrides?

Domain: Monitor, configure, and optimize database resources

- A. Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`)
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon

### 54. You want to disable parameter sniffing strictly inside `SandboxSimDB` (`ALTER DATABASE SCOPED CONFIGURATION SET ____ = OFF;`) so every query uses average density vectors without touching sibling databases on the SQL Managed Instance. Which option name completes this statement?

Domain: Monitor, configure, and optimize database resources

- A. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Use `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`, `OPTIMIZED_PLAN_FORCING`) per database

### 55. On a treasury SQL Server 2022 VM, you want a backup verification Agent job to run during idle CPU lulls whenever average CPU drops below 10% for 15 minutes rather than at a fixed clock hour. Which SQL Server Agent schedule type supports this?

Domain: Configure and manage automation of tasks

- A. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators

### 56. Your FinTech audit team requires removing `sysadmin` from all SQL Agent job owners and ensuring instant email paging on fatal SQL engine errors `823–825` and Severity `19–25`. Which two SQL Agent features must you configure? Select two.

Domain: Configure and manage automation of tasks

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Create a Windows/SQL Credential and map it to a SQL Server Agent Subsystem Proxy (`CmdExec` / `PowerShell`) instead of granting `sysadmin`
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- E. Configure Database Mail, define an Agent Operator, and create SQL Server Agent Alerts for Severity `19–25` and Errors `823`, `824`, and `825`

### 57. When configuring SQL Server Agent Alerts on a user-defined error raised via `RAISERROR (50099, 16, 1, 'Settlement variance') WITH ____`, which clause is required in `RAISERROR` so SQL Server Agent detects the event in the Windows Application / engine error log?

Domain: Configure and manage automation of tasks

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators
- D. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7

### 58. On Azure SQL Managed Instance, a DBA notices the SQL Server Agent service cannot be stopped or restarted manually from SSMS Object Explorer. Why is this behavior expected?

Domain: Configure and manage automation of tasks

- A. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- B. Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries
- C. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- D. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 59. A multi-step SQL Server Agent job succeeds on Step 1 and Step 2, yet never executes Step 3 even though no error occurred. Inspecting Step 2 properties reveals `On success action = Quit the job reporting success`. What change fixes the workflow?

Domain: Configure and manage automation of tasks

- A. Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Transparent Data Encryption (TDE) with a Customer-Managed Key (`CMK`) in Azure Key Vault (`Soft Delete` + `Purge Protection`)

### 60. A FinTech platform team deploys PCI-DSS Azure SQL logical servers via GitHub Actions Bicep workflows. Which two controls prevent secret exposure in ARM logs and validate resource diffs before execution? Select two.

Domain: Configure and manage automation of tasks

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Mark sensitive parameters with `@secure()` in Bicep and pass Key Vault secret references from the parameter file rather than cleartext values
- D. Run `az deployment group what-if` (or `New-AzResourceGroupDeployment -WhatIf`) as a pull-request gate before applying template changes
- E. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 61. In a Bicep file provisioning `Microsoft.Sql/servers/databases@2023-08-01-preview`, how do you declare `CustodyDB` as a child resource of `resource sqlServer 'Microsoft.Sql/servers@...'` so Bicep infers deployment order automatically?

Domain: Configure and manage automation of tasks

- A. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`
- D. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 62. You write an Azure PowerShell script to create a Serverless vCore database that auto-pauses after 60 minutes idle: `New-AzSqlDatabase ... -ComputeModel ____ -AutoPauseDelayInMinutes 60 -MinVCore 0.5 -VCore 4`. Which `-ComputeModel` value enables Serverless?

Domain: Configure and manage automation of tasks

- A. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- B. Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`)
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server

### 63. You script Azure CLI to enable Transparent Data Encryption with a Key Vault key URI on `sql-quarrypay`: `az sql server tde-key ____ -g rg-pay -s sql-quarrypay --server-key-type AzureKeyVault --kid https://kv.../keys/tde/123`. Which CLI verb sets the server TDE protector?

Domain: Configure and manage automation of tasks

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`)

### 64. Deploying a Business Critical Azure SQL Managed Instance via ARM takes several hours on initial virtual cluster creation, and your pipeline times out at 60 minutes while ARM continues in the background. How do you monitor real-time provisioning progress?

Domain: Configure and manage automation of tasks

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules

### 65. An ARM template attempting to delete a retired dev subnet `snet-old-mi` fails with `InUseSubnetCannotBeDeleted` even after the SQL Managed Instance was deleted 10 minutes ago. Why does this occur?

Domain: Configure and manage automation of tasks

- A. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- B. Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 66. You must deploy an Azure SQL Elastic Job Agent using a User-Assigned Managed Identity (`UAMI`) to execute hourly FX rate table updates across 50 regional Azure SQL Databases. Which four-step sequence applies?

Domain: Configure and manage automation of tasks

- A. Create Elastic Job Agent on Basic tier DB → Run `jobs.sp_add_job` before creating Target Group → Authenticate across servers with Windows NTLM local accounts → Schedule via `msdb.dbo.sp_add_job`
- B. Create S1+ Job Database & Elastic Job Agent with UAMI → Create contained UAMI user on target DBs with needed permissions → Define Target Group (`jobs.sp_add_target_group_member`) → Add T-SQL steps & schedule (`jobs.sp_add_job`)
- C. Provision Elastic Job Agent inside Azure Blob Storage → Store plaintext admin password in Git repo → Add Cosmos DB containers to Target Group → Trigger via `DBCC SHRINKDATABASE`
- D. Enable SQL Server Agent inside single Azure SQL Database → Create linked servers to 480 tenant DBs → Loop synchronously inside a scalar UDF → Grant `CONTROL SERVER` to `guest`

### 67. Why must T-SQL scripts authored for Azure SQL Elastic Jobs be written **idempotently** (e.g., `IF NOT EXISTS (SELECT 1 FROM sys.columns ...)` before `ALTER TABLE ADD`)?

Domain: Configure and manage automation of tasks

- A. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- B. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Azure SQL Database Elastic Job Agent (`jobs.sp_add_job`) authenticating to Target Groups across servers/pools via a User-Assigned Managed Identity (`UAMI`)

### 68. A FinTech cost-governance team wants a serverless Python 3.10 script running every Friday at 21:00 UTC to tag untagged Azure SQL Databases and scale down QA Elastic Pools using `azure-mgmt-sql` with zero stored credentials. Which Azure service fits best?

Domain: Configure and manage automation of tasks

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Azure Automation PowerShell / Python runbooks (or Azure Functions / Logic Apps) using a System-Assigned Managed Identity on a recurring schedule
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo

### 69. You want to cap CPU usage of a nightly batch T-SQL script running inside a single General Purpose Azure SQL Database. Proposed solution: Deploy an Azure Automation runbook that executes `CREATE WORKLOAD GROUP BatchCap WITH (REQUEST_MAX_CPU_TIME_SEC = 5)` on that single Azure SQL Database. Does the solution meet the goal?

Domain: Configure and manage automation of tasks

- A. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- B. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- C. No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases
- D. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent

### 70. An Elastic Job running across 50 FinTech databases hangs on one target database due to lock waits. Which parameter on `jobs.sp_add_jobstep` caps per-step execution runtime (`@step_timeout_seconds`) and retries cleanly while Azure Monitor alerts on failed targets?

Domain: Configure and manage automation of tasks

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- C. Configure Azure Monitor Metric / Log Alert rules routed to Action Groups and query `jobs.job_executions` in the Elastic Job database to diagnose step failures
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 71. Treasury wants a disaster-recovery archive of a live 2,000-TPS settlement Azure SQL Database with `RPO <= 5 minutes` and `100%` transactional consistency across 40 foreign-key tables. Proposed solution: Run hourly `SqlPackage /Action:Export` directly against the live primary database into Blob Storage. Does the solution meet the goal?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server
- B. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- C. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- D. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement

### 72. A European clearing bank runs SQL Server 2022 on-premises and replicates to Azure SQL Managed Instance via Managed Instance link. During a planned quarterly switch, they fail over workloads to SQL MI for two weeks and then fail back online to SQL Server 2022. Which engine capability makes this possible?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- B. Hybrid DR using Managed Instance link with bidirectional online failover between SQL Server 2022 and Azure SQL Managed Instance
- C. Expect online bidirectional planned failback from Azure SQL Managed Instance directly back to on-premises SQL Server 2016 without downtime
- D. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 73. In Azure SQL Database Hyperscale, how is intra-region High Availability achieved faster than standard General Purpose failover when a primary compute node crashes?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`)
- C. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- D. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG

### 74. After failing over an Azure SQL Failover Group during a DR drill, on-premises apps still connect to the old region for 4 minutes because an internal corporate DNS server ignores Azure's 30-second DNS TTL and caches records for 1 hour. How do you prevent stale DNS routing?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Non-disruptive DR readiness drill executing a planned zero-data-loss Failover Group switch (`Switch-AzSqlDatabaseFailoverGroup`), validating app listeners, and failing back
- D. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA

### 75. On a 2-node SQL Server 2022 Always On Availability Group VM cluster, scheduled Full backups run Sundays and Differentials run Mon–Sat on the primary. Proposed solution: Run an ad-hoc `BACKUP DATABASE [FX] TO URL = '...'` (without `COPY_ONLY`) on Wednesday noon for a dev refresh. Does the solution preserve Thursday's Differential restore chain?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- B. No — transaction log managed disks on SQL Server Azure VMs must use host caching `None`, never `ReadOnly` or `ReadWrite`
- C. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- D. No — taking an ad-hoc non-`COPY_ONLY` full backup resets the differential base and breaks downstream differential restores

### 76. On an Always On Availability Group running on SQL Server 2022 Azure VMs, you offload nightly backups onto the asynchronous secondary replica (`AutomatedBackupPreference = Secondary`). Which backup types are supported versus unsupported on an AG secondary replica?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- B. Use `BACKUP DATABASE ... WITH COPY_ONLY` for ad-hoc exports on SQL MI / AGs, and Azure Backup Recovery Services Vault SQL-aware policies (`15-min` log RPO) on SQL VMs
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access

### 77. At 16:00 UTC you complete an online Database Move of `CustodyLedger` from `sqlmi-a` to `sqlmi-b`. At 17:00 UTC compliance asks to restore `CustodyLedger` to `12:00 UTC` via PITR on `sqlmi-b`. Proposed solution: Initiate Point-in-Time Restore on `sqlmi-b` for `12:00 UTC`. Does the solution meet the goal?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- B. No — moving a database across SQL Managed Instances starts a fresh backup chain and does not carry over prior PITR backups
- C. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- D. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server

### 78. SEC Rule 17a-4 auditors require retaining yearly year-end backups of `CustodyDB` for 10 years in immutable WORM storage that cannot be deleted even by Global Admins. Which two Azure SQL features meet this mandate? Select two.

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Set Short-Term PITR retention to `3,650` days (`10 years`) and grant developers Subscription Contributor to prevent backup deletion
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Configure an Azure SQL Long-Term Retention (`LTR`) policy (`WeeklyRetention`, `MonthlyRetention`, `YearlyRetention`, `WeekOfYear`) up to 10 years
- E. Enable and lock time-based immutability (`WORM`) on the LTR backup policy so nobody can shorten retention or delete compliance backups early

### 79. You delete an active Azure SQL Database `RetiredDeskDB` whose parent logical SQL server remains active and had a 7-year Long-Term Retention (`LTR`) backup policy. Proposed solution: Restore one of `RetiredDeskDB`'s historical monthly LTR backups into a new database via `Restore-AzSqlDatabase -FromLongTermRetentionBackup -ResourceId ...`. Does the solution meet the goal?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- B. No — transaction log managed disks on SQL Server Azure VMs must use host caching `None`, never `ReadOnly` or `ReadWrite`
- C. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- D. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server

### 80. You must back up an 8 TB treasury data mart on a SQL Server 2022 Azure VM directly to Azure Blob Storage in under 45 minutes without SAS token sprawl. Which two actions should you implement? Select two.

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access
- D. Create a SQL Server `CREDENTIAL` (`IDENTITY = 'Managed Identity'` or `'SHARED ACCESS SIGNATURE'`) matching the Azure Blob container URL
- E. Stripe `BACKUP DATABASE` across multiple `TO URL = 'https://...bak'` block blob targets with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`

### 81. On SQL Server 2022, you want `BACKUP DATABASE [Treasury] TO URL = 'https://...'` to encrypt the `.bak` file itself before bytes leave SQL Server (`WITH COMPRESSION, ENCRYPTION (ALGORITHM = AES_256, SERVER ____ = BackupCert)`). Which server object protects native backup encryption?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Striped T-SQL `BACKUP DATABASE ... TO URL = ...` across up to 64 block blobs (`MAXTRANSFERSIZE`, `COMPRESSION`) authenticated via `Managed Identity` or `SHARED ACCESS SIGNATURE` Credential
- B. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- C. Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access
- D. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 82. You deploy Failover Group `fog-treasury` across UK South and UK West for coupled settlement databases. Which two settings ensure zero-config client redirection and controlled automatic failover behavior? Select two.

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Connect OLTP write traffic to `<fog>.database.windows.net` and read-only analytics to `<fog>.secondary.database.windows.net`
- B. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- C. Configure `ReadWriteFailoverPolicy = Automatic` with `GracePeriodWithDataLossHours >= 1` so transient blips do not trigger premature lossy failover
- D. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- E. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 83. When connecting a read-only Power BI gateway directly to an Active Geo-Replication secondary or a Business Critical built-in read-scale replica on the **same** server endpoint, which connection-string keyword routes the session to the read-only replica: `____=ReadOnly`?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. Failover Groups for automatic multi-database failover behind stable `<fog>.database.windows.net` / `.secondary` listeners vs Active Geo-Replication for up to 4 readable secondaries
- D. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA

### 84. You configure a synchronous-commit Always On Availability Group across Zone 1 and Zone 2 in East US 2 on SQL Server 2022 VMs, plus a third asynchronous-commit DR replica in West US 2. How many total synchronous-commit replicas (including primary) does SQL Server Enterprise support in one Availability Group?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`
- B. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- C. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- D. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG

### 85. When adding a new 900 GB database to an Always On Availability Group over a 10 Gbps VNet link without manually backing up, copying, and restoring `.bak`/`.trn` files, which `CREATE AVAILABILITY GROUP` replica property streams initial data automatically: `SEEDING_MODE = ____`?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- B. Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG

### 86. You deploy a 2-node SQL Server 2022 Failover Cluster Instance (`FCI`) on Azure VMs across Availability Zones 1 and 2, storing user databases on Premium File Shares (`SMB 3.1.1`) or `ZRS` Azure Shared Disks. Which disk redundancy option is required on an Azure Shared Disk to span multiple Availability Zones?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- B. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- C. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas
- D. Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`)

### 87. A secondary SQL Server VM receives Log Shipping `.trn` backups every 5 minutes using `WITH NORECOVERY` (fastest redo, no user connections disconnecting restores). What happens if an analyst tries to run `SELECT` against a `NORECOVERY` secondary database?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- B. Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`)
- C. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 88. During peak wire settlement, primary commits slow down on a synchronous-commit Always On Availability Group and `HADR_SYNC_COMMIT` becomes the top wait in `sys.dm_os_wait_stats`. What does high `HADR_SYNC_COMMIT` wait time indicate?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- B. Query `sys.dm_hadr_database_replica_states` (`synchronization_state_desc`, `log_send_queue_size`, `redo_queue_size`) and `sys.dm_geo_replication_link_status`, plus verify NSG probe port `59999`
- C. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

---

## Case study — AegisVault Custody

AegisVault Custody enforces zero-password governance across Azure SQL Database and SQL Managed Instance. SQL authentication must be disabled completely, database users must survive geo-failover without `master` login sync, and junior NOC engineers need server-wide DMV visibility without data-read permissions.

The next 3 questions refer to **AegisVault Custody**. Read the scenario brief once, then answer each item independently.

### 89. Which server/instance authentication configuration satisfies the zero-password mandate by completely disabling `sa` and SQL password logins across Azure SQL Database and SQL Managed Instance?

Domain: Implement a secure environment

- A. Enable Microsoft Entra-only authentication (`azuread_authentication_only`) on the logical SQL server or SQL Managed Instance
- B. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database

### 90. How should you provision database users so credentials never rely on `master` SID mappings and remain immediately valid after an automatic Failover Group switch?

Domain: Implement a secure environment

- A. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- B. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`)

### 91. Which built-in server-level role gives junior NOC engineers server-wide DMV read visibility across all databases on the Azure SQL logical server without granting `SELECT` on custody tables?

Domain: Implement a secure environment

- A. Built-in granular server-level roles (`##MS_ServerStateReader##`, `##MS_DefinitionReader##`) or `GRANT VIEW DATABASE PERFORMANCE STATE`
- B. Row-Level Security (`CREATE SECURITY POLICY`) binding a `SCHEMABINDING` inline TVF as both `FILTER PREDICATE` and `BLOCK PREDICATE`
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

---

## Case study — CrestLine Treasury

CrestLine Treasury requires 99.995% availability against datacenter zone outages plus cross-region DR with RPO <= 5 seconds for Azure SQL Database, quarterly non-disruptive DR drills verified by finance teams, and instant transaction rollback whenever a multi-million-row settlement batch aborts.

The next 3 questions refer to **CrestLine Treasury**. Read the scenario brief once, then answer each item independently.

### 92. Which Azure SQL Database architecture satisfies **both** the `99.995%` intra-region zone-outage availability target AND cross-region disaster recovery with `RPO <= 5 seconds`?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- B. Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`)
- C. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- D. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA

### 93. Which four-step procedure executes the quarterly non-disruptive regional DR drill verified by finance teams without losing a single committed settlement row or changing app connection strings?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Provision secondary SQL server with matching firewall/Private Link & Entra admin → Create Failover Group with coupled DBs → Point apps to `<fog>.database.windows.net` & `.secondary` → Run planned `Switch-AzSqlDatabaseFailoverGroup` drill
- B. Execute unplanned `AllowDataLoss` forced failover during peak checkout → Create secondary logical SQL server afterward → Hardcode regional server names in app connection strings → Skip firewall rules on secondary
- C. Create Failover Group between two servers in the exact same datacenter rack → Add `tempdb` and `master` to Failover Group → Point OLTP writes to `.secondary.database.windows.net` → Disable Geo-Replication
- D. Export nightly `.bacpac` to local laptop → Delete production database to test restore → Manually edit 50 microservice connection strings → Re-enable TDE after 6 hours

### 94. Which built-in Azure SQL engine technology guarantees instantaneous transaction rollback whenever a multi-million-row settlement batch aborts mid-run?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback

---

## Case study — MintBridge FX

MintBridge FX runs SQL Server 2022 compatibility (`160`) workloads on Azure SQL Managed Instance. A single parameterized trade-search query serves both tiny retail accounts and 40M-row institutional desks, reporting queries intermittently spill `Hash Match` operators to `tempdb`, and ad-hoc analysts starve OLTP CPU.

The next 3 questions refer to **MintBridge FX**. Read the scenario brief once, then answer each item independently.

### 95. Why do reporting queries intermittently display yellow exclamation warnings on `Hash Match` operators and spill to `tempdb`, and which IQP feature resolves this under compatibility level `160`?

Domain: Monitor, configure, and optimize database resources

- A. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- B. Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`)
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7

### 96. How do you guarantee ad-hoc risk-analyst sessions never consume more than 25% of instance CPU on the Azure SQL Managed Instance so OLTP trade matching stays responsive?

Domain: Monitor, configure, and optimize database resources

- A. Configure `cost threshold for parallelism`, `MAXDOP`, `max server memory (MB)`, and Resource Governor (`WORKLOAD GROUP` + `RESOURCE POOL` + classifier UDF) on SQL MI / VMs
- B. No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 97. Which compatibility level `160` Intelligent Query Processing feature allows the single parameterized trade-search query to maintain separate cached execution plans for tiny retail accounts versus 40M-row institutional desks simultaneously?

Domain: Monitor, configure, and optimize database resources

- A. Enable compatibility level `160` Intelligent Query Processing (`Parameter Sensitive Plan` optimization, `Memory Grant Feedback` persistence, `Scalar UDF Inlining`, `DOP Feedback`)
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- D. Replace set-based `JOIN` queries with nested `FAST_FORWARD` T-SQL cursors calling multi-statement table-valued functions per row under compat `100`

---

## Case study — QuarryPay Clearing

QuarryPay Clearing is launching a payment-dispute OLTP app inside Microsoft Fabric that needs automatic near-real-time OneLake Delta tables without ETL pipelines, while also moving an existing 1.8 TB database online between two Azure SQL Managed Instances in different VNets with zero data loss.

The next 3 questions refer to **QuarryPay Clearing**. Read the scenario brief once, then answer each item independently.

### 98. Which operational database offering inside Microsoft Fabric gives the payment-dispute app automatic near-real-time OneLake Delta Parquet tables with zero ETL pipelines?

Domain: Plan and implement data platform resources

- A. SQL Server on Azure Virtual Machines (`Ebdsv5` series) with full OS and engine version control
- B. Configure SQL Server password logins (`CREATE LOGIN ... WITH PASSWORD`) and T-SQL `BACKUP DATABASE ... TO DISK` inside SQL database in Microsoft Fabric
- C. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- D. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled

### 99. Before retiring four legacy on-premises SQL Server 2017 clearing databases, you must collect 7 days of PerfMon IOPS/CPU counters to generate right-sized Azure SQL Managed Instance SKU recommendations. Which toolset replaces retired DMA for this task?

Domain: Plan and implement data platform resources

- A. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- B. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Azure Migrate (`Azure SQL` assessment) and the Azure SQL Migration extension for Azure Data Studio / VS Code

### 100. Which network ports must be allowed bidirectionally between the two peered SQL Managed Instance subnets so the 1.8 TB online Database Move succeeds with zero data loss?

Domain: Plan and implement data platform resources

- A. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- B. Log Replay Service (`LRS`) streaming Full, Differential, and Tail-Log backups from Azure Blob Storage into SQL Managed Instance
- C. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- D. Online Azure SQL Managed Instance Database Move / Copy (`TCP 5022` & `11000–11999`, 24-hour manual completion window)

---

## Answer key and explanations

### Question 1 — B

Answer: Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica. Azure SQL Managed Instance Business Critical supports native Service Broker and cross-database transactions on local NVMe SSD storage with an included readable secondary replica. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. Local study-map skill 1.1 (Recommend an Azure SQL Offering (SQL Database, SQL Managed Instance, or SQL Server on Azure VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Compare Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview).

- **A:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Azure SQL Managed Instance Business Critical supports native Service Broker and cross-database transactions on local NVMe SSD storage with an included readable secondary replica.
- **B:** Correct. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. In this scenario: Azure SQL Managed Instance Business Critical supports native Service Broker and cross-database transactions on local NVMe SSD storage with an included readable secondary replica.
- **C:** Incorrect for this requirement. SQL Managed Instance provides near-100% SQL Server engine compatibility (cross-DB queries, SQL Agent, CLR, Service Broker), and Next-gen GP scales IOPS independently of storage up to 500 DBs. Why the keyed choice wins: Azure SQL Managed Instance Business Critical supports native Service Broker and cross-database transactions on local NVMe SSD storage with an included readable secondary replica.
- **D:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Azure SQL Managed Instance Business Critical supports native Service Broker and cross-database transactions on local NVMe SSD storage with an included readable secondary replica.

### Question 2 — A

Answer: Azure SQL Database Hyperscale tier with compute-isolated Named Replicas. Azure SQL Database Hyperscale scales seamlessly to 100 TB using page servers and supports compute-isolated Named Replicas without duplicating underlying storage. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Local study-map skill 1.1 (Recommend an Azure SQL Offering (SQL Database, SQL Managed Instance, or SQL Server on Azure VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Compare Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview).

- **A:** Correct. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. In this scenario: Azure SQL Database Hyperscale scales seamlessly to 100 TB using page servers and supports compute-isolated Named Replicas without duplicating underlying storage.
- **B:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Azure SQL Database Hyperscale scales seamlessly to 100 TB using page servers and supports compute-isolated Named Replicas without duplicating underlying storage.
- **C:** Incorrect for this requirement. SQL Server on Azure VMs (IaaS) provides full OS access, custom third-party drivers, legacy SQL Server version pinning, SSIS/SSRS/SSAS co-hosting, and `Ebdsv5` high remote storage throughput. Why the keyed choice wins: Azure SQL Database Hyperscale scales seamlessly to 100 TB using page servers and supports compute-isolated Named Replicas without duplicating underlying storage.
- **D:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Azure SQL Database Hyperscale scales seamlessly to 100 TB using page servers and supports compute-isolated Named Replicas without duplicating underlying storage.

### Question 3 — B, E

Answers: Create a dedicated VNet subnet (`/28` or larger) with no other cloud resources and delegate it to `Microsoft.Sql/managedInstances`; Associate a User-Defined Route (`UDR`) table (`0.0.0.0/0` -> `Internet` for management plane) and required NSG rules with the SQL MI subnet. Delegate an exclusive `/28+` subnet to `Microsoft.Sql/managedInstances` and bind a compliant User-Defined Route (`UDR`) table and NSG to that subnet. Local study-map skill 1.2 (Choose Automated Deployment Methods and Deploy SQL Offerings Across Windows, Linux, and Containers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated deployment options for Azure SQL and SQL Server on Linux/containers (https://learn.microsoft.com/en-us/azure/azure-sql/database/arm-templates-content-guide).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Delegate an exclusive `/28+` subnet to `Microsoft.Sql/managedInstances` and bind a compliant User-Defined Route (`UDR`) table and NSG to that subnet.
- **B:** Correct. Azure SQL Managed Instance requires an exclusive subnet delegated to `Microsoft.Sql/managedInstances` sized for current and future instance vCore/node counts. In this scenario: Delegate an exclusive `/28+` subnet to `Microsoft.Sql/managedInstances` and bind a compliant User-Defined Route (`UDR`) table and NSG to that subnet.
- **C:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Delegate an exclusive `/28+` subnet to `Microsoft.Sql/managedInstances` and bind a compliant User-Defined Route (`UDR`) table and NSG to that subnet.
- **D:** Incorrect for this requirement. Azure Arc allows variable-workload or seasonal SQL Server hosts outside Azure to be billed hourly through an Azure subscription. Why the keyed choice wins: Delegate an exclusive `/28+` subnet to `Microsoft.Sql/managedInstances` and bind a compliant User-Defined Route (`UDR`) table and NSG to that subnet.
- **E:** Correct. SQL Managed Instance requires an explicit route table and NSG bound to its delegated subnet so Azure management traffic is never blackholed by forced tunneling. In this scenario: Delegate an exclusive `/28+` subnet to `Microsoft.Sql/managedInstances` and bind a compliant User-Defined Route (`UDR`) table and NSG to that subnet.

### Question 4 — C

Answer: SQL Server on Linux configured via `mssql-conf` or Linux container images for consistent CI/CD dev-test parity. Microsoft publishes official Linux container images under `mcr.microsoft.com/mssql/server:2022-latest` for lightweight CI/CD and developer integration testing. `mssql-conf` configures memory, trace flags, Entra auth, and HA on Linux SQL Server VMs, while official Linux container images spin up fast disposable SQL instances in CI pipelines. Local study-map skill 1.2 (Choose Automated Deployment Methods and Deploy SQL Offerings Across Windows, Linux, and Containers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated deployment options for Azure SQL and SQL Server on Linux/containers (https://learn.microsoft.com/en-us/azure/azure-sql/database/arm-templates-content-guide).

- **A:** Incorrect for this requirement. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. Why the keyed choice wins: Microsoft publishes official Linux container images under `mcr.microsoft.com/mssql/server:2022-latest` for lightweight CI/CD and developer integration testing.
- **B:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: Microsoft publishes official Linux container images under `mcr.microsoft.com/mssql/server:2022-latest` for lightweight CI/CD and developer integration testing.
- **C:** Correct. `mssql-conf` configures memory, trace flags, Entra auth, and HA on Linux SQL Server VMs, while official Linux container images spin up fast disposable SQL instances in CI pipelines. In this scenario: Microsoft publishes official Linux container images under `mcr.microsoft.com/mssql/server:2022-latest` for lightweight CI/CD and developer integration testing.
- **D:** Incorrect for this requirement. Azure Arc projects on-premises and multicloud SQL Server instances into Azure for Resource Graph inventory, automated Best Practices Assessments, Entra auth (SQL 2022+), Defender, and PAYG billing. Why the keyed choice wins: Microsoft publishes official Linux container images under `mcr.microsoft.com/mssql/server:2022-latest` for lightweight CI/CD and developer integration testing.

### Question 5 — A, C, E

Answers: Query fleet-wide SQL Server version, edition, and backup status across hybrid servers via Azure Resource Graph Explorer; Enable automated SQL Best Practices Assessments and Microsoft Defender for SQL via the Azure Arc SQL Server extension; Switch eligible hybrid SQL Server instances to hourly Azure Arc pay-as-you-go billing instead of upfront core licenses. SQL Server enabled by Azure Arc provides KQL fleet queries in Azure Resource Graph, automated SQL Best Practices Assessments + Defender for SQL, and optional hourly pay-as-you-go billing. Local study-map skill 1.3 (Identify Use Cases for SQL Server Enabled by Azure Arc and SQL Database in Microsoft Fabric), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server enabled by Azure Arc and SQL database in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/database/sql/overview).

- **A:** Correct. The Azure Extension for SQL Server runs recurring configuration assessments against Microsoft Support rules and integrates Defender vulnerability/threat detection. In this scenario: SQL Server enabled by Azure Arc provides KQL fleet queries in Azure Resource Graph, automated SQL Best Practices Assessments + Defender for SQL, and optional hourly pay-as-you-go billing.
- **B:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: SQL Server enabled by Azure Arc provides KQL fleet queries in Azure Resource Graph, automated SQL Best Practices Assessments + Defender for SQL, and optional hourly pay-as-you-go billing.
- **C:** Correct. Azure Arc allows variable-workload or seasonal SQL Server hosts outside Azure to be billed hourly through an Azure subscription. In this scenario: SQL Server enabled by Azure Arc provides KQL fleet queries in Azure Resource Graph, automated SQL Best Practices Assessments + Defender for SQL, and optional hourly pay-as-you-go billing.
- **D:** Incorrect for this requirement. SQL database in Microsoft Fabric enforces Microsoft Entra authentication exclusively (SQL logins are unsupported) and manages backups/OneLake mirroring automatically as SaaS. Why the keyed choice wins: SQL Server enabled by Azure Arc provides KQL fleet queries in Azure Resource Graph, automated SQL Best Practices Assessments + Defender for SQL, and optional hourly pay-as-you-go billing.
- **E:** Correct. SQL Server enabled by Azure Arc projects on-premises and multicloud instance metadata into Azure Resource Manager for KQL-based Azure Resource Graph inventory queries. In this scenario: SQL Server enabled by Azure Arc provides KQL fleet queries in Azure Resource Graph, automated SQL Best Practices Assessments + Defender for SQL, and optional hourly pay-as-you-go billing.
- **F:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: SQL Server enabled by Azure Arc provides KQL fleet queries in Azure Resource Graph, automated SQL Best Practices Assessments + Defender for SQL, and optional hourly pay-as-you-go billing.

### Question 6 — B

Answer: SPLIT partition function for incoming future boundary → Create empty staging table on same filegroup with matching schema/indexes → ALTER TABLE ... SWITCH oldest partition to staging → Archive staging data & MERGE retired boundary. Split the future boundary first, create an index- and filegroup-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary. Sliding-window partitioning splits a new empty future range first, performs a metadata-only `ALTER TABLE ... SWITCH` into an aligned staging table, and merges the retired boundary. Local study-map skill 1.4 (Plan for Table Partitioning (`RANGE RIGHT` / `SWITCH`) and Horizontal Database Sharding (`ShardMapManager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Table partitioning and scaling out with Azure SQL Database sharding (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-scale-introduction).

- **A:** Incorrect for this requirement. Incorrect workflow: `ALTER TABLE ... SWITCH` swaps metadata between two tables in the same database/filegroup rather than writing directly to Azure Blob Storage. Why the keyed choice wins: Split the future boundary first, create an index- and filegroup-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary.
- **B:** Correct. Sliding-window partitioning splits a new empty future range first, performs a metadata-only `ALTER TABLE ... SWITCH` into an aligned staging table, and merges the retired boundary. In this scenario: Split the future boundary first, create an index- and filegroup-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary.
- **C:** Incorrect for this requirement. Incorrect workflow: `SWITCH` is strictly an intra-database metadata operation requiring identical schema, filegroup alignment, and trusted constraints—never cross-database. Why the keyed choice wins: Split the future boundary first, create an index- and filegroup-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary.
- **D:** Incorrect for this requirement. Incorrect workflow: row-by-row `DELETE` bloats the transaction log and locks tables, and `SWITCH` fails if the staging table resides on a different filegroup or lacks aligned indexes. Why the keyed choice wins: Split the future boundary first, create an index- and filegroup-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary.

### Question 7 — D

Answer: Horizontal sharding using the Elastic Database Client Library (`ShardMapManager` with `ListShardMap` or `RangeShardMap`). Elastic Database Multi-Shard Queries connect via the `ShardMapManager` shard map definition to execute T-SQL across all shards concurrently and merge results client-side. `ListShardMap` maps discrete `TenantId` keys and `RangeShardMap` maps contiguous ID spans to independent Azure SQL Databases, routing data-dependent connections directly from the app tier. Local study-map skill 1.4 (Plan for Table Partitioning (`RANGE RIGHT` / `SWITCH`) and Horizontal Database Sharding (`ShardMapManager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Table partitioning and scaling out with Azure SQL Database sharding (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-scale-introduction).

- **A:** Incorrect for this requirement. `RANGE RIGHT` places each upper-boundary date value cleanly as the lower bound of its own monthly/daily partition, enabling metadata-only `SWITCH` archival when indexes are aligned. Why the keyed choice wins: Elastic Database Multi-Shard Queries connect via the `ShardMapManager` shard map definition to execute T-SQL across all shards concurrently and merge results client-side.
- **B:** Incorrect for this requirement. `sp_estimate_data_compression_savings` models space gains before compressing; `ROW`/`PAGE` shrink OLTP B-trees while `COLUMNSTORE` / `COLUMNSTORE_ARCHIVE` achieves up to 10x analytics compression. Why the keyed choice wins: Elastic Database Multi-Shard Queries connect via the `ShardMapManager` shard map definition to execute T-SQL across all shards concurrently and merge results client-side.
- **C:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Elastic Database Multi-Shard Queries connect via the `ShardMapManager` shard map definition to execute T-SQL across all shards concurrently and merge results client-side.
- **D:** Correct. `ListShardMap` maps discrete `TenantId` keys and `RangeShardMap` maps contiguous ID spans to independent Azure SQL Databases, routing data-dependent connections directly from the app tier. In this scenario: Elastic Database Multi-Shard Queries connect via the `ShardMapManager` shard map definition to execute T-SQL across all shards concurrently and merge results client-side.

### Question 8 — C

Answer: SQL IaaS Agent Extension in Full management mode paired with Azure Update Manager / Automated Patching. The SQL IaaS Agent Extension must be registered on the VM so Azure Resource Manager can validate and toggle `LicenseType AHUB` (Azure Hybrid Benefit) dynamically. The SQL IaaS Agent Extension unlocks portal license conversion (AHB/PAYG), Automated Backup, Automated Patching windows, Key Vault integration, and storage pool management on SQL VMs. Local study-map skill 1.5 (Deploy Hybrid SQL Server Solutions and Manage Patching (`SQL IaaS Agent Extension` & `Azure Update Manager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server IaaS Agent Extension, Automated Patching, and Azure Update Manager (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-agent-extension-manually-register-single-vm).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: The SQL IaaS Agent Extension must be registered on the VM so Azure Resource Manager can validate and toggle `LicenseType AHUB` (Azure Hybrid Benefit) dynamically.
- **B:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: The SQL IaaS Agent Extension must be registered on the VM so Azure Resource Manager can validate and toggle `LicenseType AHUB` (Azure Hybrid Benefit) dynamically.
- **C:** Correct. The SQL IaaS Agent Extension unlocks portal license conversion (AHB/PAYG), Automated Backup, Automated Patching windows, Key Vault integration, and storage pool management on SQL VMs. In this scenario: The SQL IaaS Agent Extension must be registered on the VM so Azure Resource Manager can validate and toggle `LicenseType AHUB` (Azure Hybrid Benefit) dynamically.
- **D:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: The SQL IaaS Agent Extension must be registered on the VM so Azure Resource Manager can validate and toggle `LicenseType AHUB` (Azure Hybrid Benefit) dynamically.

### Question 9 — D

Answer: SQL Server enabled by Azure Arc (`Microsoft.AzureArcData/sqlServerInstances`). Onboarding the branch SQL Server 2022 instances to Azure Arc enables Microsoft Entra ID authentication and Purview governance policies on-premises. Azure Arc projects on-premises and multicloud SQL Server instances into Azure for Resource Graph inventory, automated Best Practices Assessments, Entra auth (SQL 2022+), Defender, and PAYG billing. Local study-map skill 1.5 (Deploy Hybrid SQL Server Solutions and Manage Patching (`SQL IaaS Agent Extension` & `Azure Update Manager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server IaaS Agent Extension, Automated Patching, and Azure Update Manager (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-agent-extension-manually-register-single-vm).

- **A:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Onboarding the branch SQL Server 2022 instances to Azure Arc enables Microsoft Entra ID authentication and Purview governance policies on-premises.
- **B:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: Onboarding the branch SQL Server 2022 instances to Azure Arc enables Microsoft Entra ID authentication and Purview governance policies on-premises.
- **C:** Incorrect for this requirement. Elastic Pools share a pooled vCore/storage envelope across many multi-tenant databases with staggered peaks while capping per-database max vCores to stop noisy-neighbor starvation. Why the keyed choice wins: Onboarding the branch SQL Server 2022 instances to Azure Arc enables Microsoft Entra ID authentication and Purview governance policies on-premises.
- **D:** Correct. Azure Arc projects on-premises and multicloud SQL Server instances into Azure for Resource Graph inventory, automated Best Practices Assessments, Entra auth (SQL 2022+), Defender, and PAYG billing. In this scenario: Onboarding the branch SQL Server 2022 instances to Azure Arc enables Microsoft Entra ID authentication and Purview governance policies on-premises.

### Question 10 — C

Answer: Azure SQL Database vCore Elastic Pool with per-database min and max vCore limits. A 32-vCore Elastic Pool configured with per-database `max vCores = 8` time-multiplexes compute across staggered global time zones while isolating noisy neighbors. Elastic Pools share a pooled vCore/storage envelope across many multi-tenant databases with staggered peaks while capping per-database max vCores to stop noisy-neighbor starvation. Local study-map skill 1.6 (Configure Azure SQL Database for Scale and Performance (`Serverless`, `Hyperscale` Named Replicas, `Elastic Pools`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure SQL Database vCore, Serverless, Hyperscale, and Elastic Pools (https://learn.microsoft.com/en-us/azure/azure-sql/database/service-tiers-vcore).

- **A:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: A 32-vCore Elastic Pool configured with per-database `max vCores = 8` time-multiplexes compute across staggered global time zones while isolating noisy neighbors.
- **B:** Incorrect for this requirement. SQL Server on Azure VMs (IaaS) provides full OS access, custom third-party drivers, legacy SQL Server version pinning, SSIS/SSRS/SSAS co-hosting, and `Ebdsv5` high remote storage throughput. Why the keyed choice wins: A 32-vCore Elastic Pool configured with per-database `max vCores = 8` time-multiplexes compute across staggered global time zones while isolating noisy neighbors.
- **C:** Correct. Elastic Pools share a pooled vCore/storage envelope across many multi-tenant databases with staggered peaks while capping per-database max vCores to stop noisy-neighbor starvation. In this scenario: A 32-vCore Elastic Pool configured with per-database `max vCores = 8` time-multiplexes compute across staggered global time zones while isolating noisy neighbors.
- **D:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: A 32-vCore Elastic Pool configured with per-database `max vCores = 8` time-multiplexes compute across staggered global time zones while isolating noisy neighbors.

### Question 11 — D

Answer: Azure SQL Managed Instance (Next-gen General Purpose) with decoupled IOPS and storage sliders. Upgrading to Next-gen General Purpose on Azure SQL Managed Instance raises the limit to 500 databases and exposes independent IOPS and storage throughput sliders. SQL Managed Instance provides near-100% SQL Server engine compatibility (cross-DB queries, SQL Agent, CLR, Service Broker), and Next-gen GP scales IOPS independently of storage up to 500 DBs. Local study-map skill 1.7 (Configure Azure SQL Managed Instance for Scale and Performance (`Next-gen GP` Sliders & `Business Critical`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure SQL Managed Instance service tiers and Next-gen General Purpose scaling (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview).

- **A:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: Upgrading to Next-gen General Purpose on Azure SQL Managed Instance raises the limit to 500 databases and exposes independent IOPS and storage throughput sliders.
- **B:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Upgrading to Next-gen General Purpose on Azure SQL Managed Instance raises the limit to 500 databases and exposes independent IOPS and storage throughput sliders.
- **C:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Upgrading to Next-gen General Purpose on Azure SQL Managed Instance raises the limit to 500 databases and exposes independent IOPS and storage throughput sliders.
- **D:** Correct. SQL Managed Instance provides near-100% SQL Server engine compatibility (cross-DB queries, SQL Agent, CLR, Service Broker), and Next-gen GP scales IOPS independently of storage up to 500 DBs. In this scenario: Upgrading to Next-gen General Purpose on Azure SQL Managed Instance raises the limit to 500 databases and exposes independent IOPS and storage throughput sliders.

### Question 12 — A, D

Answers: Configure `ReadOnly` Azure host caching on Premium SSD data disks hosting `.mdf` and `.ndf` database files; Configure `None` Azure host caching on dedicated managed disks hosting `.ldf` SQL Server transaction log files. Set `ReadOnly` host caching on Premium SSD data disks (`.mdf`/`.ndf`) and `None` host caching on transaction log disks (`.ldf`). Local study-map skill 1.8 (Configure SQL Server on Azure VMs for Scale and Performance (`ReadOnly`/`None` Host Caching, `tempdb` NVMe, `IFI`/`LPIM`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Performance best practices for SQL Server on Azure Virtual Machines (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-checklist).

- **A:** Correct. `ReadOnly` host caching serves random OLTP data-page reads directly from Azure hypervisor RAM/SSD cache without consuming disk IOPS. In this scenario: Set `ReadOnly` host caching on Premium SSD data disks (`.mdf`/`.ndf`) and `None` host caching on transaction log disks (`.ldf`).
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Set `ReadOnly` host caching on Premium SSD data disks (`.mdf`/`.ndf`) and `None` host caching on transaction log disks (`.ldf`).
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Set `ReadOnly` host caching on Premium SSD data disks (`.mdf`/`.ndf`) and `None` host caching on transaction log disks (`.ldf`).
- **D:** Correct. Transaction log files perform sequential write-through flushes that do not benefit from read caching and must use `None` host caching. In this scenario: Set `ReadOnly` host caching on Premium SSD data disks (`.mdf`/`.ndf`) and `None` host caching on transaction log disks (`.ldf`).
- **E:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Set `ReadOnly` host caching on Premium SSD data disks (`.mdf`/`.ndf`) and `None` host caching on transaction log disks (`.ldf`).

### Question 13 — B

Answer: Premium SSD v2 / striped Premium SSD with `ReadOnly` host caching for data disks, `None` for log disks, and `tempdb` on local NVMe. Register the VM with the SQL IaaS Agent Extension Storage Configuration (or configure a Windows scheduled startup PowerShell task running before `MSSQLSERVER`) to recreate the `D:\SQLTempDB` directory automatically on boot. SQL Server Azure VM best practices use `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` caching on `.ldf` transaction log disks, and ephemeral NVMe/`D:` storage for `tempdb`. Local study-map skill 1.8 (Configure SQL Server on Azure VMs for Scale and Performance (`ReadOnly`/`None` Host Caching, `tempdb` NVMe, `IFI`/`LPIM`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Performance best practices for SQL Server on Azure Virtual Machines (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-checklist).

- **A:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Register the VM with the SQL IaaS Agent Extension Storage Configuration (or configure a Windows scheduled startup PowerShell task running before `MSSQLSERVER`) to recreate the `D:\SQLTempDB` directory automatically on boot.
- **B:** Correct. SQL Server Azure VM best practices use `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` caching on `.ldf` transaction log disks, and ephemeral NVMe/`D:` storage for `tempdb`. In this scenario: Register the VM with the SQL IaaS Agent Extension Storage Configuration (or configure a Windows scheduled startup PowerShell task running before `MSSQLSERVER`) to recreate the `D:\SQLTempDB` directory automatically on boot.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Register the VM with the SQL IaaS Agent Extension Storage Configuration (or configure a Windows scheduled startup PowerShell task running before `MSSQLSERVER`) to recreate the `D:\SQLTempDB` directory automatically on boot.
- **D:** Incorrect for this requirement. SQL Server write-ahead logging performs sequential unbuffered writes; enabling `ReadOnly` or `ReadWrite` host caching on `.ldf` disks degrades throughput or risks corruption. Why the keyed choice wins: Register the VM with the SQL IaaS Agent Extension Storage Configuration (or configure a Windows scheduled startup PowerShell task running before `MSSQLSERVER`) to recreate the `D:\SQLTempDB` directory automatically on boot.

### Question 14 — A

Answer: Evaluate `sp_estimate_data_compression_savings` and apply `ROW`, `PAGE`, or `COLUMNSTORE_ARCHIVE` compression per partition. `COLUMNSTORE_ARCHIVE` adds Microsoft XPRESS stream compression on top of standard `COLUMNSTORE` encoding, shrinking cold analytical partitions even further at minor CPU decompression cost. `sp_estimate_data_compression_savings` models space gains before compressing; `ROW`/`PAGE` shrink OLTP B-trees while `COLUMNSTORE` / `COLUMNSTORE_ARCHIVE` achieves up to 10x analytics compression. Local study-map skill 1.9 (Configure Table Partitioning Alignment and Data Compression (`ROW`, `PAGE`, `COLUMNSTORE`, `COLUMNSTORE_ARCHIVE`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure table partitioning and row/page/columnstore data compression (https://learn.microsoft.com/en-us/sql/relational-databases/data-compression/data-compression).

- **A:** Correct. `sp_estimate_data_compression_savings` models space gains before compressing; `ROW`/`PAGE` shrink OLTP B-trees while `COLUMNSTORE` / `COLUMNSTORE_ARCHIVE` achieves up to 10x analytics compression. In this scenario: `COLUMNSTORE_ARCHIVE` adds Microsoft XPRESS stream compression on top of standard `COLUMNSTORE` encoding, shrinking cold analytical partitions even further at minor CPU decompression cost.
- **B:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: `COLUMNSTORE_ARCHIVE` adds Microsoft XPRESS stream compression on top of standard `COLUMNSTORE` encoding, shrinking cold analytical partitions even further at minor CPU decompression cost.
- **C:** Incorrect for this requirement. Row-by-row cursors and multi-statement TVFs under legacy compatibility levels execute thousands of iterative context switches and 1-row cardinality guesses. Why the keyed choice wins: `COLUMNSTORE_ARCHIVE` adds Microsoft XPRESS stream compression on top of standard `COLUMNSTORE` encoding, shrinking cold analytical partitions even further at minor CPU decompression cost.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `COLUMNSTORE_ARCHIVE` adds Microsoft XPRESS stream compression on top of standard `COLUMNSTORE` encoding, shrinking cold analytical partitions even further at minor CPU decompression cost.

### Question 15 — C

Answer: Enable Availability Groups & master key on SQL Server → Establish VNet/IPsec network peering on TCP 5022 → Create Managed Instance link & seed distributed AG → Validate sync state and execute planned cutover to SQL MI. Enable Availability Groups and a master key on SQL Server, establish VNet/IPsec peering over TCP `5022`, create and seed the Managed Instance link distributed AG, and trigger planned cutover once synchronized. Managed Instance link uses a distributed Availability Group over port 5022 to seed and continuously replicate transaction logs online before executing a near-zero-downtime cutover. Local study-map skill 1.11 (Implement Online and Offline Migrations to and Between Azure SQL Services (`MI Link`, `LRS`, `SqlPackage` Copy)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Online and offline SQL migrations with Managed Instance link, Log Replay Service, and SqlPackage (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-feature-overview).

- **A:** Incorrect for this requirement. Incorrect order: distributed AG prerequisites and TCP 5022 network connectivity must be in place before creating and seeding a Managed Instance link. Why the keyed choice wins: Enable Availability Groups and a master key on SQL Server, establish VNet/IPsec peering over TCP `5022`, create and seed the Managed Instance link distributed AG, and trigger planned cutover once synchronized.
- **B:** Incorrect for this requirement. Incorrect workflow: `.bacpac` logical export/import is neither transactional on a live DB without a copy nor how Managed Instance link distributed AG replication operates. Why the keyed choice wins: Enable Availability Groups and a master key on SQL Server, establish VNet/IPsec peering over TCP `5022`, create and seed the Managed Instance link distributed AG, and trigger planned cutover once synchronized.
- **C:** Correct. Managed Instance link uses a distributed Availability Group over port 5022 to seed and continuously replicate transaction logs online before executing a near-zero-downtime cutover. In this scenario: Enable Availability Groups and a master key on SQL Server, establish VNet/IPsec peering over TCP `5022`, create and seed the Managed Instance link distributed AG, and trigger planned cutover once synchronized.
- **D:** Incorrect for this requirement. Incorrect workflow: SQL Managed Instance does not support attaching raw `.mdf`/`.ldf` files from SMB shares, and taking SQL Server offline defeats online migration. Why the keyed choice wins: Enable Availability Groups and a master key on SQL Server, establish VNet/IPsec peering over TCP `5022`, create and seed the Managed Instance link distributed AG, and trigger planned cutover once synchronized.

### Question 16 — D

Answer: Enable Microsoft Entra-only authentication (`azuread_authentication_only`) on the logical SQL server or SQL Managed Instance. A Microsoft Entra administrator (user, security group, or service principal) must already be assigned on the logical SQL server before Entra-only authentication can be enabled. Microsoft Entra-only authentication disables legacy SQL Server logins (`sa` and password auth) completely, enforcing centralized MFA, Conditional Access, and token-based Managed Identities. Local study-map skill 2.1 (Configure Microsoft Entra ID and Microsoft Entra-Only Authentication Across SQL DB, SQL MI, and SQL Server), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure and manage Microsoft Entra authentication with Azure SQL and SQL Server (https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: A Microsoft Entra administrator (user, security group, or service principal) must already be assigned on the logical SQL server before Entra-only authentication can be enabled.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: A Microsoft Entra administrator (user, security group, or service principal) must already be assigned on the logical SQL server before Entra-only authentication can be enabled.
- **C:** Incorrect for this requirement. Restoring a `.bak` onto another instance mismatches login SIDs (fixed via `ALTER USER ... WITH LOGIN`), while an explicit table/schema `DENY` always overrides `db_datareader` role `GRANT`s. Why the keyed choice wins: A Microsoft Entra administrator (user, security group, or service principal) must already be assigned on the logical SQL server before Entra-only authentication can be enabled.
- **D:** Correct. Microsoft Entra-only authentication disables legacy SQL Server logins (`sa` and password auth) completely, enforcing centralized MFA, Conditional Access, and token-based Managed Identities. In this scenario: A Microsoft Entra administrator (user, security group, or service principal) must already be assigned on the logical SQL server before Entra-only authentication can be enabled.

### Question 17 — D

Answer: Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or `Entra Kerberos`). Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos issues realm trust tickets directly from Entra ID. Microsoft Entra Kerberos issues Kerberos tickets for SQL Managed Instance without requiring customer-managed Active Directory Domain Services domain controllers inside Azure. Local study-map skill 2.2 (Configure Authentication for SQL Server on Azure VMs and SQL MI (`Microsoft Entra Kerberos` & AD Trusts)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos and AD (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/winauth-azuread-overview).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos issues realm trust tickets directly from Entra ID.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos issues realm trust tickets directly from Entra ID.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos issues realm trust tickets directly from Entra ID.
- **D:** Correct. Microsoft Entra Kerberos issues Kerberos tickets for SQL Managed Instance without requiring customer-managed Active Directory Domain Services domain controllers inside Azure. In this scenario: Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos issues realm trust tickets directly from Entra ID.

### Question 18 — B

Answer: Stored procedure encapsulation using schema ownership chaining, `EXECUTE AS OWNER`, or certificate module signing. Sign `Treasury.usp_PostJournal` with a database certificate (`ADD SIGNATURE TO Treasury.usp_PostJournal BY CERTIFICATE ...`) mapped to a signature user holding `INSERT` on `Treasury.LedgerEntries`, and grant callers only `EXECUTE`. Granting `EXECUTE` on a schema-owned or certificate-signed stored procedure lets callers run controlled DML/DDL workflows without direct table-level `SELECT`, `UPDATE`, or `IMPERSONATE` rights. Local study-map skill 2.4 (Apply Least Privilege Using Granular Server/Database Roles, Schema Chaining, `EXECUTE AS`, and T-SQL/GUI Tools), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Permissions hierarchy, server-level roles, and principle of least privilege in SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/security-server-roles).

- **A:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Sign `Treasury.usp_PostJournal` with a database certificate (`ADD SIGNATURE TO Treasury.usp_PostJournal BY CERTIFICATE ...`) mapped to a signature user holding `INSERT` on `Treasury.LedgerEntries`, and grant callers only `EXECUTE`.
- **B:** Correct. Granting `EXECUTE` on a schema-owned or certificate-signed stored procedure lets callers run controlled DML/DDL workflows without direct table-level `SELECT`, `UPDATE`, or `IMPERSONATE` rights. In this scenario: Sign `Treasury.usp_PostJournal` with a database certificate (`ADD SIGNATURE TO Treasury.usp_PostJournal BY CERTIFICATE ...`) mapped to a signature user holding `INSERT` on `Treasury.LedgerEntries`, and grant callers only `EXECUTE`.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Sign `Treasury.usp_PostJournal` with a database certificate (`ADD SIGNATURE TO Treasury.usp_PostJournal BY CERTIFICATE ...`) mapped to a signature user holding `INSERT` on `Treasury.LedgerEntries`, and grant callers only `EXECUTE`.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Sign `Treasury.usp_PostJournal` with a database certificate (`ADD SIGNATURE TO Treasury.usp_PostJournal BY CERTIFICATE ...`) mapped to a signature user holding `INSERT` on `Treasury.LedgerEntries`, and grant callers only `EXECUTE`.

### Question 19 — A

Answer: Built-in granular server-level roles (`##MS_ServerStateReader##`, `##MS_DefinitionReader##`) or `GRANT VIEW DATABASE PERFORMANCE STATE`. Assigning `##MS_DatabaseManager##` (`CREATE ANY DATABASE` permissions on the logical SQL server) lets the CI/CD principal create and manage databases under least privilege. Modern granular server roles and state permissions let monitoring accounts inspect DMVs and metadata without granting `sysadmin`, `db_owner`, or `SELECT` access to user tables. Local study-map skill 2.4 (Apply Least Privilege Using Granular Server/Database Roles, Schema Chaining, `EXECUTE AS`, and T-SQL/GUI Tools), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Permissions hierarchy, server-level roles, and principle of least privilege in SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/security-server-roles).

- **A:** Correct. Modern granular server roles and state permissions let monitoring accounts inspect DMVs and metadata without granting `sysadmin`, `db_owner`, or `SELECT` access to user tables. In this scenario: Assigning `##MS_DatabaseManager##` (`CREATE ANY DATABASE` permissions on the logical SQL server) lets the CI/CD principal create and manage databases under least privilege.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Assigning `##MS_DatabaseManager##` (`CREATE ANY DATABASE` permissions on the logical SQL server) lets the CI/CD principal create and manage databases under least privilege.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Assigning `##MS_DatabaseManager##` (`CREATE ANY DATABASE` permissions on the logical SQL server) lets the CI/CD principal create and manage databases under least privilege.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Assigning `##MS_DatabaseManager##` (`CREATE ANY DATABASE` permissions on the logical SQL server) lets the CI/CD principal create and manage databases under least privilege.

### Question 20 — B

Answer: Remap orphaned database users (`ALTER USER [u] WITH LOGIN = [u]`) and inspect explicit `DENY` permissions via `sys.database_permissions`. Executing `ALTER USER [clearing_app] WITH LOGIN = [clearing_app]` updates the database user's `SID` in `sys.database_principals` to match `sys.server_principals` without deprecated procedures. Restoring a `.bak` onto another instance mismatches login SIDs (fixed via `ALTER USER ... WITH LOGIN`), while an explicit table/schema `DENY` always overrides `db_datareader` role `GRANT`s. Local study-map skill 2.5 (Troubleshoot Authentication and Authorization Issues (Orphaned Users `ALTER USER WITH LOGIN` & `DENY` Precedence)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot SQL login, orphaned user, and Microsoft Entra authorization issues (https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/troubleshoot-orphaned-users-sql-server).

- **A:** Incorrect for this requirement. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. Why the keyed choice wins: Executing `ALTER USER [clearing_app] WITH LOGIN = [clearing_app]` updates the database user's `SID` in `sys.database_principals` to match `sys.server_principals` without deprecated procedures.
- **B:** Correct. Restoring a `.bak` onto another instance mismatches login SIDs (fixed via `ALTER USER ... WITH LOGIN`), while an explicit table/schema `DENY` always overrides `db_datareader` role `GRANT`s. In this scenario: Executing `ALTER USER [clearing_app] WITH LOGIN = [clearing_app]` updates the database user's `SID` in `sys.database_principals` to match `sys.server_principals` without deprecated procedures.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Executing `ALTER USER [clearing_app] WITH LOGIN = [clearing_app]` updates the database user's `SID` in `sys.database_principals` to match `sys.server_principals` without deprecated procedures.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Executing `ALTER USER [clearing_app] WITH LOGIN = [clearing_app]` updates the database user's `SID` in `sys.database_principals` to match `sys.server_principals` without deprecated procedures.

### Question 21 — A

Answer: Enable Soft Delete & Purge Protection on Key Vault → Assign Managed Identity to SQL server → Grant Key Vault Crypto Service Encryption User (`get`/`wrapKey`/`unwrapKey`) → Set server TDE protector to Key Vault key. Confirm Soft Delete and Purge Protection on Key Vault/HSM, assign a Managed Identity to the SQL server, grant `get`/`wrapKey`/`unwrapKey` Crypto RBAC, and set the server TDE protector to the key URI. Customer-Managed TDE requires Soft Delete and Purge Protection on Key Vault, a server Managed Identity granted `get`/`wrapKey`/`unwrapKey` permissions, and assigning the Key Vault key as TDE protector. Local study-map skill 2.6 (Implement Transparent Data Encryption (`TDE`) with Service-Managed Keys, Key Vault `CMK`, and VM Cert Backups), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Transparent Data Encryption (TDE) with service-managed and customer-managed keys in Key Vault (https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview).

- **A:** Correct. Customer-Managed TDE requires Soft Delete and Purge Protection on Key Vault, a server Managed Identity granted `get`/`wrapKey`/`unwrapKey` permissions, and assigning the Key Vault key as TDE protector. In this scenario: Confirm Soft Delete and Purge Protection on Key Vault/HSM, assign a Managed Identity to the SQL server, grant `get`/`wrapKey`/`unwrapKey` Crypto RBAC, and set the server TDE protector to the key URI.
- **B:** Incorrect for this requirement. Incorrect workflow: Azure SQL refuses Key Vault TDE protectors unless Soft Delete and Purge Protection are enabled and key-wrapping permissions are granted beforehand. Why the keyed choice wins: Confirm Soft Delete and Purge Protection on Key Vault/HSM, assign a Managed Identity to the SQL server, grant `get`/`wrapKey`/`unwrapKey` Crypto RBAC, and set the server TDE protector to the key URI.
- **C:** Incorrect for this requirement. Incorrect workflow: TDE CMK wraps the Database Encryption Key via asymmetric RSA keys in Azure Key Vault or Managed HSM, not `tempdb` symmetric keys. Why the keyed choice wins: Confirm Soft Delete and Purge Protection on Key Vault/HSM, assign a Managed Identity to the SQL server, grant `get`/`wrapKey`/`unwrapKey` Crypto RBAC, and set the server TDE protector to the key URI.
- **D:** Incorrect for this requirement. Incorrect workflow: Azure SQL CMK TDE integrates exclusively with Azure Key Vault or Azure Key Vault Managed HSM using Managed Identity, never anonymous storage URLs. Why the keyed choice wins: Confirm Soft Delete and Purge Protection on Key Vault/HSM, assign a Managed Identity to the SQL server, grant `get`/`wrapKey`/`unwrapKey` Crypto RBAC, and set the server TDE protector to the key URI.

### Question 22 — C, D

Answers: Enable both `Soft Delete` and `Purge Protection` on the Azure Key Vault or Managed HSM storing the TDE protector key; Grant the SQL server Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) on the Key Vault. Keep `Soft Delete` and `Purge Protection` enabled on Key Vault, and maintain `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) for the SQL server Managed Identity. Local study-map skill 2.6 (Implement Transparent Data Encryption (`TDE`) with Service-Managed Keys, Key Vault `CMK`, and VM Cert Backups), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Transparent Data Encryption (TDE) with service-managed and customer-managed keys in Key Vault (https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Keep `Soft Delete` and `Purge Protection` enabled on Key Vault, and maintain `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) for the SQL server Managed Identity.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Keep `Soft Delete` and `Purge Protection` enabled on Key Vault, and maintain `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) for the SQL server Managed Identity.
- **C:** Correct. The logical SQL server or SQL MI Managed Identity requires `get`, `wrapKey`, and `unwrapKey` permissions to wrap and unwrap the Database Encryption Key (`DEK`). In this scenario: Keep `Soft Delete` and `Purge Protection` enabled on Key Vault, and maintain `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) for the SQL server Managed Identity.
- **D:** Correct. Azure SQL requires both Soft Delete and Purge Protection on Key Vault so accidental or malicious key deletion can never permanently brick encrypted databases. In this scenario: Keep `Soft Delete` and `Purge Protection` enabled on Key Vault, and maintain `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) for the SQL server Managed Identity.
- **E:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: Keep `Soft Delete` and `Purge Protection` enabled on Key Vault, and maintain `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) for the SQL server Managed Identity.

### Question 23 — A

Answer: Column-level encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey`) plus `Minimal TLS version = 1.2`. Database Master Key (`DMK`, protected by the Service Master Key/password) -> Certificate (`CREATE CERTIFICATE`) -> Symmetric Key (`CREATE SYMMETRIC KEY ... ENCRYPTION BY CERTIFICATE`) -> `EncryptByKey()`. T-SQL cell-level symmetric key encryption protects specific columns inside the engine while enforcing TLS 1.2+ encrypts all TDS client traffic in transit. Local study-map skill 2.7 (Implement Object/Column-Level Encryption (`Symmetric Keys` / `Certificates`) and Enforce `Minimal TLS 1.2`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Column-level symmetric key encryption and TLS 1.2 in-transit encryption (https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/encrypt-a-column-of-data).

- **A:** Correct. T-SQL cell-level symmetric key encryption protects specific columns inside the engine while enforcing TLS 1.2+ encrypts all TDS client traffic in transit. In this scenario: Database Master Key (`DMK`, protected by the Service Master Key/password) -> Certificate (`CREATE CERTIFICATE`) -> Symmetric Key (`CREATE SYMMETRIC KEY ... ENCRYPTION BY CERTIFICATE`) -> `EncryptByKey()`.
- **B:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Database Master Key (`DMK`, protected by the Service Master Key/password) -> Certificate (`CREATE CERTIFICATE`) -> Symmetric Key (`CREATE SYMMETRIC KEY ... ENCRYPTION BY CERTIFICATE`) -> `EncryptByKey()`.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Database Master Key (`DMK`, protected by the Service Master Key/password) -> Certificate (`CREATE CERTIFICATE`) -> Symmetric Key (`CREATE SYMMETRIC KEY ... ENCRYPTION BY CERTIFICATE`) -> `EncryptByKey()`.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Database Master Key (`DMK`, protected by the Service Master Key/password) -> Certificate (`CREATE CERTIFICATE`) -> Symmetric Key (`CREATE SYMMETRIC KEY ... ENCRYPTION BY CERTIFICATE`) -> `EncryptByKey()`.

### Question 24 — A

Answer: Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database. Querying `sys.database_firewall_rules` inside the user database displays database-scoped rules created via `sp_set_database_firewall_rule` (whereas `sys.firewall_rules` lives in `master`). Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Local study-map skill 2.8 (Configure Server-Level (`master`) vs Portable Database-Level IP Firewall Rules (`sp_set_database_firewall_rule`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Server-level and database-level IP firewall rules in Azure SQL Database (https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure).

- **A:** Correct. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. In this scenario: Querying `sys.database_firewall_rules` inside the user database displays database-scoped rules created via `sp_set_database_firewall_rule` (whereas `sys.firewall_rules` lives in `master`).
- **B:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Querying `sys.database_firewall_rules` inside the user database displays database-scoped rules created via `sp_set_database_firewall_rule` (whereas `sys.firewall_rules` lives in `master`).
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Querying `sys.database_firewall_rules` inside the user database displays database-scoped rules created via `sp_set_database_firewall_rule` (whereas `sys.firewall_rules` lives in `master`).
- **D:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: Querying `sys.database_firewall_rules` inside the user database displays database-scoped rules created via `sp_set_database_firewall_rule` (whereas `sys.firewall_rules` lives in `master`).

### Question 25 — A, B

Answers: Provision a Column Master Key in Key Vault and create a Column Encryption Key with `ENCLAVE_COMPUTATIONS` enabled; Enable `Column Encryption Setting=Enabled` and pass the `Enclave Attestation Url` (or VBS zero-attestation setting) in client drivers. Create an enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`) protected by a Key Vault CMK, and set `Column Encryption Setting=Enabled` (plus enclave attestation settings) in client drivers. Local study-map skill 2.9 (Implement Always Encrypted (`Deterministic` vs `Randomized`) and Always Encrypted with VBS/SGX Secure Enclaves), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always Encrypted and Always Encrypted with secure enclaves (https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves).

- **A:** Correct. Rich confidential queries (`LIKE`, `<`, `>`, sorting) and in-place encryption require a CEK explicitly marked to permit enclave computations. In this scenario: Create an enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`) protected by a Key Vault CMK, and set `Column Encryption Setting=Enabled` (plus enclave attestation settings) in client drivers.
- **B:** Correct. Client drivers must enable Always Encrypted and verify enclave attestation before transmitting CEKs over TLS into the SQL secure enclave. In this scenario: Create an enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`) protected by a Key Vault CMK, and set `Column Encryption Setting=Enabled` (plus enclave attestation settings) in client drivers.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Create an enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`) protected by a Key Vault CMK, and set `Column Encryption Setting=Enabled` (plus enclave attestation settings) in client drivers.
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Create an enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`) protected by a Key Vault CMK, and set `Column Encryption Setting=Enabled` (plus enclave attestation settings) in client drivers.
- **E:** Incorrect for this requirement. Transaction log files perform sequential write-through flushes that do not benefit from read caching and must use `None` host caching. Why the keyed choice wins: Create an enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`) protected by a Key Vault CMK, and set `Column Encryption Setting=Enabled` (plus enclave attestation settings) in client drivers.

### Question 26 — A

Answer: Always Encrypted (`Randomized` for maximum security with zero equality leakage; `Deterministic` only when `=` joins or `GROUP BY` are required). Use `Deterministic` encryption for `AccountTaxId` so equality joins/lookups work, and `Randomized` encryption for `WireMemoNotes` to guarantee distinct ciphertexts and zero frequency leakage. Always Encrypted keeps Column Master Keys on trusted clients/Key Vault; `Randomized` produces distinct ciphertexts for identical plaintexts while `Deterministic` enables equality lookups. Local study-map skill 2.9 (Implement Always Encrypted (`Deterministic` vs `Randomized`) and Always Encrypted with VBS/SGX Secure Enclaves), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always Encrypted and Always Encrypted with secure enclaves (https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves).

- **A:** Correct. Always Encrypted keeps Column Master Keys on trusted clients/Key Vault; `Randomized` produces distinct ciphertexts for identical plaintexts while `Deterministic` enables equality lookups. In this scenario: Use `Deterministic` encryption for `AccountTaxId` so equality joins/lookups work, and `Randomized` encryption for `WireMemoNotes` to guarantee distinct ciphertexts and zero frequency leakage.
- **B:** Incorrect for this requirement. Secure enclaves delegate column decryption into an isolated memory region inside SQL, unlocking `LIKE`, `<`, `>`, `ORDER BY`, and fast in-place initial encryption without exposing plaintext to DBAs. Why the keyed choice wins: Use `Deterministic` encryption for `AccountTaxId` so equality joins/lookups work, and `Randomized` encryption for `WireMemoNotes` to guarantee distinct ciphertexts and zero frequency leakage.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Use `Deterministic` encryption for `AccountTaxId` so equality joins/lookups work, and `Randomized` encryption for `WireMemoNotes` to guarantee distinct ciphertexts and zero frequency leakage.
- **D:** Incorrect for this requirement. BYOK TDE wraps the symmetric Database Encryption Key (`DEK`) with an asymmetric RSA key in Key Vault or Managed HSM so security admins control key rotation and instant revocation. Why the keyed choice wins: Use `Deterministic` encryption for `AccountTaxId` so equality joins/lookups work, and `Randomized` encryption for `WireMemoNotes` to guarantee distinct ciphertexts and zero frequency leakage.

### Question 27 — A, B

Answers: Link Private DNS Zone `privatelink.database.windows.net` (or forward on-premises DNS) to resolve `<server>.database.windows.net` to the private IP; Set `Public network access = Disabled` (`publicNetworkAccess: Disabled`) on the logical SQL server so internet connections are rejected. Configure Private DNS Zone `privatelink.database.windows.net` (linked to the VNet/DNS forwarder) and set `Public network access = Disabled` on the logical SQL server. Local study-map skill 2.10 (Configure Azure Private Link (`privatelink.database.windows.net`), Service Endpoints, and SQL MI Subnet Security), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure Private Link, Virtual Network service endpoints, and SQL MI VNet security (https://learn.microsoft.com/en-us/azure/azure-sql/database/private-endpoint-overview).

- **A:** Correct. Clients still validate the TLS certificate for `<server>.database.windows.net`, so split-brain DNS must map the canonical FQDN via CNAME to `privatelink.database.windows.net`. In this scenario: Configure Private DNS Zone `privatelink.database.windows.net` (linked to the VNet/DNS forwarder) and set `Public network access = Disabled` on the logical SQL server.
- **B:** Correct. Creating a Private Endpoint alone leaves the public endpoint reachable unless `Public network access` is explicitly disabled on the server. In this scenario: Configure Private DNS Zone `privatelink.database.windows.net` (linked to the VNet/DNS forwarder) and set `Public network access = Disabled` on the logical SQL server.
- **C:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: Configure Private DNS Zone `privatelink.database.windows.net` (linked to the VNet/DNS forwarder) and set `Public network access = Disabled` on the logical SQL server.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure Private DNS Zone `privatelink.database.windows.net` (linked to the VNet/DNS forwarder) and set `Public network access = Disabled` on the logical SQL server.
- **E:** Incorrect for this requirement. Azure Arc allows variable-workload or seasonal SQL Server hosts outside Azure to be billed hourly through an Azure subscription. Why the keyed choice wins: Configure Private DNS Zone `privatelink.database.windows.net` (linked to the VNet/DNS forwarder) and set `Public network access = Disabled` on the logical SQL server.

### Question 28 — C

Answer: Yes — the proposed configuration satisfies every stated technical, security, and availability requirement. Yes — Outbound Firewall Rules restrict outbound network connections initiated by Azure SQL Database or SQL Managed Instance solely to approved storage/Entra FQDNs, preventing unauthorized data exfiltration. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. Local study-map skill 2.10 (Configure Azure Private Link (`privatelink.database.windows.net`), Service Endpoints, and SQL MI Subnet Security), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure Private Link, Virtual Network service endpoints, and SQL MI VNet security (https://learn.microsoft.com/en-us/azure/azure-sql/database/private-endpoint-overview).

- **A:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: Yes — Outbound Firewall Rules restrict outbound network connections initiated by Azure SQL Database or SQL Managed Instance solely to approved storage/Entra FQDNs, preventing unauthorized data exfiltration.
- **B:** Incorrect for this requirement. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Why the keyed choice wins: Yes — Outbound Firewall Rules restrict outbound network connections initiated by Azure SQL Database or SQL Managed Instance solely to approved storage/Entra FQDNs, preventing unauthorized data exfiltration.
- **C:** Correct. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. In this scenario: Yes — Outbound Firewall Rules restrict outbound network connections initiated by Azure SQL Database or SQL Managed Instance solely to approved storage/Entra FQDNs, preventing unauthorized data exfiltration.
- **D:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: Yes — Outbound Firewall Rules restrict outbound network connections initiated by Azure SQL Database or SQL Managed Instance solely to approved storage/Entra FQDNs, preventing unauthorized data exfiltration.

### Question 29 — D

Answer: SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage. T-SQL `CREATE SERVER AUDIT` on SQL Server and SQL Managed Instance supports a `WHERE` predicate clause (e.g., `WHERE server_principal_name <> N'svc_settlement'`) to filter audited events at the source. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. Local study-map skill 2.11 (Apply SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) and Server/Database Auditing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Data Discovery and Classification and Azure SQL Auditing (https://learn.microsoft.com/en-us/azure/azure-sql/database/auditing-overview).

- **A:** Incorrect for this requirement. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. Why the keyed choice wins: T-SQL `CREATE SERVER AUDIT` on SQL Server and SQL Managed Instance supports a `WHERE` predicate clause (e.g., `WHERE server_principal_name <> N'svc_settlement'`) to filter audited events at the source.
- **B:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: T-SQL `CREATE SERVER AUDIT` on SQL Server and SQL Managed Instance supports a `WHERE` predicate clause (e.g., `WHERE server_principal_name <> N'svc_settlement'`) to filter audited events at the source.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: T-SQL `CREATE SERVER AUDIT` on SQL Server and SQL Managed Instance supports a `WHERE` predicate clause (e.g., `WHERE server_principal_name <> N'svc_settlement'`) to filter audited events at the source.
- **D:** Correct. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. In this scenario: T-SQL `CREATE SERVER AUDIT` on SQL Server and SQL Managed Instance supports a `WHERE` predicate clause (e.g., `WHERE server_principal_name <> N'svc_settlement'`) to filter audited events at the source.

### Question 30 — A

Answer: SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage. Real-time SIEM ingestion (such as Microsoft Sentinel or Splunk) consuming sub-second security audit streams for automated threat correlation and anomalous-query alerting. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. Local study-map skill 2.11 (Apply SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) and Server/Database Auditing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Data Discovery and Classification and Azure SQL Auditing (https://learn.microsoft.com/en-us/azure/azure-sql/database/auditing-overview).

- **A:** Correct. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. In this scenario: Real-time SIEM ingestion (such as Microsoft Sentinel or Splunk) consuming sub-second security audit streams for automated threat correlation and anomalous-query alerting.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Real-time SIEM ingestion (such as Microsoft Sentinel or Splunk) consuming sub-second security audit streams for automated threat correlation and anomalous-query alerting.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Real-time SIEM ingestion (such as Microsoft Sentinel or Splunk) consuming sub-second security audit streams for automated threat correlation and anomalous-query alerting.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Real-time SIEM ingestion (such as Microsoft Sentinel or Splunk) consuming sub-second security audit streams for automated threat correlation and anomalous-query alerting.

### Question 31 — A

Answer: Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history. Run `EXEC sys.sp_cdc_enable_db;` and `EXEC sys.sp_cdc_enable_table ...;` — in Azure SQL Database (`S3+` and `vCore` tiers), a built-in background CDC scheduler automatically replaces SQL Server Agent capture/cleanup jobs. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. Local study-map skill 2.12 (Implement Change Tracking (`CHANGETABLE`) vs Change Data Capture (`CDC`) for Downstream Data Changes), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Track data changes with Change Tracking (CT) and Change Data Capture (CDC) (https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/track-data-changes-sql-server).

- **A:** Correct. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. In this scenario: Run `EXEC sys.sp_cdc_enable_db;` and `EXEC sys.sp_cdc_enable_table ...;` — in Azure SQL Database (`S3+` and `vCore` tiers), a built-in background CDC scheduler automatically replaces SQL Server Agent capture/cleanup jobs.
- **B:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Run `EXEC sys.sp_cdc_enable_db;` and `EXEC sys.sp_cdc_enable_table ...;` — in Azure SQL Database (`S3+` and `vCore` tiers), a built-in background CDC scheduler automatically replaces SQL Server Agent capture/cleanup jobs.
- **C:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Run `EXEC sys.sp_cdc_enable_db;` and `EXEC sys.sp_cdc_enable_table ...;` — in Azure SQL Database (`S3+` and `vCore` tiers), a built-in background CDC scheduler automatically replaces SQL Server Agent capture/cleanup jobs.
- **D:** Incorrect for this requirement. CDC requires `S3+` or `vCore` tiers in Azure SQL Database, and Change Tracking stores only net version numbers/PKs—never intermediate before/after column values. Why the keyed choice wins: Run `EXEC sys.sp_cdc_enable_db;` and `EXEC sys.sp_cdc_enable_table ...;` — in Azure SQL Database (`S3+` and `vCore` tiers), a built-in background CDC scheduler automatically replaces SQL Server Agent capture/cleanup jobs.

### Question 32 — C

Answer: Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas. Granular column-/table-/schema-level `GRANT UNMASK ON OBJECT::dbo.WireTransfers(FeeAmount)` reveals cleartext only for `FeeAmount` without unmasking every masked column across the entire database. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Local study-map skill 2.13 (Implement Dynamic Data Masking (`default`, `email`, `partial`, `random`) and Scoped `UNMASK` Permissions), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Dynamic Data Masking (DDM) in Azure SQL Database, SQL Managed Instance, and SQL Server (https://learn.microsoft.com/en-us/azure/azure-sql/database/dynamic-data-masking-overview).

- **A:** Incorrect for this requirement. RLS transparently filters `SELECT`/`UPDATE`/`DELETE` rows via `FILTER PREDICATE` and blocks unauthorized cross-tenant `INSERT`/`UPDATE` writes via `BLOCK PREDICATE` inside the engine. Why the keyed choice wins: Granular column-/table-/schema-level `GRANT UNMASK ON OBJECT::dbo.WireTransfers(FeeAmount)` reveals cleartext only for `FeeAmount` without unmasking every masked column across the entire database.
- **B:** Incorrect for this requirement. BYOK TDE wraps the symmetric Database Encryption Key (`DEK`) with an asymmetric RSA key in Key Vault or Managed HSM so security admins control key rotation and instant revocation. Why the keyed choice wins: Granular column-/table-/schema-level `GRANT UNMASK ON OBJECT::dbo.WireTransfers(FeeAmount)` reveals cleartext only for `FeeAmount` without unmasking every masked column across the entire database.
- **C:** Correct. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. In this scenario: Granular column-/table-/schema-level `GRANT UNMASK ON OBJECT::dbo.WireTransfers(FeeAmount)` reveals cleartext only for `FeeAmount` without unmasking every masked column across the entire database.
- **D:** Incorrect for this requirement. Secure enclaves delegate column decryption into an isolated memory region inside SQL, unlocking `LIKE`, `<`, `>`, `ORDER BY`, and fast in-place initial encryption without exposing plaintext to DBAs. Why the keyed choice wins: Granular column-/table-/schema-level `GRANT UNMASK ON OBJECT::dbo.WireTransfers(FeeAmount)` reveals cleartext only for `FeeAmount` without unmasking every masked column across the entire database.

### Question 33 — B, E, F

Answers: Create an inline table-valued function `WITH SCHEMABINDING` evaluating `SESSION_CONTEXT()` or `DATABASE_PRINCIPAL_ID()`; Add a `FILTER PREDICATE` in `CREATE SECURITY POLICY` to hide non-matching rows silently from `SELECT`, `UPDATE`, and `DELETE`; Add `AFTER INSERT` and `AFTER UPDATE` / `BEFORE UPDATE` `BLOCK PREDICATE` clauses in `CREATE SECURITY POLICY` (`STATE = ON`). Define a `SCHEMABINDING` inline TVF predicate and bind both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`. Local study-map skill 2.14 (Implement Cryptographic Ledger in Azure SQL (`Azure Confidential Ledger`) and Row-Level Security (`FILTER`/`BLOCK`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Ledger cryptographic tamper-evidence and Row-Level Security (RLS) in Azure SQL (https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-overview).

- **A:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Define a `SCHEMABINDING` inline TVF predicate and bind both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **B:** Correct. `FILTER PREDICATE` injects the security TVF into read, update, and delete operators transparently without changing application `SELECT` statements. In this scenario: Define a `SCHEMABINDING` inline TVF predicate and bind both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **C:** Incorrect for this requirement. Append-only Ledger tables strictly block `UPDATE`, `DELETE`, and `TRUNCATE` statements in the SQL engine so cryptographic audit trails cannot be altered. Why the keyed choice wins: Define a `SCHEMABINDING` inline TVF predicate and bind both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Define a `SCHEMABINDING` inline TVF predicate and bind both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **E:** Correct. RLS predicate functions must be inline TVFs bound with `SCHEMABINDING` so underlying columns cannot be altered silently and query plans inline cleanly. In this scenario: Define a `SCHEMABINDING` inline TVF predicate and bind both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **F:** Correct. `BLOCK PREDICATE` raises an error if a shared application login attempts to insert or update a row carrying another tenant's identifier. In this scenario: Define a `SCHEMABINDING` inline TVF predicate and bind both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.

### Question 34 — D

Answer: Create dedicated `Security` schema → Create `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT(N'TenantId')` → Create `SECURITY POLICY` with `FILTER` & `BLOCK` predicates (`STATE = ON`) → Set read-only `sp_set_session_context` on connect. Create a dedicated `Security` schema, build a `SCHEMABINDING` inline TVF checking `SESSION_CONTEXT(N'FundId')`, create an active `SECURITY POLICY` with `FILTER` + `BLOCK` predicates, and set read-only `sp_set_session_context` on connect. Best-practice multi-tenant RLS isolates objects in a dedicated schema, uses a schema-bound inline TVF predicate over read-only `SESSION_CONTEXT`, and enforces both `FILTER` and `BLOCK` predicates. Local study-map skill 2.14 (Implement Cryptographic Ledger in Azure SQL (`Azure Confidential Ledger`) and Row-Level Security (`FILTER`/`BLOCK`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Ledger cryptographic tamper-evidence and Row-Level Security (RLS) in Azure SQL (https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-overview).

- **A:** Incorrect for this requirement. Incorrect workflow: RLS requires an existing `SCHEMABINDING` inline TVF before creating the security policy, and granting `ALTER ANY SECURITY POLICY` lets tenants bypass isolation. Why the keyed choice wins: Create a dedicated `Security` schema, build a `SCHEMABINDING` inline TVF checking `SESSION_CONTEXT(N'FundId')`, create an active `SECURITY POLICY` with `FILTER` + `BLOCK` predicates, and set read-only `sp_set_session_context` on connect.
- **B:** Incorrect for this requirement. Incorrect workflow: RLS predicates must be schema-bound inline TVFs attached to a `SECURITY POLICY`, and `@read_only = 1` prevents SQL injection from changing `TenantId` mid-session. Why the keyed choice wins: Create a dedicated `Security` schema, build a `SCHEMABINDING` inline TVF checking `SESSION_CONTEXT(N'FundId')`, create an active `SECURITY POLICY` with `FILTER` + `BLOCK` predicates, and set read-only `sp_set_session_context` on connect.
- **C:** Incorrect for this requirement. Incorrect workflow: Dynamic Data Masking obfuscates column output in result sets and never filters rows or blocks cross-tenant writes. Why the keyed choice wins: Create a dedicated `Security` schema, build a `SCHEMABINDING` inline TVF checking `SESSION_CONTEXT(N'FundId')`, create an active `SECURITY POLICY` with `FILTER` + `BLOCK` predicates, and set read-only `sp_set_session_context` on connect.
- **D:** Correct. Best-practice multi-tenant RLS isolates objects in a dedicated schema, uses a schema-bound inline TVF predicate over read-only `SESSION_CONTEXT`, and enforces both `FILTER` and `BLOCK` predicates. In this scenario: Create a dedicated `Security` schema, build a `SCHEMABINDING` inline TVF checking `SESSION_CONTEXT(N'FundId')`, create an active `SECURITY POLICY` with `FILTER` + `BLOCK` predicates, and set read-only `sp_set_session_context` on connect.

### Question 35 — C

Answer: Azure Monitor metrics paired with `sys.dm_db_resource_stats` (single DB) or `sys.server_resource_stats` (SQL MI) for 15-second CPU, data I/O, log write, and memory baselines. `sys.elastic_pool_resource_stats` in `master` retains 14 days of 15-second utilization averages across the entire Elastic Pool, complementing per-database `sys.dm_db_resource_stats`. `sys.dm_db_resource_stats` retains 14 days of 15-second resource averages (`avg_cpu_percent`, `avg_data_io_percent`, `avg_log_write_percent`) to compare current peaks against normal baselines. Local study-map skill 3.1 (Establish Performance Baselines and Interpret CPU, Memory, Data I/O, Log Write, and `tempdb` Metrics), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL resource utilization and establish performance baselines (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-sql-database-azure-monitor).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `sys.elastic_pool_resource_stats` in `master` retains 14 days of 15-second utilization averages across the entire Elastic Pool, complementing per-database `sys.dm_db_resource_stats`.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: `sys.elastic_pool_resource_stats` in `master` retains 14 days of 15-second utilization averages across the entire Elastic Pool, complementing per-database `sys.dm_db_resource_stats`.
- **C:** Correct. `sys.dm_db_resource_stats` retains 14 days of 15-second resource averages (`avg_cpu_percent`, `avg_data_io_percent`, `avg_log_write_percent`) to compare current peaks against normal baselines. In this scenario: `sys.elastic_pool_resource_stats` in `master` retains 14 days of 15-second utilization averages across the entire Elastic Pool, complementing per-database `sys.dm_db_resource_stats`.
- **D:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: `sys.elastic_pool_resource_stats` in `master` retains 14 days of 15-second utilization averages across the entire Elastic Pool, complementing per-database `sys.dm_db_resource_stats`.

### Question 36 — C

Answer: Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`. High `SOS_SCHEDULER_YIELD` means runnable threads are exhausting their 4 ms CPU quantum and yielding voluntarily to other CPU-bound threads—indicating pure CPU pressure or heavy in-memory index/hash scans. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. Local study-map skill 3.1 (Establish Performance Baselines and Interpret CPU, Memory, Data I/O, Log Write, and `tempdb` Metrics), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL resource utilization and establish performance baselines (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-sql-database-azure-monitor).

- **A:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: High `SOS_SCHEDULER_YIELD` means runnable threads are exhausting their 4 ms CPU quantum and yielding voluntarily to other CPU-bound threads—indicating pure CPU pressure or heavy in-memory index/hash scans.
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: High `SOS_SCHEDULER_YIELD` means runnable threads are exhausting their 4 ms CPU quantum and yielding voluntarily to other CPU-bound threads—indicating pure CPU pressure or heavy in-memory index/hash scans.
- **C:** Correct. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. In this scenario: High `SOS_SCHEDULER_YIELD` means runnable threads are exhausting their 4 ms CPU quantum and yielding voluntarily to other CPU-bound threads—indicating pure CPU pressure or heavy in-memory index/hash scans.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: High `SOS_SCHEDULER_YIELD` means runnable threads are exhausting their 4 ms CPU quantum and yielding voluntarily to other CPU-bound threads—indicating pure CPU pressure or heavy in-memory index/hash scans.

### Question 37 — D

Answer: Azure Monitor Diagnostic Settings streaming `SQLInsights`, `QueryStoreRuntimeStatistics`, `Errors`, and `Blocks` to a Log Analytics workspace (`KQL`). Diagnostic Settings stream Azure SQL telemetry to `AzureDiagnostics` (or dedicated resource-specific tables when configured) inside the target Log Analytics workspace for KQL analysis and alerting. Diagnostic Settings export telemetry across hundreds of databases into Log Analytics so DBAs can correlate `SQLInsights`, wait stats, deadlocks, and timeouts via KQL queries and alerts. Local study-map skill 3.2 (Configure Azure Monitor Diagnostic Settings (`SQLInsights`, `AzureDiagnostics` KQL) and Resource Monitoring), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure Monitor diagnostic settings, SQLInsights logs, and metric alerts (https://learn.microsoft.com/en-us/azure/azure-sql/database/metrics-diagnostic-telemetry-logging-streaming-export-configure).

- **A:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Diagnostic Settings stream Azure SQL telemetry to `AzureDiagnostics` (or dedicated resource-specific tables when configured) inside the target Log Analytics workspace for KQL analysis and alerting.
- **B:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Diagnostic Settings stream Azure SQL telemetry to `AzureDiagnostics` (or dedicated resource-specific tables when configured) inside the target Log Analytics workspace for KQL analysis and alerting.
- **C:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Diagnostic Settings stream Azure SQL telemetry to `AzureDiagnostics` (or dedicated resource-specific tables when configured) inside the target Log Analytics workspace for KQL analysis and alerting.
- **D:** Correct. Diagnostic Settings export telemetry across hundreds of databases into Log Analytics so DBAs can correlate `SQLInsights`, wait stats, deadlocks, and timeouts via KQL queries and alerts. In this scenario: Diagnostic Settings stream Azure SQL telemetry to `AzureDiagnostics` (or dedicated resource-specific tables when configured) inside the target Log Analytics workspace for KQL analysis and alerting.

### Question 38 — C

Answer: Provision Azure Data Explorer or Fabric Eventhouse store → Create database watcher with Managed Identity → Add SQL targets & grant `VIEW SERVER PERFORMANCE STATE` + ingest roles → Start watcher & open portal dashboards. Provision the Azure Data Explorer / Fabric Eventhouse store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets + store ingest roles, and start the watcher. Database watcher streams SQL telemetry into an Azure Data Explorer or Fabric Eventhouse/KQL store using Managed Identity granted least-privilege `VIEW SERVER PERFORMANCE STATE` on SQL targets. Local study-map skill 3.3 (Monitor Workloads Using Database Watcher (ADX / Fabric Eventhouse) and Plan Fabric Database Hub Transition), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL workloads with database watcher and Database Hub in Microsoft Fabric (https://learn.microsoft.com/en-us/azure/azure-sql/database-watcher-overview).

- **A:** Incorrect for this requirement. Incorrect workflow: database watcher monitors Azure SQL Database, Elastic Pools, and SQL Managed Instance and stores telemetry in Azure Data Explorer or Fabric KQL databases. Why the keyed choice wins: Provision the Azure Data Explorer / Fabric Eventhouse store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets + store ingest roles, and start the watcher.
- **B:** Incorrect for this requirement. Incorrect workflow: Azure SQL Database PaaS exposes no underlying OS for agents, `sp_trace_create` is deprecated, and database watcher is agentless. Why the keyed choice wins: Provision the Azure Data Explorer / Fabric Eventhouse store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets + store ingest roles, and start the watcher.
- **C:** Correct. Database watcher streams SQL telemetry into an Azure Data Explorer or Fabric Eventhouse/KQL store using Managed Identity granted least-privilege `VIEW SERVER PERFORMANCE STATE` on SQL targets. In this scenario: Provision the Azure Data Explorer / Fabric Eventhouse store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets + store ingest roles, and start the watcher.
- **D:** Incorrect for this requirement. Incorrect workflow: watcher requires an Azure Data Explorer or Fabric Real-Time Analytics store and SQL targets configured first, and uses least-privilege Managed Identity rather than `sa` or Profiler. Why the keyed choice wins: Provision the Azure Data Explorer / Fabric Eventhouse store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets + store ingest roles, and start the watcher.

### Question 39 — B, D

Answers: Grant the database watcher Managed Identity `VIEW SERVER PERFORMANCE STATE` (or `VIEW DATABASE PERFORMANCE STATE`) on SQL targets; Grant the database watcher Managed Identity database `Admin` / ingest permissions on the Azure Data Explorer or Fabric Eventhouse store. Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on SQL targets and database `Admin` / ingestion permissions on the Fabric Eventhouse / ADX database. Local study-map skill 3.3 (Monitor Workloads Using Database Watcher (ADX / Fabric Eventhouse) and Plan Fabric Database Hub Transition), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL workloads with database watcher and Database Hub in Microsoft Fabric (https://learn.microsoft.com/en-us/azure/azure-sql/database-watcher-overview).

- **A:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on SQL targets and database `Admin` / ingestion permissions on the Fabric Eventhouse / ADX database.
- **B:** Correct. Database watcher creates tables, retention policies, and ingestion mappings inside the target Azure Data Explorer or Fabric Real-Time Analytics KQL database. In this scenario: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on SQL targets and database `Admin` / ingestion permissions on the Fabric Eventhouse / ADX database.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on SQL targets and database `Admin` / ingestion permissions on the Fabric Eventhouse / ADX database.
- **D:** Correct. Database watcher collects DMVs and system catalogs using least-privilege performance-state permissions rather than `sysadmin` or data-read rights. In this scenario: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on SQL targets and database `Admin` / ingestion permissions on the Fabric Eventhouse / ADX database.
- **E:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on SQL targets and database `Admin` / ingestion permissions on the Fabric Eventhouse / ADX database.

### Question 40 — A, D

Answers: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE` with `rwl` permissions) for the Azure Blob container; Define `CREATE EVENT SESSION ... ON DATABASE ADD TARGET package0.event_file(SET filename = N'https://...xel')` and start the session. Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS) for the Blob Storage container, and create an `ON DATABASE` Extended Events session targeting `package0.event_file`. Local study-map skill 3.4 (Monitor Workloads Using Extended Events (`ON DATABASE` vs `ON SERVER` & Persistent Blob `event_file` Targets)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Extended Events in Azure SQL Database and Azure SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/xevent-db-diff-from-svr).

- **A:** Correct. Azure SQL Database scopes Extended Event sessions `ON DATABASE` and streams persistent `.xel` ring-rotated files to the Blob container URL. In this scenario: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS) for the Blob Storage container, and create an `ON DATABASE` Extended Events session targeting `package0.event_file`.
- **B:** Incorrect for this requirement. Azure SQL requires both Soft Delete and Purge Protection on Key Vault so accidental or malicious key deletion can never permanently brick encrypted databases. Why the keyed choice wins: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS) for the Blob Storage container, and create an `ON DATABASE` Extended Events session targeting `package0.event_file`.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS) for the Blob Storage container, and create an `ON DATABASE` Extended Events session targeting `package0.event_file`.
- **D:** Correct. Extended Events in Azure SQL Database requires a `DATABASE SCOPED CREDENTIAL` with Read, Write, and List rights on the target Blob Storage container. In this scenario: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS) for the Blob Storage container, and create an `ON DATABASE` Extended Events session targeting `package0.event_file`.
- **E:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS) for the Blob Storage container, and create an `ON DATABASE` Extended Events session targeting `package0.event_file`.

### Question 41 — A

Answer: Extended Events (`CREATE EVENT SESSION ... ON DATABASE` in SQL DB or `ON SERVER` in SQL MI/VMs) writing to an `event_file` target in Azure Blob Storage. `sys.fn_xe_file_target_read_file` streams and parses `.xel` files directly from Azure Blob Storage (authenticated via `DATABASE SCOPED CREDENTIAL`) into T-SQL result sets. Unlike ephemeral in-memory `ring_buffer` targets, the `event_file` target persists `.xel` trace files durably in Azure Blob Storage using a database-scoped credential (Managed Identity or SAS). Local study-map skill 3.4 (Monitor Workloads Using Extended Events (`ON DATABASE` vs `ON SERVER` & Persistent Blob `event_file` Targets)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Extended Events in Azure SQL Database and Azure SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/xevent-db-diff-from-svr).

- **A:** Correct. Unlike ephemeral in-memory `ring_buffer` targets, the `event_file` target persists `.xel` trace files durably in Azure Blob Storage using a database-scoped credential (Managed Identity or SAS). In this scenario: `sys.fn_xe_file_target_read_file` streams and parses `.xel` files directly from Azure Blob Storage (authenticated via `DATABASE SCOPED CREDENTIAL`) into T-SQL result sets.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: `sys.fn_xe_file_target_read_file` streams and parses `.xel` files directly from Azure Blob Storage (authenticated via `DATABASE SCOPED CREDENTIAL`) into T-SQL result sets.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: `sys.fn_xe_file_target_read_file` streams and parses `.xel` files directly from Azure Blob Storage (authenticated via `DATABASE SCOPED CREDENTIAL`) into T-SQL result sets.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `sys.fn_xe_file_target_read_file` streams and parses `.xel` files directly from Azure Blob Storage (authenticated via `DATABASE SCOPED CREDENTIAL`) into T-SQL result sets.

### Question 42 — A, B

Answers: Execute `sys.sp_query_store_force_plan @query_id, @plan_id` to pin the historical low-latency execution plan immediately; Execute `sys.sp_query_store_set_hints @query_id, N'OPTION (RECOMPILE)'` (or `MAXDOP` / memory grant hints) without redeploying code. Use `sys.sp_query_store_force_plan` to lock in a known-good `plan_id` or `sys.sp_query_store_set_hints` to apply `OPTION (RECOMPILE)` / `OPTIMIZE FOR` hints without altering vendor T-SQL. Local study-map skill 3.5 (Configure and Monitor Query Store, Force Regressed Plans (`sp_query_store_force_plan`), and Set Query Store Hints), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance by using the Query Store, plan forcing, and Query Store hints (https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store).

- **A:** Correct. `sp_query_store_force_plan` instructs the optimizer to compile plans matching the forced `plan_id` shape without modifying application T-SQL. In this scenario: Use `sys.sp_query_store_force_plan` to lock in a known-good `plan_id` or `sys.sp_query_store_set_hints` to apply `OPTION (RECOMPILE)` / `OPTIMIZE FOR` hints without altering vendor T-SQL.
- **B:** Correct. Query Store hints attach `OPTION (...)` query hints directly to a `query_id` in Azure SQL DB, SQL MI, and SQL Server 2022+ when app code cannot be edited. In this scenario: Use `sys.sp_query_store_force_plan` to lock in a known-good `plan_id` or `sys.sp_query_store_set_hints` to apply `OPTION (RECOMPILE)` / `OPTIMIZE FOR` hints without altering vendor T-SQL.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Use `sys.sp_query_store_force_plan` to lock in a known-good `plan_id` or `sys.sp_query_store_set_hints` to apply `OPTION (RECOMPILE)` / `OPTIMIZE FOR` hints without altering vendor T-SQL.
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Use `sys.sp_query_store_force_plan` to lock in a known-good `plan_id` or `sys.sp_query_store_set_hints` to apply `OPTION (RECOMPILE)` / `OPTIMIZE FOR` hints without altering vendor T-SQL.
- **E:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Use `sys.sp_query_store_force_plan` to lock in a known-good `plan_id` or `sys.sp_query_store_set_hints` to apply `OPTION (RECOMPILE)` / `OPTIMIZE FOR` hints without altering vendor T-SQL.

### Question 43 — D

Answer: Confirm Query Store is `READ_WRITE` with wait capture → Compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`) → Force prior plan via `sp_query_store_force_plan` → Monitor `force_failure_count` & latency. Confirm Query Store is `READ_WRITE` with wait capture, compare historical plan metrics in Regressed Queries (`sys.query_store_runtime_stats`), force the healthy `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`. Resolving a parameter-sensitive plan regression uses Query Store runtime/wait history to identify the prior known-good `plan_id`, forces it immediately without code changes, and verifies forcing health. Local study-map skill 3.5 (Configure and Monitor Query Store, Force Regressed Plans (`sp_query_store_force_plan`), and Set Query Store Hints), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance by using the Query Store, plan forcing, and Query Store hints (https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store).

- **A:** Incorrect for this requirement. Incorrect workflow: purging Query Store erases the historical baseline and prior good plan needed to diagnose and force the healthy execution plan. Why the keyed choice wins: Confirm Query Store is `READ_WRITE` with wait capture, compare historical plan metrics in Regressed Queries (`sys.query_store_runtime_stats`), force the healthy `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`.
- **B:** Incorrect for this requirement. Incorrect workflow: system catalog tables cannot be updated directly and flushing the plan cache every minute spikes CPU compilations across the entire workload. Why the keyed choice wins: Confirm Query Store is `READ_WRITE` with wait capture, compare historical plan metrics in Regressed Queries (`sys.query_store_runtime_stats`), force the healthy `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`.
- **C:** Incorrect for this requirement. Incorrect workflow: restarting SQL or running offline index rebuilds causes severe production outage and does not prevent parameter-sensitive plan regressions. Why the keyed choice wins: Confirm Query Store is `READ_WRITE` with wait capture, compare historical plan metrics in Regressed Queries (`sys.query_store_runtime_stats`), force the healthy `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`.
- **D:** Correct. Resolving a parameter-sensitive plan regression uses Query Store runtime/wait history to identify the prior known-good `plan_id`, forces it immediately without code changes, and verifies forcing health. In this scenario: Confirm Query Store is `READ_WRITE` with wait capture, compare historical plan metrics in Regressed Queries (`sys.query_store_runtime_stats`), force the healthy `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`.

### Question 44 — C

Answer: Read Committed Snapshot Isolation (`READ_COMMITTED_SNAPSHOT = ON`) combined with Optimized Locking (`TID` locking + Lock After Qualification `LAQ`). Optimized Locking (`ACCELERATED_DATABASE_RECOVERY` + `OPTIMIZED_LOCKING`) holds a single Transaction ID (`TID`) lock instead of thousands of row/page locks and evaluates predicates under Lock After Qualification (`LAQ`), eliminating memory-driven lock escalation. `RCSI` uses row versioning so readers never block writers (`LCK_M_S`), while Optimized Locking in Azure SQL DB replaces thousands of row/page locks with a single Transaction ID lock and `LAQ`. Local study-map skill 3.6 (Identify and Resolve Session Blocking (`RCSI`, `Optimized Locking` `TID`/`LAQ`) and Deadlocks (`xml_deadlock_report`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Understand and resolve Azure SQL blocking problems, deadlocks, RCSI, and Optimized Locking (https://learn.microsoft.com/en-us/azure/azure-sql/database/analyze-prevent-deadlocks).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Optimized Locking (`ACCELERATED_DATABASE_RECOVERY` + `OPTIMIZED_LOCKING`) holds a single Transaction ID (`TID`) lock instead of thousands of row/page locks and evaluates predicates under Lock After Qualification (`LAQ`), eliminating memory-driven lock escalation.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Optimized Locking (`ACCELERATED_DATABASE_RECOVERY` + `OPTIMIZED_LOCKING`) holds a single Transaction ID (`TID`) lock instead of thousands of row/page locks and evaluates predicates under Lock After Qualification (`LAQ`), eliminating memory-driven lock escalation.
- **C:** Correct. `RCSI` uses row versioning so readers never block writers (`LCK_M_S`), while Optimized Locking in Azure SQL DB replaces thousands of row/page locks with a single Transaction ID lock and `LAQ`. In this scenario: Optimized Locking (`ACCELERATED_DATABASE_RECOVERY` + `OPTIMIZED_LOCKING`) holds a single Transaction ID (`TID`) lock instead of thousands of row/page locks and evaluates predicates under Lock After Qualification (`LAQ`), eliminating memory-driven lock escalation.
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Optimized Locking (`ACCELERATED_DATABASE_RECOVERY` + `OPTIMIZED_LOCKING`) holds a single Transaction ID (`TID`) lock instead of thousands of row/page locks and evaluates predicates under Lock After Qualification (`LAQ`), eliminating memory-driven lock escalation.

### Question 45 — C

Answer: Capture `xml_deadlock_report` via Extended Events or `sys.event_log`, align table modification order across transactions, and add covering indexes. Under `NOLOCK` (`READ UNCOMMITTED`), margin queries can read uncommitted rolled-back trades, skip committed rows during B-tree page splits, or double-count moved rows—whereas `RCSI` delivers lock-free committed snapshots. Cycle deadlocks (`Error 1205`) occur when concurrent transactions lock objects in opposite order or scan wide ranges; accessing tables in identical order with narrow index seeks eliminates cycles. Local study-map skill 3.6 (Identify and Resolve Session Blocking (`RCSI`, `Optimized Locking` `TID`/`LAQ`) and Deadlocks (`xml_deadlock_report`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Understand and resolve Azure SQL blocking problems, deadlocks, RCSI, and Optimized Locking (https://learn.microsoft.com/en-us/azure/azure-sql/database/analyze-prevent-deadlocks).

- **A:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Under `NOLOCK` (`READ UNCOMMITTED`), margin queries can read uncommitted rolled-back trades, skip committed rows during B-tree page splits, or double-count moved rows—whereas `RCSI` delivers lock-free committed snapshots.
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Under `NOLOCK` (`READ UNCOMMITTED`), margin queries can read uncommitted rolled-back trades, skip committed rows during B-tree page splits, or double-count moved rows—whereas `RCSI` delivers lock-free committed snapshots.
- **C:** Correct. Cycle deadlocks (`Error 1205`) occur when concurrent transactions lock objects in opposite order or scan wide ranges; accessing tables in identical order with narrow index seeks eliminates cycles. In this scenario: Under `NOLOCK` (`READ UNCOMMITTED`), margin queries can read uncommitted rolled-back trades, skip committed rows during B-tree page splits, or double-count moved rows—whereas `RCSI` delivers lock-free committed snapshots.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Under `NOLOCK` (`READ UNCOMMITTED`), margin queries can read uncommitted rolled-back trades, skip committed rows during B-tree page splits, or double-count moved rows—whereas `RCSI` delivers lock-free committed snapshots.

### Question 46 — D

Answer: Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`. `sys.dm_db_index_operational_stats` exposes granular per-index/partition row lock waits, latch waits, lock escalations, and page split counts. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. Local study-map skill 3.7 (Identify Performance Bottlenecks Using Dynamic Management Views (`sys.dm_os_wait_stats`, `sys.dm_exec_requests`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance using Dynamic Management Views (DMVs) and wait statistics (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-with-dmvs).

- **A:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: `sys.dm_db_index_operational_stats` exposes granular per-index/partition row lock waits, latch waits, lock escalations, and page split counts.
- **B:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: `sys.dm_db_index_operational_stats` exposes granular per-index/partition row lock waits, latch waits, lock escalations, and page split counts.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `sys.dm_db_index_operational_stats` exposes granular per-index/partition row lock waits, latch waits, lock escalations, and page split counts.
- **D:** Correct. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. In this scenario: `sys.dm_db_index_operational_stats` exposes granular per-index/partition row lock waits, latch waits, lock escalations, and page split counts.

### Question 47 — B

Answer: Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`. Inspecting `log_reuse_wait_desc` in `sys.databases` (e.g., `ACTIVE_TRANSACTION`, `LOG_BACKUP`, `AVAILABILITY_REPLICA`, or `CDC`) immediately identifies what holds the active log VLF open. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. Local study-map skill 3.7 (Identify Performance Bottlenecks Using Dynamic Management Views (`sys.dm_os_wait_stats`, `sys.dm_exec_requests`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance using Dynamic Management Views (DMVs) and wait statistics (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-with-dmvs).

- **A:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Inspecting `log_reuse_wait_desc` in `sys.databases` (e.g., `ACTIVE_TRANSACTION`, `LOG_BACKUP`, `AVAILABILITY_REPLICA`, or `CDC`) immediately identifies what holds the active log VLF open.
- **B:** Correct. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. In this scenario: Inspecting `log_reuse_wait_desc` in `sys.databases` (e.g., `ACTIVE_TRANSACTION`, `LOG_BACKUP`, `AVAILABILITY_REPLICA`, or `CDC`) immediately identifies what holds the active log VLF open.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Inspecting `log_reuse_wait_desc` in `sys.databases` (e.g., `ACTIVE_TRANSACTION`, `LOG_BACKUP`, `AVAILABILITY_REPLICA`, or `CDC`) immediately identifies what holds the active log VLF open.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Inspecting `log_reuse_wait_desc` in `sys.databases` (e.g., `ACTIVE_TRANSACTION`, `LOG_BACKUP`, `AVAILABILITY_REPLICA`, or `CDC`) immediately identifies what holds the active log VLF open.

### Question 48 — C

Answer: Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions. Rewriting `LEFT(CardToken, 6) = '411122'` as `CardToken LIKE '411122%'` removes the function wrapper from the indexed column so SQL seeks directly into the `411122` prefix range. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. Local study-map skill 3.8 (Design Covering/Filtered/Columnstore Indexes and Rewrite Non-SARGable or Implicit-Conversion T-SQL Constructs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server and Azure SQL index design guide and SARGable T-SQL tuning (https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide).

- **A:** Incorrect for this requirement. Row-by-row cursors and multi-statement TVFs under legacy compatibility levels execute thousands of iterative context switches and 1-row cardinality guesses. Why the keyed choice wins: Rewriting `LEFT(CardToken, 6) = '411122'` as `CardToken LIKE '411122%'` removes the function wrapper from the indexed column so SQL seeks directly into the `411122` prefix range.
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Rewriting `LEFT(CardToken, 6) = '411122'` as `CardToken LIKE '411122%'` removes the function wrapper from the indexed column so SQL seeks directly into the `411122` prefix range.
- **C:** Correct. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. In this scenario: Rewriting `LEFT(CardToken, 6) = '411122'` as `CardToken LIKE '411122%'` removes the function wrapper from the indexed column so SQL seeks directly into the `411122` prefix range.
- **D:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Rewriting `LEFT(CardToken, 6) = '411122'` as `CardToken LIKE '411122%'` removes the function wrapper from the indexed column so SQL seeks directly into the `411122` prefix range.

### Question 49 — C

Answer: Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions. Creating an updatable Nonclustered Columnstore Index (`CREATE NONCLUSTERED COLUMNSTORE INDEX`) with a filtered compression delay (`COMPRESSION_DELAY = 10 MINUTES`) accelerates real-time analytical scans on hot OLTP tables. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. Local study-map skill 3.8 (Design Covering/Filtered/Columnstore Indexes and Rewrite Non-SARGable or Implicit-Conversion T-SQL Constructs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server and Azure SQL index design guide and SARGable T-SQL tuning (https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide).

- **A:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Creating an updatable Nonclustered Columnstore Index (`CREATE NONCLUSTERED COLUMNSTORE INDEX`) with a filtered compression delay (`COMPRESSION_DELAY = 10 MINUTES`) accelerates real-time analytical scans on hot OLTP tables.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Creating an updatable Nonclustered Columnstore Index (`CREATE NONCLUSTERED COLUMNSTORE INDEX`) with a filtered compression delay (`COMPRESSION_DELAY = 10 MINUTES`) accelerates real-time analytical scans on hot OLTP tables.
- **C:** Correct. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. In this scenario: Creating an updatable Nonclustered Columnstore Index (`CREATE NONCLUSTERED COLUMNSTORE INDEX`) with a filtered compression delay (`COMPRESSION_DELAY = 10 MINUTES`) accelerates real-time analytical scans on hot OLTP tables.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Creating an updatable Nonclustered Columnstore Index (`CREATE NONCLUSTERED COLUMNSTORE INDEX`) with a filtered compression delay (`COMPRESSION_DELAY = 10 MINUTES`) accelerates real-time analytical scans on hot OLTP tables.

### Question 50 — A

Answer: Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`). The query selects or filters non-key columns absent from `IX_Trades_AccountId`, forcing SQL to hop back to the clustered index 420,000 times (eliminated by adding `INCLUDE` columns or switching to a scan/hint). Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. Local study-map skill 3.9 (Analyze Execution Plans (`Key Lookup`, `TempDB` Spills, Row Skew) and Monitor via SQL Intelligent Insights), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Execution plans and SQL Intelligent Insights automated performance diagnostics (https://learn.microsoft.com/en-us/azure/azure-sql/database/intelligent-insights-overview).

- **A:** Correct. Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. In this scenario: The query selects or filters non-key columns absent from `IX_Trades_AccountId`, forcing SQL to hop back to the clustered index 420,000 times (eliminated by adding `INCLUDE` columns or switching to a scan/hint).
- **B:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: The query selects or filters non-key columns absent from `IX_Trades_AccountId`, forcing SQL to hop back to the clustered index 420,000 times (eliminated by adding `INCLUDE` columns or switching to a scan/hint).
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: The query selects or filters non-key columns absent from `IX_Trades_AccountId`, forcing SQL to hop back to the clustered index 420,000 times (eliminated by adding `INCLUDE` columns or switching to a scan/hint).
- **D:** Incorrect for this requirement. BYOK TDE wraps the symmetric Database Encryption Key (`DEK`) with an asymmetric RSA key in Key Vault or Managed HSM so security admins control key rotation and instant revocation. Why the keyed choice wins: The query selects or filters non-key columns absent from `IX_Trades_AccountId`, forcing SQL to hop back to the clustered index 420,000 times (eliminated by adding `INCLUDE` columns or switching to a scan/hint).

### Question 51 — C, D, F

Answers: Run `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON, MAX_DURATION = 90 MINUTES)` for heavily fragmented (`>30%`) indexes; Enable `AUTO_UPDATE_STATISTICS_ASYNC = ON` and schedule targeted `UPDATE STATISTICS` jobs so user queries do not stall waiting on sampling; Run `DBCC CHECKDB WITH PHYSICAL_ONLY` during off-peak windows or offload full `DBCC CHECKDB` onto a restored backup replica. Use `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON)`, enable `AUTO_UPDATE_STATISTICS_ASYNC = ON`, and run `DBCC CHECKDB WITH PHYSICAL_ONLY`. Local study-map skill 3.10 (Implement Fragmentation-Aware Index Rebuilds (`ONLINE`, `RESUMABLE`), Async Statistics, and `DBCC CHECKDB`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Optimize index maintenance, statistics updates, and DBCC CHECKDB integrity checks (https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Use `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON)`, enable `AUTO_UPDATE_STATISTICS_ASYNC = ON`, and run `DBCC CHECKDB WITH PHYSICAL_ONLY`.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Use `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON)`, enable `AUTO_UPDATE_STATISTICS_ASYNC = ON`, and run `DBCC CHECKDB WITH PHYSICAL_ONLY`.
- **C:** Correct. `PHYSICAL_ONLY` checks page checksums, torn pages, and allocation structures at a fraction of full logical `CHECKDB` CPU/memory cost. In this scenario: Use `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON)`, enable `AUTO_UPDATE_STATISTICS_ASYNC = ON`, and run `DBCC CHECKDB WITH PHYSICAL_ONLY`.
- **D:** Correct. Resumable online index rebuilds persist progress in place, bound transaction log growth, and automatically pause at `MAX_DURATION` so later windows can `RESUME`. In this scenario: Use `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON)`, enable `AUTO_UPDATE_STATISTICS_ASYNC = ON`, and run `DBCC CHECKDB WITH PHYSICAL_ONLY`.
- **E:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Use `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON)`, enable `AUTO_UPDATE_STATISTICS_ASYNC = ON`, and run `DBCC CHECKDB WITH PHYSICAL_ONLY`.
- **F:** Correct. Asynchronous statistics updates let incoming OLTP queries execute immediately with existing stats while a background thread refreshes stale histograms. In this scenario: Use `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON)`, enable `AUTO_UPDATE_STATISTICS_ASYNC = ON`, and run `DBCC CHECKDB WITH PHYSICAL_ONLY`.

### Question 52 — B

Answer: Fragmentation-aware index maintenance (`REORGANIZE` 5–30%, `REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` >30%), `UPDATE STATISTICS`, and `DBCC CHECKDB WITH PHYSICAL_ONLY`. Shrinking moves pages from the end of files into random front gaps, shattering index physical order (`>90%` fragmentation), generating massive transaction log volume, and causing immediate autogrowth stalls the next day. `RESUMABLE = ON` lets large online index rebuilds pause and resume across maintenance windows; `AUTO_UPDATE_STATISTICS_ASYNC` avoids compile stalls; `PHYSICAL_ONLY` reduces `CHECKDB` I/O overhead. Local study-map skill 3.10 (Implement Fragmentation-Aware Index Rebuilds (`ONLINE`, `RESUMABLE`), Async Statistics, and `DBCC CHECKDB`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Optimize index maintenance, statistics updates, and DBCC CHECKDB integrity checks (https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Shrinking moves pages from the end of files into random front gaps, shattering index physical order (`>90%` fragmentation), generating massive transaction log volume, and causing immediate autogrowth stalls the next day.
- **B:** Correct. `RESUMABLE = ON` lets large online index rebuilds pause and resume across maintenance windows; `AUTO_UPDATE_STATISTICS_ASYNC` avoids compile stalls; `PHYSICAL_ONLY` reduces `CHECKDB` I/O overhead. In this scenario: Shrinking moves pages from the end of files into random front gaps, shattering index physical order (`>90%` fragmentation), generating massive transaction log volume, and causing immediate autogrowth stalls the next day.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Shrinking moves pages from the end of files into random front gaps, shattering index physical order (`>90%` fragmentation), generating massive transaction log volume, and causing immediate autogrowth stalls the next day.
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Shrinking moves pages from the end of files into random front gaps, shattering index physical order (`>90%` fragmentation), generating massive transaction log volume, and causing immediate autogrowth stalls the next day.

### Question 53 — A

Answer: Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`). By default (`INHERIT`), new Azure SQL Databases inherit Automatic Tuning configurations (`FORCE_LAST_GOOD_PLAN`, `CREATE_INDEX`, `DROP_INDEX`) from the parent logical SQL server (which itself can inherit Azure defaults). Automatic Tuning continuously monitors Query Store, automatically forces prior plans when regressions occur, creates validated missing nonclustered indexes, and removes unused duplicate indexes. Local study-map skill 3.11 (Configure Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN`, `CREATE_INDEX`, `DROP_INDEX`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automatic tuning in Azure SQL Database and Azure SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-overview).

- **A:** Correct. Automatic Tuning continuously monitors Query Store, automatically forces prior plans when regressions occur, creates validated missing nonclustered indexes, and removes unused duplicate indexes. In this scenario: By default (`INHERIT`), new Azure SQL Databases inherit Automatic Tuning configurations (`FORCE_LAST_GOOD_PLAN`, `CREATE_INDEX`, `DROP_INDEX`) from the parent logical SQL server (which itself can inherit Azure defaults).
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: By default (`INHERIT`), new Azure SQL Databases inherit Automatic Tuning configurations (`FORCE_LAST_GOOD_PLAN`, `CREATE_INDEX`, `DROP_INDEX`) from the parent logical SQL server (which itself can inherit Azure defaults).
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: By default (`INHERIT`), new Azure SQL Databases inherit Automatic Tuning configurations (`FORCE_LAST_GOOD_PLAN`, `CREATE_INDEX`, `DROP_INDEX`) from the parent logical SQL server (which itself can inherit Azure defaults).
- **D:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: By default (`INHERIT`), new Azure SQL Databases inherit Automatic Tuning configurations (`FORCE_LAST_GOOD_PLAN`, `CREATE_INDEX`, `DROP_INDEX`) from the parent logical SQL server (which itself can inherit Azure defaults).

### Question 54 — D

Answer: Use `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`, `OPTIMIZED_PLAN_FORCING`) per database. `PARAMETER_SNIFFING = OFF` disables parameter value sniffing at the database scope (equivalent to `TRACE FLAG 4136` / `OPTIMIZE FOR UNKNOWN`) exclusively for `SandboxSimDB`. Database-scoped configurations isolate optimizer settings (`MAXDOP`, CE version, parameter sniffing) to a single database without affecting sibling databases on SQL MI/VMs or requiring server access. Local study-map skill 3.13 (Implement `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: ALTER DATABASE SCOPED CONFIGURATION and dynamic compute/storage scaling (https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql).

- **A:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: `PARAMETER_SNIFFING = OFF` disables parameter value sniffing at the database scope (equivalent to `TRACE FLAG 4136` / `OPTIMIZE FOR UNKNOWN`) exclusively for `SandboxSimDB`.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: `PARAMETER_SNIFFING = OFF` disables parameter value sniffing at the database scope (equivalent to `TRACE FLAG 4136` / `OPTIMIZE FOR UNKNOWN`) exclusively for `SandboxSimDB`.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `PARAMETER_SNIFFING = OFF` disables parameter value sniffing at the database scope (equivalent to `TRACE FLAG 4136` / `OPTIMIZE FOR UNKNOWN`) exclusively for `SandboxSimDB`.
- **D:** Correct. Database-scoped configurations isolate optimizer settings (`MAXDOP`, CE version, parameter sniffing) to a single database without affecting sibling databases on SQL MI/VMs or requiring server access. In this scenario: `PARAMETER_SNIFFING = OFF` disables parameter value sniffing at the database scope (equivalent to `TRACE FLAG 4136` / `OPTIMIZE FOR UNKNOWN`) exclusively for `SandboxSimDB`.

### Question 55 — D

Answer: SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators. Choosing schedule type `Start whenever the CPUs become idle` (configured under SQL Server Agent Properties -> Idle CPU condition) triggers low-priority maintenance automatically during quiet periods. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. Local study-map skill 4.1 (Create and Schedule SQL Server Agent Maintenance Jobs, Proxies, Severity `19–25` Alerts, and Database Mail), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server Agent jobs, schedules, alerts, and Database Mail operators (https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent).

- **A:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: Choosing schedule type `Start whenever the CPUs become idle` (configured under SQL Server Agent Properties -> Idle CPU condition) triggers low-priority maintenance automatically during quiet periods.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Choosing schedule type `Start whenever the CPUs become idle` (configured under SQL Server Agent Properties -> Idle CPU condition) triggers low-priority maintenance automatically during quiet periods.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Choosing schedule type `Start whenever the CPUs become idle` (configured under SQL Server Agent Properties -> Idle CPU condition) triggers low-priority maintenance automatically during quiet periods.
- **D:** Correct. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. In this scenario: Choosing schedule type `Start whenever the CPUs become idle` (configured under SQL Server Agent Properties -> Idle CPU condition) triggers low-priority maintenance automatically during quiet periods.

### Question 56 — C, E

Answers: Create a Windows/SQL Credential and map it to a SQL Server Agent Subsystem Proxy (`CmdExec` / `PowerShell`) instead of granting `sysadmin`; Configure Database Mail, define an Agent Operator, and create SQL Server Agent Alerts for Severity `19–25` and Errors `823`, `824`, and `825`. Create Credential-backed Subsystem Proxies for non-`sysadmin` job steps, and configure Database Mail Operators bound to Severity `19–25` and Error `823–825` Alerts. Local study-map skill 4.1 (Create and Schedule SQL Server Agent Maintenance Jobs, Proxies, Severity `19–25` Alerts, and Database Mail), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server Agent jobs, schedules, alerts, and Database Mail operators (https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Create Credential-backed Subsystem Proxies for non-`sysadmin` job steps, and configure Database Mail Operators bound to Severity `19–25` and Error `823–825` Alerts.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Create Credential-backed Subsystem Proxies for non-`sysadmin` job steps, and configure Database Mail Operators bound to Severity `19–25` and Error `823–825` Alerts.
- **C:** Correct. SQL Server Agent proxies let non-`sysadmin` job owners execute external subsystem steps under a scoped least-privilege identity. In this scenario: Create Credential-backed Subsystem Proxies for non-`sysadmin` job steps, and configure Database Mail Operators bound to Severity `19–25` and Error `823–825` Alerts.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Create Credential-backed Subsystem Proxies for non-`sysadmin` job steps, and configure Database Mail Operators bound to Severity `19–25` and Error `823–825` Alerts.
- **E:** Correct. Severity `19–25` and I/O errors `823–825` indicate critical resource exhaustion or storage corruption requiring immediate DBA notification. In this scenario: Create Credential-backed Subsystem Proxies for non-`sysadmin` job steps, and configure Database Mail Operators bound to Severity `19–25` and Error `823–825` Alerts.

### Question 57 — C

Answer: SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators. User-defined messages below severity 19 must be raised `WITH LOG` (or marked `@with_log = 'TRUE'` via `sp_addmessage`) so SQL Server writes the event to the error log monitored by SQL Server Agent Alerts. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. Local study-map skill 4.1 (Create and Schedule SQL Server Agent Maintenance Jobs, Proxies, Severity `19–25` Alerts, and Database Mail), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server Agent jobs, schedules, alerts, and Database Mail operators (https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: User-defined messages below severity 19 must be raised `WITH LOG` (or marked `@with_log = 'TRUE'` via `sp_addmessage`) so SQL Server writes the event to the error log monitored by SQL Server Agent Alerts.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: User-defined messages below severity 19 must be raised `WITH LOG` (or marked `@with_log = 'TRUE'` via `sp_addmessage`) so SQL Server writes the event to the error log monitored by SQL Server Agent Alerts.
- **C:** Correct. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. In this scenario: User-defined messages below severity 19 must be raised `WITH LOG` (or marked `@with_log = 'TRUE'` via `sp_addmessage`) so SQL Server writes the event to the error log monitored by SQL Server Agent Alerts.
- **D:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: User-defined messages below severity 19 must be raised `WITH LOG` (or marked `@with_log = 'TRUE'` via `sp_addmessage`) so SQL Server writes the event to the error log monitored by SQL Server Agent Alerts.

### Question 58 — B

Answer: Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries. In Azure SQL Managed Instance, SQL Server Agent runs as an always-on managed PaaS component whose lifecycle is controlled automatically by the platform rather than exposed to manual stop/start commands. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. Local study-map skill 4.2 (Troubleshoot SQL Server Agent Job Histories, Credential/Proxy Permissions, and SQL MI Subsystem Boundaries), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot SQL Server Agent jobs, proxies, and SQL Managed Instance Agent differences (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/transact-sql-tsql-differences-sql-server).

- **A:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: In Azure SQL Managed Instance, SQL Server Agent runs as an always-on managed PaaS component whose lifecycle is controlled automatically by the platform rather than exposed to manual stop/start commands.
- **B:** Correct. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. In this scenario: In Azure SQL Managed Instance, SQL Server Agent runs as an always-on managed PaaS component whose lifecycle is controlled automatically by the platform rather than exposed to manual stop/start commands.
- **C:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: In Azure SQL Managed Instance, SQL Server Agent runs as an always-on managed PaaS component whose lifecycle is controlled automatically by the platform rather than exposed to manual stop/start commands.
- **D:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: In Azure SQL Managed Instance, SQL Server Agent runs as an always-on managed PaaS component whose lifecycle is controlled automatically by the platform rather than exposed to manual stop/start commands.

### Question 59 — A

Answer: Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries. Change Step 2's `On success action` from `Quit the job reporting success` (the default when adding a new final step earlier) to `Go to the next step`. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. Local study-map skill 4.2 (Troubleshoot SQL Server Agent Job Histories, Credential/Proxy Permissions, and SQL MI Subsystem Boundaries), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot SQL Server Agent jobs, proxies, and SQL Managed Instance Agent differences (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/transact-sql-tsql-differences-sql-server).

- **A:** Correct. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. In this scenario: Change Step 2's `On success action` from `Quit the job reporting success` (the default when adding a new final step earlier) to `Go to the next step`.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Change Step 2's `On success action` from `Quit the job reporting success` (the default when adding a new final step earlier) to `Go to the next step`.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Change Step 2's `On success action` from `Quit the job reporting success` (the default when adding a new final step earlier) to `Go to the next step`.
- **D:** Incorrect for this requirement. BYOK TDE wraps the symmetric Database Encryption Key (`DEK`) with an asymmetric RSA key in Key Vault or Managed HSM so security admins control key rotation and instant revocation. Why the keyed choice wins: Change Step 2's `On success action` from `Quit the job reporting success` (the default when adding a new final step earlier) to `Go to the next step`.

### Question 60 — C, D

Answers: Mark sensitive parameters with `@secure()` in Bicep and pass Key Vault secret references from the parameter file rather than cleartext values; Run `az deployment group what-if` (or `New-AzResourceGroupDeployment -WhatIf`) as a pull-request gate before applying template changes. Use `@secure()` Bicep parameters backed by Azure Key Vault secret references, and execute `az deployment group what-if` during pull-request checks. Local study-map skill 4.3 (Automate Idempotent Deployment Using Bicep and ARM Templates with `@secure()` Key Vault References & `what-if`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Deploy Azure SQL resources using Bicep and Azure Resource Manager (ARM) templates (https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-Quickstart-bicep).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Use `@secure()` Bicep parameters backed by Azure Key Vault secret references, and execute `az deployment group what-if` during pull-request checks.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Use `@secure()` Bicep parameters backed by Azure Key Vault secret references, and execute `az deployment group what-if` during pull-request checks.
- **C:** Correct. `@secure()` prevents secret logging in deployment history, while Key Vault references resolve secrets inside ARM at deploy time without exposing them to CI runners. In this scenario: Use `@secure()` Bicep parameters backed by Azure Key Vault secret references, and execute `az deployment group what-if` during pull-request checks.
- **D:** Correct. `what-if` calculates predicted `Create`, `Modify`, `Delete`, and `Ignore` operations against live Azure SQL resources to catch destructive config drift. In this scenario: Use `@secure()` Bicep parameters backed by Azure Key Vault secret references, and execute `az deployment group what-if` during pull-request checks.
- **E:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Use `@secure()` Bicep parameters backed by Azure Key Vault secret references, and execute `az deployment group what-if` during pull-request checks.

### Question 61 — C

Answer: Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`. Set `parent: sqlServer` inside the `databases` resource block (or nest it inside `sqlServer`), allowing Bicep to emit both the full resource ID and implicit `dependsOn` ordering automatically. Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. Local study-map skill 4.3 (Automate Idempotent Deployment Using Bicep and ARM Templates with `@secure()` Key Vault References & `what-if`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Deploy Azure SQL resources using Bicep and Azure Resource Manager (ARM) templates (https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-Quickstart-bicep).

- **A:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Set `parent: sqlServer` inside the `databases` resource block (or nest it inside `sqlServer`), allowing Bicep to emit both the full resource ID and implicit `dependsOn` ordering automatically.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Set `parent: sqlServer` inside the `databases` resource block (or nest it inside `sqlServer`), allowing Bicep to emit both the full resource ID and implicit `dependsOn` ordering automatically.
- **C:** Correct. Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. In this scenario: Set `parent: sqlServer` inside the `databases` resource block (or nest it inside `sqlServer`), allowing Bicep to emit both the full resource ID and implicit `dependsOn` ordering automatically.
- **D:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Set `parent: sqlServer` inside the `databases` resource block (or nest it inside `sqlServer`), allowing Bicep to emit both the full resource ID and implicit `dependsOn` ordering automatically.

### Question 62 — B

Answer: Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`). Specifying `-ComputeModel Serverless` (alongside `-Edition GeneralPurpose` or `-Edition Hyperscale` where supported, `-MinVCore`, `-VCore`, and `-AutoPauseDelayInMinutes`) provisions Serverless compute. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. Local study-map skill 4.4 (Automate Azure SQL Provisioning and Day-2 Management Using Azure PowerShell (`Az.Sql`) and Azure CLI (`az sql`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL management using Azure PowerShell and Azure CLI (https://learn.microsoft.com/en-us/azure/azure-sql/database/scripts/create-and-configure-database-powershell).

- **A:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Specifying `-ComputeModel Serverless` (alongside `-Edition GeneralPurpose` or `-Edition Hyperscale` where supported, `-MinVCore`, `-VCore`, and `-AutoPauseDelayInMinutes`) provisions Serverless compute.
- **B:** Correct. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. In this scenario: Specifying `-ComputeModel Serverless` (alongside `-Edition GeneralPurpose` or `-Edition Hyperscale` where supported, `-MinVCore`, `-VCore`, and `-AutoPauseDelayInMinutes`) provisions Serverless compute.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Specifying `-ComputeModel Serverless` (alongside `-Edition GeneralPurpose` or `-Edition Hyperscale` where supported, `-MinVCore`, `-VCore`, and `-AutoPauseDelayInMinutes`) provisions Serverless compute.
- **D:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Specifying `-ComputeModel Serverless` (alongside `-Edition GeneralPurpose` or `-Edition Hyperscale` where supported, `-MinVCore`, `-VCore`, and `-AutoPauseDelayInMinutes`) provisions Serverless compute.

### Question 63 — D

Answer: Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`). `az sql server tde-key set` assigns the specified Azure Key Vault key URI as the active TDE protector on the logical SQL server. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. Local study-map skill 4.4 (Automate Azure SQL Provisioning and Day-2 Management Using Azure PowerShell (`Az.Sql`) and Azure CLI (`az sql`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL management using Azure PowerShell and Azure CLI (https://learn.microsoft.com/en-us/azure/azure-sql/database/scripts/create-and-configure-database-powershell).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: `az sql server tde-key set` assigns the specified Azure Key Vault key URI as the active TDE protector on the logical SQL server.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: `az sql server tde-key set` assigns the specified Azure Key Vault key URI as the active TDE protector on the logical SQL server.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `az sql server tde-key set` assigns the specified Azure Key Vault key URI as the active TDE protector on the logical SQL server.
- **D:** Correct. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. In this scenario: `az sql server tde-key set` assigns the specified Azure Key Vault key URI as the active TDE protector on the logical SQL server.

### Question 64 — D

Answer: Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules. Query `az sql mi op list -g rg-pay --mi sqlmi-pay` (or `Get-AzSqlInstanceOperation` / portal `Operations` blade) to inspect exact step-by-step management operation percentages and estimated completion time. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. Local study-map skill 4.5 (Monitor and Troubleshoot Automated Deployments (`CorrelationId`, Quota, SQL MI Subnet Delegation/UDR/NSG)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot ARM/Bicep template and SQL Managed Instance subnet deployment errors (https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/common-deployment-errors).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Query `az sql mi op list -g rg-pay --mi sqlmi-pay` (or `Get-AzSqlInstanceOperation` / portal `Operations` blade) to inspect exact step-by-step management operation percentages and estimated completion time.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Query `az sql mi op list -g rg-pay --mi sqlmi-pay` (or `Get-AzSqlInstanceOperation` / portal `Operations` blade) to inspect exact step-by-step management operation percentages and estimated completion time.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Query `az sql mi op list -g rg-pay --mi sqlmi-pay` (or `Get-AzSqlInstanceOperation` / portal `Operations` blade) to inspect exact step-by-step management operation percentages and estimated completion time.
- **D:** Correct. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. In this scenario: Query `az sql mi op list -g rg-pay --mi sqlmi-pay` (or `Get-AzSqlInstanceOperation` / portal `Operations` blade) to inspect exact step-by-step management operation percentages and estimated completion time.

### Question 65 — B

Answer: Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules. Deleting the last SQL Managed Instance in a subnet triggers asynchronous background deletion of the underlying **Virtual Cluster** (`Microsoft.Sql/virtualClusters`); once virtual cluster cleanup finishes (or is deleted), the subnet lock clears. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. Local study-map skill 4.5 (Monitor and Troubleshoot Automated Deployments (`CorrelationId`, Quota, SQL MI Subnet Delegation/UDR/NSG)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot ARM/Bicep template and SQL Managed Instance subnet deployment errors (https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/common-deployment-errors).

- **A:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Deleting the last SQL Managed Instance in a subnet triggers asynchronous background deletion of the underlying **Virtual Cluster** (`Microsoft.Sql/virtualClusters`); once virtual cluster cleanup finishes (or is deleted), the subnet lock clears.
- **B:** Correct. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. In this scenario: Deleting the last SQL Managed Instance in a subnet triggers asynchronous background deletion of the underlying **Virtual Cluster** (`Microsoft.Sql/virtualClusters`); once virtual cluster cleanup finishes (or is deleted), the subnet lock clears.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Deleting the last SQL Managed Instance in a subnet triggers asynchronous background deletion of the underlying **Virtual Cluster** (`Microsoft.Sql/virtualClusters`); once virtual cluster cleanup finishes (or is deleted), the subnet lock clears.
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Deleting the last SQL Managed Instance in a subnet triggers asynchronous background deletion of the underlying **Virtual Cluster** (`Microsoft.Sql/virtualClusters`); once virtual cluster cleanup finishes (or is deleted), the subnet lock clears.

### Question 66 — B

Answer: Create S1+ Job Database & Elastic Job Agent with UAMI → Create contained UAMI user on target DBs with needed permissions → Define Target Group (`jobs.sp_add_target_group_member`) → Add T-SQL steps & schedule (`jobs.sp_add_job`). Provision an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and schedule T-SQL steps (`jobs.sp_add_job`). Modern Elastic Jobs use a dedicated S1+ job database, an Elastic Job Agent assigned a User-Assigned Managed Identity (UAMI) authorized on target databases, a target group, and scheduled T-SQL steps. Local study-map skill 4.6 (Create and Configure Azure SQL Database Elastic Jobs Across Target Groups Using User-Assigned Managed Identity), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Elastic jobs in Azure SQL Database with Managed Identity authentication (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-jobs-overview).

- **A:** Incorrect for this requirement. Incorrect workflow: Elastic Job databases require S1 or higher, target groups must exist before binding executions, NTLM local accounts are invalid in SQL DB, and `msdb` belongs to SQL Agent. Why the keyed choice wins: Provision an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and schedule T-SQL steps (`jobs.sp_add_job`).
- **B:** Correct. Modern Elastic Jobs use a dedicated S1+ job database, an Elastic Job Agent assigned a User-Assigned Managed Identity (UAMI) authorized on target databases, a target group, and scheduled T-SQL steps. In this scenario: Provision an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and schedule T-SQL steps (`jobs.sp_add_job`).
- **C:** Incorrect for this requirement. Incorrect workflow: Elastic Job Agents target Azure SQL servers, elastic pools, and databases using Managed Identity—never Cosmos DB containers or hardcoded Git secrets. Why the keyed choice wins: Provision an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and schedule T-SQL steps (`jobs.sp_add_job`).
- **D:** Incorrect for this requirement. Incorrect workflow: single Azure SQL Databases do not have SQL Server Agent or cross-DB linked servers in the same way as SQL MI; Elastic Jobs fan out T-SQL asynchronously. Why the keyed choice wins: Provision an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and schedule T-SQL steps (`jobs.sp_add_job`).

### Question 67 — D

Answer: Azure SQL Database Elastic Job Agent (`jobs.sp_add_job`) authenticating to Target Groups across servers/pools via a User-Assigned Managed Identity (`UAMI`). Elastic Jobs automatically retry transient network or throttling failures per target database; idempotent T-SQL ensures retries succeed cleanly if a prior attempt partially committed or ran earlier. Elastic Jobs fan out T-SQL maintenance and schema scripts asynchronously across hundreds of Azure SQL Databases, elastic pools, and subscriptions using passwordless UAMI authentication. Local study-map skill 4.6 (Create and Configure Azure SQL Database Elastic Jobs Across Target Groups Using User-Assigned Managed Identity), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Elastic jobs in Azure SQL Database with Managed Identity authentication (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-jobs-overview).

- **A:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: Elastic Jobs automatically retry transient network or throttling failures per target database; idempotent T-SQL ensures retries succeed cleanly if a prior attempt partially committed or ran earlier.
- **B:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Elastic Jobs automatically retry transient network or throttling failures per target database; idempotent T-SQL ensures retries succeed cleanly if a prior attempt partially committed or ran earlier.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Elastic Jobs automatically retry transient network or throttling failures per target database; idempotent T-SQL ensures retries succeed cleanly if a prior attempt partially committed or ran earlier.
- **D:** Correct. Elastic Jobs fan out T-SQL maintenance and schema scripts asynchronously across hundreds of Azure SQL Databases, elastic pools, and subscriptions using passwordless UAMI authentication. In this scenario: Elastic Jobs automatically retry transient network or throttling failures per target database; idempotent T-SQL ensures retries succeed cleanly if a prior attempt partially committed or ran earlier.

### Question 68 — B

Answer: Azure Automation PowerShell / Python runbooks (or Azure Functions / Logic Apps) using a System-Assigned Managed Identity on a recurring schedule. An Azure Automation Python runbook authenticating via its System-Assigned Managed Identity (`ManagedIdentityCredential`) runs scheduled `azure-mgmt-sql` maintenance serverlessly. Azure Automation runbooks authenticate via Managed Identity (`Connect-AzAccount -Identity`) to scale vCores/Elastic Pools on schedule, rotate keys, or orchestrate hybrid maintenance via Hybrid Workers. Local study-map skill 4.7 (Automate Database Maintenance and Scaling Using Azure Automation Runbooks, Logic Apps, and Azure Functions), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL maintenance tasks with Azure Automation, Logic Apps, and Functions (https://learn.microsoft.com/en-us/azure/automation/overview).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: An Azure Automation Python runbook authenticating via its System-Assigned Managed Identity (`ManagedIdentityCredential`) runs scheduled `azure-mgmt-sql` maintenance serverlessly.
- **B:** Correct. Azure Automation runbooks authenticate via Managed Identity (`Connect-AzAccount -Identity`) to scale vCores/Elastic Pools on schedule, rotate keys, or orchestrate hybrid maintenance via Hybrid Workers. In this scenario: An Azure Automation Python runbook authenticating via its System-Assigned Managed Identity (`ManagedIdentityCredential`) runs scheduled `azure-mgmt-sql` maintenance serverlessly.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: An Azure Automation Python runbook authenticating via its System-Assigned Managed Identity (`ManagedIdentityCredential`) runs scheduled `azure-mgmt-sql` maintenance serverlessly.
- **D:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: An Azure Automation Python runbook authenticating via its System-Assigned Managed Identity (`ManagedIdentityCredential`) runs scheduled `azure-mgmt-sql` maintenance serverlessly.

### Question 69 — C

Answer: No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases. No — Resource Governor (`CREATE WORKLOAD GROUP`) is unsupported on single Azure SQL Databases; instead, scale vCores via Automation or isolate workloads on read replicas / Elastic Pools. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. Local study-map skill 4.7 (Automate Database Maintenance and Scaling Using Azure Automation Runbooks, Logic Apps, and Azure Functions), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL maintenance tasks with Azure Automation, Logic Apps, and Functions (https://learn.microsoft.com/en-us/azure/automation/overview).

- **A:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: No — Resource Governor (`CREATE WORKLOAD GROUP`) is unsupported on single Azure SQL Databases; instead, scale vCores via Automation or isolate workloads on read replicas / Elastic Pools.
- **B:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: No — Resource Governor (`CREATE WORKLOAD GROUP`) is unsupported on single Azure SQL Databases; instead, scale vCores via Automation or isolate workloads on read replicas / Elastic Pools.
- **C:** Correct. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. In this scenario: No — Resource Governor (`CREATE WORKLOAD GROUP`) is unsupported on single Azure SQL Databases; instead, scale vCores via Automation or isolate workloads on read replicas / Elastic Pools.
- **D:** Incorrect for this requirement. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Why the keyed choice wins: No — Resource Governor (`CREATE WORKLOAD GROUP`) is unsupported on single Azure SQL Databases; instead, scale vCores via Automation or isolate workloads on read replicas / Elastic Pools.

### Question 70 — C

Answer: Configure Azure Monitor Metric / Log Alert rules routed to Action Groups and query `jobs.job_executions` in the Elastic Job database to diagnose step failures. Setting `@step_timeout_seconds` and `@retry_attempts` in `jobs.sp_add_jobstep` aborts hung target executions cleanly, logging the timeout in `jobs.job_executions` and Incrementing the `Failed Jobs` Azure Monitor metric. Action Groups dispatch email/SMS/webhook/Logic App notifications when alert thresholds fire, while `jobs.job_executions` exposes per-target error messages, retries, and timeouts for Elastic Jobs. Local study-map skill 4.8 (Configure Azure Monitor Action Group Alerts on Database Tasks and Troubleshoot `jobs.job_executions`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure Azure Monitor alerts and troubleshoot Elastic Jobs and automated runbooks (https://learn.microsoft.com/en-us/azure/azure-sql/database/alerts-insights-configure-portal).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Setting `@step_timeout_seconds` and `@retry_attempts` in `jobs.sp_add_jobstep` aborts hung target executions cleanly, logging the timeout in `jobs.job_executions` and Incrementing the `Failed Jobs` Azure Monitor metric.
- **B:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Setting `@step_timeout_seconds` and `@retry_attempts` in `jobs.sp_add_jobstep` aborts hung target executions cleanly, logging the timeout in `jobs.job_executions` and Incrementing the `Failed Jobs` Azure Monitor metric.
- **C:** Correct. Action Groups dispatch email/SMS/webhook/Logic App notifications when alert thresholds fire, while `jobs.job_executions` exposes per-target error messages, retries, and timeouts for Elastic Jobs. In this scenario: Setting `@step_timeout_seconds` and `@retry_attempts` in `jobs.sp_add_jobstep` aborts hung target executions cleanly, logging the timeout in `jobs.job_executions` and Incrementing the `Failed Jobs` Azure Monitor metric.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Setting `@step_timeout_seconds` and `@retry_attempts` in `jobs.sp_add_jobstep` aborts hung target executions cleanly, logging the timeout in `jobs.job_executions` and Incrementing the `Failed Jobs` Azure Monitor metric.

### Question 71 — C

Answer: No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent. No — exporting a `.bacpac` directly from an active OLTP primary is neither transactionally consistent across tables nor fast enough for a 5-minute RPO; use Failover Groups / PITR backups instead. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Local study-map skill 5.1 (Recommend HA/DR Architectures Based on RPO and RTO (`Zone Redundant`, `Failover Groups`, `Geo-Restore`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Business continuity, RPO/RTO targets, and high availability in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recovery-hadr-overview).

- **A:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: No — exporting a `.bacpac` directly from an active OLTP primary is neither transactionally consistent across tables nor fast enough for a 5-minute RPO; use Failover Groups / PITR backups instead.
- **B:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: No — exporting a `.bacpac` directly from an active OLTP primary is neither transactionally consistent across tables nor fast enough for a 5-minute RPO; use Failover Groups / PITR backups instead.
- **C:** Correct. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. In this scenario: No — exporting a `.bacpac` directly from an active OLTP primary is neither transactionally consistent across tables nor fast enough for a 5-minute RPO; use Failover Groups / PITR backups instead.
- **D:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: No — exporting a `.bacpac` directly from an active OLTP primary is neither transactionally consistent across tables nor fast enough for a 5-minute RPO; use Failover Groups / PITR backups instead.

### Question 72 — B

Answer: Hybrid DR using Managed Instance link with bidirectional online failover between SQL Server 2022 and Azure SQL Managed Instance. SQL Server 2022 introduces compatible database format/version alignment with Azure SQL Managed Instance, enabling bidirectional online planned failover over Managed Instance link. SQL Server 2022 supports two-way online planned failover back and forth with Azure SQL Managed Instance via Managed Instance link (whereas SQL Server 2016–2019 link failover is one-way to Azure). Local study-map skill 5.2 (Evaluate Hybrid HA/DR (`Managed Instance Link` Bidirectional SQL 2022 Failover) and Azure-Specific HA Tiers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Hybrid HA/DR with Managed Instance link and distributed Availability Groups (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-disaster-recovery).

- **A:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: SQL Server 2022 introduces compatible database format/version alignment with Azure SQL Managed Instance, enabling bidirectional online planned failover over Managed Instance link.
- **B:** Correct. SQL Server 2022 supports two-way online planned failover back and forth with Azure SQL Managed Instance via Managed Instance link (whereas SQL Server 2016–2019 link failover is one-way to Azure). In this scenario: SQL Server 2022 introduces compatible database format/version alignment with Azure SQL Managed Instance, enabling bidirectional online planned failover over Managed Instance link.
- **C:** Incorrect for this requirement. Managed Instance link online failback from SQL MI to SQL Server requires SQL Server 2022 or later; SQL Server 2016 and 2019 support one-way migration into SQL MI only. Why the keyed choice wins: SQL Server 2022 introduces compatible database format/version alignment with Azure SQL Managed Instance, enabling bidirectional online planned failover over Managed Instance link.
- **D:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: SQL Server 2022 introduces compatible database format/version alignment with Azure SQL Managed Instance, enabling bidirectional online planned failover over Managed Instance link.

### Question 73 — B

Answer: Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`). Hyperscale attaches hot standby secondary compute replicas (`>= 1` HA replica) directly to the shared distributed page-server tier, failing over compute in seconds without re-hydrating local storage or replaying long logs. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. Local study-map skill 5.2 (Evaluate Hybrid HA/DR (`Managed Instance Link` Bidirectional SQL 2022 Failover) and Azure-Specific HA Tiers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Hybrid HA/DR with Managed Instance link and distributed Availability Groups (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-disaster-recovery).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Hyperscale attaches hot standby secondary compute replicas (`>= 1` HA replica) directly to the shared distributed page-server tier, failing over compute in seconds without re-hydrating local storage or replaying long logs.
- **B:** Correct. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. In this scenario: Hyperscale attaches hot standby secondary compute replicas (`>= 1` HA replica) directly to the shared distributed page-server tier, failing over compute in seconds without re-hydrating local storage or replaying long logs.
- **C:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Hyperscale attaches hot standby secondary compute replicas (`>= 1` HA replica) directly to the shared distributed page-server tier, failing over compute in seconds without re-hydrating local storage or replaying long logs.
- **D:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: Hyperscale attaches hot standby secondary compute replicas (`>= 1` HA replica) directly to the shared distributed page-server tier, failing over compute in seconds without re-hydrating local storage or replaying long logs.

### Question 74 — C

Answer: Non-disruptive DR readiness drill executing a planned zero-data-loss Failover Group switch (`Switch-AzSqlDatabaseFailoverGroup`), validating app listeners, and failing back. Configure internal DNS forwarders to honor Azure's `30-second` TTL on `*.database.windows.net` / `privatelink.database.windows.net` and ensure connection pools use short connection lifetimes / retry logic (`ConnectRetryCount`). Planned failover synchronizes pending log records before switching roles (`RPO = 0`), validating secondary firewall/Entra configs and `<fog>.database.windows.net` DNS redirection safely. Local study-map skill 5.3 (Plan Non-Disruptive HA/DR Failover Drills, Listener Redirection Validation, and Read-Only Secondary Testing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Disaster recovery drills and failover testing for Azure SQL solutions (https://learn.microsoft.com/en-us/azure/azure-sql/database/disaster-recovery-drills).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Configure internal DNS forwarders to honor Azure's `30-second` TTL on `*.database.windows.net` / `privatelink.database.windows.net` and ensure connection pools use short connection lifetimes / retry logic (`ConnectRetryCount`).
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure internal DNS forwarders to honor Azure's `30-second` TTL on `*.database.windows.net` / `privatelink.database.windows.net` and ensure connection pools use short connection lifetimes / retry logic (`ConnectRetryCount`).
- **C:** Correct. Planned failover synchronizes pending log records before switching roles (`RPO = 0`), validating secondary firewall/Entra configs and `<fog>.database.windows.net` DNS redirection safely. In this scenario: Configure internal DNS forwarders to honor Azure's `30-second` TTL on `*.database.windows.net` / `privatelink.database.windows.net` and ensure connection pools use short connection lifetimes / retry logic (`ConnectRetryCount`).
- **D:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Configure internal DNS forwarders to honor Azure's `30-second` TTL on `*.database.windows.net` / `privatelink.database.windows.net` and ensure connection pools use short connection lifetimes / retry logic (`ConnectRetryCount`).

### Question 75 — D

Answer: No — taking an ad-hoc non-`COPY_ONLY` full backup resets the differential base and breaks downstream differential restores. No — running a regular Full backup without `WITH COPY_ONLY` advances the differential base LSN to Wednesday noon, breaking any Thursday Differential restore attempted on top of Sunday's Full backup. A standard `BACKUP DATABASE` updates the differential base LSN; ad-hoc exports on SQL Managed Instance or Availability Groups must specify `WITH COPY_ONLY` to preserve the backup chain. Local study-map skill 5.4 (Recommend Backup & Restore Strategies (`COPY_ONLY` on MI/AGs and Azure Backup SQL-Aware Policies on VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated backups, COPY_ONLY backups, and Azure Backup for SQL Server in Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-overview).

- **A:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: No — running a regular Full backup without `WITH COPY_ONLY` advances the differential base LSN to Wednesday noon, breaking any Thursday Differential restore attempted on top of Sunday's Full backup.
- **B:** Incorrect for this requirement. SQL Server write-ahead logging performs sequential unbuffered writes; enabling `ReadOnly` or `ReadWrite` host caching on `.ldf` disks degrades throughput or risks corruption. Why the keyed choice wins: No — running a regular Full backup without `WITH COPY_ONLY` advances the differential base LSN to Wednesday noon, breaking any Thursday Differential restore attempted on top of Sunday's Full backup.
- **C:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: No — running a regular Full backup without `WITH COPY_ONLY` advances the differential base LSN to Wednesday noon, breaking any Thursday Differential restore attempted on top of Sunday's Full backup.
- **D:** Correct. A standard `BACKUP DATABASE` updates the differential base LSN; ad-hoc exports on SQL Managed Instance or Availability Groups must specify `WITH COPY_ONLY` to preserve the backup chain. In this scenario: No — running a regular Full backup without `WITH COPY_ONLY` advances the differential base LSN to Wednesday noon, breaking any Thursday Differential restore attempted on top of Sunday's Full backup.

### Question 76 — B

Answer: Use `BACKUP DATABASE ... WITH COPY_ONLY` for ad-hoc exports on SQL MI / AGs, and Azure Backup Recovery Services Vault SQL-aware policies (`15-min` log RPO) on SQL VMs. Secondary AG replicas support `COPY_ONLY` Full backups and regular Transaction Log backups, whereas **Differential** backups (`WITH DIFFERENTIAL`) and non-`COPY_ONLY` Full backups are unsupported on secondary replicas. `COPY_ONLY` preserves the differential and log backup chain, while Azure Backup for SQL Server in Azure VMs automates application-consistent Full, Differential, and 15-minute Transaction Log backups. Local study-map skill 5.4 (Recommend Backup & Restore Strategies (`COPY_ONLY` on MI/AGs and Azure Backup SQL-Aware Policies on VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated backups, COPY_ONLY backups, and Azure Backup for SQL Server in Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-overview).

- **A:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Secondary AG replicas support `COPY_ONLY` Full backups and regular Transaction Log backups, whereas **Differential** backups (`WITH DIFFERENTIAL`) and non-`COPY_ONLY` Full backups are unsupported on secondary replicas.
- **B:** Correct. `COPY_ONLY` preserves the differential and log backup chain, while Azure Backup for SQL Server in Azure VMs automates application-consistent Full, Differential, and 15-minute Transaction Log backups. In this scenario: Secondary AG replicas support `COPY_ONLY` Full backups and regular Transaction Log backups, whereas **Differential** backups (`WITH DIFFERENTIAL`) and non-`COPY_ONLY` Full backups are unsupported on secondary replicas.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Secondary AG replicas support `COPY_ONLY` Full backups and regular Transaction Log backups, whereas **Differential** backups (`WITH DIFFERENTIAL`) and non-`COPY_ONLY` Full backups are unsupported on secondary replicas.
- **D:** Incorrect for this requirement. A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs. Why the keyed choice wins: Secondary AG replicas support `COPY_ONLY` Full backups and regular Transaction Log backups, whereas **Differential** backups (`WITH DIFFERENTIAL`) and non-`COPY_ONLY` Full backups are unsupported on secondary replicas.

### Question 77 — B

Answer: No — moving a database across SQL Managed Instances starts a fresh backup chain and does not carry over prior PITR backups. No — moving a database across SQL Managed Instances starts a brand-new backup chain at move completion (`16:00 UTC`), so pre-move PITR points are unavailable on the destination instance. Online SQL Managed Instance Database Move replicates current data with zero loss, but historical PITR backups remain tied to the source instance and are unavailable on the destination. Local study-map skill 5.5 (Perform Native Restores, Point-in-Time Restore (`1–35d` PITR), Deleted-DB Restore, and `ADR` Instant Rollback), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Point-in-time restore (PITR), Accelerated Database Recovery (ADR), and deleted DB restore (https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups).

- **A:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: No — moving a database across SQL Managed Instances starts a brand-new backup chain at move completion (`16:00 UTC`), so pre-move PITR points are unavailable on the destination instance.
- **B:** Correct. Online SQL Managed Instance Database Move replicates current data with zero loss, but historical PITR backups remain tied to the source instance and are unavailable on the destination. In this scenario: No — moving a database across SQL Managed Instances starts a brand-new backup chain at move completion (`16:00 UTC`), so pre-move PITR points are unavailable on the destination instance.
- **C:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: No — moving a database across SQL Managed Instances starts a brand-new backup chain at move completion (`16:00 UTC`), so pre-move PITR points are unavailable on the destination instance.
- **D:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: No — moving a database across SQL Managed Instances starts a brand-new backup chain at move completion (`16:00 UTC`), so pre-move PITR points are unavailable on the destination instance.

### Question 78 — D, E

Answers: Configure an Azure SQL Long-Term Retention (`LTR`) policy (`WeeklyRetention`, `MonthlyRetention`, `YearlyRetention`, `WeekOfYear`) up to 10 years; Enable and lock time-based immutability (`WORM`) on the LTR backup policy so nobody can shorten retention or delete compliance backups early. Configure a Long-Term Retention (`LTR`) policy (`YearlyRetention = P10Y`, `WeekOfYear`) and enable + lock time-based immutability (`WORM`) on the LTR policy. Local study-map skill 5.6 (Configure Long-Term Backup Retention (`LTR` up to `10y`), Time-Based Immutable WORM Locks, and Storage Redundancy), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Long-term backup retention (LTR) and time-based immutable WORM backups in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/long-term-retention-overview).

- **A:** Incorrect for this requirement. Short-Term PITR caps at `35` days (`1–35` days); multi-year retention up to `10 years` with WORM deletion lock requires Long-Term Retention (`LTR`) with time-based immutability. Why the keyed choice wins: Configure a Long-Term Retention (`LTR`) policy (`YearlyRetention = P10Y`, `WeekOfYear`) and enable + lock time-based immutability (`WORM`) on the LTR policy.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Configure a Long-Term Retention (`LTR`) policy (`YearlyRetention = P10Y`, `WeekOfYear`) and enable + lock time-based immutability (`WORM`) on the LTR policy.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure a Long-Term Retention (`LTR`) policy (`YearlyRetention = P10Y`, `WeekOfYear`) and enable + lock time-based immutability (`WORM`) on the LTR policy.
- **D:** Correct. LTR copies full backups into separate geo-redundant/zone-redundant Azure Blob tiers according to ISO-8601 duration policies (e.g., `P7Y`). In this scenario: Configure a Long-Term Retention (`LTR`) policy (`YearlyRetention = P10Y`, `WeekOfYear`) and enable + lock time-based immutability (`WORM`) on the LTR policy.
- **E:** Correct. Once locked, time-based LTR immutability enforces write-once-read-many protection against ransomware or rogue privileged admins. In this scenario: Configure a Long-Term Retention (`LTR`) policy (`YearlyRetention = P10Y`, `WeekOfYear`) and enable + lock time-based immutability (`WORM`) on the LTR policy.

### Question 79 — A

Answer: Yes — the proposed configuration satisfies every stated technical, security, and availability requirement. Yes — LTR backups live independently in Azure Blob Storage under the subscription/location and remain restorable until their configured retention period expires, even after the source database (or even the logical server) is deleted. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. Local study-map skill 5.6 (Configure Long-Term Backup Retention (`LTR` up to `10y`), Time-Based Immutable WORM Locks, and Storage Redundancy), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Long-term backup retention (LTR) and time-based immutable WORM backups in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/long-term-retention-overview).

- **A:** Correct. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. In this scenario: Yes — LTR backups live independently in Azure Blob Storage under the subscription/location and remain restorable until their configured retention period expires, even after the source database (or even the logical server) is deleted.
- **B:** Incorrect for this requirement. SQL Server write-ahead logging performs sequential unbuffered writes; enabling `ReadOnly` or `ReadWrite` host caching on `.ldf` disks degrades throughput or risks corruption. Why the keyed choice wins: Yes — LTR backups live independently in Azure Blob Storage under the subscription/location and remain restorable until their configured retention period expires, even after the source database (or even the logical server) is deleted.
- **C:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: Yes — LTR backups live independently in Azure Blob Storage under the subscription/location and remain restorable until their configured retention period expires, even after the source database (or even the logical server) is deleted.
- **D:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: Yes — LTR backups live independently in Azure Blob Storage under the subscription/location and remain restorable until their configured retention period expires, even after the source database (or even the logical server) is deleted.

### Question 80 — D, E

Answers: Create a SQL Server `CREDENTIAL` (`IDENTITY = 'Managed Identity'` or `'SHARED ACCESS SIGNATURE'`) matching the Azure Blob container URL; Stripe `BACKUP DATABASE` across multiple `TO URL = 'https://...bak'` block blob targets with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`. Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob container, and stripe `BACKUP DATABASE` across multiple `TO URL` block blobs with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`. Local study-map skill 5.7 (Back Up to and Restore from Azure Blob Storage URL Using T-SQL Stripes (`TO URL`) and Managed Identity / SAS), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server backup to URL and restore from Azure Blob Storage with Managed Identity or SAS (https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url-azure-blob-storage).

- **A:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob container, and stripe `BACKUP DATABASE` across multiple `TO URL` block blobs with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob container, and stripe `BACKUP DATABASE` across multiple `TO URL` block blobs with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`.
- **C:** Incorrect for this requirement. A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs. Why the keyed choice wins: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob container, and stripe `BACKUP DATABASE` across multiple `TO URL` block blobs with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`.
- **D:** Correct. SQL Server and SQL MI authenticate `BACKUP TO URL` / `RESTORE FROM URL` requests to Azure Storage via a server-level credential. In this scenario: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob container, and stripe `BACKUP DATABASE` across multiple `TO URL` block blobs with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`.
- **E:** Correct. Multiple `URL` targets write to Azure Block Blobs in parallel, scaling single backups up to ~12.8 TB (`64` stripes) with maximum throughput. In this scenario: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob container, and stripe `BACKUP DATABASE` across multiple `TO URL` block blobs with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`.

### Question 81 — A

Answer: Striped T-SQL `BACKUP DATABASE ... TO URL = ...` across up to 64 block blobs (`MAXTRANSFERSIZE`, `COMPRESSION`) authenticated via `Managed Identity` or `SHARED ACCESS SIGNATURE` Credential. Native SQL Server backup encryption wraps the AES-256 stream using a `SERVER CERTIFICATE` (or `SERVER ASYMMETRIC KEY`) stored in `master`. Backing up to multiple URLs creates block blobs supporting up to ~12.8 TB striped backups (`200 GB+` per blob, unlike legacy single-page-blob 1 TB limits) using `CREATE CREDENTIAL`. Local study-map skill 5.7 (Back Up to and Restore from Azure Blob Storage URL Using T-SQL Stripes (`TO URL`) and Managed Identity / SAS), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server backup to URL and restore from Azure Blob Storage with Managed Identity or SAS (https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url-azure-blob-storage).

- **A:** Correct. Backing up to multiple URLs creates block blobs supporting up to ~12.8 TB striped backups (`200 GB+` per blob, unlike legacy single-page-blob 1 TB limits) using `CREATE CREDENTIAL`. In this scenario: Native SQL Server backup encryption wraps the AES-256 stream using a `SERVER CERTIFICATE` (or `SERVER ASYMMETRIC KEY`) stored in `master`.
- **B:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: Native SQL Server backup encryption wraps the AES-256 stream using a `SERVER CERTIFICATE` (or `SERVER ASYMMETRIC KEY`) stored in `master`.
- **C:** Incorrect for this requirement. A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs. Why the keyed choice wins: Native SQL Server backup encryption wraps the AES-256 stream using a `SERVER CERTIFICATE` (or `SERVER ASYMMETRIC KEY`) stored in `master`.
- **D:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Native SQL Server backup encryption wraps the AES-256 stream using a `SERVER CERTIFICATE` (or `SERVER ASYMMETRIC KEY`) stored in `master`.

### Question 82 — A, C

Answers: Connect OLTP write traffic to `<fog>.database.windows.net` and read-only analytics to `<fog>.secondary.database.windows.net`; Configure `ReadWriteFailoverPolicy = Automatic` with `GracePeriodWithDataLossHours >= 1` so transient blips do not trigger premature lossy failover. Configure OLTP clients to use `fog-treasury.database.windows.net` and reporting clients to use `fog-treasury.secondary.database.windows.net`, and set `GracePeriodWithDataLossHours >= 1`. Local study-map skill 5.8 (Configure Failover Groups (`<fog>.database.windows.net`, Grace Period) vs Active Geo-Replication (`4` Replicas)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Failover groups and active geo-replication in Azure SQL Database and SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db).

- **A:** Correct. Failover Group listener endpoints abstract underlying regional server names and automatically redirect read-write and read-only connections after failover. In this scenario: Configure OLTP clients to use `fog-treasury.database.windows.net` and reporting clients to use `fog-treasury.secondary.database.windows.net`, and set `GracePeriodWithDataLossHours >= 1`.
- **B:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Configure OLTP clients to use `fog-treasury.database.windows.net` and reporting clients to use `fog-treasury.secondary.database.windows.net`, and set `GracePeriodWithDataLossHours >= 1`.
- **C:** Correct. The grace period controls how long Azure waits during an unrecoverable primary region outage before forcing an automatic failover if async log lag remains. In this scenario: Configure OLTP clients to use `fog-treasury.database.windows.net` and reporting clients to use `fog-treasury.secondary.database.windows.net`, and set `GracePeriodWithDataLossHours >= 1`.
- **D:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: Configure OLTP clients to use `fog-treasury.database.windows.net` and reporting clients to use `fog-treasury.secondary.database.windows.net`, and set `GracePeriodWithDataLossHours >= 1`.
- **E:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure OLTP clients to use `fog-treasury.database.windows.net` and reporting clients to use `fog-treasury.secondary.database.windows.net`, and set `GracePeriodWithDataLossHours >= 1`.

### Question 83 — C

Answer: Failover Groups for automatic multi-database failover behind stable `<fog>.database.windows.net` / `.secondary` listeners vs Active Geo-Replication for up to 4 readable secondaries. Adding `ApplicationIntent=ReadOnly` to the TDS connection string instructs the SQL gateway to route the session to the built-in Business Critical / Hyperscale read-only replica (while `<fog>.secondary.database.windows.net` routes to the Failover Group geo-secondary). Failover Groups fail over coupled databases together and redirect connection strings automatically (`GracePeriodWithDataLossHours >= 1`), whereas Active Geo-Replication supports up to 4 secondaries per DB without automatic listener redirection. Local study-map skill 5.8 (Configure Failover Groups (`<fog>.database.windows.net`, Grace Period) vs Active Geo-Replication (`4` Replicas)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Failover groups and active geo-replication in Azure SQL Database and SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db).

- **A:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Adding `ApplicationIntent=ReadOnly` to the TDS connection string instructs the SQL gateway to route the session to the built-in Business Critical / Hyperscale read-only replica (while `<fog>.secondary.database.windows.net` routes to the Failover Group geo-secondary).
- **B:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Adding `ApplicationIntent=ReadOnly` to the TDS connection string instructs the SQL gateway to route the session to the built-in Business Critical / Hyperscale read-only replica (while `<fog>.secondary.database.windows.net` routes to the Failover Group geo-secondary).
- **C:** Correct. Failover Groups fail over coupled databases together and redirect connection strings automatically (`GracePeriodWithDataLossHours >= 1`), whereas Active Geo-Replication supports up to 4 secondaries per DB without automatic listener redirection. In this scenario: Adding `ApplicationIntent=ReadOnly` to the TDS connection string instructs the SQL gateway to route the session to the built-in Business Critical / Hyperscale read-only replica (while `<fog>.secondary.database.windows.net` routes to the Failover Group geo-secondary).
- **D:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Adding `ApplicationIntent=ReadOnly` to the TDS connection string instructs the SQL gateway to route the session to the built-in Business Critical / Hyperscale read-only replica (while `<fog>.secondary.database.windows.net` routes to the Failover Group geo-secondary).

### Question 84 — A

Answer: Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`. SQL Server 2019/2022 Enterprise Edition supports up to **5** synchronous-commit replicas (out of up to 9 total replicas: 1 primary + 8 secondaries) inside a single Always On Availability Group. Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). Local study-map skill 5.9 (Configure Always On Availability Groups on SQL MI and Azure VMs (`Cloud Witness`, `DNN`, `ILB` Port `59999`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On availability groups on SQL Server on Azure VMs (Cloud Witness, DNN, ILB) (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/availability-group-overview).

- **A:** Correct. Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). In this scenario: SQL Server 2019/2022 Enterprise Edition supports up to **5** synchronous-commit replicas (out of up to 9 total replicas: 1 primary + 8 secondaries) inside a single Always On Availability Group.
- **B:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: SQL Server 2019/2022 Enterprise Edition supports up to **5** synchronous-commit replicas (out of up to 9 total replicas: 1 primary + 8 secondaries) inside a single Always On Availability Group.
- **C:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: SQL Server 2019/2022 Enterprise Edition supports up to **5** synchronous-commit replicas (out of up to 9 total replicas: 1 primary + 8 secondaries) inside a single Always On Availability Group.
- **D:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: SQL Server 2019/2022 Enterprise Edition supports up to **5** synchronous-commit replicas (out of up to 9 total replicas: 1 primary + 8 secondaries) inside a single Always On Availability Group.

### Question 85 — B

Answer: Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`. Setting `SEEDING_MODE = AUTOMATIC` (paired with `ALTER AVAILABILITY GROUP ... GRANT CREATE ANY DATABASE` on the secondary) streams initial VDI seeding directly over the TCP `5022` mirroring endpoint. Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). Local study-map skill 5.9 (Configure Always On Availability Groups on SQL MI and Azure VMs (`Cloud Witness`, `DNN`, `ILB` Port `59999`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On availability groups on SQL Server on Azure VMs (Cloud Witness, DNN, ILB) (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/availability-group-overview).

- **A:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Setting `SEEDING_MODE = AUTOMATIC` (paired with `ALTER AVAILABILITY GROUP ... GRANT CREATE ANY DATABASE` on the secondary) streams initial VDI seeding directly over the TCP `5022` mirroring endpoint.
- **B:** Correct. Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). In this scenario: Setting `SEEDING_MODE = AUTOMATIC` (paired with `ALTER AVAILABILITY GROUP ... GRANT CREATE ANY DATABASE` on the secondary) streams initial VDI seeding directly over the TCP `5022` mirroring endpoint.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Setting `SEEDING_MODE = AUTOMATIC` (paired with `ALTER AVAILABILITY GROUP ... GRANT CREATE ANY DATABASE` on the secondary) streams initial VDI seeding directly over the TCP `5022` mirroring endpoint.
- **D:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: Setting `SEEDING_MODE = AUTOMATIC` (paired with `ALTER AVAILABILITY GROUP ... GRANT CREATE ANY DATABASE` on the secondary) streams initial VDI seeding directly over the TCP `5022` mirroring endpoint.

### Question 86 — D

Answer: Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`). Zone-Redundant Storage (`ZRS`) on Premium SSD Azure Shared Disks synchronously replicates block storage across three Availability Zones so cross-zone FCI nodes can mount the shared LUN. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. Local study-map skill 5.10 (Configure Always On Failover Cluster Instances (`Azure Shared Disks` `ZRS`) and T-SQL Log Shipping on Azure VMs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On Failover Cluster Instances (Azure Shared Disks) and Log Shipping on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/failover-cluster-instance-overview).

- **A:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Zone-Redundant Storage (`ZRS`) on Premium SSD Azure Shared Disks synchronously replicates block storage across three Availability Zones so cross-zone FCI nodes can mount the shared LUN.
- **B:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: Zone-Redundant Storage (`ZRS`) on Premium SSD Azure Shared Disks synchronously replicates block storage across three Availability Zones so cross-zone FCI nodes can mount the shared LUN.
- **C:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: Zone-Redundant Storage (`ZRS`) on Premium SSD Azure Shared Disks synchronously replicates block storage across three Availability Zones so cross-zone FCI nodes can mount the shared LUN.
- **D:** Correct. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. In this scenario: Zone-Redundant Storage (`ZRS`) on Premium SSD Azure Shared Disks synchronously replicates block storage across three Availability Zones so cross-zone FCI nodes can mount the shared LUN.

### Question 87 — B

Answer: Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`). The database remains in `RESTORING` state and rejects all user `SELECT` connections (`Database '...' cannot be opened. It is in the middle of a restore`); read access requires `WITH STANDBY` (or Always On Availability Groups). Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. Local study-map skill 5.10 (Configure Always On Failover Cluster Instances (`Azure Shared Disks` `ZRS`) and T-SQL Log Shipping on Azure VMs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On Failover Cluster Instances (Azure Shared Disks) and Log Shipping on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/failover-cluster-instance-overview).

- **A:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: The database remains in `RESTORING` state and rejects all user `SELECT` connections (`Database '...' cannot be opened. It is in the middle of a restore`); read access requires `WITH STANDBY` (or Always On Availability Groups).
- **B:** Correct. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. In this scenario: The database remains in `RESTORING` state and rejects all user `SELECT` connections (`Database '...' cannot be opened. It is in the middle of a restore`); read access requires `WITH STANDBY` (or Always On Availability Groups).
- **C:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: The database remains in `RESTORING` state and rejects all user `SELECT` connections (`Database '...' cannot be opened. It is in the middle of a restore`); read access requires `WITH STANDBY` (or Always On Availability Groups).
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: The database remains in `RESTORING` state and rejects all user `SELECT` connections (`Database '...' cannot be opened. It is in the middle of a restore`); read access requires `WITH STANDBY` (or Always On Availability Groups).

### Question 88 — B

Answer: Query `sys.dm_hadr_database_replica_states` (`synchronization_state_desc`, `log_send_queue_size`, `redo_queue_size`) and `sys.dm_geo_replication_link_status`, plus verify NSG probe port `59999`. The primary replica is waiting for the synchronous secondary replica to receive, harden to its `.ldf` transaction log disk, and acknowledge commit blocks—caused by network RTT latency or slow secondary log-disk `WRITELOG` I/O. High `log_send_queue_size` indicates network bottlenecks between primary and secondary, high `redo_queue_size` indicates slow redo I/O/CPU or long-running read queries on the secondary, and blocked ILB probe port `59999` breaks AG listener routing. Local study-map skill 5.11 (Monitor and Troubleshoot HA/DR Health (`sys.dm_hadr_database_replica_states`, `redo_queue_size`, `log_send_queue_size`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor and troubleshoot Always On availability groups and geo-replication health (https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/monitor-availability-groups-transact-sql).

- **A:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: The primary replica is waiting for the synchronous secondary replica to receive, harden to its `.ldf` transaction log disk, and acknowledge commit blocks—caused by network RTT latency or slow secondary log-disk `WRITELOG` I/O.
- **B:** Correct. High `log_send_queue_size` indicates network bottlenecks between primary and secondary, high `redo_queue_size` indicates slow redo I/O/CPU or long-running read queries on the secondary, and blocked ILB probe port `59999` breaks AG listener routing. In this scenario: The primary replica is waiting for the synchronous secondary replica to receive, harden to its `.ldf` transaction log disk, and acknowledge commit blocks—caused by network RTT latency or slow secondary log-disk `WRITELOG` I/O.
- **C:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: The primary replica is waiting for the synchronous secondary replica to receive, harden to its `.ldf` transaction log disk, and acknowledge commit blocks—caused by network RTT latency or slow secondary log-disk `WRITELOG` I/O.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: The primary replica is waiting for the synchronous secondary replica to receive, harden to its `.ldf` transaction log disk, and acknowledge commit blocks—caused by network RTT latency or slow secondary log-disk `WRITELOG` I/O.

### Question 89 — A

Answer: Enable Microsoft Entra-only authentication (`azuread_authentication_only`) on the logical SQL server or SQL Managed Instance. Enabling Microsoft Entra-only authentication (`azuread_authentication_only`) rejects all SQL authentication handshakes and enforces centralized Entra ID tokens and MFA. Microsoft Entra-only authentication disables legacy SQL Server logins (`sa` and password auth) completely, enforcing centralized MFA, Conditional Access, and token-based Managed Identities. Local study-map skill 2.1 (Configure Microsoft Entra ID and Microsoft Entra-Only Authentication Across SQL DB, SQL MI, and SQL Server), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure and manage Microsoft Entra authentication with Azure SQL and SQL Server (https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview).

- **A:** Correct. Microsoft Entra-only authentication disables legacy SQL Server logins (`sa` and password auth) completely, enforcing centralized MFA, Conditional Access, and token-based Managed Identities. In this scenario: Enabling Microsoft Entra-only authentication (`azuread_authentication_only`) rejects all SQL authentication handshakes and enforces centralized Entra ID tokens and MFA.
- **B:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Enabling Microsoft Entra-only authentication (`azuread_authentication_only`) rejects all SQL authentication handshakes and enforces centralized Entra ID tokens and MFA.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Enabling Microsoft Entra-only authentication (`azuread_authentication_only`) rejects all SQL authentication handshakes and enforces centralized Entra ID tokens and MFA.
- **D:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Enabling Microsoft Entra-only authentication (`azuread_authentication_only`) rejects all SQL authentication handshakes and enforces centralized Entra ID tokens and MFA.

### Question 90 — D

Answer: Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`). Create contained database users mapped to Microsoft Entra security groups or Managed Identities (`CREATE USER [SG-Custody-App] FROM EXTERNAL PROVIDER`) inside each user database. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. Local study-map skill 2.3 (Configure Security Principals and Portable Contained Microsoft Entra Users (`FROM EXTERNAL PROVIDER`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Contained database users and Microsoft Entra security principals in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage).

- **A:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Create contained database users mapped to Microsoft Entra security groups or Managed Identities (`CREATE USER [SG-Custody-App] FROM EXTERNAL PROVIDER`) inside each user database.
- **B:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Create contained database users mapped to Microsoft Entra security groups or Managed Identities (`CREATE USER [SG-Custody-App] FROM EXTERNAL PROVIDER`) inside each user database.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Create contained database users mapped to Microsoft Entra security groups or Managed Identities (`CREATE USER [SG-Custody-App] FROM EXTERNAL PROVIDER`) inside each user database.
- **D:** Correct. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. In this scenario: Create contained database users mapped to Microsoft Entra security groups or Managed Identities (`CREATE USER [SG-Custody-App] FROM EXTERNAL PROVIDER`) inside each user database.

### Question 91 — A

Answer: Built-in granular server-level roles (`##MS_ServerStateReader##`, `##MS_DefinitionReader##`) or `GRANT VIEW DATABASE PERFORMANCE STATE`. Adding the NOC Entra group to `##MS_ServerStateReader##` grants `VIEW SERVER PERFORMANCE STATE` across all databases while withholding data-table read permissions. Modern granular server roles and state permissions let monitoring accounts inspect DMVs and metadata without granting `sysadmin`, `db_owner`, or `SELECT` access to user tables. Local study-map skill 2.3 (Configure Security Principals and Portable Contained Microsoft Entra Users (`FROM EXTERNAL PROVIDER`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Contained database users and Microsoft Entra security principals in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage).

- **A:** Correct. Modern granular server roles and state permissions let monitoring accounts inspect DMVs and metadata without granting `sysadmin`, `db_owner`, or `SELECT` access to user tables. In this scenario: Adding the NOC Entra group to `##MS_ServerStateReader##` grants `VIEW SERVER PERFORMANCE STATE` across all databases while withholding data-table read permissions.
- **B:** Incorrect for this requirement. RLS transparently filters `SELECT`/`UPDATE`/`DELETE` rows via `FILTER PREDICATE` and blocks unauthorized cross-tenant `INSERT`/`UPDATE` writes via `BLOCK PREDICATE` inside the engine. Why the keyed choice wins: Adding the NOC Entra group to `##MS_ServerStateReader##` grants `VIEW SERVER PERFORMANCE STATE` across all databases while withholding data-table read permissions.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Adding the NOC Entra group to `##MS_ServerStateReader##` grants `VIEW SERVER PERFORMANCE STATE` across all databases while withholding data-table read permissions.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Adding the NOC Entra group to `##MS_ServerStateReader##` grants `VIEW SERVER PERFORMANCE STATE` across all databases while withholding data-table read permissions.

### Question 92 — B

Answer: Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`). Deploy Azure SQL Database Business Critical with `Zone Redundant` enabled (`99.995%` SLA, `RPO = 0` across zones) paired with a cross-region Failover Group (`RPO = 5s` SLA). Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. Local study-map skill 5.1 (Recommend HA/DR Architectures Based on RPO and RTO (`Zone Redundant`, `Failover Groups`, `Geo-Restore`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Business continuity, RPO/RTO targets, and high availability in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recovery-hadr-overview).

- **A:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Deploy Azure SQL Database Business Critical with `Zone Redundant` enabled (`99.995%` SLA, `RPO = 0` across zones) paired with a cross-region Failover Group (`RPO = 5s` SLA).
- **B:** Correct. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. In this scenario: Deploy Azure SQL Database Business Critical with `Zone Redundant` enabled (`99.995%` SLA, `RPO = 0` across zones) paired with a cross-region Failover Group (`RPO = 5s` SLA).
- **C:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Deploy Azure SQL Database Business Critical with `Zone Redundant` enabled (`99.995%` SLA, `RPO = 0` across zones) paired with a cross-region Failover Group (`RPO = 5s` SLA).
- **D:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Deploy Azure SQL Database Business Critical with `Zone Redundant` enabled (`99.995%` SLA, `RPO = 0` across zones) paired with a cross-region Failover Group (`RPO = 5s` SLA).

### Question 93 — A

Answer: Provision secondary SQL server with matching firewall/Private Link & Entra admin → Create Failover Group with coupled DBs → Point apps to `<fog>.database.windows.net` & `.secondary` → Run planned `Switch-AzSqlDatabaseFailoverGroup` drill. Mirror network/Entra settings on the paired server, group coupled treasury DBs in a Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and execute planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback. A resilient Failover Group mirrors security/network configs on the secondary server, groups coupled databases under stable read-write and read-only listeners, and validates readiness via planned zero-data-loss failover. Local study-map skill 5.3 (Plan Non-Disruptive HA/DR Failover Drills, Listener Redirection Validation, and Read-Only Secondary Testing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Disaster recovery drills and failover testing for Azure SQL solutions (https://learn.microsoft.com/en-us/azure/azure-sql/database/disaster-recovery-drills).

- **A:** Correct. A resilient Failover Group mirrors security/network configs on the secondary server, groups coupled databases under stable read-write and read-only listeners, and validates readiness via planned zero-data-loss failover. In this scenario: Mirror network/Entra settings on the paired server, group coupled treasury DBs in a Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and execute planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback.
- **B:** Incorrect for this requirement. Incorrect workflow: forced failover with `AllowDataLoss` risks dropping uncommitted transactions during drills, and hardcoding regional server names breaks automatic client redirection. Why the keyed choice wins: Mirror network/Entra settings on the paired server, group coupled treasury DBs in a Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and execute planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback.
- **C:** Incorrect for this requirement. Incorrect workflow: Failover Groups span distinct regions, replicate user databases rather than `master`/`tempdb`, and `.secondary.database.windows.net` is strictly read-only. Why the keyed choice wins: Mirror network/Entra settings on the paired server, group coupled treasury DBs in a Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and execute planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback.
- **D:** Incorrect for this requirement. Incorrect workflow: deleting production databases and manually rewriting connection strings causes hours of avoidable downtime instead of testing non-disruptive Failover Group listener failover. Why the keyed choice wins: Mirror network/Entra settings on the paired server, group coupled treasury DBs in a Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and execute planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback.

### Question 94 — D

Answer: Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback. Accelerated Database Recovery (`ADR`, enabled by default in Azure SQL Database and SQL Managed Instance and available in SQL Server 2019+) uses a Persistent Version Store (`PVS`) for instantaneous rollback and aggressive log truncation. Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. Local study-map skill 5.5 (Perform Native Restores, Point-in-Time Restore (`1–35d` PITR), Deleted-DB Restore, and `ADR` Instant Rollback), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Point-in-time restore (PITR), Accelerated Database Recovery (ADR), and deleted DB restore (https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups).

- **A:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Accelerated Database Recovery (`ADR`, enabled by default in Azure SQL Database and SQL Managed Instance and available in SQL Server 2019+) uses a Persistent Version Store (`PVS`) for instantaneous rollback and aggressive log truncation.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Accelerated Database Recovery (`ADR`, enabled by default in Azure SQL Database and SQL Managed Instance and available in SQL Server 2019+) uses a Persistent Version Store (`PVS`) for instantaneous rollback and aggressive log truncation.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Accelerated Database Recovery (`ADR`, enabled by default in Azure SQL Database and SQL Managed Instance and available in SQL Server 2019+) uses a Persistent Version Store (`PVS`) for instantaneous rollback and aggressive log truncation.
- **D:** Correct. Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. In this scenario: Accelerated Database Recovery (`ADR`, enabled by default in Azure SQL Database and SQL Managed Instance and available in SQL Server 2019+) uses a Persistent Version Store (`PVS`) for instantaneous rollback and aggressive log truncation.

### Question 95 — B

Answer: Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`). Underestimated cardinality grants insufficient query workspace RAM, spilling hash buckets to `tempdb`; Percentile and Persistence Memory Grant Feedback (`compat 160`) learns actual memory needs and persists right-sized grants in Query Store. Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. Local study-map skill 3.9 (Analyze Execution Plans (`Key Lookup`, `TempDB` Spills, Row Skew) and Monitor via SQL Intelligent Insights), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Execution plans and SQL Intelligent Insights automated performance diagnostics (https://learn.microsoft.com/en-us/azure/azure-sql/database/intelligent-insights-overview).

- **A:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Underestimated cardinality grants insufficient query workspace RAM, spilling hash buckets to `tempdb`; Percentile and Persistence Memory Grant Feedback (`compat 160`) learns actual memory needs and persists right-sized grants in Query Store.
- **B:** Correct. Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. In this scenario: Underestimated cardinality grants insufficient query workspace RAM, spilling hash buckets to `tempdb`; Percentile and Persistence Memory Grant Feedback (`compat 160`) learns actual memory needs and persists right-sized grants in Query Store.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Underestimated cardinality grants insufficient query workspace RAM, spilling hash buckets to `tempdb`; Percentile and Persistence Memory Grant Feedback (`compat 160`) learns actual memory needs and persists right-sized grants in Query Store.
- **D:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Underestimated cardinality grants insufficient query workspace RAM, spilling hash buckets to `tempdb`; Percentile and Persistence Memory Grant Feedback (`compat 160`) learns actual memory needs and persists right-sized grants in Query Store.

### Question 96 — A

Answer: Configure `cost threshold for parallelism`, `MAXDOP`, `max server memory (MB)`, and Resource Governor (`WORKLOAD GROUP` + `RESOURCE POOL` + classifier UDF) on SQL MI / VMs. Create a Resource Governor `RESOURCE POOL` (`CAP_CPU_PERCENT = 25` / `MAX_CPU_PERCENT = 25`), bind a `WORKLOAD GROUP`, register a schema-bound classifier function matching analyst logins/app names, and run `ALTER RESOURCE GOVERNOR RECONFIGURE`. Tuning `cost threshold for parallelism` (e.g., 50) and `MAXDOP` curbs OLTP `CXPACKET` waits, while Resource Governor throttles reporting CPU/memory caps on SQL Server and SQL Managed Instance. Local study-map skill 3.12 (Configure Server Performance Settings (`MAXDOP`, `cost threshold`, `max server memory`) and Resource Governor), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Server configuration options (MAXDOP, memory) and Resource Governor workload isolation (https://learn.microsoft.com/en-us/sql/relational-databases/resource-governor/resource-governor).

- **A:** Correct. Tuning `cost threshold for parallelism` (e.g., 50) and `MAXDOP` curbs OLTP `CXPACKET` waits, while Resource Governor throttles reporting CPU/memory caps on SQL Server and SQL Managed Instance. In this scenario: Create a Resource Governor `RESOURCE POOL` (`CAP_CPU_PERCENT = 25` / `MAX_CPU_PERCENT = 25`), bind a `WORKLOAD GROUP`, register a schema-bound classifier function matching analyst logins/app names, and run `ALTER RESOURCE GOVERNOR RECONFIGURE`.
- **B:** Incorrect for this requirement. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. Why the keyed choice wins: Create a Resource Governor `RESOURCE POOL` (`CAP_CPU_PERCENT = 25` / `MAX_CPU_PERCENT = 25`), bind a `WORKLOAD GROUP`, register a schema-bound classifier function matching analyst logins/app names, and run `ALTER RESOURCE GOVERNOR RECONFIGURE`.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Create a Resource Governor `RESOURCE POOL` (`CAP_CPU_PERCENT = 25` / `MAX_CPU_PERCENT = 25`), bind a `WORKLOAD GROUP`, register a schema-bound classifier function matching analyst logins/app names, and run `ALTER RESOURCE GOVERNOR RECONFIGURE`.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Create a Resource Governor `RESOURCE POOL` (`CAP_CPU_PERCENT = 25` / `MAX_CPU_PERCENT = 25`), bind a `WORKLOAD GROUP`, register a schema-bound classifier function matching analyst logins/app names, and run `ALTER RESOURCE GOVERNOR RECONFIGURE`.

### Question 97 — A

Answer: Enable compatibility level `160` Intelligent Query Processing (`Parameter Sensitive Plan` optimization, `Memory Grant Feedback` persistence, `Scalar UDF Inlining`, `DOP Feedback`). Parameter Sensitive Plan (`PSP`) optimization compiles a dispatcher plan with up to three query variants bucketed by parameter cardinality skews, eliminating parameter-sniffing thrash automatically. SQL 2022 / Azure SQL compat `160` IQP caches multiple active plans per query based on parameter cardinality (`PSP`), right-sizes `tempdb`-spilling memory grants, and inlines scalar T-SQL UDFs. Local study-map skill 3.14 (Identify Use Cases for Intelligent Query Processing (`PSP` Optimization, Memory Grant Feedback, Scalar UDF Inlining)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Intelligent Query Processing (IQP) features in SQL databases (https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing).

- **A:** Correct. SQL 2022 / Azure SQL compat `160` IQP caches multiple active plans per query based on parameter cardinality (`PSP`), right-sizes `tempdb`-spilling memory grants, and inlines scalar T-SQL UDFs. In this scenario: Parameter Sensitive Plan (`PSP`) optimization compiles a dispatcher plan with up to three query variants bucketed by parameter cardinality skews, eliminating parameter-sniffing thrash automatically.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Parameter Sensitive Plan (`PSP`) optimization compiles a dispatcher plan with up to three query variants bucketed by parameter cardinality skews, eliminating parameter-sniffing thrash automatically.
- **C:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Parameter Sensitive Plan (`PSP`) optimization compiles a dispatcher plan with up to three query variants bucketed by parameter cardinality skews, eliminating parameter-sniffing thrash automatically.
- **D:** Incorrect for this requirement. Row-by-row cursors and multi-statement TVFs under legacy compatibility levels execute thousands of iterative context switches and 1-row cardinality guesses. Why the keyed choice wins: Parameter Sensitive Plan (`PSP`) optimization compiles a dispatcher plan with up to three query variants bucketed by parameter cardinality skews, eliminating parameter-sniffing thrash automatically.

### Question 98 — C

Answer: SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring). SQL database in Microsoft Fabric runs the Azure SQL engine with Microsoft Entra-only auth and automatically mirrors operational tables into OneLake in Delta Parquet format alongside a SQL analytics endpoint. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Local study-map skill 1.3 (Identify Use Cases for SQL Server Enabled by Azure Arc and SQL Database in Microsoft Fabric), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server enabled by Azure Arc and SQL database in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/database/sql/overview).

- **A:** Incorrect for this requirement. SQL Server on Azure VMs (IaaS) provides full OS access, custom third-party drivers, legacy SQL Server version pinning, SSIS/SSRS/SSAS co-hosting, and `Ebdsv5` high remote storage throughput. Why the keyed choice wins: SQL database in Microsoft Fabric runs the Azure SQL engine with Microsoft Entra-only auth and automatically mirrors operational tables into OneLake in Delta Parquet format alongside a SQL analytics endpoint.
- **B:** Incorrect for this requirement. SQL database in Microsoft Fabric enforces Microsoft Entra authentication exclusively (SQL logins are unsupported) and manages backups/OneLake mirroring automatically as SaaS. Why the keyed choice wins: SQL database in Microsoft Fabric runs the Azure SQL engine with Microsoft Entra-only auth and automatically mirrors operational tables into OneLake in Delta Parquet format alongside a SQL analytics endpoint.
- **C:** Correct. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. In this scenario: SQL database in Microsoft Fabric runs the Azure SQL engine with Microsoft Entra-only auth and automatically mirrors operational tables into OneLake in Delta Parquet format alongside a SQL analytics endpoint.
- **D:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: SQL database in Microsoft Fabric runs the Azure SQL engine with Microsoft Entra-only auth and automatically mirrors operational tables into OneLake in Delta Parquet format alongside a SQL analytics endpoint.

### Question 99 — D

Answer: Azure Migrate (`Azure SQL` assessment) and the Azure SQL Migration extension for Azure Data Studio / VS Code. Azure Migrate (`Azure SQL` assessment) and the Azure SQL Migration extension for Azure Data Studio / VS Code collect performance counters and produce right-sized PaaS/IaaS SKU recommendations. Following Data Migration Assistant (DMA) retirement, Azure Migrate and the Azure SQL Migration extension assess compatibility blockers, feature parity, and performance-based vCore SKU right-sizing. Local study-map skill 1.10 (Evaluate Migration Requirements, Offline vs Online Strategies, and SKU Sizing via Azure Migrate & ADS), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Assess and plan SQL Server migrations using Azure Migrate and Azure SQL Migration extension (https://learn.microsoft.com/en-us/data-migration/sql-server/managed-instance/overview).

- **A:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Azure Migrate (`Azure SQL` assessment) and the Azure SQL Migration extension for Azure Data Studio / VS Code collect performance counters and produce right-sized PaaS/IaaS SKU recommendations.
- **B:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Azure Migrate (`Azure SQL` assessment) and the Azure SQL Migration extension for Azure Data Studio / VS Code collect performance counters and produce right-sized PaaS/IaaS SKU recommendations.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Azure Migrate (`Azure SQL` assessment) and the Azure SQL Migration extension for Azure Data Studio / VS Code collect performance counters and produce right-sized PaaS/IaaS SKU recommendations.
- **D:** Correct. Following Data Migration Assistant (DMA) retirement, Azure Migrate and the Azure SQL Migration extension assess compatibility blockers, feature parity, and performance-based vCore SKU right-sizing. In this scenario: Azure Migrate (`Azure SQL` assessment) and the Azure SQL Migration extension for Azure Data Studio / VS Code collect performance counters and produce right-sized PaaS/IaaS SKU recommendations.

### Question 100 — D

Answer: Online Azure SQL Managed Instance Database Move / Copy (`TCP 5022` & `11000–11999`, 24-hour manual completion window). Cross-VNet online SQL Managed Instance Database Move/Copy (and Failover Groups) requires inbound and outbound TCP port `5022` plus ephemeral port range `11000–11999` on both SQL MI subnets. Online MI Database Copy/Move uses Always On seeding across instances/subscriptions; once `Ready for completion`, you have 24 hours to complete (`Move` removes source DB with zero data loss; `Copy` keeps both). Local study-map skill 1.12 (Implement Azure SQL Managed Instance Online Database Copy and Move (`24h` Completion, `TCP 5022`/`11000-11999`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Copy or move a database online across Azure SQL Managed Instances (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/database-copy-move-how-to).

- **A:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: Cross-VNet online SQL Managed Instance Database Move/Copy (and Failover Groups) requires inbound and outbound TCP port `5022` plus ephemeral port range `11000–11999` on both SQL MI subnets.
- **B:** Incorrect for this requirement. `Start-AzSqlInstanceDatabaseLogReplay` continuously replays `.bak`/`.trn` files from Blob storage until `Complete-AzSqlInstanceDatabaseLogReplay` restores the final tail-log backup. Why the keyed choice wins: Cross-VNet online SQL Managed Instance Database Move/Copy (and Failover Groups) requires inbound and outbound TCP port `5022` plus ephemeral port range `11000–11999` on both SQL MI subnets.
- **C:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Cross-VNet online SQL Managed Instance Database Move/Copy (and Failover Groups) requires inbound and outbound TCP port `5022` plus ephemeral port range `11000–11999` on both SQL MI subnets.
- **D:** Correct. Online MI Database Copy/Move uses Always On seeding across instances/subscriptions; once `Ready for completion`, you have 24 hours to complete (`Move` removes source DB with zero data loss; `Copy` keeps both). In this scenario: Cross-VNet online SQL Managed Instance Database Move/Copy (and Failover Groups) requires inbound and outbound TCP port `5022` plus ephemeral port range `11000–11999` on both SQL MI subnets.
