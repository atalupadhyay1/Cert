"""Canonical option definitions (`TERMS`) for Exam DP-300: Administering Microsoft Azure SQL Solutions.

Every entry maps `key -> (option_label, concise_technical_explanation)`.
Option labels are unique (case-insensitive) and <= 250 characters; zero banned substrings appear.
"""

TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term key: {key}')
    if len(label) > 250:
        raise ValueError(f'{key}: label length {len(label)} > 250')
    if len(meaning) > 360:
        raise ValueError(f'{key}: meaning length {len(meaning)} > 360')
    TERMS[key] = (label, meaning)


# --- Proposed Solution Yes / No Options ---
t(
    'sol_yes',
    'Yes — the proposed configuration satisfies every stated technical, security, and availability requirement',
    'The proposed architecture, T-SQL syntax, and operational parameters satisfy every requirement without violating Azure SQL platform constraints.',
)
t(
    'sol_no_bacpac',
    'No — exporting a `.bacpac` directly from an active OLTP database without copying first is not transactionally consistent',
    '`SqlPackage` exports tables sequentially rather than at a single LSN, so exporting a live write-heavy database without creating a point-in-time copy produces torn foreign-key state.',
)
t(
    'sol_no_ddm_sec',
    'No — Dynamic Data Masking only obfuscates query output and does not encrypt data on disk or block brute-force inference',
    'Dynamic Data Masking is not encryption at rest or row-level access control; users with ad-hoc `WHERE` privileges can still infer masked values unless RLS or encryption is applied.',
)
t(
    'sol_no_srv_fw',
    'No — server-level firewall rules live in `master` and do not replicate automatically to a failover secondary server',
    'Server-level IP firewall rules reside in the logical `master` database and must either be recreated on the DR logical server or replaced with portable database-level rules where appropriate.',
)
t(
    'sol_no_resgov_sqldb',
    'No — Resource Governor is supported on SQL Server and Azure SQL Managed Instance, not single Azure SQL Databases',
    'Single Azure SQL Databases do not expose `CREATE WORKLOAD GROUP` or Resource Governor; compute isolation in SQL Database uses Elastic Pools, Hyperscale named replicas, or separate DBs.',
)
t(
    'sol_no_logdisk_cache',
    'No — transaction log managed disks on SQL Server Azure VMs must use host caching `None`, never `ReadOnly` or `ReadWrite`',
    'SQL Server write-ahead logging performs sequential unbuffered writes; enabling `ReadOnly` or `ReadWrite` host caching on `.ldf` disks degrades throughput or risks corruption.',
)
t(
    'sol_no_det_like',
    'No — standard Deterministic Always Encrypted supports equality (`=`) joins/filters only, never `LIKE` or range predicates',
    'Without a secure enclave (`ALLOW_ENCLAVE_COMPUTATIONS`), Deterministic encryption permits equality comparisons only and rejects `LIKE`, `<`, `>`, or `BETWEEN` predicates.',
)
t(
    'sol_no_full_backup_chain',
    'No — taking an ad-hoc non-`COPY_ONLY` full backup resets the differential base and breaks downstream differential restores',
    'A standard `BACKUP DATABASE` updates the differential base LSN; ad-hoc exports on SQL Managed Instance or Availability Groups must specify `WITH COPY_ONLY` to preserve the backup chain.',
)
t(
    'sol_no_mi_move_pitr',
    'No — moving a database across SQL Managed Instances starts a fresh backup chain and does not carry over prior PITR backups',
    'Online SQL Managed Instance Database Move replicates current data with zero loss, but historical PITR backups remain tied to the source instance and are unavailable on the destination.',
)

