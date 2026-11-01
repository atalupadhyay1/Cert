# Microsoft Exam DP-300: Administering Microsoft Azure SQL Solutions — Full-Length Mock Exam 2

Exam DP-300 (Healthcare EHR Systems, HIPAA SQL Ledger Compliance, and SQL Managed Instance) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint & Credential Notice:** Aligned to the official **October 27, 2026** DP-300 study guide (`Microsoft Certified: Azure Database Administrator Associate`). Associate-level certification with **no prerequisite exam required**, free online annual renewal on Microsoft Learn, split-screen `learn.microsoft.com` access during non-lab exam sections, and hands-on coverage across **T-SQL**, **Azure PowerShell**, **Azure CLI**, **Bicep**, and **KQL**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` T-SQL/PowerShell/CLI/Bicep/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Azure SQL case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area T-SQL/CLI dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn Azure SQL and SQL Server documentation — never recalled live items or copied Microsoft sample case studies.

## Questions

### 1. A regional clinic network runs 95 small outpatient scheduling databases whose busy hours stagger across US time zones, and wants shared compute billing with per-clinic max vCore ceilings. Which Azure SQL Database model fits best?

Domain: Plan and implement data platform resources

- A. SQL Server on Azure Virtual Machines (`Ebdsv5` series) with full OS and engine version control
- B. Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica
- C. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- D. Azure SQL Database vCore Elastic Pool with per-database min and max vCore limits

### 2. Your hospital network team prepares `snet-ehr-sqlmi` inside `vnet-clinical-prod` to host `SaffronChart`'s SQL Managed Instance. Which two subnet configurations are required before deployment? Select two.

Domain: Plan and implement data platform resources

- A. Associate a User-Defined Route (`UDR`) table (`0.0.0.0/0` -> `Internet` for management plane) and required NSG rules with the SQL MI subnet
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Create a dedicated VNet subnet (`/28` or larger) with no other cloud resources and delegate it to `Microsoft.Sql/managedInstances`
- D. Switch eligible hybrid SQL Server instances to hourly Azure Arc pay-as-you-go billing instead of upfront core licenses
- E. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching

### 3. A healthcare DevOps engineer wants declarative infrastructure-as-code files with concise domain-specific syntax (`resource sqlmi 'Microsoft.Sql/managedInstances@...'`) that transpile directly into ARM JSON without managing external state files. Which deployment method should they choose?

Domain: Plan and implement data platform resources

- A. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`
- D. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 4. A population-health team creates a `SQL database` item in Microsoft Fabric for clinical trial intake so biostatisticians can run Spark notebooks over live intake tables without building ADF Copy pipelines. Which two native behaviors apply? Select two.

Domain: Plan and implement data platform resources

- A. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- B. Configure SQL Server password logins (`CREATE LOGIN ... WITH PASSWORD`) and T-SQL `BACKUP DATABASE ... TO DISK` inside SQL database in Microsoft Fabric
- C. Authenticate applications and users exclusively with Microsoft Entra ID identities, service principals, or workspace roles
- D. Query automatically replicated OneLake Delta Parquet tables and the read-only SQL analytics endpoint from Spark and Direct Lake
- E. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 5. Twelve hospital pathology lab SQL Server 2022 servers must stay inside sterile on-premises lab rooms next to blood analyzers, yet CISO leadership wants Microsoft Defender for SQL vulnerability assessments and Purview governance from Azure. What should you deploy?

Domain: Plan and implement data platform resources

- A. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- B. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- C. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- D. SQL Server enabled by Azure Arc (`Microsoft.AzureArcData/sqlServerInstances`)

### 6. A clinical HL7 `VitalSigns` table partitions 36 months of telemetry by `RecordedUTC`. Every month-end you must add next month's partition and move the 37th-month partition into `VitalSigns_ColdStaging` instantaneously without blocking ICU writes. Which sequence should you run?

Domain: Plan and implement data platform resources

- A. ALTER TABLE ... SWITCH oldest partition directly to Azure Blob Storage → SPLIT partition function → Rebuild entire table offline → MERGE all boundaries
- B. SPLIT partition function for incoming future boundary → Create empty staging table on same filegroup with matching schema/indexes → ALTER TABLE ... SWITCH oldest partition to staging → Archive staging data & MERGE retired boundary
- C. MERGE oldest partition boundary first → Run row-by-row DELETE on 80M rows → Create unindexed staging table on a different filegroup → SPLIT partition function
- D. Create staging table without matching CHECK constraints → SWITCH partition across two separate Azure SQL Databases → MERGE future boundary → Truncate production table

### 7. A telemedicine platform shards 200 million patient portal records by numeric `PatientId` intervals (`1–10000000`, `10000001–20000000`) across 20 Azure SQL Databases using `ShardMapManager`. Which shard map type models contiguous numeric spans: `Create____ShardMap`?

Domain: Plan and implement data platform resources

- A. Horizontal sharding using the Elastic Database Client Library (`ShardMapManager` with `ListShardMap` or `RangeShardMap`)
- B. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- C. Table partitioning using `CREATE PARTITION FUNCTION ... AS RANGE RIGHT` with aligned indexes and `ALTER TABLE ... SWITCH`
- D. Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica

### 8. An imaging PACS vendor runs SQL Server 2022 on Windows Server Azure VMs and requires automated cumulative update installation restricted strictly to Tuesdays 01:00–03:00 local hospital time plus portal AHB license tracking. What should you configure?

Domain: Plan and implement data platform resources

- A. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- B. SQL IaaS Agent Extension in Full management mode paired with Azure Update Manager / Automated Patching
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled

### 9. On an Ubuntu 22.04 VM running SQL Server 2022 for a radiology queue, you enable the SQL Server Agent service from bash via `sudo /opt/mssql/bin/mssql-conf set ____.enabled true` followed by restarting `mssql-server`. Which setting namespace enables Agent on Linux?

Domain: Plan and implement data platform resources

- A. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- B. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas
- C. SQL Server on Linux configured via `mssql-conf` or Linux container images for consistent CI/CD dev-test parity
- D. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 10. A genomic sequencing Azure SQL Database has grown to 28 TB, and restoring a test environment from standard storage takes hours. Which Azure SQL Database tier uses page servers and Blob snapshots to perform near-instantaneous database restores regardless of multi-TB size?

Domain: Plan and implement data platform resources

- A. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- B. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled

### 11. An emergency-department medication order instance on Azure SQL Managed Instance demands sub-millisecond local NVMe SSD transaction log commits, in-memory OLTP (`MEMORY_OPTIMIZED_DATA`), and a free built-in readable secondary replica. Which tier is required?

Domain: Plan and implement data platform resources

- A. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. Azure SQL Managed Instance (Next-gen General Purpose) with decoupled IOPS and storage sliders
- D. Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica

### 12. You are architecting disk layout on an `E64bds_v5` Azure VM for a high-throughput hospital billing SQL Server 2022 instance. Which three storage configurations follow Microsoft performance guidelines? Select three.

Domain: Plan and implement data platform resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- C. Configure `None` Azure host caching on dedicated managed disks hosting `.ldf` SQL Server transaction log files
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- E. Configure `ReadOnly` Azure host caching on Premium SSD data disks hosting `.mdf` and `.ndf` database files
- F. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script

### 13. During an autogrowth event of a 64 GB `.ndf` clinical image datafile on a SQL Server Windows VM, sessions stall for 90 seconds while Windows zeroes new disk blocks. Proposed solution: Grant `Perform volume maintenance tasks` (`____`) and `Lock pages in memory` to the SQL Server service account and restart SQL Server. Does the solution meet the goal?

Domain: Plan and implement data platform resources

- A. No — transaction log managed disks on SQL Server Azure VMs must use host caching `None`, never `ReadOnly` or `ReadWrite`
- B. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- C. No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases
- D. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement

### 14. Before applying `PAGE` compression to a 1.6 TB `LabObservations` table, you want to preview projected size reductions without locking or modifying the table via `EXEC sys.____ 'Clinical', 'LabObservations', NULL, NULL, 'PAGE';`. Which system procedure do you run?

Domain: Plan and implement data platform resources

- A. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- B. Grant `Perform volume maintenance tasks` (Instant File Initialization) and `Lock pages in memory` to the SQL Server service account
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Evaluate `sp_estimate_data_compression_savings` and apply `ROW`, `PAGE`, or `COLUMNSTORE_ARCHIVE` compression per partition

### 15. A hospital DBA needs a schema-and-data archive of an active 24x7 intake Azure SQL Database processing 800 writes/sec. Proposed solution: Run `SqlPackage /Action:Export /TargetFile:Intake.bacpac` directly against the live read-write primary database without creating a copy. Does the solution meet the goal?

Domain: Plan and implement data platform resources

- A. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- B. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- C. No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases
- D. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement

### 16. You must relocate `RadiologyIndexDB` online from an overloaded Azure SQL Managed Instance in `vnet-east-a` to a larger SQL Managed Instance in `vnet-east-b` with zero data loss, removing the source copy once finished. Which four-step workflow applies?

Domain: Plan and implement data platform resources

- A. Verify VNet peering & TCP 5022 + 11000-11999 rules → Start online Database Move from source to target SQL MI → Wait for seeding to reach Ready for completion → Complete move within 24 hours so target comes online
- B. Start online Database Move → Wait 72 hours in Ready for completion state → Open TCP 5022 + 11000-11999 rules → Expect PITR backups from source MI to transfer automatically
- C. Stop source SQL Managed Instance compute → Detach user database via sp_detach_db → Copy files over port 1433 → Reattach database on target SQL MI
- D. Export `.bacpac` to Azure Table storage → Import `.bacpac` onto target SQL MI → Complete move after 48 hours → Retain source database online automatically

### 17. HIPAA auditors cite lingering SQL password accounts on `sqlmi-saffron-prod`. Which setting blocks all SQL logins and enforces centralized MFA and Conditional Access tokens across the entire SQL Managed Instance?

Domain: Implement a secure environment

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Enable Microsoft Entra-only authentication (`azuread_authentication_only`) on the logical SQL server or SQL Managed Instance
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database

### 18. An HL7 ingestion Azure Function `fn-hl7-ingest` uses a User-Assigned Managed Identity `id-hl7-ingest` and needs `db_datawriter` inside `ClinicalDB`. After `CREATE USER [id-hl7-ingest] FROM EXTERNAL PROVIDER`, which T-SQL statement grants write access: `ALTER ROLE ____ ADD MEMBER [id-hl7-ingest];`?

Domain: Implement a secure environment

- A. Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`)
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- D. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database

### 19. Clinician workstations joined to hybrid Microsoft Entra ID open a legacy Win32 cardiology viewer that uses `Integrated Security=SSPI` Kerberos tickets against Azure SQL Managed Instance. How do you enable Windows Authentication without deploying AD DS VMs?

Domain: Implement a secure environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or `Entra Kerberos`)
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 20. Why are contained Microsoft Entra database users (`FROM EXTERNAL PROVIDER`) preferred over traditional server-level SQL logins mapped to database users in Geo-Replicated Azure SQL Databases?

Domain: Implement a secure environment

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- C. Remap orphaned database users (`ALTER USER [u] WITH LOGIN = [u]`) and inspect explicit `DENY` permissions via `sys.database_permissions`
- D. Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`)

### 21. A compliance schema scanner needs to inspect table, view, and stored procedure definitions across all databases on an Azure SQL logical server without viewing any patient data rows. Which built-in server-level role fits best?

Domain: Implement a secure environment

- A. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Built-in granular server-level roles (`##MS_ServerStateReader##`, `##MS_DefinitionReader##`) or `GRANT VIEW DATABASE PERFORMANCE STATE`

### 22. Pharmacists call `Rx.usp_ApproveControlledOrder`, which writes an audit entry and updates `Rx.Orders`. You need the procedure to verify temporal stock tables under a dedicated low-privilege execution context via `CREATE PROCEDURE Rx.usp_ApproveControlledOrder WITH ____ AS 'rx_verifier'`. Which clause sets execution context?

Domain: Implement a secure environment

- A. Stored procedure encapsulation using schema ownership chaining, `EXECUTE AS OWNER`, or certificate module signing
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- D. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`

### 23. A clinical triage screen must filter `WHERE PatientSSN LIKE '%6109'` while keeping column keys out of DBA reach. Proposed solution: Grant `SELECT` to the app role and encrypt `PatientSSN` with standard Deterministic Always Encrypted without any secure enclave. Does the solution meet the goal?

Domain: Implement a secure environment

- A. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server
- B. No — standard Deterministic Always Encrypted supports equality (`=`) joins/filters only, never `LIKE` or range predicates
- C. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- D. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference

### 24. A nurse practitioner belongs to Entra group `SG-Clinicians` (`GRANT SELECT ON SCHEMA::Chart`) and `SG-Contractors` (`DENY SELECT ON OBJECT::Chart.PsychNotes`). When she queries `Chart.PsychNotes`, access is denied, and she runs `SELECT * FROM ____('Chart.PsychNotes', 'OBJECT')` to verify effective rights. Which built-in function returns her effective permissions?

Domain: Implement a secure environment

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- C. Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history
- D. Remap orphaned database users (`ALTER USER [u] WITH LOGIN = [u]`) and inspect explicit `DENY` permissions via `sys.database_permissions`

### 25. You rotate `VerityMed`'s TDE protector key to a new Azure Key Vault in a separate security subscription. Which two prerequisites must be in place on that Key Vault before rotation succeeds? Select two.

Domain: Implement a secure environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Grant the SQL server Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) on the Key Vault
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Enable both `Soft Delete` and `Purge Protection` on the Azure Key Vault or Managed HSM storing the TDE protector key
- E. Configure `None` Azure host caching on dedicated managed disks hosting `.ldf` SQL Server transaction log files

### 26. To disallow legacy TLS 1.0 and TLS 1.1 connections from older lab middleware against `sql-veritymed` via Azure CLI, you run `az sql server update -g rg-hipaa -n sql-veritymed --minimal-tls-version ____`. Which value enforces modern transport security?

Domain: Implement a secure environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- C. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database
- D. Column-level encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey`) plus `Minimal TLS version = 1.2`

### 27. An external toxicology lab connects from fixed NAT IP `203.0.113.77` exclusively to `ToxicologyDB`, and the firewall rule must travel automatically with `ToxicologyDB` during geo-failover. Proposed solution: Execute `EXEC sys.sp_set_database_firewall_rule` inside `ToxicologyDB`. Does the solution meet the goal?

Domain: Implement a secure environment

- A. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server
- B. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- C. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- D. No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases

### 28. You need to encrypt an existing 80-million-row `Patients.NationalId` column in-place on Azure SQL Database so clinicians can run `LIKE` and range queries without downloading data out of the database. Which four-step sequence applies?

Domain: Implement a secure environment

- A. Disable TLS on client connection string → Set `Column Encryption Setting=Disabled` → Create Deterministic CEK without CMK → Run `LIKE` wildcard queries
- B. Grant Azure SQL DBA `unwrapKey` on CMK inside T-SQL → Decrypt column via server stored procedure → Apply Dynamic Data Masking → Enable VBS enclave
- C. Run in-place column encryption first → Create non-enclave CEK without ENCLAVE_COMPUTATIONS → Store plaintext CMK inside sys.configurations → Enable VBS enclave last
- D. Enable VBS enclave on Azure SQL Database → Provision Key Vault CMK & enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`) → Grant client Key Vault key permissions & attestation → Run in-place `ALTER TABLE` encryption

### 29. Clinicians must run `BETWEEN` date-of-birth range filters and `LIKE` name searches on encrypted PHI columns in Azure SQL Database using VBS secure enclaves. Which two configurations are mandatory? Select two.

Domain: Implement a secure environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Provision a Column Master Key in Key Vault and create a Column Encryption Key with `ENCLAVE_COMPUTATIONS` enabled
- C. Enable `Column Encryption Setting=Enabled` and pass the `Enclave Attestation Url` (or VBS zero-attestation setting) in client drivers
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- E. Configure `ReadOnly` Azure host caching on Premium SSD data disks hosting `.mdf` and `.ndf` database files

### 30. Hospital security mandates that `VerityMed`'s Azure SQL Database accept connections exclusively over Azure Private Link from `vnet-hipaa-core`. Which two configurations complete Private Link lockdown? Select two.

Domain: Implement a secure environment

- A. Link Private DNS Zone `privatelink.database.windows.net` (or forward on-premises DNS) to resolve `<server>.database.windows.net` to the private IP
- B. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- C. Switch eligible hybrid SQL Server instances to hourly Azure Arc pay-as-you-go billing instead of upfront core licenses
- D. Set `Public network access = Disabled` (`publicNetworkAccess: Disabled`) on the logical SQL server so internet connections are rejected
- E. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 31. How does a Virtual Network Service Endpoint (`Microsoft.Sql`) differ from an Azure Private Endpoint when securing traffic from an Azure Kubernetes Service subnet to Azure SQL Database?

Domain: Implement a secure environment

- A. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- B. Virtual Network Service Endpoints (`Microsoft.Sql`) with outbound storage firewall rules, or dedicated `/28+` delegated subnet for SQL MI
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database

### 32. Which system catalog view lets a HIPAA compliance script inventory every column currently tagged with sensitivity labels and information types inside a database: `SELECT schema_name(o.schema_id), o.name, c.name, s.label FROM sys.____ s ...`?

Domain: Implement a secure environment

- A. SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 33. An adverse-drug-event analytics lakehouse must capture **every intermediate before-and-after column value** whenever a dosage row in `Rx.Dosages` is updated three times between 15-minute ETL runs (`EXEC sys.sp_cdc_enable_table ...`). Which feature is required?

Domain: Implement a secure environment

- A. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- B. Enable Change Data Capture (`CDC`) on DTU `Basic`/`S0–S2` databases or expect Change Tracking (`CT`) to retain every intermediate `UPDATE` value
- C. Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history
- D. Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database

### 34. Billing clerks querying `Patients.NationalHealthNo` (`'NHS-449182-77'`) must see `'NHS-XXXXXX-77'` (`first 4` chars exposed, `XXXXXX` mask, `last 3` chars exposed) via `ADD MASKED WITH (FUNCTION = '____(4, "XXXXXX", 3)')`. Which masking function applies?

Domain: Implement a secure environment

- A. Row-Level Security (`CREATE SECURITY POLICY`) binding a `SCHEMABINDING` inline TVF as both `FILTER PREDICATE` and `BLOCK PREDICATE`
- B. Transparent Data Encryption (TDE) with a Customer-Managed Key (`CMK`) in Azure Key Vault (`Soft Delete` + `Purge Protection`)
- C. Always Encrypted (`Randomized` for maximum security with zero equality leakage; `Deterministic` only when `=` joins or `GROUP BY` are required)
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 35. A multi-hospital behavioral health database isolates rows by `HospitalFacilityId` for shared API connections. Which three Row-Level Security elements prevent clinics from either reading or writing another hospital's patient notes? Select three.

Domain: Implement a secure environment

- A. Truncate or `DELETE` historical rows from an append-only Ledger table (`LEDGER = ON (APPEND_ONLY = ON)`) to purge audit history in place
- B. Add `AFTER INSERT` and `AFTER UPDATE` / `BEFORE UPDATE` `BLOCK PREDICATE` clauses in `CREATE SECURITY POLICY` (`STATE = ON`)
- C. Add a `FILTER PREDICATE` in `CREATE SECURITY POLICY` to hide non-matching rows silently from `SELECT`, `UPDATE`, and `DELETE`
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- E. Create an inline table-valued function `WITH SCHEMABINDING` evaluating `SESSION_CONTEXT()` or `DATABASE_PRINCIPAL_ID()`
- F. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 36. After migrating `SaffronChart` onto Azure SQL Managed Instance, which catalog view provides 15-second historical snapshots of instance CPU, storage space, and I/O counts over the past 14 days: `SELECT * FROM sys.____ ORDER BY start_time DESC`?

Domain: Monitor, configure, and optimize database resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Azure Monitor metrics paired with `sys.dm_db_resource_stats` (single DB) or `sys.server_resource_stats` (SQL MI) for 15-second CPU, data I/O, log write, and memory baselines

### 37. During morning nurse shift handoff, transaction commits slow down and `WRITELOG` jumps to #1 in `sys.dm_os_wait_stats` while CPU sits at 18%. What bottleneck causes high `WRITELOG` wait times?

Domain: Monitor, configure, and optimize database resources

- A. Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- D. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas

### 38. You configure Azure Monitor Diagnostic Settings across 40 clinical Azure SQL Databases so deadlocks, query runtime stats, and wait statistics flow into a central Log Analytics workspace without polling each database via T-SQL. Which log categories should you stream?

Domain: Monitor, configure, and optimize database resources

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- C. Azure Monitor Diagnostic Settings streaming `SQLInsights`, `QueryStoreRuntimeStatistics`, `Errors`, and `Blocks` to a Log Analytics workspace (`KQL`)
- D. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server

### 39. You are deploying `database watcher` into `PulseCrest`'s subscription backed by a Microsoft Fabric Eventhouse KQL database. Which four-step provisioning sequence should you execute?

Domain: Monitor, configure, and optimize database resources

- A. Start database watcher before selecting data store or SQL targets → Grant `sysadmin` via blank-password `sa` login → Store time-series telemetry in Azure Queue Storage → Enable SQL Profiler trace
- B. Provision Azure Data Explorer or Fabric Eventhouse store → Create database watcher with Managed Identity → Add SQL targets & grant `VIEW SERVER PERFORMANCE STATE` + ingest roles → Start watcher & open portal dashboards
- C. Create database watcher targeting Azure Cosmos DB for Gremlin → Store metrics in Azure Table storage → Authenticate via anonymous public SAS → Query dashboards via Gremlin
- D. Install third-party kernel drivers inside Azure SQL Database PaaS OS → Configure SMB share on domain controller → Export `.trc` files via `sp_trace_create` → Query via MDX

### 40. Why should production DBAs prefer Extended Events writing to `event_file` over `ring_buffer` when diagnosing intermittent overnight timeouts on Azure SQL Database?

Domain: Monitor, configure, and optimize database resources

- A. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- B. Extended Events (`CREATE EVENT SESSION ... ON DATABASE` in SQL DB or `ON SERVER` in SQL MI/VMs) writing to an `event_file` target in Azure Blob Storage
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 41. An upgraded EHR vendor assembly emits an inefficient parameterized T-SQL query whose source code is locked inside a compiled DLL. Which two Query Store procedures let you fix its plan shape or attach hints immediately? Select two.

Domain: Monitor, configure, and optimize database resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Execute `sys.sp_query_store_set_hints @query_id, N'OPTION (RECOMPILE)'` (or `MAXDOP` / memory grant hints) without redeploying code
- D. Execute `sys.sp_query_store_force_plan @query_id, @plan_id` to pin the historical low-latency execution plan immediately
- E. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 42. Following weekend statistics skew on `LabResults`, query `query_id = 418` regresses from an Index Seek (`plan_id = 12`) to a Parallel Table Scan (`plan_id = 79`). Which four-step Query Store procedure restores performance safely?

Domain: Monitor, configure, and optimize database resources

- A. Restart SQL Server production instance during peak traffic → Rebuild every index with `ONLINE = OFF` → Enable `AUTO_CLOSE = ON` → Check Query Store
- B. Confirm Query Store is `READ_WRITE` with wait capture → Compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`) → Force prior plan via `sp_query_store_force_plan` → Monitor `force_failure_count` & latency
- C. Set Query Store `OPERATION_MODE = READ_ONLY` → Modify `sys.query_store_plan` system catalog via `UPDATE` → Run `DBCC FREEPROCCACHE` every minute → Disable statistics
- D. Run `ALTER DATABASE ... SET QUERY_STORE CLEAR ALL` first → Inspect Regressed Queries history → Force new regressed plan ID → Set `OPERATION_MODE = OFF`

### 43. Physician chart reads (`SELECT`) stall behind pharmacy dispense `UPDATE` transactions, yet clinical safety strictly prohibits dirty reads (`NOLOCK`). You run `ALTER DATABASE ClinicalDB SET ____ = ON;` to eliminate reader-writer blocking safely. Which setting completes this statement?

Domain: Monitor, configure, and optimize database resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Read Committed Snapshot Isolation (`READ_COMMITTED_SNAPSHOT = ON`) combined with Optimized Locking (`TID` locking + Lock After Qualification `LAQ`)
- D. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 44. On Azure SQL Managed Instance, where do you retrieve the historical XML deadlock graphs captured automatically by the engine's built-in health session without starting SQL Profiler?

Domain: Monitor, configure, and optimize database resources

- A. Capture `xml_deadlock_report` via Extended Events or `sys.event_log`, align table modification order across transactions, and add covering indexes
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 45. Before starting `database watcher` collection on `PulseCrest`'s three SQL Managed Instances into Azure Data Explorer, security asks for the exact least-privilege permissions required on both ends. Which two grants are required? Select two.

Domain: Monitor, configure, and optimize database resources

- A. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- B. Grant the database watcher Managed Identity `VIEW SERVER PERFORMANCE STATE` (or `VIEW DATABASE PERFORMANCE STATE`) on SQL targets
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Grant the database watcher Managed Identity database `Admin` / ingest permissions on the Azure Data Explorer or Fabric Eventhouse store
- E. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 46. Which DMV query ranks the highest cumulative CPU-consuming T-SQL statements currently cached in an Azure SQL Database: `SELECT TOP 10 total_worker_time / execution_count AS AvgCpuUs FROM sys.____ ORDER BY total_worker_time DESC`?

Domain: Monitor, configure, and optimize database resources

- A. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- B. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- C. Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 47. A clinical analytics table `EncounterFacts` stores 800 million historical rows queried via `SUM()`, `AVG()`, and `GROUP BY DiagnosisCode` across wide date ranges while rarely updating individual rows. Which index architecture provides up to 10x compression and batch-mode scan speed?

Domain: Monitor, configure, and optimize database resources

- A. Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- D. Replace set-based `JOIN` queries with nested `FAST_FORWARD` T-SQL cursors calling multi-statement table-valued functions per row under compat `100`

### 48. In an execution plan for `WHERE NationalId = @id`, you see a `CONVERT_IMPLICIT(NVARCHAR(20), [NationalId], 0)` warning and an `Index Scan` instead of an `Index Seek` because `@id` was passed as Unicode `NVARCHAR` against a `VARCHAR(20)` column. Why did SQL scan the entire index?

Domain: Monitor, configure, and optimize database resources

- A. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`)

### 49. You inspect `sys.query_store_plan` and notice `is_forced_plan = 1` alongside `last_force_failure_reason_desc = 'NO_PLAN'` after an engineer renamed nonclustered index `IX_Claims_Payer`. Why did plan forcing fail without failing the query itself?

Domain: Monitor, configure, and optimize database resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Query Store (`OPERATION_MODE = READ_WRITE`, `QUERY_CAPTURE_MODE = AUTO`) using `sp_query_store_force_plan` and `sp_query_store_set_hints`
- D. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7

### 50. Your nightly index script inspects `avg_fragmentation_in_percent` from `sys.dm_db_index_physical_stats`. According to standard Microsoft thresholds, how should indexes with `18%` fragmentation versus `42%` fragmentation (>1,000 pages) be maintained?

Domain: Monitor, configure, and optimize database resources

- A. Fragmentation-aware index maintenance (`REORGANIZE` 5–30%, `REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` >30%), `UPDATE STATISTICS`, and `DBCC CHECKDB WITH PHYSICAL_ONLY`
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon

### 51. Running full `DBCC CHECKDB` every night on a 6 TB SQL Server 2022 EHR VM spikes CPU and buffer-pool churn for four hours. Which two strategies verify physical corruption safely with minimal production OLTP impact?

Domain: Monitor, configure, and optimize database resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Fragmentation-aware index maintenance (`REORGANIZE` 5–30%, `REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` >30%), `UPDATE STATISTICS`, and `DBCC CHECKDB WITH PHYSICAL_ONLY`
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 52. You enable `ALTER DATABASE PharmacyDB SET AUTOMATIC_TUNING (FORCE_LAST_GOOD_PLAN = ON);`. Under what condition does Azure SQL Database automatically unforce an auto-forced plan?

Domain: Monitor, configure, and optimize database resources

- A. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`)

### 53. After upgrading `ClinicalArchiveDB` from compatibility level `110` to `160`, two legacy vendor queries regress due to the new Cardinality Estimator while 500 other queries speed up. Which T-SQL statement reverts only that database's CE model while keeping `compat 160` IQP features: `ALTER DATABASE SCOPED CONFIGURATION SET ____ = ON;`?

Domain: Monitor, configure, and optimize database resources

- A. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Use `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`, `OPTIMIZED_PLAN_FORCING`) per database

### 54. You upgrade `SaffronChart`'s EHR database on SQL Managed Instance to compatibility level `160`. Which three Intelligent Query Processing (`IQP`) improvements become active automatically without rewriting T-SQL? Select three.

