"""Canonical 4-step ordered action sequences (`→`) for Exam DP-300 (`kind == 'O'`).

Every sequence option contains exactly 3 `→` arrows (4 steps), stays under 245 characters,
and avoids banned substrings (`drop `, `drag `, `click `, `dummy`, `placeholder`, `todo`).
"""
from terms import TERMS

SEQUENCES = {}


def s(key, label, meaning):
    if label.count('→') != 3:
        raise ValueError(f'{key}: expected 3 arrows, got {label.count("→")}')
    if len(label) > 245:
        raise ValueError(f'{key}: sequence label length {len(label)} > 245')
    SEQUENCES[key] = (label, meaning)
    TERMS[key] = (label, meaning)


# 1. Online SQL Server -> SQL MI migration via Managed Instance link (Domain 1)
s(
    'seq_mi_link_ok',
    'Enable Availability Groups & master key on SQL Server → Establish VNet/IPsec network peering on TCP 5022 → Create Managed Instance link & seed distributed AG → Validate sync state and execute planned cutover to SQL MI',
    'Managed Instance link uses a distributed Availability Group over port 5022 to seed and continuously replicate transaction logs online before executing a near-zero-downtime cutover.',
)
s(
    'seq_mi_link_w1',
    'Create Managed Instance link & seed distributed AG → Enable Availability Groups & master key on SQL Server → Execute planned cutover to SQL MI → Establish VNet/IPsec network peering on TCP 5022',
    'Incorrect order: distributed AG prerequisites and TCP 5022 network connectivity must be in place before creating and seeding a Managed Instance link.',
)
s(
    'seq_mi_link_w2',
    'Export live `.bacpac` via SqlPackage without database copy → Establish VNet peering on UDP 1434 → Restore `.bacpac` onto SQL MI → Enable Availability Groups on SQL Server',
    'Incorrect workflow: `.bacpac` logical export/import is neither transactional on a live DB without a copy nor how Managed Instance link distributed AG replication operates.',
)
s(
    'seq_mi_link_w3',
    'Take SQL Server offline immediately → Copy raw `.mdf`/`.ldf` files to Azure Files SMB → Attach `.mdf` files directly on SQL Managed Instance → Start distributed AG seeding',
    'Incorrect workflow: SQL Managed Instance does not support attaching raw `.mdf`/`.ldf` files from SMB shares, and taking SQL Server offline defeats online migration.',
)

# 2. Online Azure SQL MI cross-instance database move (Domain 1)
s(
    'seq_mi_move_ok',
    'Verify VNet peering & TCP 5022 + 11000-11999 rules → Start online Database Move from source to target SQL MI → Wait for seeding to reach Ready for completion → Complete move within 24 hours so target comes online',
    'Online SQL MI database move requires bidirectional TCP 5022 and 11000–11999 connectivity, seeds asynchronously until Ready for completion, and must be manually completed within 24 hours.',
)
s(
    'seq_mi_move_w1',
    'Start online Database Move → Wait 72 hours in Ready for completion state → Open TCP 5022 + 11000-11999 rules → Expect PITR backups from source MI to transfer automatically',
    'Incorrect workflow: network ports must be open before seeding, operations uncompleted after 24 hours auto-cancel, and source PITR history never transfers with a moved database.',
)
s(
    'seq_mi_move_w2',
    'Stop source SQL Managed Instance compute → Detach user database via sp_detach_db → Copy files over port 1433 → Reattach database on target SQL MI',
    'Incorrect workflow: `sp_detach_db` is unsupported in Azure SQL Managed Instance and online Database Move replicates via Always On availability group seeding without stopping compute.',
)
s(
    'seq_mi_move_w3',
    'Export `.bacpac` to Azure Table storage → Import `.bacpac` onto target SQL MI → Complete move after 48 hours → Retain source database online automatically',
    'Incorrect workflow: `.bacpac` files are stored in Blob storage rather than Table storage, the completion window is 24 hours, and Move removes the source DB upon completion.',
)

