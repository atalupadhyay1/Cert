# Exam DP-300 Case Study Briefs (Sets 1–6)

Every mock exam contains 4 original Azure SQL Database Administration case studies of 3 questions (12 items per set, 24 scenarios total). Paste the relevant scenario into a Udemy practice-test description if uploading `practice-set-N.csv`, or upload `case-embedded-set-N.csv` where each case stem embeds the full scenario directly.

## Exam 1: Omnichannel E-Commerce, Hyperscale Read-Scale, and Hybrid Azure Arc Retail

### Case study — BrambleBox Stores

BrambleBox Stores operates 320 SQL Server 2022 instances on Windows and Linux servers across regional distribution warehouses outside Azure. Leadership wants a single Azure portal inventory, automated SQL Best Practices Assessments, centralized Microsoft Entra authentication, and hourly pay-as-you-go billing.

Questions in this block:

1. You onboard all 320 warehouse SQL Server 2022 instances to Azure Arc. Which three management and licensing capabilities become available from the Azure control plane? Select three. _(A, D, F)_
2. Regional warehouse servers must remain in on-premises racks for local scanner sub-millisecond latency while using Microsoft Entra authentication on SQL Server 2022. Which hybrid service enables Microsoft Entra authentication on those non-Azure hosts? _(A)_
3. Leadership decides to migrate 12 back-office SQL Server 2016 instances into Azure SQL PaaS and wants automated feature-blocker detection plus performance-based vCore SKU sizing. Which modern Microsoft toolset should you run? _(D)_

### Case study — HarborPick Fulfillment

HarborPick Fulfillment runs high-concurrency warehouse picking on Azure SQL Database. After a nightly batch skews inventory counts, a critical stored procedure regresses to a slow nested-loops plan, reader sessions wait behind `LCK_M_S` writer locks, and schema maintenance must run across 35 regional databases.

Questions in this block:

1. Which two built-in Query Store stored procedures let you immediately stabilize the regressed warehouse-picking query without modifying or redeploying application code? Select two. _(A, E)_
2. Which database concurrency features eliminate `LCK_M_S` reader waits behind writers and replace thousands of row locks with a single Transaction ID (`TID`) lock without permitting dirty reads? _(A)_
3. You must roll out DDL schema updates and index maintenance across all 35 regional Azure SQL Databases passwordlessly, automatically including new regional databases added later. Which two Elastic Job configurations should you use? Select two. _(A, C)_

### Case study — KestrelCart Commerce

KestrelCart Commerce runs a 14 TB multi-region order database in Azure SQL Database experiencing rapid seasonal growth, bursty BI read traffic from three analytics teams that must be compute-isolated from OLTP checkouts, and 18 non-production staging databases that sit idle every night and weekend.

Questions in this block:

1. Which Azure SQL Database service tier and read-scale feature should you recommend for the 14 TB primary order database so three analytics teams get isolated vCore compute over shared storage? _(C)_
2. Which Azure SQL Database compute configuration minimizes compute cost for the 18 non-production staging databases that sit completely idle every night and weekend? _(C)_
3. You partition `OrderHistory` monthly on `OrderTimestamp DATETIME2` using `CREATE PARTITION FUNCTION pf_Month (DATETIME2) AS RANGE ____ FOR VALUES ('2026-01-01', '2026-02-01')` so midnight `'2026-01-01 00:00:00'` rows land in January's partition. Which strategy applies? _(A)_

### Case study — VelvetLoom Checkout

VelvetLoom Checkout stores payment tokens and customer SSNs in Azure SQL Database. Fraud investigators must run `LIKE` suffix searches on encrypted SSNs without DBAs ever seeing plaintext keys or values, all public internet access must be blocked, and regional support reps may view only their own country rows.

Questions in this block:

1. Which encryption technology lets fraud investigators run `WHERE SSN LIKE '%-4821'` while guaranteeing DBAs never access plaintext SSNs or Column Master Keys? _(D)_
2. Which network configuration blocks all public internet access to the Azure SQL Database and routes payment microservice traffic exclusively over a private VNet IP? _(C)_
3. Regional support reps must query and update only rows matching their assigned `CountryIso` and be blocked from inserting rows for other countries. Which three Row-Level Security components should you implement? Select three. _(B, D, F)_