# --- Domain 1: Plan and Implement Data Platform Resources ---
t(
    'sqldb_hyperscale',
    'Azure SQL Database Hyperscale tier with compute-isolated Named Replicas',
    'Hyperscale scales up to 100 TB via distributed page servers, performs constant-time log restores, and attaches up to 30 Named Replicas with independent vCore compute over shared storage.',
)
t(
    'sqldb_serverless',
    'Azure SQL Database vCore Serverless compute tier with Auto-pause delay enabled',
    'Serverless auto-scales compute between configured min and max vCores per second and pauses compute billing during idle periods (minimum 1-hour auto-pause delay), charging only storage.',
)
t(
    'sqldb_elastic_pool',
    'Azure SQL Database vCore Elastic Pool with per-database min and max vCore limits',
    'Elastic Pools share a pooled vCore/storage envelope across many multi-tenant databases with staggered peaks while capping per-database max vCores to stop noisy-neighbor starvation.',
)
t(
    'sqlmi_nextgen_gp',
    'Azure SQL Managed Instance (Next-gen General Purpose) with decoupled IOPS and storage sliders',
    'SQL Managed Instance provides near-100% SQL Server engine compatibility (cross-DB queries, SQL Agent, CLR, Service Broker), and Next-gen GP scales IOPS independently of storage up to 500 DBs.',
)
t(
    'sqlmi_bc',
    'Azure SQL Managed Instance Business Critical tier with local SSD storage and built-in read-scale replica',
    'Business Critical SQL MI uses local NVMe SSDs on an Always On availability group quorum for lowest I/O latency, highest IOPS, and one free readable secondary replica.',
)
t(
    'sqlvm_iaas',
    'SQL Server on Azure Virtual Machines (`Ebdsv5` series) with full OS and engine version control',
    'SQL Server on Azure VMs (IaaS) provides full OS access, custom third-party drivers, legacy SQL Server version pinning, SSIS/SSRS/SSAS co-hosting, and `Ebdsv5` high remote storage throughput.',
)
t(
    'sql_linux_containers',
    'SQL Server on Linux configured via `mssql-conf` or Linux container images for consistent CI/CD dev-test parity',
    '`mssql-conf` configures memory, trace flags, Entra auth, and HA on Linux SQL Server VMs, while official Linux container images spin up fast disposable SQL instances in CI pipelines.',
)
t(
    'arc_sql_server',
    'SQL Server enabled by Azure Arc (`Microsoft.AzureArcData/sqlServerInstances`)',
    'Azure Arc projects on-premises and multicloud SQL Server instances into Azure for Resource Graph inventory, automated Best Practices Assessments, Entra auth (SQL 2022+), Defender, and PAYG billing.',
)
t(
    'fabric_sql_db',
    'SQL database in Microsoft Fabric (`Database` workload with automatic OneLake Delta mirroring)',
    'SQL database in Microsoft Fabric runs the Azure SQL engine for OLTP with Microsoft Entra-only auth, automatic near-real-time OneLake Delta Parquet replication, and a read-only SQL analytics endpoint.',
)
t(
    'partition_range_right',
    'Table partitioning using `CREATE PARTITION FUNCTION ... AS RANGE RIGHT` with aligned indexes and `ALTER TABLE ... SWITCH`',
    '`RANGE RIGHT` places each upper-boundary date value cleanly as the lower bound of its own monthly/daily partition, enabling metadata-only `SWITCH` archival when indexes are aligned.',
)
t(
    'sharding_elastic_scale',
    'Horizontal sharding using the Elastic Database Client Library (`ShardMapManager` with `ListShardMap` or `RangeShardMap`)',
    '`ListShardMap` maps discrete `TenantId` keys and `RangeShardMap` maps contiguous ID spans to independent Azure SQL Databases, routing data-dependent connections directly from the app tier.',
)
t(
    'iaas_agent_extension',
    'SQL IaaS Agent Extension in Full management mode paired with Azure Update Manager / Automated Patching',
    'The SQL IaaS Agent Extension unlocks portal license conversion (AHB/PAYG), Automated Backup, Automated Patching windows, Key Vault integration, and storage pool management on SQL VMs.',
)
t(
    'vm_storage_caching',
    'Premium SSD v2 / striped Premium SSD with `ReadOnly` host caching for data disks, `None` for log disks, and `tempdb` on local NVMe',
    'SQL Server Azure VM best practices use `ReadOnly` host caching on `.mdf`/`.ndf` data disks, `None` caching on `.ldf` transaction log disks, and ephemeral NVMe/`D:` storage for `tempdb`.',
)
t(
    'vm_ifi_lpim',
    'Grant `Perform volume maintenance tasks` (Instant File Initialization) and `Lock pages in memory` to the SQL Server service account',
    'Instant File Initialization skips zeroing `.mdf`/`.ndf` data file growth (never `.ldf`), while Lock Pages in Memory prevents Windows from paging the SQL buffer pool to disk.',
)
t(
    'data_compression_est',
    'Evaluate `sp_estimate_data_compression_savings` and apply `ROW`, `PAGE`, or `COLUMNSTORE_ARCHIVE` compression per partition',
    '`sp_estimate_data_compression_savings` models space gains before compressing; `ROW`/`PAGE` shrink OLTP B-trees while `COLUMNSTORE` / `COLUMNSTORE_ARCHIVE` achieves up to 10x analytics compression.',
)
t(
    'azure_migrate_ads',
    'Azure Migrate (`Azure SQL` assessment) and the Azure SQL Migration extension for Azure Data Studio / VS Code',
    'Following Data Migration Assistant (DMA) retirement, Azure Migrate and the Azure SQL Migration extension assess compatibility blockers, feature parity, and performance-based vCore SKU right-sizing.',
)
t(
    'mi_link_online',
    'Managed Instance link using a distributed Availability Group over TCP 5022 for near-zero-downtime online cutover',
    'Managed Instance link replicates on-premises or VM SQL Server databases continuously to SQL MI via distributed AG seeding and supports bidirectional planned failover on SQL Server 2022+.',
)
t(
    'lrs_online_migration',
    'Log Replay Service (`LRS`) streaming Full, Differential, and Tail-Log backups from Azure Blob Storage into SQL Managed Instance',
    '`Start-AzSqlInstanceDatabaseLogReplay` continuously replays `.bak`/`.trn` files from Blob storage until `Complete-AzSqlInstanceDatabaseLogReplay` restores the final tail-log backup.',
)
t(
    'bacpac_copy_export',
    'Create a transactionally consistent database copy (`CREATE DATABASE ... AS COPY OF`), export `.bacpac` via `SqlPackage`, then remove the copy',
    'Creating a point-in-time database copy isolates active OLTP writes so `SqlPackage /Action:Export` produces a foreign-key-consistent `.bacpac` archive in Azure Blob Storage.',
)
t(
    'mi_db_copy_move',
    'Online Azure SQL Managed Instance Database Move / Copy (`TCP 5022` & `11000–11999`, 24-hour manual completion window)',
    'Online MI Database Copy/Move uses Always On seeding across instances/subscriptions; once `Ready for completion`, you have 24 hours to complete (`Move` removes source DB with zero data loss; `Copy` keeps both).',
)