# 3. Sliding-window partition SWITCH archive (Domain 1)
s(
    'seq_part_switch_ok',
    'SPLIT partition function for incoming future boundary → Create empty staging table on same filegroup with matching schema/indexes → ALTER TABLE ... SWITCH oldest partition to staging → Archive staging data & MERGE retired boundary',
    'Sliding-window partitioning splits a new empty future range first, performs a metadata-only `ALTER TABLE ... SWITCH` into an aligned staging table, and merges the retired boundary.',
)
s(
    'seq_part_switch_w1',
    'MERGE oldest partition boundary first → Run row-by-row DELETE on 80M rows → Create unindexed staging table on a different filegroup → SPLIT partition function',
    'Incorrect workflow: row-by-row `DELETE` bloats the transaction log and locks tables, and `SWITCH` fails if the staging table resides on a different filegroup or lacks aligned indexes.',
)
s(
    'seq_part_switch_w2',
    'ALTER TABLE ... SWITCH oldest partition directly to Azure Blob Storage → SPLIT partition function → Rebuild entire table offline → MERGE all boundaries',
    'Incorrect workflow: `ALTER TABLE ... SWITCH` swaps metadata between two tables in the same database/filegroup rather than writing directly to Azure Blob Storage.',
)
s(
    'seq_part_switch_w3',
    'Create staging table without matching CHECK constraints → SWITCH partition across two separate Azure SQL Databases → MERGE future boundary → Truncate production table',
    'Incorrect workflow: `SWITCH` is strictly an intra-database metadata operation requiring identical schema, filegroup alignment, and trusted constraints—never cross-database.',
)

# 4. TDE Customer-Managed Key (CMK) rotation & configuration in Azure SQL (Domain 2)
s(
    'seq_tde_cmk_ok',
    'Enable Soft Delete & Purge Protection on Key Vault → Assign Managed Identity to SQL server → Grant Key Vault Crypto Service Encryption User (`get`/`wrapKey`/`unwrapKey`) → Set server TDE protector to Key Vault key',
    'Customer-Managed TDE requires Soft Delete and Purge Protection on Key Vault, a server Managed Identity granted `get`/`wrapKey`/`unwrapKey` permissions, and assigning the Key Vault key as TDE protector.',
)
s(
    'seq_tde_cmk_w1',
    'Set server TDE protector to Key Vault key → Disable Soft Delete and Purge Protection on Key Vault → Assign Managed Identity after encryption starts → Export DEK plaintext to Blob storage',
    'Incorrect workflow: Azure SQL refuses Key Vault TDE protectors unless Soft Delete and Purge Protection are enabled and key-wrapping permissions are granted beforehand.',
)
s(
    'seq_tde_cmk_w2',
    'Create symmetric key inside tempdb → Grant db_datareader in Key Vault → Set database compatibility level to 100 → Restart Azure SQL Database service',
    'Incorrect workflow: TDE CMK wraps the Database Encryption Key via asymmetric RSA keys in Azure Key Vault or Managed HSM, not `tempdb` symmetric keys.',
)
s(
    'seq_tde_cmk_w3',
    'Upload plaintext `.pfx` directly to Azure Table storage → Grant anonymous public read on container → Point TDE protector to Table URL → Disable TLS 1.2',
    'Incorrect workflow: Azure SQL CMK TDE integrates exclusively with Azure Key Vault or Azure Key Vault Managed HSM using Managed Identity, never anonymous storage URLs.',
)

# 5. Always Encrypted with VBS secure enclaves & in-place encryption (Domain 2)
s(
    'seq_enclave_ok',
    'Enable VBS enclave on Azure SQL Database → Provision Key Vault CMK & enclave-enabled CEK (`ENCLAVE_COMPUTATIONS`) → Grant client Key Vault key permissions & attestation → Run in-place `ALTER TABLE` encryption',
    'In-place Always Encrypted with VBS enclaves requires enabling a VBS enclave on the DB, creating an enclave-enabled CEK (`ALLOW_ENCLAVE_COMPUTATIONS`), and running cryptographic operations inside the enclave.',
)
s(
    'seq_enclave_w1',
    'Run in-place column encryption first → Create non-enclave CEK without ENCLAVE_COMPUTATIONS → Store plaintext CMK inside sys.configurations → Enable VBS enclave last',
    'Incorrect workflow: in-place encryption fails unless the database enclave is active and the CEK was created with `ENCLAVE_COMPUTATIONS` beforehand; CMKs never live in `sys.configurations`.',
)
s(
    'seq_enclave_w2',
    'Grant Azure SQL DBA `unwrapKey` on CMK inside T-SQL → Decrypt column via server stored procedure → Apply Dynamic Data Masking → Enable VBS enclave',
    'Incorrect workflow: Always Encrypted keeps CMKs out of SQL engine T-SQL reach so DBAs cannot decrypt data; enclaves process keys only inside attested enclave memory.',
)
s(
    'seq_enclave_w3',
    'Disable TLS on client connection string → Set `Column Encryption Setting=Disabled` → Create Deterministic CEK without CMK → Run `LIKE` wildcard queries',
    'Incorrect workflow: `LIKE` pattern queries on Always Encrypted columns require `Column Encryption Setting=Enabled`, enclave attestation, and Randomized/enclave-enabled encryption.',
)