## Exam 2: Healthcare EHR Systems, HIPAA SQL Ledger Compliance, and SQL Managed Instance

### Case study — CuraSpan Regional Health

CuraSpan Regional Health hosts clinical applications on Azure SQL Managed Instance in East US 2 with a paired DR region in Central US. Compliance mandates automatic multi-database regional failover under one listener endpoint, ad-hoc `.bak` exports that never disrupt differential chains, and 7-year immutable WORM backups.

Questions in this block:

1. Which cross-region DR solution satisfies automatic multi-database failover between East US 2 and Central US under a single stable connection listener endpoint? _(A)_
2. Why must ad-hoc T-SQL `.bak` exports on the SQL Managed Instance always include `WITH COPY_ONLY` (`BACKUP DATABASE [EHR] TO URL = '...' WITH COPY_ONLY`)? _(A)_
3. Which two backup configurations satisfy the 7-year HIPAA retention mandate with ransomware-proof WORM protection on SQL Managed Instance? Select two. _(C, D)_

### Case study — PulseCrest Diagnostics

PulseCrest Diagnostics manages 40 Azure SQL Databases and three SQL Managed Instances. Operations wants centralized near-real-time KQL performance dashboards in Microsoft Fabric Eventhouse while planning for 2027 monitoring lifecycle changes, plus persistent Extended Events session files and I/O wait root-cause analysis.

Questions in this block:

1. Which monitoring solution collects agentless performance telemetry from all 40 Azure SQL Databases and 3 SQL Managed Instances into Fabric Eventhouse KQL dashboards, and what 2027 lifecycle transition must the team plan for? _(D)_
2. You must configure persistent Extended Events `.xel` session files for a single clinical Azure SQL Database so deadlock and timeout traces survive failovers. Which two steps are required? Select two. _(A, E)_
3. An imaging lookup query `SELECT AccessionNo, Modality, StudyDate FROM Studies WHERE PatientMRN = @mrn` performs an `Index Seek` on `IX_Studies_PatientMRN` followed by 85,000 `Key Lookup` reads causing `PAGEIOLATCH_SH` waits. How do you eliminate the `Key Lookup`? _(C)_

### Case study — SaffronChart Clinical

SaffronChart Clinical is migrating a 3.5 TB on-premises SQL Server 2022 EHR platform that relies on cross-database `JOIN` queries across four databases, SQL Server Agent jobs, and CLR assemblies into Azure PaaS with under five minutes of cutover downtime and an option to fail back to SQL Server 2022.

Questions in this block:

1. Which Azure SQL PaaS offering natively supports four-part cross-database `JOIN` queries, SQL Server Agent jobs, and safe CLR assemblies without managing guest OS patching? _(A)_
2. Which migration technology replicates the 3.5 TB SQL Server 2022 EHR databases continuously to Azure SQL Managed Instance with under five minutes of cutover downtime AND preserves online failback to SQL Server 2022? _(A)_
3. On the 32-vCore Azure SQL Managed Instance, ad-hoc Epidemiology Power BI DirectQuery users occasionally consume 100% CPU. How can you cap `SG-Epidemiology` logins via `CREATE RESOURCE POOL PoolEpi WITH (____ = 25)`? _(A)_

### Case study — VerityMed Pharmacy

VerityMed Pharmacy records controlled-substance dispensing logs in Azure SQL Database. Regulators require cryptographic proof to external auditors that historical dispense rows were never tampered with by DBAs, Customer-Managed Key TDE stored in Azure Key Vault, and auditing restricted to classified PHI columns.

Questions in this block:

1. In what four-step order must you configure Customer-Managed Key (`CMK`) Transparent Data Encryption in Azure Key Vault for the pharmacy logical SQL server? _(C)_
2. How do you tag PHI dispensing columns so Azure SQL Auditing captures sensitivity metadata and minimizes audit noise to sensitive accesses? _(D)_
3. Which Azure SQL feature provides cryptographic Merkle-tree proof to external DEA regulators (verified via `EXEC sys.____ @digest_locations`) that historical controlled-substance dispense rows were never altered or deleted? _(C)_