Domain: Monitor, configure, and optimize database resources

- A. Leverage Scalar UDF Inlining (`compat 150+`) so eligible T-SQL scalar functions fold into relational subqueries enabling parallel plans
- B. Leverage Parameter Sensitive Plan (`PSP`) optimization under compatibility level `160` to cache separate plans for skewed parameter sizes
- C. Leverage Percentile and Persistence Memory Grant Feedback (`compat 160`) to eliminate recurring `tempdb` sort/hash spills and wasted RAM
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- E. Replace set-based `JOIN` queries with nested `FAST_FORWARD` T-SQL cursors calling multi-statement table-valued functions per row under compat `100`
- F. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking

### 55. On `SaffronChart`'s SQL Managed Instance, you schedule a weekly T-SQL statistics job followed by a child cleanup step that should execute **only** if Step 1 fails. Which SQL Server Agent job step flow property configures this behavior?

Domain: Configure and manage automation of tasks

- A. SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 56. A hospital DBA wants SQL Server Agent on an Azure VM to trigger an automated log-backup job immediately whenever the `ClinicalDB` transaction log exceeds 80% full. Which SQL Server Agent alert type detects performance counter thresholds?

Domain: Configure and manage automation of tasks

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- C. SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 57. You are standardizing SQL Server Agent security and fatal-error alerting across eight clinical SQL Server 2022 Azure VMs. Which two configurations enforce least privilege and immediate hardware/corruption paging? Select two.

Domain: Configure and manage automation of tasks

- A. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- B. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- C. Configure Database Mail, define an Agent Operator, and create SQL Server Agent Alerts for Severity `19–25` and Errors `823`, `824`, and `825`
- D. Create a Windows/SQL Credential and map it to a SQL Server Agent Subsystem Proxy (`CmdExec` / `PowerShell`) instead of granting `sysadmin`
- E. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server

### 58. A non-`sysadmin` job owner updates a SQL Server Agent PowerShell step on a SQL Server VM, and the job immediately fails with `The step failed because the proxy account does not have permissions`. Where do you grant the job owner access to use that proxy?

Domain: Configure and manage automation of tasks

- A. Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 59. A scheduled SQL Server Agent job on a SQL Server VM shows `Next Run = Not scheduled` even though its schedule is enabled and SQL Server Engine is online. Checking `sys.dm_server_services` reveals `SQL Server Agent (MSSQLSERVER)` status is `Stopped` with `Startup Type = Manual`. How do you prevent recurrence after OS patching reboots?

Domain: Configure and manage automation of tasks

- A. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- B. Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 60. Your hospital cloud platform team deploys HIPAA Azure SQL servers via Azure DevOps Bicep pipelines. Which two pipeline practices prevent secret leakage and catch unintended resource deletions before deployment? Select two.

Domain: Configure and manage automation of tasks

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Mark sensitive parameters with `@secure()` in Bicep and pass Key Vault secret references from the parameter file rather than cleartext values
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- E. Run `az deployment group what-if` (or `New-AzResourceGroupDeployment -WhatIf`) as a pull-request gate before applying template changes

### 61. What happens when you re-run an ARM or Bicep deployment in default `Incremental` mode (`--mode Incremental`) after adding one new firewall rule to an existing `Microsoft.Sql/servers` template?

Domain: Configure and manage automation of tasks

- A. Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`
- B. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 62. You automate provisioning of a Next-gen General Purpose SQL Managed Instance via Azure CLI: `az sql mi ____ -g rg-hipaa -n sqlmi-ehr --subnet /subscriptions/.../subnets/snet-mi --capacity 8 --storage 512`. Which CLI command creates the instance?

Domain: Configure and manage automation of tasks

- A. Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`)
- B. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7

### 63. You write a PowerShell script to trigger a planned zero-data-loss regional switch of a SQL Managed Instance Failover Group: `____ -ResourceGroupName "rg-dr" -Location "centralus" -FailoverGroupName "fog-curaspan"`. Which cmdlet executes the planned switch?

Domain: Configure and manage automation of tasks

- A. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- B. Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`)
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 64. A Bicep deployment of Azure SQL Managed Instance hangs and fails because a newly attached corporate firewall UDR forces `0.0.0.0/0` to a virtual appliance (`VirtualAppliance`) without exempting Azure SQL MI management service tags. How do you fix this?

Domain: Configure and manage automation of tasks

- A. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- B. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- C. Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 65. An automated Bicep deployment creating a Key Vault-protected Azure SQL Database fails with `InvalidKeyVaultKeyName` because the Bicep template deployed the SQL TDE protector **in parallel** before the Key Vault role assignment propagated. Which Bicep construct enforces sequential ordering?

Domain: Configure and manage automation of tasks

- A. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- B. Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules
- C. Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 66. You manage 65 clinic Azure SQL Databases across three logical SQL servers and need to run nightly T-SQL reference-code table syncs across all 65 databases without managing SQL credentials or VMs. Which native PaaS feature is purpose-built for this?

Domain: Configure and manage automation of tasks

- A. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo
- B. Azure SQL Database Elastic Job Agent (`jobs.sp_add_job`) authenticating to Target Groups across servers/pools via a User-Assigned Managed Identity (`UAMI`)
- C. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- D. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 67. You are deploying an Elastic Job Agent to run weekly `UPDATE STATISTICS` across 40 diagnostic Azure SQL Databases using passwordless authentication. Which four-step sequence configures the agent end to end?

Domain: Configure and manage automation of tasks

- A. Create S1+ Job Database & Elastic Job Agent with UAMI → Create contained UAMI user on target DBs with needed permissions → Define Target Group (`jobs.sp_add_target_group_member`) → Add T-SQL steps & schedule (`jobs.sp_add_job`)
- B. Create Elastic Job Agent on Basic tier DB → Run `jobs.sp_add_job` before creating Target Group → Authenticate across servers with Windows NTLM local accounts → Schedule via `msdb.dbo.sp_add_job`
- C. Enable SQL Server Agent inside single Azure SQL Database → Create linked servers to 480 tenant DBs → Loop synchronously inside a scalar UDF → Grant `CONTROL SERVER` to `guest`
- D. Provision Elastic Job Agent inside Azure Blob Storage → Store plaintext admin password in Git repo → Add Cosmos DB containers to Target Group → Trigger via `DBCC SHRINKDATABASE`

### 68. A hybrid hospital has eight on-premises SQL Server 2019 instances inside a private VLAN with no inbound internet ports, and wants Azure Automation PowerShell runbooks to trigger local maintenance scripts securely over outbound HTTPS `443`. Which component enables this?

Domain: Configure and manage automation of tasks

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`
- C. Azure Automation PowerShell / Python runbooks (or Azure Functions / Logic Apps) using a System-Assigned Managed Identity on a recurring schedule
- D. Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo

### 69. You author an Azure Function on a Timer trigger (`0 0 22 * * 1-5`) in C# or Python that pauses/scales dev-test SQL resources via Azure SDK without storing client secrets in `local.settings.json`. How should the Function authenticate to Azure Resource Manager?

Domain: Configure and manage automation of tasks

- A. Azure Automation PowerShell / Python runbooks (or Azure Functions / Logic Apps) using a System-Assigned Managed Identity on a recurring schedule
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 70. You want PagerDuty and SMS notifications within two minutes whenever CPU exceeds 90% for 10 minutes or deadlock count >= 1 on any production clinical Azure SQL Database. What should you configure in Azure Monitor?

Domain: Configure and manage automation of tasks

- A. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- B. Configure Azure Monitor Metric / Log Alert rules routed to Action Groups and query `jobs.job_executions` in the Elastic Job database to diagnose step failures
- C. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

### 71. A radiology metadata Azure SQL Database requires `99.995%` availability SLA against single-datacenter power/cooling failures inside East US 2 with zero data loss (`RPO = 0`). Proposed solution: Deploy Business Critical vCore tier with `Zone Redundant` enabled (`-ZoneRedundant`). Does the solution meet the goal?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- B. No — transaction log managed disks on SQL Server Azure VMs must use host caching `None`, never `ReadOnly` or `ReadWrite`
- C. No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent
- D. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement

### 72. A regional clinic still runs SQL Server **2019** on-premises and establishes a Managed Instance link to Azure SQL Managed Instance for DR. What critical failback limitation applies to SQL Server 2019 compared to SQL Server 2022?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Expect online bidirectional planned failback from Azure SQL Managed Instance directly back to on-premises SQL Server 2016 without downtime
- B. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- C. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- D. Hybrid DR using Managed Instance link with bidirectional online failover between SQL Server 2022 and Azure SQL Managed Instance

### 73. When deploying SQL Server 2022 Enterprise on Azure VMs inside a single region that lacks Availability Zones, which VM placement construct protects your 2-node Always On Availability Group against simultaneous host rack maintenance or single-PDU hardware faults?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`)
- C. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- D. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG

### 74. Before hospital accreditation, you must prove `CuraSpan`'s multi-database DR environment can fail over to Central US and back with zero data loss and zero application config edits. Which four-step drill sequence should you execute?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Export nightly `.bacpac` to local laptop → Delete production database to test restore → Manually edit 50 microservice connection strings → Re-enable TDE after 6 hours
- B. Execute unplanned `AllowDataLoss` forced failover during peak checkout → Create secondary logical SQL server afterward → Hardcode regional server names in app connection strings → Skip firewall rules on secondary
- C. Provision secondary SQL server with matching firewall/Private Link & Entra admin → Create Failover Group with coupled DBs → Point apps to `<fog>.database.windows.net` & `.secondary` → Run planned `Switch-AzSqlDatabaseFailoverGroup` drill
- D. Create Failover Group between two servers in the exact same datacenter rack → Add `tempdb` and `master` to Failover Group → Point OLTP writes to `.secondary.database.windows.net` → Disable Geo-Replication

### 75. During a non-disruptive read-only DR verification test, clinical reporting apps connect to `<fog>.secondary.database.windows.net` with `ApplicationIntent=ReadOnly`. What should your pre-drill checklist verify on the secondary region before testing?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- C. Non-disruptive DR readiness drill executing a planned zero-data-loss Failover Group switch (`Switch-AzSqlDatabaseFailoverGroup`), validating app listeners, and failing back
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 76. You move ` OncologyDB` online to a new Azure SQL Managed Instance via Database Move at 18:00 UTC, and at 19:00 UTC a physician asks to restore `OncologyDB` via PITR to 10:00 UTC earlier that morning. Proposed solution: Run PITR on the destination SQL Managed Instance targeting 10:00 UTC. Does the solution meet the goal?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Yes — the proposed configuration satisfies every stated technical, security, and availability requirement
- B. No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference
- C. No — moving a database across SQL Managed Instances starts a fresh backup chain and does not carry over prior PITR backups
- D. No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server

### 77. An administrator accidentally deletes Azure SQL Database `LabOrdersDB` (configured with 35-day PITR) two hours ago, while the parent logical SQL server `sql-pulsecrest` still exists. Can you recover `LabOrdersDB` to the exact minute before deletion?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Set Short-Term PITR retention to `3,650` days (`10 years`) and grant developers Subscription Contributor to prevent backup deletion
- B. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- C. Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 78. On a SQL Server 2022 Azure VM, a junior developer runs an unfiltered `UPDATE` at `2026-11-01 11:42:15`. After restoring the last Full (`NORECOVERY`) and Differential (`NORECOVERY`) backups to `EHR_Recovery`, which T-SQL clause on `RESTORE LOG` stops replay right before the mistake: `RESTORE LOG ... WITH ____ = '2026-11-01T11:42:14', RECOVERY`?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access
- C. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- D. Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback

### 79. What is the maximum short-term Point-in-Time Restore (`PITR`) retention period versus the maximum Long-Term Retention (`LTR`) period supported on Azure SQL Database and Azure SQL Managed Instance?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Long-Term Retention (`LTR`) weekly/monthly/yearly backups up to `10 years` protected by a locked time-based immutable (`WORM`) policy and `RA-GRS` / `ZRS` backup storage
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. Set Short-Term PITR retention to `3,650` days (`10 years`) and grant developers Subscription Contributor to prevent backup deletion

### 80. You are scripting T-SQL `BACKUP DATABASE` on a SQL Server 2022 Azure VM to write a 3.2 TB PACS metadata database to Azure Blob Storage using passwordless Managed Identity authentication. Which two steps are required? Select two.

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access
- B. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- C. Create a SQL Server `CREDENTIAL` (`IDENTITY = 'Managed Identity'` or `'SHARED ACCESS SIGNATURE'`) matching the Azure Blob container URL
- D. Stripe `BACKUP DATABASE` across multiple `TO URL = 'https://...bak'` block blob targets with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`
- E. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 81. When restoring a 4-stripe block-blob backup from Azure Blob Storage onto a SQL Server 2022 DR VM, how must `RESTORE DATABASE [PACS] FROM ...` specify the URLs?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- B. Striped T-SQL `BACKUP DATABASE ... TO URL = ...` across up to 64 block blobs (`MAXTRANSFERSIZE`, `COMPRESSION`) authenticated via `Managed Identity` or `SHARED ACCESS SIGNATURE` Credential
- C. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- D. Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access

### 82. Why should a multi-database clinical EHR workload use an Azure SQL Failover Group rather than independent Active Geo-Replication links on each database when transactional consistency across databases is mandatory?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script
- B. Failover Groups for automatic multi-database failover behind stable `<fog>.database.windows.net` / `.secondary` listeners vs Active Geo-Replication for up to 4 readable secondaries
- C. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- D. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 83. When creating an Instance Failover Group between two Azure SQL Managed Instances in different regions, what VNet and port prerequisites must exist between the primary and secondary SQL MI subnets?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- B. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- C. Failover Groups for automatic multi-database failover behind stable `<fog>.database.windows.net` / `.secondary` listeners vs Active Geo-Replication for up to 4 readable secondaries
- D. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica

### 84. You deploy a 2-node SQL Server 2022 Always On Availability Group spanning a hospital datacenter subnet (`10.10.1.0/24`) and an Azure VNet subnet (`10.20.1.0/24`). Which two configurations ensure quorum stability and fast client failover? Select two.

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Configure an Azure Cloud Witness in a standard Storage Account (`LRS`/`ZRS`) to provide lightweight quorum voting for a 2-node WSFC
- B. Deploy a Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` TCP `59999`) listener and set `MultiSubnetFailover=True` on clients
- C. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- D. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG
- E. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections

### 85. An Always On Availability Group on Azure VMs uses an Azure Internal Standard Load Balancer (`ILB`) listener on IP `10.20.1.50`. Clients can connect directly to the primary VM IP, yet connections to `10.20.1.50` time out completely. Which NSG rule is likely missing?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG
- D. Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`

### 86. How does an Always On Failover Cluster Instance (`FCI`) differ from an Always On Availability Group (`AG`) regarding storage redundancy and readable secondaries on Azure VMs?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- B. Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`)
- C. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas
- D. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching

### 87. In a T-SQL Log Shipping topology (`Primary -> Monitor -> Secondary`), which three SQL Server Agent jobs execute the replication pipeline across the servers?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- B. Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`)
- C. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 88. On an Azure SQL Database configured with Active Geo-Replication, which DMV in `master` or the user database shows `replication_state_desc` (`SEEDING`, `CATCH_UP`), `replication_lag_sec`, and `last_replication` timestamps: `SELECT * FROM sys.____`?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Query `sys.dm_hadr_database_replica_states` (`synchronization_state_desc`, `log_send_queue_size`, `redo_queue_size`) and `sys.dm_geo_replication_link_status`, plus verify NSG probe port `59999`
- D. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database

---

## Case study — CuraSpan Regional Health

CuraSpan Regional Health hosts clinical applications on Azure SQL Managed Instance in East US 2 with a paired DR region in Central US. Compliance mandates automatic multi-database regional failover under one listener endpoint, ad-hoc `.bak` exports that never disrupt differential chains, and 7-year immutable WORM backups.

The next 3 questions refer to **CuraSpan Regional Health**. Read the scenario brief once, then answer each item independently.

### 89. Which cross-region DR solution satisfies automatic multi-database failover between East US 2 and Central US under a single stable connection listener endpoint?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`)
- B. Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA
- C. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- D. Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica

### 90. Why must ad-hoc T-SQL `.bak` exports on the SQL Managed Instance always include `WITH COPY_ONLY` (`BACKUP DATABASE [EHR] TO URL = '...' WITH COPY_ONLY`)?

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Use `BACKUP DATABASE ... WITH COPY_ONLY` for ad-hoc exports on SQL MI / AGs, and Azure Backup Recovery Services Vault SQL-aware policies (`15-min` log RPO) on SQL VMs
- B. Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access
- C. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- D. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases

### 91. Which two backup configurations satisfy the 7-year HIPAA retention mandate with ransomware-proof WORM protection on SQL Managed Instance? Select two.

Domain: Plan and configure a high availability and disaster recovery (HA/DR) environment

- A. Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Enable and lock time-based immutability (`WORM`) on the LTR backup policy so nobody can shorten retention or delete compliance backups early
- D. Configure an Azure SQL Long-Term Retention (`LTR`) policy (`WeeklyRetention`, `MonthlyRetention`, `YearlyRetention`, `WeekOfYear`) up to 10 years
- E. Set Short-Term PITR retention to `3,650` days (`10 years`) and grant developers Subscription Contributor to prevent backup deletion

---

## Case study — PulseCrest Diagnostics

PulseCrest Diagnostics manages 40 Azure SQL Databases and three SQL Managed Instances. Operations wants centralized near-real-time KQL performance dashboards in Microsoft Fabric Eventhouse while planning for 2027 monitoring lifecycle changes, plus persistent Extended Events session files and I/O wait root-cause analysis.

The next 3 questions refer to **PulseCrest Diagnostics**. Read the scenario brief once, then answer each item independently.

### 92. Which monitoring solution collects agentless performance telemetry from all 40 Azure SQL Databases and 3 SQL Managed Instances into Fabric Eventhouse KQL dashboards, and what 2027 lifecycle transition must the team plan for?

Domain: Monitor, configure, and optimize database resources

- A. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- B. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables
- C. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- D. Database watcher streaming SQL DB and SQL MI telemetry into Fabric Eventhouse / Azure Data Explorer (with planned transition to Database Hub in Microsoft Fabric)

### 93. You must configure persistent Extended Events `.xel` session files for a single clinical Azure SQL Database so deadlock and timeout traces survive failovers. Which two steps are required? Select two.

Domain: Monitor, configure, and optimize database resources

