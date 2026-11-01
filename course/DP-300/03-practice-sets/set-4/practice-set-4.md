# Microsoft Exam DP-300: Administering Microsoft Azure SQL Solutions — Full-Length Mock Exam 4

Exam DP-300 (Smart Manufacturing ERP, IaaS SQL Server on Azure VMs, and Elastic Jobs) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint & Credential Notice:** Aligned to the official **October 27, 2026** DP-300 study guide (`Microsoft Certified: Azure Database Administrator Associate`). Associate-level certification with **no prerequisite exam required**, free online annual renewal on Microsoft Learn, split-screen `learn.microsoft.com` access during non-lab exam sections, and hands-on coverage across **T-SQL**, **Azure PowerShell**, **Azure CLI**, **Bicep**, and **KQL**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` T-SQL/PowerShell/CLI/Bicep/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Azure SQL case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area T-SQL/CLI dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn Azure SQL and SQL Server documentation — never recalled live items or copied Microsoft sample case studies.

## Questions

### 1. A shop-floor MES system requires SQL Server 2022 Enterprise with FileStream varbinary documents on NTFS volumes, custom Linked Servers to an AS/400 OLE DB driver installed in Windows, and SSIS packages running locally. Which Azure SQL option supports all of these?

Domain: Plan and implement data platform resources

- A. Azure SQL Database vCore Elastic Pool with per-database min and max vCore limits
- B. SQL Server on Azure Virtual Machines (`Ebdsv5` series) with full OS and engine version control
- C. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- D. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)

### 2. A supplier portal team wants managed PaaS patching and HA while preserving SQL Server Agent jobs, `msdb` Database Mail, and cross-database queries across 15 ERP modules without paying Business Critical pricing. Which offering fits best?

Domain: Plan and implement data platform resources

- A. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas
- D. Azure SQL Managed Instance (Next-gen General Purpose) with decoupled IOPS and storage sliders

### 3. Before deploying an Azure SQL Managed Instance into `vnet-manufacturing-eu`, your network automation script validates the target subnet. Which two configurations must pass validation? Select two.

Domain: Plan and implement data platform resources

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- C. Switch eligible hybrid SQL Server instances to hourly Azure Arc pay-as-you-go billing instead of upfront core licenses
- D. Associate a User-Defined Route (`UDR`) table (`0.0.0.0/0` -> `Internet` for management plane) and required NSG rules with the SQL MI subnet
- E. Create a dedicated VNet subnet (`/28` or larger) with no other cloud resources and delegate it to `Microsoft.Sql/managedInstances`

### 4. You register a custom Windows Server + SQL Server 2022 VM with the SQL IaaS Agent Extension via ARM/Bicep resource type `Microsoft.SqlVirtualMachine/____` so Automated Backup and storage pools configure declaratively. Which ARM resource type represents the SQL VM registration?

Domain: Plan and implement data platform resources

- A. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- B. Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 5. Quality-control engineers spin up a `SQL database` item inside Microsoft Fabric to capture assembly-line defect tickets and blend them immediately with Spark Lakehouse notebooks. Which two built-in characteristics apply? Select two.

Domain: Plan and implement data platform resources

- A. Query automatically replicated OneLake Delta Parquet tables and the read-only SQL analytics endpoint from Spark and Direct Lake
- B. Authenticate applications and users exclusively with Microsoft Entra ID identities, service principals, or workspace roles
- C. Configure SQL Server password logins (`CREATE LOGIN ... WITH PASSWORD`) and T-SQL `BACKUP DATABASE ... TO DISK` inside SQL database in Microsoft Fabric
- D. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- E. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 6. Sixteen remote stamping plants run SQL Server 2022 on ruggedized edge servers with intermittent WAN links and seasonal shifts. Connecting them as SQL Server enabled by Azure Arc unlocks which T-SQL fleet command feature from Azure?

Domain: Plan and implement data platform resources

- A. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. SQL Server enabled by Azure Arc (`Microsoft.AzureArcData/sqlServerInstances`)
- D. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)

### 7. A robotics `TorqueReadings` table partitions weekly sensor batches by `ReadingWeekStart`. Every Monday at 00:01 UTC you must add a new empty weekly partition and swap out the 105th-week partition with zero blocking `DELETE` I/O. Which four-step sequence should you run?

Domain: Plan and implement data platform resources

- A. MERGE oldest partition boundary first → Run row-by-row DELETE on 80M rows → Create unindexed staging table on a different filegroup → SPLIT partition function
- B. Create staging table without matching CHECK constraints → SWITCH partition across two separate Azure SQL Databases → MERGE future boundary → Truncate production table
- C. SPLIT partition function for incoming future boundary → Create empty staging table on same filegroup with matching schema/indexes → ALTER TABLE ... SWITCH oldest partition to staging → Archive staging data & MERGE retired boundary
- D. ALTER TABLE ... SWITCH oldest partition directly to Azure Blob Storage → SPLIT partition function → Rebuild entire table offline → MERGE all boundaries

### 8. Why must every nonclustered index on a partitioned table include the partitioning column (either as a key or implicitly via storage alignment on the same `PARTITION SCHEME`) before `ALTER TABLE ... SWITCH` can succeed?

Domain: Plan and implement data platform resources

- A. Table partitioning using `CREATE PARTITION FUNCTION ... AS RANGE RIGHT` with aligned indexes and `ALTER TABLE ... SWITCH`
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- D. Horizontal sharding using the Elastic Database Client Library (`ShardMapManager` with `ListShardMap` or `RangeShardMap`)

### 9. An industrial IoT gateway runs SQL Server 2022 on SUSE Linux Enterprise Server (`SLES 15`). Where does SQL Server on Linux write its default `errorlog` and `system_health` diagnostic files on the Linux filesystem?

Domain: Plan and implement data platform resources

- A. SQL Server on Linux configured via `mssql-conf` or Linux container images for consistent CI/CD dev-test parity
- B. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- C. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- D. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas

### 10. An engineering CAD simulation database in Azure SQL Database runs intense 16-vCore bursts on Tuesdays and Thursdays from 09:00–17:00 and receives zero connections the rest of the week. Which configuration minimizes cost without manual scaling scripts?

Domain: Plan and implement data platform resources

- A. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica
- D. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas

### 11. A plant warehouse execution database on Azure SQL Managed Instance uses Hekaton memory-optimized tables (`SCHEMA_AND_DATA`) to ingest 40,000 barcode scans per second. Which SQL Managed Instance service tier is mandatory for In-Memory OLTP?

Domain: Plan and implement data platform resources

- A. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- B. Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica
- C. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- D. Azure SQL Managed Instance (Next-gen General Purpose) with decoupled IOPS and storage sliders

### 12. To shrink sensor partitions older than two years inside a 4.2-billion-row Clustered Columnstore table (`REBUILD PARTITION = 1 WITH (DATA_COMPRESSION = ____)`) while keeping recent 90-day partitions fast, which partition-level T-SQL rebuild option should you apply?

Domain: Plan and implement data platform resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Evaluate `sp_estimate_data_compression_savings` and apply `ROW`, `PAGE`, or `COLUMNSTORE_ARCHIVE` compression per partition
- C. Replace set-based `JOIN` queries with nested `FAST_FORWARD` T-SQL cursors calling multi-statement table-valued functions per row under compat `100`
- D. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon

### 13. Before migrating six legacy factory SQL Server 2014 instances, you want to detect deprecated T-SQL syntax, unsupported trace flags, and target compatibility blockers for Azure SQL Database vs SQL Managed Instance. Which supported Microsoft assessment tool should you use?

Domain: Plan and implement data platform resources

- A. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- B. Azure Migrate (`Azure SQL` assessment) and the Azure SQL Migration extension for Azure Data Studio / VS Code
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 14. A segmented factory VLAN forbids opening direct inbound/outbound TCP `5022` between on-premises SQL Server 2019 and Azure SQL Managed Instance, yet outbound HTTPS `443` to Azure Blob Storage is allowed and online migration with minimal cutover is required. Which migration method works over HTTPS Blob Storage?

Domain: Plan and implement data platform resources

- A. Log Replay Service (`LRS`) streaming Full, Differential, and Tail-Log backups from Azure Blob Storage into SQL Managed Instance
- B. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- C. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- D. Expect online bidirectional planned failback from Azure SQL Managed Instance directly back to on-premises SQL Server 2016 without downtime

### 15. You need to consolidate `MES_RoutingDB` online from a dev-shared SQL Managed Instance to a dedicated production SQL Managed Instance in another peered VNet, dropping the source copy automatically with zero data loss. Which four-step workflow applies?

Domain: Plan and implement data platform resources

- A. Verify VNet peering & TCP 5022 + 11000-11999 rules → Start online Database Move from source to target SQL MI → Wait for seeding to reach Ready for completion → Complete move within 24 hours so target comes online
- B. Stop source SQL Managed Instance compute → Detach user database via sp_detach_db → Copy files over port 1433 → Reattach database on target SQL MI
- C. Start online Database Move → Wait 72 hours in Ready for completion state → Open TCP 5022 + 11000-11999 rules → Expect PITR backups from source MI to transfer automatically
- D. Export `.bacpac` to Azure Table storage → Import `.bacpac` onto target SQL MI → Complete move after 48 hours → Retain source database online automatically

### 16. Corporate InfoSec requires eliminating all password-based SQL logins on SQL Server 2022 Azure VMs onboarded to Azure Arc and on Azure SQL Managed Instances. Which authentication posture achieves this?

Domain: Implement a secure environment

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- C. Enable Microsoft Entra-only authentication (`azuread_authentication_only`) on the logical SQL server or SQL Managed Instance
- D. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database

### 17. An IoT telemetry ingestion container runs on Azure Container Apps with User-Assigned Managed Identity `uami-plc-ingest`. Which T-SQL command inside `TelemetryDB` grants passwordless authentication: `CREATE USER [uami-plc-ingest] FROM ____;`?

Domain: Implement a secure environment

- A. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`)
- D. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database

### 18. You create a server-level Microsoft Entra login in `master` on SQL Managed Instance via `CREATE LOGIN [SG-Plant-DBAs] FROM ____;`. Which clause authenticates Entra identities at the instance scope on SQL MI and SQL Server 2022?

Domain: Implement a secure environment

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`)
- C. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- D. Remap orphaned database users (`ALTER USER [u] WITH LOGIN = [u]`) and inspect explicit `DENY` permissions via `sys.database_permissions`

### 19. A plant reliability dashboard service needs to read `sys.dm_os_performance_counters` and `sys.dm_hadr_fabric_replica_states` on SQL Server 2022 without holding `VIEW SERVER SECURITY STATE` or `sysadmin`. Which SQL 2022 granular server permission applies: `GRANT VIEW SERVER ____ STATE TO [svc_dash];`?

Domain: Implement a secure environment

- A. Built-in granular server-level roles (`##MS_ServerStateReader##`, `##MS_DefinitionReader##`) or `GRANT VIEW DATABASE PERFORMANCE STATE`
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Row-Level Security (`CREATE SECURITY POLICY`) binding a `SCHEMABINDING` inline TVF as both `FILTER PREDICATE` and `BLOCK PREDICATE`

### 20. Warehouse scanners invoke `Inventory.usp_AdjustBinQty` to update `Inventory.StockBins`. Both objects belong to schema `Inventory` owned by `dbo`. If you grant `EXECUTE ON Inventory.usp_AdjustBinQty TO [RoleScanners]` and grant **zero** permissions on `Inventory.StockBins`, what happens when `[RoleScanners]` calls the procedure?

Domain: Implement a secure environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Stored procedure encapsulation using schema ownership chaining, `EXECUTE AS OWNER`, or certificate module signing

### 21. Supplier procurement analysts have ad-hoc `SELECT` rights on `Suppliers` and must be cryptographically prevented from reading plaintext `UnitBidCost` on disk or inferring costs via `WHERE UnitBidCost BETWEEN 10 AND 12`. Proposed solution: Add `MASKED WITH (FUNCTION = 'default()')` on `UnitBidCost` only. Does the solution meet the goal?

Domain: Implement a secure environment

- A. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server
- B. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- C. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- D. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference

### 22. You configure Customer-Managed Key (`CMK`) Transparent Data Encryption on `sqlmi-foundrygrid` using Azure Key Vault. Which two Key Vault configurations are mandatory? Select two.

Domain: Implement a secure environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Grant the SQL server Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) on the Key Vault
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Enable both `Soft Delete` and `Purge Protection` on the Azure Key Vault or Managed HSM storing the TDE protector key
- E. Configure `None` Azure host caching on dedicated managed disks hosting `.ldf` SQL Server transaction log files

### 23. Which DMV on SQL Server 2022, Azure SQL Database, and SQL Managed Instance reports `encryption_state` (`3 = Encrypted`, `2 = Encryption in progress`), `percent_complete`, and `encryptor_thumbprint` for TDE: `SELECT db_name(database_id), encryption_state, percent_complete FROM sys.____`?

Domain: Implement a secure environment

- A. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server

### 24. A SaaS quality-inspection vendor connects from IP `192.0.2.88` to `QualityDB` on `sql-anvilpeak-east`, which replicates to `sql-anvilpeak-west`. Proposed solution: Add `192.0.2.88` as a server-level firewall rule on `sql-anvilpeak-east` only and take no action on `sql-anvilpeak-west` or inside `QualityDB`. Does the solution survive regional failover?

Domain: Implement a secure environment

- A. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- B. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- C. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- D. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server

### 25. HR is encrypting `Employees.SalaryBand` and `Employees.TaxIdentifier` in-place on Azure SQL Database using VBS secure enclaves so payroll stored procedures can run `<` and `>` comparisons securely. Which four-step workflow applies?

Domain: Implement a secure environment

- A. Grant Azure SQL DBA `unwrapKey` on CMK inside T-SQL → Decrypt column via server stored procedure → Apply Dynamic Data Masking → Enable VBS enclave
- B. Run in-place column encryption first → Create non-enclave CEK without ENCLAVE_COMPUTATIONS → Store plaintext CMK inside sys.configurations → Enable VBS enclave last
- C. Enable VBS enclave on Azure SQL Database → Provision Key Vault CMK & enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`) → Grant client Key Vault key permissions & attestation → Run in-place `ALTER TABLE` encryption
- D. Disable TLS on client connection string → Set `Column Encryption Setting=Disabled` → Create Deterministic CEK without CMK → Run `LIKE` wildcard queries

### 26. An R&D patent database uses Always Encrypted with secure enclaves so engineers can run `LIKE '%alloy%'` pattern searches over encrypted `FormulaCode` values. Which two configurations must be present? Select two.

Domain: Implement a secure environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Configure `ReadOnly` Azure host caching on Premium SSD data disks hosting `.mdf` and `.ndf` database files
- D. Enable `Column Encryption Setting=Enabled` and pass the `Enclave Attestation Url` (or VBS zero-attestation setting) in client drivers
- E. Provision a Column Master Key in Key Vault and create a Column Encryption Key with `ENCLAVE_COMPUTATIONS` enabled

### 27. OT/ICS cybersecurity standards forbid any public internet endpoint on `sql-weldcore.database.windows.net` and require plant gateways over ExpressRoute to connect via Private Link. Which two configurations complete this lockdown? Select two.

Domain: Implement a secure environment

- A. Switch eligible hybrid SQL Server instances to hourly Azure Arc pay-as-you-go billing instead of upfront core licenses
- B. Link Private DNS Zone `privatelink.database.windows.net` (or forward on-premises DNS) to resolve `<server>.database.windows.net` to the private IP
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Set `Public network access = Disabled` (`publicNetworkAccess: Disabled`) on the logical SQL server so internet connections are rejected
- E. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script

### 28. When connecting plant applications in `vnet-hub` to an Azure SQL Managed Instance deployed inside `snet-sqlmi` (`vnet-spoke`), which endpoint and port handles internal VNet application TDS connections by default?

Domain: Implement a secure environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Virtual Network Service Endpoints (`Microsoft.Sql`) with outbound storage firewall rules, or dedicated `/28+` delegated subnet for SQL MI
- C. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 29. Export-control ITAR auditors require classifying `PartBlueprints.ExportClassification` as `Highly Confidential` via T-SQL and logging every `SELECT` against it to an immutable Storage Account. Which two features work together to deliver this?

Domain: Implement a secure environment

- A. SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage
- B. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history

### 30. On a SQL Server 2022 Azure VM writing native SQL Server Audit `.sqlaudit` files to disk or Blob storage, which built-in table-valued function reads `.sqlaudit` binary files inside T-SQL: `SELECT event_time, statement FROM sys.____('D:\Audit\*.sqlaudit', DEFAULT, DEFAULT)`?

Domain: Implement a secure environment

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 31. An offline warehouse handheld scanner syncs changed `PartMaster` rows every morning using SQL Change Tracking (`ALTER DATABASE ERP SET CHANGE_TRACKING = ON (CHANGE_RETENTION = 7 DAYS, AUTO_CLEANUP = ON)`). What happens if a scanner stays offline for **12 days** before syncing?

Domain: Implement a secure environment

- A. Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history
- B. Enable Change Data Capture (`CDC`) on DTU `Basic`/`S0–S2` databases or expect Change Tracking (`CT`) to retain every intermediate `UPDATE` value
- C. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 32. Temp line supervisors query `Workers.HourlyWage` (`DECIMAL(10,2)`) and should see a randomized wage between `15.00` and `25.00` instead of `0.00` so test screens look realistic. Which Dynamic Data Masking function achieves this: `ADD MASKED WITH (FUNCTION = '____(15, 25)')`?

Domain: Implement a secure environment

- A. Always Encrypted with VBS or Intel SGX secure enclaves (`ALLOW_ENCLAVE_COMPUTATIONS` + `Column Encryption Setting=Enabled`)
- B. Row-Level Security (`CREATE SECURITY POLICY`) binding a `SCHEMABINDING` inline TVF as both `FILTER PREDICATE` and `BLOCK PREDICATE`
- C. Transparent Data Encryption (TDE) with a Customer-Managed Key (`CMK`) in Azure Key Vault (`Soft Delete` + `Purge Protection`)
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 33. Contract manufacturers share a `WorkOrders` table (`SupplierOrgId`) in Azure SQL Database. Which three Row-Level Security components guarantee each contract manufacturer can only view and modify its own `SupplierOrgId` rows? Select three.

Domain: Implement a secure environment

- A. Truncate or `DELETE` historical rows from an append-only Ledger table (`LEDGER = ON (APPEND_ONLY = ON)`) to purge audit history in place
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Add a `FILTER PREDICATE` in `CREATE SECURITY POLICY` to hide non-matching rows silently from `SELECT`, `UPDATE`, and `DELETE`
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- E. Add `AFTER INSERT` and `AFTER UPDATE` / `BEFORE UPDATE` `BLOCK PREDICATE` clauses in `CREATE SECURITY POLICY` (`STATE = ON`)
- F. Create an inline table-valued function `WITH SCHEMABINDING` evaluating `SESSION_CONTEXT()` or `DATABASE_PRINCIPAL_ID()`

### 34. You are deploying Row-Level Security on `Manufacturing.BatchLots` so pooled shop-floor API sessions using `SESSION_CONTEXT(N'PlantCode')` cannot read or write sibling factory lots. Which four-step sequence applies?

Domain: Implement a secure environment

- A. Create `SECURITY POLICY` with `STATE = ON` first → Create multi-statement TVF without `SCHEMABINDING` → Grant tenants `ALTER ANY SECURITY POLICY` → Store `TenantId` in a global temp table
- B. Create non-schema-bound scalar UDF → Attach UDF to `sys.sp_set_firewall_rule` → Enable Change Tracking → Set `SESSION_CONTEXT` with `@read_only = 0` so users can switch tenants
- C. Apply `ADD MASKED WITH (FUNCTION = 'default()')` on `TenantId` → Create `AFTER INSERT` trigger → Grant `UNMASK` to shared app login → Expect row filtering
- D. Create dedicated `Security` schema → Create `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT(N'TenantId')` → Create `SECURITY POLICY` with `FILTER` & `BLOCK` predicates (`STATE = ON`) → Set read-only `sp_set_session_context` on connect

### 35. On `AnvilPeak`'s SQL Server 2022 Windows VM, you build a PerfMon storage baseline before ERP go-live. Which PerfMon counter measures average milliseconds per physical disk read transfer on the `.mdf` volume (healthy `< 5–10 ms` on Premium SSD): `PhysicalDisk: ____`?

Domain: Monitor, configure, and optimize database resources

- A. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- B. Azure Monitor metrics paired with `sys.dm_db_resource_stats` (single DB) or `sys.server_resource_stats` (SQL MI) for 15-second CPU, data I/O, log write, and memory baselines
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 36. On SQL Server 2022, `Page life expectancy` (`PLE`) is often misinterpreted alone. Pairing `PLE` with `Buffer cache hit ratio`, `Memory Grants Pending`, and `PAGEIOLATCH_SH` waits reveals memory pressure accurately when which symptom appears?

Domain: Monitor, configure, and optimize database resources

- A. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Azure Monitor metrics paired with `sys.dm_db_resource_stats` (single DB) or `sys.server_resource_stats` (SQL MI) for 15-second CPU, data I/O, log write, and memory baselines
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 37. You stream metrics and logs from 30 plant Azure SQL Databases into Log Analytics and build an Azure Monitor Workbook visualizing p95 CPU, `tempdb` percent, and deadlock spikes across plants. Which feature exports those platform logs continuously without running T-SQL pollers?

Domain: Monitor, configure, and optimize database resources

- A. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- B. Azure Monitor Diagnostic Settings streaming `SQLInsights`, `QueryStoreRuntimeStatistics`, `Errors`, and `Blocks` to a Log Analytics workspace (`KQL`)
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server

### 38. You are setting up `database watcher` to monitor manufacturing Azure SQL Databases and Elastic Pools into a Fabric Eventhouse KQL database. Which four-step workflow provisions the solution?

Domain: Monitor, configure, and optimize database resources

- A. Install third-party kernel drivers inside Azure SQL Database PaaS OS → Configure SMB share on domain controller → Export `.trc` files via `sp_trace_create` → Query via MDX
- B. Create database watcher targeting Azure Cosmos DB for Gremlin → Store metrics in Azure Table storage → Authenticate via anonymous public SAS → Query dashboards via Gremlin
- C. Provision Azure Data Explorer or Fabric Eventhouse store → Create database watcher with Managed Identity → Add SQL targets & grant `VIEW SERVER PERFORMANCE STATE` + ingest roles → Start watcher & open portal dashboards
- D. Start database watcher before selecting data store or SQL targets → Grant `sysadmin` via blank-password `sa` login → Store time-series telemetry in Azure Queue Storage → Enable SQL Profiler trace

### 39. Your manufacturing monitoring team configures least-privilege permissions for `database watcher` streaming SQL MI metrics into Fabric Eventhouse (while planning transition to Database Hub in Fabric before April 30, 2027). Which two role grants are required? Select two.

Domain: Monitor, configure, and optimize database resources

- A. Grant the database watcher Managed Identity `VIEW SERVER PERFORMANCE STATE` (or `VIEW DATABASE PERFORMANCE STATE`) on SQL targets
- B. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- E. Grant the database watcher Managed Identity database `Admin` / ingest permissions on the Azure Data Explorer or Fabric Eventhouse store

### 40. You must record persistent `.xel` Extended Events traces for `attention` (client command timeout) events on `TelemetryDB` in Azure SQL Database. Which two steps are required? Select two.

Domain: Monitor, configure, and optimize database resources

- A. Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE` with `rwl` permissions) for the Azure Blob container
- B. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- C. Define `CREATE EVENT SESSION ... ON DATABASE ADD TARGET package0.event_file(SET filename = N'https://...xel')` and start the session
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- E. Enable both `Soft Delete` and `Purge Protection` on the Azure Key Vault or Managed HSM storing the TDE protector key

### 41. When defining an Extended Events session to capture slow T-SQL batches (`sql_batch_completed`) with minimal overhead on a 15,000-TPS ERP server, where should you place the `WHERE duration > 5000000` (5-second) filter?

Domain: Monitor, configure, and optimize database resources

- A. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Extended Events (`CREATE EVENT SESSION ... ON DATABASE` in SQL DB or `ON SERVER` in SQL MI/VMs) writing to an `event_file` target in Azure Blob Storage

### 42. A closed-source shop-floor MES binary runs an unindexed `MAXDOP 0` query saturating all 64 vCores during shift changes. Which two Query Store stored procedures let a DBA cap its parallelism or force a serial plan without changing the MES binary? Select two.

Domain: Monitor, configure, and optimize database resources

- A. Execute `sys.sp_query_store_force_plan @query_id, @plan_id` to pin the historical low-latency execution plan immediately
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Execute `sys.sp_query_store_set_hints @query_id, N'OPTION (RECOMPILE)'` (or `MAXDOP` / memory grant hints) without redeploying code
- E. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 43. A BOM explosion stored procedure regresses from 18 ms to 9,400 ms after an atypical single-part run poisoned the cached plan. Which four-step Query Store workflow restores the 18 ms plan cleanly?

Domain: Monitor, configure, and optimize database resources

- A. Set Query Store `OPERATION_MODE = READ_ONLY` → Modify `sys.query_store_plan` system catalog via `UPDATE` → Run `DBCC FREEPROCCACHE` every minute → Disable statistics
- B. Run `ALTER DATABASE ... SET QUERY_STORE CLEAR ALL` first → Inspect Regressed Queries history → Force new regressed plan ID → Set `OPERATION_MODE = OFF`
- C. Confirm Query Store is `READ_WRITE` with wait capture → Compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`) → Force prior plan via `sp_query_store_force_plan` → Monitor `force_failure_count` & latency
- D. Restart SQL Server production instance during peak traffic → Rebuild every index with `ONLINE = OFF` → Enable `AUTO_CLOSE = ON` → Check Query Store

### 44. On `AnvilPeak`'s SQL Server 2022 VM (`READ_COMMITTED_SNAPSHOT = OFF` inherited from SQL 2008), BOM `SELECT` reports block behind MRP `UPDATE` runs on `LCK_M_S`. Before enabling `ALTER DATABASE ERP SET READ_COMMITTED_SNAPSHOT ON WITH ROLLBACK IMMEDIATE`, which subsystem capacity must you verify?

Domain: Monitor, configure, and optimize database resources

- A. Read Committed Snapshot Isolation (`READ_COMMITTED_SNAPSHOT = ON`) combined with Optimized Locking (`TID` locking + Lock After Qualification `LAQ`)
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 45. Two assembly-line threads update `WorkOrders` and `SerialNumbers` concurrently and occasionally deadlock. One thread is an interactive operator kiosk and the other is a retryable background sync job (`SET ____ LOW;`). Which session setting ensures the background sync job is chosen as the deadlock victim first?

Domain: Monitor, configure, and optimize database resources

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- C. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- D. Capture `xml_deadlock_report` via Extended Events or `sys.event_log`, align table modification order across transactions, and add covering indexes

### 46. On `AnvilPeak`'s 64-vCore SQL Server VM, `PAGELATCH_EX` and `PAGELATCH_UP` (note: **not** `PAGEIOLATCH`) spike on database ID `2` (`2:1:1`, `2:1:2`, `2:1:3` PFS/GAM/SGAM pages). What classic bottleneck do `2:1:*` `PAGELATCH_*` waits indicate?

Domain: Monitor, configure, and optimize database resources

- A. Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7

### 47. Which DMV joined to `sys.dm_db_missing_index_group_stats` displays equality columns, inequality columns, and suggested `INCLUDE` columns—and why shouldn't you blindly create every index listed in it?

Domain: Monitor, configure, and optimize database resources

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- D. Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`

### 48. A bill-of-materials query filters `WHERE PartCode + '-' + Revision = @full_sku`, forcing an `Index Scan` across 25M rows despite a composite index on `(PartCode, Revision)`. How should you rewrite the `WHERE` predicate?

Domain: Monitor, configure, and optimize database resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions
- C. Replace set-based `JOIN` queries with nested `FAST_FORWARD` T-SQL cursors calling multi-statement table-valued functions per row under compat `100`
- D. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon

### 49. You compare two candidate T-SQL rewrites in SSMS using `SET STATISTICS IO, TIME ON;` and Actual Execution Plans. Query A finishes in 90 ms with `logical reads 420`; Query B finishes in 85 ms from warm cache with `logical reads 185,000` (`CPU time = 640 ms` across 8 threads). Which query scales better under 200 concurrent users and why?

Domain: Monitor, configure, and optimize database resources

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- C. Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`)
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 50. In an execution plan, a `Sort` operator consumes 76% of query cost solely to satisfy `SELECT DISTINCT` on a join between `Orders` and `OrderLines` where the developer only wanted orders that have at least one line. Which T-SQL rewrite eliminates both row multiplication and the expensive `Sort`?

Domain: Monitor, configure, and optimize database resources

- A. Transparent Data Encryption (TDE) with a Customer-Managed Key (`CMK`) in Azure Key Vault (`Soft Delete` + `Purge Protection`)
- B. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`)