## Exam 3: Global FinTech Payments, Confidential Enclaves, and Zero-Data-Loss HA/DR

### Case study — AegisVault Custody

AegisVault Custody enforces zero-password governance across Azure SQL Database and SQL Managed Instance. SQL authentication must be disabled completely, database users must survive geo-failover without `master` login sync, and junior NOC engineers need server-wide DMV visibility without data-read permissions.

Questions in this block:

1. Which server/instance authentication configuration satisfies the zero-password mandate by completely disabling `sa` and SQL password logins across Azure SQL Database and SQL Managed Instance? _(A)_
2. How should you provision database users so credentials never rely on `master` SID mappings and remain immediately valid after an automatic Failover Group switch? _(D)_
3. Which built-in server-level role gives junior NOC engineers server-wide DMV read visibility across all databases on the Azure SQL logical server without granting `SELECT` on custody tables? _(A)_

### Case study — CrestLine Treasury

CrestLine Treasury requires 99.995% availability against datacenter zone outages plus cross-region DR with RPO <= 5 seconds for Azure SQL Database, quarterly non-disruptive DR drills verified by finance teams, and instant transaction rollback whenever a multi-million-row settlement batch aborts.

Questions in this block:

1. Which Azure SQL Database architecture satisfies **both** the `99.995%` intra-region zone-outage availability target AND cross-region disaster recovery with `RPO <= 5 seconds`? _(B)_
2. Which four-step procedure executes the quarterly non-disruptive regional DR drill verified by finance teams without losing a single committed settlement row or changing app connection strings? _(A)_
3. Which built-in Azure SQL engine technology guarantees instantaneous transaction rollback whenever a multi-million-row settlement batch aborts mid-run? _(D)_

### Case study — MintBridge FX

MintBridge FX runs SQL Server 2022 compatibility (`160`) workloads on Azure SQL Managed Instance. A single parameterized trade-search query serves both tiny retail accounts and 40M-row institutional desks, reporting queries intermittently spill `Hash Match` operators to `tempdb`, and ad-hoc analysts starve OLTP CPU.

Questions in this block:

1. Why do reporting queries intermittently display yellow exclamation warnings on `Hash Match` operators and spill to `tempdb`, and which IQP feature resolves this under compatibility level `160`? _(B)_
2. How do you guarantee ad-hoc risk-analyst sessions never consume more than 25% of instance CPU on the Azure SQL Managed Instance so OLTP trade matching stays responsive? _(A)_
3. Which compatibility level `160` Intelligent Query Processing feature allows the single parameterized trade-search query to maintain separate cached execution plans for tiny retail accounts versus 40M-row institutional desks simultaneously? _(A)_

### Case study — QuarryPay Clearing

QuarryPay Clearing is launching a payment-dispute OLTP app inside Microsoft Fabric that needs automatic near-real-time OneLake Delta tables without ETL pipelines, while also moving an existing 1.8 TB database online between two Azure SQL Managed Instances in different VNets with zero data loss.

Questions in this block:

1. Which operational database offering inside Microsoft Fabric gives the payment-dispute app automatic near-real-time OneLake Delta Parquet tables with zero ETL pipelines? _(C)_
2. Before retiring four legacy on-premises SQL Server 2017 clearing databases, you must collect 7 days of PerfMon IOPS/CPU counters to generate right-sized Azure SQL Managed Instance SKU recommendations. Which toolset replaces retired DMA for this task? _(D)_
3. Which network ports must be allowed bidirectionally between the two peered SQL Managed Instance subnets so the 1.8 TB online Database Move succeeds with zero data loss? _(D)_

## Exam 4: Smart Manufacturing ERP, IaaS SQL Server on Azure VMs, and Elastic Jobs

### Case study — AnvilPeak Robotics

AnvilPeak Robotics deploys a 12 TB ERP database on SQL Server 2022 Enterprise on an Azure `E64bds_v5` VM. Storage architects must optimize host caching and disk layout across OS, data, transaction log, and `tempdb` volumes while automating OS/SQL cumulative updates inside strict Sunday maintenance windows.