# --- Domain 2: Implement a Secure Environment ---
t(
    'entra_only_auth',
    'Enable Microsoft Entra-only authentication (`azuread_authentication_only`) on the logical SQL server or SQL Managed Instance',
    'Microsoft Entra-only authentication disables legacy SQL Server logins (`sa` and password auth) completely, enforcing centralized MFA, Conditional Access, and token-based Managed Identities.',
)
t(
    'entra_kerberos_mi',
    'Windows Authentication for Azure SQL Managed Instance backed by Microsoft Entra Kerberos (`Incoming Trust`-based or `Entra Kerberos`)',
    'Microsoft Entra Kerberos issues Kerberos tickets for SQL Managed Instance without requiring customer-managed Active Directory Domain Services domain controllers inside Azure.',
)
t(
    'contained_entra_user',
    'Contained database user mapped to a Microsoft Entra security group (`CREATE USER [Group] FROM EXTERNAL PROVIDER`)',
    'Contained Entra group users authenticate directly at the user database without `master` SID mappings, automatically surviving Failover Group / Geo-Replication failovers and onboarding group members.',
)
t(
    'least_priv_server_roles',
    'Built-in granular server-level roles (`##MS_ServerStateReader##`, `##MS_DefinitionReader##`) or `GRANT VIEW DATABASE PERFORMANCE STATE`',
    'Modern granular server roles and state permissions let monitoring accounts inspect DMVs and metadata without granting `sysadmin`, `db_owner`, or `SELECT` access to user tables.',
)
t(
    'module_signing_exec_as',
    'Stored procedure encapsulation using schema ownership chaining, `EXECUTE AS OWNER`, or certificate module signing',
    'Granting `EXECUTE` on a schema-owned or certificate-signed stored procedure lets callers run controlled DML/DDL workflows without direct table-level `SELECT`, `UPDATE`, or `IMPERSONATE` rights.',
)
t(
    'fix_orphaned_users_deny',
    'Remap orphaned database users (`ALTER USER [u] WITH LOGIN = [u]`) and inspect explicit `DENY` permissions via `sys.database_permissions`',
    'Restoring a `.bak` onto another instance mismatches login SIDs (fixed via `ALTER USER ... WITH LOGIN`), while an explicit table/schema `DENY` always overrides `db_datareader` role `GRANT`s.',
)
t(
    'tde_cmk_akv',
    'Transparent Data Encryption (TDE) with a Customer-Managed Key (`CMK`) in Azure Key Vault (`Soft Delete` + `Purge Protection`)',
    'BYOK TDE wraps the symmetric Database Encryption Key (`DEK`) with an asymmetric RSA key in Key Vault or Managed HSM so security admins control key rotation and instant revocation.',
)
t(
    'tde_cert_backup_vm',
    'Back up the TDE encryption certificate and private key (`BACKUP CERTIFICATE ... WITH PRIVATE KEY`) from `master` before restoring onto another SQL Server',
    'Without the original TDE certificate and private key restored into the target SQL Server `master` database, a TDE-encrypted `.bak` or detached `.mdf` cannot be decrypted anywhere.',
)
t(
    'col_sym_encryption_tls',
    'Column-level encryption (`CREATE MASTER KEY` -> `CREATE CERTIFICATE` -> `CREATE SYMMETRIC KEY` -> `EncryptByKey`) plus `Minimal TLS version = 1.2`',
    'T-SQL cell-level symmetric key encryption protects specific columns inside the engine while enforcing TLS 1.2+ encrypts all TDS client traffic in transit.',
)
t(
    'db_firewall_rules',
    'Database-level IP firewall rules (`sys.sp_set_database_firewall_rule`) stored inside the user database',
    'Unlike server-level rules stored in `master`, database-level IP firewall rules travel inside the user database across Active Geo-Replication and Failover Group failovers.',
)
t(
    'ae_deterministic_vs_rand',
    'Always Encrypted (`Randomized` for maximum security with zero equality leakage; `Deterministic` only when `=` joins or `GROUP BY` are required)',
    'Always Encrypted keeps Column Master Keys on trusted clients/Key Vault; `Randomized` produces distinct ciphertexts for identical plaintexts while `Deterministic` enables equality lookups.',
)
t(
    'ae_secure_enclaves',
    'Always Encrypted with VBS or Intel SGX secure enclaves (`ALLOW_ENCLAVE_COMPUTATIONS` + `Column Encryption Setting=Enabled`)',
    'Secure enclaves delegate column decryption into an isolated memory region inside SQL, unlocking `LIKE`, `<`, `>`, `ORDER BY`, and fast in-place initial encryption without exposing plaintext to DBAs.',
)
t(
    'private_endpoint_pls',
    'Azure Private Endpoint (`Microsoft.Network/privateEndpoints`) paired with `privatelink.database.windows.net` Private DNS and `publicNetworkAccess = Disabled`',
    'Private Link maps the SQL server to a private RFC 1918 IP inside your VNet accessible over VPN/ExpressRoute, blocking public internet exposure and cross-tenant data exfiltration.',
)
t(
    'vnet_service_endpoint_mi',
    'Virtual Network Service Endpoints (`Microsoft.Sql`) with outbound storage firewall rules, or dedicated `/28+` delegated subnet for SQL MI',
    'VNet Service Endpoints restrict Azure SQL public endpoint traffic to a specific VNet subnet without private IPs, whereas SQL Managed Instance deploys directly into a dedicated delegated VNet subnet.',
)
t(
    'data_class_sql_audit',
    'SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) integrated with Azure SQL Auditing to Log Analytics / immutable Storage',
    '`ADD SENSITIVITY CLASSIFICATION` tags columns with `LABEL` and `INFORMATION_TYPE`, populating `data_sensitivity_information` in SQL Audit logs whenever classified columns are queried.',
)
t(
    'ct_vs_cdc',
    'Change Tracking (`CHANGETABLE(CHANGES ...)`) for lightweight net PK sync; Change Data Capture (`sys.sp_cdc_enable_table`) for full intermediate before/after history',
    'Change Tracking records only which primary keys changed with minimal overhead, whereas CDC reads the transaction log asynchronously to retain every intermediate `INSERT`/`UPDATE`/`DELETE` payload.',
)
t(
    'ddm_functions_unmask',
    'Dynamic Data Masking (`default()`, `email()`, `partial()`, `random()`) with `GRANT UNMASK` scoped to authorized roles or schemas',
    'DDM masks query result columns on the fly for non-privileged callers (`db_owner` and `UNMASK` holders see cleartext) using built-in masking functions without altering stored values.',
)
t(
    'sql_ledger_acl',
    'Azure SQL Ledger (`LEDGER = ON` append-only or updatable tables) storing SHA-256 database digests in Azure Confidential Ledger and verifying via `sp_verify_database_ledger`',
    'SQL Ledger chains transactional Merkle-tree hashes into tamper-evident blocks stored externally in Azure Confidential Ledger or WORM Blob storage to prove cryptographic integrity to auditors.',
)
t(
    'rls_filter_block',
    'Row-Level Security (`CREATE SECURITY POLICY`) binding a `SCHEMABINDING` inline TVF as both `FILTER PREDICATE` and `BLOCK PREDICATE`',
    'RLS transparently filters `SELECT`/`UPDATE`/`DELETE` rows via `FILTER PREDICATE` and blocks unauthorized cross-tenant `INSERT`/`UPDATE` writes via `BLOCK PREDICATE` inside the engine.',
)