### 51. After loading 40 million new rows into today's `ProductionRuns` partition (`5%` of a 900M-row table), the optimizer still estimates `1 row` for today's date because the global 20%-change auto-stats threshold hasn't fired yet (on older settings) or stats lag. Which targeted command refreshes histogram steps fast?

Domain: Monitor, configure, and optimize database resources

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Fragmentation-aware index maintenance (`REORGANIZE` 5–30%, `REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` >30%), `UPDATE STATISTICS`, and `DBCC CHECKDB WITH PHYSICAL_ONLY`
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 52. You query `SELECT name, desired_state_desc, actual_state_desc, reason_desc FROM sys.database_automatic_tuning_options` on Azure SQL Database and see `FORCE_LAST_GOOD_PLAN` has `desired_state_desc = ON` while `actual_state_desc = OFF` and `reason_desc = QUERY_STORE_OFF`. How do you fix this?

Domain: Monitor, configure, and optimize database resources

- A. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`)
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 53. On `AnvilPeak`'s `E64bds_v5` VM (`64 vCores`, `512 GB RAM`, 2 NUMA nodes of 32 cores) running SQL Server 2022 alongside a monitoring agent, why must you explicitly cap `sp_configure 'max server memory (MB)'` below `512 GB` (e.g., `~460,000 MB`) and set `MAXDOP = 8`?

Domain: Monitor, configure, and optimize database resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Configure `cost threshold for parallelism`, `MAXDOP`, `max server memory (MB)`, and Resource Governor (`WORKLOAD GROUP` + `RESOURCE POOL` + classifier UDF) on SQL MI / VMs
- D. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching

### 54. A plant historian database on SQL Managed Instance experiences occasional long plan-compilation stalls on a complex 28-table view, and you enable `ALTER DATABASE SCOPED CONFIGURATION SET ____ = ON;` in SQL 2022 / Azure SQL to store replayable compilation optimization scripts in Query Store. Which feature is this?

Domain: Monitor, configure, and optimize database resources

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Use `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`, `OPTIMIZED_PLAN_FORCING`) per database
- C. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 55. You manage 12 SQL Server 2022 VMs across four factories and want to define standard nightly backup and `CHECKDB` SQL Agent jobs once on a central Master Server (`MSX`) and push them automatically to all 11 Target Servers (`TSX`). Which built-in SQL Server Agent feature provides this?

Domain: Configure and manage automation of tasks

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators
- D. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo

### 56. In Database Mail on SQL Server 2022 VMs, you configure a primary SMTP relay (`smtp-pri.turbinespan.internal`) and a secondary failover SMTP relay (`smtp-dr.turbinespan.internal`) so operator alerts still send if `smtp-pri` goes down. How does a Database Mail **Profile** achieve SMTP failover?

Domain: Configure and manage automation of tasks

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators
- D. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7

### 57. SQL Server Agent alerts fail to send emails after enabling an Alert->Operator notification on a freshly installed SQL Server 2022 VM, even though `sp_send_dbmail` test emails succeed manually! Which checkbox in `SQL Server Agent Properties -> Alert System` was forgotten followed by restarting SQL Agent?

Domain: Configure and manage automation of tasks

- A. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- B. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- C. Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries
- D. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 58. A SQL Server Agent job launched at 01:00 is still showing `Executing` at 09:00 (`hung`), whereas `msdb.dbo.sysjobhistory` only logs completed runs. Which stored procedure or table in `msdb` shows currently running active Agent sessions: `EXEC msdb.dbo.____`?

Domain: Configure and manage automation of tasks

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries
- D. Transparent Data Encryption (TDE) with a Customer-Managed Key (`CMK`) in Azure Key Vault (`Soft Delete` + `Purge Protection`)

### 59. To allow an ARM or Bicep deployment to pull a secret reference directly from Azure Key Vault `kv-turbinespan-prod` during `az deployment group create`, which property must be enabled on the Key Vault access configuration: `enabledFor____: true`?

Domain: Configure and manage automation of tasks

- A. Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`
- B. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 60. You automate creating a point-in-time test clone of production `MES_Prod` onto the same logical server via Azure CLI: `az sql db ____ -g rg-plant -s sql-plant -n MES_Prod --dest-name MES_PerfTest --service-objective GP_Gen5_8`. Which `az sql db` subcommand creates an online transactionally consistent copy?

Domain: Configure and manage automation of tasks

- A. Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`)
- B. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- C. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- D. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 61. Your PowerShell runbook registers a newly provisioned IaaS SQL Server VM with the SQL VM resource provider in Full mode: `____ -ResourceGroupName "rg-erp" -Name "vm-erp01" -Location "westeurope" -LicenseType "AHUB" -SqlManagementType "Full"`. Which `Az.SqlVirtualMachine` cmdlet performs this registration?

Domain: Configure and manage automation of tasks

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`)
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 62. A GitHub Actions Bicep deployment creating `sql-plant-prod` fails with `ServerNameAlreadyExists` even though no server by that name exists in your resource group or subscription. Why did this failure occur?

Domain: Configure and manage automation of tasks

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 63. An automated deployment pipeline needs a foreign-key-consistent `.bacpac` snapshot of an active 500-writes/sec factory `OrdersDB` every evening. Proposed solution: Run `SqlPackage /Action:Export` directly against the active read-write `OrdersDB` endpoint without creating a temporary `az sql db copy` first. Does the solution meet the goal?

Domain: Configure and manage automation of tasks

- A. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- B. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server
- C. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- D. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement

### 64. You deploy an Azure SQL Elastic Job Agent to run index maintenance across 28 regional supplier Azure SQL Databases using User-Assigned Managed Identity (`UAMI`). Which four-step workflow configures the agent?

Domain: Configure and manage automation of tasks

- A. Create Elastic Job Agent on Basic tier DB → Run `jobs.sp_add_job` before creating Target Group → Authenticate across servers with Windows NTLM local accounts → Schedule via `msdb.dbo.sp_add_job`
- B. Provision Elastic Job Agent inside Azure Blob Storage → Store plaintext admin password in Git repo → Add Cosmos DB containers to Target Group → Trigger via `DBCC SHRINKDATABASE`
- C. Create S1+ Job Database & Elastic Job Agent with UAMI → Create contained UAMI user on target DBs with needed permissions → Define Target Group (`jobs.sp_add_target_group_member`) → Add T-SQL steps & schedule (`jobs.sp_add_job`)
- D. Enable SQL Server Agent inside single Azure SQL Database → Create linked servers to 480 tenant DBs → Loop synchronously inside a scalar UDF → Grant `CONTROL SERVER` to `guest`

### 65. You add an Elastic Pool `pool-suppliers` to an Elastic Job Target Group, yet you want **one** specific read-only archive database `SupplierArchive2020` inside that pool skipped during nightly DDL jobs. How do you exclude a single database from a pool-targeted Elastic Job?

Domain: Configure and manage automation of tasks

- A. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- B. Azure SQL Database Elastic Job Agent (`jobs.sp_add_job`) authenticating to Target Groups across servers/pools via a User-Assigned Managed Identity (`UAMI`)
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 66. To avoid paying 24x7 compute for a 4-node non-production SQL Server 2022 QA VM cluster (`vm-qa-sql01..04`), you want to stop (`Deallocate`) the VMs every weekday at 20:00 and start them at 06:30 in strict sequence (`Witness/DC -> Node1 -> Node2`). Which Azure service orchestrates this cleanly?

Domain: Configure and manage automation of tasks

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Azure Automation PowerShell / Python runbooks (or Azure Functions / Logic Apps) using a System-Assigned Managed Identity on a recurring schedule

### 67. A plant analytics team runs heavy Python ETL scripts against a single Azure SQL Database (`GP_Gen5_8`) and wants to cap ETL memory grants via Resource Governor. Proposed solution: Trigger an Azure Function that runs `CREATE RESOURCE POOL PoolETL` inside that single Azure SQL Database. Does the solution meet the goal?

Domain: Configure and manage automation of tasks

- A. No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases
- B. No — transaction log managed disks on SQL Server Azure VMs must use host caching `None`, never `ReadOnly` or `ReadWrite`
- C. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- D. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement

### 68. An Elastic Job step fails on 4 out of 28 supplier databases with `Login failed for user '<token-identified principal>'`. What was missed on those 4 target databases?

Domain: Configure and manage automation of tasks

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Configure Azure Monitor Metric / Log Alert rules routed to Action Groups and query `jobs.job_executions` in the Elastic Job database to diagnose step failures
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7

### 69. A factory safety-compliance Azure SQL Database in West Europe requires automatic cross-region failover to North Europe (`RPO <= 5s`, `RTO <= 1h` SLA) if West Europe suffers a regional outage. Which feature meets this requirement?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- B. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- C. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- D. Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`)

### 70. An IoT staging database in Azure SQL Database General Purpose needs intra-region resilience against a single Availability Zone power failure with `RPO = 0` and without changing service tier to Business Critical. Proposed solution: Enable `Zone Redundant` compute and `ZRS` storage on General Purpose vCore. Does the solution meet the goal?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server
- B. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- C. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- D. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement

### 71. A German robotics plant runs SQL Server 2022 Enterprise on-premises for sub-millisecond PLC latency and maintains a warm cloud DR replica in Azure SQL Managed Instance in Germany West Central. Which technology supports online planned failover to Azure and online failback to the plant?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- B. Hybrid DR using Managed Instance link with bidirectional online failover between SQL Server 2022 and Azure SQL Managed Instance
- C. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- D. Expect online bidirectional planned failback from Azure SQL Managed Instance directly back to on-premises SQL Server 2016 without downtime

### 72. Annual ISO-22301 business-continuity audits require demonstrating a zero-data-loss regional failover and failback of four coupled MES Azure SQL Databases. Which four-step Failover Group drill procedure applies?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Execute unplanned `AllowDataLoss` forced failover during peak checkout → Create secondary logical SQL server afterward → Hardcode regional server names in app connection strings → Skip firewall rules on secondary
- B. Export nightly `.bacpac` to local laptop → Delete production database to test restore → Manually edit 50 microservice connection strings → Re-enable TDE after 6 hours
- C. Create Failover Group between two servers in the exact same datacenter rack → Add `tempdb` and `master` to Failover Group → Point OLTP writes to `.secondary.database.windows.net` → Disable Geo-Replication
- D. Provision secondary SQL server with matching firewall/Private Link & Entra admin → Create Failover Group with coupled DBs → Point apps to `<fog>.database.windows.net` & `.secondary` → Run planned `Switch-AzSqlDatabaseFailoverGroup` drill

### 73. You want to test how an application behaves when a SQL Server 2022 Always On Availability Group fails over on Azure VMs **without** losing uncommitted transactions. Which T-SQL command on the synchronized secondary replica performs a planned zero-data-loss manual failover: `ALTER AVAILABILITY GROUP [AG_ERP] ____;`?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Non-disruptive DR readiness drill executing a planned zero-data-loss Failover Group switch (`Switch-AzSqlDatabaseFailoverGroup`), validating app listeners, and failing back
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 74. Your SQL Server 2022 VM backup schedule runs Full backups Sundays 01:00, Differentials Mon–Sat 01:00, and Log backups every 15 minutes. Proposed solution: On Tuesday 14:00, an engineer exports a standard `BACKUP DATABASE [ERP] TO DISK = 'N:\Adhoc.bak'` (omitting `COPY_ONLY`) and deletes `Adhoc.bak` an hour later. Does Wednesday's Differential still restore onto Sunday's Full backup?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- B. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server
- C. No — taking an ad-hoc non-`COPY_ONLY` full backup resets the differential base and breaks downstream differential restores
- D. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement

### 75. When protecting SQL Server 2022 on Azure VMs with Azure Backup Recovery Services Vault, what happens if a DBA also leaves a separate third-party VSS backup agent scheduled on the same VM without `COPY_ONLY`?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Use `BACKUP DATABASE ... WITH COPY_ONLY` for ad-hoc exports on SQL MI / AGs, and Azure Backup Recovery Services Vault SQL-aware policies (`15-min` log RPO) on SQL VMs
- C. Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access
- D. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching

### 76. A developer accidentally truncates `QualityInspections` at `08:30 UTC` on Azure SQL Managed Instance. You run Point-in-Time Restore to `08:29 UTC` creating `MES_Recovered` on the **same** or a **different** SQL Managed Instance. Is cross-instance PITR supported on SQL Managed Instance?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- D. Set Short-Term PITR retention to `3,650` days (`10 years`) and grant developers Subscription Contributor to prevent backup deletion

### 77. On SQL Server 2022 Azure VMs, a single runaway `DELETE` statement ran for 3 hours before filling 85% of the transaction log. With `ALTER DATABASE ERP SET ACCELERATED_DATABASE_RECOVERY = ON` enabled beforehand, why didn't the transaction log grow to 100%?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 78. Automotive product-liability regulations require retaining annual SQL backups for 10 years with locked WORM protection against insider deletion. Which two Azure SQL Long-Term Retention (`LTR`) settings satisfy this requirement? Select two.

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Configure an Azure SQL Long-Term Retention (`LTR`) policy (`WeeklyRetention`, `MonthlyRetention`, `YearlyRetention`, `WeekOfYear`) up to 10 years
- B. Set Short-Term PITR retention to `3,650` days (`10 years`) and grant developers Subscription Contributor to prevent backup deletion
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- E. Enable and lock time-based immutability (`WORM`) on the LTR backup policy so nobody can shorten retention or delete compliance backups early

### 79. If a production Azure SQL Database lives in a single-region datacenter with strict data-residency laws forbidding any cross-border data replication to a paired geo-region, which `--backup-storage-redundancy` value keeps automated and LTR backups strictly inside the primary region?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- B. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- C. Set Short-Term PITR retention to `3,650` days (`10 years`) and grant developers Subscription Contributor to prevent backup deletion
- D. Long-Term Retention (`LTR`) weekly/monthly/yearly backups up to `10 years` protected by a locked time-based immutable (`WORM`) policy and `RA-GRS` / `ZRS` backup storage

### 80. On `AnvilPeak`'s 12 TB ERP SQL Server 2022 Azure VM, you script native T-SQL `BACKUP DATABASE` directly to Azure Blob Storage over high-throughput networking without SAS token rotation. Which two steps are required? Select two.

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access
- C. Stripe `BACKUP DATABASE` across multiple `TO URL = 'https://...bak'` block blob targets with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`
- D. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- E. Create a SQL Server `CREDENTIAL` (`IDENTITY = 'Managed Identity'` or `'SHARED ACCESS SIGNATURE'`) matching the Azure Blob container URL

### 81. Before restoring a production database on a SQL Server 2022 VM after storage failure while the `.ldf` file on `L:` is still intact, which critical final backup must you take first (`BACKUP LOG [ERP] TO URL = '...' WITH ____`) to capture committed transactions since the last 15-minute log backup?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- B. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- C. Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access
- D. Striped T-SQL `BACKUP DATABASE ... TO URL = ...` across up to 64 block blobs (`MAXTRANSFERSIZE`, `COMPRESSION`) authenticated via `Managed Identity` or `SHARED ACCESS SIGNATURE` Credential

### 82. An Azure SQL Database uses Active Geo-Replication to replicate `PartsCatalogDB` from West Europe to East US for low-latency North American reads. If you manually fail over `PartsCatalogDB` via `Set-AzSqlDatabaseSecondary -Failover`, what must application connection strings do when **no** Failover Group exists?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. Failover Groups for automatic multi-database failover behind stable `<fog>.database.windows.net` / `.secondary` listeners vs Active Geo-Replication for up to 4 readable secondaries
- D. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica

### 83. In Azure SQL Database, can a Failover Group contain databases from **different** Elastic Pools on the same primary logical SQL server?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Failover Groups for automatic multi-database failover behind stable `<fog>.database.windows.net` / `.secondary` listeners vs Active Geo-Replication for up to 4 readable secondaries
- B. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica

### 84. You deploy a 2-node SQL Server 2022 Always On Availability Group across two Azure Availability Zones in different subnets (`10.50.1.0/24` and `10.50.2.0/24`). Which two configurations prevent split-brain quorum loss and 21-second TCP reconnect timeouts? Select two.

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG
- C. Configure an Azure Cloud Witness in a standard Storage Account (`LRS`/`ZRS`) to provide lightweight quorum voting for a 2-node WSFC
- D. Deploy a Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` TCP `59999`) listener and set `MultiSubnetFailover=True` on clients
- E. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching

### 85. In SQL Server 2022 Enterprise Edition, a legacy plant app modifies SQL Agent jobs and SQL logins yet connects through an Always On Availability Group listener. Which **new SQL Server 2022** AG feature replicates `master`/`msdb`-like logins, permissions, and Agent jobs inside the AG itself: `CREATE AVAILABILITY GROUP ... WITH (____)`?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`
- B. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG

### 86. Which two shared-storage options does Microsoft officially support for deploying a multi-zone Windows SQL Server Always On Failover Cluster Instance (`FCI`) on Azure Virtual Machines without third-party SAN software?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- B. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas
- C. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- D. Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`)

### 87. During a Log Shipping restore job with `WITH STANDBY`, active BI queries holding locks on the secondary database prevent the 15-minute `.trn` restore from acquiring exclusive database access. Which Log Shipping secondary option resolves this cleanly?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`)
- C. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- D. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled

### 88. On a SQL Server 2022 Always On Availability Group, `sys.dm_hadr_database_replica_states` shows `synchronization_state_desc = 'NOT SYNCHRONIZING'` and `is_suspended = 1` (`suspend_reason_desc = 'SUSPEND_FROM_USER'`) on the secondary database after a disk expansion. Which T-SQL command resumes data movement: `ALTER DATABASE [ERP] SET HADR ____;`?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Query `sys.dm_hadr_database_replica_states` (`synchronization_state_desc`, `log_send_queue_size`, `redo_queue_size`) and `sys.dm_geo_replication_link_status`, plus verify NSG probe port `59999`
- B. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

---

## Case study — AnvilPeak Robotics

AnvilPeak Robotics deploys a 12 TB ERP database on SQL Server 2022 Enterprise on an Azure `E64bds_v5` VM. Storage architects must optimize host caching and disk layout across OS, data, transaction log, and `tempdb` volumes while automating OS/SQL cumulative updates inside strict Sunday maintenance windows.

The next 3 questions refer to **AnvilPeak Robotics**. Read the scenario brief once, then answer each item independently.

### 89. Which management extension and patching service automate Windows and SQL Server 2022 cumulative updates strictly inside Sunday maintenance windows on the `E64bds_v5` VM?

Domain: Plan and implement data platform resources

- A. SQL IaaS Agent Extension in Full management mode paired with Azure Update Manager / Automated Patching
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- D. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled

### 90. Which three storage and caching configurations should storage architects apply across the `E64bds_v5` VM's data, transaction log, and `tempdb` volumes? Select three.

Domain: Plan and implement data platform resources

- A. Configure `None` Azure host caching on dedicated managed disks hosting `.ldf` SQL Server transaction log files
- B. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- E. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- F. Configure `ReadOnly` Azure host caching on Premium SSD data disks hosting `.mdf` and `.ndf` database files

### 91. When restoring the 12 TB ERP database onto the `E64bds_v5` VM, `.mdf` creation takes 45 minutes zero-initializing 12 TB of space while `.ldf` still zero-initializes normally. Which Windows security policy skips `.mdf`/`.ndf` zero-initialization safely?

Domain: Plan and implement data platform resources

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Grant `Perform volume maintenance tasks` (Instant File Initialization) and `Lock pages in memory` to the SQL Server service account
- C. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

---

## Case study — FoundryGrid Supply

FoundryGrid Supply joins legacy `.NET` plant clients that require integrated Windows Kerberos authentication to Azure SQL Managed Instance without deploying AD Domain Controllers in Azure, restores on-premises `.bak` files whose SQL users lose login mappings, and encrypts vendor IBAN columns.

The next 3 questions refer to **FoundryGrid Supply**. Read the scenario brief once, then answer each item independently.

### 92. How do you enable legacy `.NET` plant clients to connect to Azure SQL Managed Instance using integrated Windows Kerberos authentication without deploying AD Domain Controllers in Azure?

Domain: Implement a secure environment

- A. Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or `Entra Kerberos`)
- B. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 93. After restoring on-premises `.bak` files onto SQL Managed Instance, legacy SQL database users exist in `sys.database_principals` yet fail login mapping because SIDs differ. Which query identifies orphaned SQL users and which command repairs them?

Domain: Implement a secure environment

- A. Remap orphaned database users (`ALTER USER [u] WITH LOGIN = [u]`) and inspect explicit `DENY` permissions via `sys.database_permissions`
- B. Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 94. Plant legacy ERP stored procedures must encrypt and decrypt `VendorIBAN` columns directly inside T-SQL without upgrading 200 shop-floor client drivers for Always Encrypted. Which encryption approach works inside T-SQL?

Domain: Implement a secure environment

- A. Column-level encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey`) plus `Minimal TLS version = 1.2`
- B. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

---

## Case study — TurbineSpan Plant Ops

TurbineSpan Plant Ops provisions Azure SQL environments through GitHub Actions Bicep pipelines without exposing administrator secrets, needs immediate email alerts whenever severity 19–25 fatal SQL engine errors occur on SQL Server VMs, and runs a 2-node multi-subnet Always On Availability Group in Azure.

The next 3 questions refer to **TurbineSpan Plant Ops**. Read the scenario brief once, then answer each item independently.

### 95. Which two SQL Server Agent configurations notify plant DBAs immediately by email on fatal severity `19–25` engine errors while running PowerShell maintenance steps without `sysadmin`? Select two.

Domain: Configure and manage automation of tasks

- A. Create a Windows/SQL Credential and map it to a SQL Server Agent Subsystem Proxy (`CmdExec` / `PowerShell`) instead of granting `sysadmin`
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- E. Configure Database Mail, define an Agent Operator, and create SQL Server Agent Alerts for Severity `19–25` and Errors `823`, `824`, and `825`

### 96. Which two Bicep and GitHub Actions practices ensure Azure SQL deployments never expose administrator secrets and preview infrastructure changes before applying them? Select two.

Domain: Configure and manage automation of tasks

- A. Mark sensitive parameters with `@secure()` in Bicep and pass Key Vault secret references from the parameter file rather than cleartext values
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- E. Run `az deployment group what-if` (or `New-AzResourceGroupDeployment -WhatIf`) as a pull-request gate before applying template changes

### 97. What two-node cluster and listener architecture enables sub-second multi-subnet failover for the Always On Availability Group across two Azure subnets without Internal Load Balancer probe latency?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- D. Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`

---

## Case study — WeldCore Telemetry

WeldCore Telemetry stores 4.2 billion sensor rows in Azure SQL Database. Queries aggregate 90-day sensor trends while rarely touching partitions older than two years, 600 GB clustered index rebuilds regularly exceed 90-minute maintenance windows, and legacy T-SQL scalar UDFs serialize CPU execution.

The next 3 questions refer to **WeldCore Telemetry**. Read the scenario brief once, then answer each item independently.

### 98. Queries aggregating 90-day sensor trends (`SELECT SensorType, AVG(TempC) FROM Readings WHERE ReadingUTC >= DATEADD(day, -90, SYSUTCDATETIME()) GROUP BY SensorType`) run over 4.2 billion rows. Why does a date-ordered Clustered Columnstore Index excel here?

Domain: Monitor, configure, and optimize database resources

- A. Replace set-based `JOIN` queries with nested `FAST_FORWARD` T-SQL cursors calling multi-statement table-valued functions per row under compat `100`
- B. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- C. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- D. Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions

### 99. 600 GB clustered index rebuilds exceed the 90-minute maintenance window and previously rolled back completely when killed. Proposed solution: Run `ALTER INDEX CCI_OR_PK ON ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON, MAX_DURATION = 90 MINUTES)` so work pauses cleanly at 90 minutes and resumes next window. Does the solution meet the goal?

Domain: Monitor, configure, and optimize database resources

- A. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- B. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- C. No — transaction log managed disks on SQL Server Azure VMs must use host caching `None`, never `ReadOnly` or `ReadWrite`
- D. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement

### 100. Upgrading the telemetry database to compatibility level `160` eliminates row-by-row scalar T-SQL UDF bottlenecks (`INLINE = ON`) alongside two other flagship IQP capabilities. Which three IQP features belong to this `compat 150/160` family? Select three.

Domain: Monitor, configure, and optimize database resources

- A. Leverage Percentile and Persistence Memory Grant Feedback (`compat 160`) to eliminate recurring `tempdb` sort/hash spills and wasted RAM
- B. Leverage Scalar UDF Inlining (`compat 150+`) so eligible T-SQL scalar functions fold into relational subqueries enabling parallel plans
- C. Replace set-based `JOIN` queries with nested `FAST_FORWARD` T-SQL cursors calling multi-statement table-valued functions per row under compat `100`
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- E. Leverage Parameter Sensitive Plan (`PSP`) optimization under compatibility level `160` to cache separate plans for skewed parameter sizes
- F. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

---

## Answer key and explanations

### Question 1 — B