Questions in this block:

1. Which management extension and patching service automate Windows and SQL Server 2022 cumulative updates strictly inside Sunday maintenance windows on the `E64bds_v5` VM? _(A)_
2. Which three storage and caching configurations should storage architects apply across the `E64bds_v5` VM's data, transaction log, and `tempdb` volumes? Select three. _(A, B, F)_
3. When restoring the 12 TB ERP database onto the `E64bds_v5` VM, `.mdf` creation takes 45 minutes zero-initializing 12 TB of space while `.ldf` still zero-initializes normally. Which Windows security policy skips `.mdf`/`.ndf` zero-initialization safely? _(B)_

### Case study — FoundryGrid Supply

FoundryGrid Supply joins legacy `.NET` plant clients that require integrated Windows Kerberos authentication to Azure SQL Managed Instance without deploying AD Domain Controllers in Azure, restores on-premises `.bak` files whose SQL users lose login mappings, and encrypts vendor IBAN columns.

Questions in this block:

1. How do you enable legacy `.NET` plant clients to connect to Azure SQL Managed Instance using integrated Windows Kerberos authentication without deploying AD Domain Controllers in Azure? _(A)_
2. After restoring on-premises `.bak` files onto SQL Managed Instance, legacy SQL database users exist in `sys.database_principals` yet fail login mapping because SIDs differ. Which query identifies orphaned SQL users and which command repairs them? _(A)_
3. Plant legacy ERP stored procedures must encrypt and decrypt `VendorIBAN` columns directly inside T-SQL without upgrading 200 shop-floor client drivers for Always Encrypted. Which encryption approach works inside T-SQL? _(A)_

### Case study — TurbineSpan Plant Ops

TurbineSpan Plant Ops provisions Azure SQL environments through GitHub Actions Bicep pipelines without exposing administrator secrets, needs immediate email alerts whenever severity 19–25 fatal SQL engine errors occur on SQL Server VMs, and runs a 2-node multi-subnet Always On Availability Group in Azure.

Questions in this block:

1. Which two SQL Server Agent configurations notify plant DBAs immediately by email on fatal severity `19–25` engine errors while running PowerShell maintenance steps without `sysadmin`? Select two. _(A, E)_
2. Which two Bicep and GitHub Actions practices ensure Azure SQL deployments never expose administrator secrets and preview infrastructure changes before applying them? Select two. _(A, E)_
3. What two-node cluster and listener architecture enables sub-second multi-subnet failover for the Always On Availability Group across two Azure subnets without Internal Load Balancer probe latency? _(D)_

### Case study — WeldCore Telemetry

WeldCore Telemetry stores 4.2 billion sensor rows in Azure SQL Database. Queries aggregate 90-day sensor trends while rarely touching partitions older than two years, 600 GB clustered index rebuilds regularly exceed 90-minute maintenance windows, and legacy T-SQL scalar UDFs serialize CPU execution.

Questions in this block:

1. Queries aggregating 90-day sensor trends (`SELECT SensorType, AVG(TempC) FROM Readings WHERE ReadingUTC >= DATEADD(day, -90, SYSUTCDATETIME()) GROUP BY SensorType`) run over 4.2 billion rows. Why does a date-ordered Clustered Columnstore Index excel here? _(D)_
2. 600 GB clustered index rebuilds exceed the 90-minute maintenance window and previously rolled back completely when killed. Proposed solution: Run `ALTER INDEX CCI_OR_PK ON ... REBUILD WITH (ONLINE = ON, RESUMABLE = ON, MAX_DURATION = 90 MINUTES)` so work pauses cleanly at 90 minutes and resumes next window. Does the solution meet the goal? _(D)_
3. Upgrading the telemetry database to compatibility level `160` eliminates row-by-row scalar T-SQL UDF bottlenecks (`INLINE = ON`) alongside two other flagship IQP capabilities. Which three IQP features belong to this `compat 150/160` family? Select three. _(A, B, E)_

## Exam 5: SaaS Multi-Tenant Platforms, Sharded Elastic Pools, and Query Store Tuning

### Case study — CloudSlate Billing