- A. Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE` with `rwl` permissions) for the Azure Blob container
- B. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- C. Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching
- D. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- E. Define `CREATE EVENT SESSION ... ON DATABASE ADD TARGET package0.event_file(SET filename = N'https://...xel')` and start the session

### 94. An imaging lookup query `SELECT AccessionNo, Modality, StudyDate FROM Studies WHERE PatientMRN = @mrn` performs an `Index Seek` on `IX_Studies_PatientMRN` followed by 85,000 `Key Lookup` reads causing `PAGEIOLATCH_SH` waits. How do you eliminate the `Key Lookup`?

Domain: Monitor, configure, and optimize database resources

- A. Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon
- B. Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking
- C. Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions
- D. Replace set-based `JOIN` queries with nested `FAST_FORWARD` T-SQL cursors calling multi-statement table-valued functions per row under compat `100`

---

## Case study — SaffronChart Clinical

SaffronChart Clinical is migrating a 3.5 TB on-premises SQL Server 2022 EHR platform that relies on cross-database `JOIN` queries across four databases, SQL Server Agent jobs, and CLR assemblies into Azure PaaS with under five minutes of cutover downtime and an option to fail back to SQL Server 2022.

The next 3 questions refer to **SaffronChart Clinical**. Read the scenario brief once, then answer each item independently.

### 95. Which Azure SQL PaaS offering natively supports four-part cross-database `JOIN` queries, SQL Server Agent jobs, and safe CLR assemblies without managing guest OS patching?

Domain: Plan and implement data platform resources

- A. Azure SQL Managed Instance (Next-gen General Purpose) with decoupled IOPS and storage sliders
- B. Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled
- C. SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)
- D. Azure SQL Database Hyperscale tier with compute-isolated Named Replicas

### 96. Which migration technology replicates the 3.5 TB SQL Server 2022 EHR databases continuously to Azure SQL Managed Instance with under five minutes of cutover downtime AND preserves online failback to SQL Server 2022?

Domain: Plan and implement data platform resources

- A. Managed Instance link using a distributed Availability Group over TCP 5022 for near-zero-downtime online cutover
- B. Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy
- C. Expect online bidirectional planned failback from Azure SQL Managed Instance directly back to on-premises SQL Server 2016 without downtime
- D. Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables

### 97. On the 32-vCore Azure SQL Managed Instance, ad-hoc Epidemiology Power BI DirectQuery users occasionally consume 100% CPU. How can you cap `SG-Epidemiology` logins via `CREATE RESOURCE POOL PoolEpi WITH (____ = 25)`?

Domain: Monitor, configure, and optimize database resources

- A. Configure `cost threshold for parallelism`, `MAXDOP`, `max server memory (MB)`, and Resource Governor (`WORKLOAD GROUP` + `RESOURCE POOL` + classifier UDF) on SQL MI / VMs
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database
- D. No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases

---

## Case study — VerityMed Pharmacy

VerityMed Pharmacy records controlled-substance dispensing logs in Azure SQL Database. Regulators require cryptographic proof to external auditors that historical dispense rows were never tampered with by DBAs, Customer-Managed Key TDE stored in Azure Key Vault, and auditing restricted to classified PHI columns.

The next 3 questions refer to **VerityMed Pharmacy**. Read the scenario brief once, then answer each item independently.

### 98. In what four-step order must you configure Customer-Managed Key (`CMK`) Transparent Data Encryption in Azure Key Vault for the pharmacy logical SQL server?

Domain: Implement a secure environment

- A. Upload plaintext `.pfx` directly to Azure Table storage → Grant anonymous public read on container → Point TDE protector to Table URL → Disable TLS 1.2
- B. Set server TDE protector to Key Vault key → Disable Soft Delete and Purge Protection on Key Vault → Assign Managed Identity after encryption starts → Export DEK plaintext to Blob storage
- C. Enable Soft Delete & Purge Protection on Key Vault → Assign Managed Identity to SQL server → Grant Key Vault Crypto Service Encryption User (`get`/`wrapKey`/`unwrapKey`) → Set server TDE protector to Key Vault key
- D. Create symmetric key inside tempdb → Grant db_datareader in Key Vault → Set database compatibility level to 100 → Restart Azure SQL Database service

### 99. How do you tag PHI dispensing columns so Azure SQL Auditing captures sensitivity metadata and minimizes audit noise to sensitive accesses?

Domain: Implement a secure environment

- A. Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7
- B. Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases
- C. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- D. SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage

### 100. Which Azure SQL feature provides cryptographic Merkle-tree proof to external DEA regulators (verified via `EXEC sys.____ @digest_locations`) that historical controlled-substance dispense rows were never altered or deleted?

Domain: Implement a secure environment

- A. Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas
- B. Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history
- C. Azure SQL Ledger (`LEDGER = ON` append-only or updatable tables) storing SHA-256 database digests in Azure Confidential Ledger and verifying via `sp_verify_database_ledger`
- D. Truncate or `DELETE` historical rows from an append-only Ledger table (`LEDGER = ON (APPEND_ONLY = ON)`) to purge audit history in place

---

## Answer key and explanations

### Question 1 — D

Answer: Azure SQL Database vCore Elastic Pool with per-database min and max vCore limits. An Azure SQL Database vCore Elastic Pool shares pooled compute across staggered databases while enforcing per-database max vCores so no busy clinic starves neighboring clinics. Elastic Pools share a pooled vCore/storage envelope across many multi-tenant databases with staggered peaks while capping per-database max vCores to stop noisy-neighbor starvation. Local study-map skill 1.1 (Recommend an Azure SQL Offering (SQL Database, SQL Managed Instance, or SQL Server on Azure VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Compare Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview).

- **A:** Incorrect for this requirement. SQL Server on Azure VMs (IaaS) provides full OS access, custom third-party drivers, legacy SQL Server version pinning, SSIS/SSRS/SSAS co-hosting, and `Ebdsv5` high remote storage throughput. Why the keyed choice wins: An Azure SQL Database vCore Elastic Pool shares pooled compute across staggered databases while enforcing per-database max vCores so no busy clinic starves neighboring clinics.
- **B:** Incorrect for this requirement. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. Why the keyed choice wins: An Azure SQL Database vCore Elastic Pool shares pooled compute across staggered databases while enforcing per-database max vCores so no busy clinic starves neighboring clinics.
- **C:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: An Azure SQL Database vCore Elastic Pool shares pooled compute across staggered databases while enforcing per-database max vCores so no busy clinic starves neighboring clinics.
- **D:** Correct. Elastic Pools share a pooled vCore/storage envelope across many multi-tenant databases with staggered peaks while capping per-database max vCores to stop noisy-neighbor starvation. In this scenario: An Azure SQL Database vCore Elastic Pool shares pooled compute across staggered databases while enforcing per-database max vCores so no busy clinic starves neighboring clinics.

### Question 2 — A, C

Answers: Create a dedicated VNet subnet (`/28` or larger) with no other cloud resources and delegate it to `Microsoft.Sql/managedInstances`; Associate a User-Defined Route (`UDR`) table (`0.0.0.0/0` -> `Internet` for management plane) and required NSG rules with the SQL MI subnet. SQL Managed Instance requires an exclusive `/28+` subnet delegated to `Microsoft.Sql/managedInstances` with a bound User-Defined Route (`UDR`) table and NSG. Local study-map skill 1.2 (Choose Automated Deployment Methods and Deploy SQL Offerings Across Windows, Linux, and Containers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated deployment options for Azure SQL and SQL Server on Linux/containers (https://learn.microsoft.com/en-us/azure/azure-sql/database/arm-templates-content-guide).

- **A:** Correct. SQL Managed Instance requires an explicit route table and NSG bound to its delegated subnet so Azure management traffic is never blackholed by forced tunneling. In this scenario: SQL Managed Instance requires an exclusive `/28+` subnet delegated to `Microsoft.Sql/managedInstances` with a bound User-Defined Route (`UDR`) table and NSG.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: SQL Managed Instance requires an exclusive `/28+` subnet delegated to `Microsoft.Sql/managedInstances` with a bound User-Defined Route (`UDR`) table and NSG.
- **C:** Correct. Azure SQL Managed Instance requires an exclusive subnet delegated to `Microsoft.Sql/managedInstances` sized for current and future instance vCore/node counts. In this scenario: SQL Managed Instance requires an exclusive `/28+` subnet delegated to `Microsoft.Sql/managedInstances` with a bound User-Defined Route (`UDR`) table and NSG.
- **D:** Incorrect for this requirement. Azure Arc allows variable-workload or seasonal SQL Server hosts outside Azure to be billed hourly through an Azure subscription. Why the keyed choice wins: SQL Managed Instance requires an exclusive `/28+` subnet delegated to `Microsoft.Sql/managedInstances` with a bound User-Defined Route (`UDR`) table and NSG.
- **E:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: SQL Managed Instance requires an exclusive `/28+` subnet delegated to `Microsoft.Sql/managedInstances` with a bound User-Defined Route (`UDR`) table and NSG.

### Question 3 — C

Answer: Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`. Azure Bicep provides concise, type-checked declarative syntax that compiles transparently to idempotent ARM templates with zero external state-file management. Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. Local study-map skill 1.2 (Choose Automated Deployment Methods and Deploy SQL Offerings Across Windows, Linux, and Containers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated deployment options for Azure SQL and SQL Server on Linux/containers (https://learn.microsoft.com/en-us/azure/azure-sql/database/arm-templates-content-guide).

- **A:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Azure Bicep provides concise, type-checked declarative syntax that compiles transparently to idempotent ARM templates with zero external state-file management.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Azure Bicep provides concise, type-checked declarative syntax that compiles transparently to idempotent ARM templates with zero external state-file management.
- **C:** Correct. Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. In this scenario: Azure Bicep provides concise, type-checked declarative syntax that compiles transparently to idempotent ARM templates with zero external state-file management.
- **D:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Azure Bicep provides concise, type-checked declarative syntax that compiles transparently to idempotent ARM templates with zero external state-file management.

### Question 4 — C, D

Answers: Authenticate applications and users exclusively with Microsoft Entra ID identities, service principals, or workspace roles; Query automatically replicated OneLake Delta Parquet tables and the read-only SQL analytics endpoint from Spark and Direct Lake. SQL database in Microsoft Fabric enforces Microsoft Entra-only authentication and automatically mirrors operational tables into OneLake in Delta Parquet format alongside a SQL analytics endpoint. Local study-map skill 1.3 (Identify Use Cases for SQL Server Enabled by Azure Arc and SQL Database in Microsoft Fabric), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server enabled by Azure Arc and SQL database in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/database/sql/overview).

- **A:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: SQL database in Microsoft Fabric enforces Microsoft Entra-only authentication and automatically mirrors operational tables into OneLake in Delta Parquet format alongside a SQL analytics endpoint.
- **B:** Incorrect for this requirement. SQL database in Microsoft Fabric enforces Microsoft Entra authentication exclusively (SQL logins are unsupported) and manages backups/OneLake mirroring automatically as SaaS. Why the keyed choice wins: SQL database in Microsoft Fabric enforces Microsoft Entra-only authentication and automatically mirrors operational tables into OneLake in Delta Parquet format alongside a SQL analytics endpoint.
- **C:** Correct. SQL database in Microsoft Fabric relies exclusively on Microsoft Entra authentication and workspace/item permissions rather than SQL logins. In this scenario: SQL database in Microsoft Fabric enforces Microsoft Entra-only authentication and automatically mirrors operational tables into OneLake in Delta Parquet format alongside a SQL analytics endpoint.
- **D:** Correct. In this scenario: SQL database in Microsoft Fabric enforces Microsoft Entra-only authentication and automatically mirrors operational tables into OneLake in Delta Parquet format alongside a SQL analytics endpoint.
- **E:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: SQL database in Microsoft Fabric enforces Microsoft Entra-only authentication and automatically mirrors operational tables into OneLake in Delta Parquet format alongside a SQL analytics endpoint.

### Question 5 — D

Answer: SQL Server enabled by Azure Arc (`Microsoft.AzureArcData/sqlServerInstances`). Onboarding the pathology hosts as SQL Server enabled by Azure Arc extends Microsoft Defender for Cloud, Purview access policies, and Best Practices Assessments to on-premises SQL instances. Azure Arc projects on-premises and multicloud SQL Server instances into Azure for Resource Graph inventory, automated Best Practices Assessments, Entra auth (SQL 2022+), Defender, and PAYG billing. Local study-map skill 1.3 (Identify Use Cases for SQL Server Enabled by Azure Arc and SQL Database in Microsoft Fabric), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server enabled by Azure Arc and SQL database in Microsoft Fabric (https://learn.microsoft.com/en-us/fabric/database/sql/overview).

- **A:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Onboarding the pathology hosts as SQL Server enabled by Azure Arc extends Microsoft Defender for Cloud, Purview access policies, and Best Practices Assessments to on-premises SQL instances.
- **B:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: Onboarding the pathology hosts as SQL Server enabled by Azure Arc extends Microsoft Defender for Cloud, Purview access policies, and Best Practices Assessments to on-premises SQL instances.
- **C:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Onboarding the pathology hosts as SQL Server enabled by Azure Arc extends Microsoft Defender for Cloud, Purview access policies, and Best Practices Assessments to on-premises SQL instances.
- **D:** Correct. Azure Arc projects on-premises and multicloud SQL Server instances into Azure for Resource Graph inventory, automated Best Practices Assessments, Entra auth (SQL 2022+), Defender, and PAYG billing. In this scenario: Onboarding the pathology hosts as SQL Server enabled by Azure Arc extends Microsoft Defender for Cloud, Purview access policies, and Best Practices Assessments to on-premises SQL instances.

### Question 6 — B

Answer: SPLIT partition function for incoming future boundary → Create empty staging table on same filegroup with matching schema/indexes → ALTER TABLE ... SWITCH oldest partition to staging → Archive staging data & MERGE retired boundary. Split the new future boundary first, create a filegroup- and index-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary. Sliding-window partitioning splits a new empty future range first, performs a metadata-only `ALTER TABLE ... SWITCH` into an aligned staging table, and merges the retired boundary. Local study-map skill 1.4 (Plan for Table Partitioning (`RANGE RIGHT` / `SWITCH`) and Horizontal Database Sharding (`ShardMapManager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Table partitioning and scaling out with Azure SQL Database sharding (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-scale-introduction).

- **A:** Incorrect for this requirement. Incorrect workflow: `ALTER TABLE ... SWITCH` swaps metadata between two tables in the same database/filegroup rather than writing directly to Azure Blob Storage. Why the keyed choice wins: Split the new future boundary first, create a filegroup- and index-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary.
- **B:** Correct. Sliding-window partitioning splits a new empty future range first, performs a metadata-only `ALTER TABLE ... SWITCH` into an aligned staging table, and merges the retired boundary. In this scenario: Split the new future boundary first, create a filegroup- and index-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary.
- **C:** Incorrect for this requirement. Incorrect workflow: row-by-row `DELETE` bloats the transaction log and locks tables, and `SWITCH` fails if the staging table resides on a different filegroup or lacks aligned indexes. Why the keyed choice wins: Split the new future boundary first, create a filegroup- and index-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary.
- **D:** Incorrect for this requirement. Incorrect workflow: `SWITCH` is strictly an intra-database metadata operation requiring identical schema, filegroup alignment, and trusted constraints—never cross-database. Why the keyed choice wins: Split the new future boundary first, create a filegroup- and index-aligned empty staging table, run metadata-only `ALTER TABLE ... SWITCH`, and merge the retired oldest boundary.

### Question 7 — A

Answer: Horizontal sharding using the Elastic Database Client Library (`ShardMapManager` with `ListShardMap` or `RangeShardMap`). A `RangeShardMap` maps contiguous `[Low, High)` key intervals to individual shard databases, whereas a `ListShardMap` maps discrete individual tenant or country keys. `ListShardMap` maps discrete `TenantId` keys and `RangeShardMap` maps contiguous ID spans to independent Azure SQL Databases, routing data-dependent connections directly from the app tier. Local study-map skill 1.4 (Plan for Table Partitioning (`RANGE RIGHT` / `SWITCH`) and Horizontal Database Sharding (`ShardMapManager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Table partitioning and scaling out with Azure SQL Database sharding (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-scale-introduction).

- **A:** Correct. `ListShardMap` maps discrete `TenantId` keys and `RangeShardMap` maps contiguous ID spans to independent Azure SQL Databases, routing data-dependent connections directly from the app tier. In this scenario: A `RangeShardMap` maps contiguous `[Low, High)` key intervals to individual shard databases, whereas a `ListShardMap` maps discrete individual tenant or country keys.
- **B:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: A `RangeShardMap` maps contiguous `[Low, High)` key intervals to individual shard databases, whereas a `ListShardMap` maps discrete individual tenant or country keys.
- **C:** Incorrect for this requirement. `RANGE RIGHT` places each upper-boundary date value cleanly as the lower bound of its own monthly/daily partition, enabling metadata-only `SWITCH` archival when indexes are aligned. Why the keyed choice wins: A `RangeShardMap` maps contiguous `[Low, High)` key intervals to individual shard databases, whereas a `ListShardMap` maps discrete individual tenant or country keys.
- **D:** Incorrect for this requirement. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. Why the keyed choice wins: A `RangeShardMap` maps contiguous `[Low, High)` key intervals to individual shard databases, whereas a `ListShardMap` maps discrete individual tenant or country keys.

### Question 8 — B

Answer: SQL IaaS Agent Extension in Full management mode paired with Azure Update Manager / Automated Patching. Install the SQL IaaS Agent Extension in Full management mode and schedule recurring OS/SQL maintenance configurations through Azure Update Manager / Automated Patching. The SQL IaaS Agent Extension unlocks portal license conversion (AHB/PAYG), Automated Backup, Automated Patching windows, Key Vault integration, and storage pool management on SQL VMs. Local study-map skill 1.5 (Deploy Hybrid SQL Server Solutions and Manage Patching (`SQL IaaS Agent Extension` & `Azure Update Manager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server IaaS Agent Extension, Automated Patching, and Azure Update Manager (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-agent-extension-manually-register-single-vm).

- **A:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: Install the SQL IaaS Agent Extension in Full management mode and schedule recurring OS/SQL maintenance configurations through Azure Update Manager / Automated Patching.
- **B:** Correct. The SQL IaaS Agent Extension unlocks portal license conversion (AHB/PAYG), Automated Backup, Automated Patching windows, Key Vault integration, and storage pool management on SQL VMs. In this scenario: Install the SQL IaaS Agent Extension in Full management mode and schedule recurring OS/SQL maintenance configurations through Azure Update Manager / Automated Patching.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Install the SQL IaaS Agent Extension in Full management mode and schedule recurring OS/SQL maintenance configurations through Azure Update Manager / Automated Patching.
- **D:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Install the SQL IaaS Agent Extension in Full management mode and schedule recurring OS/SQL maintenance configurations through Azure Update Manager / Automated Patching.

### Question 9 — C

Answer: SQL Server on Linux configured via `mssql-conf` or Linux container images for consistent CI/CD dev-test parity. Setting `sqlagent.enabled true` via `mssql-conf` activates the built-in SQL Server Agent process inside SQL Server on Linux. `mssql-conf` configures memory, trace flags, Entra auth, and HA on Linux SQL Server VMs, while official Linux container images spin up fast disposable SQL instances in CI pipelines. Local study-map skill 1.5 (Deploy Hybrid SQL Server Solutions and Manage Patching (`SQL IaaS Agent Extension` & `Azure Update Manager`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server IaaS Agent Extension, Automated Patching, and Azure Update Manager (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-agent-extension-manually-register-single-vm).

- **A:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Setting `sqlagent.enabled true` via `mssql-conf` activates the built-in SQL Server Agent process inside SQL Server on Linux.
- **B:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: Setting `sqlagent.enabled true` via `mssql-conf` activates the built-in SQL Server Agent process inside SQL Server on Linux.
- **C:** Correct. `mssql-conf` configures memory, trace flags, Entra auth, and HA on Linux SQL Server VMs, while official Linux container images spin up fast disposable SQL instances in CI pipelines. In this scenario: Setting `sqlagent.enabled true` via `mssql-conf` activates the built-in SQL Server Agent process inside SQL Server on Linux.
- **D:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Setting `sqlagent.enabled true` via `mssql-conf` activates the built-in SQL Server Agent process inside SQL Server on Linux.

### Question 10 — B

Answer: Azure SQL Database Hyperscale tier with compute-isolated Named Replicas. Azure SQL Database Hyperscale decouples compute from page servers backed by snapshot-capable storage, enabling constant-time backups and fast restores even at tens of terabytes. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Local study-map skill 1.6 (Configure Azure SQL Database for Scale and Performance (`Serverless`, `Hyperscale` Named Replicas, `Elastic Pools`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure SQL Database vCore, Serverless, Hyperscale, and Elastic Pools (https://learn.microsoft.com/en-us/azure/azure-sql/database/service-tiers-vcore).

- **A:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Azure SQL Database Hyperscale decouples compute from page servers backed by snapshot-capable storage, enabling constant-time backups and fast restores even at tens of terabytes.
- **B:** Correct. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. In this scenario: Azure SQL Database Hyperscale decouples compute from page servers backed by snapshot-capable storage, enabling constant-time backups and fast restores even at tens of terabytes.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Azure SQL Database Hyperscale decouples compute from page servers backed by snapshot-capable storage, enabling constant-time backups and fast restores even at tens of terabytes.
- **D:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Azure SQL Database Hyperscale decouples compute from page servers backed by snapshot-capable storage, enabling constant-time backups and fast restores even at tens of terabytes.

### Question 11 — D

Answer: Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica. The Business Critical tier of Azure SQL Managed Instance provides local SSD storage, In-Memory OLTP support, highest IOPS-per-vCore, and one included read-scale secondary replica. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. Local study-map skill 1.7 (Configure Azure SQL Managed Instance for Scale and Performance (`Next-gen GP` Sliders & `Business Critical`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure SQL Managed Instance service tiers and Next-gen General Purpose scaling (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview).

- **A:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: The Business Critical tier of Azure SQL Managed Instance provides local SSD storage, In-Memory OLTP support, highest IOPS-per-vCore, and one included read-scale secondary replica.
- **B:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: The Business Critical tier of Azure SQL Managed Instance provides local SSD storage, In-Memory OLTP support, highest IOPS-per-vCore, and one included read-scale secondary replica.
- **C:** Incorrect for this requirement. SQL Managed Instance provides near-100% SQL Server engine compatibility (cross-DB queries, SQL Agent, CLR, Service Broker), and Next-gen GP scales IOPS independently of storage up to 500 DBs. Why the keyed choice wins: The Business Critical tier of Azure SQL Managed Instance provides local SSD storage, In-Memory OLTP support, highest IOPS-per-vCore, and one included read-scale secondary replica.
- **D:** Correct. Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica. In this scenario: The Business Critical tier of Azure SQL Managed Instance provides local SSD storage, In-Memory OLTP support, highest IOPS-per-vCore, and one included read-scale secondary replica.

### Question 12 — C, E, F

Answers: Configure `ReadOnly` Azure host caching on Premium SSD data disks hosting `.mdf` and `.ndf` database files; Configure `None` Azure host caching on dedicated managed disks hosting `.ldf` SQL Server transaction log files; Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script. Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` transaction log disks, and place `tempdb` files on the fast ephemeral local NVMe volume. Local study-map skill 1.8 (Configure SQL Server on Azure VMs for Scale and Performance (`ReadOnly`/`None` Host Caching, `tempdb` NVMe, `IFI`/`LPIM`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Performance best practices for SQL Server on Azure Virtual Machines (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-checklist).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` transaction log disks, and place `tempdb` files on the fast ephemeral local NVMe volume.
- **B:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` transaction log disks, and place `tempdb` files on the fast ephemeral local NVMe volume.
- **C:** Correct. Transaction log files perform sequential write-through flushes that do not benefit from read caching and must use `None` host caching. In this scenario: Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` transaction log disks, and place `tempdb` files on the fast ephemeral local NVMe volume.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` transaction log disks, and place `tempdb` files on the fast ephemeral local NVMe volume.
- **E:** Correct. `ReadOnly` host caching serves random OLTP data-page reads directly from Azure hypervisor RAM/SSD cache without consuming disk IOPS. In this scenario: Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` transaction log disks, and place `tempdb` files on the fast ephemeral local NVMe volume.
- **F:** Correct. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. In this scenario: Configure `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` host caching on `.ldf` transaction log disks, and place `tempdb` files on the fast ephemeral local NVMe volume.

### Question 13 — D

Answer: Yes — the proposed configuration satisfies every stated technical, security, and availability requirement. Yes — granting `Perform volume maintenance tasks` enables Instant File Initialization (`IFI`) so `.mdf`/`.ndf` data files skip zero-writing on allocation, while `Lock pages in memory` protects buffer pool RAM. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. Local study-map skill 1.8 (Configure SQL Server on Azure VMs for Scale and Performance (`ReadOnly`/`None` Host Caching, `tempdb` NVMe, `IFI`/`LPIM`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Performance best practices for SQL Server on Azure Virtual Machines (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-checklist).

- **A:** Incorrect for this requirement. SQL Server write-ahead logging performs sequential unbuffered writes; enabling `ReadOnly` or `ReadWrite` host caching on `.ldf` disks degrades throughput or risks corruption. Why the keyed choice wins: Yes — granting `Perform volume maintenance tasks` enables Instant File Initialization (`IFI`) so `.mdf`/`.ndf` data files skip zero-writing on allocation, while `Lock pages in memory` protects buffer pool RAM.
- **B:** Incorrect for this requirement. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Why the keyed choice wins: Yes — granting `Perform volume maintenance tasks` enables Instant File Initialization (`IFI`) so `.mdf`/`.ndf` data files skip zero-writing on allocation, while `Lock pages in memory` protects buffer pool RAM.
- **C:** Incorrect for this requirement. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. Why the keyed choice wins: Yes — granting `Perform volume maintenance tasks` enables Instant File Initialization (`IFI`) so `.mdf`/`.ndf` data files skip zero-writing on allocation, while `Lock pages in memory` protects buffer pool RAM.
- **D:** Correct. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. In this scenario: Yes — granting `Perform volume maintenance tasks` enables Instant File Initialization (`IFI`) so `.mdf`/`.ndf` data files skip zero-writing on allocation, while `Lock pages in memory` protects buffer pool RAM.

### Question 14 — D

Answer: Evaluate `sp_estimate_data_compression_savings` and apply `ROW`, `PAGE`, or `COLUMNSTORE_ARCHIVE` compression per partition. `sp_estimate_data_compression_savings` samples table/index pages in `tempdb` and estimates compressed versus current size for `ROW`, `PAGE`, `COLUMNSTORE`, or `COLUMNSTORE_ARCHIVE`. `sp_estimate_data_compression_savings` models space gains before compressing; `ROW`/`PAGE` shrink OLTP B-trees while `COLUMNSTORE` / `COLUMNSTORE_ARCHIVE` achieves up to 10x analytics compression. Local study-map skill 1.9 (Configure Table Partitioning Alignment and Data Compression (`ROW`, `PAGE`, `COLUMNSTORE`, `COLUMNSTORE_ARCHIVE`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure table partitioning and row/page/columnstore data compression (https://learn.microsoft.com/en-us/sql/relational-databases/data-compression/data-compression).

- **A:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: `sp_estimate_data_compression_savings` samples table/index pages in `tempdb` and estimates compressed versus current size for `ROW`, `PAGE`, `COLUMNSTORE`, or `COLUMNSTORE_ARCHIVE`.
- **B:** Incorrect for this requirement. Instant File Initialization skips zeroing `.mdf`/`.ndf` data file growth (never `.ldf`), while Lock Pages in Memory prevents Windows from paging the SQL buffer pool to disk. Why the keyed choice wins: `sp_estimate_data_compression_savings` samples table/index pages in `tempdb` and estimates compressed versus current size for `ROW`, `PAGE`, `COLUMNSTORE`, or `COLUMNSTORE_ARCHIVE`.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `sp_estimate_data_compression_savings` samples table/index pages in `tempdb` and estimates compressed versus current size for `ROW`, `PAGE`, `COLUMNSTORE`, or `COLUMNSTORE_ARCHIVE`.
- **D:** Correct. `sp_estimate_data_compression_savings` models space gains before compressing; `ROW`/`PAGE` shrink OLTP B-trees while `COLUMNSTORE` / `COLUMNSTORE_ARCHIVE` achieves up to 10x analytics compression. In this scenario: `sp_estimate_data_compression_savings` samples table/index pages in `tempdb` and estimates compressed versus current size for `ROW`, `PAGE`, `COLUMNSTORE`, or `COLUMNSTORE_ARCHIVE`.

### Question 15 — B

Answer: No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent. No — `SqlPackage` reads tables sequentially without snapshot transaction isolation across tables, so exporting a live write-heavy OLTP database directly yields inconsistent foreign-key data unless exported from a database copy. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Local study-map skill 1.10 (Evaluate Migration Requirements, Offline vs Online Strategies, and SKU Sizing via Azure Migrate & ADS), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Assess and plan SQL Server migrations using Azure Migrate and Azure SQL Migration extension (https://learn.microsoft.com/en-us/data-migration/sql-server/managed-instance/overview).

- **A:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: No — `SqlPackage` reads tables sequentially without snapshot transaction isolation across tables, so exporting a live write-heavy OLTP database directly yields inconsistent foreign-key data unless exported from a database copy.
- **B:** Correct. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. In this scenario: No — `SqlPackage` reads tables sequentially without snapshot transaction isolation across tables, so exporting a live write-heavy OLTP database directly yields inconsistent foreign-key data unless exported from a database copy.
- **C:** Incorrect for this requirement. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. Why the keyed choice wins: No — `SqlPackage` reads tables sequentially without snapshot transaction isolation across tables, so exporting a live write-heavy OLTP database directly yields inconsistent foreign-key data unless exported from a database copy.
- **D:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: No — `SqlPackage` reads tables sequentially without snapshot transaction isolation across tables, so exporting a live write-heavy OLTP database directly yields inconsistent foreign-key data unless exported from a database copy.

### Question 16 — A

Answer: Verify VNet peering & TCP 5022 + 11000-11999 rules → Start online Database Move from source to target SQL MI → Wait for seeding to reach Ready for completion → Complete move within 24 hours so target comes online. Verify VNet peering plus TCP `5022` and `11000–11999` rules first, start the online Database Move, wait for `Ready for completion`, and manually complete the move within 24 hours. Online SQL MI database move requires bidirectional TCP 5022 and 11000–11999 connectivity, seeds asynchronously until Ready for completion, and must be manually completed within 24 hours. Local study-map skill 1.12 (Implement Azure SQL Managed Instance Online Database Copy and Move (`24h` Completion, `TCP 5022`/`11000-11999`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Copy or move a database online across Azure SQL Managed Instances (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/database-copy-move-how-to).

- **A:** Correct. Online SQL MI database move requires bidirectional TCP 5022 and 11000–11999 connectivity, seeds asynchronously until Ready for completion, and must be manually completed within 24 hours. In this scenario: Verify VNet peering plus TCP `5022` and `11000–11999` rules first, start the online Database Move, wait for `Ready for completion`, and manually complete the move within 24 hours.
- **B:** Incorrect for this requirement. Incorrect workflow: network ports must be open before seeding, operations uncompleted after 24 hours auto-cancel, and source PITR history never transfers with a moved database. Why the keyed choice wins: Verify VNet peering plus TCP `5022` and `11000–11999` rules first, start the online Database Move, wait for `Ready for completion`, and manually complete the move within 24 hours.
- **C:** Incorrect for this requirement. Incorrect workflow: `sp_detach_db` is unsupported in Azure SQL Managed Instance and online Database Move replicates via Always On availability group seeding without stopping compute. Why the keyed choice wins: Verify VNet peering plus TCP `5022` and `11000–11999` rules first, start the online Database Move, wait for `Ready for completion`, and manually complete the move within 24 hours.
- **D:** Incorrect for this requirement. Incorrect workflow: `.bacpac` files are stored in Blob storage rather than Table storage, the completion window is 24 hours, and Move removes the source DB upon completion. Why the keyed choice wins: Verify VNet peering plus TCP `5022` and `11000–11999` rules first, start the online Database Move, wait for `Ready for completion`, and manually complete the move within 24 hours.

### Question 17 — B

Answer: Enable Microsoft Entra-only authentication (`azuread_authentication_only`) on the logical SQL server or SQL Managed Instance. Enabling Microsoft Entra-only authentication disables Mixed Mode SQL password logins instance-wide so only Microsoft Entra users, groups, and Managed Identities can authenticate. Microsoft Entra-only authentication disables legacy SQL Server logins (`sa` and password auth) completely, enforcing centralized MFA, Conditional Access, and token-based Managed Identities. Local study-map skill 2.1 (Configure Microsoft Entra ID and Microsoft Entra-Only Authentication Across SQL DB, SQL MI, and SQL Server), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure and manage Microsoft Entra authentication with Azure SQL and SQL Server (https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Enabling Microsoft Entra-only authentication disables Mixed Mode SQL password logins instance-wide so only Microsoft Entra users, groups, and Managed Identities can authenticate.
- **B:** Correct. Microsoft Entra-only authentication disables legacy SQL Server logins (`sa` and password auth) completely, enforcing centralized MFA, Conditional Access, and token-based Managed Identities. In this scenario: Enabling Microsoft Entra-only authentication disables Mixed Mode SQL password logins instance-wide so only Microsoft Entra users, groups, and Managed Identities can authenticate.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Enabling Microsoft Entra-only authentication disables Mixed Mode SQL password logins instance-wide so only Microsoft Entra users, groups, and Managed Identities can authenticate.
- **D:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Enabling Microsoft Entra-only authentication disables Mixed Mode SQL password logins instance-wide so only Microsoft Entra users, groups, and Managed Identities can authenticate.

### Question 18 — A

Answer: Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`). Adding the contained Managed Identity user to fixed database role `db_datawriter` (`ALTER ROLE db_datawriter ADD MEMBER ...`) grants least-privilege `INSERT`/`UPDATE`/`DELETE` rights without `db_owner`. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. Local study-map skill 2.1 (Configure Microsoft Entra ID and Microsoft Entra-Only Authentication Across SQL DB, SQL MI, and SQL Server), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure and manage Microsoft Entra authentication with Azure SQL and SQL Server (https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview).

- **A:** Correct. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. In this scenario: Adding the contained Managed Identity user to fixed database role `db_datawriter` (`ALTER ROLE db_datawriter ADD MEMBER ...`) grants least-privilege `INSERT`/`UPDATE`/`DELETE` rights without `db_owner`.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Adding the contained Managed Identity user to fixed database role `db_datawriter` (`ALTER ROLE db_datawriter ADD MEMBER ...`) grants least-privilege `INSERT`/`UPDATE`/`DELETE` rights without `db_owner`.
- **C:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Adding the contained Managed Identity user to fixed database role `db_datawriter` (`ALTER ROLE db_datawriter ADD MEMBER ...`) grants least-privilege `INSERT`/`UPDATE`/`DELETE` rights without `db_owner`.
- **D:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Adding the contained Managed Identity user to fixed database role `db_datawriter` (`ALTER ROLE db_datawriter ADD MEMBER ...`) grants least-privilege `INSERT`/`UPDATE`/`DELETE` rights without `db_owner`.

### Question 19 — B

Answer: Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or `Entra Kerberos`). Configure Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos, registering the SQL MI Kerberos service principal in Entra ID. Microsoft Entra Kerberos issues Kerberos tickets for SQL Managed Instance without requiring customer-managed Active Directory Domain Services domain controllers inside Azure. Local study-map skill 2.2 (Configure Authentication for SQL Server on Azure VMs and SQL MI (`Microsoft Entra Kerberos` & AD Trusts)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos and AD (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/winauth-azuread-overview).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos, registering the SQL MI Kerberos service principal in Entra ID.
- **B:** Correct. Microsoft Entra Kerberos issues Kerberos tickets for SQL Managed Instance without requiring customer-managed Active Directory Domain Services domain controllers inside Azure. In this scenario: Configure Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos, registering the SQL MI Kerberos service principal in Entra ID.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Configure Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos, registering the SQL MI Kerberos service principal in Entra ID.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Configure Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos, registering the SQL MI Kerberos service principal in Entra ID.

### Question 20 — D

Answer: Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`). Contained database users store authentication metadata inside the replicated user database itself, avoiding orphaned SID mismatches in `master` after a regional failover. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. Local study-map skill 2.3 (Configure Security Principals and Portable Contained Microsoft Entra Users (`FROM EXTERNAL PROVIDER`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Contained database users and Microsoft Entra security principals in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Contained database users store authentication metadata inside the replicated user database itself, avoiding orphaned SID mismatches in `master` after a regional failover.
- **B:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Contained database users store authentication metadata inside the replicated user database itself, avoiding orphaned SID mismatches in `master` after a regional failover.
- **C:** Incorrect for this requirement. Restoring a `.bak` onto another instance mismatches login SIDs (fixed via `ALTER USER ... WITH LOGIN`), while an explicit table/schema `DENY` always overrides `db_datareader` role `GRANT`s. Why the keyed choice wins: Contained database users store authentication metadata inside the replicated user database itself, avoiding orphaned SID mismatches in `master` after a regional failover.
- **D:** Correct. Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members. In this scenario: Contained database users store authentication metadata inside the replicated user database itself, avoiding orphaned SID mismatches in `master` after a regional failover.

### Question 21 — D

Answer: Built-in granular server-level roles (`##MS_ServerStateReader##`, `##MS_DefinitionReader##`) or `GRANT VIEW DATABASE PERFORMANCE STATE`. Adding the scanner identity to `##MS_DefinitionReader##` grants `VIEW ANY DEFINITION` across the logical server without granting `SELECT` access to underlying clinical data rows. Modern granular server roles and state permissions let monitoring accounts inspect DMVs and metadata without granting `sysadmin`, `db_owner`, or `SELECT` access to user tables. Local study-map skill 2.3 (Configure Security Principals and Portable Contained Microsoft Entra Users (`FROM EXTERNAL PROVIDER`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Contained database users and Microsoft Entra security principals in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage).

- **A:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Adding the scanner identity to `##MS_DefinitionReader##` grants `VIEW ANY DEFINITION` across the logical server without granting `SELECT` access to underlying clinical data rows.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Adding the scanner identity to `##MS_DefinitionReader##` grants `VIEW ANY DEFINITION` across the logical server without granting `SELECT` access to underlying clinical data rows.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Adding the scanner identity to `##MS_DefinitionReader##` grants `VIEW ANY DEFINITION` across the logical server without granting `SELECT` access to underlying clinical data rows.
- **D:** Correct. Modern granular server roles and state permissions let monitoring accounts inspect DMVs and metadata without granting `sysadmin`, `db_owner`, or `SELECT` access to user tables. In this scenario: Adding the scanner identity to `##MS_DefinitionReader##` grants `VIEW ANY DEFINITION` across the logical server without granting `SELECT` access to underlying clinical data rows.

### Question 22 — A

Answer: Stored procedure encapsulation using schema ownership chaining, `EXECUTE AS OWNER`, or certificate module signing. Specifying `WITH EXECUTE AS 'rx_verifier'` (or signing the module with a certificate) switches permission checks inside the stored procedure to `rx_verifier` without granting callers direct table rights. Granting `EXECUTE` on a schema-owned or certificate-signed stored procedure lets callers run controlled DML/DDL workflows without direct table-level `SELECT`, `UPDATE`, or `IMPERSONATE` rights. Local study-map skill 2.4 (Apply Least Privilege Using Granular Server/Database Roles, Schema Chaining, `EXECUTE AS`, and T-SQL/GUI Tools), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Permissions hierarchy, server-level roles, and principle of least privilege in SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/security-server-roles).

- **A:** Correct. Granting `EXECUTE` on a schema-owned or certificate-signed stored procedure lets callers run controlled DML/DDL workflows without direct table-level `SELECT`, `UPDATE`, or `IMPERSONATE` rights. In this scenario: Specifying `WITH EXECUTE AS 'rx_verifier'` (or signing the module with a certificate) switches permission checks inside the stored procedure to `rx_verifier` without granting callers direct table rights.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Specifying `WITH EXECUTE AS 'rx_verifier'` (or signing the module with a certificate) switches permission checks inside the stored procedure to `rx_verifier` without granting callers direct table rights.
- **C:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Specifying `WITH EXECUTE AS 'rx_verifier'` (or signing the module with a certificate) switches permission checks inside the stored procedure to `rx_verifier` without granting callers direct table rights.
- **D:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Specifying `WITH EXECUTE AS 'rx_verifier'` (or signing the module with a certificate) switches permission checks inside the stored procedure to `rx_verifier` without granting callers direct table rights.

### Question 23 — B

Answer: No — standard Deterministic Always Encrypted supports equality (`=`) joins/filters only, never `LIKE` or range predicates. No — standard Deterministic Always Encrypted without a secure enclave (`ALLOW_ENCLAVE_COMPUTATIONS`) supports equality (`=`) comparisons only and rejects `LIKE` wildcard filters. Without a secure enclave (`ALLOW_ENCLAVE_COMPUTATIONS`), Deterministic encryption permits equality comparisons only and rejects `LIKE`, `<`, `>`, or `BETWEEN` predicates. Local study-map skill 2.4 (Apply Least Privilege Using Granular Server/Database Roles, Schema Chaining, `EXECUTE AS`, and T-SQL/GUI Tools), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Permissions hierarchy, server-level roles, and principle of least privilege in SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/security-server-roles).

- **A:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: No — standard Deterministic Always Encrypted without a secure enclave (`ALLOW_ENCLAVE_COMPUTATIONS`) supports equality (`=`) comparisons only and rejects `LIKE` wildcard filters.
- **B:** Correct. Without a secure enclave (`ALLOW_ENCLAVE_COMPUTATIONS`), Deterministic encryption permits equality comparisons only and rejects `LIKE`, `<`, `>`, or `BETWEEN` predicates. In this scenario: No — standard Deterministic Always Encrypted without a secure enclave (`ALLOW_ENCLAVE_COMPUTATIONS`) supports equality (`=`) comparisons only and rejects `LIKE` wildcard filters.
- **C:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: No — standard Deterministic Always Encrypted without a secure enclave (`ALLOW_ENCLAVE_COMPUTATIONS`) supports equality (`=`) comparisons only and rejects `LIKE` wildcard filters.
- **D:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: No — standard Deterministic Always Encrypted without a secure enclave (`ALLOW_ENCLAVE_COMPUTATIONS`) supports equality (`=`) comparisons only and rejects `LIKE` wildcard filters.

### Question 24 — D

Answer: Remap orphaned database users (`ALTER USER [u] WITH LOGIN = [u]`) and inspect explicit `DENY` permissions via `sys.database_permissions`. `sys.fn_my_permissions('Chart.PsychNotes', 'OBJECT')` evaluates the caller's effective permissions, confirming that an explicit `DENY` on `SG-Contractors` overrides the `GRANT` inherited from `SG-Clinicians`. Restoring a `.bak` onto another instance mismatches login SIDs (fixed via `ALTER USER ... WITH LOGIN`), while an explicit table/schema `DENY` always overrides `db_datareader` role `GRANT`s. Local study-map skill 2.5 (Troubleshoot Authentication and Authorization Issues (Orphaned Users `ALTER USER WITH LOGIN` & `DENY` Precedence)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot SQL login, orphaned user, and Microsoft Entra authorization issues (https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/troubleshoot-orphaned-users-sql-server).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: `sys.fn_my_permissions('Chart.PsychNotes', 'OBJECT')` evaluates the caller's effective permissions, confirming that an explicit `DENY` on `SG-Contractors` overrides the `GRANT` inherited from `SG-Clinicians`.
- **B:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: `sys.fn_my_permissions('Chart.PsychNotes', 'OBJECT')` evaluates the caller's effective permissions, confirming that an explicit `DENY` on `SG-Contractors` overrides the `GRANT` inherited from `SG-Clinicians`.
- **C:** Incorrect for this requirement. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. Why the keyed choice wins: `sys.fn_my_permissions('Chart.PsychNotes', 'OBJECT')` evaluates the caller's effective permissions, confirming that an explicit `DENY` on `SG-Contractors` overrides the `GRANT` inherited from `SG-Clinicians`.
- **D:** Correct. Restoring a `.bak` onto another instance mismatches login SIDs (fixed via `ALTER USER ... WITH LOGIN`), while an explicit table/schema `DENY` always overrides `db_datareader` role `GRANT`s. In this scenario: `sys.fn_my_permissions('Chart.PsychNotes', 'OBJECT')` evaluates the caller's effective permissions, confirming that an explicit `DENY` on `SG-Contractors` overrides the `GRANT` inherited from `SG-Clinicians`.

### Question 25 — B, D

Answers: Enable both `Soft Delete` and `Purge Protection` on the Azure Key Vault or Managed HSM storing the TDE protector key; Grant the SQL server Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) on the Key Vault. Enable `Soft Delete` and `Purge Protection` on the Key Vault, and grant the SQL server's Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`). Local study-map skill 2.6 (Implement Transparent Data Encryption (`TDE`) with Service-Managed Keys, Key Vault `CMK`, and VM Cert Backups), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Transparent Data Encryption (TDE) with service-managed and customer-managed keys in Key Vault (https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Enable `Soft Delete` and `Purge Protection` on the Key Vault, and grant the SQL server's Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`).
- **B:** Correct. The logical SQL server or SQL MI Managed Identity requires `get`, `wrapKey`, and `unwrapKey` permissions to wrap and unwrap the Database Encryption Key (`DEK`). In this scenario: Enable `Soft Delete` and `Purge Protection` on the Key Vault, and grant the SQL server's Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`).
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Enable `Soft Delete` and `Purge Protection` on the Key Vault, and grant the SQL server's Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`).
- **D:** Correct. Azure SQL requires both Soft Delete and Purge Protection on Key Vault so accidental or malicious key deletion can never permanently brick encrypted databases. In this scenario: Enable `Soft Delete` and `Purge Protection` on the Key Vault, and grant the SQL server's Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`).
- **E:** Incorrect for this requirement. Transaction log files perform sequential write-through flushes that do not benefit from read caching and must use `None` host caching. Why the keyed choice wins: Enable `Soft Delete` and `Purge Protection` on the Key Vault, and grant the SQL server's Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`).

### Question 26 — D

Answer: Column-level encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey`) plus `Minimal TLS version = 1.2`. Setting `--minimal-tls-version 1.2` rejects TLS 1.0/1.1 handshakes at the SQL gateway and ensures all TDS connections negotiate TLS 1.2 or higher. T-SQL cell-level symmetric key encryption protects specific columns inside the engine while enforcing TLS 1.2+ encrypts all TDS client traffic in transit. Local study-map skill 2.7 (Implement Object/Column-Level Encryption (`Symmetric Keys` / `Certificates`) and Enforce `Minimal TLS 1.2`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Column-level symmetric key encryption and TLS 1.2 in-transit encryption (https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/encrypt-a-column-of-data).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Setting `--minimal-tls-version 1.2` rejects TLS 1.0/1.1 handshakes at the SQL gateway and ensures all TDS connections negotiate TLS 1.2 or higher.
- **B:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Setting `--minimal-tls-version 1.2` rejects TLS 1.0/1.1 handshakes at the SQL gateway and ensures all TDS connections negotiate TLS 1.2 or higher.
- **C:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Setting `--minimal-tls-version 1.2` rejects TLS 1.0/1.1 handshakes at the SQL gateway and ensures all TDS connections negotiate TLS 1.2 or higher.
- **D:** Correct. T-SQL cell-level symmetric key encryption protects specific columns inside the engine while enforcing TLS 1.2+ encrypts all TDS client traffic in transit. In this scenario: Setting `--minimal-tls-version 1.2` rejects TLS 1.0/1.1 handshakes at the SQL gateway and ensures all TDS connections negotiate TLS 1.2 or higher.

### Question 27 — C

Answer: Yes — the proposed configuration satisfies every stated technical, security, and availability requirement. Yes — creating a database-level IP firewall rule (`sp_set_database_firewall_rule`) scopes access strictly to `ToxicologyDB` and replicates inside the user database to geo-secondaries. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. Local study-map skill 2.8 (Configure Server-Level (`master`) vs Portable Database-Level IP Firewall Rules (`sp_set_database_firewall_rule`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Server-level and database-level IP firewall rules in Azure SQL Database (https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure).

- **A:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: Yes — creating a database-level IP firewall rule (`sp_set_database_firewall_rule`) scopes access strictly to `ToxicologyDB` and replicates inside the user database to geo-secondaries.
- **B:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: Yes — creating a database-level IP firewall rule (`sp_set_database_firewall_rule`) scopes access strictly to `ToxicologyDB` and replicates inside the user database to geo-secondaries.
- **C:** Correct. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. In this scenario: Yes — creating a database-level IP firewall rule (`sp_set_database_firewall_rule`) scopes access strictly to `ToxicologyDB` and replicates inside the user database to geo-secondaries.
- **D:** Incorrect for this requirement. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. Why the keyed choice wins: Yes — creating a database-level IP firewall rule (`sp_set_database_firewall_rule`) scopes access strictly to `ToxicologyDB` and replicates inside the user database to geo-secondaries.

### Question 28 — D

Answer: Enable VBS enclave on Azure SQL Database → Provision Key Vault CMK & enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`) → Grant client Key Vault key permissions & attestation → Run in-place `ALTER TABLE` encryption. Enable a VBS secure enclave on the Azure SQL Database first, create a Key Vault CMK and enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), configure client Key Vault/attestation access, and run in-place `ALTER TABLE` encryption. In-place Always Encrypted with VBS enclaves requires enabling a VBS enclave on the DB, creating an enclave-enabled CEK (`ALLOW_ENCLAVE_COMPUTATIONS`), and running cryptographic operations inside the enclave. Local study-map skill 2.9 (Implement Always Encrypted (`Deterministic` vs `Randomized`) and Always Encrypted with VBS/SGX Secure Enclaves), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always Encrypted and Always Encrypted with secure enclaves (https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves).

- **A:** Incorrect for this requirement. Incorrect workflow: `LIKE` pattern queries on Always Encrypted columns require `Column Encryption Setting=Enabled`, enclave attestation, and Randomized/enclave-enabled encryption. Why the keyed choice wins: Enable a VBS secure enclave on the Azure SQL Database first, create a Key Vault CMK and enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), configure client Key Vault/attestation access, and run in-place `ALTER TABLE` encryption.
- **B:** Incorrect for this requirement. Incorrect workflow: Always Encrypted keeps CMKs out of SQL engine T-SQL reach so DBAs cannot decrypt data; enclaves process keys only inside attested enclave memory. Why the keyed choice wins: Enable a VBS secure enclave on the Azure SQL Database first, create a Key Vault CMK and enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), configure client Key Vault/attestation access, and run in-place `ALTER TABLE` encryption.
- **C:** Incorrect for this requirement. Incorrect workflow: in-place encryption fails unless the database enclave is active and the CEK was created with `ENCLAVE_COMPUTATIONS` beforehand; CMKs never live in `sys.configurations`. Why the keyed choice wins: Enable a VBS secure enclave on the Azure SQL Database first, create a Key Vault CMK and enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), configure client Key Vault/attestation access, and run in-place `ALTER TABLE` encryption.
- **D:** Correct. In-place Always Encrypted with VBS enclaves requires enabling a VBS enclave on the DB, creating an enclave-enabled CEK (`ALLOW_ENCLAVE_COMPUTATIONS`), and running cryptographic operations inside the enclave. In this scenario: Enable a VBS secure enclave on the Azure SQL Database first, create a Key Vault CMK and enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), configure client Key Vault/attestation access, and run in-place `ALTER TABLE` encryption.