Answer: SQL Server on Azure Virtual Machines (`Ebdsv5` series) with full OS and engine version control. SQL Server on Azure Virtual Machines (IaaS) supports NTFS FileStream, custom Windows OLE DB third-party drivers for Linked Servers, and co-hosted SSIS packages under full OS control. SQL Server on Azure VMs (IaaS) provides full OS access, custom third-party drivers, legacy SQL Server version pinning, SSIS/SSRS/SSAS co-hosting, and `Ebdsv5` high remote storage throughput. Local study-map skill 1.1 (Recommend an Azure SQL Offering (SQL Database, SQL Managed Instance, or SQL Server on Azure VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Compare Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview).

- **A:** Incorrect for this requirement. Elastic Pools share a pooled vCore/storage envelope across many multi-tenant databases with staggered peaks while capping per-database max vCores to stop noisy-neighbor starvation. Why the keyed choice wins: SQL Server on Azure Virtual Machines (IaaS) supports NTFS FileStream, custom Windows OLE DB third-party drivers for Linked Servers, and co-hosted SSIS packages under full OS control.
- **B:** Correct. SQL Server on Azure VMs (IaaS) provides full OS access, custom third-party drivers, legacy SQL Server version pinning, SSIS/SSRS/SSAS co-hosting, and `Ebdsv5` high remote storage throughput. In this scenario: SQL Server on Azure Virtual Machines (IaaS) supports NTFS FileStream, custom Windows OLE DB third-party drivers for Linked Servers, and co-hosted SSIS packages under full OS control.
- **C:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: SQL Server on Azure Virtual Machines (IaaS) supports NTFS FileStream, custom Windows OLE DB third-party drivers for Linked Servers, and co-hosted SSIS packages under full OS control.
- **D:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: SQL Server on Azure Virtual Machines (IaaS) supports NTFS FileStream, custom Windows OLE DB third-party drivers for Linked Servers, and co-hosted SSIS packages under full OS control.

### Question 2 — D

Answer: Azure SQL Managed Instance (Next-gen General Purpose) with decoupled IOPS and storage sliders. Azure SQL Managed Instance (General Purpose / Next-gen General Purpose) delivers managed PaaS operations alongside SQL Agent, Database Mail, and native cross-database queries. SQL Managed Instance provides near-100% SQL Server engine compatibility (cross-DB queries, SQL Agent, CLR, Service Broker), and Next-gen GP scales IOPS independently of storage up to 500 DBs. Local study-map skill 1.1 (Recommend an Azure SQL Offering (SQL Database, SQL Managed Instance, or SQL Server on Azure VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Compare Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview).

- **A:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Azure SQL Managed Instance (General Purpose / Next-gen General Purpose) delivers managed PaaS operations alongside SQL Agent, Database Mail, and native cross-database queries.
- **B:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Azure SQL Managed Instance (General Purpose / Next-gen General Purpose) delivers managed PaaS operations alongside SQL Agent, Database Mail, and native cross-database queries.
- **C:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: Azure SQL Managed Instance (General Purpose / Next-gen General Purpose) delivers managed PaaS operations alongside SQL Agent, Database Mail, and native cross-database queries.
- **D:** Correct. SQL Managed Instance provides near-100% SQL Server engine compatibility (cross-DB queries, SQL Agent, CLR, Service Broker), and Next-gen GP scales IOPS independently of storage up to 500 DBs. In this scenario: Azure SQL Managed Instance (General Purpose / Next-gen General Purpose) delivers managed PaaS operations alongside SQL Agent, Database Mail, and native cross-database queries.

### Question 3 — D, E

Answers: Create a dedicated VNet subnet (`/28` or larger) with no other cloud resources and delegate it to `Microsoft.Sql/managedInstances`; Associate a User-Defined Route (`UDR`) table (`0.0.0.0/0` -> `Internet` for management plane) and required NSG rules with the SQL MI subnet. Provision an empty `/28+` subnet delegated exclusively to `Microsoft.Sql/managedInstances`, and attach a compliant User-Defined Route (`UDR`) table and NSG. Local study-map skill 1.2 (Choose Automated Deployment Methods and Deploy SQL Offerings Across Windows, Linux, and Containers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated deployment options for Azure SQL and SQL Server on Linux/containers (https://learn.microsoft.com/en-us/azure/azure-sql/database/arm-templates-content-guide).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Provision an empty `/28+` subnet delegated exclusively to `Microsoft.Sql/managedInstances`, and attach a compliant User-Defined Route (`UDR`) table and NSG.
- **B:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Provision an empty `/28+` subnet delegated exclusively to `Microsoft.Sql/managedInstances`, and attach a compliant User-Defined Route (`UDR`) table and NSG.
- **C:** Incorrect for this requirement. Azure Arc allows variable-workload or seasonal SQL Server hosts outside Azure to be billed hourly through an Azure subscription. Why the keyed choice wins: Provision an empty `/28+` subnet delegated exclusively to `Microsoft.Sql/managedInstances`, and attach a compliant User-Defined Route (`UDR`) table and NSG.
- **D:** Correct. SQL Managed Instance requires an explicit route table and NSG bound to its delegated subnet so Azure management traffic is never blackholed by forced tunneling. In this scenario: Provision an empty `/28+` subnet delegated exclusively to `Microsoft.Sql/managedInstances`, and attach a compliant User-Defined Route (`UDR`) table and NSG.
- **E:** Correct. Azure SQL Managed Instance requires an exclusive subnet delegated to `Microsoft.Sql/managedInstances` sized for current and future instance vCore/node counts. In this scenario: Provision an empty `/28+` subnet delegated exclusively to `Microsoft.Sql/managedInstances`, and attach a compliant User-Defined Route (`UDR`) table and NSG.

### Question 4 — B

Answer: Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`. `Microsoft.SqlVirtualMachine/sqlVirtualMachines` registers the compute VM with the SQL VM resource provider to manage licensing, patching, backups, and storage pools declaratively. Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. Local study-map skill 1.2 (Choose Automated Deployment Methods and Deploy SQL Offerings Across Windows, Linux, and Containers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated deployment options for Azure SQL and SQL Server on Linux/containers (https://learn.microsoft.com/en-us/azure/azure-sql/database/arm-templates-content-guide).

- **A:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: `Microsoft.SqlVirtualMachine/sqlVirtualMachines` registers the compute VM with the SQL VM resource provider to manage licensing, patching, backups, and storage pools declaratively.
- **B:** Correct. Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. In this scenario: `Microsoft.SqlVirtualMachine/sqlVirtualMachines` registers the compute VM with the SQL VM resource provider to manage licensing, patching, backups, and storage pools declaratively.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: `Microsoft.SqlVirtualMachine/sqlVirtualMachines` registers the compute VM with the SQL VM resource provider to manage licensing, patching, backups, and storage pools declaratively.
- **D:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: `Microsoft.SqlVirtualMachine/sqlVirtualMachines` registers the compute VM with the SQL VM resource provider to manage licensing, patching, backups, and storage pools declaratively.

### Question 5 — A, B

Answers: Authenticate applications and users exclusively with Microsoft Entra ID identities, service principals, or workspace roles; Query automatically replicated OneLake Delta Parquet tables and the read-only SQL analytics endpoint from Spark and Direct Lake. SQL database in Microsoft Fabric uses Microsoft Entra-only authentication and automatically mirrors operational tables as OneLake Delta Parquet with a read-only SQL analytics endpoint. Local study-map skill 1.3 (Identify Use Cases for SQL Server Enabled by Azure Arc and SQL Database in Microsoft Fabric), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server enabled by Azure Arc and SQL database in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/database/sql/overview).

- **A:** Correct. Every SQL database in Microsoft Fabric automatically mirrors operational tables into OneLake in Delta Parquet format and exposes a SQL analytics endpoint. In this scenario: SQL database in Microsoft Fabric uses Microsoft Entra-only authentication and automatically mirrors operational tables as OneLake Delta Parquet with a read-only SQL analytics endpoint.
- **B:** Correct. SQL database in Microsoft Fabric relies exclusively on Microsoft Entra authentication and workspace/item permissions rather than SQL logins. In this scenario: SQL database in Microsoft Fabric uses Microsoft Entra-only authentication and automatically mirrors operational tables as OneLake Delta Parquet with a read-only SQL analytics endpoint.
- **C:** Incorrect for this requirement. SQL database in Microsoft Fabric enforces Microsoft Entra authentication exclusively (SQL logins are unsupported) and manages backups/OneLake mirroring automatically as SaaS. Why the keyed choice wins: SQL database in Microsoft Fabric uses Microsoft Entra-only authentication and automatically mirrors operational tables as OneLake Delta Parquet with a read-only SQL analytics endpoint.
- **D:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: SQL database in Microsoft Fabric uses Microsoft Entra-only authentication and automatically mirrors operational tables as OneLake Delta Parquet with a read-only SQL analytics endpoint.
- **E:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: SQL database in Microsoft Fabric uses Microsoft Entra-only authentication and automatically mirrors operational tables as OneLake Delta Parquet with a read-only SQL analytics endpoint.

### Question 6 — C

Answer: SQL Server enabled by Azure Arc (`Microsoft.AzureArcData/sqlServerInstances`). Azure Arc-enabled servers `Run Command` and Azure Resource Graph let DBAs execute compliance/configuration queries and run automated SQL Best Practices Assessments centrally across all 16 plants. Azure Arc projects on-premises and multicloud SQL Server instances into Azure for Resource Graph inventory, automated Best Practices Assessments, Entra auth (SQL 2022+), Defender, and PAYG billing. Local study-map skill 1.3 (Identify Use Cases for SQL Server Enabled by Azure Arc and SQL Database in Microsoft Fabric), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server enabled by Azure Arc and SQL database in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/database/sql/overview).

- **A:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Azure Arc-enabled servers `Run Command` and Azure Resource Graph let DBAs execute compliance/configuration queries and run automated SQL Best Practices Assessments centrally across all 16 plants.
- **B:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Azure Arc-enabled servers `Run Command` and Azure Resource Graph let DBAs execute compliance/configuration queries and run automated SQL Best Practices Assessments centrally across all 16 plants.
- **C:** Correct. Azure Arc projects on-premises and multicloud SQL Server instances into Azure for Resource Graph inventory, automated Best Practices Assessments, Entra auth (SQL 2022+), Defender, and PAYG billing. In this scenario: Azure Arc-enabled servers `Run Command` and Azure Resource Graph let DBAs execute compliance/configuration queries and run automated SQL Best Practices Assessments centrally across all 16 plants.
- **D:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: Azure Arc-enabled servers `Run Command` and Azure Resource Graph let DBAs execute compliance/configuration queries and run automated SQL Best Practices Assessments centrally across all 16 plants.

### Question 7 — C

Answer: SPLIT partition function for incoming future boundary → Create empty staging table on same filegroup with matching schema/indexes → ALTER TABLE ... SWITCH oldest partition to staging → Archive staging data & MERGE retired boundary. Split the new future boundary first, create an index- and filegroup-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary. Sliding-window partitioning splits a new empty future range first, performs a metadata-only `ALTER TABLE ... SWITCH` into an aligned staging table, and merges the retired boundary. Local study-map skill 1.4 (Plan for Table Partitioning (`RANGE RIGHT` / `SWITCH`) and Horizontal Database Sharding (`ShardMapManager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Table partitioning and scaling out with Azure SQL Database sharding (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-scale-introduction).

- **A:** Incorrect for this requirement. Incorrect workflow: row-by-row `DELETE` bloats the transaction log and locks tables, and `SWITCH` fails if the staging table resides on a different filegroup or lacks aligned indexes. Why the keyed choice wins: Split the new future boundary first, create an index- and filegroup-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary.
- **B:** Incorrect for this requirement. Incorrect workflow: `SWITCH` is strictly an intra-database metadata operation requiring identical schema, filegroup alignment, and trusted constraints—never cross-database. Why the keyed choice wins: Split the new future boundary first, create an index- and filegroup-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary.
- **C:** Correct. Sliding-window partitioning splits a new empty future range first, performs a metadata-only `ALTER TABLE ... SWITCH` into an aligned staging table, and merges the retired boundary. In this scenario: Split the new future boundary first, create an index- and filegroup-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary.
- **D:** Incorrect for this requirement. Incorrect workflow: `ALTER TABLE ... SWITCH` swaps metadata between two tables in the same database/filegroup rather than writing directly to Azure Blob Storage. Why the keyed choice wins: Split the new future boundary first, create an index- and filegroup-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary.

### Question 8 — A

Answer: Table partitioning using `CREATE PARTITION FUNCTION ... AS RANGE RIGHT` with aligned indexes and `ALTER TABLE ... SWITCH`. SQL Server metadata-only `SWITCH` swaps entire physical partition B-trees in milliseconds only when the table and **all** of its nonclustered indexes are partition-aligned on the same partition function. `RANGE RIGHT` places each upper-boundary date value cleanly as the lower bound of its own monthly/daily partition, enabling metadata-only `SWITCH` archival when indexes are aligned. Local study-map skill 1.4 (Plan for Table Partitioning (`RANGE RIGHT` / `SWITCH`) and Horizontal Database Sharding (`ShardMapManager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Table partitioning and scaling out with Azure SQL Database sharding (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-scale-introduction).

- **A:** Correct. `RANGE RIGHT` places each upper-boundary date value cleanly as the lower bound of its own monthly/daily partition, enabling metadata-only `SWITCH` archival when indexes are aligned. In this scenario: SQL Server metadata-only `SWITCH` swaps entire physical partition B-trees in milliseconds only when the table and **all** of its nonclustered indexes are partition-aligned on the same partition function.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: SQL Server metadata-only `SWITCH` swaps entire physical partition B-trees in milliseconds only when the table and **all** of its nonclustered indexes are partition-aligned on the same partition function.
- **C:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: SQL Server metadata-only `SWITCH` swaps entire physical partition B-trees in milliseconds only when the table and **all** of its nonclustered indexes are partition-aligned on the same partition function.
- **D:** Incorrect for this requirement. `ListShardMap` maps discrete `TenantId` keys and `RangeShardMap` maps contiguous ID spans to independent Azure SQL Databases, routing data-dependent connections directly from the app tier. Why the keyed choice wins: SQL Server metadata-only `SWITCH` swaps entire physical partition B-trees in milliseconds only when the table and **all** of its nonclustered indexes are partition-aligned on the same partition function.

### Question 9 — A

Answer: SQL Server on Linux configured via `mssql-conf` or Linux container images for consistent CI/CD dev-test parity. By default on Linux, SQL Server stores system databases and diagnostic logs (`errorlog`, `.xel` health files) under `/var/opt/mssql` (`/var/opt/mssql/log`). `mssql-conf` configures memory, trace flags, Entra auth, and HA on Linux SQL Server VMs, while official Linux container images spin up fast disposable SQL instances in CI pipelines. Local study-map skill 1.5 (Deploy Hybrid SQL Server Solutions and Manage Patching (`SQL IaaS Agent Extension` & `Azure Update Manager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server IaaS Agent Extension, Automated Patching, and Azure Update Manager (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-agent-extension-manually-register-single-vm).

- **A:** Correct. `mssql-conf` configures memory, trace flags, Entra auth, and HA on Linux SQL Server VMs, while official Linux container images spin up fast disposable SQL instances in CI pipelines. In this scenario: By default on Linux, SQL Server stores system databases and diagnostic logs (`errorlog`, `.xel` health files) under `/var/opt/mssql` (`/var/opt/mssql/log`).
- **B:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: By default on Linux, SQL Server stores system databases and diagnostic logs (`errorlog`, `.xel` health files) under `/var/opt/mssql` (`/var/opt/mssql/log`).
- **C:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: By default on Linux, SQL Server stores system databases and diagnostic logs (`errorlog`, `.xel` health files) under `/var/opt/mssql` (`/var/opt/mssql/log`).
- **D:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: By default on Linux, SQL Server stores system databases and diagnostic logs (`errorlog`, `.xel` health files) under `/var/opt/mssql` (`/var/opt/mssql/log`).

### Question 10 — B

Answer: Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled. Azure SQL Database vCore Serverless (`MinVCore = 2`, `MaxVCore = 16`, `AutoPauseDelay = 60 minutes`) scales dynamically during CAD runs and pauses compute billing completely when idle. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Local study-map skill 1.6 (Configure Azure SQL Database for Scale and Performance (`Serverless`, `Hyperscale` Named Replicas, `Elastic Pools`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure SQL Database vCore, Serverless, Hyperscale, and Elastic Pools (https://learn.microsoft.com/en-us/azure/azure-sql/database/service-tiers-vcore).

- **A:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Azure SQL Database vCore Serverless (`MinVCore = 2`, `MaxVCore = 16`, `AutoPauseDelay = 60 minutes`) scales dynamically during CAD runs and pauses compute billing completely when idle.
- **B:** Correct. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. In this scenario: Azure SQL Database vCore Serverless (`MinVCore = 2`, `MaxVCore = 16`, `AutoPauseDelay = 60 minutes`) scales dynamically during CAD runs and pauses compute billing completely when idle.
- **C:** Incorrect for this requirement. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. Why the keyed choice wins: Azure SQL Database vCore Serverless (`MinVCore = 2`, `MaxVCore = 16`, `AutoPauseDelay = 60 minutes`) scales dynamically during CAD runs and pauses compute billing completely when idle.
- **D:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: Azure SQL Database vCore Serverless (`MinVCore = 2`, `MaxVCore = 16`, `AutoPauseDelay = 60 minutes`) scales dynamically during CAD runs and pauses compute billing completely when idle.

### Question 11 — B

Answer: Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica. In-Memory OLTP (`MEMORY_OPTIMIZED_DATA` filegroups) requires the Business Critical service tier in Azure SQL Database and Azure SQL Managed Instance. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. Local study-map skill 1.7 (Configure Azure SQL Managed Instance for Scale and Performance (`Next-gen GP` Sliders & `Business Critical`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure SQL Managed Instance service tiers and Next-gen General Purpose scaling (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview).

- **A:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: In-Memory OLTP (`MEMORY_OPTIMIZED_DATA` filegroups) requires the Business Critical service tier in Azure SQL Database and Azure SQL Managed Instance.
- **B:** Correct. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. In this scenario: In-Memory OLTP (`MEMORY_OPTIMIZED_DATA` filegroups) requires the Business Critical service tier in Azure SQL Database and Azure SQL Managed Instance.
- **C:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: In-Memory OLTP (`MEMORY_OPTIMIZED_DATA` filegroups) requires the Business Critical service tier in Azure SQL Database and Azure SQL Managed Instance.
- **D:** Incorrect for this requirement. SQL Managed Instance provides near-100% SQL Server engine compatibility (cross-DB queries, SQL Agent, CLR, Service Broker), and Next-gen GP scales IOPS independently of storage up to 500 DBs. Why the keyed choice wins: In-Memory OLTP (`MEMORY_OPTIMIZED_DATA` filegroups) requires the Business Critical service tier in Azure SQL Database and Azure SQL Managed Instance.

### Question 12 — B

Answer: Evaluate `sp_estimate_data_compression_savings` and apply `ROW`, `PAGE`, or `COLUMNSTORE_ARCHIVE` compression per partition. Rebuilding only historical partitions (`PARTITION = 1 TO 24`) with `DATA_COMPRESSION = COLUMNSTORE_ARCHIVE` applies extra XPRESS archival compression to cold partitions while keeping active 90-day partitions on standard `COLUMNSTORE`. `sp_estimate_data_compression_savings` models space gains before compressing; `ROW`/`PAGE` shrink OLTP B-trees while `COLUMNSTORE` / `COLUMNSTORE_ARCHIVE` achieves up to 10x analytics compression. Local study-map skill 1.9 (Configure Table Partitioning Alignment and Data Compression (`ROW`, `PAGE`, `COLUMNSTORE`, `COLUMNSTORE_ARCHIVE`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure table partitioning and row/page/columnstore data compression (https://learn.microsoft.com/en-us/sql/relational-databases/data-compression/data-compression).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Rebuilding only historical partitions (`PARTITION = 1 TO 24`) with `DATA_COMPRESSION = COLUMNSTORE_ARCHIVE` applies extra XPRESS archival compression to cold partitions while keeping active 90-day partitions on standard `COLUMNSTORE`.
- **B:** Correct. `sp_estimate_data_compression_savings` models space gains before compressing; `ROW`/`PAGE` shrink OLTP B-trees while `COLUMNSTORE` / `COLUMNSTORE_ARCHIVE` achieves up to 10x analytics compression. In this scenario: Rebuilding only historical partitions (`PARTITION = 1 TO 24`) with `DATA_COMPRESSION = COLUMNSTORE_ARCHIVE` applies extra XPRESS archival compression to cold partitions while keeping active 90-day partitions on standard `COLUMNSTORE`.
- **C:** Incorrect for this requirement. Row-by-row cursors and multi-statement TVFs under legacy compatibility levels execute thousands of iterative context switches and 1-row cardinality guesses. Why the keyed choice wins: Rebuilding only historical partitions (`PARTITION = 1 TO 24`) with `DATA_COMPRESSION = COLUMNSTORE_ARCHIVE` applies extra XPRESS archival compression to cold partitions while keeping active 90-day partitions on standard `COLUMNSTORE`.
- **D:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Rebuilding only historical partitions (`PARTITION = 1 TO 24`) with `DATA_COMPRESSION = COLUMNSTORE_ARCHIVE` applies extra XPRESS archival compression to cold partitions while keeping active 90-day partitions on standard `COLUMNSTORE`.

### Question 13 — B

Answer: Azure Migrate (`Azure SQL` assessment) and the Azure SQL Migration extension for Azure Data Studio / VS Code. Use Azure Migrate (`Azure SQL` assessment) or the Azure SQL Migration extension in Azure Data Studio / VS Code (which replaced retired Data Migration Assistant `DMA`). Following Data Migration Assistant (DMA) retirement, Azure Migrate and the Azure SQL Migration extension assess compatibility blockers, feature parity, and performance-based vCore SKU right-sizing. Local study-map skill 1.10 (Evaluate Migration Requirements, Offline vs Online Strategies, and SKU Sizing via Azure Migrate & ADS), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Assess and plan SQL Server migrations using Azure Migrate and Azure SQL Migration extension (https://learn.microsoft.com/en-us/data-migration/sql-server/managed-instance/overview).

- **A:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Use Azure Migrate (`Azure SQL` assessment) or the Azure SQL Migration extension in Azure Data Studio / VS Code (which replaced retired Data Migration Assistant `DMA`).
- **B:** Correct. Following Data Migration Assistant (DMA) retirement, Azure Migrate and the Azure SQL Migration extension assess compatibility blockers, feature parity, and performance-based vCore SKU right-sizing. In this scenario: Use Azure Migrate (`Azure SQL` assessment) or the Azure SQL Migration extension in Azure Data Studio / VS Code (which replaced retired Data Migration Assistant `DMA`).
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Use Azure Migrate (`Azure SQL` assessment) or the Azure SQL Migration extension in Azure Data Studio / VS Code (which replaced retired Data Migration Assistant `DMA`).
- **D:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Use Azure Migrate (`Azure SQL` assessment) or the Azure SQL Migration extension in Azure Data Studio / VS Code (which replaced retired Data Migration Assistant `DMA`).

### Question 14 — A

Answer: Log Replay Service (`LRS`) streaming Full, Differential, and Tail-Log backups from Azure Blob Storage into SQL Managed Instance. Log Replay Service (`LRS`, `Start-AzSqlInstanceDatabaseLogReplay`) continuously replays Full, Differential, and Transaction Log `.bak`/`.trn` backups from Azure Blob Storage over HTTPS without requiring TCP `5022` VNet peering. `Start-AzSqlInstanceDatabaseLogReplay` continuously replays `.bak`/`.trn` files from Blob storage until `Complete-AzSqlInstanceDatabaseLogReplay` restores the final tail-log backup. Local study-map skill 1.11 (Implement Online and Offline Migrations to and Between Azure SQL Services (`MI Link`, `LRS`, `SqlPackage` Copy)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Online and offline SQL migrations with Managed Instance link, Log Replay Service, and SqlPackage (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-feature-overview).

- **A:** Correct. `Start-AzSqlInstanceDatabaseLogReplay` continuously replays `.bak`/`.trn` files from Blob storage until `Complete-AzSqlInstanceDatabaseLogReplay` restores the final tail-log backup. In this scenario: Log Replay Service (`LRS`, `Start-AzSqlInstanceDatabaseLogReplay`) continuously replays Full, Differential, and Transaction Log `.bak`/`.trn` backups from Azure Blob Storage over HTTPS without requiring TCP `5022` VNet peering.
- **B:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Log Replay Service (`LRS`, `Start-AzSqlInstanceDatabaseLogReplay`) continuously replays Full, Differential, and Transaction Log `.bak`/`.trn` backups from Azure Blob Storage over HTTPS without requiring TCP `5022` VNet peering.
- **C:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: Log Replay Service (`LRS`, `Start-AzSqlInstanceDatabaseLogReplay`) continuously replays Full, Differential, and Transaction Log `.bak`/`.trn` backups from Azure Blob Storage over HTTPS without requiring TCP `5022` VNet peering.
- **D:** Incorrect for this requirement. Managed Instance link online failback from SQL MI to SQL Server requires SQL Server 2022 or later; SQL Server 2016 and 2019 support one-way migration into SQL MI only. Why the keyed choice wins: Log Replay Service (`LRS`, `Start-AzSqlInstanceDatabaseLogReplay`) continuously replays Full, Differential, and Transaction Log `.bak`/`.trn` backups from Azure Blob Storage over HTTPS without requiring TCP `5022` VNet peering.

### Question 15 — A

Answer: Verify VNet peering & TCP 5022 + 11000-11999 rules → Start online Database Move from source to target SQL MI → Wait for seeding to reach Ready for completion → Complete move within 24 hours so target comes online. Verify VNet peering and TCP `5022` + `11000–11999` NSG rules, start the online Database Move, wait for `Ready for completion`, and complete the move within 24 hours. Online SQL MI database move requires bidirectional TCP 5022 and 11000–11999 connectivity, seeds asynchronously until Ready for completion, and must be manually completed within 24 hours. Local study-map skill 1.12 (Implement Azure SQL Managed Instance Online Database Copy and Move (`24h` Completion, `TCP 5022`/`11000-11999`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Copy or move a database online across Azure SQL Managed Instances (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/database-copy-move-how-to).

- **A:** Correct. Online SQL MI database move requires bidirectional TCP 5022 and 11000–11999 connectivity, seeds asynchronously until Ready for completion, and must be manually completed within 24 hours. In this scenario: Verify VNet peering and TCP `5022` + `11000–11999` NSG rules, start the online Database Move, wait for `Ready for completion`, and complete the move within 24 hours.
- **B:** Incorrect for this requirement. Incorrect workflow: `sp_detach_db` is unsupported in Azure SQL Managed Instance and online Database Move replicates via Always On availability group seeding without stopping compute. Why the keyed choice wins: Verify VNet peering and TCP `5022` + `11000–11999` NSG rules, start the online Database Move, wait for `Ready for completion`, and complete the move within 24 hours.
- **C:** Incorrect for this requirement. Incorrect workflow: network ports must be open before seeding, operations uncompleted after 24 hours auto-cancel, and source PITR history never transfers with a moved database. Why the keyed choice wins: Verify VNet peering and TCP `5022` + `11000–11999` NSG rules, start the online Database Move, wait for `Ready for completion`, and complete the move within 24 hours.
- **D:** Incorrect for this requirement. Incorrect workflow: `.bacpac` files are stored in Blob storage rather than Table storage, the completion window is 24 hours, and Move removes the source DB upon completion. Why the keyed choice wins: Verify VNet peering and TCP `5022` + `11000–11999` NSG rules, start the online Database Move, wait for `Ready for completion`, and complete the move within 24 hours.

### Question 16 — C

Answer: Enable Microsoft Entra-only authentication (`azuread_authentication_only`) on the logical SQL server or SQL Managed Instance. Configuring Microsoft Entra authentication and enabling Microsoft Entra-only authentication disables Mixed Mode SQL password logins completely. Microsoft Entra-only authentication disables legacy SQL Server logins (`sa` and password auth) completely, enforcing centralized MFA, Conditional Access, and token-based Managed Identities. Local study-map skill 2.1 (Configure Microsoft Entra ID and Microsoft Entra-Only Authentication Across SQL DB, SQL MI, and SQL Server), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure and manage Microsoft Entra authentication with Azure SQL and SQL Server (https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Configuring Microsoft Entra authentication and enabling Microsoft Entra-only authentication disables Mixed Mode SQL password logins completely.
- **B:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Configuring Microsoft Entra authentication and enabling Microsoft Entra-only authentication disables Mixed Mode SQL password logins completely.
- **C:** Correct. Microsoft Entra-only authentication disables legacy SQL Server logins (`sa` and password auth) completely, enforcing centralized MFA, Conditional Access, and token-based Managed Identities. In this scenario: Configuring Microsoft Entra authentication and enabling Microsoft Entra-only authentication disables Mixed Mode SQL password logins completely.
- **D:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Configuring Microsoft Entra authentication and enabling Microsoft Entra-only authentication disables Mixed Mode SQL password logins completely.

### Question 17 — C

Answer: Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`). Executing `CREATE USER [uami-plc-ingest] FROM EXTERNAL PROVIDER` creates a contained Entra principal mapped to the Managed Identity's client/object ID. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. Local study-map skill 2.1 (Configure Microsoft Entra ID and Microsoft Entra-Only Authentication Across SQL DB, SQL MI, and SQL Server), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure and manage Microsoft Entra authentication with Azure SQL and SQL Server (https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview).

- **A:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Executing `CREATE USER [uami-plc-ingest] FROM EXTERNAL PROVIDER` creates a contained Entra principal mapped to the Managed Identity's client/object ID.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Executing `CREATE USER [uami-plc-ingest] FROM EXTERNAL PROVIDER` creates a contained Entra principal mapped to the Managed Identity's client/object ID.
- **C:** Correct. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. In this scenario: Executing `CREATE USER [uami-plc-ingest] FROM EXTERNAL PROVIDER` creates a contained Entra principal mapped to the Managed Identity's client/object ID.
- **D:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Executing `CREATE USER [uami-plc-ingest] FROM EXTERNAL PROVIDER` creates a contained Entra principal mapped to the Managed Identity's client/object ID.

### Question 18 — B

Answer: Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`). `FROM EXTERNAL PROVIDER` creates server-level logins in `master` on SQL MI / SQL Server 2022 as well as contained database users inside user databases. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. Local study-map skill 2.3 (Configure Security Principals and Portable Contained Microsoft Entra Users (`FROM EXTERNAL PROVIDER`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Contained database users and Microsoft Entra security principals in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: `FROM EXTERNAL PROVIDER` creates server-level logins in `master` on SQL MI / SQL Server 2022 as well as contained database users inside user databases.
- **B:** Correct. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. In this scenario: `FROM EXTERNAL PROVIDER` creates server-level logins in `master` on SQL MI / SQL Server 2022 as well as contained database users inside user databases.
- **C:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: `FROM EXTERNAL PROVIDER` creates server-level logins in `master` on SQL MI / SQL Server 2022 as well as contained database users inside user databases.
- **D:** Incorrect for this requirement. Restoring a `.bak` onto another instance mismatches login SIDs (fixed via `ALTER USER ... WITH LOGIN`), while an explicit table/schema `DENY` always overrides `db_datareader` role `GRANT`s. Why the keyed choice wins: `FROM EXTERNAL PROVIDER` creates server-level logins in `master` on SQL MI / SQL Server 2022 as well as contained database users inside user databases.

### Question 19 — A

Answer: Built-in granular server-level roles (`##MS_ServerStateReader##`, `##MS_DefinitionReader##`) or `GRANT VIEW DATABASE PERFORMANCE STATE`. SQL Server 2022 split `VIEW SERVER STATE` into `VIEW SERVER PERFORMANCE STATE` and `VIEW SERVER SECURITY STATE`, allowing monitoring tools to read performance DMVs under stricter least privilege. Modern granular server roles and state permissions let monitoring accounts inspect DMVs and metadata without granting `sysadmin`, `db_owner`, or `SELECT` access to user tables. Local study-map skill 2.3 (Configure Security Principals and Portable Contained Microsoft Entra Users (`FROM EXTERNAL PROVIDER`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Contained database users and Microsoft Entra security principals in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage).

- **A:** Correct. Modern granular server roles and state permissions let monitoring accounts inspect DMVs and metadata without granting `sysadmin`, `db_owner`, or `SELECT` access to user tables. In this scenario: SQL Server 2022 split `VIEW SERVER STATE` into `VIEW SERVER PERFORMANCE STATE` and `VIEW SERVER SECURITY STATE`, allowing monitoring tools to read performance DMVs under stricter least privilege.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: SQL Server 2022 split `VIEW SERVER STATE` into `VIEW SERVER PERFORMANCE STATE` and `VIEW SERVER SECURITY STATE`, allowing monitoring tools to read performance DMVs under stricter least privilege.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: SQL Server 2022 split `VIEW SERVER STATE` into `VIEW SERVER PERFORMANCE STATE` and `VIEW SERVER SECURITY STATE`, allowing monitoring tools to read performance DMVs under stricter least privilege.
- **D:** Incorrect for this requirement. RLS transparently filters `SELECT`/`UPDATE`/`DELETE` rows via `FILTER PREDICATE` and blocks unauthorized cross-tenant `INSERT`/`UPDATE` writes via `BLOCK PREDICATE` inside the engine. Why the keyed choice wins: SQL Server 2022 split `VIEW SERVER STATE` into `VIEW SERVER PERFORMANCE STATE` and `VIEW SERVER SECURITY STATE`, allowing monitoring tools to read performance DMVs under stricter least privilege.

### Question 20 — D

Answer: Stored procedure encapsulation using schema ownership chaining, `EXECUTE AS OWNER`, or certificate module signing. Because `Inventory.usp_AdjustBinQty` and `Inventory.StockBins` share the exact same owner (`dbo`), unbroken ownership chaining skips permission checks on `Inventory.StockBins` and the `UPDATE` succeeds cleanly. Granting `EXECUTE` on a schema-owned or certificate-signed stored procedure lets callers run controlled DML/DDL workflows without direct table-level `SELECT`, `UPDATE`, or `IMPERSONATE` rights. Local study-map skill 2.4 (Apply Least Privilege Using Granular Server/Database Roles, Schema Chaining, `EXECUTE AS`, and T-SQL/GUI Tools), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Permissions hierarchy, server-level roles, and principle of least privilege in SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/security-server-roles).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Because `Inventory.usp_AdjustBinQty` and `Inventory.StockBins` share the exact same owner (`dbo`), unbroken ownership chaining skips permission checks on `Inventory.StockBins` and the `UPDATE` succeeds cleanly.
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Because `Inventory.usp_AdjustBinQty` and `Inventory.StockBins` share the exact same owner (`dbo`), unbroken ownership chaining skips permission checks on `Inventory.StockBins` and the `UPDATE` succeeds cleanly.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Because `Inventory.usp_AdjustBinQty` and `Inventory.StockBins` share the exact same owner (`dbo`), unbroken ownership chaining skips permission checks on `Inventory.StockBins` and the `UPDATE` succeeds cleanly.
- **D:** Correct. Granting `EXECUTE` on a schema-owned or certificate-signed stored procedure lets callers run controlled DML/DDL workflows without direct table-level `SELECT`, `UPDATE`, or `IMPERSONATE` rights. In this scenario: Because `Inventory.usp_AdjustBinQty` and `Inventory.StockBins` share the exact same owner (`dbo`), unbroken ownership chaining skips permission checks on `Inventory.StockBins` and the `UPDATE` succeeds cleanly.

### Question 21 — D

Answer: No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference. No — Dynamic Data Masking neither encrypts data on disk nor blocks `WHERE` range-inference queries from ad-hoc `SELECT` users; column-level permissions or Always Encrypted is required. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Local study-map skill 2.4 (Apply Least Privilege Using Granular Server/Database Roles, Schema Chaining, `EXECUTE AS`, and T-SQL/GUI Tools), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Permissions hierarchy, server-level roles, and principle of least privilege in SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/security-server-roles).

- **A:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: No — Dynamic Data Masking neither encrypts data on disk nor blocks `WHERE` range-inference queries from ad-hoc `SELECT` users; column-level permissions or Always Encrypted is required.
- **B:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: No — Dynamic Data Masking neither encrypts data on disk nor blocks `WHERE` range-inference queries from ad-hoc `SELECT` users; column-level permissions or Always Encrypted is required.
- **C:** Incorrect for this requirement. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Why the keyed choice wins: No — Dynamic Data Masking neither encrypts data on disk nor blocks `WHERE` range-inference queries from ad-hoc `SELECT` users; column-level permissions or Always Encrypted is required.
- **D:** Correct. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. In this scenario: No — Dynamic Data Masking neither encrypts data on disk nor blocks `WHERE` range-inference queries from ad-hoc `SELECT` users; column-level permissions or Always Encrypted is required.

### Question 22 — B, D

Answers: Enable both `Soft Delete` and `Purge Protection` on the Azure Key Vault or Managed HSM storing the TDE protector key; Grant the SQL server Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) on the Key Vault. Enable `Soft Delete` and `Purge Protection` on the Key Vault, and grant the SQL Managed Instance's Managed Identity `get`, `wrapKey`, and `unwrapKey` (`Key Vault Crypto Service Encryption User`). Local study-map skill 2.6 (Implement Transparent Data Encryption (`TDE`) with Service-Managed Keys, Key Vault `CMK`, and VM Cert Backups), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Transparent Data Encryption (TDE) with service-managed and customer-managed keys in Key Vault (https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Enable `Soft Delete` and `Purge Protection` on the Key Vault, and grant the SQL Managed Instance's Managed Identity `get`, `wrapKey`, and `unwrapKey` (`Key Vault Crypto Service Encryption User`).
- **B:** Correct. The logical SQL server or SQL MI Managed Identity requires `get`, `wrapKey`, and `unwrapKey` permissions to wrap and unwrap the Database Encryption Key (`DEK`). In this scenario: Enable `Soft Delete` and `Purge Protection` on the Key Vault, and grant the SQL Managed Instance's Managed Identity `get`, `wrapKey`, and `unwrapKey` (`Key Vault Crypto Service Encryption User`).
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Enable `Soft Delete` and `Purge Protection` on the Key Vault, and grant the SQL Managed Instance's Managed Identity `get`, `wrapKey`, and `unwrapKey` (`Key Vault Crypto Service Encryption User`).
- **D:** Correct. Azure SQL requires both Soft Delete and Purge Protection on Key Vault so accidental or malicious key deletion can never permanently brick encrypted databases. In this scenario: Enable `Soft Delete` and `Purge Protection` on the Key Vault, and grant the SQL Managed Instance's Managed Identity `get`, `wrapKey`, and `unwrapKey` (`Key Vault Crypto Service Encryption User`).
- **E:** Incorrect for this requirement. Transaction log files perform sequential write-through flushes that do not benefit from read caching and must use `None` host caching. Why the keyed choice wins: Enable `Soft Delete` and `Purge Protection` on the Key Vault, and grant the SQL Managed Instance's Managed Identity `get`, `wrapKey`, and `unwrapKey` (`Key Vault Crypto Service Encryption User`).

### Question 23 — D

Answer: Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server. `sys.dm_database_encryption_keys` tracks real-time TDE scan progress, `encryption_state`, key algorithm, and certificate/asymmetric-key thumbprints across all databases. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Local study-map skill 2.6 (Implement Transparent Data Encryption (`TDE`) with Service-Managed Keys, Key Vault `CMK`, and VM Cert Backups), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Transparent Data Encryption (TDE) with service-managed and customer-managed keys in Key Vault (https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview).

- **A:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: `sys.dm_database_encryption_keys` tracks real-time TDE scan progress, `encryption_state`, key algorithm, and certificate/asymmetric-key thumbprints across all databases.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: `sys.dm_database_encryption_keys` tracks real-time TDE scan progress, `encryption_state`, key algorithm, and certificate/asymmetric-key thumbprints across all databases.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: `sys.dm_database_encryption_keys` tracks real-time TDE scan progress, `encryption_state`, key algorithm, and certificate/asymmetric-key thumbprints across all databases.
- **D:** Correct. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. In this scenario: `sys.dm_database_encryption_keys` tracks real-time TDE scan progress, `encryption_state`, key algorithm, and certificate/asymmetric-key thumbprints across all databases.

### Question 24 — D

Answer: No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server. No — server-level firewall rules in `master` do not replicate automatically to the secondary server; either replicate server rules via IaC on `sql-anvilpeak-west` or create a portable database-level rule in `QualityDB`. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Local study-map skill 2.8 (Configure Server-Level (`master`) vs Portable Database-Level IP Firewall Rules (`sp_set_database_firewall_rule`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Server-level and database-level IP firewall rules in Azure SQL Database (https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure).

- **A:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: No — server-level firewall rules in `master` do not replicate automatically to the secondary server; either replicate server rules via IaC on `sql-anvilpeak-west` or create a portable database-level rule in `QualityDB`.
- **B:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: No — server-level firewall rules in `master` do not replicate automatically to the secondary server; either replicate server rules via IaC on `sql-anvilpeak-west` or create a portable database-level rule in `QualityDB`.
- **C:** Incorrect for this requirement. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Why the keyed choice wins: No — server-level firewall rules in `master` do not replicate automatically to the secondary server; either replicate server rules via IaC on `sql-anvilpeak-west` or create a portable database-level rule in `QualityDB`.
- **D:** Correct. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. In this scenario: No — server-level firewall rules in `master` do not replicate automatically to the secondary server; either replicate server rules via IaC on `sql-anvilpeak-west` or create a portable database-level rule in `QualityDB`.

### Question 25 — C

Answer: Enable VBS enclave on Azure SQL Database → Provision Key Vault CMK & enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`) → Grant client Key Vault key permissions & attestation → Run in-place `ALTER TABLE` encryption. Enable a VBS enclave on the Azure SQL Database, create a Key Vault CMK and enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), configure client Key Vault/attestation access, and run in-place `ALTER TABLE` encryption. In-place Always Encrypted with VBS enclaves requires enabling a VBS enclave on the DB, creating an enclave-enabled CEK (`ALLOW_ENCLAVE_COMPUTATIONS`), and running cryptographic operations inside the enclave. Local study-map skill 2.9 (Implement Always Encrypted (`Deterministic` vs `Randomized`) and Always Encrypted with VBS/SGX Secure Enclaves), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always Encrypted and Always Encrypted with secure enclaves (https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves).

- **A:** Incorrect for this requirement. Incorrect workflow: Always Encrypted keeps CMKs out of SQL engine T-SQL reach so DBAs cannot decrypt data; enclaves process keys only inside attested enclave memory. Why the keyed choice wins: Enable a VBS enclave on the Azure SQL Database, create a Key Vault CMK and enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), configure client Key Vault/attestation access, and run in-place `ALTER TABLE` encryption.
- **B:** Incorrect for this requirement. Incorrect workflow: in-place encryption fails unless the database enclave is active and the CEK was created with `ENCLAVE_COMPUTATIONS` beforehand; CMKs never live in `sys.configurations`. Why the keyed choice wins: Enable a VBS enclave on the Azure SQL Database, create a Key Vault CMK and enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), configure client Key Vault/attestation access, and run in-place `ALTER TABLE` encryption.
- **C:** Correct. In-place Always Encrypted with VBS enclaves requires enabling a VBS enclave on the DB, creating an enclave-enabled CEK (`ALLOW_ENCLAVE_COMPUTATIONS`), and running cryptographic operations inside the enclave. In this scenario: Enable a VBS enclave on the Azure SQL Database, create a Key Vault CMK and enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), configure client Key Vault/attestation access, and run in-place `ALTER TABLE` encryption.
- **D:** Incorrect for this requirement. Incorrect workflow: `LIKE` pattern queries on Always Encrypted columns require `Column Encryption Setting=Enabled`, enclave attestation, and Randomized/enclave-enabled encryption. Why the keyed choice wins: Enable a VBS enclave on the Azure SQL Database, create a Key Vault CMK and enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), configure client Key Vault/attestation access, and run in-place `ALTER TABLE` encryption.

### Question 26 — D, E

Answers: Provision a Column Master Key in Key Vault and create a Column Encryption Key with `ENCLAVE_COMPUTATIONS` enabled; Enable `Column Encryption Setting=Enabled` and pass the `Enclave Attestation Url` (or VBS zero-attestation setting) in client drivers. Provision a Key Vault CMK + CEK with `ENCLAVE_COMPUTATIONS` enabled, and enable `Column Encryption Setting=Enabled` with enclave attestation in client connection strings. Local study-map skill 2.9 (Implement Always Encrypted (`Deterministic` vs `Randomized`) and Always Encrypted with VBS/SGX Secure Enclaves), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always Encrypted and Always Encrypted with secure enclaves (https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Provision a Key Vault CMK + CEK with `ENCLAVE_COMPUTATIONS` enabled, and enable `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Provision a Key Vault CMK + CEK with `ENCLAVE_COMPUTATIONS` enabled, and enable `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.
- **C:** Incorrect for this requirement. `ReadOnly` host caching serves random OLTP data-page reads directly from Azure hypervisor RAM/SSD cache without consuming disk IOPS. Why the keyed choice wins: Provision a Key Vault CMK + CEK with `ENCLAVE_COMPUTATIONS` enabled, and enable `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.
- **D:** Correct. Client drivers must enable Always Encrypted and verify enclave attestation before transmitting CEKs over TLS into the SQL secure enclave. In this scenario: Provision a Key Vault CMK + CEK with `ENCLAVE_COMPUTATIONS` enabled, and enable `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.
- **E:** Correct. Rich confidential queries (`LIKE`, `<`, `>`, sorting) and in-place encryption require a CEK explicitly marked to permit enclave computations. In this scenario: Provision a Key Vault CMK + CEK with `ENCLAVE_COMPUTATIONS` enabled, and enable `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.

### Question 27 — B, D

Answers: Link Private DNS Zone `privatelink.database.windows.net` (or forward on-premises DNS) to resolve `<server>.database.windows.net` to the private IP; Set `Public network access = Disabled` (`publicNetworkAccess: Disabled`) on the logical SQL server so internet connections are rejected. Link Private DNS Zone `privatelink.database.windows.net` (with DNS forwarding for ExpressRoute clients) and set `Public network access = Disabled` on the logical SQL server. Local study-map skill 2.10 (Configure Azure Private Link (`privatelink.database.windows.net`), Service Endpoints, and SQL MI Subnet Security), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure Private Link, Virtual Network service endpoints, and SQL MI VNet security (https://learn.microsoft.com/en-us/azure/azure-sql/database/private-endpoint-overview).

- **A:** Incorrect for this requirement. Azure Arc allows variable-workload or seasonal SQL Server hosts outside Azure to be billed hourly through an Azure subscription. Why the keyed choice wins: Link Private DNS Zone `privatelink.database.windows.net` (with DNS forwarding for ExpressRoute clients) and set `Public network access = Disabled` on the logical SQL server.
- **B:** Correct. Clients still validate the TLS certificate for `<server>.database.windows.net`, so split-brain DNS must map the canonical FQDN via CNAME to `privatelink.database.windows.net`. In this scenario: Link Private DNS Zone `privatelink.database.windows.net` (with DNS forwarding for ExpressRoute clients) and set `Public network access = Disabled` on the logical SQL server.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Link Private DNS Zone `privatelink.database.windows.net` (with DNS forwarding for ExpressRoute clients) and set `Public network access = Disabled` on the logical SQL server.
- **D:** Correct. Creating a Private Endpoint alone leaves the public endpoint reachable unless `Public network access` is explicitly disabled on the server. In this scenario: Link Private DNS Zone `privatelink.database.windows.net` (with DNS forwarding for ExpressRoute clients) and set `Public network access = Disabled` on the logical SQL server.
- **E:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: Link Private DNS Zone `privatelink.database.windows.net` (with DNS forwarding for ExpressRoute clients) and set `Public network access = Disabled` on the logical SQL server.

### Question 28 — B

Answer: Virtual Network Service Endpoints (`Microsoft.Sql`) with outbound storage firewall rules, or dedicated `/28+` delegated subnet for SQL MI. The SQL Managed Instance **VNet-local endpoint** (`<mi_name>.<dns_zone>.database.windows.net`) listens on standard private TCP port `1433` inside the delegated subnet over VNet peering (whereas the optional public endpoint uses TCP `3342`). VNet Service Endpoints restrict Azure SQL public endpoint traffic to a specific VNet subnet without private IPs, whereas SQL Managed Instance deploys directly into a dedicated delegated VNet subnet. Local study-map skill 2.10 (Configure Azure Private Link (`privatelink.database.windows.net`), Service Endpoints, and SQL MI Subnet Security), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure Private Link, Virtual Network service endpoints, and SQL MI VNet security (https://learn.microsoft.com/en-us/azure/azure-sql/database/private-endpoint-overview).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: The SQL Managed Instance **VNet-local endpoint** (`<mi_name>.<dns_zone>.database.windows.net`) listens on standard private TCP port `1433` inside the delegated subnet over VNet peering (whereas the optional public endpoint uses TCP `3342`).
- **B:** Correct. VNet Service Endpoints restrict Azure SQL public endpoint traffic to a specific VNet subnet without private IPs, whereas SQL Managed Instance deploys directly into a dedicated delegated VNet subnet. In this scenario: The SQL Managed Instance **VNet-local endpoint** (`<mi_name>.<dns_zone>.database.windows.net`) listens on standard private TCP port `1433` inside the delegated subnet over VNet peering (whereas the optional public endpoint uses TCP `3342`).
- **C:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: The SQL Managed Instance **VNet-local endpoint** (`<mi_name>.<dns_zone>.database.windows.net`) listens on standard private TCP port `1433` inside the delegated subnet over VNet peering (whereas the optional public endpoint uses TCP `3342`).
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: The SQL Managed Instance **VNet-local endpoint** (`<mi_name>.<dns_zone>.database.windows.net`) listens on standard private TCP port `1433` inside the delegated subnet over VNet peering (whereas the optional public endpoint uses TCP `3342`).

### Question 29 — A

Answer: SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage. Tag the column via `ADD SENSITIVITY CLASSIFICATION` and enable Azure SQL Auditing (`BATCH_COMPLETED_GROUP`) writing via Managed Identity to immutable Azure Blob Storage / Log Analytics. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. Local study-map skill 2.11 (Apply SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) and Server/Database Auditing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Data Discovery and Classification and Azure SQL Auditing (https://learn.microsoft.com/en-us/azure/azure-sql/database/auditing-overview).

- **A:** Correct. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. In this scenario: Tag the column via `ADD SENSITIVITY CLASSIFICATION` and enable Azure SQL Auditing (`BATCH_COMPLETED_GROUP`) writing via Managed Identity to immutable Azure Blob Storage / Log Analytics.
- **B:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Tag the column via `ADD SENSITIVITY CLASSIFICATION` and enable Azure SQL Auditing (`BATCH_COMPLETED_GROUP`) writing via Managed Identity to immutable Azure Blob Storage / Log Analytics.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Tag the column via `ADD SENSITIVITY CLASSIFICATION` and enable Azure SQL Auditing (`BATCH_COMPLETED_GROUP`) writing via Managed Identity to immutable Azure Blob Storage / Log Analytics.
- **D:** Incorrect for this requirement. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. Why the keyed choice wins: Tag the column via `ADD SENSITIVITY CLASSIFICATION` and enable Azure SQL Auditing (`BATCH_COMPLETED_GROUP`) writing via Managed Identity to immutable Azure Blob Storage / Log Analytics.

### Question 30 — B

Answer: SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage. `sys.fn_get_audit_file` parses `.sqlaudit` files (local disk on VMs or Blob URLs on SQL DB/MI) into relational audit rows showing `event_time`, `server_principal_name`, `statement`, and `data_sensitivity_information`. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. Local study-map skill 2.11 (Apply SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) and Server/Database Auditing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Data Discovery and Classification and Azure SQL Auditing (https://learn.microsoft.com/en-us/azure/azure-sql/database/auditing-overview).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `sys.fn_get_audit_file` parses `.sqlaudit` files (local disk on VMs or Blob URLs on SQL DB/MI) into relational audit rows showing `event_time`, `server_principal_name`, `statement`, and `data_sensitivity_information`.
- **B:** Correct. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. In this scenario: `sys.fn_get_audit_file` parses `.sqlaudit` files (local disk on VMs or Blob URLs on SQL DB/MI) into relational audit rows showing `event_time`, `server_principal_name`, `statement`, and `data_sensitivity_information`.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: `sys.fn_get_audit_file` parses `.sqlaudit` files (local disk on VMs or Blob URLs on SQL DB/MI) into relational audit rows showing `event_time`, `server_principal_name`, `statement`, and `data_sensitivity_information`.
- **D:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: `sys.fn_get_audit_file` parses `.sqlaudit` files (local disk on VMs or Blob URLs on SQL DB/MI) into relational audit rows showing `event_time`, `server_principal_name`, `statement`, and `data_sensitivity_information`.

### Question 31 — A

Answer: Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history. Because `@last_sync_version` is older than `CHANGE_TRACKING_MIN_VALID_VERSION(OBJECT_ID('PartMaster'))` (7-day retention), the client must perform a full re-initialization snapshot of `PartMaster`. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. Local study-map skill 2.12 (Implement Change Tracking (`CHANGETABLE`) vs Change Data Capture (`CDC`) for Downstream Data Changes), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Track data changes with Change Tracking (CT) and Change Data Capture (CDC) (https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/track-data-changes-sql-server).

- **A:** Correct. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. In this scenario: Because `@last_sync_version` is older than `CHANGE_TRACKING_MIN_VALID_VERSION(OBJECT_ID('PartMaster'))` (7-day retention), the client must perform a full re-initialization snapshot of `PartMaster`.
- **B:** Incorrect for this requirement. CDC requires `S3+` or `vCore` tiers in Azure SQL Database, and Change Tracking stores only net version numbers/PKs—never intermediate before/after column values. Why the keyed choice wins: Because `@last_sync_version` is older than `CHANGE_TRACKING_MIN_VALID_VERSION(OBJECT_ID('PartMaster'))` (7-day retention), the client must perform a full re-initialization snapshot of `PartMaster`.
- **C:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Because `@last_sync_version` is older than `CHANGE_TRACKING_MIN_VALID_VERSION(OBJECT_ID('PartMaster'))` (7-day retention), the client must perform a full re-initialization snapshot of `PartMaster`.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Because `@last_sync_version` is older than `CHANGE_TRACKING_MIN_VALID_VERSION(OBJECT_ID('PartMaster'))` (7-day retention), the client must perform a full re-initialization snapshot of `PartMaster`.

### Question 32 — D

Answer: Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas. Dynamic Data Masking's `random(start_range, end_range)` function replaces numeric column values with a random number inside `[15, 25]` at query execution time. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Local study-map skill 2.13 (Implement Dynamic Data Masking (`default`, `email`, `partial`, `random`) and Scoped `UNMASK` Permissions), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Dynamic Data Masking (DDM) in Azure SQL Database, SQL Managed Instance, and SQL Server (https://learn.microsoft.com/en-us/azure/azure-sql/database/dynamic-data-masking-overview).

- **A:** Incorrect for this requirement. Secure enclaves delegate column decryption into an isolated memory region inside SQL, unlocking `LIKE`, `<`, `>`, `ORDER BY`, and fast in-place initial encryption without exposing plaintext to DBAs. Why the keyed choice wins: Dynamic Data Masking's `random(start_range, end_range)` function replaces numeric column values with a random number inside `[15, 25]` at query execution time.
- **B:** Incorrect for this requirement. RLS transparently filters `SELECT`/`UPDATE`/`DELETE` rows via `FILTER PREDICATE` and blocks unauthorized cross-tenant `INSERT`/`UPDATE` writes via `BLOCK PREDICATE` inside the engine. Why the keyed choice wins: Dynamic Data Masking's `random(start_range, end_range)` function replaces numeric column values with a random number inside `[15, 25]` at query execution time.
- **C:** Incorrect for this requirement. BYOK TDE wraps the symmetric Database Encryption Key (`DEK`) with an asymmetric RSA key in Key Vault or Managed HSM so security admins control key rotation and instant revocation. Why the keyed choice wins: Dynamic Data Masking's `random(start_range, end_range)` function replaces numeric column values with a random number inside `[15, 25]` at query execution time.
- **D:** Correct. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. In this scenario: Dynamic Data Masking's `random(start_range, end_range)` function replaces numeric column values with a random number inside `[15, 25]` at query execution time.

### Question 33 — C, E, F

Answers: Create an inline table-valued function `WITH SCHEMABINDING` evaluating `SESSION_CONTEXT()` or `DATABASE_PRINCIPAL_ID()`; Add a `FILTER PREDICATE` in `CREATE SECURITY POLICY` to hide non-matching rows silently from `SELECT`, `UPDATE`, and `DELETE`; Add `AFTER INSERT` and `AFTER UPDATE` / `BEFORE UPDATE` `BLOCK PREDICATE` clauses in `CREATE SECURITY POLICY` (`STATE = ON`). Create a `SCHEMABINDING` inline TVF predicate and attach both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`. Local study-map skill 2.14 (Implement Cryptographic Ledger in Azure SQL (`Azure Confidential Ledger`) and Row-Level Security (`FILTER`/`BLOCK`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Ledger cryptographic tamper-evidence and Row-Level Security (RLS) in Azure SQL (https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-overview).

- **A:** Incorrect for this requirement. Append-only Ledger tables strictly block `UPDATE`, `DELETE`, and `TRUNCATE` statements in the SQL engine so cryptographic audit trails cannot be altered. Why the keyed choice wins: Create a `SCHEMABINDING` inline TVF predicate and attach both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Create a `SCHEMABINDING` inline TVF predicate and attach both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **C:** Correct. `FILTER PREDICATE` injects the security TVF into read, update, and delete operators transparently without changing application `SELECT` statements. In this scenario: Create a `SCHEMABINDING` inline TVF predicate and attach both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Create a `SCHEMABINDING` inline TVF predicate and attach both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **E:** Correct. `BLOCK PREDICATE` raises an error if a shared application login attempts to insert or update a row carrying another tenant's identifier. In this scenario: Create a `SCHEMABINDING` inline TVF predicate and attach both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **F:** Correct. RLS predicate functions must be inline TVFs bound with `SCHEMABINDING` so underlying columns cannot be altered silently and query plans inline cleanly. In this scenario: Create a `SCHEMABINDING` inline TVF predicate and attach both `FILTER PREDICATE` and `BLOCK PREDICATE` clauses inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.

### Question 34 — D

Answer: Create dedicated `Security` schema → Create `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT(N'TenantId')` → Create `SECURITY POLICY` with `FILTER` & `BLOCK` predicates (`STATE = ON`) → Set read-only `sp_set_session_context` on connect. Create a dedicated `Security` schema, build a `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT(N'PlantCode')`, create an active `SECURITY POLICY` with `FILTER` + `BLOCK` predicates, and set read-only `sp_set_session_context` on connect. Best-practice multi-tenant RLS isolates objects in a dedicated schema, uses a schema-bound inline TVF predicate over read-only `SESSION_CONTEXT`, and enforces both `FILTER` and `BLOCK` predicates. Local study-map skill 2.14 (Implement Cryptographic Ledger in Azure SQL (`Azure Confidential Ledger`) and Row-Level Security (`FILTER`/`BLOCK`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Ledger cryptographic tamper-evidence and Row-Level Security (RLS) in Azure SQL (https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-overview).

- **A:** Incorrect for this requirement. Incorrect workflow: RLS requires an existing `SCHEMABINDING` inline TVF before creating the security policy, and granting `ALTER ANY SECURITY POLICY` lets tenants bypass isolation. Why the keyed choice wins: Create a dedicated `Security` schema, build a `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT(N'PlantCode')`, create an active `SECURITY POLICY` with `FILTER` + `BLOCK` predicates, and set read-only `sp_set_session_context` on connect.
- **B:** Incorrect for this requirement. Incorrect workflow: RLS predicates must be schema-bound inline TVFs attached to a `SECURITY POLICY`, and `@read_only = 1` prevents SQL injection from changing `TenantId` mid-session. Why the keyed choice wins: Create a dedicated `Security` schema, build a `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT(N'PlantCode')`, create an active `SECURITY POLICY` with `FILTER` + `BLOCK` predicates, and set read-only `sp_set_session_context` on connect.
- **C:** Incorrect for this requirement. Incorrect workflow: Dynamic Data Masking obfuscates column output in result sets and never filters rows or blocks cross-tenant writes. Why the keyed choice wins: Create a dedicated `Security` schema, build a `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT(N'PlantCode')`, create an active `SECURITY POLICY` with `FILTER` + `BLOCK` predicates, and set read-only `sp_set_session_context` on connect.
- **D:** Correct. Best-practice multi-tenant RLS isolates objects in a dedicated schema, uses a schema-bound inline TVF predicate over read-only `SESSION_CONTEXT`, and enforces both `FILTER` and `BLOCK` predicates. In this scenario: Create a dedicated `Security` schema, build a `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT(N'PlantCode')`, create an active `SECURITY POLICY` with `FILTER` + `BLOCK` predicates, and set read-only `sp_set_session_context` on connect.

### Question 35 — B

Answer: Azure Monitor metrics paired with `sys.dm_db_resource_stats` (single DB) or `sys.server_resource_stats` (SQL MI) for 15-second CPU, data I/O, log write, and memory baselines. `Avg. Disk sec/Read` (and `Avg. Disk sec/Write` on the `.ldf` volume, multiplied by 1,000 for milliseconds) directly measures storage latency perceived by Windows and SQL Server. `sys.dm_db_resource_stats` retains 14 days of 15-second resource averages (`avg_cpu_percent`, `avg_data_io_percent`, `avg_log_write_percent`) to compare current peaks against normal baselines. Local study-map skill 3.1 (Establish Performance Baselines and Interpret CPU, Memory, Data I/O, Log Write, and `tempdb` Metrics), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL resource utilization and establish performance baselines (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-sql-database-azure-monitor).

- **A:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: `Avg. Disk sec/Read` (and `Avg. Disk sec/Write` on the `.ldf` volume, multiplied by 1,000 for milliseconds) directly measures storage latency perceived by Windows and SQL Server.
- **B:** Correct. `sys.dm_db_resource_stats` retains 14 days of 15-second resource averages (`avg_cpu_percent`, `avg_data_io_percent`, `avg_log_write_percent`) to compare current peaks against normal baselines. In this scenario: `Avg. Disk sec/Read` (and `Avg. Disk sec/Write` on the `.ldf` volume, multiplied by 1,000 for milliseconds) directly measures storage latency perceived by Windows and SQL Server.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `Avg. Disk sec/Read` (and `Avg. Disk sec/Write` on the `.ldf` volume, multiplied by 1,000 for milliseconds) directly measures storage latency perceived by Windows and SQL Server.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: `Avg. Disk sec/Read` (and `Avg. Disk sec/Write` on the `.ldf` volume, multiplied by 1,000 for milliseconds) directly measures storage latency perceived by Windows and SQL Server.

### Question 36 — C

Answer: Azure Monitor metrics paired with `sys.dm_db_resource_stats` (single DB) or `sys.server_resource_stats` (SQL MI) for 15-second CPU, data I/O, log write, and memory baselines. Sustained non-zero `Memory Grants Pending` (`RESOURCE_SEMAPHORE` waits) alongside sharp `PLE` drops and rising `PAGEIOLATCH_SH` physical reads confirms genuine buffer-pool / workspace memory starvation. `sys.dm_db_resource_stats` retains 14 days of 15-second resource averages (`avg_cpu_percent`, `avg_data_io_percent`, `avg_log_write_percent`) to compare current peaks against normal baselines. Local study-map skill 3.1 (Establish Performance Baselines and Interpret CPU, Memory, Data I/O, Log Write, and `tempdb` Metrics), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL resource utilization and establish performance baselines (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-sql-database-azure-monitor).

- **A:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Sustained non-zero `Memory Grants Pending` (`RESOURCE_SEMAPHORE` waits) alongside sharp `PLE` drops and rising `PAGEIOLATCH_SH` physical reads confirms genuine buffer-pool / workspace memory starvation.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Sustained non-zero `Memory Grants Pending` (`RESOURCE_SEMAPHORE` waits) alongside sharp `PLE` drops and rising `PAGEIOLATCH_SH` physical reads confirms genuine buffer-pool / workspace memory starvation.
- **C:** Correct. `sys.dm_db_resource_stats` retains 14 days of 15-second resource averages (`avg_cpu_percent`, `avg_data_io_percent`, `avg_log_write_percent`) to compare current peaks against normal baselines. In this scenario: Sustained non-zero `Memory Grants Pending` (`RESOURCE_SEMAPHORE` waits) alongside sharp `PLE` drops and rising `PAGEIOLATCH_SH` physical reads confirms genuine buffer-pool / workspace memory starvation.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Sustained non-zero `Memory Grants Pending` (`RESOURCE_SEMAPHORE` waits) alongside sharp `PLE` drops and rising `PAGEIOLATCH_SH` physical reads confirms genuine buffer-pool / workspace memory starvation.

### Question 37 — B

Answer: Azure Monitor Diagnostic Settings streaming `SQLInsights`, `QueryStoreRuntimeStatistics`, `Errors`, and `Blocks` to a Log Analytics workspace (`KQL`). Azure Monitor Diagnostic Settings configured on each database stream `Basic`/`InstanceAndAppAdvanced` metrics, `Errors`, `Deadlocks`, and `QueryStoreRuntimeStatistics` directly into Log Analytics. Diagnostic Settings export telemetry across hundreds of databases into Log Analytics so DBAs can correlate `SQLInsights`, wait stats, deadlocks, and timeouts via KQL queries and alerts. Local study-map skill 3.2 (Configure Azure Monitor Diagnostic Settings (`SQLInsights`, `AzureDiagnostics` KQL) and Resource Monitoring), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure Monitor diagnostic settings, SQLInsights logs, and metric alerts (https://learn.microsoft.com/en-us/azure/azure-sql/database/metrics-diagnostic-telemetry-logging-streaming-export-configure).

- **A:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Azure Monitor Diagnostic Settings configured on each database stream `Basic`/`InstanceAndAppAdvanced` metrics, `Errors`, `Deadlocks`, and `QueryStoreRuntimeStatistics` directly into Log Analytics.
- **B:** Correct. Diagnostic Settings export telemetry across hundreds of databases into Log Analytics so DBAs can correlate `SQLInsights`, wait stats, deadlocks, and timeouts via KQL queries and alerts. In this scenario: Azure Monitor Diagnostic Settings configured on each database stream `Basic`/`InstanceAndAppAdvanced` metrics, `Errors`, `Deadlocks`, and `QueryStoreRuntimeStatistics` directly into Log Analytics.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Azure Monitor Diagnostic Settings configured on each database stream `Basic`/`InstanceAndAppAdvanced` metrics, `Errors`, `Deadlocks`, and `QueryStoreRuntimeStatistics` directly into Log Analytics.
- **D:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Azure Monitor Diagnostic Settings configured on each database stream `Basic`/`InstanceAndAppAdvanced` metrics, `Errors`, `Deadlocks`, and `QueryStoreRuntimeStatistics` directly into Log Analytics.

### Question 38 — C

Answer: Provision Azure Data Explorer or Fabric Eventhouse store → Create database watcher with Managed Identity → Add SQL targets & grant `VIEW SERVER PERFORMANCE STATE` + ingest roles → Start watcher & open portal dashboards. Provision the Fabric Eventhouse / ADX data store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets + store ingest roles, and start the watcher. Database watcher streams SQL telemetry into an Azure Data Explorer or Fabric Eventhouse/KQL store using Managed Identity granted least-privilege `VIEW SERVER PERFORMANCE STATE` on SQL targets. Local study-map skill 3.3 (Monitor Workloads Using Database Watcher (ADX / Fabric Eventhouse) and Plan Fabric Database Hub Transition), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL workloads with database watcher and Database Hub in Microsoft Fabric (https://learn.microsoft.com/en-us/azure/azure-sql/database-watcher-overview).

- **A:** Incorrect for this requirement. Incorrect workflow: Azure SQL Database PaaS exposes no underlying OS for agents, `sp_trace_create` is deprecated, and database watcher is agentless. Why the keyed choice wins: Provision the Fabric Eventhouse / ADX data store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets + store ingest roles, and start the watcher.
- **B:** Incorrect for this requirement. Incorrect workflow: database watcher monitors Azure SQL Database, Elastic Pools, and SQL Managed Instance and stores telemetry in Azure Data Explorer or Fabric KQL databases. Why the keyed choice wins: Provision the Fabric Eventhouse / ADX data store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets + store ingest roles, and start the watcher.
- **C:** Correct. Database watcher streams SQL telemetry into an Azure Data Explorer or Fabric Eventhouse/KQL store using Managed Identity granted least-privilege `VIEW SERVER PERFORMANCE STATE` on SQL targets. In this scenario: Provision the Fabric Eventhouse / ADX data store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets + store ingest roles, and start the watcher.
- **D:** Incorrect for this requirement. Incorrect workflow: watcher requires an Azure Data Explorer or Fabric Real-Time Analytics store and SQL targets configured first, and uses least-privilege Managed Identity rather than `sa` or Profiler. Why the keyed choice wins: Provision the Fabric Eventhouse / ADX data store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets + store ingest roles, and start the watcher.

### Question 39 — A, E

Answers: Grant the database watcher Managed Identity `VIEW SERVER PERFORMANCE STATE` (or `VIEW DATABASE PERFORMANCE STATE`) on SQL targets; Grant the database watcher Managed Identity database `Admin` / ingest permissions on the Azure Data Explorer or Fabric Eventhouse store. Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on SQL targets, and grant database `Admin` / ingestion permissions on the Fabric Eventhouse / ADX database. Local study-map skill 3.3 (Monitor Workloads Using Database Watcher (ADX / Fabric Eventhouse) and Plan Fabric Database Hub Transition), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL workloads with database watcher and Database Hub in Microsoft Fabric (https://learn.microsoft.com/en-us/azure/azure-sql/database-watcher-overview).

- **A:** Correct. Database watcher collects DMVs and system catalogs using least-privilege performance-state permissions rather than `sysadmin` or data-read rights. In this scenario: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on SQL targets, and grant database `Admin` / ingestion permissions on the Fabric Eventhouse / ADX database.
- **B:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on SQL targets, and grant database `Admin` / ingestion permissions on the Fabric Eventhouse / ADX database.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on SQL targets, and grant database `Admin` / ingestion permissions on the Fabric Eventhouse / ADX database.
- **D:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on SQL targets, and grant database `Admin` / ingestion permissions on the Fabric Eventhouse / ADX database.
- **E:** Correct. Database watcher creates tables, retention policies, and ingestion mappings inside the target Azure Data Explorer or Fabric Real-Time Analytics KQL database. In this scenario: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on SQL targets, and grant database `Admin` / ingestion permissions on the Fabric Eventhouse / ADX database.

### Question 40 — A, C

Answers: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE` with `rwl` permissions) for the Azure Blob container; Define `CREATE EVENT SESSION ... ON DATABASE ADD TARGET package0.event_file(SET filename = N'https://...xel')` and start the session. Authenticate `TelemetryDB` to the Blob trace container via a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS), and define an `ON DATABASE` Extended Events session capturing `sqlserver.attention` into `package0.event_file`. Local study-map skill 3.4 (Monitor Workloads Using Extended Events (`ON DATABASE` vs `ON SERVER` & Persistent Blob `event_file` Targets)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Extended Events in Azure SQL Database and Azure SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/xevent-db-diff-from-svr).

- **A:** Correct. Extended Events in Azure SQL Database requires a `DATABASE SCOPED CREDENTIAL` with Read, Write, and List rights on the target Blob Storage container. In this scenario: Authenticate `TelemetryDB` to the Blob trace container via a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS), and define an `ON DATABASE` Extended Events session capturing `sqlserver.attention` into `package0.event_file`.
- **B:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Authenticate `TelemetryDB` to the Blob trace container via a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS), and define an `ON DATABASE` Extended Events session capturing `sqlserver.attention` into `package0.event_file`.
- **C:** Correct. Azure SQL Database scopes Extended Event sessions `ON DATABASE` and streams persistent `.xel` ring-rotated files to the Blob container URL. In this scenario: Authenticate `TelemetryDB` to the Blob trace container via a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS), and define an `ON DATABASE` Extended Events session capturing `sqlserver.attention` into `package0.event_file`.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Authenticate `TelemetryDB` to the Blob trace container via a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS), and define an `ON DATABASE` Extended Events session capturing `sqlserver.attention` into `package0.event_file`.
- **E:** Incorrect for this requirement. Azure SQL requires both Soft Delete and Purge Protection on Key Vault so accidental or malicious key deletion can never permanently brick encrypted databases. Why the keyed choice wins: Authenticate `TelemetryDB` to the Blob trace container via a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS), and define an `ON DATABASE` Extended Events session capturing `sqlserver.attention` into `package0.event_file`.

### Question 41 — D

Answer: Extended Events (`CREATE EVENT SESSION ... ON DATABASE` in SQL DB or `ON SERVER` in SQL MI/VMs) writing to an `event_file` target in Azure Blob Storage. Attach the predicate (`WHERE ([duration] > (5000000))`) directly inside the `ADD EVENT sqlserver.sql_batch_completed(...)` clause so the engine discards sub-5-second events synchronously before firing actions or writing targets. Unlike ephemeral in-memory `ring_buffer` targets, the `event_file` target persists `.xel` trace files durably in Azure Blob Storage using a database-scoped credential (Managed Identity or SAS). Local study-map skill 3.4 (Monitor Workloads Using Extended Events (`ON DATABASE` vs `ON SERVER` & Persistent Blob `event_file` Targets)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Extended Events in Azure SQL Database and Azure SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/xevent-db-diff-from-svr).

- **A:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Attach the predicate (`WHERE ([duration] > (5000000))`) directly inside the `ADD EVENT sqlserver.sql_batch_completed(...)` clause so the engine discards sub-5-second events synchronously before firing actions or writing targets.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Attach the predicate (`WHERE ([duration] > (5000000))`) directly inside the `ADD EVENT sqlserver.sql_batch_completed(...)` clause so the engine discards sub-5-second events synchronously before firing actions or writing targets.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Attach the predicate (`WHERE ([duration] > (5000000))`) directly inside the `ADD EVENT sqlserver.sql_batch_completed(...)` clause so the engine discards sub-5-second events synchronously before firing actions or writing targets.
- **D:** Correct. Unlike ephemeral in-memory `ring_buffer` targets, the `event_file` target persists `.xel` trace files durably in Azure Blob Storage using a database-scoped credential (Managed Identity or SAS). In this scenario: Attach the predicate (`WHERE ([duration] > (5000000))`) directly inside the `ADD EVENT sqlserver.sql_batch_completed(...)` clause so the engine discards sub-5-second events synchronously before firing actions or writing targets.

### Question 42 — A, D

Answers: Execute `sys.sp_query_store_force_plan @query_id, @plan_id` to pin the historical low-latency execution plan immediately; Execute `sys.sp_query_store_set_hints @query_id, N'OPTION (RECOMPILE)'` (or `MAXDOP` / memory grant hints) without redeploying code. Use `sys.sp_query_store_set_hints` (e.g., `N'OPTION (MAXDOP 2)'`) or `sys.sp_query_store_force_plan` to pin a low-DOP historical plan directly on the `query_id`. Local study-map skill 3.5 (Configure and Monitor Query Store, Force Regressed Plans (`sp_query_store_force_plan`), and Set Query Store Hints), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance by using the Query Store, plan forcing, and Query Store hints (https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store).

- **A:** Correct. `sp_query_store_force_plan` instructs the optimizer to compile plans matching the forced `plan_id` shape without modifying application T-SQL. In this scenario: Use `sys.sp_query_store_set_hints` (e.g., `N'OPTION (MAXDOP 2)'`) or `sys.sp_query_store_force_plan` to pin a low-DOP historical plan directly on the `query_id`.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Use `sys.sp_query_store_set_hints` (e.g., `N'OPTION (MAXDOP 2)'`) or `sys.sp_query_store_force_plan` to pin a low-DOP historical plan directly on the `query_id`.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Use `sys.sp_query_store_set_hints` (e.g., `N'OPTION (MAXDOP 2)'`) or `sys.sp_query_store_force_plan` to pin a low-DOP historical plan directly on the `query_id`.
- **D:** Correct. Query Store hints attach `OPTION (...)` query hints directly to a `query_id` in Azure SQL DB, SQL MI, and SQL Server 2022+ when app code cannot be edited. In this scenario: Use `sys.sp_query_store_set_hints` (e.g., `N'OPTION (MAXDOP 2)'`) or `sys.sp_query_store_force_plan` to pin a low-DOP historical plan directly on the `query_id`.
- **E:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Use `sys.sp_query_store_set_hints` (e.g., `N'OPTION (MAXDOP 2)'`) or `sys.sp_query_store_force_plan` to pin a low-DOP historical plan directly on the `query_id`.

### Question 43 — C

Answer: Confirm Query Store is `READ_WRITE` with wait capture → Compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`) → Force prior plan via `sp_query_store_force_plan` → Monitor `force_failure_count` & latency. Confirm Query Store is `READ_WRITE` with wait capture, compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`), force the 18 ms `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`. Resolving a parameter-sensitive plan regression uses Query Store runtime/wait history to identify the prior known-good `plan_id`, forces it immediately without code changes, and verifies forcing health. Local study-map skill 3.5 (Configure and Monitor Query Store, Force Regressed Plans (`sp_query_store_force_plan`), and Set Query Store Hints), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance by using the Query Store, plan forcing, and Query Store hints (https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store).

- **A:** Incorrect for this requirement. Incorrect workflow: system catalog tables cannot be updated directly and flushing the plan cache every minute spikes CPU compilations across the entire workload. Why the keyed choice wins: Confirm Query Store is `READ_WRITE` with wait capture, compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`), force the 18 ms `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`.
- **B:** Incorrect for this requirement. Incorrect workflow: purging Query Store erases the historical baseline and prior good plan needed to diagnose and force the healthy execution plan. Why the keyed choice wins: Confirm Query Store is `READ_WRITE` with wait capture, compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`), force the 18 ms `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`.
- **C:** Correct. Resolving a parameter-sensitive plan regression uses Query Store runtime/wait history to identify the prior known-good `plan_id`, forces it immediately without code changes, and verifies forcing health. In this scenario: Confirm Query Store is `READ_WRITE` with wait capture, compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`), force the 18 ms `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`.
- **D:** Incorrect for this requirement. Incorrect workflow: restarting SQL or running offline index rebuilds causes severe production outage and does not prevent parameter-sensitive plan regressions. Why the keyed choice wins: Confirm Query Store is `READ_WRITE` with wait capture, compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`), force the 18 ms `plan_id` via `sp_query_store_force_plan`, and monitor `force_failure_count`.

### Question 44 — A

Answer: Read Committed Snapshot Isolation (`READ_COMMITTED_SNAPSHOT = ON`) combined with Optimized Locking (`TID` locking + Lock After Qualification `LAQ`). Enabling `RCSI` on SQL Server VMs without `ADR` stores row versions in `tempdb` (whereas when `ADR = ON`, versions live in the database's `PVS`), so verify `tempdb` / `PVS` throughput and free space. `RCSI` uses row versioning so readers never block writers (`LCK_M_S`), while Optimized Locking in Azure SQL DB replaces thousands of row/page locks with a single Transaction ID lock and `LAQ`. Local study-map skill 3.6 (Identify and Resolve Session Blocking (`RCSI`, `Optimized Locking` `TID`/`LAQ`) and Deadlocks (`xml_deadlock_report`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Understand and resolve Azure SQL blocking problems, deadlocks, RCSI, and Optimized Locking (https://learn.microsoft.com/en-us/azure/azure-sql/database/analyze-prevent-deadlocks).

- **A:** Correct. `RCSI` uses row versioning so readers never block writers (`LCK_M_S`), while Optimized Locking in Azure SQL DB replaces thousands of row/page locks with a single Transaction ID lock and `LAQ`. In this scenario: Enabling `RCSI` on SQL Server VMs without `ADR` stores row versions in `tempdb` (whereas when `ADR = ON`, versions live in the database's `PVS`), so verify `tempdb` / `PVS` throughput and free space.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Enabling `RCSI` on SQL Server VMs without `ADR` stores row versions in `tempdb` (whereas when `ADR = ON`, versions live in the database's `PVS`), so verify `tempdb` / `PVS` throughput and free space.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Enabling `RCSI` on SQL Server VMs without `ADR` stores row versions in `tempdb` (whereas when `ADR = ON`, versions live in the database's `PVS`), so verify `tempdb` / `PVS` throughput and free space.
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Enabling `RCSI` on SQL Server VMs without `ADR` stores row versions in `tempdb` (whereas when `ADR = ON`, versions live in the database's `PVS`), so verify `tempdb` / `PVS` throughput and free space.

### Question 45 — D

Answer: Capture `xml_deadlock_report` via Extended Events or `sys.event_log`, align table modification order across transactions, and add covering indexes. Setting `SET DEADLOCK_PRIORITY LOW` in the background sync session instructs SQL Server's lock monitor to sacrifice the retryable background job rather than killing the interactive kiosk transaction. Cycle deadlocks (`Error 1205`) occur when concurrent transactions lock objects in opposite order or scan wide ranges; accessing tables in identical order with narrow index seeks eliminates cycles. Local study-map skill 3.6 (Identify and Resolve Session Blocking (`RCSI`, `Optimized Locking` `TID`/`LAQ`) and Deadlocks (`xml_deadlock_report`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Understand and resolve Azure SQL blocking problems, deadlocks, RCSI, and Optimized Locking (https://learn.microsoft.com/en-us/azure/azure-sql/database/analyze-prevent-deadlocks).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Setting `SET DEADLOCK_PRIORITY LOW` in the background sync session instructs SQL Server's lock monitor to sacrifice the retryable background job rather than killing the interactive kiosk transaction.
- **B:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Setting `SET DEADLOCK_PRIORITY LOW` in the background sync session instructs SQL Server's lock monitor to sacrifice the retryable background job rather than killing the interactive kiosk transaction.
- **C:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Setting `SET DEADLOCK_PRIORITY LOW` in the background sync session instructs SQL Server's lock monitor to sacrifice the retryable background job rather than killing the interactive kiosk transaction.
- **D:** Correct. Cycle deadlocks (`Error 1205`) occur when concurrent transactions lock objects in opposite order or scan wide ranges; accessing tables in identical order with narrow index seeks eliminates cycles. In this scenario: Setting `SET DEADLOCK_PRIORITY LOW` in the background sync session instructs SQL Server's lock monitor to sacrifice the retryable background job rather than killing the interactive kiosk transaction.

### Question 46 — A

Answer: Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`. In-memory allocation bitmap contention (`PFS`/`GAM`/`SGAM`) in `tempdb` (`database_id = 2`), mitigated by configuring 8 equal-sized `tempdb` data files on NVMe plus SQL 2022 memory-optimized `tempdb` metadata. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. Local study-map skill 3.7 (Identify Performance Bottlenecks Using Dynamic Management Views (`sys.dm_os_wait_stats`, `sys.dm_exec_requests`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance using Dynamic Management Views (DMVs) and wait statistics (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-with-dmvs).

- **A:** Correct. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. In this scenario: In-memory allocation bitmap contention (`PFS`/`GAM`/`SGAM`) in `tempdb` (`database_id = 2`), mitigated by configuring 8 equal-sized `tempdb` data files on NVMe plus SQL 2022 memory-optimized `tempdb` metadata.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: In-memory allocation bitmap contention (`PFS`/`GAM`/`SGAM`) in `tempdb` (`database_id = 2`), mitigated by configuring 8 equal-sized `tempdb` data files on NVMe plus SQL 2022 memory-optimized `tempdb` metadata.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: In-memory allocation bitmap contention (`PFS`/`GAM`/`SGAM`) in `tempdb` (`database_id = 2`), mitigated by configuring 8 equal-sized `tempdb` data files on NVMe plus SQL 2022 memory-optimized `tempdb` metadata.
- **D:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: In-memory allocation bitmap contention (`PFS`/`GAM`/`SGAM`) in `tempdb` (`database_id = 2`), mitigated by configuring 8 equal-sized `tempdb` data files on NVMe plus SQL 2022 memory-optimized `tempdb` metadata.

### Question 47 — D

Answer: Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`. `sys.dm_db_missing_index_details` lists candidate key/`INCLUDE` columns, yet creating every suggestion blindly ignores existing overlapping indexes, column order selectivity, and `INSERT`/`UPDATE` write amplification. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. Local study-map skill 3.7 (Identify Performance Bottlenecks Using Dynamic Management Views (`sys.dm_os_wait_stats`, `sys.dm_exec_requests`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance using Dynamic Management Views (DMVs) and wait statistics (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-with-dmvs).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: `sys.dm_db_missing_index_details` lists candidate key/`INCLUDE` columns, yet creating every suggestion blindly ignores existing overlapping indexes, column order selectivity, and `INSERT`/`UPDATE` write amplification.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `sys.dm_db_missing_index_details` lists candidate key/`INCLUDE` columns, yet creating every suggestion blindly ignores existing overlapping indexes, column order selectivity, and `INSERT`/`UPDATE` write amplification.
- **C:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: `sys.dm_db_missing_index_details` lists candidate key/`INCLUDE` columns, yet creating every suggestion blindly ignores existing overlapping indexes, column order selectivity, and `INSERT`/`UPDATE` write amplification.
- **D:** Correct. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. In this scenario: `sys.dm_db_missing_index_details` lists candidate key/`INCLUDE` columns, yet creating every suggestion blindly ignores existing overlapping indexes, column order selectivity, and `INSERT`/`UPDATE` write amplification.

### Question 48 — B

Answer: Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions. Split the expression into SARGable column predicates (`WHERE PartCode = @part AND Revision = @rev`) or index a persisted computed column so SQL performs a direct composite `Index Seek`. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. Local study-map skill 3.8 (Design Covering/Filtered/Columnstore Indexes and Rewrite Non-SARGable or Implicit-Conversion T-SQL Constructs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server and Azure SQL index design guide and SARGable T-SQL tuning (https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Split the expression into SARGable column predicates (`WHERE PartCode = @part AND Revision = @rev`) or index a persisted computed column so SQL performs a direct composite `Index Seek`.
- **B:** Correct. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. In this scenario: Split the expression into SARGable column predicates (`WHERE PartCode = @part AND Revision = @rev`) or index a persisted computed column so SQL performs a direct composite `Index Seek`.
- **C:** Incorrect for this requirement. Row-by-row cursors and multi-statement TVFs under legacy compatibility levels execute thousands of iterative context switches and 1-row cardinality guesses. Why the keyed choice wins: Split the expression into SARGable column predicates (`WHERE PartCode = @part AND Revision = @rev`) or index a persisted computed column so SQL performs a direct composite `Index Seek`.
- **D:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Split the expression into SARGable column predicates (`WHERE PartCode = @part AND Revision = @rev`) or index a persisted computed column so SQL performs a direct composite `Index Seek`.

### Question 49 — C

Answer: Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`). Query A scales vastly better because `420` logical reads versus `185,000` consumes 440x less CPU and buffer-pool memory bandwidth under high concurrency. Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. Local study-map skill 3.9 (Analyze Execution Plans (`Key Lookup`, `TempDB` Spills, Row Skew) and Monitor via SQL Intelligent Insights), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Execution plans and SQL Intelligent Insights automated performance diagnostics (https://learn.microsoft.com/en-us/azure/azure-sql/database/intelligent-insights-overview).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Query A scales vastly better because `420` logical reads versus `185,000` consumes 440x less CPU and buffer-pool memory bandwidth under high concurrency.
- **B:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Query A scales vastly better because `420` logical reads versus `185,000` consumes 440x less CPU and buffer-pool memory bandwidth under high concurrency.
- **C:** Correct. Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. In this scenario: Query A scales vastly better because `420` logical reads versus `185,000` consumes 440x less CPU and buffer-pool memory bandwidth under high concurrency.
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Query A scales vastly better because `420` logical reads versus `185,000` consumes 440x less CPU and buffer-pool memory bandwidth under high concurrency.

### Question 50 — D

Answer: Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`). Rewriting the `INNER JOIN` + `DISTINCT` as a semi-join `WHERE EXISTS (SELECT 1 FROM OrderLines ol WHERE ol.OrderId = o.OrderId)` stops at the first matching line per order without duplicating rows or sorting. Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. Local study-map skill 3.9 (Analyze Execution Plans (`Key Lookup`, `TempDB` Spills, Row Skew) and Monitor via SQL Intelligent Insights), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Execution plans and SQL Intelligent Insights automated performance diagnostics (https://learn.microsoft.com/en-us/azure/azure-sql/database/intelligent-insights-overview).

- **A:** Incorrect for this requirement. BYOK TDE wraps the symmetric Database Encryption Key (`DEK`) with an asymmetric RSA key in Key Vault or Managed HSM so security admins control key rotation and instant revocation. Why the keyed choice wins: Rewriting the `INNER JOIN` + `DISTINCT` as a semi-join `WHERE EXISTS (SELECT 1 FROM OrderLines ol WHERE ol.OrderId = o.OrderId)` stops at the first matching line per order without duplicating rows or sorting.
- **B:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Rewriting the `INNER JOIN` + `DISTINCT` as a semi-join `WHERE EXISTS (SELECT 1 FROM OrderLines ol WHERE ol.OrderId = o.OrderId)` stops at the first matching line per order without duplicating rows or sorting.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Rewriting the `INNER JOIN` + `DISTINCT` as a semi-join `WHERE EXISTS (SELECT 1 FROM OrderLines ol WHERE ol.OrderId = o.OrderId)` stops at the first matching line per order without duplicating rows or sorting.
- **D:** Correct. Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. In this scenario: Rewriting the `INNER JOIN` + `DISTINCT` as a semi-join `WHERE EXISTS (SELECT 1 FROM OrderLines ol WHERE ol.OrderId = o.OrderId)` stops at the first matching line per order without duplicating rows or sorting.

### Question 51 — C

Answer: Fragmentation-aware index maintenance (`REORGANIZE` 5–30%, `REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` >30%), `UPDATE STATISTICS`, and `DBCC CHECKDB WITH PHYSICAL_ONLY`. Running `UPDATE STATISTICS dbo.ProductionRuns WITH FULLSCAN` (or incremental partition statistics `RESAMPLE ON PARTITIONS(...)`) immediately updates the leading-edge date histogram step (`ascending key` problem). `RESUMABLE = ON` lets large online index rebuilds pause and resume across maintenance windows; `AUTO_UPDATE_STATISTICS_ASYNC` avoids compile stalls; `PHYSICAL_ONLY` reduces `CHECKDB` I/O overhead. Local study-map skill 3.10 (Implement Fragmentation-Aware Index Rebuilds (`ONLINE`, `RESUMABLE`), Async Statistics, and `DBCC CHECKDB`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Optimize index maintenance, statistics updates, and DBCC CHECKDB integrity checks (https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Running `UPDATE STATISTICS dbo.ProductionRuns WITH FULLSCAN` (or incremental partition statistics `RESAMPLE ON PARTITIONS(...)`) immediately updates the leading-edge date histogram step (`ascending key` problem).
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Running `UPDATE STATISTICS dbo.ProductionRuns WITH FULLSCAN` (or incremental partition statistics `RESAMPLE ON PARTITIONS(...)`) immediately updates the leading-edge date histogram step (`ascending key` problem).
- **C:** Correct. `RESUMABLE = ON` lets large online index rebuilds pause and resume across maintenance windows; `AUTO_UPDATE_STATISTICS_ASYNC` avoids compile stalls; `PHYSICAL_ONLY` reduces `CHECKDB` I/O overhead. In this scenario: Running `UPDATE STATISTICS dbo.ProductionRuns WITH FULLSCAN` (or incremental partition statistics `RESAMPLE ON PARTITIONS(...)`) immediately updates the leading-edge date histogram step (`ascending key` problem).
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Running `UPDATE STATISTICS dbo.ProductionRuns WITH FULLSCAN` (or incremental partition statistics `RESAMPLE ON PARTITIONS(...)`) immediately updates the leading-edge date histogram step (`ascending key` problem).

### Question 52 — C

Answer: Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`). Automatic Tuning relies completely on Query Store telemetry; enabling `ALTER DATABASE ... SET QUERY_STORE = ON (OPERATION_MODE = READ_WRITE)` transitions `actual_state_desc` to `ON`. Automatic Tuning continuously monitors Query Store, automatically forces prior plans when regressions occur, creates validated missing nonclustered indexes, and removes unused duplicate indexes. Local study-map skill 3.11 (Configure Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN`, `CREATE_INDEX`, `DROP_INDEX`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automatic tuning in Azure SQL Database and Azure SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-overview).

- **A:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Automatic Tuning relies completely on Query Store telemetry; enabling `ALTER DATABASE ... SET QUERY_STORE = ON (OPERATION_MODE = READ_WRITE)` transitions `actual_state_desc` to `ON`.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Automatic Tuning relies completely on Query Store telemetry; enabling `ALTER DATABASE ... SET QUERY_STORE = ON (OPERATION_MODE = READ_WRITE)` transitions `actual_state_desc` to `ON`.
- **C:** Correct. Automatic Tuning continuously monitors Query Store, automatically forces prior plans when regressions occur, creates validated missing nonclustered indexes, and removes unused duplicate indexes. In this scenario: Automatic Tuning relies completely on Query Store telemetry; enabling `ALTER DATABASE ... SET QUERY_STORE = ON (OPERATION_MODE = READ_WRITE)` transitions `actual_state_desc` to `ON`.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Automatic Tuning relies completely on Query Store telemetry; enabling `ALTER DATABASE ... SET QUERY_STORE = ON (OPERATION_MODE = READ_WRITE)` transitions `actual_state_desc` to `ON`.

### Question 53 — C

Answer: Configure `cost threshold for parallelism`, `MAXDOP`, `max server memory (MB)`, and Resource Governor (`WORKLOAD GROUP` + `RESOURCE POOL` + classifier UDF) on SQL MI / VMs. Leaving `max server memory` uncapped (`2147483647 MB`) lets the SQL buffer pool starve the Windows OS, thread stacks, and extensions, while Microsoft recommends initial `MAXDOP = 8` on NUMA nodes with `>8` cores. Tuning `cost threshold for parallelism` (e.g., 50) and `MAXDOP` curbs OLTP `CXPACKET` waits, while Resource Governor throttles reporting CPU/memory caps on SQL Server and SQL Managed Instance. Local study-map skill 3.12 (Configure Server Performance Settings (`MAXDOP`, `cost threshold`, `max server memory`) and Resource Governor), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Server configuration options (MAXDOP, memory) and Resource Governor workload isolation (https://learn.microsoft.com/en-us/sql/relational-databases/resource-governor/resource-governor).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Leaving `max server memory` uncapped (`2147483647 MB`) lets the SQL buffer pool starve the Windows OS, thread stacks, and extensions, while Microsoft recommends initial `MAXDOP = 8` on NUMA nodes with `>8` cores.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Leaving `max server memory` uncapped (`2147483647 MB`) lets the SQL buffer pool starve the Windows OS, thread stacks, and extensions, while Microsoft recommends initial `MAXDOP = 8` on NUMA nodes with `>8` cores.
- **C:** Correct. Tuning `cost threshold for parallelism` (e.g., 50) and `MAXDOP` curbs OLTP `CXPACKET` waits, while Resource Governor throttles reporting CPU/memory caps on SQL Server and SQL Managed Instance. In this scenario: Leaving `max server memory` uncapped (`2147483647 MB`) lets the SQL buffer pool starve the Windows OS, thread stacks, and extensions, while Microsoft recommends initial `MAXDOP = 8` on NUMA nodes with `>8` cores.
- **D:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Leaving `max server memory` uncapped (`2147483647 MB`) lets the SQL buffer pool starve the Windows OS, thread stacks, and extensions, while Microsoft recommends initial `MAXDOP = 8` on NUMA nodes with `>8` cores.

### Question 54 — B

Answer: Use `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`, `OPTIMIZED_PLAN_FORCING`) per database. Optimized Plan Forcing (`OPTIMIZED_PLAN_FORCING = ON`) records compilation replay scripts in Query Store, slashing repeat compilation CPU time for forced complex plans. Database-scoped configurations isolate optimizer settings (`MAXDOP`, CE version, parameter sniffing) to a single database without affecting sibling databases on SQL MI/VMs or requiring server access. Local study-map skill 3.13 (Implement `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: ALTER DATABASE SCOPED CONFIGURATION and dynamic compute/storage scaling (https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Optimized Plan Forcing (`OPTIMIZED_PLAN_FORCING = ON`) records compilation replay scripts in Query Store, slashing repeat compilation CPU time for forced complex plans.
- **B:** Correct. Database-scoped configurations isolate optimizer settings (`MAXDOP`, CE version, parameter sniffing) to a single database without affecting sibling databases on SQL MI/VMs or requiring server access. In this scenario: Optimized Plan Forcing (`OPTIMIZED_PLAN_FORCING = ON`) records compilation replay scripts in Query Store, slashing repeat compilation CPU time for forced complex plans.
- **C:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Optimized Plan Forcing (`OPTIMIZED_PLAN_FORCING = ON`) records compilation replay scripts in Query Store, slashing repeat compilation CPU time for forced complex plans.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Optimized Plan Forcing (`OPTIMIZED_PLAN_FORCING = ON`) records compilation replay scripts in Query Store, slashing repeat compilation CPU time for forced complex plans.

### Question 55 — C

Answer: SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators. SQL Server Agent **Multi-Server Administration** (`Master Server MSX` -> `Target Servers TSX` over encrypted TLS channels) centrally distributes schedules and aggregates job statuses across SQL Server VMs. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. Local study-map skill 4.1 (Create and Schedule SQL Server Agent Maintenance Jobs, Proxies, Severity `19–25` Alerts, and Database Mail), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server Agent jobs, schedules, alerts, and Database Mail operators (https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: SQL Server Agent **Multi-Server Administration** (`Master Server MSX` -> `Target Servers TSX` over encrypted TLS channels) centrally distributes schedules and aggregates job statuses across SQL Server VMs.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: SQL Server Agent **Multi-Server Administration** (`Master Server MSX` -> `Target Servers TSX` over encrypted TLS channels) centrally distributes schedules and aggregates job statuses across SQL Server VMs.
- **C:** Correct. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. In this scenario: SQL Server Agent **Multi-Server Administration** (`Master Server MSX` -> `Target Servers TSX` over encrypted TLS channels) centrally distributes schedules and aggregates job statuses across SQL Server VMs.
- **D:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: SQL Server Agent **Multi-Server Administration** (`Master Server MSX` -> `Target Servers TSX` over encrypted TLS channels) centrally distributes schedules and aggregates job statuses across SQL Server VMs.

### Question 56 — C

Answer: SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators. Adding multiple Database Mail **Accounts** with ascending sequence numbers (`1`, `2`) inside a single Database Mail **Profile** makes SQL Server automatically fail over to Account `2` if Account `1`'s SMTP server is unreachable. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. Local study-map skill 4.1 (Create and Schedule SQL Server Agent Maintenance Jobs, Proxies, Severity `19–25` Alerts, and Database Mail), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server Agent jobs, schedules, alerts, and Database Mail operators (https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Adding multiple Database Mail **Accounts** with ascending sequence numbers (`1`, `2`) inside a single Database Mail **Profile** makes SQL Server automatically fail over to Account `2` if Account `1`'s SMTP server is unreachable.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Adding multiple Database Mail **Accounts** with ascending sequence numbers (`1`, `2`) inside a single Database Mail **Profile** makes SQL Server automatically fail over to Account `2` if Account `1`'s SMTP server is unreachable.
- **C:** Correct. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. In this scenario: Adding multiple Database Mail **Accounts** with ascending sequence numbers (`1`, `2`) inside a single Database Mail **Profile** makes SQL Server automatically fail over to Account `2` if Account `1`'s SMTP server is unreachable.
- **D:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Adding multiple Database Mail **Accounts** with ascending sequence numbers (`1`, `2`) inside a single Database Mail **Profile** makes SQL Server automatically fail over to Account `2` if Account `1`'s SMTP server is unreachable.

### Question 57 — C

Answer: Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries. Enabling **Mail profile** (`Enable mail profile -> Database Mail`) under `SQL Server Agent Properties -> Alert System` and restarting the `SQLServerAgent` service is required before Agent alerts can dispatch Database Mail. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. Local study-map skill 4.2 (Troubleshoot SQL Server Agent Job Histories, Credential/Proxy Permissions, and SQL MI Subsystem Boundaries), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot SQL Server Agent jobs, proxies, and SQL Managed Instance Agent differences (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/transact-sql-tsql-differences-sql-server).

- **A:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: Enabling **Mail profile** (`Enable mail profile -> Database Mail`) under `SQL Server Agent Properties -> Alert System` and restarting the `SQLServerAgent` service is required before Agent alerts can dispatch Database Mail.
- **B:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Enabling **Mail profile** (`Enable mail profile -> Database Mail`) under `SQL Server Agent Properties -> Alert System` and restarting the `SQLServerAgent` service is required before Agent alerts can dispatch Database Mail.
- **C:** Correct. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. In this scenario: Enabling **Mail profile** (`Enable mail profile -> Database Mail`) under `SQL Server Agent Properties -> Alert System` and restarting the `SQLServerAgent` service is required before Agent alerts can dispatch Database Mail.
- **D:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Enabling **Mail profile** (`Enable mail profile -> Database Mail`) under `SQL Server Agent Properties -> Alert System` and restarting the `SQLServerAgent` service is required before Agent alerts can dispatch Database Mail.

### Question 58 — C

Answer: Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries. Calling `EXEC msdb.dbo.sp_help_jobactivity` (or querying `msdb.dbo.sysjobactivity` where `start_execution_date IS NOT NULL AND stop_execution_date IS NULL`) lists currently executing Agent jobs and active step IDs. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. Local study-map skill 4.2 (Troubleshoot SQL Server Agent Job Histories, Credential/Proxy Permissions, and SQL MI Subsystem Boundaries), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot SQL Server Agent jobs, proxies, and SQL Managed Instance Agent differences (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/transact-sql-tsql-differences-sql-server).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Calling `EXEC msdb.dbo.sp_help_jobactivity` (or querying `msdb.dbo.sysjobactivity` where `start_execution_date IS NOT NULL AND stop_execution_date IS NULL`) lists currently executing Agent jobs and active step IDs.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Calling `EXEC msdb.dbo.sp_help_jobactivity` (or querying `msdb.dbo.sysjobactivity` where `start_execution_date IS NOT NULL AND stop_execution_date IS NULL`) lists currently executing Agent jobs and active step IDs.
- **C:** Correct. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. In this scenario: Calling `EXEC msdb.dbo.sp_help_jobactivity` (or querying `msdb.dbo.sysjobactivity` where `start_execution_date IS NOT NULL AND stop_execution_date IS NULL`) lists currently executing Agent jobs and active step IDs.
- **D:** Incorrect for this requirement. BYOK TDE wraps the symmetric Database Encryption Key (`DEK`) with an asymmetric RSA key in Key Vault or Managed HSM so security admins control key rotation and instant revocation. Why the keyed choice wins: Calling `EXEC msdb.dbo.sp_help_jobactivity` (or querying `msdb.dbo.sysjobactivity` where `start_execution_date IS NOT NULL AND stop_execution_date IS NULL`) lists currently executing Agent jobs and active step IDs.

### Question 59 — A

Answer: Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`. Setting `enabledForTemplateDeployment: true` (`Azure Resource Manager for template deployment` + `Key Vault Secrets User` RBAC for the deploying principal) authorizes ARM to resolve Key Vault secret references. Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. Local study-map skill 4.3 (Automate Idempotent Deployment Using Bicep and ARM Templates with `@secure()` Key Vault References & `what-if`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Deploy Azure SQL resources using Bicep and Azure Resource Manager (ARM) templates (https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-Quickstart-bicep).

- **A:** Correct. Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. In this scenario: Setting `enabledForTemplateDeployment: true` (`Azure Resource Manager for template deployment` + `Key Vault Secrets User` RBAC for the deploying principal) authorizes ARM to resolve Key Vault secret references.
- **B:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Setting `enabledForTemplateDeployment: true` (`Azure Resource Manager for template deployment` + `Key Vault Secrets User` RBAC for the deploying principal) authorizes ARM to resolve Key Vault secret references.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Setting `enabledForTemplateDeployment: true` (`Azure Resource Manager for template deployment` + `Key Vault Secrets User` RBAC for the deploying principal) authorizes ARM to resolve Key Vault secret references.
- **D:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Setting `enabledForTemplateDeployment: true` (`Azure Resource Manager for template deployment` + `Key Vault Secrets User` RBAC for the deploying principal) authorizes ARM to resolve Key Vault secret references.

### Question 60 — A

Answer: Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`). `az sql db copy` creates an independent transactionally consistent copy of an Azure SQL Database onto the same or a target logical SQL server. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. Local study-map skill 4.4 (Automate Azure SQL Provisioning and Day-2 Management Using Azure PowerShell (`Az.Sql`) and Azure CLI (`az sql`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL management using Azure PowerShell and Azure CLI (https://learn.microsoft.com/en-us/azure/azure-sql/database/scripts/create-and-configure-database-powershell).

- **A:** Correct. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. In this scenario: `az sql db copy` creates an independent transactionally consistent copy of an Azure SQL Database onto the same or a target logical SQL server.
- **B:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: `az sql db copy` creates an independent transactionally consistent copy of an Azure SQL Database onto the same or a target logical SQL server.
- **C:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: `az sql db copy` creates an independent transactionally consistent copy of an Azure SQL Database onto the same or a target logical SQL server.
- **D:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: `az sql db copy` creates an independent transactionally consistent copy of an Azure SQL Database onto the same or a target logical SQL server.

### Question 61 — C

Answer: Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`). `New-AzSqlVM` registers the existing `Microsoft.Compute/virtualMachines` instance as a `Microsoft.SqlVirtualMachine` resource in Full management mode. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. Local study-map skill 4.4 (Automate Azure SQL Provisioning and Day-2 Management Using Azure PowerShell (`Az.Sql`) and Azure CLI (`az sql`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL management using Azure PowerShell and Azure CLI (https://learn.microsoft.com/en-us/azure/azure-sql/database/scripts/create-and-configure-database-powershell).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `New-AzSqlVM` registers the existing `Microsoft.Compute/virtualMachines` instance as a `Microsoft.SqlVirtualMachine` resource in Full management mode.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: `New-AzSqlVM` registers the existing `Microsoft.Compute/virtualMachines` instance as a `Microsoft.SqlVirtualMachine` resource in Full management mode.
- **C:** Correct. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. In this scenario: `New-AzSqlVM` registers the existing `Microsoft.Compute/virtualMachines` instance as a `Microsoft.SqlVirtualMachine` resource in Full management mode.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: `New-AzSqlVM` registers the existing `Microsoft.Compute/virtualMachines` instance as a `Microsoft.SqlVirtualMachine` resource in Full management mode.

### Question 62 — B

Answer: Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules. Logical Azure SQL Server names (`<name>.database.windows.net`) occupy a **globally unique** public DNS namespace across all Azure tenants worldwide; append a deterministic `uniqueString(resourceGroup().id)` suffix in Bicep. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. Local study-map skill 4.5 (Monitor and Troubleshoot Automated Deployments (`CorrelationId`, Quota, SQL MI Subnet Delegation/UDR/NSG)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot ARM/Bicep template and SQL Managed Instance subnet deployment errors (https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/common-deployment-errors).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Logical Azure SQL Server names (`<name>.database.windows.net`) occupy a **globally unique** public DNS namespace across all Azure tenants worldwide; append a deterministic `uniqueString(resourceGroup().id)` suffix in Bicep.
- **B:** Correct. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. In this scenario: Logical Azure SQL Server names (`<name>.database.windows.net`) occupy a **globally unique** public DNS namespace across all Azure tenants worldwide; append a deterministic `uniqueString(resourceGroup().id)` suffix in Bicep.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Logical Azure SQL Server names (`<name>.database.windows.net`) occupy a **globally unique** public DNS namespace across all Azure tenants worldwide; append a deterministic `uniqueString(resourceGroup().id)` suffix in Bicep.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Logical Azure SQL Server names (`<name>.database.windows.net`) occupy a **globally unique** public DNS namespace across all Azure tenants worldwide; append a deterministic `uniqueString(resourceGroup().id)` suffix in Bicep.

### Question 63 — C

Answer: No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent. No — exporting `.bacpac` directly from an active write-heavy OLTP database produces torn cross-table state; run `az sql db copy`, export from the static copy, and delete the copy afterward. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Local study-map skill 4.5 (Monitor and Troubleshoot Automated Deployments (`CorrelationId`, Quota, SQL MI Subnet Delegation/UDR/NSG)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot ARM/Bicep template and SQL Managed Instance subnet deployment errors (https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/common-deployment-errors).

- **A:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: No — exporting `.bacpac` directly from an active write-heavy OLTP database produces torn cross-table state; run `az sql db copy`, export from the static copy, and delete the copy afterward.
- **B:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: No — exporting `.bacpac` directly from an active write-heavy OLTP database produces torn cross-table state; run `az sql db copy`, export from the static copy, and delete the copy afterward.
- **C:** Correct. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. In this scenario: No — exporting `.bacpac` directly from an active write-heavy OLTP database produces torn cross-table state; run `az sql db copy`, export from the static copy, and delete the copy afterward.
- **D:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: No — exporting `.bacpac` directly from an active write-heavy OLTP database produces torn cross-table state; run `az sql db copy`, export from the static copy, and delete the copy afterward.

### Question 64 — C

Answer: Create S1+ Job Database & Elastic Job Agent with UAMI → Create contained UAMI user on target DBs with needed permissions → Define Target Group (`jobs.sp_add_target_group_member`) → Add T-SQL steps & schedule (`jobs.sp_add_job`). Provision an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and add T-SQL steps/schedule (`jobs.sp_add_job`). Modern Elastic Jobs use a dedicated S1+ job database, an Elastic Job Agent assigned a User-Assigned Managed Identity (UAMI) authorized on target databases, a target group, and scheduled T-SQL steps. Local study-map skill 4.6 (Create and Configure Azure SQL Database Elastic Jobs Across Target Groups Using User-Assigned Managed Identity), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Elastic jobs in Azure SQL Database with Managed Identity authentication (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-jobs-overview).

- **A:** Incorrect for this requirement. Incorrect workflow: Elastic Job databases require S1 or higher, target groups must exist before binding executions, NTLM local accounts are invalid in SQL DB, and `msdb` belongs to SQL Agent. Why the keyed choice wins: Provision an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and add T-SQL steps/schedule (`jobs.sp_add_job`).
- **B:** Incorrect for this requirement. Incorrect workflow: Elastic Job Agents target Azure SQL servers, elastic pools, and databases using Managed Identity—never Cosmos DB containers or hardcoded Git secrets. Why the keyed choice wins: Provision an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and add T-SQL steps/schedule (`jobs.sp_add_job`).
- **C:** Correct. Modern Elastic Jobs use a dedicated S1+ job database, an Elastic Job Agent assigned a User-Assigned Managed Identity (UAMI) authorized on target databases, a target group, and scheduled T-SQL steps. In this scenario: Provision an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and add T-SQL steps/schedule (`jobs.sp_add_job`).
- **D:** Incorrect for this requirement. Incorrect workflow: single Azure SQL Databases do not have SQL Server Agent or cross-DB linked servers in the same way as SQL MI; Elastic Jobs fan out T-SQL asynchronously. Why the keyed choice wins: Provision an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and add T-SQL steps/schedule (`jobs.sp_add_job`).

### Question 65 — B

Answer: Azure SQL Database Elastic Job Agent (`jobs.sp_add_job`) authenticating to Target Groups across servers/pools via a User-Assigned Managed Identity (`UAMI`). Call `EXEC jobs.sp_add_target_group_member` with `@membership_type = 'Exclude'` and `@target_type = 'SqlDatabase'` for `SupplierArchive2020` alongside the `'Include'` member for `pool-suppliers`. Elastic Jobs fan out T-SQL maintenance and schema scripts asynchronously across hundreds of Azure SQL Databases, elastic pools, and subscriptions using passwordless UAMI authentication. Local study-map skill 4.6 (Create and Configure Azure SQL Database Elastic Jobs Across Target Groups Using User-Assigned Managed Identity), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Elastic jobs in Azure SQL Database with Managed Identity authentication (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-jobs-overview).

- **A:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: Call `EXEC jobs.sp_add_target_group_member` with `@membership_type = 'Exclude'` and `@target_type = 'SqlDatabase'` for `SupplierArchive2020` alongside the `'Include'` member for `pool-suppliers`.
- **B:** Correct. Elastic Jobs fan out T-SQL maintenance and schema scripts asynchronously across hundreds of Azure SQL Databases, elastic pools, and subscriptions using passwordless UAMI authentication. In this scenario: Call `EXEC jobs.sp_add_target_group_member` with `@membership_type = 'Exclude'` and `@target_type = 'SqlDatabase'` for `SupplierArchive2020` alongside the `'Include'` member for `pool-suppliers`.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Call `EXEC jobs.sp_add_target_group_member` with `@membership_type = 'Exclude'` and `@target_type = 'SqlDatabase'` for `SupplierArchive2020` alongside the `'Include'` member for `pool-suppliers`.
- **D:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Call `EXEC jobs.sp_add_target_group_member` with `@membership_type = 'Exclude'` and `@target_type = 'SqlDatabase'` for `SupplierArchive2020` alongside the `'Include'` member for `pool-suppliers`.

### Question 66 — D

Answer: Azure Automation PowerShell / Python runbooks (or Azure Functions / Logic Apps) using a System-Assigned Managed Identity on a recurring schedule. An Azure Automation PowerShell runbook authenticating with its System-Assigned Managed Identity (`Start-AzVM` / `Stop-AzVM -Force`) enforces ordered startup/shutdown schedules without extra compute infrastructure. Azure Automation runbooks authenticate via Managed Identity (`Connect-AzAccount -Identity`) to scale vCores/Elastic Pools on schedule, rotate keys, or orchestrate hybrid maintenance via Hybrid Workers. Local study-map skill 4.7 (Automate Database Maintenance and Scaling Using Azure Automation Runbooks, Logic Apps, and Azure Functions), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL maintenance tasks with Azure Automation, Logic Apps, and Functions (https://learn.microsoft.com/en-us/azure/automation/overview).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: An Azure Automation PowerShell runbook authenticating with its System-Assigned Managed Identity (`Start-AzVM` / `Stop-AzVM -Force`) enforces ordered startup/shutdown schedules without extra compute infrastructure.
- **B:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: An Azure Automation PowerShell runbook authenticating with its System-Assigned Managed Identity (`Start-AzVM` / `Stop-AzVM -Force`) enforces ordered startup/shutdown schedules without extra compute infrastructure.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: An Azure Automation PowerShell runbook authenticating with its System-Assigned Managed Identity (`Start-AzVM` / `Stop-AzVM -Force`) enforces ordered startup/shutdown schedules without extra compute infrastructure.
- **D:** Correct. Azure Automation runbooks authenticate via Managed Identity (`Connect-AzAccount -Identity`) to scale vCores/Elastic Pools on schedule, rotate keys, or orchestrate hybrid maintenance via Hybrid Workers. In this scenario: An Azure Automation PowerShell runbook authenticating with its System-Assigned Managed Identity (`Start-AzVM` / `Stop-AzVM -Force`) enforces ordered startup/shutdown schedules without extra compute infrastructure.

### Question 67 — A

Answer: No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases. No — Resource Governor is unsupported in single Azure SQL Databases; throttle query memory grants via `MAX_GRANT_PERCENT` hints / Query Store hints or offload reads to a secondary replica. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. Local study-map skill 4.7 (Automate Database Maintenance and Scaling Using Azure Automation Runbooks, Logic Apps, and Azure Functions), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL maintenance tasks with Azure Automation, Logic Apps, and Functions (https://learn.microsoft.com/en-us/azure/automation/overview).

- **A:** Correct. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. In this scenario: No — Resource Governor is unsupported in single Azure SQL Databases; throttle query memory grants via `MAX_GRANT_PERCENT` hints / Query Store hints or offload reads to a secondary replica.
- **B:** Incorrect for this requirement. SQL Server write-ahead logging performs sequential unbuffered writes; enabling `ReadOnly` or `ReadWrite` host caching on `.ldf` disks degrades throughput or risks corruption. Why the keyed choice wins: No — Resource Governor is unsupported in single Azure SQL Databases; throttle query memory grants via `MAX_GRANT_PERCENT` hints / Query Store hints or offload reads to a secondary replica.
- **C:** Incorrect for this requirement. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Why the keyed choice wins: No — Resource Governor is unsupported in single Azure SQL Databases; throttle query memory grants via `MAX_GRANT_PERCENT` hints / Query Store hints or offload reads to a secondary replica.
- **D:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: No — Resource Governor is unsupported in single Azure SQL Databases; throttle query memory grants via `MAX_GRANT_PERCENT` hints / Query Store hints or offload reads to a secondary replica.

### Question 68 — B

Answer: Configure Azure Monitor Metric / Log Alert rules routed to Action Groups and query `jobs.job_executions` in the Elastic Job database to diagnose step failures. Although the User-Assigned Managed Identity was attached to the Elastic Job Agent, those 4 databases are missing `CREATE USER [<uami-name>] FROM EXTERNAL PROVIDER` and the required database role permissions. Action Groups dispatch email/SMS/webhook/Logic App notifications when alert thresholds fire, while `jobs.job_executions` exposes per-target error messages, retries, and timeouts for Elastic Jobs. Local study-map skill 4.8 (Configure Azure Monitor Action Group Alerts on Database Tasks and Troubleshoot `jobs.job_executions`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure Azure Monitor alerts and troubleshoot Elastic Jobs and automated runbooks (https://learn.microsoft.com/en-us/azure/azure-sql/database/alerts-insights-configure-portal).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Although the User-Assigned Managed Identity was attached to the Elastic Job Agent, those 4 databases are missing `CREATE USER [<uami-name>] FROM EXTERNAL PROVIDER` and the required database role permissions.
- **B:** Correct. Action Groups dispatch email/SMS/webhook/Logic App notifications when alert thresholds fire, while `jobs.job_executions` exposes per-target error messages, retries, and timeouts for Elastic Jobs. In this scenario: Although the User-Assigned Managed Identity was attached to the Elastic Job Agent, those 4 databases are missing `CREATE USER [<uami-name>] FROM EXTERNAL PROVIDER` and the required database role permissions.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Although the User-Assigned Managed Identity was attached to the Elastic Job Agent, those 4 databases are missing `CREATE USER [<uami-name>] FROM EXTERNAL PROVIDER` and the required database role permissions.
- **D:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Although the User-Assigned Managed Identity was attached to the Elastic Job Agent, those 4 databases are missing `CREATE USER [<uami-name>] FROM EXTERNAL PROVIDER` and the required database role permissions.

### Question 69 — D

Answer: Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`). Configuring a cross-region Failover Group between West Europe and North Europe provides automatic regional failover with an SLA-backed `RPO = 5s` (planned `RPO = 0`) and `RTO = 1h`. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. Local study-map skill 5.1 (Recommend HA/DR Architectures Based on RPO and RTO (`Zone Redundant`, `Failover Groups`, `Geo-Restore`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Business continuity, RPO/RTO targets, and high availability in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recovery-hadr-overview).

- **A:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Configuring a cross-region Failover Group between West Europe and North Europe provides automatic regional failover with an SLA-backed `RPO = 5s` (planned `RPO = 0`) and `RTO = 1h`.
- **B:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Configuring a cross-region Failover Group between West Europe and North Europe provides automatic regional failover with an SLA-backed `RPO = 5s` (planned `RPO = 0`) and `RTO = 1h`.
- **C:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Configuring a cross-region Failover Group between West Europe and North Europe provides automatic regional failover with an SLA-backed `RPO = 5s` (planned `RPO = 0`) and `RTO = 1h`.
- **D:** Correct. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. In this scenario: Configuring a cross-region Failover Group between West Europe and North Europe provides automatic regional failover with an SLA-backed `RPO = 5s` (planned `RPO = 0`) and `RTO = 1h`.

### Question 70 — D

Answer: Yes — the proposed configuration satisfies every stated technical, security, and availability requirement. Yes — General Purpose vCore supports Zone Redundant HA backed by synchronous `ZRS` storage across three Availability Zones, providing `RPO = 0` zone-outage protection at General Purpose pricing. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. Local study-map skill 5.1 (Recommend HA/DR Architectures Based on RPO and RTO (`Zone Redundant`, `Failover Groups`, `Geo-Restore`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Business continuity, RPO/RTO targets, and high availability in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recovery-hadr-overview).

- **A:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: Yes — General Purpose vCore supports Zone Redundant HA backed by synchronous `ZRS` storage across three Availability Zones, providing `RPO = 0` zone-outage protection at General Purpose pricing.
- **B:** Incorrect for this requirement. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Why the keyed choice wins: Yes — General Purpose vCore supports Zone Redundant HA backed by synchronous `ZRS` storage across three Availability Zones, providing `RPO = 0` zone-outage protection at General Purpose pricing.
- **C:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: Yes — General Purpose vCore supports Zone Redundant HA backed by synchronous `ZRS` storage across three Availability Zones, providing `RPO = 0` zone-outage protection at General Purpose pricing.
- **D:** Correct. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. In this scenario: Yes — General Purpose vCore supports Zone Redundant HA backed by synchronous `ZRS` storage across three Availability Zones, providing `RPO = 0` zone-outage protection at General Purpose pricing.

### Question 71 — B

Answer: Hybrid DR using Managed Instance link with bidirectional online failover between SQL Server 2022 and Azure SQL Managed Instance. Managed Instance link with SQL Server 2022 uses a distributed Availability Group to replicate continuously and execute bidirectional online planned failovers between SQL Server 2022 and SQL MI. SQL Server 2022 supports two-way online planned failover back and forth with Azure SQL Managed Instance via Managed Instance link (whereas SQL Server 2016–2019 link failover is one-way to Azure). Local study-map skill 5.2 (Evaluate Hybrid HA/DR (`Managed Instance Link` Bidirectional SQL 2022 Failover) and Azure-Specific HA Tiers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Hybrid HA/DR with Managed Instance link and distributed Availability Groups (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-disaster-recovery).

- **A:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: Managed Instance link with SQL Server 2022 uses a distributed Availability Group to replicate continuously and execute bidirectional online planned failovers between SQL Server 2022 and SQL MI.
- **B:** Correct. SQL Server 2022 supports two-way online planned failover back and forth with Azure SQL Managed Instance via Managed Instance link (whereas SQL Server 2016–2019 link failover is one-way to Azure). In this scenario: Managed Instance link with SQL Server 2022 uses a distributed Availability Group to replicate continuously and execute bidirectional online planned failovers between SQL Server 2022 and SQL MI.
- **C:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Managed Instance link with SQL Server 2022 uses a distributed Availability Group to replicate continuously and execute bidirectional online planned failovers between SQL Server 2022 and SQL MI.
- **D:** Incorrect for this requirement. Managed Instance link online failback from SQL MI to SQL Server requires SQL Server 2022 or later; SQL Server 2016 and 2019 support one-way migration into SQL MI only. Why the keyed choice wins: Managed Instance link with SQL Server 2022 uses a distributed Availability Group to replicate continuously and execute bidirectional online planned failovers between SQL Server 2022 and SQL MI.

### Question 72 — D

Answer: Provision secondary SQL server with matching firewall/Private Link & Entra admin → Create Failover Group with coupled DBs → Point apps to `<fog>.database.windows.net` & `.secondary` → Run planned `Switch-AzSqlDatabaseFailoverGroup` drill. Mirror network/Entra configs on the secondary server, place all four MES DBs in one Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and run planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback. A resilient Failover Group mirrors security/network configs on the secondary server, groups coupled databases under stable read-write and read-only listeners, and validates readiness via planned zero-data-loss failover. Local study-map skill 5.3 (Plan Non-Disruptive HA/DR Failover Drills, Listener Redirection Validation, and Read-Only Secondary Testing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Disaster recovery drills and failover testing for Azure SQL solutions (https://learn.microsoft.com/en-us/azure/azure-sql/database/disaster-recovery-drills).

- **A:** Incorrect for this requirement. Incorrect workflow: forced failover with `AllowDataLoss` risks dropping uncommitted transactions during drills, and hardcoding regional server names breaks automatic client redirection. Why the keyed choice wins: Mirror network/Entra configs on the secondary server, place all four MES DBs in one Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and run planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback.
- **B:** Incorrect for this requirement. Incorrect workflow: deleting production databases and manually rewriting connection strings causes hours of avoidable downtime instead of testing non-disruptive Failover Group listener failover. Why the keyed choice wins: Mirror network/Entra configs on the secondary server, place all four MES DBs in one Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and run planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback.
- **C:** Incorrect for this requirement. Incorrect workflow: Failover Groups span distinct regions, replicate user databases rather than `master`/`tempdb`, and `.secondary.database.windows.net` is strictly read-only. Why the keyed choice wins: Mirror network/Entra configs on the secondary server, place all four MES DBs in one Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and run planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback.
- **D:** Correct. A resilient Failover Group mirrors security/network configs on the secondary server, groups coupled databases under stable read-write and read-only listeners, and validates readiness via planned zero-data-loss failover. In this scenario: Mirror network/Entra configs on the secondary server, place all four MES DBs in one Failover Group, point apps to `<fog>.database.windows.net` / `.secondary`, and run planned `Switch-AzSqlDatabaseFailoverGroup` failover and failback.

### Question 73 — A

Answer: Non-disruptive DR readiness drill executing a planned zero-data-loss Failover Group switch (`Switch-AzSqlDatabaseFailoverGroup`), validating app listeners, and failing back. Running `ALTER AVAILABILITY GROUP [AG_ERP] FAILOVER;` on a `SYNCHRONIZED` synchronous-commit secondary replica performs a planned zero-data-loss switch (never use `FORCE_FAILOVER_ALLOW_DATA_LOSS` for routine drills). Planned failover synchronizes pending log records before switching roles (`RPO = 0`), validating secondary firewall/Entra configs and `<fog>.database.windows.net` DNS redirection safely. Local study-map skill 5.3 (Plan Non-Disruptive HA/DR Failover Drills, Listener Redirection Validation, and Read-Only Secondary Testing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Disaster recovery drills and failover testing for Azure SQL solutions (https://learn.microsoft.com/en-us/azure/azure-sql/database/disaster-recovery-drills).

- **A:** Correct. Planned failover synchronizes pending log records before switching roles (`RPO = 0`), validating secondary firewall/Entra configs and `<fog>.database.windows.net` DNS redirection safely. In this scenario: Running `ALTER AVAILABILITY GROUP [AG_ERP] FAILOVER;` on a `SYNCHRONIZED` synchronous-commit secondary replica performs a planned zero-data-loss switch (never use `FORCE_FAILOVER_ALLOW_DATA_LOSS` for routine drills).
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Running `ALTER AVAILABILITY GROUP [AG_ERP] FAILOVER;` on a `SYNCHRONIZED` synchronous-commit secondary replica performs a planned zero-data-loss switch (never use `FORCE_FAILOVER_ALLOW_DATA_LOSS` for routine drills).
- **C:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Running `ALTER AVAILABILITY GROUP [AG_ERP] FAILOVER;` on a `SYNCHRONIZED` synchronous-commit secondary replica performs a planned zero-data-loss switch (never use `FORCE_FAILOVER_ALLOW_DATA_LOSS` for routine drills).
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Running `ALTER AVAILABILITY GROUP [AG_ERP] FAILOVER;` on a `SYNCHRONIZED` synchronous-commit secondary replica performs a planned zero-data-loss switch (never use `FORCE_FAILOVER_ALLOW_DATA_LOSS` for routine drills).

### Question 74 — C

Answer: No — taking an ad-hoc non-`COPY_ONLY` full backup resets the differential base and breaks downstream differential restores. No — omitting `WITH COPY_ONLY` reset `differential_base_lsn` to the deleted Tuesday `Adhoc.bak` file, rendering Wednesday's Differential unusable on top of Sunday's Full backup. A standard `BACKUP DATABASE` updates the differential base LSN; ad-hoc exports on SQL Managed Instance or Availability Groups must specify `WITH COPY_ONLY` to preserve the backup chain. Local study-map skill 5.4 (Recommend Backup & Restore Strategies (`COPY_ONLY` on MI/AGs and Azure Backup SQL-Aware Policies on VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated backups, COPY_ONLY backups, and Azure Backup for SQL Server in Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-overview).

- **A:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: No — omitting `WITH COPY_ONLY` reset `differential_base_lsn` to the deleted Tuesday `Adhoc.bak` file, rendering Wednesday's Differential unusable on top of Sunday's Full backup.
- **B:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: No — omitting `WITH COPY_ONLY` reset `differential_base_lsn` to the deleted Tuesday `Adhoc.bak` file, rendering Wednesday's Differential unusable on top of Sunday's Full backup.
- **C:** Correct. A standard `BACKUP DATABASE` updates the differential base LSN; ad-hoc exports on SQL Managed Instance or Availability Groups must specify `WITH COPY_ONLY` to preserve the backup chain. In this scenario: No — omitting `WITH COPY_ONLY` reset `differential_base_lsn` to the deleted Tuesday `Adhoc.bak` file, rendering Wednesday's Differential unusable on top of Sunday's Full backup.
- **D:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: No — omitting `WITH COPY_ONLY` reset `differential_base_lsn` to the deleted Tuesday `Adhoc.bak` file, rendering Wednesday's Differential unusable on top of Sunday's Full backup.

### Question 75 — B

Answer: Use `BACKUP DATABASE ... WITH COPY_ONLY` for ad-hoc exports on SQL MI / AGs, and Azure Backup Recovery Services Vault SQL-aware policies (`15-min` log RPO) on SQL VMs. Conflicting non-`COPY_ONLY` VSS/VDI full backups break differential base LSN tracking and truncate transaction logs out of sequence, causing Azure Backup log chain validation errors. `COPY_ONLY` preserves the differential and log backup chain, while Azure Backup for SQL Server in Azure VMs automates application-consistent Full, Differential, and 15-minute Transaction Log backups. Local study-map skill 5.4 (Recommend Backup & Restore Strategies (`COPY_ONLY` on MI/AGs and Azure Backup SQL-Aware Policies on VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated backups, COPY_ONLY backups, and Azure Backup for SQL Server in Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-overview).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Conflicting non-`COPY_ONLY` VSS/VDI full backups break differential base LSN tracking and truncate transaction logs out of sequence, causing Azure Backup log chain validation errors.
- **B:** Correct. `COPY_ONLY` preserves the differential and log backup chain, while Azure Backup for SQL Server in Azure VMs automates application-consistent Full, Differential, and 15-minute Transaction Log backups. In this scenario: Conflicting non-`COPY_ONLY` VSS/VDI full backups break differential base LSN tracking and truncate transaction logs out of sequence, causing Azure Backup log chain validation errors.
- **C:** Incorrect for this requirement. A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs. Why the keyed choice wins: Conflicting non-`COPY_ONLY` VSS/VDI full backups break differential base LSN tracking and truncate transaction logs out of sequence, causing Azure Backup log chain validation errors.
- **D:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Conflicting non-`COPY_ONLY` VSS/VDI full backups break differential base LSN tracking and truncate transaction logs out of sequence, causing Azure Backup log chain validation errors.

### Question 76 — A

Answer: Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback. Yes — Azure SQL Managed Instance supports restoring automated PITR backups either onto the same SQL Managed Instance under a new database name or onto a different SQL Managed Instance in the same subscription/region (or paired geo-region via Geo-Restore). Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. Local study-map skill 5.5 (Perform Native Restores, Point-in-Time Restore (`1–35d` PITR), Deleted-DB Restore, and `ADR` Instant Rollback), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Point-in-time restore (PITR), Accelerated Database Recovery (ADR), and deleted DB restore (https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups).

- **A:** Correct. Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. In this scenario: Yes — Azure SQL Managed Instance supports restoring automated PITR backups either onto the same SQL Managed Instance under a new database name or onto a different SQL Managed Instance in the same subscription/region (or paired geo-region via Geo-Restore).
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Yes — Azure SQL Managed Instance supports restoring automated PITR backups either onto the same SQL Managed Instance under a new database name or onto a different SQL Managed Instance in the same subscription/region (or paired geo-region via Geo-Restore).
- **C:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: Yes — Azure SQL Managed Instance supports restoring automated PITR backups either onto the same SQL Managed Instance under a new database name or onto a different SQL Managed Instance in the same subscription/region (or paired geo-region via Geo-Restore).
- **D:** Incorrect for this requirement. Short-Term PITR caps at `35` days (`1–35` days); multi-year retention up to `10 years` with WORM deletion lock requires Long-Term Retention (`LTR`) with time-based immutability. Why the keyed choice wins: Yes — Azure SQL Managed Instance supports restoring automated PITR backups either onto the same SQL Managed Instance under a new database name or onto a different SQL Managed Instance in the same subscription/region (or paired geo-region via Geo-Restore).

### Question 77 — B

Answer: Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback. Under `ADR`, only tiny non-versioned metadata operations write to the in-memory `sLog`, allowing SQL Server to aggressively truncate inactive `.ldf` virtual log files even while a long-running transaction remains open. Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. Local study-map skill 5.5 (Perform Native Restores, Point-in-Time Restore (`1–35d` PITR), Deleted-DB Restore, and `ADR` Instant Rollback), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Point-in-time restore (PITR), Accelerated Database Recovery (ADR), and deleted DB restore (https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Under `ADR`, only tiny non-versioned metadata operations write to the in-memory `sLog`, allowing SQL Server to aggressively truncate inactive `.ldf` virtual log files even while a long-running transaction remains open.
- **B:** Correct. Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. In this scenario: Under `ADR`, only tiny non-versioned metadata operations write to the in-memory `sLog`, allowing SQL Server to aggressively truncate inactive `.ldf` virtual log files even while a long-running transaction remains open.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Under `ADR`, only tiny non-versioned metadata operations write to the in-memory `sLog`, allowing SQL Server to aggressively truncate inactive `.ldf` virtual log files even while a long-running transaction remains open.
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Under `ADR`, only tiny non-versioned metadata operations write to the in-memory `sLog`, allowing SQL Server to aggressively truncate inactive `.ldf` virtual log files even while a long-running transaction remains open.

### Question 78 — A, E

Answers: Configure an Azure SQL Long-Term Retention (`LTR`) policy (`WeeklyRetention`, `MonthlyRetention`, `YearlyRetention`, `WeekOfYear`) up to 10 years; Enable and lock time-based immutability (`WORM`) on the LTR backup policy so nobody can shorten retention or delete compliance backups early. Configure an LTR retention policy (`YearlyRetention = P10Y`, `WeekOfYear`) and enable + lock time-based immutability (`WORM`) on the LTR policy. Local study-map skill 5.6 (Configure Long-Term Backup Retention (`LTR` up to `10y`), Time-Based Immutable WORM Locks, and Storage Redundancy), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Long-term backup retention (LTR) and time-based immutable WORM backups in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/long-term-retention-overview).

- **A:** Correct. LTR copies full backups into separate geo-redundant/zone-redundant Azure Blob tiers according to ISO-8601 duration policies (e.g., `P7Y`). In this scenario: Configure an LTR retention policy (`YearlyRetention = P10Y`, `WeekOfYear`) and enable + lock time-based immutability (`WORM`) on the LTR policy.
- **B:** Incorrect for this requirement. Short-Term PITR caps at `35` days (`1–35` days); multi-year retention up to `10 years` with WORM deletion lock requires Long-Term Retention (`LTR`) with time-based immutability. Why the keyed choice wins: Configure an LTR retention policy (`YearlyRetention = P10Y`, `WeekOfYear`) and enable + lock time-based immutability (`WORM`) on the LTR policy.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Configure an LTR retention policy (`YearlyRetention = P10Y`, `WeekOfYear`) and enable + lock time-based immutability (`WORM`) on the LTR policy.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure an LTR retention policy (`YearlyRetention = P10Y`, `WeekOfYear`) and enable + lock time-based immutability (`WORM`) on the LTR policy.
- **E:** Correct. Once locked, time-based LTR immutability enforces write-once-read-many protection against ransomware or rogue privileged admins. In this scenario: Configure an LTR retention policy (`YearlyRetention = P10Y`, `WeekOfYear`) and enable + lock time-based immutability (`WORM`) on the LTR policy.

### Question 79 — D

Answer: Long-Term Retention (`LTR`) weekly/monthly/yearly backups up to `10 years` protected by a locked time-based immutable (`WORM`) policy and `RA-GRS` / `ZRS` backup storage. Setting `--backup-storage-redundancy Zone` (`ZRS`) or `Local` (`LRS`) keeps all backup blobs strictly within the primary Azure region rather than replicating to the paired geo-region (`Geo` / `RA-GRS`). LTR retains compliance backups up to 10 years independently of PITR, and locking time-based immutability prevents even Subscription Owners from deleting backups before expiry. Local study-map skill 5.6 (Configure Long-Term Backup Retention (`LTR` up to `10y`), Time-Based Immutable WORM Locks, and Storage Redundancy), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Long-term backup retention (LTR) and time-based immutable WORM backups in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/long-term-retention-overview).

- **A:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Setting `--backup-storage-redundancy Zone` (`ZRS`) or `Local` (`LRS`) keeps all backup blobs strictly within the primary Azure region rather than replicating to the paired geo-region (`Geo` / `RA-GRS`).
- **B:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Setting `--backup-storage-redundancy Zone` (`ZRS`) or `Local` (`LRS`) keeps all backup blobs strictly within the primary Azure region rather than replicating to the paired geo-region (`Geo` / `RA-GRS`).
- **C:** Incorrect for this requirement. Short-Term PITR caps at `35` days (`1–35` days); multi-year retention up to `10 years` with WORM deletion lock requires Long-Term Retention (`LTR`) with time-based immutability. Why the keyed choice wins: Setting `--backup-storage-redundancy Zone` (`ZRS`) or `Local` (`LRS`) keeps all backup blobs strictly within the primary Azure region rather than replicating to the paired geo-region (`Geo` / `RA-GRS`).
- **D:** Correct. LTR retains compliance backups up to 10 years independently of PITR, and locking time-based immutability prevents even Subscription Owners from deleting backups before expiry. In this scenario: Setting `--backup-storage-redundancy Zone` (`ZRS`) or `Local` (`LRS`) keeps all backup blobs strictly within the primary Azure region rather than replicating to the paired geo-region (`Geo` / `RA-GRS`).

### Question 80 — C, E

Answers: Create a SQL Server `CREDENTIAL` (`IDENTITY = 'Managed Identity'` or `'SHARED ACCESS SIGNATURE'`) matching the Azure Blob container URL; Stripe `BACKUP DATABASE` across multiple `TO URL = 'https://...bak'` block blob targets with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`. Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob container URL, and stripe `BACKUP DATABASE` across up to 64 `TO URL` block blobs with `COMPRESSION` and tuned `MAXTRANSFERSIZE`. Local study-map skill 5.7 (Back Up to and Restore from Azure Blob Storage URL Using T-SQL Stripes (`TO URL`) and Managed Identity / SAS), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server backup to URL and restore from Azure Blob Storage with Managed Identity or SAS (https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url-azure-blob-storage).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob container URL, and stripe `BACKUP DATABASE` across up to 64 `TO URL` block blobs with `COMPRESSION` and tuned `MAXTRANSFERSIZE`.
- **B:** Incorrect for this requirement. A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs. Why the keyed choice wins: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob container URL, and stripe `BACKUP DATABASE` across up to 64 `TO URL` block blobs with `COMPRESSION` and tuned `MAXTRANSFERSIZE`.
- **C:** Correct. Multiple `URL` targets write to Azure Block Blobs in parallel, scaling single backups up to ~12.8 TB (`64` stripes) with maximum throughput. In this scenario: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob container URL, and stripe `BACKUP DATABASE` across up to 64 `TO URL` block blobs with `COMPRESSION` and tuned `MAXTRANSFERSIZE`.
- **D:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob container URL, and stripe `BACKUP DATABASE` across up to 64 `TO URL` block blobs with `COMPRESSION` and tuned `MAXTRANSFERSIZE`.
- **E:** Correct. SQL Server and SQL MI authenticate `BACKUP TO URL` / `RESTORE FROM URL` requests to Azure Storage via a server-level credential. In this scenario: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob container URL, and stripe `BACKUP DATABASE` across up to 64 `TO URL` block blobs with `COMPRESSION` and tuned `MAXTRANSFERSIZE`.

### Question 81 — D

Answer: Striped T-SQL `BACKUP DATABASE ... TO URL = ...` across up to 64 block blobs (`MAXTRANSFERSIZE`, `COMPRESSION`) authenticated via `Managed Identity` or `SHARED ACCESS SIGNATURE` Credential. Taking a **tail-log backup** (`BACKUP LOG ... WITH NORECOVERY`, or `WITH CONTINUE_AFTER_ERROR` if `.mdf` disks are damaged) captures every committed log record up to the failure instant for zero-data-loss recovery. Backing up to multiple URLs creates block blobs supporting up to ~12.8 TB striped backups (`200 GB+` per blob, unlike legacy single-page-blob 1 TB limits) using `CREATE CREDENTIAL`. Local study-map skill 5.7 (Back Up to and Restore from Azure Blob Storage URL Using T-SQL Stripes (`TO URL`) and Managed Identity / SAS), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server backup to URL and restore from Azure Blob Storage with Managed Identity or SAS (https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url-azure-blob-storage).

- **A:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Taking a **tail-log backup** (`BACKUP LOG ... WITH NORECOVERY`, or `WITH CONTINUE_AFTER_ERROR` if `.mdf` disks are damaged) captures every committed log record up to the failure instant for zero-data-loss recovery.
- **B:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: Taking a **tail-log backup** (`BACKUP LOG ... WITH NORECOVERY`, or `WITH CONTINUE_AFTER_ERROR` if `.mdf` disks are damaged) captures every committed log record up to the failure instant for zero-data-loss recovery.
- **C:** Incorrect for this requirement. A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs. Why the keyed choice wins: Taking a **tail-log backup** (`BACKUP LOG ... WITH NORECOVERY`, or `WITH CONTINUE_AFTER_ERROR` if `.mdf` disks are damaged) captures every committed log record up to the failure instant for zero-data-loss recovery.
- **D:** Correct. Backing up to multiple URLs creates block blobs supporting up to ~12.8 TB striped backups (`200 GB+` per blob, unlike legacy single-page-blob 1 TB limits) using `CREATE CREDENTIAL`. In this scenario: Taking a **tail-log backup** (`BACKUP LOG ... WITH NORECOVERY`, or `WITH CONTINUE_AFTER_ERROR` if `.mdf` disks are damaged) captures every committed log record up to the failure instant for zero-data-loss recovery.

### Question 82 — C

Answer: Failover Groups for automatic multi-database failover behind stable `<fog>.database.windows.net` / `.secondary` listeners vs Active Geo-Replication for up to 4 readable secondaries. Without a Failover Group listener (`<fog>.database.windows.net`), applications must update their connection strings (or custom DNS CNAME / Traffic Manager config) to point to the promoted East US logical server name. Failover Groups fail over coupled databases together and redirect connection strings automatically (`GracePeriodWithDataLossHours >= 1`), whereas Active Geo-Replication supports up to 4 secondaries per DB without automatic listener redirection. Local study-map skill 5.8 (Configure Failover Groups (`<fog>.database.windows.net`, Grace Period) vs Active Geo-Replication (`4` Replicas)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Failover groups and active geo-replication in Azure SQL Database and SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db).

- **A:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Without a Failover Group listener (`<fog>.database.windows.net`), applications must update their connection strings (or custom DNS CNAME / Traffic Manager config) to point to the promoted East US logical server name.
- **B:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Without a Failover Group listener (`<fog>.database.windows.net`), applications must update their connection strings (or custom DNS CNAME / Traffic Manager config) to point to the promoted East US logical server name.
- **C:** Correct. Failover Groups fail over coupled databases together and redirect connection strings automatically (`GracePeriodWithDataLossHours >= 1`), whereas Active Geo-Replication supports up to 4 secondaries per DB without automatic listener redirection. In this scenario: Without a Failover Group listener (`<fog>.database.windows.net`), applications must update their connection strings (or custom DNS CNAME / Traffic Manager config) to point to the promoted East US logical server name.
- **D:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Without a Failover Group listener (`<fog>.database.windows.net`), applications must update their connection strings (or custom DNS CNAME / Traffic Manager config) to point to the promoted East US logical server name.

### Question 83 — A

Answer: Failover Groups for automatic multi-database failover behind stable `<fog>.database.windows.net` / `.secondary` listeners vs Active Geo-Replication for up to 4 readable secondaries. Yes — a single Failover Group on a logical SQL server can include standalone databases and databases across one or more Elastic Pools on that server, failing them over together to matching pools/server in the partner region. Failover Groups fail over coupled databases together and redirect connection strings automatically (`GracePeriodWithDataLossHours >= 1`), whereas Active Geo-Replication supports up to 4 secondaries per DB without automatic listener redirection. Local study-map skill 5.8 (Configure Failover Groups (`<fog>.database.windows.net`, Grace Period) vs Active Geo-Replication (`4` Replicas)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Failover groups and active geo-replication in Azure SQL Database and SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db).

- **A:** Correct. Failover Groups fail over coupled databases together and redirect connection strings automatically (`GracePeriodWithDataLossHours >= 1`), whereas Active Geo-Replication supports up to 4 secondaries per DB without automatic listener redirection. In this scenario: Yes — a single Failover Group on a logical SQL server can include standalone databases and databases across one or more Elastic Pools on that server, failing them over together to matching pools/server in the partner region.
- **B:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Yes — a single Failover Group on a logical SQL server can include standalone databases and databases across one or more Elastic Pools on that server, failing them over together to matching pools/server in the partner region.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Yes — a single Failover Group on a logical SQL server can include standalone databases and databases across one or more Elastic Pools on that server, failing them over together to matching pools/server in the partner region.
- **D:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Yes — a single Failover Group on a logical SQL server can include standalone databases and databases across one or more Elastic Pools on that server, failing them over together to matching pools/server in the partner region.

### Question 84 — C, D

Answers: Configure an Azure Cloud Witness in a standard Storage Account (`LRS`/`ZRS`) to provide lightweight quorum voting for a 2-node WSFC; Deploy a Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` TCP `59999`) listener and set `MultiSubnetFailover=True` on clients. Configure an Azure Cloud Witness for odd-vote WSFC quorum, and set `MultiSubnetFailover=True` on all client connection strings connecting to the multi-subnet/DNN listener. Local study-map skill 5.9 (Configure Always On Availability Groups on SQL MI and Azure VMs (`Cloud Witness`, `DNN`, `ILB` Port `59999`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On availability groups on SQL Server on Azure VMs (Cloud Witness, DNN, ILB) (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/availability-group-overview).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure an Azure Cloud Witness for odd-vote WSFC quorum, and set `MultiSubnetFailover=True` on all client connection strings connecting to the multi-subnet/DNN listener.
- **B:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: Configure an Azure Cloud Witness for odd-vote WSFC quorum, and set `MultiSubnetFailover=True` on all client connection strings connecting to the multi-subnet/DNN listener.
- **C:** Correct. Cloud Witness maintains a tiny blob arbitration file without the cost and patching overhead of running a third witness VM. In this scenario: Configure an Azure Cloud Witness for odd-vote WSFC quorum, and set `MultiSubnetFailover=True` on all client connection strings connecting to the multi-subnet/DNN listener.
- **D:** Correct. `MultiSubnetFailover=True` makes SQL client drivers try all listener IPs in parallel across subnets, cutting cross-subnet AG failover reconnect latency to seconds. In this scenario: Configure an Azure Cloud Witness for odd-vote WSFC quorum, and set `MultiSubnetFailover=True` on all client connection strings connecting to the multi-subnet/DNN listener.
- **E:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Configure an Azure Cloud Witness for odd-vote WSFC quorum, and set `MultiSubnetFailover=True` on all client connection strings connecting to the multi-subnet/DNN listener.

### Question 85 — A

Answer: Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`. SQL Server 2022 **Contained Availability Groups** (`WITH (CONTAINED)`) create dedicated contained `AG_master` and `AG_msdb` system databases that fail over logins, users, and SQL Agent jobs automatically with the AG. Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). Local study-map skill 5.9 (Configure Always On Availability Groups on SQL MI and Azure VMs (`Cloud Witness`, `DNN`, `ILB` Port `59999`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On availability groups on SQL Server on Azure VMs (Cloud Witness, DNN, ILB) (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/availability-group-overview).

- **A:** Correct. Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). In this scenario: SQL Server 2022 **Contained Availability Groups** (`WITH (CONTAINED)`) create dedicated contained `AG_master` and `AG_msdb` system databases that fail over logins, users, and SQL Agent jobs automatically with the AG.
- **B:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: SQL Server 2022 **Contained Availability Groups** (`WITH (CONTAINED)`) create dedicated contained `AG_master` and `AG_msdb` system databases that fail over logins, users, and SQL Agent jobs automatically with the AG.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: SQL Server 2022 **Contained Availability Groups** (`WITH (CONTAINED)`) create dedicated contained `AG_master` and `AG_msdb` system databases that fail over logins, users, and SQL Agent jobs automatically with the AG.
- **D:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: SQL Server 2022 **Contained Availability Groups** (`WITH (CONTAINED)`) create dedicated contained `AG_master` and `AG_msdb` system databases that fail over logins, users, and SQL Agent jobs automatically with the AG.

### Question 86 — D

Answer: Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`). Zone-Redundant (`ZRS`) Premium SSD **Azure Shared Disks** and **Azure Premium Files** (`SMB` shares; alongside Storage Spaces Direct `S2D`) are officially supported shared storage back-ends for Azure VM FCIs. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. Local study-map skill 5.10 (Configure Always On Failover Cluster Instances (`Azure Shared Disks` `ZRS`) and T-SQL Log Shipping on Azure VMs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On Failover Cluster Instances (Azure Shared Disks) and Log Shipping on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/failover-cluster-instance-overview).

- **A:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: Zone-Redundant (`ZRS`) Premium SSD **Azure Shared Disks** and **Azure Premium Files** (`SMB` shares; alongside Storage Spaces Direct `S2D`) are officially supported shared storage back-ends for Azure VM FCIs.
- **B:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: Zone-Redundant (`ZRS`) Premium SSD **Azure Shared Disks** and **Azure Premium Files** (`SMB` shares; alongside Storage Spaces Direct `S2D`) are officially supported shared storage back-ends for Azure VM FCIs.
- **C:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Zone-Redundant (`ZRS`) Premium SSD **Azure Shared Disks** and **Azure Premium Files** (`SMB` shares; alongside Storage Spaces Direct `S2D`) are officially supported shared storage back-ends for Azure VM FCIs.
- **D:** Correct. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. In this scenario: Zone-Redundant (`ZRS`) Premium SSD **Azure Shared Disks** and **Azure Premium Files** (`SMB` shares; alongside Storage Spaces Direct `S2D`) are officially supported shared storage back-ends for Azure VM FCIs.

### Question 87 — B

Answer: Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`). Enable `Disconnect users in the database when restoring backups` in Log Shipping secondary properties so active read sessions are terminated briefly when each `.trn` log batch restores. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. Local study-map skill 5.10 (Configure Always On Failover Cluster Instances (`Azure Shared Disks` `ZRS`) and T-SQL Log Shipping on Azure VMs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On Failover Cluster Instances (Azure Shared Disks) and Log Shipping on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/failover-cluster-instance-overview).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Enable `Disconnect users in the database when restoring backups` in Log Shipping secondary properties so active read sessions are terminated briefly when each `.trn` log batch restores.
- **B:** Correct. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. In this scenario: Enable `Disconnect users in the database when restoring backups` in Log Shipping secondary properties so active read sessions are terminated briefly when each `.trn` log batch restores.
- **C:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Enable `Disconnect users in the database when restoring backups` in Log Shipping secondary properties so active read sessions are terminated briefly when each `.trn` log batch restores.
- **D:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Enable `Disconnect users in the database when restoring backups` in Log Shipping secondary properties so active read sessions are terminated briefly when each `.trn` log batch restores.

### Question 88 — A

Answer: Query `sys.dm_hadr_database_replica_states` (`synchronization_state_desc`, `log_send_queue_size`, `redo_queue_size`) and `sys.dm_geo_replication_link_status`, plus verify NSG probe port `59999`. Executing `ALTER DATABASE [ERP] SET HADR RESUME;` on the suspended replica resumes Always On log transport and redo synchronization immediately. High `log_send_queue_size` indicates network bottlenecks between primary and secondary, high `redo_queue_size` indicates slow redo I/O/CPU or long-running read queries on the secondary, and blocked ILB probe port `59999` breaks AG listener routing. Local study-map skill 5.11 (Monitor and Troubleshoot HA/DR Health (`sys.dm_hadr_database_replica_states`, `redo_queue_size`, `log_send_queue_size`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor and troubleshoot Always On availability groups and geo-replication health (https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/monitor-availability-groups-transact-sql).

- **A:** Correct. High `log_send_queue_size` indicates network bottlenecks between primary and secondary, high `redo_queue_size` indicates slow redo I/O/CPU or long-running read queries on the secondary, and blocked ILB probe port `59999` breaks AG listener routing. In this scenario: Executing `ALTER DATABASE [ERP] SET HADR RESUME;` on the suspended replica resumes Always On log transport and redo synchronization immediately.
- **B:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: Executing `ALTER DATABASE [ERP] SET HADR RESUME;` on the suspended replica resumes Always On log transport and redo synchronization immediately.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Executing `ALTER DATABASE [ERP] SET HADR RESUME;` on the suspended replica resumes Always On log transport and redo synchronization immediately.
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Executing `ALTER DATABASE [ERP] SET HADR RESUME;` on the suspended replica resumes Always On log transport and redo synchronization immediately.

### Question 89 — A

Answer: SQL IaaS Agent Extension in Full management mode paired with Azure Update Manager / Automated Patching. Registering the VM with the SQL IaaS Agent Extension (Full mode) integrated with Azure Update Manager / Automated Patching schedules OS and SQL cumulative updates inside defined maintenance windows. The SQL IaaS Agent Extension unlocks portal license conversion (AHB/PAYG), Automated Backup, Automated Patching windows, Key Vault integration, and storage pool management on SQL VMs. Local study-map skill 1.5 (Deploy Hybrid SQL Server Solutions and Manage Patching (`SQL IaaS Agent Extension` & `Azure Update Manager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server IaaS Agent Extension, Automated Patching, and Azure Update Manager (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-agent-extension-manually-register-single-vm).

- **A:** Correct. The SQL IaaS Agent Extension unlocks portal license conversion (AHB/PAYG), Automated Backup, Automated Patching windows, Key Vault integration, and storage pool management on SQL VMs. In this scenario: Registering the VM with the SQL IaaS Agent Extension (Full mode) integrated with Azure Update Manager / Automated Patching schedules OS and SQL cumulative updates inside defined maintenance windows.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Registering the VM with the SQL IaaS Agent Extension (Full mode) integrated with Azure Update Manager / Automated Patching schedules OS and SQL cumulative updates inside defined maintenance windows.
- **C:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: Registering the VM with the SQL IaaS Agent Extension (Full mode) integrated with Azure Update Manager / Automated Patching schedules OS and SQL cumulative updates inside defined maintenance windows.
- **D:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Registering the VM with the SQL IaaS Agent Extension (Full mode) integrated with Azure Update Manager / Automated Patching schedules OS and SQL cumulative updates inside defined maintenance windows.

### Question 90 — A, B, F

Answers: Configure `ReadOnly` Azure host caching on Premium SSD data disks hosting `.mdf` and `.ndf` database files; Configure `None` Azure host caching on dedicated managed disks hosting `.ldf` SQL Server transaction log files; Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script. Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` log disks, and place `tempdb` files on the local ephemeral NVMe SSD volume. Local study-map skill 1.8 (Configure SQL Server on Azure VMs for Scale and Performance (`ReadOnly`/`None` Host Caching, `tempdb` NVMe, `IFI`/`LPIM`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Performance best practices for SQL Server on Azure Virtual Machines (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-checklist).

- **A:** Correct. Transaction log files perform sequential write-through flushes that do not benefit from read caching and must use `None` host caching. In this scenario: Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` log disks, and place `tempdb` files on the local ephemeral NVMe SSD volume.
- **B:** Correct. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. In this scenario: Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` log disks, and place `tempdb` files on the local ephemeral NVMe SSD volume.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` log disks, and place `tempdb` files on the local ephemeral NVMe SSD volume.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` log disks, and place `tempdb` files on the local ephemeral NVMe SSD volume.
- **E:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` log disks, and place `tempdb` files on the local ephemeral NVMe SSD volume.
- **F:** Correct. `ReadOnly` host caching serves random OLTP data-page reads directly from Azure hypervisor RAM/SSD cache without consuming disk IOPS. In this scenario: Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` log disks, and place `tempdb` files on the local ephemeral NVMe SSD volume.

### Question 91 — B

Answer: Grant `Perform volume maintenance tasks` (Instant File Initialization) and `Lock pages in memory` to the SQL Server service account. Granting `Perform volume maintenance tasks` to the SQL Server service account enables Instant File Initialization (`IFI`) for data files (`.mdf`/`.ndf`), slashing restore and file-growth allocation times (note `.ldf` log files always zero-initialize). Instant File Initialization skips zeroing `.mdf`/`.ndf` data file growth (never `.ldf`), while Lock Pages in Memory prevents Windows from paging the SQL buffer pool to disk. Local study-map skill 1.8 (Configure SQL Server on Azure VMs for Scale and Performance (`ReadOnly`/`None` Host Caching, `tempdb` NVMe, `IFI`/`LPIM`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Performance best practices for SQL Server on Azure Virtual Machines (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-checklist).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Granting `Perform volume maintenance tasks` to the SQL Server service account enables Instant File Initialization (`IFI`) for data files (`.mdf`/`.ndf`), slashing restore and file-growth allocation times (note `.ldf` log files always zero-initialize).
- **B:** Correct. Instant File Initialization skips zeroing `.mdf`/`.ndf` data file growth (never `.ldf`), while Lock Pages in Memory prevents Windows from paging the SQL buffer pool to disk. In this scenario: Granting `Perform volume maintenance tasks` to the SQL Server service account enables Instant File Initialization (`IFI`) for data files (`.mdf`/`.ndf`), slashing restore and file-growth allocation times (note `.ldf` log files always zero-initialize).
- **C:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Granting `Perform volume maintenance tasks` to the SQL Server service account enables Instant File Initialization (`IFI`) for data files (`.mdf`/`.ndf`), slashing restore and file-growth allocation times (note `.ldf` log files always zero-initialize).
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Granting `Perform volume maintenance tasks` to the SQL Server service account enables Instant File Initialization (`IFI`) for data files (`.mdf`/`.ndf`), slashing restore and file-growth allocation times (note `.ldf` log files always zero-initialize).

### Question 92 — A

Answer: Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or `Entra Kerberos`). Configure Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or cloud-native Entra Kerberos realm). Microsoft Entra Kerberos issues Kerberos tickets for SQL Managed Instance without requiring customer-managed Active Directory Domain Services domain controllers inside Azure. Local study-map skill 2.2 (Configure Authentication for SQL Server on Azure VMs and SQL MI (`Microsoft Entra Kerberos` & AD Trusts)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos and AD (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/winauth-azuread-overview).

- **A:** Correct. Microsoft Entra Kerberos issues Kerberos tickets for SQL Managed Instance without requiring customer-managed Active Directory Domain Services domain controllers inside Azure. In this scenario: Configure Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or cloud-native Entra Kerberos realm).
- **B:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Configure Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or cloud-native Entra Kerberos realm).
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or cloud-native Entra Kerberos realm).
- **D:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Configure Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or cloud-native Entra Kerberos realm).

### Question 93 — A

Answer: Remap orphaned database users (`ALTER USER [u] WITH LOGIN = [u]`) and inspect explicit `DENY` permissions via `sys.database_permissions`. Query `sys.database_principals` unmatched in `sys.server_principals` (or `sp_change_users_login 'Report'` on legacy versions) and run `ALTER USER [UserName] WITH LOGIN = [LoginName]` (or migrate to contained Entra users). Restoring a `.bak` onto another instance mismatches login SIDs (fixed via `ALTER USER ... WITH LOGIN`), while an explicit table/schema `DENY` always overrides `db_datareader` role `GRANT`s. Local study-map skill 2.5 (Troubleshoot Authentication and Authorization Issues (Orphaned Users `ALTER USER WITH LOGIN` & `DENY` Precedence)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot SQL login, orphaned user, and Microsoft Entra authorization issues (https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/troubleshoot-orphaned-users-sql-server).

- **A:** Correct. Restoring a `.bak` onto another instance mismatches login SIDs (fixed via `ALTER USER ... WITH LOGIN`), while an explicit table/schema `DENY` always overrides `db_datareader` role `GRANT`s. In this scenario: Query `sys.database_principals` unmatched in `sys.server_principals` (or `sp_change_users_login 'Report'` on legacy versions) and run `ALTER USER [UserName] WITH LOGIN = [LoginName]` (or migrate to contained Entra users).
- **B:** Incorrect for this requirement. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. Why the keyed choice wins: Query `sys.database_principals` unmatched in `sys.server_principals` (or `sp_change_users_login 'Report'` on legacy versions) and run `ALTER USER [UserName] WITH LOGIN = [LoginName]` (or migrate to contained Entra users).
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Query `sys.database_principals` unmatched in `sys.server_principals` (or `sp_change_users_login 'Report'` on legacy versions) and run `ALTER USER [UserName] WITH LOGIN = [LoginName]` (or migrate to contained Entra users).
- **D:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Query `sys.database_principals` unmatched in `sys.server_principals` (or `sp_change_users_login 'Report'` on legacy versions) and run `ALTER USER [UserName] WITH LOGIN = [LoginName]` (or migrate to contained Entra users).

### Question 94 — A

Answer: Column-level encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey`) plus `Minimal TLS version = 1.2`. Column-level symmetric key encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey` / `DecryptByKey`) encrypts sensitive cells inside T-SQL while enforcing `Minimal TLS 1.2` in transit. T-SQL cell-level symmetric key encryption protects specific columns inside the engine while enforcing TLS 1.2+ encrypts all TDS client traffic in transit. Local study-map skill 2.7 (Implement Object/Column-Level Encryption (`Symmetric Keys` / `Certificates`) and Enforce `Minimal TLS 1.2`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Column-level symmetric key encryption and TLS 1.2 in-transit encryption (https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/encrypt-a-column-of-data).

- **A:** Correct. T-SQL cell-level symmetric key encryption protects specific columns inside the engine while enforcing TLS 1.2+ encrypts all TDS client traffic in transit. In this scenario: Column-level symmetric key encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey` / `DecryptByKey`) encrypts sensitive cells inside T-SQL while enforcing `Minimal TLS 1.2` in transit.
- **B:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Column-level symmetric key encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey` / `DecryptByKey`) encrypts sensitive cells inside T-SQL while enforcing `Minimal TLS 1.2` in transit.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Column-level symmetric key encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey` / `DecryptByKey`) encrypts sensitive cells inside T-SQL while enforcing `Minimal TLS 1.2` in transit.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Column-level symmetric key encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey` / `DecryptByKey`) encrypts sensitive cells inside T-SQL while enforcing `Minimal TLS 1.2` in transit.

### Question 95 — A, E

Answers: Create a Windows/SQL Credential and map it to a SQL Server Agent Subsystem Proxy (`CmdExec` / `PowerShell`) instead of granting `sysadmin`; Configure Database Mail, define an Agent Operator, and create SQL Server Agent Alerts for Severity `19–25` and Errors `823`, `824`, and `825`. Configure Database Mail with a SQL Agent Operator attached to Severity `19–25` / Error `823–825` Alerts, and execute PowerShell steps via Credential-backed SQL Agent Subsystem Proxies. Local study-map skill 4.1 (Create and Schedule SQL Server Agent Maintenance Jobs, Proxies, Severity `19–25` Alerts, and Database Mail), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server Agent jobs, schedules, alerts, and Database Mail operators (https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent).

- **A:** Correct. SQL Server Agent proxies let non-`sysadmin` job owners execute external subsystem steps under a scoped least-privilege identity. In this scenario: Configure Database Mail with a SQL Agent Operator attached to Severity `19–25` / Error `823–825` Alerts, and execute PowerShell steps via Credential-backed SQL Agent Subsystem Proxies.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure Database Mail with a SQL Agent Operator attached to Severity `19–25` / Error `823–825` Alerts, and execute PowerShell steps via Credential-backed SQL Agent Subsystem Proxies.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Configure Database Mail with a SQL Agent Operator attached to Severity `19–25` / Error `823–825` Alerts, and execute PowerShell steps via Credential-backed SQL Agent Subsystem Proxies.
- **D:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Configure Database Mail with a SQL Agent Operator attached to Severity `19–25` / Error `823–825` Alerts, and execute PowerShell steps via Credential-backed SQL Agent Subsystem Proxies.
- **E:** Correct. Severity `19–25` and I/O errors `823–825` indicate critical resource exhaustion or storage corruption requiring immediate DBA notification. In this scenario: Configure Database Mail with a SQL Agent Operator attached to Severity `19–25` / Error `823–825` Alerts, and execute PowerShell steps via Credential-backed SQL Agent Subsystem Proxies.

### Question 96 — A, E

Answers: Mark sensitive parameters with `@secure()` in Bicep and pass Key Vault secret references from the parameter file rather than cleartext values; Run `az deployment group what-if` (or `New-AzResourceGroupDeployment -WhatIf`) as a pull-request gate before applying template changes. Mark sensitive parameters `@secure()` referencing Azure Key Vault secrets at deploy time, and run `az deployment group what-if` in pull-request validation gates. Local study-map skill 4.3 (Automate Idempotent Deployment Using Bicep and ARM Templates with `@secure()` Key Vault References & `what-if`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Deploy Azure SQL resources using Bicep and Azure Resource Manager (ARM) templates (https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-Quickstart-bicep).

- **A:** Correct. `@secure()` prevents secret logging in deployment history, while Key Vault references resolve secrets inside ARM at deploy time without exposing them to CI runners. In this scenario: Mark sensitive parameters `@secure()` referencing Azure Key Vault secrets at deploy time, and run `az deployment group what-if` in pull-request validation gates.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Mark sensitive parameters `@secure()` referencing Azure Key Vault secrets at deploy time, and run `az deployment group what-if` in pull-request validation gates.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Mark sensitive parameters `@secure()` referencing Azure Key Vault secrets at deploy time, and run `az deployment group what-if` in pull-request validation gates.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Mark sensitive parameters `@secure()` referencing Azure Key Vault secrets at deploy time, and run `az deployment group what-if` in pull-request validation gates.
- **E:** Correct. `what-if` calculates predicted `Create`, `Modify`, `Delete`, and `Ignore` operations against live Azure SQL resources to catch destructive config drift. In this scenario: Mark sensitive parameters `@secure()` referencing Azure Key Vault secrets at deploy time, and run `az deployment group what-if` in pull-request validation gates.

### Question 97 — D

Answer: Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`. Configure a Windows Server Failover Cluster (`WSFC`) with an Azure Cloud Witness and a Distributed Network Name (`DNN`) listener paired with `MultiSubnetFailover=True` on all client connection strings. Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). Local study-map skill 5.2 (Evaluate Hybrid HA/DR (`Managed Instance Link` Bidirectional SQL 2022 Failover) and Azure-Specific HA Tiers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Hybrid HA/DR with Managed Instance link and distributed Availability Groups (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-disaster-recovery).

- **A:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: Configure a Windows Server Failover Cluster (`WSFC`) with an Azure Cloud Witness and a Distributed Network Name (`DNN`) listener paired with `MultiSubnetFailover=True` on all client connection strings.
- **B:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Configure a Windows Server Failover Cluster (`WSFC`) with an Azure Cloud Witness and a Distributed Network Name (`DNN`) listener paired with `MultiSubnetFailover=True` on all client connection strings.
- **C:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: Configure a Windows Server Failover Cluster (`WSFC`) with an Azure Cloud Witness and a Distributed Network Name (`DNN`) listener paired with `MultiSubnetFailover=True` on all client connection strings.
- **D:** Correct. Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). In this scenario: Configure a Windows Server Failover Cluster (`WSFC`) with an Azure Cloud Witness and a Distributed Network Name (`DNN`) listener paired with `MultiSubnetFailover=True` on all client connection strings.

### Question 98 — D

Answer: Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions. Ordered Clustered Columnstore Indexes store min/max `ReadingUTC` metadata per 1M-row compressed rowgroup, allowing **rowgroup (segment) elimination** to skip all 2+ years of older rowgroups without reading them from storage. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. Local study-map skill 3.8 (Design Covering/Filtered/Columnstore Indexes and Rewrite Non-SARGable or Implicit-Conversion T-SQL Constructs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server and Azure SQL index design guide and SARGable T-SQL tuning (https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide).

- **A:** Incorrect for this requirement. Row-by-row cursors and multi-statement TVFs under legacy compatibility levels execute thousands of iterative context switches and 1-row cardinality guesses. Why the keyed choice wins: Ordered Clustered Columnstore Indexes store min/max `ReadingUTC` metadata per 1M-row compressed rowgroup, allowing **rowgroup (segment) elimination** to skip all 2+ years of older rowgroups without reading them from storage.
- **B:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Ordered Clustered Columnstore Indexes store min/max `ReadingUTC` metadata per 1M-row compressed rowgroup, allowing **rowgroup (segment) elimination** to skip all 2+ years of older rowgroups without reading them from storage.
- **C:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Ordered Clustered Columnstore Indexes store min/max `ReadingUTC` metadata per 1M-row compressed rowgroup, allowing **rowgroup (segment) elimination** to skip all 2+ years of older rowgroups without reading them from storage.
- **D:** Correct. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. In this scenario: Ordered Clustered Columnstore Indexes store min/max `ReadingUTC` metadata per 1M-row compressed rowgroup, allowing **rowgroup (segment) elimination** to skip all 2+ years of older rowgroups without reading them from storage.

### Question 99 — D

Answer: Yes — the proposed configuration satisfies every stated technical, security, and availability requirement. Yes — `RESUMABLE = ON` with `MAX_DURATION = 90 MINUTES` commits incremental progress without holding long transaction logs and pauses cleanly so `ALTER INDEX ... RESUME` continues where it stopped. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. Local study-map skill 3.10 (Implement Fragmentation-Aware Index Rebuilds (`ONLINE`, `RESUMABLE`), Async Statistics, and `DBCC CHECKDB`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Optimize index maintenance, statistics updates, and DBCC CHECKDB integrity checks (https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes).

- **A:** Incorrect for this requirement. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Why the keyed choice wins: Yes — `RESUMABLE = ON` with `MAX_DURATION = 90 MINUTES` commits incremental progress without holding long transaction logs and pauses cleanly so `ALTER INDEX ... RESUME` continues where it stopped.
- **B:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: Yes — `RESUMABLE = ON` with `MAX_DURATION = 90 MINUTES` commits incremental progress without holding long transaction logs and pauses cleanly so `ALTER INDEX ... RESUME` continues where it stopped.
- **C:** Incorrect for this requirement. SQL Server write-ahead logging performs sequential unbuffered writes; enabling `ReadOnly` or `ReadWrite` host caching on `.ldf` disks degrades throughput or risks corruption. Why the keyed choice wins: Yes — `RESUMABLE = ON` with `MAX_DURATION = 90 MINUTES` commits incremental progress without holding long transaction logs and pauses cleanly so `ALTER INDEX ... RESUME` continues where it stopped.
- **D:** Correct. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. In this scenario: Yes — `RESUMABLE = ON` with `MAX_DURATION = 90 MINUTES` commits incremental progress without holding long transaction logs and pauses cleanly so `ALTER INDEX ... RESUME` continues where it stopped.

### Question 100 — A, B, E

Answers: Leverage Parameter Sensitive Plan (`PSP`) optimization under compatibility level `160` to cache separate plans for skewed parameter sizes; Leverage Percentile and Persistence Memory Grant Feedback (`compat 160`) to eliminate recurring `tempdb` sort/hash spills and wasted RAM; Leverage Scalar UDF Inlining (`compat 150+`) so eligible T-SQL scalar functions fold into relational subqueries enabling parallel plans. Scalar UDF Inlining transforms eligible scalar T-SQL functions into relational subqueries allowing parallel plans, alongside Parameter Sensitive Plan (`PSP`) optimization and Memory Grant Feedback. Local study-map skill 3.14 (Identify Use Cases for Intelligent Query Processing (`PSP` Optimization, Memory Grant Feedback, Scalar UDF Inlining)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Intelligent Query Processing (IQP) features in SQL databases (https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing).

- **A:** Correct. Memory Grant Feedback adjusts overestimated or underestimated query memory grants across executions and persists learned grants in Query Store. In this scenario: Scalar UDF Inlining transforms eligible scalar T-SQL functions into relational subqueries allowing parallel plans, alongside Parameter Sensitive Plan (`PSP`) optimization and Memory Grant Feedback.
- **B:** Correct. Scalar UDF Inlining transforms row-by-row T-SQL scalar function invocations into set-based relational operators that no longer block parallelism. In this scenario: Scalar UDF Inlining transforms eligible scalar T-SQL functions into relational subqueries allowing parallel plans, alongside Parameter Sensitive Plan (`PSP`) optimization and Memory Grant Feedback.
- **C:** Incorrect for this requirement. Row-by-row cursors and multi-statement TVFs under legacy compatibility levels execute thousands of iterative context switches and 1-row cardinality guesses. Why the keyed choice wins: Scalar UDF Inlining transforms eligible scalar T-SQL functions into relational subqueries allowing parallel plans, alongside Parameter Sensitive Plan (`PSP`) optimization and Memory Grant Feedback.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Scalar UDF Inlining transforms eligible scalar T-SQL functions into relational subqueries allowing parallel plans, alongside Parameter Sensitive Plan (`PSP`) optimization and Memory Grant Feedback.
- **E:** Correct. PSP optimization generates up to three active dispatcher query variants so small lookups use Index Seeks while massive skews use Parallel Scans. In this scenario: Scalar UDF Inlining transforms eligible scalar T-SQL functions into relational subqueries allowing parallel plans, alongside Parameter Sensitive Plan (`PSP`) optimization and Memory Grant Feedback.
- **F:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Scalar UDF Inlining transforms eligible scalar T-SQL functions into relational subqueries allowing parallel plans, alongside Parameter Sensitive Plan (`PSP`) optimization and Memory Grant Feedback.