CloudSlate Billing consolidates smaller SaaS tenants into a shared Azure SQL Database table keyed by `TenantId`. Application queries use a shared Managed Identity connection pool yet must never read or insert another tenant's rows, and a billing microservice needs lightweight incremental row-change sync.

Questions in this block:

1. You classify `TenantBankRouting` and `TaxVatNumber` with `ADD SENSITIVITY CLASSIFICATION` and stream Azure SQL Auditing to Log Analytics. Which column in `AzureDiagnostics` lets KQL queries filter specifically for touches on classified columns? _(A)_
2. Which feature (`SELECT * FROM ____(CHANGES Billing.Invoices, @last_version) AS CT`) gives the billing microservice lightweight incremental primary-key row-change synchronization with minimal storage and log overhead? _(C)_
3. Shared Managed Identity connections pool across tenants in `Invoices` (`TenantId`). Which three Row-Level Security components prevent any session from reading or inserting another tenant's rows? Select three. _(A, B, D)_

### Case study — MetricLoom SaaS

MetricLoom SaaS monitors 120 Azure SQL Databases centrally in Log Analytics. Automated AI anomaly detection must pinpoint query regressions and locking storms, parallel OLTP queries suffer heavy `CXPACKET` waits on a 32-vCore database, and weekly corruption checks must avoid production I/O spikes.

Questions in this block:

1. Which Azure Monitor Diagnostic Settings category must be streamed to Log Analytics so automated AI anomaly detection pinpoints query regressions, locking storms, and `MAXDOP` pressure across all 120 databases? _(D)_
2. Parallel OLTP point-lookup queries on the 32-vCore database suffer heavy `CXPACKET` and `CXCONSUMER` waits. Which DMV confirms top wait types and which configuration mitigates excessive OLTP parallelism? _(D)_
3. You standardize automated maintenance across all 120 SaaS databases so index rebuilds pause gracefully, stats updates never stall OLTP compiles, and weekly corruption checks avoid production I/O storms. Which three practices should you enforce? Select three. _(B, D, F)_

### Case study — StackBeacon Ops

StackBeacon Ops executes T-SQL schema rollouts and index maintenance across 480 Azure SQL Databases without storing SQL passwords, scales Elastic Pool vCores up at 07:00 UTC and down at 20:00 UTC via serverless runbooks, and serves low-latency read replicas in four global continents.

Questions in this block:

1. Which native Azure SQL feature executes T-SQL schema rollouts and index maintenance across all 480 tenant databases passwordlessly without storing SQL logins? _(D)_
2. Which serverless Azure automation pattern (`Connect-AzAccount -____; Set-AzSqlElasticPool ...`) scales Elastic Pool vCores up at 07:00 UTC and down at 20:00 UTC daily without managing VMs or storing client secrets? _(B)_
3. Which Azure SQL Database replication feature provides low-latency read-only replicas simultaneously across **four** global continents (`North America`, `Europe`, `Asia`, `Australia`)? _(B)_

### Case study — TenantHive CRM

TenantHive CRM hosts 480 customer databases with staggered regional peak hours in Azure SQL Database. No single noisy tenant may monopolize compute, an application routing directory must map `TenantId` keys to individual shards, and large enterprise tenants are migrating online from SQL Server VMs via blob logs.

Questions in this block:

1. Which Azure SQL Database deployment model shares compute efficiently across the 480 staggered customer databases while enforcing strict per-tenant max vCore ceilings against noisy neighbors? _(D)_
2. Which Elastic Database component maintains the application routing directory mapping discrete `TenantId` GUIDs (`ListShardMap`) to individual shard connection strings across the 480 databases? _(A)_
3. Enterprise tenants are migrating online from SQL Server VMs into SQL Managed Instance by continuously staging `.bak` and `.trn` log files in Azure Blob Storage via `Start-AzSqlInstanceDatabase____`. Which online migration service replays those Blob logs until final cutover? _(B)_

## Exam 6: Public Transit, Energy Grids, Hybrid Always On, and Cloud Backup/Restore

### Case study — GridHarbor Utilities