# --- Domain 3: Monitor, Configure, and Optimize Database Resources ---
t(
    'baseline_dm_resource_stats',
    'Azure Monitor metrics paired with `sys.dm_db_resource_stats` (single DB) or `sys.server_resource_stats` (SQL MI) for 15-second CPU, data I/O, log write, and memory baselines',
    '`sys.dm_db_resource_stats` retains 14 days of 15-second resource averages (`avg_cpu_percent`, `avg_data_io_percent`, `avg_log_write_percent`) to compare current peaks against normal baselines.',
)
t(
    'diag_settings_kql',
    'Azure Monitor Diagnostic Settings streaming `SQLInsights`, `QueryStoreRuntimeStatistics`, `Errors`, and `Blocks` to a Log Analytics workspace (`KQL`)',
    'Diagnostic Settings export telemetry across hundreds of databases into Log Analytics so DBAs can correlate `SQLInsights`, wait stats, deadlocks, and timeouts via KQL queries and alerts.',
)
t(
    'db_watcher_fabric_hub',
    'Database watcher streaming SQL DB and SQL MI telemetry into Fabric Eventhouse / Azure Data Explorer (with planned transition to Database Hub in Microsoft Fabric)',
    'Database watcher collects agentless performance telemetry via `VIEW SERVER PERFORMANCE STATE` into KQL stores; Microsoft announced transition to Database Hub in Fabric ahead of April 30, 2027 retirement.',
)
t(
    'xe_event_file_blob',
    'Extended Events (`CREATE EVENT SESSION ... ON DATABASE` in SQL DB or `ON SERVER` in SQL MI/VMs) writing to an `event_file` target in Azure Blob Storage',
    'Unlike ephemeral in-memory `ring_buffer` targets, the `event_file` target persists `.xel` trace files durably in Azure Blob Storage using a database-scoped credential (Managed Identity or SAS).',
)
t(
    'qstore_force_hints',
    'Query Store (`OPERATION_MODE = READ_WRITE`, `QUERY_CAPTURE_MODE = AUTO`) using `sp_query_store_force_plan` and `sp_query_store_set_hints`',
    'Query Store persists plan and runtime/wait telemetry across restarts, allowing DBAs to force a known-good `plan_id` or inject `OPTION (RECOMPILE)` / `MAXDOP` hints without altering app code.',
)
t(
    'rcsi_optimized_locking',
    'Read Committed Snapshot Isolation (`READ_COMMITTED_SNAPSHOT = ON`) combined with Optimized Locking (`TID` locking + Lock After Qualification `LAQ`)',
    '`RCSI` uses row versioning so readers never block writers (`LCK_M_S`), while Optimized Locking in Azure SQL DB replaces thousands of row/page locks with a single Transaction ID lock and `LAQ`.',
)
t(
    'deadlock_xml_fix',
    'Capture `xml_deadlock_report` via Extended Events or `sys.event_log`, align table modification order across transactions, and add covering indexes',
    'Cycle deadlocks (`Error 1205`) occur when concurrent transactions lock objects in opposite order or scan wide ranges; accessing tables in identical order with narrow index seeks eliminates cycles.',
)
t(
    'dmv_wait_stats_diag',
    'Query `sys.dm_os_wait_stats` / `sys.dm_db_wait_stats`, `sys.dm_exec_requests`, `sys.dm_tran_locks`, and `sys.dm_db_tempdb_space_usage`',
    'Wait categories pinpoint root causes: `PAGEIOLATCH_*` indicates storage data reads, `WRITELOG` indicates log flush latency, `SOS_SCHEDULER_YIELD` indicates CPU pressure, and `LCK_M_*` indicates blocking.',
)
t(
    'covering_index_sargable',
    'Create a selective nonclustered covering index (`CREATE NONCLUSTERED INDEX ... INCLUDE (...)`) and rewrite predicates to be SARGable without implicit type conversions',
    'Adding `INCLUDE` columns eliminates expensive `Key Lookup` operators, while removing functions (`YEAR(col)`) and `VARCHAR`/`NVARCHAR` mismatches turns full index scans into fast index seeks.',
)
t(
    'exec_plan_intelligent_insights',
    'Inspect Actual Execution Plans (`Key Lookup`, `TempDB` sort/hash spill warnings, cardinality skew) alongside SQL Intelligent Insights (`SQLInsights`)',
    'Actual Execution Plans expose runtime row vs estimated row skews and `tempdb` spills, while SQL Intelligent Insights automatically compares a 7-day rolling baseline to diagnose regressions.',
)
t(
    'index_stats_checkdb_maint',
    'Fragmentation-aware index maintenance (`REORGANIZE` 5–30%, `REBUILD WITH (ONLINE = ON, RESUMABLE = ON)` >30%), `UPDATE STATISTICS`, and `DBCC CHECKDB WITH PHYSICAL_ONLY`',
    '`RESUMABLE = ON` lets large online index rebuilds pause and resume across maintenance windows; `AUTO_UPDATE_STATISTICS_ASYNC` avoids compile stalls; `PHYSICAL_ONLY` reduces `CHECKDB` I/O overhead.',
)
t(
    'auto_tuning_sqldb',
    'Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN = ON`, `CREATE_INDEX = ON`, `DROP_INDEX = ON`)',
    'Automatic Tuning continuously monitors Query Store, automatically forces prior plans when regressions occur, creates validated missing nonclustered indexes, and removes unused duplicate indexes.',
)
t(
    'res_governor_maxdop',
    'Configure `cost threshold for parallelism`, `MAXDOP`, `max server memory (MB)`, and Resource Governor (`WORKLOAD GROUP` + `RESOURCE POOL` + classifier UDF) on SQL MI / VMs',
    'Tuning `cost threshold for parallelism` (e.g., 50) and `MAXDOP` curbs OLTP `CXPACKET` waits, while Resource Governor throttles reporting CPU/memory caps on SQL Server and SQL Managed Instance.',
)
t(
    'db_scoped_config',
    'Use `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`, `OPTIMIZED_PLAN_FORCING`) per database',
    'Database-scoped configurations isolate optimizer settings (`MAXDOP`, CE version, parameter sniffing) to a single database without affecting sibling databases on SQL MI/VMs or requiring server access.',
)
t(
    'iqp_psp_mgf_udf',
    'Enable compatibility level `160` Intelligent Query Processing (`Parameter Sensitive Plan` optimization, `Memory Grant Feedback` persistence, `Scalar UDF Inlining`, `DOP Feedback`)',
    'SQL 2022 / Azure SQL compat `160` IQP caches multiple active plans per query based on parameter cardinality (`PSP`), right-sizes `tempdb`-spilling memory grants, and inlines scalar T-SQL UDFs.',
)

# --- Domain 4: Configure and Manage Automation of Tasks ---
t(
    'sql_agent_alerts_proxies',
    'SQL Server Agent multi-step jobs using Credentials + Subsystem Proxies, Severity `19–25` / Error `823–825` Alerts, and Database Mail Operators',
    'Least-privilege Agent steps run under Credential-backed Proxies rather than `sysadmin`, while SQL Agent Alerts notify Operators immediately via Database Mail on fatal engine/I/O errors.',
)
t(
    'sql_agent_troubleshoot_mi',
    'Inspect `msdb.dbo.sysjobhistory` / `sp_help_jobhistory`, verify proxy/credential permissions, and account for SQL Managed Instance Agent subsystem boundaries',
    'Job step failures surface in `msdb.dbo.sysjobhistory`; on SQL Managed Instance, Agent runs inside PaaS boundaries where host OS `CmdExec`/ActiveX access is restricted compared to IaaS VMs.',
)
t(
    'bicep_arm_kv_whatif',
    'Declarative Bicep / ARM templates (`Microsoft.Sql/servers`) referencing Azure Key Vault secrets via `@secure()` parameters and validated with `az deployment group what-if`',
    'Bicep compiles to idempotent ARM JSON, injects secrets directly from Key Vault without exposing plaintext in CI logs, and previews resource mutations safely via `what-if` before execution.',
)
t(
    'pwsh_azcli_sql',
    'Idempotent day-2 scripting with Azure PowerShell (`New-AzSqlDatabase`, `Set-AzSqlElasticPool`) or Azure CLI (`az sql db update`, `az sql mi update`)',
    '`Az.Sql` cmdlets and `az sql` CLI commands automate repeatable provisioning, tier/vCore scaling, failover triggers, and firewall/backup updates from DevOps pipelines or shell scripts.',
)
t(
    'troubleshoot_arm_mi_subnet',
    'Diagnose deployment failures via `Get-AzResourceGroupDeploymentOperation` / Activity Log `CorrelationId`, checking regional vCore quotas and SQL MI subnet delegation/NSG/UDR rules',
    'SQL Managed Instance deployments fail most commonly when the subnet lacks `/28+` IP space, `Microsoft.Sql/managedInstances` delegation, route table (`0.0.0.0/0` NextHop `Internet`), or regional vCore quota.',
)
t(
    'elastic_jobs_uami',
    'Azure SQL Database Elastic Job Agent (`jobs.sp_add_job`) authenticating to Target Groups across servers/pools via a User-Assigned Managed Identity (`UAMI`)',
    'Elastic Jobs fan out T-SQL maintenance and schema scripts asynchronously across hundreds of Azure SQL Databases, elastic pools, and subscriptions using passwordless UAMI authentication.',
)
t(
    'azure_automation_runbooks',
    'Azure Automation PowerShell / Python runbooks (or Azure Functions / Logic Apps) using a System-Assigned Managed Identity on a recurring schedule',
    'Azure Automation runbooks authenticate via Managed Identity (`Connect-AzAccount -Identity`) to scale vCores/Elastic Pools on schedule, rotate keys, or orchestrate hybrid maintenance via Hybrid Workers.',
)
t(
    'monitor_alerts_elastic_diag',
    'Configure Azure Monitor Metric / Log Alert rules routed to Action Groups and query `jobs.job_executions` in the Elastic Job database to diagnose step failures',
    'Action Groups dispatch email/SMS/webhook/Logic App notifications when alert thresholds fire, while `jobs.job_executions` exposes per-target error messages, retries, and timeouts for Elastic Jobs.',
)

