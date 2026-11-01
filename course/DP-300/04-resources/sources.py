"""Official Microsoft Learn study guide and primary documentation references for Exam DP-300.

Verified November 1, 2026 against the October 27, 2026 Exam DP-300 Study Guide
(`Study guide for Exam DP-300: Administering Microsoft Azure SQL Solutions`).
"""

STUDY_GUIDE_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300'
CERT_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/'
EXAM_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/exams/dp-300/'

SKILL_SOURCES = {
    # Domain 1: Plan and implement data platform resources (15–20% -> 18 items)
    '1.1': (
        'Compare Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VMs',
        'https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview',
    ),
    '1.2': (
        'Automated deployment options for Azure SQL and SQL Server on Linux/containers',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/arm-templates-content-guide',
    ),
    '1.3': (
        'SQL Server enabled by Azure Arc and SQL database in Microsoft Fabric',
        'https://learn.microsoft.com/en-us/fabric/database/sql/overview',
    ),
    '1.4': (
        'Table partitioning and scaling out with Azure SQL Database sharding',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-scale-introduction',
    ),
    '1.5': (
        'SQL Server IaaS Agent Extension, Automated Patching, and Azure Update Manager',
        'https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-agent-extension-manually-register-single-vm',
    ),
    '1.6': (
        'Azure SQL Database vCore, Serverless, Hyperscale, and Elastic Pools',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/service-tiers-vcore',
    ),
    '1.7': (
        'Azure SQL Managed Instance service tiers and Next-gen General Purpose scaling',
        'https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview',
    ),
    '1.8': (
        'Performance best practices for SQL Server on Azure Virtual Machines',
        'https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-checklist',
    ),
    '1.9': (
        'Configure table partitioning and row/page/columnstore data compression',
        'https://learn.microsoft.com/en-us/sql/relational-databases/data-compression/data-compression',
    ),
    '1.10': (
        'Assess and plan SQL Server migrations using Azure Migrate and Azure SQL Migration extension',
        'https://learn.microsoft.com/en-us/data-migration/sql-server/managed-instance/overview',
    ),
    '1.11': (
        'Online and offline SQL migrations with Managed Instance link, Log Replay Service, and SqlPackage',
        'https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-feature-overview',
    ),
    '1.12': (
        'Copy or move a database online across Azure SQL Managed Instances',
        'https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/database-copy-move-how-to',
    ),

    # Domain 2: Implement a secure environment (20–25% -> 22 items)
    '2.1': (
        'Configure and manage Microsoft Entra authentication with Azure SQL and SQL Server',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview',
    ),
    '2.2': (
        'Windows Authentication for Azure SQL Managed Instance using Microsoft Entra Kerberos and AD',
        'https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/winauth-azuread-overview',
    ),
    '2.3': (
        'Contained database users and Microsoft Entra security principals in Azure SQL',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage',
    ),
    '2.4': (
        'Permissions hierarchy, server-level roles, and principle of least privilege in SQL',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/security-server-roles',
    ),
    '2.5': (
        'Troubleshoot SQL login, orphaned user, and Microsoft Entra authorization issues',
        'https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/troubleshoot-orphaned-users-sql-server',
    ),
    '2.6': (
        'Transparent Data Encryption (TDE) with service-managed and customer-managed keys in Key Vault',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview',
    ),
    '2.7': (
        'Column-level symmetric key encryption and TLS 1.2 in-transit encryption',
        'https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/encrypt-a-column-of-data',
    ),
    '2.8': (
        'Server-level and database-level IP firewall rules in Azure SQL Database',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure',
    ),
    '2.9': (
        'Always Encrypted and Always Encrypted with secure enclaves',
        'https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves',
    ),
    '2.10': (
        'Azure Private Link, Virtual Network service endpoints, and SQL MI VNet security',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/private-endpoint-overview',
    ),
    '2.11': (
        'SQL Data Discovery and Classification and Azure SQL Auditing',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/auditing-overview',
    ),
    '2.12': (
        'Track data changes with Change Tracking (CT) and Change Data Capture (CDC)',
        'https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/track-data-changes-sql-server',
    ),
    '2.13': (
        'Dynamic Data Masking (DDM) in Azure SQL Database, SQL Managed Instance, and SQL Server',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/dynamic-data-masking-overview',
    ),
    '2.14': (
        'Ledger cryptographic tamper-evidence and Row-Level Security (RLS) in Azure SQL',
        'https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-overview',
    ),

    # Domain 3: Monitor, configure, and optimize database resources (20–25% -> 23 items)
    '3.1': (
        'Monitor Azure SQL resource utilization and establish performance baselines',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-sql-database-azure-monitor',
    ),
    '3.2': (
        'Azure Monitor diagnostic settings, SQLInsights logs, and metric alerts',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/metrics-diagnostic-telemetry-logging-streaming-export-configure',
    ),
    '3.3': (
        'Monitor Azure SQL workloads with database watcher and Database Hub in Microsoft Fabric',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database-watcher-overview',
    ),
    '3.4': (
        'Extended Events in Azure SQL Database and Azure SQL Managed Instance',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/xevent-db-diff-from-svr',
    ),
    '3.5': (
        'Monitor performance by using the Query Store, plan forcing, and Query Store hints',
        'https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store',
    ),
    '3.6': (
        'Understand and resolve Azure SQL blocking problems, deadlocks, RCSI, and Optimized Locking',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/analyze-prevent-deadlocks',
    ),
    '3.7': (
        'Monitor performance using Dynamic Management Views (DMVs) and wait statistics',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-with-dmvs',
    ),
    '3.8': (
        'SQL Server and Azure SQL index design guide and SARGable T-SQL tuning',
        'https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide',
    ),
    '3.9': (
        'Execution plans and SQL Intelligent Insights automated performance diagnostics',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/intelligent-insights-overview',
    ),
    '3.10': (
        'Optimize index maintenance, statistics updates, and DBCC CHECKDB integrity checks',
        'https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes',
    ),
    '3.11': (
        'Automatic tuning in Azure SQL Database and Azure SQL Managed Instance',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-overview',
    ),
    '3.12': (
        'Server configuration options (MAXDOP, memory) and Resource Governor workload isolation',
        'https://learn.microsoft.com/en-us/sql/relational-databases/resource-governor/resource-governor',
    ),
    '3.13': (
        'ALTER DATABASE SCOPED CONFIGURATION and dynamic compute/storage scaling',
        'https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-scoped-configuration-transact-sql',
    ),
    '3.14': (
        'Intelligent Query Processing (IQP) features in SQL databases',
        'https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing',
    ),

    # Domain 4: Configure and manage automation of tasks (15–20% -> 16 items)
    '4.1': (
        'SQL Server Agent jobs, schedules, alerts, and Database Mail operators',
        'https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent',
    ),
    '4.2': (
        'Troubleshoot SQL Server Agent jobs, proxies, and SQL Managed Instance Agent differences',
        'https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/transact-sql-tsql-differences-sql-server',
    ),
    '4.3': (
        'Deploy Azure SQL resources using Bicep and Azure Resource Manager (ARM) templates',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-Quickstart-bicep',
    ),
    '4.4': (
        'Automate Azure SQL management using Azure PowerShell and Azure CLI',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/scripts/create-and-configure-database-powershell',
    ),
    '4.5': (
        'Troubleshoot ARM/Bicep template and SQL Managed Instance subnet deployment errors',
        'https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/common-deployment-errors',
    ),
    '4.6': (
        'Elastic jobs in Azure SQL Database with Managed Identity authentication',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-jobs-overview',
    ),
    '4.7': (
        'Automate Azure SQL maintenance tasks with Azure Automation, Logic Apps, and Functions',
        'https://learn.microsoft.com/en-us/azure/automation/overview',
    ),
    '4.8': (
        'Configure Azure Monitor alerts and troubleshoot Elastic Jobs and automated runbooks',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/alerts-insights-configure-portal',
    ),

    # Domain 5: Plan and configure a high availability and disaster recovery (HA/DR) environment (20–25% -> 21 items)
    '5.1': (
        'Business continuity, RPO/RTO targets, and high availability in Azure SQL',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recovery-hadr-overview',
    ),
    '5.2': (
        'Hybrid HA/DR with Managed Instance link and distributed Availability Groups',
        'https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-disaster-recovery',
    ),
    '5.3': (
        'Disaster recovery drills and failover testing for Azure SQL solutions',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/disaster-recovery-drills',
    ),
    '5.4': (
        'Automated backups, COPY_ONLY backups, and Azure Backup for SQL Server in Azure VMs',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-overview',
    ),
    '5.5': (
        'Point-in-time restore (PITR), Accelerated Database Recovery (ADR), and deleted DB restore',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups',
    ),
    '5.6': (
        'Long-term backup retention (LTR) and time-based immutable WORM backups in Azure SQL',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/long-term-retention-overview',
    ),
    '5.7': (
        'SQL Server backup to URL and restore from Azure Blob Storage with Managed Identity or SAS',
        'https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/sql-server-backup-to-url-azure-blob-storage',
    ),
    '5.8': (
        'Failover groups and active geo-replication in Azure SQL Database and SQL Managed Instance',
        'https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db',
    ),
    '5.9': (
        'Always On availability groups on SQL Server on Azure VMs (Cloud Witness, DNN, ILB)',
        'https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/availability-group-overview',
    ),
    '5.10': (
        'Always On Failover Cluster Instances (Azure Shared Disks) and Log Shipping on Azure VMs',
        'https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/failover-cluster-instance-overview',
    ),
    '5.11': (
        'Monitor and troubleshoot Always On availability groups and geo-replication health',
        'https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/monitor-availability-groups-transact-sql',
    ),
}