GridHarbor Utilities operates NERC-CIP regulated SQL Server VMs and Azure SQL Databases. On-premises apps over ExpressRoute must resolve SQL DB to private VNet IPs, a TDE-protected VM database is moving to a new host, and an auditor still cannot `SELECT` from a table despite being added to `db_datareader`.

Questions in this block:

1. Why can the auditor still not `SELECT` from `Grid.TransformerLoad` despite being added to `db_datareader`, and which catalog query confirms the block? _(C)_
2. What mandatory step (`BACKUP ____ [TDECert] TO FILE = '...' WITH PRIVATE KEY (...)`) must you perform in `master` on the source SQL Server VM **before** moving or restoring the TDE-protected database onto the new host VM? _(C)_
3. How must DNS be configured so on-premises apps over ExpressRoute resolve `<server>.database.windows.net` to the Private Endpoint IP inside the Azure VNet? _(A)_

### Case study — HydroCrest Dam Control

HydroCrest Dam Control requires instance-level shared-storage failover (`Always On FCI`) across Availability Zones on Azure VMs for an app that does not support AG listeners, multi-TB native T-SQL backups directly to Azure Blob Storage above 200 GB per file, and troubleshooting growing AG secondary redo queues.

Questions in this block:

1. Which two T-SQL backup configurations allow native multi-TB `BACKUP DATABASE` directly to Azure Blob Storage exceeding 200 GB per file without SAS secrets? Select two. _(A, D)_
2. Which shared-storage configuration enables a 2-node Always On Failover Cluster Instance (`FCI`) across Availability Zones on Azure VMs for the dam-control application that does not support AG listeners? _(B)_
3. `sys.dm_hadr_database_replica_states` shows `redo_queue_size` growing steadily on the AG secondary while `log_send_queue_size` is tiny, and `sys.dm_exec_requests` on the secondary shows `DB_STARTUP` / `REDO` blocked on `LCK_M_SCH_M` behind a 45-minute BI `SELECT` query (`LCK_M_SCH_S`). What happened? _(A)_

### Case study — RailVantage Transit

RailVantage Transit is assessing 85 on-premises SQL Server 2016–2022 instances for Azure readiness, feature blockers, and right-sized vCore SKUs after Microsoft retired DMA, exporting a live 450 GB Azure SQL Database to `.bacpac` with transactional consistency, and evaluating `ROW` vs `PAGE` compression.

Questions in this block:

1. Which stored procedure (`EXEC sys.____ @schema_name = 'dbo', @object_name = 'Timetables', @index_id = NULL, @partition_number = NULL, @data_compression = 'PAGE'`) lets DBAs compare projected disk savings between `ROW` and `PAGE` compression before rebuilding? _(B)_
2. Which modern Microsoft assessment toolset should you use across all 85 on-premises SQL Server 2016–2022 instances to identify compatibility blockers and right-sized vCore SKUs now that DMA is retired? _(D)_
3. How do you export a 100% transactionally consistent `.bacpac` archive of the live 450 GB Azure SQL Database (`CREATE DATABASE [Ticketing_Copy] AS ____ OF [Ticketing];` -> `SqlPackage /Action:Export`) without halting commuter ticketing writes? _(D)_

### Case study — SolarisSpan Dispatch

SolarisSpan Dispatch experiences frequent HTTP 500 errors from `1205` deadlocks between two stored procedures updating `CrewAssignments` and `Vehicles`, 250 ms compile pauses when synchronous statistics refreshes block peak dispatch queries, and a post-upgrade cardinality regression on one database.

Questions in this block:

1. How should you eliminate the `1205` deadlocks occurring between the two stored procedures updating `CrewAssignments` and `Vehicles`? _(A)_
2. Which database setting (`ALTER DATABASE DispatchDB SET ____ ON`) eliminates the 250 ms synchronous query-compile pauses when stale statistics trigger auto-updates during peak dispatch traffic? _(A)_
3. Which single T-SQL statement (`ALTER DATABASE SCOPED CONFIGURATION SET ____ = ON;`) reverts **only** the upgraded dispatch database to the SQL Server 2012 (`70`) Cardinality Estimator without lowering database compatibility level below `160`? _(A)_