# --- Domain 5: Plan and Configure a High Availability and Disaster Recovery (HA/DR) Environment ---
t(
    'hadr_rpo_rto_matrix',
    'Align tiers to RPO/RTO: `Zone Redundant` (`RPO = 0` intra-region HA), `Failover Groups` (`RPO = 5s`, `RTO = 1h` SLA cross-region DR), vs `Geo-Restore` (`RPO = 1h`, `RTO = 12h`)',
    'Zone Redundancy survives datacenter zone loss with zero data loss; Failover Groups / Active Geo-Replication provide low-RPO/RTO regional DR; Geo-Restore is lowest-cost DR from RA-GRS backups.',
)
t(
    'hybrid_hadr_mi_link_2022',
    'Hybrid DR using Managed Instance link with bidirectional online failover between SQL Server 2022 and Azure SQL Managed Instance',
    'SQL Server 2022 supports two-way online planned failover back and forth with Azure SQL Managed Instance via Managed Instance link (whereas SQL Server 2016–2019 link failover is one-way to Azure).',
)
t(
    'dr_drill_planned_failover',
    'Non-disruptive DR readiness drill executing a planned zero-data-loss Failover Group switch (`Switch-AzSqlDatabaseFailoverGroup`), validating app listeners, and failing back',
    'Planned failover synchronizes pending log records before switching roles (`RPO = 0`), validating secondary firewall/Entra configs and `<fog>.database.windows.net` DNS redirection safely.',
)
t(
    'copy_only_azure_backup_vm',
    'Use `BACKUP DATABASE ... WITH COPY_ONLY` for ad-hoc exports on SQL MI / AGs, and Azure Backup Recovery Services Vault SQL-aware policies (`15-min` log RPO) on SQL VMs',
    '`COPY_ONLY` preserves the differential and log backup chain, while Azure Backup for SQL Server in Azure VMs automates application-consistent Full, Differential, and 15-minute Transaction Log backups.',
)
t(
    'pitr_adr_deleted_restore',
    'Automated Point-in-Time Restore (`1–35` days PITR), Deleted-Database restore from the logical server, and Accelerated Database Recovery (`ADR`) instant rollback',
    'Azure SQL DB/MI retains automated backups for `1–35` days (`STOPAT`-equivalent PITR even if a DB was deleted within retention), while `ADR` uses a Persistent Version Store for instant rollback.',
)
t(
    'ltr_immutable_worm',
    'Long-Term Retention (`LTR`) weekly/monthly/yearly backups up to `10 years` protected by a locked time-based immutable (`WORM`) policy and `RA-GRS` / `ZRS` backup storage',
    'LTR retains compliance backups up to 10 years independently of PITR, and locking time-based immutability prevents even Subscription Owners from deleting backups before expiry.',
)
t(
    'backup_to_url_striped',
    'Striped T-SQL `BACKUP DATABASE ... TO URL = ...` across up to 64 block blobs (`MAXTRANSFERSIZE`, `COMPRESSION`) authenticated via `Managed Identity` or `SHARED ACCESS SIGNATURE` Credential',
    'Backing up to multiple URLs creates block blobs supporting up to ~12.8 TB striped backups (`200 GB+` per blob, unlike legacy single-page-blob 1 TB limits) using `CREATE CREDENTIAL`.',
)
t(
    'failover_group_vs_active_geo',
    'Failover Groups for automatic multi-database failover behind stable `<fog>.database.windows.net` / `.secondary` listeners vs Active Geo-Replication for up to 4 readable secondaries',
    'Failover Groups fail over coupled databases together and redirect connection strings automatically (`GracePeriodWithDataLossHours >= 1`), whereas Active Geo-Replication supports up to 4 secondaries per DB without automatic listener redirection.',
)
t(
    'ag_azure_vm_dnn_ilb',
    'Always On Availability Group on Azure VMs using WSFC with Azure Cloud Witness, Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` port `59999`), and `MultiSubnetFailover=True`',
    'Cloud Witness provides low-cost Blob quorum without a third VM; `DNN` routes multi-subnet AG traffic via DNS without ILB failover delay (requiring `MultiSubnetFailover=True` in client drivers).',
)
t(
    'fci_shared_disks_logship',
    'Always On Failover Cluster Instance (`FCI`) on Azure VMs backed by `ZRS` Premium SSD Azure Shared Disks (or `S2D`), or Log Shipping (`BACKUP LOG` -> copy -> `RESTORE LOG WITH NORECOVERY`/`STANDBY`)',
    'Azure Shared Disks provide native SCSI PR shared block storage across Availability Zones for instance-level FCI failover, whereas Log Shipping maintains warm DR secondaries via scheduled `.trn` restores.',
)
t(
    'hadr_dmv_troubleshoot',
    'Query `sys.dm_hadr_database_replica_states` (`synchronization_state_desc`, `log_send_queue_size`, `redo_queue_size`) and `sys.dm_geo_replication_link_status`, plus verify NSG probe port `59999`',
    'High `log_send_queue_size` indicates network bottlenecks between primary and secondary, high `redo_queue_size` indicates slow redo I/O/CPU or long-running read queries on the secondary, and blocked ILB probe port `59999` breaks AG listener routing.',
)