# 6. Row-Level Security (RLS) multi-tenant isolation rollout (Domain 2)
s(
    'seq_rls_ok',
    'Create dedicated `Security` schema → Create `SCHEMABINDING` inline TVF reading `SESSION_CONTEXT(N\'TenantId\')` → Create `SECURITY POLICY` with `FILTER` & `BLOCK` predicates (`STATE = ON`) → Set read-only `sp_set_session_context` on connect',
    'Best-practice multi-tenant RLS isolates objects in a dedicated schema, uses a schema-bound inline TVF predicate over read-only `SESSION_CONTEXT`, and enforces both `FILTER` and `BLOCK` predicates.',
)
s(
    'seq_rls_w1',
    'Create `SECURITY POLICY` with `STATE = ON` first → Create multi-statement TVF without `SCHEMABINDING` → Grant tenants `ALTER ANY SECURITY POLICY` → Store `TenantId` in a global temp table',
    'Incorrect workflow: RLS requires an existing `SCHEMABINDING` inline TVF before creating the security policy, and granting `ALTER ANY SECURITY POLICY` lets tenants bypass isolation.',
)
s(
    'seq_rls_w2',
    'Apply `ADD MASKED WITH (FUNCTION = \'default()\')` on `TenantId` → Create `AFTER INSERT` trigger → Grant `UNMASK` to shared app login → Expect row filtering',
    'Incorrect workflow: Dynamic Data Masking obfuscates column output in result sets and never filters rows or blocks cross-tenant writes.',
)
s(
    'seq_rls_w3',
    'Create non-schema-bound scalar UDF → Attach UDF to `sys.sp_set_firewall_rule` → Enable Change Tracking → Set `SESSION_CONTEXT` with `@read_only = 0` so users can switch tenants',
    'Incorrect workflow: RLS predicates must be schema-bound inline TVFs attached to a `SECURITY POLICY`, and `@read_only = 1` prevents SQL injection from changing `TenantId` mid-session.',
)

# 7. Query Store regression diagnosis & safe plan forcing (Domain 3)
s(
    'seq_qstore_ok',
    'Confirm Query Store is `READ_WRITE` with wait capture → Compare plan IDs in Regressed Queries (`sys.query_store_runtime_stats`) → Force prior plan via `sp_query_store_force_plan` → Monitor `force_failure_count` & latency',
    'Resolving a parameter-sensitive plan regression uses Query Store runtime/wait history to identify the prior known-good `plan_id`, forces it immediately without code changes, and verifies forcing health.',
)
s(
    'seq_qstore_w1',
    'Run `ALTER DATABASE ... SET QUERY_STORE CLEAR ALL` first → Inspect Regressed Queries history → Force new regressed plan ID → Set `OPERATION_MODE = OFF`',
    'Incorrect workflow: purging Query Store erases the historical baseline and prior good plan needed to diagnose and force the healthy execution plan.',
)
s(
    'seq_qstore_w2',
    'Restart SQL Server production instance during peak traffic → Rebuild every index with `ONLINE = OFF` → Enable `AUTO_CLOSE = ON` → Check Query Store',
    'Incorrect workflow: restarting SQL or running offline index rebuilds causes severe production outage and does not prevent parameter-sensitive plan regressions.',
)
s(
    'seq_qstore_w3',
    'Set Query Store `OPERATION_MODE = READ_ONLY` → Modify `sys.query_store_plan` system catalog via `UPDATE` → Run `DBCC FREEPROCCACHE` every minute → Disable statistics',
    'Incorrect workflow: system catalog tables cannot be updated directly and flushing the plan cache every minute spikes CPU compilations across the entire workload.',
)

# 8. Database watcher provisioning for Azure SQL estate (Domain 3)
s(
    'seq_dbwatcher_ok',
    'Provision Azure Data Explorer or Fabric Eventhouse store → Create database watcher with Managed Identity → Add SQL targets & grant `VIEW SERVER PERFORMANCE STATE` + ingest roles → Start watcher & open portal dashboards',
    'Database watcher streams SQL telemetry into an Azure Data Explorer or Fabric Eventhouse/KQL store using Managed Identity granted least-privilege `VIEW SERVER PERFORMANCE STATE` on SQL targets.',
)
s(
    'seq_dbwatcher_w1',
    'Start database watcher before selecting data store or SQL targets → Grant `sysadmin` via blank-password `sa` login → Store time-series telemetry in Azure Queue Storage → Enable SQL Profiler trace',
    'Incorrect workflow: watcher requires an Azure Data Explorer or Fabric Real-Time Analytics store and SQL targets configured first, and uses least-privilege Managed Identity rather than `sa` or Profiler.',
)
s(
    'seq_dbwatcher_w2',
    'Install third-party kernel drivers inside Azure SQL Database PaaS OS → Configure SMB share on domain controller → Export `.trc` files via `sp_trace_create` → Query via MDX',
    'Incorrect workflow: Azure SQL Database PaaS exposes no underlying OS for agents, `sp_trace_create` is deprecated, and database watcher is agentless.',
)
s(
    'seq_dbwatcher_w3',
    'Create database watcher targeting Azure Cosmos DB for Gremlin → Store metrics in Azure Table storage → Authenticate via anonymous public SAS → Query dashboards via Gremlin',
    'Incorrect workflow: database watcher monitors Azure SQL Database, Elastic Pools, and SQL Managed Instance and stores telemetry in Azure Data Explorer or Fabric KQL databases.',
)

