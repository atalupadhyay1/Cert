"""Load 600 authored Exam DP-300: Administering Microsoft Azure SQL Solutions items.

Aligned to the official Microsoft Learn Study Guide for Exam DP-300
(Skills measured as of October 27, 2026; study guide updated October 30, 2026).
Passing Exam DP-300 earns the Associate-level `Microsoft Certified: Azure Database
Administrator Associate` credential (no prerequisite certification required;
700 / 1000 scaled passing score; 100 minutes exam time without labs / 120 minutes
with labs; annual free online renewal on Microsoft Learn; split-screen
`learn.microsoft.com` open-book access in non-lab sections).
"""
from pathlib import Path
import re
from terms import TERMS
import sequences as _sequences  # noqa: F401 — registers SEQUENCES into TERMS

HERE = Path(__file__).resolve().parent

DOMAINS = {
    1: 'Plan and implement data platform resources',
    2: 'Implement a secure environment',
    3: 'Monitor, configure, and optimize database resources',
    4: 'Configure and manage automation of tasks',
    5: 'Plan and configure a high availability and disaster recovery (HA/DR) environment',
}

DOMAIN_NOTES = {
    1: 'Azure SQL DB / SQL MI / SQL VM Sizing, Azure Arc SQL Server, SQL DB in Fabric, Partitioning & Sharding, Storage/Host Caching, Azure Migrate, Managed Instance Link, LRS & MI Online DB Copy/Move (15–20%)',
    2: 'Microsoft Entra ID & Entra Kerberos Auth, Contained Users, Least Privilege, TDE CMK in Key Vault, Always Encrypted & Secure Enclaves, Private Link, Data Classification, Auditing, CT/CDC, DDM, SQL Ledger & RLS (20–25%)',
    3: 'Azure Monitor & DMVs, Database Watcher & Fabric Database Hub, Extended Events, Query Store Plan Forcing & Hints, RCSI & Optimized Locking, Indexing & SARGable T-SQL, Intelligent Insights, Resumable Rebuilds, Resource Governor & IQP (20–25%)',
    4: 'SQL Server Agent Jobs/Proxies/Alerts, Declarative Bicep & ARM with Key Vault, Azure PowerShell & Azure CLI, MI Subnet Troubleshooting, Elastic Jobs with UAMI, Azure Automation Runbooks & Azure Monitor Action Groups (15–20%)',
    5: 'RPO/RTO Architecture, Hybrid MI Link Bidirectional DR, Non-Disruptive DR Drills, COPY_ONLY & Azure Backup, PITR & ADR, Immutable WORM LTR, Striped Backup to URL, Failover Groups, Always On AGs/FCIs & Log Shipping (20–25%)',
}

TOPICS = {
    1: 'Full-Length Mock Exam 1',
    2: 'Full-Length Mock Exam 2',
    3: 'Full-Length Mock Exam 3',
    4: 'Full-Length Mock Exam 4',
    5: 'Full-Length Mock Exam 5',
    6: 'Full-Length Mock Exam 6',
}

SUBTITLES = {
    1: 'Omnichannel E-Commerce, Hyperscale Read-Scale, and Hybrid Azure Arc Retail',
    2: 'Healthcare EHR Systems, HIPAA SQL Ledger Compliance, and SQL Managed Instance',
    3: 'Global FinTech Payments, Confidential Enclaves, and Zero-Data-Loss HA/DR',
    4: 'Smart Manufacturing ERP, IaaS SQL Server on Azure VMs, and Elastic Jobs',
    5: 'SaaS Multi-Tenant Platforms, Sharded Elastic Pools, and Query Store Tuning',
    6: 'Public Transit, Energy Grids, Hybrid Always On, and Cloud Backup/Restore',
}