# --- High-Signal Plausible Distractors (Wrong Tools, Anti-Patterns & Retired Options) ---
t(
    'bad_dma_retired',
    'Download and run standalone Microsoft Data Migration Assistant (`DMA`) with Stretch Database enabled for warm archive tables',
    'Both standalone Data Migration Assistant (retired July 2025) and SQL Server Stretch Database (retired) are deprecated; use Azure Migrate / Azure SQL Migration extension and partitioning/Fabric/Blob tiering.',
)
t(
    'bad_dtu_basic_14tb',
    'Azure SQL Database DTU `Basic` or `Standard S0` tier with a single shared primary replica',
    'DTU Basic supports max 2 GB and Standard S0–S2 max 250 GB without compute-isolated read replicas, making them incapable of hosting multi-TB OLTP workloads.',
)
t(
    'bad_sql_profiler_prod',
    'Attach legacy SQL Server Profiler GUI (`sp_trace_create`) interactively against peak production OLTP servers 24x7',
    'Interactive SQL Server Profiler GUI tracing imposes heavy observer overhead and is deprecated in favor of lightweight Extended Events and Query Store.',
)
t(
    'bad_shrinkdatabase_nightly',
    'Schedule nightly `DBCC SHRINKDATABASE` and `AUTO_SHRINK = ON` across all production OLTP databases',
    '`DBCC SHRINKDATABASE` and `AUTO_SHRINK` cause massive physical index fragmentation (`>90%`), heavy transaction log generation, and immediate file regrow stalls.',
)
t(
    'bad_sa_sysadmin_shared',
    'Enable Mixed Mode, share the `sa` login password in plaintext pipeline variables, and add monitoring users to `sysadmin`',
    'Sharing `sa` credentials or granting `sysadmin` violates least privilege, bypasses auditing attribution, and fails Microsoft Entra-only zero-password compliance.',
)
t(
    'bad_public_0000_firewall',
    'Add server-level firewall rule `0.0.0.0` to `255.255.255.255` and disable TLS encryption on client connections',
    'Opening `0.0.0.0–255.255.255.255` exposes the SQL endpoint to the entire public internet rather than isolating traffic via Private Endpoints or scoped IP rules.',
)
t(
    'bad_tempdb_os_disk',
    'Place SQL Server `.mdf`, `.ldf`, and `tempdb` files together on the Azure VM OS disk (`C:`) with `ReadWrite` host caching',
    'Placing database or log files on `C:` or enabling `ReadWrite` caching risks data corruption during host crashes and exhausts OS disk IOPS caps.',
)
t(
    'bad_fabric_sql_auth',
    'Configure SQL Server password logins (`CREATE LOGIN ... WITH PASSWORD`) and T-SQL `BACKUP DATABASE ... TO DISK` inside SQL database in Microsoft Fabric',
    'SQL database in Microsoft Fabric enforces Microsoft Entra authentication exclusively (SQL logins are unsupported) and manages backups/OneLake mirroring automatically as SaaS.',
)
t(
    'bad_nolock_dirty_reads',
    'Add `WITH (NOLOCK)` or `READ UNCOMMITTED` table hints to every financial and clinical `SELECT` query to eliminate blocking',
    '`NOLOCK` (`READ UNCOMMITTED`) permits dirty reads of uncommitted rolled-back rows, double-counting rows, or skipping committed rows during page splits—unacceptable for accurate OLTP.',
)
t(
    'bad_freeproccache_cron',
    'Run `DBCC FREEPROCCACHE` every 5 minutes via a cron job and disable `AUTO_CREATE_STATISTICS` across the database',
    'Flushing the entire plan cache repeatedly causes CPU compilation storms across all queries, and disabling statistics forces blind cardinality guesses.',
)
t(
    'bad_index_every_column',
    'Create 25 overlapping single-column nonclustered indexes on every table column and rebuild all indexes with `ONLINE = OFF` at noon',
    'Over-indexing inflates every `INSERT`/`UPDATE`/`DELETE` write and log flush, while `ONLINE = OFF` holds exclusive schema/table locks that block production traffic.',
)
t(
    'bad_cdc_sqldb_basic',
    'Enable Change Data Capture (`CDC`) on DTU `Basic`/`S0–S2` databases or expect Change Tracking (`CT`) to retain every intermediate `UPDATE` value',
    'CDC requires `S3+` or `vCore` tiers in Azure SQL Database, and Change Tracking stores only net version numbers/PKs—never intermediate before/after column values.',
)
t(
    'bad_geo_restore_5sec',
    'Rely solely on Geo-Restore from `RA-GRS` automated backups to meet a 5-second RPO and 60-second automatic failover RTO SLA',
    'Geo-Restore downloads and restores geo-replicated backups into a new server with an RPO of up to 1 hour and RTO of up to 12 hours, never automatic 5-second RPO failover.',
)
t(
    'bad_mi_link_twoway_2016',
    'Expect online bidirectional planned failback from Azure SQL Managed Instance directly back to on-premises SQL Server 2016 without downtime',
    'Managed Instance link online failback from SQL MI to SQL Server requires SQL Server 2022 or later; SQL Server 2016 and 2019 support one-way migration into SQL MI only.',
)
t(
    'bad_ag_single_vm_no_witness',
    'Deploy a 2-node Always On Availability Group in a single Availability Set without any quorum witness and block TCP `59999` on the NSG',
    'A 2-node WSFC without a Cloud/File-Share Witness loses quorum if one node fails, and blocking Azure ILB health-probe port `59999` blackholes AG listener connections.',
)
t(
    'bad_page_blob_striped_64',
    'Back up a 6 TB database to a single unstriped Azure Page Blob URL (`WITH CREDENTIAL` omitted) using anonymous public container access',
    'A single Page Blob `BACKUP TO URL` maxes out at 1 TB and requires a SQL Credential; multi-TB cloud backups must stripe across multiple Block Blob URLs.',
)
t(
    'bad_ltr_pitr_confused',
    'Set Short-Term PITR retention to `3,650` days (`10 years`) and grant developers Subscription Contributor to prevent backup deletion',
    'Short-Term PITR caps at `35` days (`1–35` days); multi-year retention up to `10 years` with WORM deletion lock requires Long-Term Retention (`LTR`) with time-based immutability.',
)
t(
    'bad_ledger_alter_drop',
    'Truncate or `DELETE` historical rows from an append-only Ledger table (`LEDGER = ON (APPEND_ONLY = ON)`) to purge audit history in place',
    'Append-only Ledger tables strictly block `UPDATE`, `DELETE`, and `TRUNCATE` statements in the SQL engine so cryptographic audit trails cannot be altered.',
)
t(
    'bad_scalar_udf_cursor',
    'Replace set-based `JOIN` queries with nested `FAST_FORWARD` T-SQL cursors calling multi-statement table-valued functions per row under compat `100`',
    'Row-by-row cursors and multi-statement TVFs under legacy compatibility levels execute thousands of iterative context switches and 1-row cardinality guesses.',
)
t(
    'bad_elastic_job_sql_agent_db',
    'Start the built-in `SQLServerAgent` Windows service inside a single Azure SQL Database and store target server passwords in a public GitHub repo',
    'Single Azure SQL Databases do not expose `SQLServerAgent`; cross-database PaaS scheduling uses Elastic Job Agents with Managed Identity or Azure Automation.',
)