### Question 29 — B, C

Answers: Provision a Column Master Key in Key Vault and create a Column Encryption Key with `ENCLAVE_COMPUTATIONS` enabled; Enable `Column Encryption Setting=Enabled` and pass the `Enclave Attestation Url` (or VBS zero-attestation setting) in client drivers. Provision a Key Vault CMK plus an enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), and enable `Column Encryption Setting=Enabled` with enclave attestation in client connection strings. Local study-map skill 2.9 (Implement Always Encrypted (`Deterministic` vs `Randomized`) and Always Encrypted with VBS/SGX Secure Enclaves), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always Encrypted and Always Encrypted with secure enclaves (https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Provision a Key Vault CMK plus an enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), and enable `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.
- **B:** Correct. Rich confidential queries (`LIKE`, `<`, `>`, sorting) and in-place encryption require a CEK explicitly marked to permit enclave computations. In this scenario: Provision a Key Vault CMK plus an enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), and enable `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.
- **C:** Correct. Client drivers must enable Always Encrypted and verify enclave attestation before transmitting CEKs over TLS into the SQL secure enclave. In this scenario: Provision a Key Vault CMK plus an enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), and enable `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Provision a Key Vault CMK plus an enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), and enable `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.
- **E:** Incorrect for this requirement. `ReadOnly` host caching serves random OLTP data-page reads directly from Azure hypervisor RAM/SSD cache without consuming disk IOPS. Why the keyed choice wins: Provision a Key Vault CMK plus an enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`), and enable `Column Encryption Setting=Enabled` with enclave attestation in client connection strings.

### Question 30 — A, D

Answers: Link Private DNS Zone `privatelink.database.windows.net` (or forward on-premises DNS) to resolve `<server>.database.windows.net` to the private IP; Set `Public network access = Disabled` (`publicNetworkAccess: Disabled`) on the logical SQL server so internet connections are rejected. Link Private DNS Zone `privatelink.database.windows.net` so clients resolve the SQL FQDN to the private endpoint IP, and set `Public network access = Disabled` on the logical SQL server. Local study-map skill 2.10 (Configure Azure Private Link (`privatelink.database.windows.net`), Service Endpoints, and SQL MI Subnet Security), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure Private Link, Virtual Network service endpoints, and SQL MI VNet security (https://learn.microsoft.com/en-us/azure/azure-sql/database/private-endpoint-overview).

- **A:** Correct. Clients still validate the TLS certificate for `<server>.database.windows.net`, so split-brain DNS must map the canonical FQDN via CNAME to `privatelink.database.windows.net`. In this scenario: Link Private DNS Zone `privatelink.database.windows.net` so clients resolve the SQL FQDN to the private endpoint IP, and set `Public network access = Disabled` on the logical SQL server.
- **B:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Link Private DNS Zone `privatelink.database.windows.net` so clients resolve the SQL FQDN to the private endpoint IP, and set `Public network access = Disabled` on the logical SQL server.
- **C:** Incorrect for this requirement. Azure Arc allows variable-workload or seasonal SQL Server hosts outside Azure to be billed hourly through an Azure subscription. Why the keyed choice wins: Link Private DNS Zone `privatelink.database.windows.net` so clients resolve the SQL FQDN to the private endpoint IP, and set `Public network access = Disabled` on the logical SQL server.
- **D:** Correct. Creating a Private Endpoint alone leaves the public endpoint reachable unless `Public network access` is explicitly disabled on the server. In this scenario: Link Private DNS Zone `privatelink.database.windows.net` so clients resolve the SQL FQDN to the private endpoint IP, and set `Public network access = Disabled` on the logical SQL server.
- **E:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Link Private DNS Zone `privatelink.database.windows.net` so clients resolve the SQL FQDN to the private endpoint IP, and set `Public network access = Disabled` on the logical SQL server.

### Question 31 — B

Answer: Virtual Network Service Endpoints (`Microsoft.Sql`) with outbound storage firewall rules, or dedicated `/28+` delegated subnet for SQL MI. A VNet Service Endpoint restricts connections at the SQL public endpoint to traffic originating from that VNet/subnet IP backbone without assigning a private RFC 1918 IP, whereas Private Endpoint maps a private VNet IP and lets you disable public access completely. VNet Service Endpoints restrict Azure SQL public endpoint traffic to a specific VNet subnet without private IPs, whereas SQL Managed Instance deploys directly into a dedicated delegated VNet subnet. Local study-map skill 2.10 (Configure Azure Private Link (`privatelink.database.windows.net`), Service Endpoints, and SQL MI Subnet Security), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure Private Link, Virtual Network service endpoints, and SQL MI VNet security (https://learn.microsoft.com/en-us/azure/azure-sql/database/private-endpoint-overview).

- **A:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: A VNet Service Endpoint restricts connections at the SQL public endpoint to traffic originating from that VNet/subnet IP backbone without assigning a private RFC 1918 IP, whereas Private Endpoint maps a private VNet IP and lets you disable public access completely.
- **B:** Correct. VNet Service Endpoints restrict Azure SQL public endpoint traffic to a specific VNet subnet without private IPs, whereas SQL Managed Instance deploys directly into a dedicated delegated VNet subnet. In this scenario: A VNet Service Endpoint restricts connections at the SQL public endpoint to traffic originating from that VNet/subnet IP backbone without assigning a private RFC 1918 IP, whereas Private Endpoint maps a private VNet IP and lets you disable public access completely.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: A VNet Service Endpoint restricts connections at the SQL public endpoint to traffic originating from that VNet/subnet IP backbone without assigning a private RFC 1918 IP, whereas Private Endpoint maps a private VNet IP and lets you disable public access completely.
- **D:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: A VNet Service Endpoint restricts connections at the SQL public endpoint to traffic originating from that VNet/subnet IP backbone without assigning a private RFC 1918 IP, whereas Private Endpoint maps a private VNet IP and lets you disable public access completely.

### Question 32 — A

Answer: SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage. `sys.sensitivity_classifications` exposes every column's assigned `label`, `label_id`, `information_type`, and `rank` set via `ADD SENSITIVITY CLASSIFICATION` or the portal classification blade. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. Local study-map skill 2.11 (Apply SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) and Server/Database Auditing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Data Discovery and Classification and Azure SQL Auditing (https://learn.microsoft.com/en-us/azure/azure-sql/database/auditing-overview).

- **A:** Correct. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. In this scenario: `sys.sensitivity_classifications` exposes every column's assigned `label`, `label_id`, `information_type`, and `rank` set via `ADD SENSITIVITY CLASSIFICATION` or the portal classification blade.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: `sys.sensitivity_classifications` exposes every column's assigned `label`, `label_id`, `information_type`, and `rank` set via `ADD SENSITIVITY CLASSIFICATION` or the portal classification blade.
- **C:** Incorrect for this requirement. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. Why the keyed choice wins: `sys.sensitivity_classifications` exposes every column's assigned `label`, `label_id`, `information_type`, and `rank` set via `ADD SENSITIVITY CLASSIFICATION` or the portal classification blade.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: `sys.sensitivity_classifications` exposes every column's assigned `label`, `label_id`, `information_type`, and `rank` set via `ADD SENSITIVITY CLASSIFICATION` or the portal classification blade.

### Question 33 — C

Answer: Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history. Change Data Capture (`CDC`) reads the transaction log asynchronously to record every intermediate `INSERT`, `DELETE`, and before/after `UPDATE` row image in `cdc.*_CT` change tables. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. Local study-map skill 2.12 (Implement Change Tracking (`CHANGETABLE`) vs Change Data Capture (`CDC`) for Downstream Data Changes), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Track data changes with Change Tracking (CT) and Change Data Capture (CDC) (https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/track-data-changes-sql-server).

- **A:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Change Data Capture (`CDC`) reads the transaction log asynchronously to record every intermediate `INSERT`, `DELETE`, and before/after `UPDATE` row image in `cdc.*_CT` change tables.
- **B:** Incorrect for this requirement. CDC requires `S3+` or `vCore` tiers in Azure SQL Database, and Change Tracking stores only net version numbers/PKs—never intermediate before/after column values. Why the keyed choice wins: Change Data Capture (`CDC`) reads the transaction log asynchronously to record every intermediate `INSERT`, `DELETE`, and before/after `UPDATE` row image in `cdc.*_CT` change tables.
- **C:** Correct. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. In this scenario: Change Data Capture (`CDC`) reads the transaction log asynchronously to record every intermediate `INSERT`, `DELETE`, and before/after `UPDATE` row image in `cdc.*_CT` change tables.
- **D:** Incorrect for this requirement. Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers. Why the keyed choice wins: Change Data Capture (`CDC`) reads the transaction log asynchronously to record every intermediate `INSERT`, `DELETE`, and before/after `UPDATE` row image in `cdc.*_CT` change tables.

### Question 34 — D

Answer: Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas. Dynamic Data Masking's `partial(prefix, "padding", suffix)` function reveals the first 4 and final 3 characters while replacing middle characters with `"XXXXXX"`. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Local study-map skill 2.13 (Implement Dynamic Data Masking (`default`, `email`, `partial`, `random`) and Scoped `UNMASK` Permissions), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Dynamic Data Masking (DDM) in Azure SQL Database, SQL Managed Instance, and SQL Server (https://learn.microsoft.com/en-us/azure/azure-sql/database/dynamic-data-masking-overview).

- **A:** Incorrect for this requirement. RLS transparently filters `SELECT`/`UPDATE`/`DELETE` rows via `FILTER PREDICATE` and blocks unauthorized cross-tenant `INSERT`/`UPDATE` writes via `BLOCK PREDICATE` inside the engine. Why the keyed choice wins: Dynamic Data Masking's `partial(prefix, "padding", suffix)` function reveals the first 4 and final 3 characters while replacing middle characters with `"XXXXXX"`.
- **B:** Incorrect for this requirement. BYOK TDE wraps the symmetric Database Encryption Key (`DEK`) with an asymmetric RSA key in Key Vault or Managed HSM so security admins control key rotation and instant revocation. Why the keyed choice wins: Dynamic Data Masking's `partial(prefix, "padding", suffix)` function reveals the first 4 and final 3 characters while replacing middle characters with `"XXXXXX"`.
- **C:** Incorrect for this requirement. Always Encrypted keeps Column Master Keys on trusted clients/Key Vault; `Randomized` produces distinct ciphertexts for identical plaintexts while `Deterministic` enables equality lookups. Why the keyed choice wins: Dynamic Data Masking's `partial(prefix, "padding", suffix)` function reveals the first 4 and final 3 characters while replacing middle characters with `"XXXXXX"`.
- **D:** Correct. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. In this scenario: Dynamic Data Masking's `partial(prefix, "padding", suffix)` function reveals the first 4 and final 3 characters while replacing middle characters with `"XXXXXX"`.

### Question 35 — B, C, E

Answers: Create an inline table-valued function `WITH SCHEMABINDING` evaluating `SESSION_CONTEXT()` or `DATABASE_PRINCIPAL_ID()`; Add a `FILTER PREDICATE` in `CREATE SECURITY POLICY` to hide non-matching rows silently from `SELECT`, `UPDATE`, and `DELETE`; Add `AFTER INSERT` and `AFTER UPDATE` / `BEFORE UPDATE` `BLOCK PREDICATE` clauses in `CREATE SECURITY POLICY` (`STATE = ON`). Create a `SCHEMABINDING` inline TVF predicate and attach both a `FILTER PREDICATE` and `BLOCK PREDICATE` inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`. Local study-map skill 2.14 (Implement Cryptographic Ledger in Azure SQL (`Azure Confidential Ledger`) and Row-Level Security (`FILTER`/`BLOCK`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Ledger cryptographic tamper-evidence and Row-Level Security (RLS) in Azure SQL (https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-overview).

- **A:** Incorrect for this requirement. Append-only Ledger tables strictly block `UPDATE`, `DELETE`, and `TRUNCATE` statements in the SQL engine so cryptographic audit trails cannot be altered. Why the keyed choice wins: Create a `SCHEMABINDING` inline TVF predicate and attach both a `FILTER PREDICATE` and `BLOCK PREDICATE` inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **B:** Correct. `BLOCK PREDICATE` raises an error if a shared application login attempts to insert or update a row carrying another tenant's identifier. In this scenario: Create a `SCHEMABINDING` inline TVF predicate and attach both a `FILTER PREDICATE` and `BLOCK PREDICATE` inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **C:** Correct. `FILTER PREDICATE` injects the security TVF into read, update, and delete operators transparently without changing application `SELECT` statements. In this scenario: Create a `SCHEMABINDING` inline TVF predicate and attach both a `FILTER PREDICATE` and `BLOCK PREDICATE` inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Create a `SCHEMABINDING` inline TVF predicate and attach both a `FILTER PREDICATE` and `BLOCK PREDICATE` inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **E:** Correct. RLS predicate functions must be inline TVFs bound with `SCHEMABINDING` so underlying columns cannot be altered silently and query plans inline cleanly. In this scenario: Create a `SCHEMABINDING` inline TVF predicate and attach both a `FILTER PREDICATE` and `BLOCK PREDICATE` inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.
- **F:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Create a `SCHEMABINDING` inline TVF predicate and attach both a `FILTER PREDICATE` and `BLOCK PREDICATE` inside `CREATE SECURITY POLICY ... WITH (STATE = ON)`.

### Question 36 — D

Answer: Azure Monitor metrics paired with `sys.dm_db_resource_stats` (single DB) or `sys.server_resource_stats` (SQL MI) for 15-second CPU, data I/O, log write, and memory baselines. On Azure SQL Managed Instance, `sys.server_resource_stats` exposes built-in 15-second instance telemetry history (complementing `sys.dm_db_resource_stats` on single Azure SQL Databases). `sys.dm_db_resource_stats` retains 14 days of 15-second resource averages (`avg_cpu_percent`, `avg_data_io_percent`, `avg_log_write_percent`) to compare current peaks against normal baselines. Local study-map skill 3.1 (Establish Performance Baselines and Interpret CPU, Memory, Data I/O, Log Write, and `tempdb` Metrics), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL resource utilization and establish performance baselines (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-sql-database-azure-monitor).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: On Azure SQL Managed Instance, `sys.server_resource_stats` exposes built-in 15-second instance telemetry history (complementing `sys.dm_db_resource_stats` on single Azure SQL Databases).
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: On Azure SQL Managed Instance, `sys.server_resource_stats` exposes built-in 15-second instance telemetry history (complementing `sys.dm_db_resource_stats` on single Azure SQL Databases).
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: On Azure SQL Managed Instance, `sys.server_resource_stats` exposes built-in 15-second instance telemetry history (complementing `sys.dm_db_resource_stats` on single Azure SQL Databases).
- **D:** Correct. `sys.dm_db_resource_stats` retains 14 days of 15-second resource averages (`avg_cpu_percent`, `avg_data_io_percent`, `avg_log_write_percent`) to compare current peaks against normal baselines. In this scenario: On Azure SQL Managed Instance, `sys.server_resource_stats` exposes built-in 15-second instance telemetry history (complementing `sys.dm_db_resource_stats` on single Azure SQL Databases).

### Question 37 — A

Answer: Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`. High `WRITELOG` waits occur when sessions wait for the transaction log buffer flush to harden on storage—caused by chatty tiny row-by-row autocommit loops or insufficient log IOPS/throughput tier limits. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. Local study-map skill 3.1 (Establish Performance Baselines and Interpret CPU, Memory, Data I/O, Log Write, and `tempdb` Metrics), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL resource utilization and establish performance baselines (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-sql-database-azure-monitor).

- **A:** Correct. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. In this scenario: High `WRITELOG` waits occur when sessions wait for the transaction log buffer flush to harden on storage—caused by chatty tiny row-by-row autocommit loops or insufficient log IOPS/throughput tier limits.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: High `WRITELOG` waits occur when sessions wait for the transaction log buffer flush to harden on storage—caused by chatty tiny row-by-row autocommit loops or insufficient log IOPS/throughput tier limits.
- **C:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: High `WRITELOG` waits occur when sessions wait for the transaction log buffer flush to harden on storage—caused by chatty tiny row-by-row autocommit loops or insufficient log IOPS/throughput tier limits.
- **D:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: High `WRITELOG` waits occur when sessions wait for the transaction log buffer flush to harden on storage—caused by chatty tiny row-by-row autocommit loops or insufficient log IOPS/throughput tier limits.

### Question 38 — C

Answer: Azure Monitor Diagnostic Settings streaming `SQLInsights`, `QueryStoreRuntimeStatistics`, `Errors`, and `Blocks` to a Log Analytics workspace (`KQL`). Streaming `Deadlocks`, `QueryStoreRuntimeStatistics`, `QueryStoreWaitStatistics`, and `SQLInsights` to Log Analytics centralizes estate-wide KQL performance diagnostics and alerting. Diagnostic Settings export telemetry across hundreds of databases into Log Analytics so DBAs can correlate `SQLInsights`, wait stats, deadlocks, and timeouts via KQL queries and alerts. Local study-map skill 3.2 (Configure Azure Monitor Diagnostic Settings (`SQLInsights`, `AzureDiagnostics` KQL) and Resource Monitoring), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Azure Monitor diagnostic settings, SQLInsights logs, and metric alerts (https://learn.microsoft.com/en-us/azure/azure-sql/database/metrics-diagnostic-telemetry-logging-streaming-export-configure).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Streaming `Deadlocks`, `QueryStoreRuntimeStatistics`, `QueryStoreWaitStatistics`, and `SQLInsights` to Log Analytics centralizes estate-wide KQL performance diagnostics and alerting.
- **B:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Streaming `Deadlocks`, `QueryStoreRuntimeStatistics`, `QueryStoreWaitStatistics`, and `SQLInsights` to Log Analytics centralizes estate-wide KQL performance diagnostics and alerting.
- **C:** Correct. Diagnostic Settings export telemetry across hundreds of databases into Log Analytics so DBAs can correlate `SQLInsights`, wait stats, deadlocks, and timeouts via KQL queries and alerts. In this scenario: Streaming `Deadlocks`, `QueryStoreRuntimeStatistics`, `QueryStoreWaitStatistics`, and `SQLInsights` to Log Analytics centralizes estate-wide KQL performance diagnostics and alerting.
- **D:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Streaming `Deadlocks`, `QueryStoreRuntimeStatistics`, `QueryStoreWaitStatistics`, and `SQLInsights` to Log Analytics centralizes estate-wide KQL performance diagnostics and alerting.

### Question 39 — B

Answer: Provision Azure Data Explorer or Fabric Eventhouse store → Create database watcher with Managed Identity → Add SQL targets & grant `VIEW SERVER PERFORMANCE STATE` + ingest roles → Start watcher & open portal dashboards. Provision the Fabric Eventhouse / ADX store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets plus store ingest rights, and start the watcher. Database watcher streams SQL telemetry into an Azure Data Explorer or Fabric Eventhouse/KQL store using Managed Identity granted least-privilege `VIEW SERVER PERFORMANCE STATE` on SQL targets. Local study-map skill 3.3 (Monitor Workloads Using Database Watcher (ADX / Fabric Eventhouse) and Plan Fabric Database Hub Transition), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL workloads with database watcher and Database Hub in Microsoft Fabric (https://learn.microsoft.com/en-us/azure/azure-sql/database-watcher-overview).

- **A:** Incorrect for this requirement. Incorrect workflow: watcher requires an Azure Data Explorer or Fabric Real-Time Analytics store and SQL targets configured first, and uses least-privilege Managed Identity rather than `sa` or Profiler. Why the keyed choice wins: Provision the Fabric Eventhouse / ADX store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets plus store ingest rights, and start the watcher.
- **B:** Correct. Database watcher streams SQL telemetry into an Azure Data Explorer or Fabric Eventhouse/KQL store using Managed Identity granted least-privilege `VIEW SERVER PERFORMANCE STATE` on SQL targets. In this scenario: Provision the Fabric Eventhouse / ADX store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets plus store ingest rights, and start the watcher.
- **C:** Incorrect for this requirement. Incorrect workflow: database watcher monitors Azure SQL Database, Elastic Pools, and SQL Managed Instance and stores telemetry in Azure Data Explorer or Fabric KQL databases. Why the keyed choice wins: Provision the Fabric Eventhouse / ADX store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets plus store ingest rights, and start the watcher.
- **D:** Incorrect for this requirement. Incorrect workflow: Azure SQL Database PaaS exposes no underlying OS for agents, `sp_trace_create` is deprecated, and database watcher is agentless. Why the keyed choice wins: Provision the Fabric Eventhouse / ADX store first, create the database watcher with Managed Identity, grant `VIEW SERVER PERFORMANCE STATE` on SQL targets plus store ingest rights, and start the watcher.

### Question 40 — B

Answer: Extended Events (`CREATE EVENT SESSION ... ON DATABASE` in SQL DB or `ON SERVER` in SQL MI/VMs) writing to an `event_file` target in Azure Blob Storage. The in-memory `ring_buffer` target caps memory (`<= 4 MB`), wraps/evicts older events, and vanishes on failover, whereas `event_file` writes durable `.xel` files to Azure Blob Storage. Unlike ephemeral in-memory `ring_buffer` targets, the `event_file` target persists `.xel` trace files durably in Azure Blob Storage using a database-scoped credential (Managed Identity or SAS). Local study-map skill 3.4 (Monitor Workloads Using Extended Events (`ON DATABASE` vs `ON SERVER` & Persistent Blob `event_file` Targets)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Extended Events in Azure SQL Database and Azure SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/xevent-db-diff-from-svr).

- **A:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: The in-memory `ring_buffer` target caps memory (`<= 4 MB`), wraps/evicts older events, and vanishes on failover, whereas `event_file` writes durable `.xel` files to Azure Blob Storage.
- **B:** Correct. Unlike ephemeral in-memory `ring_buffer` targets, the `event_file` target persists `.xel` trace files durably in Azure Blob Storage using a database-scoped credential (Managed Identity or SAS). In this scenario: The in-memory `ring_buffer` target caps memory (`<= 4 MB`), wraps/evicts older events, and vanishes on failover, whereas `event_file` writes durable `.xel` files to Azure Blob Storage.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: The in-memory `ring_buffer` target caps memory (`<= 4 MB`), wraps/evicts older events, and vanishes on failover, whereas `event_file` writes durable `.xel` files to Azure Blob Storage.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: The in-memory `ring_buffer` target caps memory (`<= 4 MB`), wraps/evicts older events, and vanishes on failover, whereas `event_file` writes durable `.xel` files to Azure Blob Storage.

### Question 41 — C, D

Answers: Execute `sys.sp_query_store_force_plan @query_id, @plan_id` to pin the historical low-latency execution plan immediately; Execute `sys.sp_query_store_set_hints @query_id, N'OPTION (RECOMPILE)'` (or `MAXDOP` / memory grant hints) without redeploying code. `sys.sp_query_store_force_plan` forces a specific historical `plan_id`, and `sys.sp_query_store_set_hints` applies `OPTION (...)` query hints directly to the `query_id` without editing vendor code. Local study-map skill 3.5 (Configure and Monitor Query Store, Force Regressed Plans (`sp_query_store_force_plan`), and Set Query Store Hints), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance by using the Query Store, plan forcing, and Query Store hints (https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `sys.sp_query_store_force_plan` forces a specific historical `plan_id`, and `sys.sp_query_store_set_hints` applies `OPTION (...)` query hints directly to the `query_id` without editing vendor code.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: `sys.sp_query_store_force_plan` forces a specific historical `plan_id`, and `sys.sp_query_store_set_hints` applies `OPTION (...)` query hints directly to the `query_id` without editing vendor code.
- **C:** Correct. Query Store hints attach `OPTION (...)` query hints directly to a `query_id` in Azure SQL DB, SQL MI, and SQL Server 2022+ when app code cannot be edited. In this scenario: `sys.sp_query_store_force_plan` forces a specific historical `plan_id`, and `sys.sp_query_store_set_hints` applies `OPTION (...)` query hints directly to the `query_id` without editing vendor code.
- **D:** Correct. `sp_query_store_force_plan` instructs the optimizer to compile plans matching the forced `plan_id` shape without modifying application T-SQL. In this scenario: `sys.sp_query_store_force_plan` forces a specific historical `plan_id`, and `sys.sp_query_store_set_hints` applies `OPTION (...)` query hints directly to the `query_id` without editing vendor code.
- **E:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: `sys.sp_query_store_force_plan` forces a specific historical `plan_id`, and `sys.sp_query_store_set_hints` applies `OPTION (...)` query hints directly to the `query_id` without editing vendor code.

### Question 42 — B

Answer: Confirm Query Store is `READ_WRITE` with wait capture → Compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`) → Force prior plan via `sp_query_store_force_plan` → Monitor `force_failure_count` & latency. Confirm Query Store is `READ_WRITE` with wait capture, compare plan metrics in Regressed Queries (`sys.query_store_runtime_stats`), force `plan_id = 12` via `sp_query_store_force_plan`, and monitor `force_failure_count`. Resolving a parameter-sensitive plan regression uses Query Store runtime/wait history to identify the prior known-good `plan_id`, forces it immediately without code changes, and verifies forcing health. Local study-map skill 3.5 (Configure and Monitor Query Store, Force Regressed Plans (`sp_query_store_force_plan`), and Set Query Store Hints), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance by using the Query Store, plan forcing, and Query Store hints (https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store).

- **A:** Incorrect for this requirement. Incorrect workflow: restarting SQL or running offline index rebuilds causes severe production outage and does not prevent parameter-sensitive plan regressions. Why the keyed choice wins: Confirm Query Store is `READ_WRITE` with wait capture, compare plan metrics in Regressed Queries (`sys.query_store_runtime_stats`), force `plan_id = 12` via `sp_query_store_force_plan`, and monitor `force_failure_count`.
- **B:** Correct. Resolving a parameter-sensitive plan regression uses Query Store runtime/wait history to identify the prior known-good `plan_id`, forces it immediately without code changes, and verifies forcing health. In this scenario: Confirm Query Store is `READ_WRITE` with wait capture, compare plan metrics in Regressed Queries (`sys.query_store_runtime_stats`), force `plan_id = 12` via `sp_query_store_force_plan`, and monitor `force_failure_count`.
- **C:** Incorrect for this requirement. Incorrect workflow: system catalog tables cannot be updated directly and flushing the plan cache every minute spikes CPU compilations across the entire workload. Why the keyed choice wins: Confirm Query Store is `READ_WRITE` with wait capture, compare plan metrics in Regressed Queries (`sys.query_store_runtime_stats`), force `plan_id = 12` via `sp_query_store_force_plan`, and monitor `force_failure_count`.
- **D:** Incorrect for this requirement. Incorrect workflow: purging Query Store erases the historical baseline and prior good plan needed to diagnose and force the healthy execution plan. Why the keyed choice wins: Confirm Query Store is `READ_WRITE` with wait capture, compare plan metrics in Regressed Queries (`sys.query_store_runtime_stats`), force `plan_id = 12` via `sp_query_store_force_plan`, and monitor `force_failure_count`.

### Question 43 — C

Answer: Read Committed Snapshot Isolation (`READ_COMMITTED_SNAPSHOT = ON`) combined with Optimized Locking (`TID` locking + Lock After Qualification `LAQ`). Enabling `READ_COMMITTED_SNAPSHOT` (`RCSI`, which is on by default in Azure SQL Database and configurable on SQL Server/MI) serves transactionally consistent row versions without shared `LCK_M_S` reader locks. `RCSI` uses row versioning so readers never block writers (`LCK_M_S`), while Optimized Locking in Azure SQL DB replaces thousands of row/page locks with a single Transaction ID lock and `LAQ`. Local study-map skill 3.6 (Identify and Resolve Session Blocking (`RCSI`, `Optimized Locking` `TID`/`LAQ`) and Deadlocks (`xml_deadlock_report`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Understand and resolve Azure SQL blocking problems, deadlocks, RCSI, and Optimized Locking (https://learn.microsoft.com/en-us/azure/azure-sql/database/analyze-prevent-deadlocks).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Enabling `READ_COMMITTED_SNAPSHOT` (`RCSI`, which is on by default in Azure SQL Database and configurable on SQL Server/MI) serves transactionally consistent row versions without shared `LCK_M_S` reader locks.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Enabling `READ_COMMITTED_SNAPSHOT` (`RCSI`, which is on by default in Azure SQL Database and configurable on SQL Server/MI) serves transactionally consistent row versions without shared `LCK_M_S` reader locks.
- **C:** Correct. `RCSI` uses row versioning so readers never block writers (`LCK_M_S`), while Optimized Locking in Azure SQL DB replaces thousands of row/page locks with a single Transaction ID lock and `LAQ`. In this scenario: Enabling `READ_COMMITTED_SNAPSHOT` (`RCSI`, which is on by default in Azure SQL Database and configurable on SQL Server/MI) serves transactionally consistent row versions without shared `LCK_M_S` reader locks.
- **D:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Enabling `READ_COMMITTED_SNAPSHOT` (`RCSI`, which is on by default in Azure SQL Database and configurable on SQL Server/MI) serves transactionally consistent row versions without shared `LCK_M_S` reader locks.

### Question 44 — A

Answer: Capture `xml_deadlock_report` via Extended Events or `sys.event_log`, align table modification order across transactions, and add covering indexes. Read the `xml_deadlock_report` events from the built-in `system_health` Extended Events session (or `database_xml_deadlock_report` in `sys.event_log` on Azure SQL Database), then align lock acquisition order. Cycle deadlocks (`Error 1205`) occur when concurrent transactions lock objects in opposite order or scan wide ranges; accessing tables in identical order with narrow index seeks eliminates cycles. Local study-map skill 3.6 (Identify and Resolve Session Blocking (`RCSI`, `Optimized Locking` `TID`/`LAQ`) and Deadlocks (`xml_deadlock_report`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Understand and resolve Azure SQL blocking problems, deadlocks, RCSI, and Optimized Locking (https://learn.microsoft.com/en-us/azure/azure-sql/database/analyze-prevent-deadlocks).

- **A:** Correct. Cycle deadlocks (`Error 1205`) occur when concurrent transactions lock objects in opposite order or scan wide ranges; accessing tables in identical order with narrow index seeks eliminates cycles. In this scenario: Read the `xml_deadlock_report` events from the built-in `system_health` Extended Events session (or `database_xml_deadlock_report` in `sys.event_log` on Azure SQL Database), then align lock acquisition order.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Read the `xml_deadlock_report` events from the built-in `system_health` Extended Events session (or `database_xml_deadlock_report` in `sys.event_log` on Azure SQL Database), then align lock acquisition order.
- **C:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Read the `xml_deadlock_report` events from the built-in `system_health` Extended Events session (or `database_xml_deadlock_report` in `sys.event_log` on Azure SQL Database), then align lock acquisition order.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Read the `xml_deadlock_report` events from the built-in `system_health` Extended Events session (or `database_xml_deadlock_report` in `sys.event_log` on Azure SQL Database), then align lock acquisition order.

### Question 45 — B, D

Answers: Grant the database watcher Managed Identity `VIEW SERVER PERFORMANCE STATE` (or `VIEW DATABASE PERFORMANCE STATE`) on SQL targets; Grant the database watcher Managed Identity database `Admin` / ingest permissions on the Azure Data Explorer or Fabric Eventhouse store. Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on the SQL Managed Instances, and grant database `Admin` / ingestion permissions on the Azure Data Explorer database. Local study-map skill 3.7 (Identify Performance Bottlenecks Using Dynamic Management Views (`sys.dm_os_wait_stats`, `sys.dm_exec_requests`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance using Dynamic Management Views (DMVs) and wait statistics (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-with-dmvs).

- **A:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on the SQL Managed Instances, and grant database `Admin` / ingestion permissions on the Azure Data Explorer database.
- **B:** Correct. Database watcher collects DMVs and system catalogs using least-privilege performance-state permissions rather than `sysadmin` or data-read rights. In this scenario: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on the SQL Managed Instances, and grant database `Admin` / ingestion permissions on the Azure Data Explorer database.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on the SQL Managed Instances, and grant database `Admin` / ingestion permissions on the Azure Data Explorer database.
- **D:** Correct. Database watcher creates tables, retention policies, and ingestion mappings inside the target Azure Data Explorer or Fabric Real-Time Analytics KQL database. In this scenario: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on the SQL Managed Instances, and grant database `Admin` / ingestion permissions on the Azure Data Explorer database.
- **E:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Grant `VIEW SERVER PERFORMANCE STATE` to the watcher Managed Identity on the SQL Managed Instances, and grant database `Admin` / ingestion permissions on the Azure Data Explorer database.

### Question 46 — C

Answer: Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`. `sys.dm_exec_query_stats` aggregates `total_worker_time` (CPU microseconds), `total_logical_reads`, and `execution_count` per cached query hash, joinable to `sys.dm_exec_sql_text(sql_handle)`. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. Local study-map skill 3.7 (Identify Performance Bottlenecks Using Dynamic Management Views (`sys.dm_os_wait_stats`, `sys.dm_exec_requests`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor performance using Dynamic Management Views (DMVs) and wait statistics (https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-with-dmvs).

- **A:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: `sys.dm_exec_query_stats` aggregates `total_worker_time` (CPU microseconds), `total_logical_reads`, and `execution_count` per cached query hash, joinable to `sys.dm_exec_sql_text(sql_handle)`.
- **B:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: `sys.dm_exec_query_stats` aggregates `total_worker_time` (CPU microseconds), `total_logical_reads`, and `execution_count` per cached query hash, joinable to `sys.dm_exec_sql_text(sql_handle)`.
- **C:** Correct. Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking. In this scenario: `sys.dm_exec_query_stats` aggregates `total_worker_time` (CPU microseconds), `total_logical_reads`, and `execution_count` per cached query hash, joinable to `sys.dm_exec_sql_text(sql_handle)`.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `sys.dm_exec_query_stats` aggregates `total_worker_time` (CPU microseconds), `total_logical_reads`, and `execution_count` per cached query hash, joinable to `sys.dm_exec_sql_text(sql_handle)`.

### Question 47 — A

Answer: Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions. A Clustered Columnstore Index (`CREATE CLUSTERED COLUMNSTORE INDEX`) stores columns in compressed rowgroups with segment elimination and batch-mode vector execution ideal for analytical aggregations. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. Local study-map skill 3.8 (Design Covering/Filtered/Columnstore Indexes and Rewrite Non-SARGable or Implicit-Conversion T-SQL Constructs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server and Azure SQL index design guide and SARGable T-SQL tuning (https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide).

- **A:** Correct. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. In this scenario: A Clustered Columnstore Index (`CREATE CLUSTERED COLUMNSTORE INDEX`) stores columns in compressed rowgroups with segment elimination and batch-mode vector execution ideal for analytical aggregations.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: A Clustered Columnstore Index (`CREATE CLUSTERED COLUMNSTORE INDEX`) stores columns in compressed rowgroups with segment elimination and batch-mode vector execution ideal for analytical aggregations.
- **C:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: A Clustered Columnstore Index (`CREATE CLUSTERED COLUMNSTORE INDEX`) stores columns in compressed rowgroups with segment elimination and batch-mode vector execution ideal for analytical aggregations.
- **D:** Incorrect for this requirement. Row-by-row cursors and multi-statement TVFs under legacy compatibility levels execute thousands of iterative context switches and 1-row cardinality guesses. Why the keyed choice wins: A Clustered Columnstore Index (`CREATE CLUSTERED COLUMNSTORE INDEX`) stores columns in compressed rowgroups with segment elimination and batch-mode vector execution ideal for analytical aggregations.

### Question 48 — D

Answer: Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`). Because `NVARCHAR` has higher data-type precedence than `VARCHAR`, SQL converts every table row's `NationalId` column to `NVARCHAR` at runtime, rendering the `VARCHAR` B-tree index non-SARGable. Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. Local study-map skill 3.9 (Analyze Execution Plans (`Key Lookup`, `TempDB` Spills, Row Skew) and Monitor via SQL Intelligent Insights), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Execution plans and SQL Intelligent Insights automated performance diagnostics (https://learn.microsoft.com/en-us/azure/azure-sql/database/intelligent-insights-overview).

- **A:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Because `NVARCHAR` has higher data-type precedence than `VARCHAR`, SQL converts every table row's `NationalId` column to `NVARCHAR` at runtime, rendering the `VARCHAR` B-tree index non-SARGable.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Because `NVARCHAR` has higher data-type precedence than `VARCHAR`, SQL converts every table row's `NationalId` column to `NVARCHAR` at runtime, rendering the `VARCHAR` B-tree index non-SARGable.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Because `NVARCHAR` has higher data-type precedence than `VARCHAR`, SQL converts every table row's `NationalId` column to `NVARCHAR` at runtime, rendering the `VARCHAR` B-tree index non-SARGable.
- **D:** Correct. Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions. In this scenario: Because `NVARCHAR` has higher data-type precedence than `VARCHAR`, SQL converts every table row's `NationalId` column to `NVARCHAR` at runtime, rendering the `VARCHAR` B-tree index non-SARGable.

### Question 49 — C

Answer: Query Store (`OPERATION_MODE = READ_WRITE`, `QUERY_CAPTURE_MODE = AUTO`) using `sp_query_store_force_plan` and `sp_query_store_set_hints`. When an index referenced inside a forced plan is renamed or removed, Query Store logs `NO_PLAN` in `last_force_failure_reason_desc` and gracefully falls back to compiling a fresh non-forced plan so user queries still succeed. Query Store persists plan and runtime/wait telemetry across restarts, allowing DBAs to force a known-good `plan_id` or inject `OPTION (RECOMPILE)` / `MAXDOP` hints without altering app code. Local study-map skill 3.9 (Analyze Execution Plans (`Key Lookup`, `TempDB` Spills, Row Skew) and Monitor via SQL Intelligent Insights), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Execution plans and SQL Intelligent Insights automated performance diagnostics (https://learn.microsoft.com/en-us/azure/azure-sql/database/intelligent-insights-overview).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: When an index referenced inside a forced plan is renamed or removed, Query Store logs `NO_PLAN` in `last_force_failure_reason_desc` and gracefully falls back to compiling a fresh non-forced plan so user queries still succeed.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: When an index referenced inside a forced plan is renamed or removed, Query Store logs `NO_PLAN` in `last_force_failure_reason_desc` and gracefully falls back to compiling a fresh non-forced plan so user queries still succeed.
- **C:** Correct. Query Store persists plan and runtime/wait telemetry across restarts, allowing DBAs to force a known-good `plan_id` or inject `OPTION (RECOMPILE)` / `MAXDOP` hints without altering app code. In this scenario: When an index referenced inside a forced plan is renamed or removed, Query Store logs `NO_PLAN` in `last_force_failure_reason_desc` and gracefully falls back to compiling a fresh non-forced plan so user queries still succeed.
- **D:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: When an index referenced inside a forced plan is renamed or removed, Query Store logs `NO_PLAN` in `last_force_failure_reason_desc` and gracefully falls back to compiling a fresh non-forced plan so user queries still succeed.

### Question 50 — A

Answer: Fragmentation-aware index maintenance (`REORGANIZE` 5–30%, `REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` >30%), `UPDATE STATISTICS`, and `DBCC CHECKDB WITH PHYSICAL_ONLY`. Use lightweight online leaf-level `ALTER INDEX ... REORGANIZE` for moderate fragmentation (`5%–30%`) and `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` for heavy fragmentation (`>30%`). `RESUMABLE = ON` lets large online index rebuilds pause and resume across maintenance windows; `AUTO_UPDATE_STATISTICS_ASYNC` avoids compile stalls; `PHYSICAL_ONLY` reduces `CHECKDB` I/O overhead. Local study-map skill 3.10 (Implement Fragmentation-Aware Index Rebuilds (`ONLINE`, `RESUMABLE`), Async Statistics, and `DBCC CHECKDB`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Optimize index maintenance, statistics updates, and DBCC CHECKDB integrity checks (https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes).

- **A:** Correct. `RESUMABLE = ON` lets large online index rebuilds pause and resume across maintenance windows; `AUTO_UPDATE_STATISTICS_ASYNC` avoids compile stalls; `PHYSICAL_ONLY` reduces `CHECKDB` I/O overhead. In this scenario: Use lightweight online leaf-level `ALTER INDEX ... REORGANIZE` for moderate fragmentation (`5%–30%`) and `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` for heavy fragmentation (`>30%`).
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Use lightweight online leaf-level `ALTER INDEX ... REORGANIZE` for moderate fragmentation (`5%–30%`) and `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` for heavy fragmentation (`>30%`).
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Use lightweight online leaf-level `ALTER INDEX ... REORGANIZE` for moderate fragmentation (`5%–30%`) and `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` for heavy fragmentation (`>30%`).
- **D:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Use lightweight online leaf-level `ALTER INDEX ... REORGANIZE` for moderate fragmentation (`5%–30%`) and `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` for heavy fragmentation (`>30%`).

### Question 51 — C

Answer: Fragmentation-aware index maintenance (`REORGANIZE` 5–30%, `REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` >30%), `UPDATE STATISTICS`, and `DBCC CHECKDB WITH PHYSICAL_ONLY`. Run lightweight `DBCC CHECKDB WITH PHYSICAL_ONLY` on production to validate page checksums/headers rapidly, and restore nightly backups onto a separate staging server to run full logical `DBCC CHECKDB`. `RESUMABLE = ON` lets large online index rebuilds pause and resume across maintenance windows; `AUTO_UPDATE_STATISTICS_ASYNC` avoids compile stalls; `PHYSICAL_ONLY` reduces `CHECKDB` I/O overhead. Local study-map skill 3.10 (Implement Fragmentation-Aware Index Rebuilds (`ONLINE`, `RESUMABLE`), Async Statistics, and `DBCC CHECKDB`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Optimize index maintenance, statistics updates, and DBCC CHECKDB integrity checks (https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Run lightweight `DBCC CHECKDB WITH PHYSICAL_ONLY` on production to validate page checksums/headers rapidly, and restore nightly backups onto a separate staging server to run full logical `DBCC CHECKDB`.
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Run lightweight `DBCC CHECKDB WITH PHYSICAL_ONLY` on production to validate page checksums/headers rapidly, and restore nightly backups onto a separate staging server to run full logical `DBCC CHECKDB`.
- **C:** Correct. `RESUMABLE = ON` lets large online index rebuilds pause and resume across maintenance windows; `AUTO_UPDATE_STATISTICS_ASYNC` avoids compile stalls; `PHYSICAL_ONLY` reduces `CHECKDB` I/O overhead. In this scenario: Run lightweight `DBCC CHECKDB WITH PHYSICAL_ONLY` on production to validate page checksums/headers rapidly, and restore nightly backups onto a separate staging server to run full logical `DBCC CHECKDB`.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Run lightweight `DBCC CHECKDB WITH PHYSICAL_ONLY` on production to validate page checksums/headers rapidly, and restore nightly backups onto a separate staging server to run full logical `DBCC CHECKDB`.

### Question 52 — D

Answer: Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`). Automatic Tuning monitors the forced plan continuously; if underlying schema changes or data distribution shifts make the forced plan underperform, or when a recompile threshold occurs, Azure automatically unforces it to let the optimizer find a better plan. Automatic Tuning continuously monitors Query Store, automatically forces prior plans when regressions occur, creates validated missing nonclustered indexes, and removes unused duplicate indexes. Local study-map skill 3.11 (Configure Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN`, `CREATE_INDEX`, `DROP_INDEX`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automatic tuning in Azure SQL Database and Azure SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-overview).

- **A:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Automatic Tuning monitors the forced plan continuously; if underlying schema changes or data distribution shifts make the forced plan underperform, or when a recompile threshold occurs, Azure automatically unforces it to let the optimizer find a better plan.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Automatic Tuning monitors the forced plan continuously; if underlying schema changes or data distribution shifts make the forced plan underperform, or when a recompile threshold occurs, Azure automatically unforces it to let the optimizer find a better plan.
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Automatic Tuning monitors the forced plan continuously; if underlying schema changes or data distribution shifts make the forced plan underperform, or when a recompile threshold occurs, Azure automatically unforces it to let the optimizer find a better plan.
- **D:** Correct. Automatic Tuning continuously monitors Query Store, automatically forces prior plans when regressions occur, creates validated missing nonclustered indexes, and removes unused duplicate indexes. In this scenario: Automatic Tuning monitors the forced plan continuously; if underlying schema changes or data distribution shifts make the forced plan underperform, or when a recompile threshold occurs, Azure automatically unforces it to let the optimizer find a better plan.

### Question 53 — D

Answer: Use `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`, `OPTIMIZED_PLAN_FORCING`) per database. Setting `LEGACY_CARDINALITY_ESTIMATION = ON` at the database scope (or via a `USE HINT('FORCE_LEGACY_CARDINALITY_ESTIMATION')` Query Store hint for just those two queries) retains compatibility level `160` without downgrading the database. Database-scoped configurations isolate optimizer settings (`MAXDOP`, CE version, parameter sniffing) to a single database without affecting sibling databases on SQL MI/VMs or requiring server access. Local study-map skill 3.13 (Implement `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: ALTER DATABASE SCOPED CONFIGURATION and dynamic compute/storage scaling (https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql).

- **A:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Setting `LEGACY_CARDINALITY_ESTIMATION = ON` at the database scope (or via a `USE HINT('FORCE_LEGACY_CARDINALITY_ESTIMATION')` Query Store hint for just those two queries) retains compatibility level `160` without downgrading the database.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Setting `LEGACY_CARDINALITY_ESTIMATION = ON` at the database scope (or via a `USE HINT('FORCE_LEGACY_CARDINALITY_ESTIMATION')` Query Store hint for just those two queries) retains compatibility level `160` without downgrading the database.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Setting `LEGACY_CARDINALITY_ESTIMATION = ON` at the database scope (or via a `USE HINT('FORCE_LEGACY_CARDINALITY_ESTIMATION')` Query Store hint for just those two queries) retains compatibility level `160` without downgrading the database.
- **D:** Correct. Database-scoped configurations isolate optimizer settings (`MAXDOP`, CE version, parameter sniffing) to a single database without affecting sibling databases on SQL MI/VMs or requiring server access. In this scenario: Setting `LEGACY_CARDINALITY_ESTIMATION = ON` at the database scope (or via a `USE HINT('FORCE_LEGACY_CARDINALITY_ESTIMATION')` Query Store hint for just those two queries) retains compatibility level `160` without downgrading the database.

### Question 54 — A, B, C

Answers: Leverage Parameter Sensitive Plan (`PSP`) optimization under compatibility level `160` to cache separate plans for skewed parameter sizes; Leverage Percentile and Persistence Memory Grant Feedback (`compat 160`) to eliminate recurring `tempdb` sort/hash spills and wasted RAM; Leverage Scalar UDF Inlining (`compat 150+`) so eligible T-SQL scalar functions fold into relational subqueries enabling parallel plans. Compatibility level `160` activates Parameter Sensitive Plan (`PSP`) optimization, Percentile & Persistence Memory Grant Feedback, and Scalar UDF Inlining (introduced in `150` and enhanced in `160`). Local study-map skill 3.14 (Identify Use Cases for Intelligent Query Processing (`PSP` Optimization, Memory Grant Feedback, Scalar UDF Inlining)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Intelligent Query Processing (IQP) features in SQL databases (https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing).

- **A:** Correct. Scalar UDF Inlining transforms row-by-row T-SQL scalar function invocations into set-based relational operators that no longer block parallelism. In this scenario: Compatibility level `160` activates Parameter Sensitive Plan (`PSP`) optimization, Percentile & Persistence Memory Grant Feedback, and Scalar UDF Inlining (introduced in `150` and enhanced in `160`).
- **B:** Correct. PSP optimization generates up to three active dispatcher query variants so small lookups use Index Seeks while massive skews use Parallel Scans. In this scenario: Compatibility level `160` activates Parameter Sensitive Plan (`PSP`) optimization, Percentile & Persistence Memory Grant Feedback, and Scalar UDF Inlining (introduced in `150` and enhanced in `160`).
- **C:** Correct. Memory Grant Feedback adjusts overestimated or underestimated query memory grants across executions and persists learned grants in Query Store. In this scenario: Compatibility level `160` activates Parameter Sensitive Plan (`PSP`) optimization, Percentile & Persistence Memory Grant Feedback, and Scalar UDF Inlining (introduced in `150` and enhanced in `160`).
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Compatibility level `160` activates Parameter Sensitive Plan (`PSP`) optimization, Percentile & Persistence Memory Grant Feedback, and Scalar UDF Inlining (introduced in `150` and enhanced in `160`).
- **E:** Incorrect for this requirement. Row-by-row cursors and multi-statement TVFs under legacy compatibility levels execute thousands of iterative context switches and 1-row cardinality guesses. Why the keyed choice wins: Compatibility level `160` activates Parameter Sensitive Plan (`PSP`) optimization, Percentile & Persistence Memory Grant Feedback, and Scalar UDF Inlining (introduced in `150` and enhanced in `160`).
- **F:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Compatibility level `160` activates Parameter Sensitive Plan (`PSP`) optimization, Percentile & Persistence Memory Grant Feedback, and Scalar UDF Inlining (introduced in `150` and enhanced in `160`).

### Question 55 — A

Answer: SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators. Set Step 1's `On success action` to `Quit the job reporting success` and `On failure action` to `Go to step: [Step 2 — Cleanup & Alert]`. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. Local study-map skill 4.1 (Create and Schedule SQL Server Agent Maintenance Jobs, Proxies, Severity `19–25` Alerts, and Database Mail), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server Agent jobs, schedules, alerts, and Database Mail operators (https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent).

- **A:** Correct. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. In this scenario: Set Step 1's `On success action` to `Quit the job reporting success` and `On failure action` to `Go to step: [Step 2 — Cleanup & Alert]`.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Set Step 1's `On success action` to `Quit the job reporting success` and `On failure action` to `Go to step: [Step 2 — Cleanup & Alert]`.
- **C:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: Set Step 1's `On success action` to `Quit the job reporting success` and `On failure action` to `Go to step: [Step 2 — Cleanup & Alert]`.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Set Step 1's `On success action` to `Quit the job reporting success` and `On failure action` to `Go to step: [Step 2 — Cleanup & Alert]`.

### Question 56 — C

Answer: SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators. A `SQL Server performance condition alert` monitoring `SQLServer:Databases | Percent Log Used | ClinicalDB | > | 80` triggers the response log-backup job and notifies the Operator automatically. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. Local study-map skill 4.1 (Create and Schedule SQL Server Agent Maintenance Jobs, Proxies, Severity `19–25` Alerts, and Database Mail), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server Agent jobs, schedules, alerts, and Database Mail operators (https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: A `SQL Server performance condition alert` monitoring `SQLServer:Databases | Percent Log Used | ClinicalDB | > | 80` triggers the response log-backup job and notifies the Operator automatically.
- **B:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: A `SQL Server performance condition alert` monitoring `SQLServer:Databases | Percent Log Used | ClinicalDB | > | 80` triggers the response log-backup job and notifies the Operator automatically.
- **C:** Correct. Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors. In this scenario: A `SQL Server performance condition alert` monitoring `SQLServer:Databases | Percent Log Used | ClinicalDB | > | 80` triggers the response log-backup job and notifies the Operator automatically.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: A `SQL Server performance condition alert` monitoring `SQLServer:Databases | Percent Log Used | ClinicalDB | > | 80` triggers the response log-backup job and notifies the Operator automatically.

### Question 57 — C, D

Answers: Create a Windows/SQL Credential and map it to a SQL Server Agent Subsystem Proxy (`CmdExec` / `PowerShell`) instead of granting `sysadmin`; Configure Database Mail, define an Agent Operator, and create SQL Server Agent Alerts for Severity `19–25` and Errors `823`, `824`, and `825`. Bind least-privilege Credentials to SQL Server Agent Subsystem Proxies for non-`sysadmin` steps, and attach Database Mail Operators to Severity `19–25` and Error `823–825` Alerts. Local study-map skill 4.1 (Create and Schedule SQL Server Agent Maintenance Jobs, Proxies, Severity `19–25` Alerts, and Database Mail), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server Agent jobs, schedules, alerts, and Database Mail operators (https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent).

- **A:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Bind least-privilege Credentials to SQL Server Agent Subsystem Proxies for non-`sysadmin` steps, and attach Database Mail Operators to Severity `19–25` and Error `823–825` Alerts.
- **B:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Bind least-privilege Credentials to SQL Server Agent Subsystem Proxies for non-`sysadmin` steps, and attach Database Mail Operators to Severity `19–25` and Error `823–825` Alerts.
- **C:** Correct. Severity `19–25` and I/O errors `823–825` indicate critical resource exhaustion or storage corruption requiring immediate DBA notification. In this scenario: Bind least-privilege Credentials to SQL Server Agent Subsystem Proxies for non-`sysadmin` steps, and attach Database Mail Operators to Severity `19–25` and Error `823–825` Alerts.
- **D:** Correct. SQL Server Agent proxies let non-`sysadmin` job owners execute external subsystem steps under a scoped least-privilege identity. In this scenario: Bind least-privilege Credentials to SQL Server Agent Subsystem Proxies for non-`sysadmin` steps, and attach Database Mail Operators to Severity `19–25` and Error `823–825` Alerts.
- **E:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Bind least-privilege Credentials to SQL Server Agent Subsystem Proxies for non-`sysadmin` steps, and attach Database Mail Operators to Severity `19–25` and Error `823–825` Alerts.

### Question 58 — A

Answer: Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries. In `msdb` (`sp_grant_login_to_proxy` or SSMS Proxy Account Principals), grant the job owner's login or fixed `msdb` role (`SQLAgentUserRole`) permission to use that specific SQL Agent Proxy. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. Local study-map skill 4.2 (Troubleshoot SQL Server Agent Job Histories, Credential/Proxy Permissions, and SQL MI Subsystem Boundaries), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot SQL Server Agent jobs, proxies, and SQL Managed Instance Agent differences (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/transact-sql-tsql-differences-sql-server).

- **A:** Correct. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. In this scenario: In `msdb` (`sp_grant_login_to_proxy` or SSMS Proxy Account Principals), grant the job owner's login or fixed `msdb` role (`SQLAgentUserRole`) permission to use that specific SQL Agent Proxy.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: In `msdb` (`sp_grant_login_to_proxy` or SSMS Proxy Account Principals), grant the job owner's login or fixed `msdb` role (`SQLAgentUserRole`) permission to use that specific SQL Agent Proxy.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: In `msdb` (`sp_grant_login_to_proxy` or SSMS Proxy Account Principals), grant the job owner's login or fixed `msdb` role (`SQLAgentUserRole`) permission to use that specific SQL Agent Proxy.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: In `msdb` (`sp_grant_login_to_proxy` or SSMS Proxy Account Principals), grant the job owner's login or fixed `msdb` role (`SQLAgentUserRole`) permission to use that specific SQL Agent Proxy.

### Question 59 — B

Answer: Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries. Set the `SQLServerAgent` service startup type to `Automatic` (via SQL Server Configuration Manager or `Set-Service -StartupType Automatic`) and start the service so Agent resumes schedules after host reboots. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. Local study-map skill 4.2 (Troubleshoot SQL Server Agent Job Histories, Credential/Proxy Permissions, and SQL MI Subsystem Boundaries), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot SQL Server Agent jobs, proxies, and SQL Managed Instance Agent differences (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/transact-sql-tsql-differences-sql-server).

- **A:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: Set the `SQLServerAgent` service startup type to `Automatic` (via SQL Server Configuration Manager or `Set-Service -StartupType Automatic`) and start the service so Agent resumes schedules after host reboots.
- **B:** Correct. Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs. In this scenario: Set the `SQLServerAgent` service startup type to `Automatic` (via SQL Server Configuration Manager or `Set-Service -StartupType Automatic`) and start the service so Agent resumes schedules after host reboots.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Set the `SQLServerAgent` service startup type to `Automatic` (via SQL Server Configuration Manager or `Set-Service -StartupType Automatic`) and start the service so Agent resumes schedules after host reboots.
- **D:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Set the `SQLServerAgent` service startup type to `Automatic` (via SQL Server Configuration Manager or `Set-Service -StartupType Automatic`) and start the service so Agent resumes schedules after host reboots.

### Question 60 — B, E

Answers: Mark sensitive parameters with `@secure()` in Bicep and pass Key Vault secret references from the parameter file rather than cleartext values; Run `az deployment group what-if` (or `New-AzResourceGroupDeployment -WhatIf`) as a pull-request gate before applying template changes. Decorate sensitive Bicep parameters with `@secure()` backed by Azure Key Vault secret references, and gate deployments with `az deployment group what-if`. Local study-map skill 4.3 (Automate Idempotent Deployment Using Bicep and ARM Templates with `@secure()` Key Vault References & `what-if`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Deploy Azure SQL resources using Bicep and Azure Resource Manager (ARM) templates (https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-Quickstart-bicep).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Decorate sensitive Bicep parameters with `@secure()` backed by Azure Key Vault secret references, and gate deployments with `az deployment group what-if`.
- **B:** Correct. `@secure()` prevents secret logging in deployment history, while Key Vault references resolve secrets inside ARM at deploy time without exposing them to CI runners. In this scenario: Decorate sensitive Bicep parameters with `@secure()` backed by Azure Key Vault secret references, and gate deployments with `az deployment group what-if`.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Decorate sensitive Bicep parameters with `@secure()` backed by Azure Key Vault secret references, and gate deployments with `az deployment group what-if`.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Decorate sensitive Bicep parameters with `@secure()` backed by Azure Key Vault secret references, and gate deployments with `az deployment group what-if`.
- **E:** Correct. `what-if` calculates predicted `Create`, `Modify`, `Delete`, and `Ignore` operations against live Azure SQL resources to catch destructive config drift. In this scenario: Decorate sensitive Bicep parameters with `@secure()` backed by Azure Key Vault secret references, and gate deployments with `az deployment group what-if`.

### Question 61 — A

Answer: Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`. In `Incremental` mode, ARM idempotently creates or updates resources declared in the template while leaving existing sibling resources in the resource group untouched (unlike `Complete` mode, which deletes undeclared resources). Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. Local study-map skill 4.3 (Automate Idempotent Deployment Using Bicep and ARM Templates with `@secure()` Key Vault References & `what-if`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Deploy Azure SQL resources using Bicep and Azure Resource Manager (ARM) templates (https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-Quickstart-bicep).

- **A:** Correct. Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution. In this scenario: In `Incremental` mode, ARM idempotently creates or updates resources declared in the template while leaving existing sibling resources in the resource group untouched (unlike `Complete` mode, which deletes undeclared resources).
- **B:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: In `Incremental` mode, ARM idempotently creates or updates resources declared in the template while leaving existing sibling resources in the resource group untouched (unlike `Complete` mode, which deletes undeclared resources).
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: In `Incremental` mode, ARM idempotently creates or updates resources declared in the template while leaving existing sibling resources in the resource group untouched (unlike `Complete` mode, which deletes undeclared resources).
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: In `Incremental` mode, ARM idempotently creates or updates resources declared in the template while leaving existing sibling resources in the resource group untouched (unlike `Complete` mode, which deletes undeclared resources).

### Question 62 — A

Answer: Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`). `az sql mi create` provisions a new Azure SQL Managed Instance inside the specified delegated subnet URI with the requested vCore capacity and storage size. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. Local study-map skill 4.4 (Automate Azure SQL Provisioning and Day-2 Management Using Azure PowerShell (`Az.Sql`) and Azure CLI (`az sql`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL management using Azure PowerShell and Azure CLI (https://learn.microsoft.com/en-us/azure/azure-sql/database/scripts/create-and-configure-database-powershell).

- **A:** Correct. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. In this scenario: `az sql mi create` provisions a new Azure SQL Managed Instance inside the specified delegated subnet URI with the requested vCore capacity and storage size.
- **B:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: `az sql mi create` provisions a new Azure SQL Managed Instance inside the specified delegated subnet URI with the requested vCore capacity and storage size.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: `az sql mi create` provisions a new Azure SQL Managed Instance inside the specified delegated subnet URI with the requested vCore capacity and storage size.
- **D:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: `az sql mi create` provisions a new Azure SQL Managed Instance inside the specified delegated subnet URI with the requested vCore capacity and storage size.

### Question 63 — B

Answer: Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`). Running `Switch-AzSqlDatabaseInstanceFailoverGroup` against the secondary location promotes the secondary SQL Managed Instance cleanly without `-AllowDataLoss`. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. Local study-map skill 4.4 (Automate Azure SQL Provisioning and Day-2 Management Using Azure PowerShell (`Az.Sql`) and Azure CLI (`az sql`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL management using Azure PowerShell and Azure CLI (https://learn.microsoft.com/en-us/azure/azure-sql/database/scripts/create-and-configure-database-powershell).

- **A:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Running `Switch-AzSqlDatabaseInstanceFailoverGroup` against the secondary location promotes the secondary SQL Managed Instance cleanly without `-AllowDataLoss`.
- **B:** Correct. `Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts. In this scenario: Running `Switch-AzSqlDatabaseInstanceFailoverGroup` against the secondary location promotes the secondary SQL Managed Instance cleanly without `-AllowDataLoss`.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Running `Switch-AzSqlDatabaseInstanceFailoverGroup` against the secondary location promotes the secondary SQL Managed Instance cleanly without `-AllowDataLoss`.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Running `Switch-AzSqlDatabaseInstanceFailoverGroup` against the secondary location promotes the secondary SQL Managed Instance cleanly without `-AllowDataLoss`.

### Question 64 — C

Answer: Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules. Ensure the SQL MI subnet route table routes required Azure SQL Managed Instance management-plane traffic (`SqlManagement` service tag / `0.0.0.0/0` per current single-tag UDR guidance) directly to `Internet` and allows required inbound/outbound NSG ports. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. Local study-map skill 4.5 (Monitor and Troubleshoot Automated Deployments (`CorrelationId`, Quota, SQL MI Subnet Delegation/UDR/NSG)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot ARM/Bicep template and SQL Managed Instance subnet deployment errors (https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/common-deployment-errors).

- **A:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Ensure the SQL MI subnet route table routes required Azure SQL Managed Instance management-plane traffic (`SqlManagement` service tag / `0.0.0.0/0` per current single-tag UDR guidance) directly to `Internet` and allows required inbound/outbound NSG ports.
- **B:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Ensure the SQL MI subnet route table routes required Azure SQL Managed Instance management-plane traffic (`SqlManagement` service tag / `0.0.0.0/0` per current single-tag UDR guidance) directly to `Internet` and allows required inbound/outbound NSG ports.
- **C:** Correct. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. In this scenario: Ensure the SQL MI subnet route table routes required Azure SQL Managed Instance management-plane traffic (`SqlManagement` service tag / `0.0.0.0/0` per current single-tag UDR guidance) directly to `Internet` and allows required inbound/outbound NSG ports.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Ensure the SQL MI subnet route table routes required Azure SQL Managed Instance management-plane traffic (`SqlManagement` service tag / `0.0.0.0/0` per current single-tag UDR guidance) directly to `Internet` and allows required inbound/outbound NSG ports.

### Question 65 — B

Answer: Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules. Add an explicit `dependsOn: [kvRoleAssignment]` (or reference the symbolic resource output) on the TDE protector resource so ARM waits for Key Vault RBAC propagation first. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. Local study-map skill 4.5 (Monitor and Troubleshoot Automated Deployments (`CorrelationId`, Quota, SQL MI Subnet Delegation/UDR/NSG)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Troubleshoot ARM/Bicep template and SQL Managed Instance subnet deployment errors (https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/common-deployment-errors).

- **A:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Add an explicit `dependsOn: [kvRoleAssignment]` (or reference the symbolic resource output) on the TDE protector resource so ARM waits for Key Vault RBAC propagation first.
- **B:** Correct. SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota. In this scenario: Add an explicit `dependsOn: [kvRoleAssignment]` (or reference the symbolic resource output) on the TDE protector resource so ARM waits for Key Vault RBAC propagation first.
- **C:** Incorrect for this requirement. Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere. Why the keyed choice wins: Add an explicit `dependsOn: [kvRoleAssignment]` (or reference the symbolic resource output) on the TDE protector resource so ARM waits for Key Vault RBAC propagation first.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Add an explicit `dependsOn: [kvRoleAssignment]` (or reference the symbolic resource output) on the TDE protector resource so ARM waits for Key Vault RBAC propagation first.

### Question 66 — B

Answer: Azure SQL Database Elastic Job Agent (`jobs.sp_add_job`) authenticating to Target Groups across servers/pools via a User-Assigned Managed Identity (`UAMI`). An Azure SQL Database Elastic Job Agent configured with a User-Assigned Managed Identity fans out T-SQL scripts reliably across Target Groups spanning multiple servers, pools, and subscriptions. Elastic Jobs fan out T-SQL maintenance and schema scripts asynchronously across hundreds of Azure SQL Databases, elastic pools, and subscriptions using passwordless UAMI authentication. Local study-map skill 4.6 (Create and Configure Azure SQL Database Elastic Jobs Across Target Groups Using User-Assigned Managed Identity), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Elastic jobs in Azure SQL Database with Managed Identity authentication (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-jobs-overview).

- **A:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: An Azure SQL Database Elastic Job Agent configured with a User-Assigned Managed Identity fans out T-SQL scripts reliably across Target Groups spanning multiple servers, pools, and subscriptions.
- **B:** Correct. Elastic Jobs fan out T-SQL maintenance and schema scripts asynchronously across hundreds of Azure SQL Databases, elastic pools, and subscriptions using passwordless UAMI authentication. In this scenario: An Azure SQL Database Elastic Job Agent configured with a User-Assigned Managed Identity fans out T-SQL scripts reliably across Target Groups spanning multiple servers, pools, and subscriptions.
- **C:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: An Azure SQL Database Elastic Job Agent configured with a User-Assigned Managed Identity fans out T-SQL scripts reliably across Target Groups spanning multiple servers, pools, and subscriptions.
- **D:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: An Azure SQL Database Elastic Job Agent configured with a User-Assigned Managed Identity fans out T-SQL scripts reliably across Target Groups spanning multiple servers, pools, and subscriptions.

### Question 67 — A

Answer: Create S1+ Job Database & Elastic Job Agent with UAMI → Create contained UAMI user on target DBs with needed permissions → Define Target Group (`jobs.sp_add_target_group_member`) → Add T-SQL steps & schedule (`jobs.sp_add_job`). Create an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and schedule T-SQL steps (`jobs.sp_add_job`). Modern Elastic Jobs use a dedicated S1+ job database, an Elastic Job Agent assigned a User-Assigned Managed Identity (UAMI) authorized on target databases, a target group, and scheduled T-SQL steps. Local study-map skill 4.6 (Create and Configure Azure SQL Database Elastic Jobs Across Target Groups Using User-Assigned Managed Identity), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Elastic jobs in Azure SQL Database with Managed Identity authentication (https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-jobs-overview).

- **A:** Correct. Modern Elastic Jobs use a dedicated S1+ job database, an Elastic Job Agent assigned a User-Assigned Managed Identity (UAMI) authorized on target databases, a target group, and scheduled T-SQL steps. In this scenario: Create an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and schedule T-SQL steps (`jobs.sp_add_job`).
- **B:** Incorrect for this requirement. Incorrect workflow: Elastic Job databases require S1 or higher, target groups must exist before binding executions, NTLM local accounts are invalid in SQL DB, and `msdb` belongs to SQL Agent. Why the keyed choice wins: Create an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and schedule T-SQL steps (`jobs.sp_add_job`).
- **C:** Incorrect for this requirement. Incorrect workflow: single Azure SQL Databases do not have SQL Server Agent or cross-DB linked servers in the same way as SQL MI; Elastic Jobs fan out T-SQL asynchronously. Why the keyed choice wins: Create an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and schedule T-SQL steps (`jobs.sp_add_job`).
- **D:** Incorrect for this requirement. Incorrect workflow: Elastic Job Agents target Azure SQL servers, elastic pools, and databases using Managed Identity—never Cosmos DB containers or hardcoded Git secrets. Why the keyed choice wins: Create an S1+ Job Database and Elastic Job Agent with UAMI, create contained UAMI users on target DBs, define the Target Group (`jobs.sp_add_target_group_member`), and schedule T-SQL steps (`jobs.sp_add_job`).

### Question 68 — C

Answer: Azure Automation PowerShell / Python runbooks (or Azure Functions / Logic Apps) using a System-Assigned Managed Identity on a recurring schedule. Deploying the Azure Automation Hybrid Runbook Worker extension onto Arc-enabled or Azure-connected servers lets Azure Automation execute PowerShell runbooks locally against private on-premises SQL instances. Azure Automation runbooks authenticate via Managed Identity (`Connect-AzAccount -Identity`) to scale vCores/Elastic Pools on schedule, rotate keys, or orchestrate hybrid maintenance via Hybrid Workers. Local study-map skill 4.7 (Automate Database Maintenance and Scaling Using Azure Automation Runbooks, Logic Apps, and Azure Functions), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL maintenance tasks with Azure Automation, Logic Apps, and Functions (https://learn.microsoft.com/en-us/azure/automation/overview).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Deploying the Azure Automation Hybrid Runbook Worker extension onto Arc-enabled or Azure-connected servers lets Azure Automation execute PowerShell runbooks locally against private on-premises SQL instances.
- **B:** Incorrect for this requirement. Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance. Why the keyed choice wins: Deploying the Azure Automation Hybrid Runbook Worker extension onto Arc-enabled or Azure-connected servers lets Azure Automation execute PowerShell runbooks locally against private on-premises SQL instances.
- **C:** Correct. Azure Automation runbooks authenticate via Managed Identity (`Connect-AzAccount -Identity`) to scale vCores/Elastic Pools on schedule, rotate keys, or orchestrate hybrid maintenance via Hybrid Workers. In this scenario: Deploying the Azure Automation Hybrid Runbook Worker extension onto Arc-enabled or Azure-connected servers lets Azure Automation execute PowerShell runbooks locally against private on-premises SQL instances.
- **D:** Incorrect for this requirement. Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation. Why the keyed choice wins: Deploying the Azure Automation Hybrid Runbook Worker extension onto Arc-enabled or Azure-connected servers lets Azure Automation execute PowerShell runbooks locally against private on-premises SQL instances.

### Question 69 — A

Answer: Azure Automation PowerShell / Python runbooks (or Azure Functions / Logic Apps) using a System-Assigned Managed Identity on a recurring schedule. Enable a System-Assigned or User-Assigned Managed Identity on the Function App, use `DefaultAzureCredential`, and assign scoped `SQL DB Contributor` Azure RBAC on the dev-test resource group. Azure Automation runbooks authenticate via Managed Identity (`Connect-AzAccount -Identity`) to scale vCores/Elastic Pools on schedule, rotate keys, or orchestrate hybrid maintenance via Hybrid Workers. Local study-map skill 4.7 (Automate Database Maintenance and Scaling Using Azure Automation Runbooks, Logic Apps, and Azure Functions), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automate Azure SQL maintenance tasks with Azure Automation, Logic Apps, and Functions (https://learn.microsoft.com/en-us/azure/automation/overview).

- **A:** Correct. Azure Automation runbooks authenticate via Managed Identity (`Connect-AzAccount -Identity`) to scale vCores/Elastic Pools on schedule, rotate keys, or orchestrate hybrid maintenance via Hybrid Workers. In this scenario: Enable a System-Assigned or User-Assigned Managed Identity on the Function App, use `DefaultAzureCredential`, and assign scoped `SQL DB Contributor` Azure RBAC on the dev-test resource group.
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Enable a System-Assigned or User-Assigned Managed Identity on the Function App, use `DefaultAzureCredential`, and assign scoped `SQL DB Contributor` Azure RBAC on the dev-test resource group.
- **C:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Enable a System-Assigned or User-Assigned Managed Identity on the Function App, use `DefaultAzureCredential`, and assign scoped `SQL DB Contributor` Azure RBAC on the dev-test resource group.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Enable a System-Assigned or User-Assigned Managed Identity on the Function App, use `DefaultAzureCredential`, and assign scoped `SQL DB Contributor` Azure RBAC on the dev-test resource group.

### Question 70 — B

Answer: Configure Azure Monitor Metric / Log Alert rules routed to Action Groups and query `jobs.job_executions` in the Elastic Job database to diagnose step failures. Create an Azure Monitor Metric Alert rule scoped to the resource group/subscription targeting `cpu_percent` and `deadlock` metrics, bound to an Action Group with SMS and PagerDuty webhook receivers. Action Groups dispatch email/SMS/webhook/Logic App notifications when alert thresholds fire, while `jobs.job_executions` exposes per-target error messages, retries, and timeouts for Elastic Jobs. Local study-map skill 4.8 (Configure Azure Monitor Action Group Alerts on Database Tasks and Troubleshoot `jobs.job_executions`), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Configure Azure Monitor alerts and troubleshoot Elastic Jobs and automated runbooks (https://learn.microsoft.com/en-us/azure/azure-sql/database/alerts-insights-configure-portal).

- **A:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Create an Azure Monitor Metric Alert rule scoped to the resource group/subscription targeting `cpu_percent` and `deadlock` metrics, bound to an Action Group with SMS and PagerDuty webhook receivers.
- **B:** Correct. Action Groups dispatch email/SMS/webhook/Logic App notifications when alert thresholds fire, while `jobs.job_executions` exposes per-target error messages, retries, and timeouts for Elastic Jobs. In this scenario: Create an Azure Monitor Metric Alert rule scoped to the resource group/subscription targeting `cpu_percent` and `deadlock` metrics, bound to an Action Group with SMS and PagerDuty webhook receivers.
- **C:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Create an Azure Monitor Metric Alert rule scoped to the resource group/subscription targeting `cpu_percent` and `deadlock` metrics, bound to an Action Group with SMS and PagerDuty webhook receivers.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Create an Azure Monitor Metric Alert rule scoped to the resource group/subscription targeting `cpu_percent` and `deadlock` metrics, bound to an Action Group with SMS and PagerDuty webhook receivers.

### Question 71 — D

Answer: Yes — the proposed configuration satisfies every stated technical, security, and availability requirement. Yes — Business Critical with Zone Redundancy places synchronous Always On replicas across three physically separate Availability Zones, delivering `RPO = 0` intra-region failover and the `99.995%` SLA. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. Local study-map skill 5.1 (Recommend HA/DR Architectures Based on RPO and RTO (`Zone Redundant`, `Failover Groups`, `Geo-Restore`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Business continuity, RPO/RTO targets, and high availability in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recovery-hadr-overview).

- **A:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: Yes — Business Critical with Zone Redundancy places synchronous Always On replicas across three physically separate Availability Zones, delivering `RPO = 0` intra-region failover and the `99.995%` SLA.
- **B:** Incorrect for this requirement. SQL Server write-ahead logging performs sequential unbuffered writes; enabling `ReadOnly` or `ReadWrite` host caching on `.ldf` disks degrades throughput or risks corruption. Why the keyed choice wins: Yes — Business Critical with Zone Redundancy places synchronous Always On replicas across three physically separate Availability Zones, delivering `RPO = 0` intra-region failover and the `99.995%` SLA.
- **C:** Incorrect for this requirement. `SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state. Why the keyed choice wins: Yes — Business Critical with Zone Redundancy places synchronous Always On replicas across three physically separate Availability Zones, delivering `RPO = 0` intra-region failover and the `99.995%` SLA.
- **D:** Correct. The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints. In this scenario: Yes — Business Critical with Zone Redundancy places synchronous Always On replicas across three physically separate Availability Zones, delivering `RPO = 0` intra-region failover and the `99.995%` SLA.

### Question 72 — D

Answer: Hybrid DR using Managed Instance link with bidirectional online failover between SQL Server 2022 and Azure SQL Managed Instance. With SQL Server 2016 and 2019, Managed Instance link failover into Azure SQL Managed Instance is **one-way** (you cannot fail back online via the link to SQL 2019), whereas SQL Server 2022+ supports bidirectional online failback. SQL Server 2022 supports two-way online planned failover back and forth with Azure SQL Managed Instance via Managed Instance link (whereas SQL Server 2016–2019 link failover is one-way to Azure). Local study-map skill 5.2 (Evaluate Hybrid HA/DR (`Managed Instance Link` Bidirectional SQL 2022 Failover) and Azure-Specific HA Tiers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Hybrid HA/DR with Managed Instance link and distributed Availability Groups (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-disaster-recovery).

- **A:** Incorrect for this requirement. Managed Instance link online failback from SQL MI to SQL Server requires SQL Server 2022 or later; SQL Server 2016 and 2019 support one-way migration into SQL MI only. Why the keyed choice wins: With SQL Server 2016 and 2019, Managed Instance link failover into Azure SQL Managed Instance is **one-way** (you cannot fail back online via the link to SQL 2019), whereas SQL Server 2022+ supports bidirectional online failback.
- **B:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: With SQL Server 2016 and 2019, Managed Instance link failover into Azure SQL Managed Instance is **one-way** (you cannot fail back online via the link to SQL 2019), whereas SQL Server 2022+ supports bidirectional online failback.
- **C:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: With SQL Server 2016 and 2019, Managed Instance link failover into Azure SQL Managed Instance is **one-way** (you cannot fail back online via the link to SQL 2019), whereas SQL Server 2022+ supports bidirectional online failback.
- **D:** Correct. SQL Server 2022 supports two-way online planned failover back and forth with Azure SQL Managed Instance via Managed Instance link (whereas SQL Server 2016–2019 link failover is one-way to Azure). In this scenario: With SQL Server 2016 and 2019, Managed Instance link failover into Azure SQL Managed Instance is **one-way** (you cannot fail back online via the link to SQL 2019), whereas SQL Server 2022+ supports bidirectional online failback.

### Question 73 — B

Answer: Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`). Placing both SQL Server VMs in an Azure Availability Set (or Proximity Placement Group + Availability Set with separate Fault Domains and Update Domains) isolates replicas across physical racks and host update waves. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. Local study-map skill 5.2 (Evaluate Hybrid HA/DR (`Managed Instance Link` Bidirectional SQL 2022 Failover) and Azure-Specific HA Tiers), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Hybrid HA/DR with Managed Instance link and distributed Availability Groups (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-disaster-recovery).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Placing both SQL Server VMs in an Azure Availability Set (or Proximity Placement Group + Availability Set with separate Fault Domains and Update Domains) isolates replicas across physical racks and host update waves.
- **B:** Correct. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. In this scenario: Placing both SQL Server VMs in an Azure Availability Set (or Proximity Placement Group + Availability Set with separate Fault Domains and Update Domains) isolates replicas across physical racks and host update waves.
- **C:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Placing both SQL Server VMs in an Azure Availability Set (or Proximity Placement Group + Availability Set with separate Fault Domains and Update Domains) isolates replicas across physical racks and host update waves.
- **D:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: Placing both SQL Server VMs in an Azure Availability Set (or Proximity Placement Group + Availability Set with separate Fault Domains and Update Domains) isolates replicas across physical racks and host update waves.

### Question 74 — C

Answer: Provision secondary SQL server with matching firewall/Private Link & Entra admin → Create Failover Group with coupled DBs → Point apps to `<fog>.database.windows.net` & `.secondary` → Run planned `Switch-AzSqlDatabaseFailoverGroup` drill. Verify matching network/Entra settings on the secondary server, confirm all coupled DBs belong to the Failover Group, validate apps use `<fog>.database.windows.net` / `.secondary`, and run planned failover + failback. A resilient Failover Group mirrors security/network configs on the secondary server, groups coupled databases under stable read-write and read-only listeners, and validates readiness via planned zero-data-loss failover. Local study-map skill 5.3 (Plan Non-Disruptive HA/DR Failover Drills, Listener Redirection Validation, and Read-Only Secondary Testing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Disaster recovery drills and failover testing for Azure SQL solutions (https://learn.microsoft.com/en-us/azure/azure-sql/database/disaster-recovery-drills).

- **A:** Incorrect for this requirement. Incorrect workflow: deleting production databases and manually rewriting connection strings causes hours of avoidable downtime instead of testing non-disruptive Failover Group listener failover. Why the keyed choice wins: Verify matching network/Entra settings on the secondary server, confirm all coupled DBs belong to the Failover Group, validate apps use `<fog>.database.windows.net` / `.secondary`, and run planned failover + failback.
- **B:** Incorrect for this requirement. Incorrect workflow: forced failover with `AllowDataLoss` risks dropping uncommitted transactions during drills, and hardcoding regional server names breaks automatic client redirection. Why the keyed choice wins: Verify matching network/Entra settings on the secondary server, confirm all coupled DBs belong to the Failover Group, validate apps use `<fog>.database.windows.net` / `.secondary`, and run planned failover + failback.
- **C:** Correct. A resilient Failover Group mirrors security/network configs on the secondary server, groups coupled databases under stable read-write and read-only listeners, and validates readiness via planned zero-data-loss failover. In this scenario: Verify matching network/Entra settings on the secondary server, confirm all coupled DBs belong to the Failover Group, validate apps use `<fog>.database.windows.net` / `.secondary`, and run planned failover + failback.
- **D:** Incorrect for this requirement. Incorrect workflow: Failover Groups span distinct regions, replicate user databases rather than `master`/`tempdb`, and `.secondary.database.windows.net` is strictly read-only. Why the keyed choice wins: Verify matching network/Entra settings on the secondary server, confirm all coupled DBs belong to the Failover Group, validate apps use `<fog>.database.windows.net` / `.secondary`, and run planned failover + failback.

### Question 75 — C

Answer: Non-disruptive DR readiness drill executing a planned zero-data-loss Failover Group switch (`Switch-AzSqlDatabaseFailoverGroup`), validating app listeners, and failing back. Confirm Private Endpoints / firewall rules, Microsoft Entra admin, Key Vault CMK permissions, and contained database users or `master` SID logins match the primary server so secondary connections succeed immediately. Planned failover synchronizes pending log records before switching roles (`RPO = 0`), validating secondary firewall/Entra configs and `<fog>.database.windows.net` DNS redirection safely. Local study-map skill 5.3 (Plan Non-Disruptive HA/DR Failover Drills, Listener Redirection Validation, and Read-Only Secondary Testing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Disaster recovery drills and failover testing for Azure SQL solutions (https://learn.microsoft.com/en-us/azure/azure-sql/database/disaster-recovery-drills).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Confirm Private Endpoints / firewall rules, Microsoft Entra admin, Key Vault CMK permissions, and contained database users or `master` SID logins match the primary server so secondary connections succeed immediately.
- **B:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Confirm Private Endpoints / firewall rules, Microsoft Entra admin, Key Vault CMK permissions, and contained database users or `master` SID logins match the primary server so secondary connections succeed immediately.
- **C:** Correct. Planned failover synchronizes pending log records before switching roles (`RPO = 0`), validating secondary firewall/Entra configs and `<fog>.database.windows.net` DNS redirection safely. In this scenario: Confirm Private Endpoints / firewall rules, Microsoft Entra admin, Key Vault CMK permissions, and contained database users or `master` SID logins match the primary server so secondary connections succeed immediately.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Confirm Private Endpoints / firewall rules, Microsoft Entra admin, Key Vault CMK permissions, and contained database users or `master` SID logins match the primary server so secondary connections succeed immediately.

### Question 76 — C

Answer: No — moving a database across SQL Managed Instances starts a fresh backup chain and does not carry over prior PITR backups. No — moving a database across SQL Managed Instances starts a brand-new backup chain upon completion; pre-move PITR backups do not transfer to the destination instance. Online SQL Managed Instance Database Move replicates current data with zero loss, but historical PITR backups remain tied to the source instance and are unavailable on the destination. Local study-map skill 5.4 (Recommend Backup & Restore Strategies (`COPY_ONLY` on MI/AGs and Azure Backup SQL-Aware Policies on VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated backups, COPY_ONLY backups, and Azure Backup for SQL Server in Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-overview).

- **A:** Incorrect for this requirement. The proposed solution fails at least one stated technical, security, or availability requirement. Why the keyed choice wins: No — moving a database across SQL Managed Instances starts a brand-new backup chain upon completion; pre-move PITR backups do not transfer to the destination instance.
- **B:** Incorrect for this requirement. Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied. Why the keyed choice wins: No — moving a database across SQL Managed Instances starts a brand-new backup chain upon completion; pre-move PITR backups do not transfer to the destination instance.
- **C:** Correct. Online SQL Managed Instance Database Move replicates current data with zero loss, but historical PITR backups remain tied to the source instance and are unavailable on the destination. In this scenario: No — moving a database across SQL Managed Instances starts a brand-new backup chain upon completion; pre-move PITR backups do not transfer to the destination instance.
- **D:** Incorrect for this requirement. Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate. Why the keyed choice wins: No — moving a database across SQL Managed Instances starts a brand-new backup chain upon completion; pre-move PITR backups do not transfer to the destination instance.

### Question 77 — C

Answer: Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback. Yes — as long as the parent logical SQL server itself was not deleted, Azure retains automated PITR backups of deleted databases for the configured `1–35` day retention period (`Deleted databases` blade / `Restore-AzSqlDatabase -FromDeletedDatabaseBackup`). Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. Local study-map skill 5.5 (Perform Native Restores, Point-in-Time Restore (`1–35d` PITR), Deleted-DB Restore, and `ADR` Instant Rollback), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Point-in-time restore (PITR), Accelerated Database Recovery (ADR), and deleted DB restore (https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups).

- **A:** Incorrect for this requirement. Short-Term PITR caps at `35` days (`1–35` days); multi-year retention up to `10 years` with WORM deletion lock requires Long-Term Retention (`LTR`) with time-based immutability. Why the keyed choice wins: Yes — as long as the parent logical SQL server itself was not deleted, Azure retains automated PITR backups of deleted databases for the configured `1–35` day retention period (`Deleted databases` blade / `Restore-AzSqlDatabase -FromDeletedDatabaseBackup`).
- **B:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: Yes — as long as the parent logical SQL server itself was not deleted, Azure retains automated PITR backups of deleted databases for the configured `1–35` day retention period (`Deleted databases` blade / `Restore-AzSqlDatabase -FromDeletedDatabaseBackup`).
- **C:** Correct. Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. In this scenario: Yes — as long as the parent logical SQL server itself was not deleted, Azure retains automated PITR backups of deleted databases for the configured `1–35` day retention period (`Deleted databases` blade / `Restore-AzSqlDatabase -FromDeletedDatabaseBackup`).
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Yes — as long as the parent logical SQL server itself was not deleted, Azure retains automated PITR backups of deleted databases for the configured `1–35` day retention period (`Deleted databases` blade / `Restore-AzSqlDatabase -FromDeletedDatabaseBackup`).

### Question 78 — D

Answer: Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback. Specifying `STOPAT = '2026-11-01T11:42:14'` with `RECOVERY` on the final transaction log backup replays committed log records up to the exact second before the erroneous `UPDATE`. Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. Local study-map skill 5.5 (Perform Native Restores, Point-in-Time Restore (`1–35d` PITR), Deleted-DB Restore, and `ADR` Instant Rollback), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Point-in-time restore (PITR), Accelerated Database Recovery (ADR), and deleted DB restore (https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Specifying `STOPAT = '2026-11-01T11:42:14'` with `RECOVERY` on the final transaction log backup replays committed log records up to the exact second before the erroneous `UPDATE`.
- **B:** Incorrect for this requirement. A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs. Why the keyed choice wins: Specifying `STOPAT = '2026-11-01T11:42:14'` with `RECOVERY` on the final transaction log backup replays committed log records up to the exact second before the erroneous `UPDATE`.
- **C:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Specifying `STOPAT = '2026-11-01T11:42:14'` with `RECOVERY` on the final transaction log backup replays committed log records up to the exact second before the erroneous `UPDATE`.
- **D:** Correct. Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback. In this scenario: Specifying `STOPAT = '2026-11-01T11:42:14'` with `RECOVERY` on the final transaction log backup replays committed log records up to the exact second before the erroneous `UPDATE`.

### Question 79 — A

Answer: Long-Term Retention (`LTR`) weekly/monthly/yearly backups up to `10 years` protected by a locked time-based immutable (`WORM`) policy and `RA-GRS` / `ZRS` backup storage. Short-term PITR supports `1` to `35` days (7 days default), whereas Long-Term Retention (`LTR`) retains full weekly, monthly, and yearly backups for up to `10` years. LTR retains compliance backups up to 10 years independently of PITR, and locking time-based immutability prevents even Subscription Owners from deleting backups before expiry. Local study-map skill 5.6 (Configure Long-Term Backup Retention (`LTR` up to `10y`), Time-Based Immutable WORM Locks, and Storage Redundancy), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Long-term backup retention (LTR) and time-based immutable WORM backups in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/long-term-retention-overview).

- **A:** Correct. LTR retains compliance backups up to 10 years independently of PITR, and locking time-based immutability prevents even Subscription Owners from deleting backups before expiry. In this scenario: Short-term PITR supports `1` to `35` days (7 days default), whereas Long-Term Retention (`LTR`) retains full weekly, monthly, and yearly backups for up to `10` years.
- **B:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Short-term PITR supports `1` to `35` days (7 days default), whereas Long-Term Retention (`LTR`) retains full weekly, monthly, and yearly backups for up to `10` years.
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Short-term PITR supports `1` to `35` days (7 days default), whereas Long-Term Retention (`LTR`) retains full weekly, monthly, and yearly backups for up to `10` years.
- **D:** Incorrect for this requirement. Short-Term PITR caps at `35` days (`1–35` days); multi-year retention up to `10 years` with WORM deletion lock requires Long-Term Retention (`LTR`) with time-based immutability. Why the keyed choice wins: Short-term PITR supports `1` to `35` days (7 days default), whereas Long-Term Retention (`LTR`) retains full weekly, monthly, and yearly backups for up to `10` years.

### Question 80 — C, D

Answers: Create a SQL Server `CREDENTIAL` (`IDENTITY = 'Managed Identity'` or `'SHARED ACCESS SIGNATURE'`) matching the Azure Blob container URL; Stripe `BACKUP DATABASE` across multiple `TO URL = 'https://...bak'` block blob targets with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`. Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob Storage endpoint (granting the VM identity `Storage Blob Data Contributor`), and stripe `BACKUP DATABASE` across multiple `TO URL` block blobs. Local study-map skill 5.7 (Back Up to and Restore from Azure Blob Storage URL Using T-SQL Stripes (`TO URL`) and Managed Identity / SAS), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server backup to URL and restore from Azure Blob Storage with Managed Identity or SAS (https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url-azure-blob-storage).

- **A:** Incorrect for this requirement. A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs. Why the keyed choice wins: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob Storage endpoint (granting the VM identity `Storage Blob Data Contributor`), and stripe `BACKUP DATABASE` across multiple `TO URL` block blobs.
- **B:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob Storage endpoint (granting the VM identity `Storage Blob Data Contributor`), and stripe `BACKUP DATABASE` across multiple `TO URL` block blobs.
- **C:** Correct. SQL Server and SQL MI authenticate `BACKUP TO URL` / `RESTORE FROM URL` requests to Azure Storage via a server-level credential. In this scenario: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob Storage endpoint (granting the VM identity `Storage Blob Data Contributor`), and stripe `BACKUP DATABASE` across multiple `TO URL` block blobs.
- **D:** Correct. Multiple `URL` targets write to Azure Block Blobs in parallel, scaling single backups up to ~12.8 TB (`64` stripes) with maximum throughput. In this scenario: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob Storage endpoint (granting the VM identity `Storage Blob Data Contributor`), and stripe `BACKUP DATABASE` across multiple `TO URL` block blobs.
- **E:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Create a server `CREDENTIAL` with `IDENTITY = 'Managed Identity'` for the Blob Storage endpoint (granting the VM identity `Storage Blob Data Contributor`), and stripe `BACKUP DATABASE` across multiple `TO URL` block blobs.

### Question 81 — B

Answer: Striped T-SQL `BACKUP DATABASE ... TO URL = ...` across up to 64 block blobs (`MAXTRANSFERSIZE`, `COMPRESSION`) authenticated via `Managed Identity` or `SHARED ACCESS SIGNATURE` Credential. List **all four** striped `URL = 'https://.../PACS_1.bak', URL = 'https://.../PACS_2.bak', ...` clauses together in a single `RESTORE DATABASE` command backed by a matching server `CREDENTIAL`. Backing up to multiple URLs creates block blobs supporting up to ~12.8 TB striped backups (`200 GB+` per blob, unlike legacy single-page-blob 1 TB limits) using `CREATE CREDENTIAL`. Local study-map skill 5.7 (Back Up to and Restore from Azure Blob Storage URL Using T-SQL Stripes (`TO URL`) and Managed Identity / SAS), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server backup to URL and restore from Azure Blob Storage with Managed Identity or SAS (https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url-azure-blob-storage).

- **A:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: List **all four** striped `URL = 'https://.../PACS_1.bak', URL = 'https://.../PACS_2.bak', ...` clauses together in a single `RESTORE DATABASE` command backed by a matching server `CREDENTIAL`.
- **B:** Correct. Backing up to multiple URLs creates block blobs supporting up to ~12.8 TB striped backups (`200 GB+` per blob, unlike legacy single-page-blob 1 TB limits) using `CREATE CREDENTIAL`. In this scenario: List **all four** striped `URL = 'https://.../PACS_1.bak', URL = 'https://.../PACS_2.bak', ...` clauses together in a single `RESTORE DATABASE` command backed by a matching server `CREDENTIAL`.
- **C:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: List **all four** striped `URL = 'https://.../PACS_1.bak', URL = 'https://.../PACS_2.bak', ...` clauses together in a single `RESTORE DATABASE` command backed by a matching server `CREDENTIAL`.
- **D:** Incorrect for this requirement. A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs. Why the keyed choice wins: List **all four** striped `URL = 'https://.../PACS_1.bak', URL = 'https://.../PACS_2.bak', ...` clauses together in a single `RESTORE DATABASE` command backed by a matching server `CREDENTIAL`.

### Question 82 — B

Answer: Failover Groups for automatic multi-database failover behind stable `<fog>.database.windows.net` / `.secondary` listeners vs Active Geo-Replication for up to 4 readable secondaries. A Failover Group fails over all member databases together as a unit behind stable `<fog>.database.windows.net` and `.secondary` listener endpoints, whereas independent Active Geo-Replication fails over databases individually without listener redirection. Failover Groups fail over coupled databases together and redirect connection strings automatically (`GracePeriodWithDataLossHours >= 1`), whereas Active Geo-Replication supports up to 4 secondaries per DB without automatic listener redirection. Local study-map skill 5.8 (Configure Failover Groups (`<fog>.database.windows.net`, Grace Period) vs Active Geo-Replication (`4` Replicas)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Failover groups and active geo-replication in Azure SQL Database and SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db).

- **A:** Incorrect for this requirement. Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth. Why the keyed choice wins: A Failover Group fails over all member databases together as a unit behind stable `<fog>.database.windows.net` and `.secondary` listener endpoints, whereas independent Active Geo-Replication fails over databases individually without listener redirection.
- **B:** Correct. Failover Groups fail over coupled databases together and redirect connection strings automatically (`GracePeriodWithDataLossHours >= 1`), whereas Active Geo-Replication supports up to 4 secondaries per DB without automatic listener redirection. In this scenario: A Failover Group fails over all member databases together as a unit behind stable `<fog>.database.windows.net` and `.secondary` listener endpoints, whereas independent Active Geo-Replication fails over databases individually without listener redirection.
- **C:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: A Failover Group fails over all member databases together as a unit behind stable `<fog>.database.windows.net` and `.secondary` listener endpoints, whereas independent Active Geo-Replication fails over databases individually without listener redirection.
- **D:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: A Failover Group fails over all member databases together as a unit behind stable `<fog>.database.windows.net` and `.secondary` listener endpoints, whereas independent Active Geo-Replication fails over databases individually without listener redirection.

### Question 83 — C

Answer: Failover Groups for automatic multi-database failover behind stable `<fog>.database.windows.net` / `.secondary` listeners vs Active Geo-Replication for up to 4 readable secondaries. Both SQL Managed Instances must reside in non-overlapping IP ranges connected via Global VNet Peering (or VPN/ExpressRoute) with NSGs permitting bidirectional TCP `5022` and ephemeral ports `11000–11999`. Failover Groups fail over coupled databases together and redirect connection strings automatically (`GracePeriodWithDataLossHours >= 1`), whereas Active Geo-Replication supports up to 4 secondaries per DB without automatic listener redirection. Local study-map skill 5.8 (Configure Failover Groups (`<fog>.database.windows.net`, Grace Period) vs Active Geo-Replication (`4` Replicas)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Failover groups and active geo-replication in Azure SQL Database and SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db).

- **A:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Both SQL Managed Instances must reside in non-overlapping IP ranges connected via Global VNet Peering (or VPN/ExpressRoute) with NSGs permitting bidirectional TCP `5022` and ephemeral ports `11000–11999`.
- **B:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: Both SQL Managed Instances must reside in non-overlapping IP ranges connected via Global VNet Peering (or VPN/ExpressRoute) with NSGs permitting bidirectional TCP `5022` and ephemeral ports `11000–11999`.
- **C:** Correct. Failover Groups fail over coupled databases together and redirect connection strings automatically (`GracePeriodWithDataLossHours >= 1`), whereas Active Geo-Replication supports up to 4 secondaries per DB without automatic listener redirection. In this scenario: Both SQL Managed Instances must reside in non-overlapping IP ranges connected via Global VNet Peering (or VPN/ExpressRoute) with NSGs permitting bidirectional TCP `5022` and ephemeral ports `11000–11999`.
- **D:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: Both SQL Managed Instances must reside in non-overlapping IP ranges connected via Global VNet Peering (or VPN/ExpressRoute) with NSGs permitting bidirectional TCP `5022` and ephemeral ports `11000–11999`.

### Question 84 — A, B

Answers: Configure an Azure Cloud Witness in a standard Storage Account (`LRS`/`ZRS`) to provide lightweight quorum voting for a 2-node WSFC; Deploy a Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` TCP `59999`) listener and set `MultiSubnetFailover=True` on clients. Configure an Azure Cloud Witness for 3-vote WSFC quorum arbitration, and configure a multi-subnet listener with `MultiSubnetFailover=True` in all client connection strings. Local study-map skill 5.9 (Configure Always On Availability Groups on SQL MI and Azure VMs (`Cloud Witness`, `DNN`, `ILB` Port `59999`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On availability groups on SQL Server on Azure VMs (Cloud Witness, DNN, ILB) (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/availability-group-overview).

- **A:** Correct. Cloud Witness maintains a tiny blob arbitration file without the cost and patching overhead of running a third witness VM. In this scenario: Configure an Azure Cloud Witness for 3-vote WSFC quorum arbitration, and configure a multi-subnet listener with `MultiSubnetFailover=True` in all client connection strings.
- **B:** Correct. `MultiSubnetFailover=True` makes SQL client drivers try all listener IPs in parallel across subnets, cutting cross-subnet AG failover reconnect latency to seconds. In this scenario: Configure an Azure Cloud Witness for 3-vote WSFC quorum arbitration, and configure a multi-subnet listener with `MultiSubnetFailover=True` in all client connection strings.
- **C:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Configure an Azure Cloud Witness for 3-vote WSFC quorum arbitration, and configure a multi-subnet listener with `MultiSubnetFailover=True` in all client connection strings.
- **D:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: Configure an Azure Cloud Witness for 3-vote WSFC quorum arbitration, and configure a multi-subnet listener with `MultiSubnetFailover=True` in all client connection strings.
- **E:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure an Azure Cloud Witness for 3-vote WSFC quorum arbitration, and configure a multi-subnet listener with `MultiSubnetFailover=True` in all client connection strings.

### Question 85 — D

Answer: Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`. The subnet NSG is blocking inbound health-probe traffic from Azure Load Balancer (`AzureLoadBalancer` service tag / `168.63.129.16`) on the configured WSFC IP probe port (commonly TCP `59999`). Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). Local study-map skill 5.9 (Configure Always On Availability Groups on SQL MI and Azure VMs (`Cloud Witness`, `DNN`, `ILB` Port `59999`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On availability groups on SQL Server on Azure VMs (Cloud Witness, DNN, ILB) (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/availability-group-overview).

- **A:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: The subnet NSG is blocking inbound health-probe traffic from Azure Load Balancer (`AzureLoadBalancer` service tag / `168.63.129.16`) on the configured WSFC IP probe port (commonly TCP `59999`).
- **B:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: The subnet NSG is blocking inbound health-probe traffic from Azure Load Balancer (`AzureLoadBalancer` service tag / `168.63.129.16`) on the configured WSFC IP probe port (commonly TCP `59999`).
- **C:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: The subnet NSG is blocking inbound health-probe traffic from Azure Load Balancer (`AzureLoadBalancer` service tag / `168.63.129.16`) on the configured WSFC IP probe port (commonly TCP `59999`).
- **D:** Correct. Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers). In this scenario: The subnet NSG is blocking inbound health-probe traffic from Azure Load Balancer (`AzureLoadBalancer` service tag / `168.63.129.16`) on the configured WSFC IP probe port (commonly TCP `59999`).

### Question 86 — B

Answer: Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`). An FCI shares single-copy storage (`ZRS` Azure Shared Disks or Premium Azure Files) across nodes for whole-instance failover with **no** readable secondary copy, whereas an AG maintains independent database copies per node and supports readable secondaries. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. Local study-map skill 5.10 (Configure Always On Failover Cluster Instances (`Azure Shared Disks` `ZRS`) and T-SQL Log Shipping on Azure VMs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On Failover Cluster Instances (Azure Shared Disks) and Log Shipping on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/failover-cluster-instance-overview).

- **A:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: An FCI shares single-copy storage (`ZRS` Azure Shared Disks or Premium Azure Files) across nodes for whole-instance failover with **no** readable secondary copy, whereas an AG maintains independent database copies per node and supports readable secondaries.
- **B:** Correct. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. In this scenario: An FCI shares single-copy storage (`ZRS` Azure Shared Disks or Premium Azure Files) across nodes for whole-instance failover with **no** readable secondary copy, whereas an AG maintains independent database copies per node and supports readable secondaries.
- **C:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: An FCI shares single-copy storage (`ZRS` Azure Shared Disks or Premium Azure Files) across nodes for whole-instance failover with **no** readable secondary copy, whereas an AG maintains independent database copies per node and supports readable secondaries.
- **D:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: An FCI shares single-copy storage (`ZRS` Azure Shared Disks or Premium Azure Files) across nodes for whole-instance failover with **no** readable secondary copy, whereas an AG maintains independent database copies per node and supports readable secondaries.

### Question 87 — B

Answer: Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`). The **Backup job** runs on the primary server (`sqllogship.exe -Backup`), while the **Copy job** and **Restore job** (`NORECOVERY` or `STANDBY`) run on the secondary server. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. Local study-map skill 5.10 (Configure Always On Failover Cluster Instances (`Azure Shared Disks` `ZRS`) and T-SQL Log Shipping on Azure VMs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Always On Failover Cluster Instances (Azure Shared Disks) and Log Shipping on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/failover-cluster-instance-overview).

- **A:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: The **Backup job** runs on the primary server (`sqllogship.exe -Backup`), while the **Copy job** and **Restore job** (`NORECOVERY` or `STANDBY`) run on the secondary server.
- **B:** Correct. Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores. In this scenario: The **Backup job** runs on the primary server (`sqllogship.exe -Backup`), while the **Copy job** and **Restore job** (`NORECOVERY` or `STANDBY`) run on the secondary server.
- **C:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: The **Backup job** runs on the primary server (`sqllogship.exe -Backup`), while the **Copy job** and **Restore job** (`NORECOVERY` or `STANDBY`) run on the secondary server.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: The **Backup job** runs on the primary server (`sqllogship.exe -Backup`), while the **Copy job** and **Restore job** (`NORECOVERY` or `STANDBY`) run on the secondary server.

### Question 88 — C

Answer: Query `sys.dm_hadr_database_replica_states` (`synchronization_state_desc`, `log_send_queue_size`, `redo_queue_size`) and `sys.dm_geo_replication_link_status`, plus verify NSG probe port `59999`. Querying `sys.dm_geo_replication_link_status` returns real-time link state (`SEEDING`, `CATCH_UP`, `SUSPENDED`), replication lag in seconds, and last hardened commit time for every geo-secondary. High `log_send_queue_size` indicates network bottlenecks between primary and secondary, high `redo_queue_size` indicates slow redo I/O/CPU or long-running read queries on the secondary, and blocked ILB probe port `59999` breaks AG listener routing. Local study-map skill 5.11 (Monitor and Troubleshoot HA/DR Health (`sys.dm_hadr_database_replica_states`, `redo_queue_size`, `log_send_queue_size`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor and troubleshoot Always On availability groups and geo-replication health (https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/monitor-availability-groups-transact-sql).

- **A:** Incorrect for this requirement. A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections. Why the keyed choice wins: Querying `sys.dm_geo_replication_link_status` returns real-time link state (`SEEDING`, `CATCH_UP`, `SUSPENDED`), replication lag in seconds, and last hardened commit time for every geo-secondary.
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Querying `sys.dm_geo_replication_link_status` returns real-time link state (`SEEDING`, `CATCH_UP`, `SUSPENDED`), replication lag in seconds, and last hardened commit time for every geo-secondary.
- **C:** Correct. High `log_send_queue_size` indicates network bottlenecks between primary and secondary, high `redo_queue_size` indicates slow redo I/O/CPU or long-running read queries on the secondary, and blocked ILB probe port `59999` breaks AG listener routing. In this scenario: Querying `sys.dm_geo_replication_link_status` returns real-time link state (`SEEDING`, `CATCH_UP`, `SUSPENDED`), replication lag in seconds, and last hardened commit time for every geo-secondary.
- **D:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Querying `sys.dm_geo_replication_link_status` returns real-time link state (`SEEDING`, `CATCH_UP`, `SUSPENDED`), replication lag in seconds, and last hardened commit time for every geo-secondary.

### Question 89 — A

Answer: Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`). An Instance Failover Group across the East US 2 and Central US Azure SQL Managed Instances replicates all user databases together and redirects `<fog>.<dns_zone>.database.windows.net` automatically. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. Local study-map skill 5.1 (Recommend HA/DR Architectures Based on RPO and RTO (`Zone Redundant`, `Failover Groups`, `Geo-Restore`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Business continuity, RPO/RTO targets, and high availability in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recovery-hadr-overview).

- **A:** Correct. Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups. In this scenario: An Instance Failover Group across the East US 2 and Central US Azure SQL Managed Instances replicates all user databases together and redirects `<fog>.<dns_zone>.database.windows.net` automatically.
- **B:** Incorrect for this requirement. Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover. Why the keyed choice wins: An Instance Failover Group across the East US 2 and Central US Azure SQL Managed Instances replicates all user databases together and redirects `<fog>.<dns_zone>.database.windows.net` automatically.
- **C:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: An Instance Failover Group across the East US 2 and Central US Azure SQL Managed Instances replicates all user databases together and redirects `<fog>.<dns_zone>.database.windows.net` automatically.
- **D:** Incorrect for this requirement. DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads. Why the keyed choice wins: An Instance Failover Group across the East US 2 and Central US Azure SQL Managed Instances replicates all user databases together and redirects `<fog>.<dns_zone>.database.windows.net` automatically.

### Question 90 — A

Answer: Use `BACKUP DATABASE ... WITH COPY_ONLY` for ad-hoc exports on SQL MI / AGs, and Azure Backup Recovery Services Vault SQL-aware policies (`15-min` log RPO) on SQL VMs. Azure SQL Managed Instance manages automated Full, Differential, and Log backups internally; user-initiated `BACKUP DATABASE` only permits `WITH COPY_ONLY` so the automated differential base LSN is never disrupted. `COPY_ONLY` preserves the differential and log backup chain, while Azure Backup for SQL Server in Azure VMs automates application-consistent Full, Differential, and 15-minute Transaction Log backups. Local study-map skill 5.4 (Recommend Backup & Restore Strategies (`COPY_ONLY` on MI/AGs and Azure Backup SQL-Aware Policies on VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Automated backups, COPY_ONLY backups, and Azure Backup for SQL Server in Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-overview).

- **A:** Correct. `COPY_ONLY` preserves the differential and log backup chain, while Azure Backup for SQL Server in Azure VMs automates application-consistent Full, Differential, and 15-minute Transaction Log backups. In this scenario: Azure SQL Managed Instance manages automated Full, Differential, and Log backups internally; user-initiated `BACKUP DATABASE` only permits `WITH COPY_ONLY` so the automated differential base LSN is never disrupted.
- **B:** Incorrect for this requirement. A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs. Why the keyed choice wins: Azure SQL Managed Instance manages automated Full, Differential, and Log backups internally; user-initiated `BACKUP DATABASE` only permits `WITH COPY_ONLY` so the automated differential base LSN is never disrupted.
- **C:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Azure SQL Managed Instance manages automated Full, Differential, and Log backups internally; user-initiated `BACKUP DATABASE` only permits `WITH COPY_ONLY` so the automated differential base LSN is never disrupted.
- **D:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Azure SQL Managed Instance manages automated Full, Differential, and Log backups internally; user-initiated `BACKUP DATABASE` only permits `WITH COPY_ONLY` so the automated differential base LSN is never disrupted.

### Question 91 — C, D

Answers: Configure an Azure SQL Long-Term Retention (`LTR`) policy (`WeeklyRetention`, `MonthlyRetention`, `YearlyRetention`, `WeekOfYear`) up to 10 years; Enable and lock time-based immutability (`WORM`) on the LTR backup policy so nobody can shorten retention or delete compliance backups early. Configure a Long-Term Retention (`LTR`) policy (`YearlyRetention = P7Y` / `MonthlyRetention`) and enable + lock time-based immutability (`WORM`) on the LTR backups. Local study-map skill 5.6 (Configure Long-Term Backup Retention (`LTR` up to `10y`), Time-Based Immutable WORM Locks, and Storage Redundancy), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Long-term backup retention (LTR) and time-based immutable WORM backups in Azure SQL (https://learn.microsoft.com/en-us/azure/azure-sql/database/long-term-retention-overview).

- **A:** Incorrect for this requirement. Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules. Why the keyed choice wins: Configure a Long-Term Retention (`LTR`) policy (`YearlyRetention = P7Y` / `MonthlyRetention`) and enable + lock time-based immutability (`WORM`) on the LTR backups.
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Configure a Long-Term Retention (`LTR`) policy (`YearlyRetention = P7Y` / `MonthlyRetention`) and enable + lock time-based immutability (`WORM`) on the LTR backups.
- **C:** Correct. Once locked, time-based LTR immutability enforces write-once-read-many protection against ransomware or rogue privileged admins. In this scenario: Configure a Long-Term Retention (`LTR`) policy (`YearlyRetention = P7Y` / `MonthlyRetention`) and enable + lock time-based immutability (`WORM`) on the LTR backups.
- **D:** Correct. LTR copies full backups into separate geo-redundant/zone-redundant Azure Blob tiers according to ISO-8601 duration policies (e.g., `P7Y`). In this scenario: Configure a Long-Term Retention (`LTR`) policy (`YearlyRetention = P7Y` / `MonthlyRetention`) and enable + lock time-based immutability (`WORM`) on the LTR backups.
- **E:** Incorrect for this requirement. Short-Term PITR caps at `35` days (`1–35` days); multi-year retention up to `10 years` with WORM deletion lock requires Long-Term Retention (`LTR`) with time-based immutability. Why the keyed choice wins: Configure a Long-Term Retention (`LTR`) policy (`YearlyRetention = P7Y` / `MonthlyRetention`) and enable + lock time-based immutability (`WORM`) on the LTR backups.

### Question 92 — D

Answer: Database watcher streaming SQL DB and SQL MI telemetry into Fabric Eventhouse / Azure Data Explorer (with planned transition to Database Hub in Microsoft Fabric). Database watcher streams SQL DB and SQL MI telemetry into Fabric Eventhouse / Azure Data Explorer via `VIEW SERVER PERFORMANCE STATE`, and teams must plan transition to Database Hub in Microsoft Fabric ahead of database watcher's April 30, 2027 retirement. Database watcher collects agentless performance telemetry via `VIEW SERVER PERFORMANCE STATE` into KQL stores; Microsoft announced transition to Database Hub in Fabric ahead of April 30, 2027 retirement. Local study-map skill 3.3 (Monitor Workloads Using Database Watcher (ADX / Fabric Eventhouse) and Plan Fabric Database Hub Transition), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Monitor Azure SQL workloads with database watcher and Database Hub in Microsoft Fabric (https://learn.microsoft.com/en-us/azure/azure-sql/database-watcher-overview).

- **A:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Database watcher streams SQL DB and SQL MI telemetry into Fabric Eventhouse / Azure Data Explorer via `VIEW SERVER PERFORMANCE STATE`, and teams must plan transition to Database Hub in Microsoft Fabric ahead of database watcher's April 30, 2027 retirement.
- **B:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Database watcher streams SQL DB and SQL MI telemetry into Fabric Eventhouse / Azure Data Explorer via `VIEW SERVER PERFORMANCE STATE`, and teams must plan transition to Database Hub in Microsoft Fabric ahead of database watcher's April 30, 2027 retirement.
- **C:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Database watcher streams SQL DB and SQL MI telemetry into Fabric Eventhouse / Azure Data Explorer via `VIEW SERVER PERFORMANCE STATE`, and teams must plan transition to Database Hub in Microsoft Fabric ahead of database watcher's April 30, 2027 retirement.
- **D:** Correct. Database watcher collects agentless performance telemetry via `VIEW SERVER PERFORMANCE STATE` into KQL stores; Microsoft announced transition to Database Hub in Fabric ahead of April 30, 2027 retirement. In this scenario: Database watcher streams SQL DB and SQL MI telemetry into Fabric Eventhouse / Azure Data Explorer via `VIEW SERVER PERFORMANCE STATE`, and teams must plan transition to Database Hub in Microsoft Fabric ahead of database watcher's April 30, 2027 retirement.

### Question 93 — A, E

Answers: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE` with `rwl` permissions) for the Azure Blob container; Define `CREATE EVENT SESSION ... ON DATABASE ADD TARGET package0.event_file(SET filename = N'https://...xel')` and start the session. Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS) for the Azure Blob container, and create an `ON DATABASE` Extended Events session writing to `package0.event_file`. Local study-map skill 3.4 (Monitor Workloads Using Extended Events (`ON DATABASE` vs `ON SERVER` & Persistent Blob `event_file` Targets)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Extended Events in Azure SQL Database and Azure SQL Managed Instance (https://learn.microsoft.com/en-us/azure/azure-sql/database/xevent-db-diff-from-svr).

- **A:** Correct. Extended Events in Azure SQL Database requires a `DATABASE SCOPED CREDENTIAL` with Read, Write, and List rights on the target Blob Storage container. In this scenario: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS) for the Azure Blob container, and create an `ON DATABASE` Extended Events session writing to `package0.event_file`.
- **B:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS) for the Azure Blob container, and create an `ON DATABASE` Extended Events session writing to `package0.event_file`.
- **C:** Incorrect for this requirement. Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps. Why the keyed choice wins: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS) for the Azure Blob container, and create an `ON DATABASE` Extended Events session writing to `package0.event_file`.
- **D:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS) for the Azure Blob container, and create an `ON DATABASE` Extended Events session writing to `package0.event_file`.
- **E:** Correct. Azure SQL Database scopes Extended Event sessions `ON DATABASE` and streams persistent `.xel` ring-rotated files to the Blob container URL. In this scenario: Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `rwl` SAS) for the Azure Blob container, and create an `ON DATABASE` Extended Events session writing to `package0.event_file`.

### Question 94 — C

Answer: Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions. Redefine `IX_Studies_PatientMRN` as a covering nonclustered index with `INCLUDE (AccessionNo, Modality, StudyDate)` (and ensure `@mrn` matches `PatientMRN`'s exact data type to avoid implicit conversion). Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. Local study-map skill 3.8 (Design Covering/Filtered/Columnstore Indexes and Rewrite Non-SARGable or Implicit-Conversion T-SQL Constructs), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Server and Azure SQL index design guide and SARGable T-SQL tuning (https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide).

- **A:** Incorrect for this requirement. Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic. Why the keyed choice wins: Redefine `IX_Studies_PatientMRN` as a covering nonclustered index with `INCLUDE (AccessionNo, Modality, StudyDate)` (and ensure `@mrn` matches `PatientMRN`'s exact data type to avoid implicit conversion).
- **B:** Incorrect for this requirement. `NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP. Why the keyed choice wins: Redefine `IX_Studies_PatientMRN` as a covering nonclustered index with `INCLUDE (AccessionNo, Modality, StudyDate)` (and ensure `@mrn` matches `PatientMRN`'s exact data type to avoid implicit conversion).
- **C:** Correct. Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks. In this scenario: Redefine `IX_Studies_PatientMRN` as a covering nonclustered index with `INCLUDE (AccessionNo, Modality, StudyDate)` (and ensure `@mrn` matches `PatientMRN`'s exact data type to avoid implicit conversion).
- **D:** Incorrect for this requirement. Row-by-row cursors and multi-statement TVFs under legacy compatibility levels execute thousands of iterative context switches and 1-row cardinality guesses. Why the keyed choice wins: Redefine `IX_Studies_PatientMRN` as a covering nonclustered index with `INCLUDE (AccessionNo, Modality, StudyDate)` (and ensure `@mrn` matches `PatientMRN`'s exact data type to avoid implicit conversion).

### Question 95 — A

Answer: Azure SQL Managed Instance (Next-gen General Purpose) with decoupled IOPS and storage sliders. Azure SQL Managed Instance delivers near-100% SQL Server surface-area compatibility—including instance-scoped cross-database queries, SQL Agent, and CLR—inside a managed PaaS virtual cluster. SQL Managed Instance provides near-100% SQL Server engine compatibility (cross-DB queries, SQL Agent, CLR, Service Broker), and Next-gen GP scales IOPS independently of storage up to 500 DBs. Local study-map skill 1.1 (Recommend an Azure SQL Offering (SQL Database, SQL Managed Instance, or SQL Server on Azure VMs)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Compare Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VMs (https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview).

- **A:** Correct. SQL Managed Instance provides near-100% SQL Server engine compatibility (cross-DB queries, SQL Agent, CLR, Service Broker), and Next-gen GP scales IOPS independently of storage up to 500 DBs. In this scenario: Azure SQL Managed Instance delivers near-100% SQL Server surface-area compatibility—including instance-scoped cross-database queries, SQL Agent, and CLR—inside a managed PaaS virtual cluster.
- **B:** Incorrect for this requirement. Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage. Why the keyed choice wins: Azure SQL Managed Instance delivers near-100% SQL Server surface-area compatibility—including instance-scoped cross-database queries, SQL Agent, and CLR—inside a managed PaaS virtual cluster.
- **C:** Incorrect for this requirement. SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint. Why the keyed choice wins: Azure SQL Managed Instance delivers near-100% SQL Server surface-area compatibility—including instance-scoped cross-database queries, SQL Agent, and CLR—inside a managed PaaS virtual cluster.
- **D:** Incorrect for this requirement. Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage. Why the keyed choice wins: Azure SQL Managed Instance delivers near-100% SQL Server surface-area compatibility—including instance-scoped cross-database queries, SQL Agent, and CLR—inside a managed PaaS virtual cluster.

### Question 96 — A

Answer: Managed Instance link using a distributed Availability Group over TCP 5022 for near-zero-downtime online cutover. Managed Instance link establishes a distributed Availability Group over TCP 5022 between SQL Server 2022 and SQL Managed Instance, enabling near-zero-downtime cutover and bidirectional failback on SQL Server 2022. Managed Instance link replicates on-premises or VM SQL Server databases continuously to SQL MI via distributed AG seeding and supports bidirectional planned failover on SQL Server 2022+. Local study-map skill 1.11 (Implement Online and Offline Migrations to and Between Azure SQL Services (`MI Link`, `LRS`, `SqlPackage` Copy)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Online and offline SQL migrations with Managed Instance link, Log Replay Service, and SqlPackage (https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-feature-overview).

- **A:** Correct. Managed Instance link replicates on-premises or VM SQL Server databases continuously to SQL MI via distributed AG seeding and supports bidirectional planned failover on SQL Server 2022+. In this scenario: Managed Instance link establishes a distributed Availability Group over TCP 5022 between SQL Server 2022 and SQL Managed Instance, enabling near-zero-downtime cutover and bidirectional failback on SQL Server 2022.
- **B:** Incorrect for this requirement. Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage. Why the keyed choice wins: Managed Instance link establishes a distributed Availability Group over TCP 5022 between SQL Server 2022 and SQL Managed Instance, enabling near-zero-downtime cutover and bidirectional failback on SQL Server 2022.
- **C:** Incorrect for this requirement. Managed Instance link online failback from SQL MI to SQL Server requires SQL Server 2022 or later; SQL Server 2016 and 2019 support one-way migration into SQL MI only. Why the keyed choice wins: Managed Instance link establishes a distributed Availability Group over TCP 5022 between SQL Server 2022 and SQL Managed Instance, enabling near-zero-downtime cutover and bidirectional failback on SQL Server 2022.
- **D:** Incorrect for this requirement. Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering. Why the keyed choice wins: Managed Instance link establishes a distributed Availability Group over TCP 5022 between SQL Server 2022 and SQL Managed Instance, enabling near-zero-downtime cutover and bidirectional failback on SQL Server 2022.

### Question 97 — A

Answer: Configure `cost threshold for parallelism`, `MAXDOP`, `max server memory (MB)`, and Resource Governor (`WORKLOAD GROUP` + `RESOURCE POOL` + classifier UDF) on SQL MI / VMs. Configure Resource Governor on SQL Managed Instance with a schema-bound classifier function routing `SG-Epidemiology` sessions to a custom `WORKLOAD GROUP` and `RESOURCE POOL` (`CAP_CPU_PERCENT` / `MAX_CPU_PERCENT = 25`). Tuning `cost threshold for parallelism` (e.g., 50) and `MAXDOP` curbs OLTP `CXPACKET` waits, while Resource Governor throttles reporting CPU/memory caps on SQL Server and SQL Managed Instance. Local study-map skill 3.12 (Configure Server Performance Settings (`MAXDOP`, `cost threshold`, `max server memory`) and Resource Governor), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Server configuration options (MAXDOP, memory) and Resource Governor workload isolation (https://learn.microsoft.com/en-us/sql/relational-databases/resource-governor/resource-governor).

- **A:** Correct. Tuning `cost threshold for parallelism` (e.g., 50) and `MAXDOP` curbs OLTP `CXPACKET` waits, while Resource Governor throttles reporting CPU/memory caps on SQL Server and SQL Managed Instance. In this scenario: Configure Resource Governor on SQL Managed Instance with a schema-bound classifier function routing `SG-Epidemiology` sessions to a custom `WORKLOAD GROUP` and `RESOURCE POOL` (`CAP_CPU_PERCENT` / `MAX_CPU_PERCENT = 25`).
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Configure Resource Governor on SQL Managed Instance with a schema-bound classifier function routing `SG-Epidemiology` sessions to a custom `WORKLOAD GROUP` and `RESOURCE POOL` (`CAP_CPU_PERCENT` / `MAX_CPU_PERCENT = 25`).
- **C:** Incorrect for this requirement. Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses. Why the keyed choice wins: Configure Resource Governor on SQL Managed Instance with a schema-bound classifier function routing `SG-Epidemiology` sessions to a custom `WORKLOAD GROUP` and `RESOURCE POOL` (`CAP_CPU_PERCENT` / `MAX_CPU_PERCENT = 25`).
- **D:** Incorrect for this requirement. Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs. Why the keyed choice wins: Configure Resource Governor on SQL Managed Instance with a schema-bound classifier function routing `SG-Epidemiology` sessions to a custom `WORKLOAD GROUP` and `RESOURCE POOL` (`CAP_CPU_PERCENT` / `MAX_CPU_PERCENT = 25`).

### Question 98 — C

Answer: Enable Soft Delete & Purge Protection on Key Vault → Assign Managed Identity to SQL server → Grant Key Vault Crypto Service Encryption User (`get`/`wrapKey`/`unwrapKey`) → Set server TDE protector to Key Vault key. Enable Soft Delete and Purge Protection on Key Vault first, assign a Managed Identity to the SQL server, grant `Key Vault Crypto Service Encryption User` (`get`/`wrapKey`/`unwrapKey`), and set the server TDE protector. Customer-Managed TDE requires Soft Delete and Purge Protection on Key Vault, a server Managed Identity granted `get`/`wrapKey`/`unwrapKey` permissions, and assigning the Key Vault key as TDE protector. Local study-map skill 2.6 (Implement Transparent Data Encryption (`TDE`) with Service-Managed Keys, Key Vault `CMK`, and VM Cert Backups), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Transparent Data Encryption (TDE) with service-managed and customer-managed keys in Key Vault (https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview).

- **A:** Incorrect for this requirement. Incorrect workflow: Azure SQL CMK TDE integrates exclusively with Azure Key Vault or Azure Key Vault Managed HSM using Managed Identity, never anonymous storage URLs. Why the keyed choice wins: Enable Soft Delete and Purge Protection on Key Vault first, assign a Managed Identity to the SQL server, grant `Key Vault Crypto Service Encryption User` (`get`/`wrapKey`/`unwrapKey`), and set the server TDE protector.
- **B:** Incorrect for this requirement. Incorrect workflow: Azure SQL refuses Key Vault TDE protectors unless Soft Delete and Purge Protection are enabled and key-wrapping permissions are granted beforehand. Why the keyed choice wins: Enable Soft Delete and Purge Protection on Key Vault first, assign a Managed Identity to the SQL server, grant `Key Vault Crypto Service Encryption User` (`get`/`wrapKey`/`unwrapKey`), and set the server TDE protector.
- **C:** Correct. Customer-Managed TDE requires Soft Delete and Purge Protection on Key Vault, a server Managed Identity granted `get`/`wrapKey`/`unwrapKey` permissions, and assigning the Key Vault key as TDE protector. In this scenario: Enable Soft Delete and Purge Protection on Key Vault first, assign a Managed Identity to the SQL server, grant `Key Vault Crypto Service Encryption User` (`get`/`wrapKey`/`unwrapKey`), and set the server TDE protector.
- **D:** Incorrect for this requirement. Incorrect workflow: TDE CMK wraps the Database Encryption Key via asymmetric RSA keys in Azure Key Vault or Managed HSM, not `tempdb` symmetric keys. Why the keyed choice wins: Enable Soft Delete and Purge Protection on Key Vault first, assign a Managed Identity to the SQL server, grant `Key Vault Crypto Service Encryption User` (`get`/`wrapKey`/`unwrapKey`), and set the server TDE protector.

### Question 99 — D

Answer: SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage. Apply `ADD SENSITIVITY CLASSIFICATION` (`LABEL`, `INFORMATION_TYPE`) to PHI columns and enable Azure SQL Auditing to Log Analytics / immutable Storage (using audit predicate filtering where server/MI rules apply). `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. Local study-map skill 2.11 (Apply SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) and Server/Database Auditing), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: SQL Data Discovery and Classification and Azure SQL Auditing (https://learn.microsoft.com/en-us/azure/azure-sql/database/auditing-overview).

- **A:** Incorrect for this requirement. Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store. Why the keyed choice wins: Apply `ADD SENSITIVITY CLASSIFICATION` (`LABEL`, `INFORMATION_TYPE`) to PHI columns and enable Azure SQL Auditing to Log Analytics / immutable Storage (using audit predicate filtering where server/MI rules apply).
- **B:** Incorrect for this requirement. `DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls. Why the keyed choice wins: Apply `ADD SENSITIVITY CLASSIFICATION` (`LABEL`, `INFORMATION_TYPE`) to PHI columns and enable Azure SQL Auditing to Log Analytics / immutable Storage (using audit predicate filtering where server/MI rules apply).
- **C:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Apply `ADD SENSITIVITY CLASSIFICATION` (`LABEL`, `INFORMATION_TYPE`) to PHI columns and enable Azure SQL Auditing to Log Analytics / immutable Storage (using audit predicate filtering where server/MI rules apply).
- **D:** Correct. `ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried. In this scenario: Apply `ADD SENSITIVITY CLASSIFICATION` (`LABEL`, `INFORMATION_TYPE`) to PHI columns and enable Azure SQL Auditing to Log Analytics / immutable Storage (using audit predicate filtering where server/MI rules apply).

### Question 100 — C

Answer: Azure SQL Ledger (`LEDGER = ON` append-only or updatable tables) storing SHA-256 database digests in Azure Confidential Ledger and verifying via `sp_verify_database_ledger`. Creating an append-only Ledger table (`WITH (LEDGER = ON (APPEND_ONLY = ON))`) paired with automatic digest storage in Azure Confidential Ledger and verification via `sys.sp_verify_database_ledger` proves cryptographic tamper-evidence. SQL Ledger chains transactional Merkle-tree hashes into tamper-evident blocks stored externally in Azure Confidential Ledger or WORM Blob storage to prove cryptographic integrity to auditors. Local study-map skill 2.14 (Implement Cryptographic Ledger in Azure SQL (`Azure Confidential Ledger`) and Row-Level Security (`FILTER`/`BLOCK`)), aligned to the official DP-300 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300). Primary reference: Ledger cryptographic tamper-evidence and Row-Level Security (RLS) in Azure SQL (https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-overview).

- **A:** Incorrect for this requirement. DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values. Why the keyed choice wins: Creating an append-only Ledger table (`WITH (LEDGER = ON (APPEND_ONLY = ON))`) paired with automatic digest storage in Azure Confidential Ledger and verification via `sys.sp_verify_database_ledger` proves cryptographic tamper-evidence.
- **B:** Incorrect for this requirement. Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload. Why the keyed choice wins: Creating an append-only Ledger table (`WITH (LEDGER = ON (APPEND_ONLY = ON))`) paired with automatic digest storage in Azure Confidential Ledger and verification via `sys.sp_verify_database_ledger` proves cryptographic tamper-evidence.
- **C:** Correct. SQL Ledger chains transactional Merkle-tree hashes into tamper-evident blocks stored externally in Azure Confidential Ledger or WORM Blob storage to prove cryptographic integrity to auditors. In this scenario: Creating an append-only Ledger table (`WITH (LEDGER = ON (APPEND_ONLY = ON))`) paired with automatic digest storage in Azure Confidential Ledger and verification via `sys.sp_verify_database_ledger` proves cryptographic tamper-evidence.
- **D:** Incorrect for this requirement. Append-only Ledger tables strictly block `UPDATE`, `DELETE`, and `TRUNCATE` statements in the SQL engine so cryptographic audit trails cannot be altered. Why the keyed choice wins: Creating an append-only Ledger table (`WITH (LEDGER = ON (APPEND_ONLY = ON))`) paired with automatic digest storage in Azure Confidential Ledger and verification via `sys.sp_verify_database_ledger` proves cryptographic tamper-evidence.
