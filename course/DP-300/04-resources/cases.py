"""Twenty-four original Azure SQL Database Administration case studies (four 3-question cases per mock exam).

Every scenario captures concrete October 27, 2026 Exam DP-300 constraints — PaaS vs IaaS sizing,
Azure Arc & SQL DB in Fabric, online migrations & MI database copy/move, Entra ID/enclaves/Ledger/RLS,
Query Store/Database watcher/DMVs/IQP, Bicep/Elastic Jobs/SQL Agent, and Failover Groups/AGs/LTR —
in under 400 characters so embedded stems stay well below Udemy's 1,000-character limit.
Official Microsoft fictional company names are never used.
"""

CASES = {
    # --- Exam 1: Omnichannel E-Commerce, Hyperscale Read-Scale & Hybrid Arc Retail ---
    'KestrelCart Commerce': (
        'KestrelCart Commerce runs a 14 TB multi-region order database in Azure SQL Database experiencing rapid '
        'seasonal growth, bursty BI read traffic from three analytics teams that must be compute-isolated from OLTP '
        'checkouts, and 18 non-production staging databases that sit idle every night and weekend.'
    ),
    'BrambleBox Stores': (
        'BrambleBox Stores operates 320 SQL Server 2022 instances on Windows and Linux servers across regional '
        'distribution warehouses outside Azure. Leadership wants a single Azure portal inventory, automated SQL '
        'Best Practices Assessments, centralized Microsoft Entra authentication, and hourly pay-as-you-go billing.'
    ),
    'VelvetLoom Checkout': (
        'VelvetLoom Checkout stores payment tokens and customer SSNs in Azure SQL Database. Fraud investigators '
        'must run `LIKE` suffix searches on encrypted SSNs without DBAs ever seeing plaintext keys or values, all '
        'public internet access must be blocked, and regional support reps may view only their own country rows.'
    ),
    'HarborPick Fulfillment': (
        'HarborPick Fulfillment runs high-concurrency warehouse picking on Azure SQL Database. After a nightly '
        'batch skews inventory counts, a critical stored procedure regresses to a slow nested-loops plan, reader '
        'sessions wait behind `LCK_M_S` writer locks, and schema maintenance must run across 35 regional databases.'
    ),

    # --- Exam 2: Healthcare EHR Systems, HIPAA Ledger Compliance & SQL Managed Instance ---
    'SaffronChart Clinical': (
        'SaffronChart Clinical is migrating a 3.5 TB on-premises SQL Server 2022 EHR platform that relies on '
        'cross-database `JOIN` queries across four databases, SQL Server Agent jobs, and CLR assemblies into '
        'Azure PaaS with under five minutes of cutover downtime and an option to fail back to SQL Server 2022.'
    ),
    'VerityMed Pharmacy': (
        'VerityMed Pharmacy records controlled-substance dispensing logs in Azure SQL Database. Regulators require '
        'cryptographic proof to external auditors that historical dispense rows were never tampered with by DBAs, '
        'Customer-Managed Key TDE stored in Azure Key Vault, and auditing restricted to classified PHI columns.'
    ),
    'PulseCrest Diagnostics': (
        'PulseCrest Diagnostics manages 40 Azure SQL Databases and three SQL Managed Instances. Operations wants '
        'centralized near-real-time KQL performance dashboards in Microsoft Fabric Eventhouse while planning for '
        '2027 monitoring lifecycle changes, plus persistent Extended Events session files and I/O wait root-cause analysis.'
    ),
    'CuraSpan Regional Health': (
        'CuraSpan Regional Health hosts clinical applications on Azure SQL Managed Instance in East US 2 with a '
        'paired DR region in Central US. Compliance mandates automatic multi-database regional failover under one '
        'listener endpoint, ad-hoc `.bak` exports that never disrupt differential chains, and 7-year immutable WORM backups.'
    ),

    # --- Exam 3: Global FinTech Payments, Confidential Enclaves & Zero-Data-Loss HA/DR ---
    'QuarryPay Clearing': (
        'QuarryPay Clearing is launching a payment-dispute OLTP app inside Microsoft Fabric that needs automatic '
        'near-real-time OneLake Delta tables without ETL pipelines, while also moving an existing 1.8 TB database '
        'online between two Azure SQL Managed Instances in different VNets with zero data loss.'
    ),
    'AegisVault Custody': (
        'AegisVault Custody enforces zero-password governance across Azure SQL Database and SQL Managed Instance. '
        'SQL authentication must be disabled completely, database users must survive geo-failover without `master` '
        'login sync, and junior NOC engineers need server-wide DMV visibility without data-read permissions.'
    ),
    'MintBridge FX': (
        'MintBridge FX runs SQL Server 2022 compatibility (`160`) workloads on Azure SQL Managed Instance. A single '
        'parameterized trade-search query serves both tiny retail accounts and 40M-row institutional desks, reporting '
        'queries intermittently spill `Hash Match` operators to `tempdb`, and ad-hoc analysts starve OLTP CPU.'
    ),
    'CrestLine Treasury': (
        'CrestLine Treasury requires 99.995% availability against datacenter zone outages plus cross-region DR '
        'with RPO <= 5 seconds for Azure SQL Database, quarterly non-disruptive DR drills verified by finance '
        'teams, and instant transaction rollback whenever a multi-million-row settlement batch aborts.'
    ),

    # --- Exam 4: Smart Manufacturing ERP, IaaS SQL Server on Azure VMs & Elastic Jobs ---
    'AnvilPeak Robotics': (
        'AnvilPeak Robotics deploys a 12 TB ERP database on SQL Server 2022 Enterprise on an Azure `E64bds_v5` VM. '
        'Storage architects must optimize host caching and disk layout across OS, data, transaction log, and '
        '`tempdb` volumes while automating OS/SQL cumulative updates inside strict Sunday maintenance windows.'
    ),
    'FoundryGrid Supply': (
        'FoundryGrid Supply joins legacy `.NET` plant clients that require integrated Windows Kerberos '
        'authentication to Azure SQL Managed Instance without deploying AD Domain Controllers in Azure, restores '
        'on-premises `.bak` files whose SQL users lose login mappings, and encrypts vendor IBAN columns.'
    ),
    'WeldCore Telemetry': (
        'WeldCore Telemetry stores 4.2 billion sensor rows in Azure SQL Database. Queries aggregate 90-day sensor '
        'trends while rarely touching partitions older than two years, 600 GB clustered index rebuilds regularly '
        'exceed 90-minute maintenance windows, and legacy T-SQL scalar UDFs serialize CPU execution.'
    ),
    'TurbineSpan Plant Ops': (
        'TurbineSpan Plant Ops provisions Azure SQL environments through GitHub Actions Bicep pipelines without '
        'exposing administrator secrets, needs immediate email alerts whenever severity 19–25 fatal SQL engine '
        'errors occur on SQL Server VMs, and runs a 2-node multi-subnet Always On Availability Group in Azure.'
    ),

    # --- Exam 5: SaaS Multi-Tenant Platforms, Sharded Elastic Pools & Query Store Tuning ---
    'TenantHive CRM': (
        'TenantHive CRM hosts 480 customer databases with staggered regional peak hours in Azure SQL Database. '
        'No single noisy tenant may monopolize compute, an application routing directory must map `TenantId` keys '
        'to individual shards, and large enterprise tenants are migrating online from SQL Server VMs via blob logs.'
    ),
    'CloudSlate Billing': (
        'CloudSlate Billing consolidates smaller SaaS tenants into a shared Azure SQL Database table keyed by '
        '`TenantId`. Application queries use a shared Managed Identity connection pool yet must never read or '
        'insert another tenant\'s rows, and a billing microservice needs lightweight incremental row-change sync.'
    ),
    'MetricLoom SaaS': (
        'MetricLoom SaaS monitors 120 Azure SQL Databases centrally in Log Analytics. Automated AI anomaly '
        'detection must pinpoint query regressions and locking storms, parallel OLTP queries suffer heavy '
        '`CXPACKET` waits on a 32-vCore database, and weekly corruption checks must avoid production I/O spikes.'
    ),
    'StackBeacon Ops': (
        'StackBeacon Ops executes T-SQL schema rollouts and index maintenance across 480 Azure SQL Databases '
        'without storing SQL passwords, scales Elastic Pool vCores up at 07:00 UTC and down at 20:00 UTC via '
        'serverless runbooks, and serves low-latency read replicas in four global continents.'
    ),

    # --- Exam 6: Public Transit, Energy Grids, Hybrid Always On & Cloud Backup/Restore ---
    'RailVantage Transit': (
        'RailVantage Transit is assessing 85 on-premises SQL Server 2016–2022 instances for Azure readiness, '
        'feature blockers, and right-sized vCore SKUs after Microsoft retired DMA, exporting a live 450 GB Azure '
        'SQL Database to `.bacpac` with transactional consistency, and evaluating `ROW` vs `PAGE` compression.'
    ),
    'GridHarbor Utilities': (
        'GridHarbor Utilities operates NERC-CIP regulated SQL Server VMs and Azure SQL Databases. On-premises '
        'apps over ExpressRoute must resolve SQL DB to private VNet IPs, a TDE-protected VM database is moving to '
        'a new host, and an auditor still cannot `SELECT` from a table despite being added to `db_datareader`.'
    ),
    'SolarisSpan Dispatch': (
        'SolarisSpan Dispatch experiences frequent HTTP 500 errors from `1205` deadlocks between two stored '
        'procedures updating `CrewAssignments` and `Vehicles`, 250 ms compile pauses when synchronous statistics '
        'refreshes block peak dispatch queries, and a post-upgrade cardinality regression on one database.'
    ),
    'HydroCrest Dam Control': (
        'HydroCrest Dam Control requires instance-level shared-storage failover (`Always On FCI`) across Availability '
        'Zones on Azure VMs for an app that does not support AG listeners, multi-TB native T-SQL backups directly '
        'to Azure Blob Storage above 200 GB per file, and troubleshooting growing AG secondary redo queues.'
    ),
}