# --- Atomic Multi-Select & Single-Choice Configuration Building Blocks ---
# Domain 1 atomic blocks
t(
    'arc_resource_graph',
    'Query fleet-wide SQL Server version, edition, and backup status across hybrid servers via Azure Resource Graph Explorer',
    'SQL Server enabled by Azure Arc projects on-premises and multicloud instance metadata into Azure Resource Manager for KQL-based Azure Resource Graph inventory queries.',
)
t(
    'arc_best_practices',
    'Enable automated SQL Best Practices Assessments and Microsoft Defender for SQL via the Azure Arc SQL Server extension',
    'The Azure Extension for SQL Server runs recurring configuration assessments against Microsoft Support rules and integrates Defender vulnerability/threat detection.',
)
t(
    'arc_payg_billing',
    'Switch eligible hybrid SQL Server instances to hourly Azure Arc pay-as-you-go billing instead of upfront core licenses',
    'Azure Arc allows variable-workload or seasonal SQL Server hosts outside Azure to be billed hourly through an Azure subscription.',
)
t(
    'fabric_sql_entra_only',
    'Authenticate applications and users exclusively with Microsoft Entra ID identities, service principals, or workspace roles',
    'SQL database in Microsoft Fabric relies exclusively on Microsoft Entra authentication and workspace/item permissions rather than SQL logins.',
)
t(
    'fabric_sql_onelake_delta',
    'Query automatically replicated OneLake Delta Parquet tables and the read-only SQL analytics endpoint from Spark and Direct Lake',
    'Every SQL database in Microsoft Fabric automatically mirrors operational tables into OneLake in Delta Parquet format and exposes a SQL analytics endpoint.',
)
t(
    'mi_subnet_delegation',
    'Create a dedicated VNet subnet (`/28` or larger) with no other cloud resources and delegate it to `Microsoft.Sql/managedInstances`',
    'Azure SQL Managed Instance requires an exclusive subnet delegated to `Microsoft.Sql/managedInstances` sized for current and future instance vCore/node counts.',
)
t(
    'mi_subnet_route_table',
    'Associate a User-Defined Route (`UDR`) table (`0.0.0.0/0` -> `Internet` for management plane) and required NSG rules with the SQL MI subnet',
    'SQL Managed Instance requires an explicit route table and NSG bound to its delegated subnet so Azure management traffic is never blackholed by forced tunneling.',
)
t(
    'vm_readonly_data_cache',
    'Configure `ReadOnly` Azure host caching on Premium SSD data disks hosting `.mdf` and `.ndf` database files',
    '`ReadOnly` host caching serves random OLTP data-page reads directly from Azure hypervisor RAM/SSD cache without consuming disk IOPS.',
)
t(
    'vm_none_log_cache',
    'Configure `None` Azure host caching on dedicated managed disks hosting `.ldf` SQL Server transaction log files',
    'Transaction log files perform sequential write-through flushes that do not benefit from read caching and must use `None` host caching.',
)
t(
    'vm_tempdb_nvme',
    'Place `tempdb` data and log files (8 equal-sized `.mdf`/`.ndf` files) on the ephemeral local NVMe SSD volume with a startup folder-creation script',
    'Local ephemeral NVMe storage delivers ultra-low latency for `tempdb` spills and version stores without consuming remote disk IOPS bandwidth.',
)

# Domain 2 atomic blocks
t(
    'akv_soft_delete_purge',
    'Enable both `Soft Delete` and `Purge Protection` on the Azure Key Vault or Managed HSM storing the TDE protector key',
    'Azure SQL requires both Soft Delete and Purge Protection on Key Vault so accidental or malicious key deletion can never permanently brick encrypted databases.',
)
t(
    'akv_wrap_unwrap_rbac',
    'Grant the SQL server Managed Identity `Key Vault Crypto Service Encryption User` (`get`, `wrapKey`, `unwrapKey`) on the Key Vault',
    'The logical SQL server or SQL MI Managed Identity requires `get`, `wrapKey`, and `unwrapKey` permissions to wrap and unwrap the Database Encryption Key (`DEK`).',
)
t(
    'rls_schemabinding_tvf',
    'Create an inline table-valued function `WITH SCHEMABINDING` evaluating `SESSION_CONTEXT()` or `DATABASE_PRINCIPAL_ID()`',
    'RLS predicate functions must be inline TVFs bound with `SCHEMABINDING` so underlying columns cannot be altered silently and query plans inline cleanly.',
)
t(
    'rls_filter_predicate',
    'Add a `FILTER PREDICATE` in `CREATE SECURITY POLICY` to hide non-matching rows silently from `SELECT`, `UPDATE`, and `DELETE`',
    '`FILTER PREDICATE` injects the security TVF into read, update, and delete operators transparently without changing application `SELECT` statements.',
)
t(
    'rls_block_predicate',
    'Add `AFTER INSERT` and `AFTER UPDATE` / `BEFORE UPDATE` `BLOCK PREDICATE` clauses in `CREATE SECURITY POLICY` (`STATE = ON`)',
    '`BLOCK PREDICATE` raises an error if a shared application login attempts to insert or update a row carrying another tenant\'s identifier.',
)
t(
    'ae_cmk_cek_enclave',
    'Provision a Column Master Key in Key Vault and create a Column Encryption Key with `ENCLAVE_COMPUTATIONS` enabled',
    'Rich confidential queries (`LIKE`, `<`, `>`, sorting) and in-place encryption require a CEK explicitly marked to permit enclave computations.',
)
t(
    'ae_client_conn_enclave',
    'Enable `Column Encryption Setting=Enabled` and pass the `Enclave Attestation Url` (or VBS zero-attestation setting) in client drivers',
    'Client drivers must enable Always Encrypted and verify enclave attestation before transmitting CEKs over TLS into the SQL secure enclave.',
)
t(
    'pls_private_dns_zone',
    'Link Private DNS Zone `privatelink.database.windows.net` (or forward on-premises DNS) to resolve `<server>.database.windows.net` to the private IP',
    'Clients still validate the TLS certificate for `<server>.database.windows.net`, so split-brain DNS must map the canonical FQDN via CNAME to `privatelink.database.windows.net`.',
)
t(
    'pls_disable_public_net',
    'Set `Public network access = Disabled` (`publicNetworkAccess: Disabled`) on the logical SQL server so internet connections are rejected',
    'Creating a Private Endpoint alone leaves the public endpoint reachable unless `Public network access` is explicitly disabled on the server.',
)