SKILLS = {
    # Domain 1: Plan and implement data platform resources (15–20% -> 18 items)
    '1.1': 'Recommend an Azure SQL Offering (SQL Database, SQL Managed Instance, or SQL Server on Azure VMs)',
    '1.2': 'Choose Automated Deployment Methods and Deploy SQL Offerings Across Windows, Linux, and Containers',
    '1.3': 'Identify Use Cases for SQL Server Enabled by Azure Arc and SQL Database in Microsoft Fabric',
    '1.4': 'Plan for Table Partitioning (`RANGE RIGHT` / `SWITCH`) and Horizontal Database Sharding (`ShardMapManager`)',
    '1.5': 'Deploy Hybrid SQL Server Solutions and Manage Patching (`SQL IaaS Agent Extension` & `Azure Update Manager`)',
    '1.6': 'Configure Azure SQL Database for Scale and Performance (`Serverless`, `Hyperscale` Named Replicas, `Elastic Pools`)',
    '1.7': 'Configure Azure SQL Managed Instance for Scale and Performance (`Next-gen GP` Sliders & `Business Critical`)',
    '1.8': 'Configure SQL Server on Azure VMs for Scale and Performance (`ReadOnly`/`None` Host Caching, `tempdb` NVMe, `IFI`/`LPIM`)',
    '1.9': 'Configure Table Partitioning Alignment and Data Compression (`ROW`, `PAGE`, `COLUMNSTORE`, `COLUMNSTORE_ARCHIVE`)',
    '1.10': 'Evaluate Migration Requirements, Offline vs Online Strategies, and SKU Sizing via Azure Migrate & ADS',
    '1.11': 'Implement Online and Offline Migrations to and Between Azure SQL Services (`MI Link`, `LRS`, `SqlPackage` Copy)',
    '1.12': 'Implement Azure SQL Managed Instance Online Database Copy and Move (`24h` Completion, `TCP 5022`/`11000-11999`)',

    # Domain 2: Implement a secure environment (20–25% -> 22 items)
    '2.1': 'Configure Microsoft Entra ID and Microsoft Entra-Only Authentication Across SQL DB, SQL MI, and SQL Server',
    '2.2': 'Configure Authentication for SQL Server on Azure VMs and SQL MI (`Microsoft Entra Kerberos` & AD Trusts)',
    '2.3': 'Configure Security Principals and Portable Contained Microsoft Entra Users (`FROM EXTERNAL PROVIDER`)',
    '2.4': 'Apply Least Privilege Using Granular Server/Database Roles, Schema Chaining, `EXECUTE AS`, and T-SQL/GUI Tools',
    '2.5': 'Troubleshoot Authentication and Authorization Issues (Orphaned Users `ALTER USER WITH LOGIN` & `DENY` Precedence)',
    '2.6': 'Implement Transparent Data Encryption (`TDE`) with Service-Managed Keys, Key Vault `CMK`, and VM Cert Backups',
    '2.7': 'Implement Object/Column-Level Encryption (`Symmetric Keys` / `Certificates`) and Enforce `Minimal TLS 1.2`',
    '2.8': 'Configure Server-Level (`master`) vs Portable Database-Level IP Firewall Rules (`sp_set_database_firewall_rule`)',
    '2.9': 'Implement Always Encrypted (`Deterministic` vs `Randomized`) and Always Encrypted with VBS/SGX Secure Enclaves',
    '2.10': 'Configure Azure Private Link (`privatelink.database.windows.net`), Service Endpoints, and SQL MI Subnet Security',
    '2.11': 'Apply SQL Data Discovery & Classification (`ADD SENSITIVITY CLASSIFICATION`) and Server/Database Auditing',
    '2.12': 'Implement Change Tracking (`CHANGETABLE`) vs Change Data Capture (`CDC`) for Downstream Data Changes',
    '2.13': 'Implement Dynamic Data Masking (`default`, `email`, `partial`, `random`) and Scoped `UNMASK` Permissions',
    '2.14': 'Implement Cryptographic Ledger in Azure SQL (`Azure Confidential Ledger`) and Row-Level Security (`FILTER`/`BLOCK`)',

    # Domain 3: Monitor, configure, and optimize database resources (20–25% -> 23 items)
    '3.1': 'Establish Performance Baselines and Interpret CPU, Memory, Data I/O, Log Write, and `tempdb` Metrics',
    '3.2': 'Configure Azure Monitor Diagnostic Settings (`SQLInsights`, `AzureDiagnostics` KQL) and Resource Monitoring',
    '3.3': 'Monitor Workloads Using Database Watcher (ADX / Fabric Eventhouse) and Plan Fabric Database Hub Transition',
    '3.4': 'Monitor Workloads Using Extended Events (`ON DATABASE` vs `ON SERVER` & Persistent Blob `event_file` Targets)',
    '3.5': 'Configure and Monitor Query Store, Force Regressed Plans (`sp_query_store_force_plan`), and Set Query Store Hints',
    '3.6': 'Identify and Resolve Session Blocking (`RCSI`, `Optimized Locking` `TID`/`LAQ`) and Deadlocks (`xml_deadlock_report`)',
    '3.7': 'Identify Performance Bottlenecks Using Dynamic Management Views (`sys.dm_os_wait_stats`, `sys.dm_exec_requests`)',
    '3.8': 'Design Covering/Filtered/Columnstore Indexes and Rewrite Non-SARGable or Implicit-Conversion T-SQL Constructs',
    '3.9': 'Analyze Execution Plans (`Key Lookup`, `TempDB` Spills, Row Skew) and Monitor via SQL Intelligent Insights',
    '3.10': 'Implement Fragmentation-Aware Index Rebuilds (`ONLINE`, `RESUMABLE`), Async Statistics, and `DBCC CHECKDB`',
    '3.11': 'Configure Azure SQL Database Automatic Tuning (`FORCE_LAST_GOOD_PLAN`, `CREATE_INDEX`, `DROP_INDEX`)',
    '3.12': 'Configure Server Performance Settings (`MAXDOP`, `cost threshold`, `max server memory`) and Resource Governor',
    '3.13': 'Implement `ALTER DATABASE SCOPED CONFIGURATION` (`MAXDOP`, `LEGACY_CARDINALITY_ESTIMATION`, `PARAMETER_SNIFFING`)',
    '3.14': 'Identify Use Cases for Intelligent Query Processing (`PSP` Optimization, Memory Grant Feedback, Scalar UDF Inlining)',

    # Domain 4: Configure and manage automation of tasks (15–20% -> 16 items)
    '4.1': 'Create and Schedule SQL Server Agent Maintenance Jobs, Proxies, Severity `19–25` Alerts, and Database Mail',
    '4.2': 'Troubleshoot SQL Server Agent Job Histories, Credential/Proxy Permissions, and SQL MI Subsystem Boundaries',
    '4.3': 'Automate Idempotent Deployment Using Bicep and ARM Templates with `@secure()` Key Vault References & `what-if`',
    '4.4': 'Automate Azure SQL Provisioning and Day-2 Management Using Azure PowerShell (`Az.Sql`) and Azure CLI (`az sql`)',
    '4.5': 'Monitor and Troubleshoot Automated Deployments (`CorrelationId`, Quota, SQL MI Subnet Delegation/UDR/NSG)',
    '4.6': 'Create and Configure Azure SQL Database Elastic Jobs Across Target Groups Using User-Assigned Managed Identity',
    '4.7': 'Automate Database Maintenance and Scaling Using Azure Automation Runbooks, Logic Apps, and Azure Functions',
    '4.8': 'Configure Azure Monitor Action Group Alerts on Database Tasks and Troubleshoot `jobs.job_executions`',

    # Domain 5: Plan and configure a high availability and disaster recovery (HA/DR) environment (20–25% -> 21 items)
    '5.1': 'Recommend HA/DR Architectures Based on RPO and RTO (`Zone Redundant`, `Failover Groups`, `Geo-Restore`)',
    '5.2': 'Evaluate Hybrid HA/DR (`Managed Instance Link` Bidirectional SQL 2022 Failover) and Azure-Specific HA Tiers',
    '5.3': 'Plan Non-Disruptive HA/DR Failover Drills, Listener Redirection Validation, and Read-Only Secondary Testing',
    '5.4': 'Recommend Backup & Restore Strategies (`COPY_ONLY` on MI/AGs and Azure Backup SQL-Aware Policies on VMs)',
    '5.5': 'Perform Native Restores, Point-in-Time Restore (`1–35d` PITR), Deleted-DB Restore, and `ADR` Instant Rollback',
    '5.6': 'Configure Long-Term Backup Retention (`LTR` up to `10y`), Time-Based Immutable WORM Locks, and Storage Redundancy',
    '5.7': 'Back Up to and Restore from Azure Blob Storage URL Using T-SQL Stripes (`TO URL`) and Managed Identity / SAS',
    '5.8': 'Configure Failover Groups (`<fog>.database.windows.net`, Grace Period) vs Active Geo-Replication (`4` Replicas)',
    '5.9': 'Configure Always On Availability Groups on SQL MI and Azure VMs (`Cloud Witness`, `DNN`, `ILB` Port `59999`)',
    '5.10': 'Configure Always On Failover Cluster Instances (`Azure Shared Disks` `ZRS`) and T-SQL Log Shipping on Azure VMs',
    '5.11': 'Monitor and Troubleshoot HA/DR Health (`sys.dm_hadr_database_replica_states`, `redo_queue_size`, `log_send_queue_size`)',
}
VALID_TASKS = set(SKILLS)