# 9. Elastic Jobs setup with User-Assigned Managed Identity (Domain 4)
s(
    'seq_elastic_job_ok',
    'Create S1+ Job Database & Elastic Job Agent with UAMI → Create contained UAMI user on target DBs with needed permissions → Define Target Group (`jobs.sp_add_target_group_member`) → Add T-SQL steps & schedule (`jobs.sp_add_job`)',
    'Modern Elastic Jobs use a dedicated S1+ job database, an Elastic Job Agent assigned a User-Assigned Managed Identity (UAMI) authorized on target databases, a target group, and scheduled T-SQL steps.',
)
s(
    'seq_elastic_job_w1',
    'Create Elastic Job Agent on Basic tier DB → Run `jobs.sp_add_job` before creating Target Group → Authenticate across servers with Windows NTLM local accounts → Schedule via `msdb.dbo.sp_add_job`',
    'Incorrect workflow: Elastic Job databases require S1 or higher, target groups must exist before binding executions, NTLM local accounts are invalid in SQL DB, and `msdb` belongs to SQL Agent.',
)
s(
    'seq_elastic_job_w2',
    'Enable SQL Server Agent inside single Azure SQL Database → Create linked servers to 480 tenant DBs → Loop synchronously inside a scalar UDF → Grant `CONTROL SERVER` to `guest`',
    'Incorrect workflow: single Azure SQL Databases do not have SQL Server Agent or cross-DB linked servers in the same way as SQL MI; Elastic Jobs fan out T-SQL asynchronously.',
)
s(
    'seq_elastic_job_w3',
    'Provision Elastic Job Agent inside Azure Blob Storage → Store plaintext admin password in Git repo → Add Cosmos DB containers to Target Group → Trigger via `DBCC SHRINKDATABASE`',
    'Incorrect workflow: Elastic Job Agents target Azure SQL servers, elastic pools, and databases using Managed Identity—never Cosmos DB containers or hardcoded Git secrets.',
)

# 10. Multi-database Failover Group setup & non-disruptive DR drill (Domain 5)
s(
    'seq_fog_drill_ok',
    'Provision secondary SQL server with matching firewall/Private Link & Entra admin → Create Failover Group with coupled DBs → Point apps to `<fog>.database.windows.net` & `.secondary` → Run planned `Switch-AzSqlDatabaseFailoverGroup` drill',
    'A resilient Failover Group mirrors security/network configs on the secondary server, groups coupled databases under stable read-write and read-only listeners, and validates readiness via planned zero-data-loss failover.',
)
s(
    'seq_fog_drill_w1',
    'Execute unplanned `AllowDataLoss` forced failover during peak checkout → Create secondary logical SQL server afterward → Hardcode regional server names in app connection strings → Skip firewall rules on secondary',
    'Incorrect workflow: forced failover with `AllowDataLoss` risks dropping uncommitted transactions during drills, and hardcoding regional server names breaks automatic client redirection.',
)
s(
    'seq_fog_drill_w2',
    'Create Failover Group between two servers in the exact same datacenter rack → Add `tempdb` and `master` to Failover Group → Point OLTP writes to `.secondary.database.windows.net` → Disable Geo-Replication',
    'Incorrect workflow: Failover Groups span distinct regions, replicate user databases rather than `master`/`tempdb`, and `.secondary.database.windows.net` is strictly read-only.',
)
s(
    'seq_fog_drill_w3',
    'Export nightly `.bacpac` to local laptop → Delete production database to test restore → Manually edit 50 microservice connection strings → Re-enable TDE after 6 hours',
    'Incorrect workflow: deleting production databases and manually rewriting connection strings causes hours of avoidable downtime instead of testing non-disruptive Failover Group listener failover.',
)