# Domain 3 atomic blocks
t(
    'qs_force_plan_proc',
    'Execute `sys.sp_query_store_force_plan @query_id, @plan_id` to pin the historical low-latency execution plan immediately',
    '`sp_query_store_force_plan` instructs the optimizer to compile plans matching the forced `plan_id` shape without modifying application T-SQL.',
)
t(
    'qs_set_hints_proc',
    'Execute `sys.sp_query_store_set_hints @query_id, N\'OPTION (RECOMPILE)\'` (or `MAXDOP` / memory grant hints) without redeploying code',
    'Query Store hints attach `OPTION (...)` query hints directly to a `query_id` in Azure SQL DB, SQL MI, and SQL Server 2022+ when app code cannot be edited.',
)
t(
    'dbwatcher_uami_perm',
    'Grant the database watcher Managed Identity `VIEW SERVER PERFORMANCE STATE` (or `VIEW DATABASE PERFORMANCE STATE`) on SQL targets',
    'Database watcher collects DMVs and system catalogs using least-privilege performance-state permissions rather than `sysadmin` or data-read rights.',
)
t(
    'dbwatcher_adx_eventhouse',
    'Grant the database watcher Managed Identity database `Admin` / ingest permissions on the Azure Data Explorer or Fabric Eventhouse store',
    'Database watcher creates tables, retention policies, and ingestion mappings inside the target Azure Data Explorer or Fabric Real-Time Analytics KQL database.',
)
t(
    'xe_cred_blob_container',
    'Create a `DATABASE SCOPED CREDENTIAL` (`Managed Identity` or `SHARED ACCESS SIGNATURE` with `rwl` permissions) for the Azure Blob container',
    'Extended Events in Azure SQL Database requires a `DATABASE SCOPED CREDENTIAL` with Read, Write, and List rights on the target Blob Storage container.',
)
t(
    'xe_event_file_target',
    'Define `CREATE EVENT SESSION ... ON DATABASE ADD TARGET package0.event_file(SET filename = N\'https://...xel\')` and start the session',
    'Azure SQL Database scopes Extended Event sessions `ON DATABASE` and streams persistent `.xel` ring-rotated files to the Blob container URL.',
)
t(
    'maint_resumable_online',
    'Run `ALTER INDEX ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON, MAX_DURATION = 90 MINUTES)` for heavily fragmented (`>30%`) indexes',
    'Resumable online index rebuilds persist progress in place, bound transaction log growth, and automatically pause at `MAX_DURATION` so later windows can `RESUME`.',
)
t(
    'maint_async_stats',
    'Enable `AUTO_UPDATE_STATISTICS_ASYNC = ON` and schedule targeted `UPDATE STATISTICS` jobs so user queries do not stall waiting on sampling',
    'Asynchronous statistics updates let incoming OLTP queries execute immediately with existing stats while a background thread refreshes stale histograms.',
)
t(
    'maint_physical_only_checkdb',
    'Run `DBCC CHECKDB WITH PHYSICAL_ONLY` during off-peak windows or offload full `DBCC CHECKDB` onto a restored backup replica',
    '`PHYSICAL_ONLY` checks page checksums, torn pages, and allocation structures at a fraction of full logical `CHECKDB` CPU/memory cost.',
)
t(
    'iqp_psp_opt',
    'Leverage Parameter Sensitive Plan (`PSP`) optimization under compatibility level `160` to cache separate plans for skewed parameter sizes',
    'PSP optimization generates up to three active dispatcher query variants so small lookups use Index Seeks while massive skews use Parallel Scans.',
)
t(
    'iqp_mem_grant_feedback',
    'Leverage Percentile and Persistence Memory Grant Feedback (`compat 160`) to eliminate recurring `tempdb` sort/hash spills and wasted RAM',
    'Memory Grant Feedback adjusts overestimated or underestimated query memory grants across executions and persists learned grants in Query Store.',
)
t(
    'iqp_scalar_udf_inlining',
    'Leverage Scalar UDF Inlining (`compat 150+`) so eligible T-SQL scalar functions fold into relational subqueries enabling parallel plans',
    'Scalar UDF Inlining transforms row-by-row T-SQL scalar function invocations into set-based relational operators that no longer block parallelism.',
)

# Domain 4 atomic blocks
t(
    'bicep_secure_kv_ref',
    'Mark sensitive parameters with `@secure()` in Bicep and pass Key Vault secret references from the parameter file rather than cleartext values',
    '`@secure()` prevents secret logging in deployment history, while Key Vault references resolve secrets inside ARM at deploy time without exposing them to CI runners.',
)
t(
    'bicep_whatif_preview',
    'Run `az deployment group what-if` (or `New-AzResourceGroupDeployment -WhatIf`) as a pull-request gate before applying template changes',
    '`what-if` calculates predicted `Create`, `Modify`, `Delete`, and `Ignore` operations against live Azure SQL resources to catch destructive config drift.',
)
t(
    'ej_uami_contained_user',
    'Assign a User-Assigned Managed Identity to the Elastic Job Agent and create a contained `FROM EXTERNAL PROVIDER` user on target databases',
    'Modern Elastic Jobs authenticate across Azure SQL servers and subscriptions using a User-Assigned Managed Identity without managing SQL credential passwords.',
)
t(
    'ej_target_group_pools',
    'Add logical SQL servers or Elastic Pools (`include` / `exclude` members) to an Elastic Job Target Group so new tenant DBs inherit jobs automatically',
    'Targeting at the server or Elastic Pool level dynamically discovers newly created tenant databases on each job run without editing job definitions.',
)
t(
    'agent_credential_proxy',
    'Create a Windows/SQL Credential and map it to a SQL Server Agent Subsystem Proxy (`CmdExec` / `PowerShell`) instead of granting `sysadmin`',
    'SQL Server Agent proxies let non-`sysadmin` job owners execute external subsystem steps under a scoped least-privilege identity.',
)
t(
    'agent_severity_dbmail',
    'Configure Database Mail, define an Agent Operator, and create SQL Server Agent Alerts for Severity `19–25` and Errors `823`, `824`, and `825`',
    'Severity `19–25` and I/O errors `823–825` indicate critical resource exhaustion or storage corruption requiring immediate DBA notification.',
)

# Domain 5 atomic blocks
t(
    'fog_listeners_rw_ro',
    'Connect OLTP write traffic to `<fog>.database.windows.net` and read-only analytics to `<fog>.secondary.database.windows.net`',
    'Failover Group listener endpoints abstract underlying regional server names and automatically redirect read-write and read-only connections after failover.',
)
t(
    'fog_grace_period_hours',
    'Configure `ReadWriteFailoverPolicy = Automatic` with `GracePeriodWithDataLossHours >= 1` so transient blips do not trigger premature lossy failover',
    'The grace period controls how long Azure waits during an unrecoverable primary region outage before forcing an automatic failover if async log lag remains.',
)
t(
    'ag_cloud_witness',
    'Configure an Azure Cloud Witness in a standard Storage Account (`LRS`/`ZRS`) to provide lightweight quorum voting for a 2-node WSFC',
    'Cloud Witness maintains a tiny blob arbitration file without the cost and patching overhead of running a third witness VM.',
)
t(
    'ag_multisubnetfailover_true',
    'Deploy a Distributed Network Name (`DNN`) or Internal Load Balancer (`ILB` TCP `59999`) listener and set `MultiSubnetFailover=True` on clients',
    '`MultiSubnetFailover=True` makes SQL client drivers try all listener IPs in parallel across subnets, cutting cross-subnet AG failover reconnect latency to seconds.',
)
t(
    'url_cred_managed_id',
    'Create a SQL Server `CREDENTIAL` (`IDENTITY = \'Managed Identity\'` or `\'SHARED ACCESS SIGNATURE\'`) matching the Azure Blob container URL',
    'SQL Server and SQL MI authenticate `BACKUP TO URL` / `RESTORE FROM URL` requests to Azure Storage via a server-level credential.',
)
t(
    'url_multi_blob_stripe',
    'Stripe `BACKUP DATABASE` across multiple `TO URL = \'https://...bak\'` block blob targets with `COMPRESSION` and `MAXTRANSFERSIZE = 4194304`',
    'Multiple `URL` targets write to Azure Block Blobs in parallel, scaling single backups up to ~12.8 TB (`64` stripes) with maximum throughput.',
)
t(
    'ltr_schedule_policy',
    'Configure an Azure SQL Long-Term Retention (`LTR`) policy (`WeeklyRetention`, `MonthlyRetention`, `YearlyRetention`, `WeekOfYear`) up to 10 years',
    'LTR copies full backups into separate geo-redundant/zone-redundant Azure Blob tiers according to ISO-8601 duration policies (e.g., `P7Y`).',
)
t(
    'ltr_time_immutability',
    'Enable and lock time-based immutability (`WORM`) on the LTR backup policy so nobody can shorten retention or delete compliance backups early',
    'Once locked, time-based LTR immutability enforces write-once-read-many protection against ransomware or rogue privileged admins.',
)