OFFICIAL_RANGES = {
    1: (15, 20),
    2: (20, 25),
    3: (20, 25),
    4: (15, 20),
    5: (20, 25),
}

ALLOCATIONS = {
    n: {1: 18, 2: 22, 3: 23, 4: 16, 5: 21}
    for n in range(1, 7)
}

SKILL_PLAN = {
    # Domain 1 = 18
    '1.1': 2, '1.2': 2, '1.3': 2, '1.4': 2, '1.5': 2,
    '1.6': 1, '1.7': 1, '1.8': 2, '1.9': 1, '1.10': 1, '1.11': 1, '1.12': 1,
    # Domain 2 = 22
    '2.1': 2, '2.2': 1, '2.3': 2, '2.4': 2, '2.5': 1,
    '2.6': 2, '2.7': 1, '2.8': 1, '2.9': 2, '2.10': 2,
    '2.11': 2, '2.12': 1, '2.13': 1, '2.14': 2,
    # Domain 3 = 23
    '3.1': 2, '3.2': 1, '3.3': 2, '3.4': 2, '3.5': 2,
    '3.6': 2, '3.7': 2, '3.8': 2, '3.9': 2, '3.10': 2,
    '3.11': 1, '3.12': 1, '3.13': 1, '3.14': 1,
    # Domain 4 = 16
    '4.1': 3, '4.2': 2, '4.3': 2, '4.4': 2, '4.5': 2,
    '4.6': 2, '4.7': 2, '4.8': 1,
    # Domain 5 = 21
    '5.1': 2, '5.2': 2, '5.3': 2, '5.4': 2, '5.5': 2,
    '5.6': 2, '5.7': 2, '5.8': 2, '5.9': 2, '5.10': 2, '5.11': 1,
}

ITEM_TOTAL = 100
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
TYPE_PLAN = {'multiple-choice': 76, 'multi-select': 16, 'ordering': 8}
MULTI_PLAN = {1: 3, 2: 4, 3: 4, 4: 2, 5: 3}
CODE_FILL_FLOOR = 18
PROPOSED_SOL_FLOOR = 6
CASE_STUDIES = 4
CASE_SIZE = 3

SPLIT_PIPE_RE = re.compile(r'(?<!\\)\|')


def _load_set(number: int):
    path = HERE / 'questions' / f'{number}.txt'
    records = []
    for lineno, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        parts = [p.replace(r'\|', '|').strip() for p in SPLIT_PIPE_RE.split(line)]
        if len(parts) != 6:
            raise ValueError(f'{path.name}:{lineno}: expected 6 pipe-separated fields, got {len(parts)}')
        task, kind, answers_s, distractors_s, question, reason = parts
        domain = int(task.split('.')[0])
        answers = [k.strip() for k in answers_s.split(',') if k.strip()]
        distractors = [k.strip() for k in distractors_s.split(',') if k.strip()]
        records.append({
            'id': f'E{number}Q{len(records) + 1:03d}',
            'domain': domain,
            'task': task,
            'kind': kind,
            'answers': answers,
            'distractors': distractors,
            'keys': answers + distractors,
            'question': question,
            'reason': reason,
        })
    return records


BANK = {n: _load_set(n) for n in range(1, 7)}
