"""Canonical DP-900 option and distractor library (July 21, 2026 study guide)."""
from sequences import SEQUENCES

BASE_TERMS = {
    # Domain 1: Core Data Concepts (1.1 - 1.11)
    'structured_data': (
        'Structured data',
        'Structured data adheres to a fixed tabular schema of rows and typed columns, such as relational SQL tables or schema-consistent CSV tables.',
    ),
    'semi_structured_data': (
        'Semi-structured data',
        'Semi-structured data uses self-describing tags, keys, or nested hierarchies (such as JSON, XML, Avro, or YAML) without requiring a rigid relational table schema.',
    ),
    'unstructured_data': (
        'Unstructured data',
        'Unstructured data lacks a predefined field or tag structure and is stored as raw binary or text blobs such as MP4 videos, WAV audio, JPEG images, and PDFs.',
    ),
    'csv_format': (
        'Delimited text format (CSV or TSV)',
        'CSV and TSV store flat rows as plain text separated by commas or tabs, offering universal human readability but lacking nested hierarchy or columnar compression.',
    ),
    'json_format': (
        'JavaScript Object Notation (JSON) document format',
        'JSON represents semi-structured entities using hierarchical key-value pairs and arrays, supporting flexible per-document fields across web APIs and document stores.',
    ),
    'parquet_format': (
        'Apache Parquet columnar storage format',
        'Apache Parquet stores data column-by-column with embedded schema metadata, predicate pushdown, and high compression, accelerating analytical scans over selected columns.',
    ),
    'avro_format': (
        'Apache Avro row-based binary format with JSON schema',
        'Apache Avro packs serialized row records alongside a JSON header schema, making it compact for streaming event pipelines, Kafka/Event Hubs payloads, and schema evolution.',
    ),
    'orc_format': (
        'Optimized Row Columnar (ORC) stripe format',
        'ORC organizes data into compressed stripes with lightweight footer indexes, optimizing large Hive and analytical batch reads.',
    ),
    'key_value_db': (
        'Key-value non-relational store',
        'A key-value store associates each unique key with an opaque or property-bag value, delivering fast single-key lookups and horizontal partitioning without table joins.',
    ),
    'document_db': (
        'Document database',
        'A document database stores self-contained JSON/BSON documents indexed across nested attributes so each entity can evolve fields without schema migrations.',
    ),
    'column_family_db': (
        'Column-family (wide-column) database',
        'A column-family database groups related columns into families keyed by row and partition keys (such as Apache Cassandra or HBase) for massive write throughput.',
    ),
    'graph_db': (
        'Graph database (vertices and directed edges)',
        'A graph database models entities as vertices (nodes) and relationships as typed edges, enabling fast multi-hop traversals for fraud rings, social graphs, and supply dependencies.',
    ),
    'oltp_workload': (
        'Online Transaction Processing (OLTP) workload',
        'OLTP systems process high volumes of short, low-latency `INSERT`, `UPDATE`, and `DELETE` transactions using normalized schemas and ACID guarantees.',
    ),
    'olap_workload': (
        'Online Analytical Processing (OLAP) workload',
        'OLAP systems run complex read-heavy aggregations over historical data organized in denormalized star or snowflake schemas to power business reporting.',
    ),
    'acid_atomicity': (
        'Atomicity (all-or-nothing transaction unit)',
        'Atomicity guarantees that every statement in a transaction either succeeds together or rolls back completely if any step fails, preventing half-completed transfers.',
    ),
    'acid_consistency': (
        'Consistency (valid schema and constraint state)',
        'Consistency ensures a transaction transitions the database only from one valid rule-compliant state (keys, check constraints, types) to another.',
    ),
    'acid_isolation': (
        'Isolation (concurrent transactions do not interfere)',
        'Isolation prevents concurrent in-flight transactions from reading uncommitted intermediate edits or overwriting each other unpredictably via locking or row versioning.',
    ),
    'acid_durability': (
        'Durability (committed writes survive restarts or crashes)',
        'Durability guarantees that once a transaction commits, its changes are persisted to non-volatile transaction logs/storage and survive power loss or crash recovery.',
    ),
    'role_dba': (
        'Database administrator (DBA)',
        'A DBA provisions and configures database servers, enforces RBAC/security, manages backups and point-in-time recovery, and monitors/tunes query availability.',
    ),
    'role_data_engineer': (
        'Data engineer',
        'A data engineer designs, builds, and monitors batch and streaming ingestion pipelines, cleansing transformations, and lakehouse/warehouse storage layers.',
    ),
    'role_data_analyst': (
        'Data analyst',
        'A data analyst explores curated datasets, models semantic relationships and DAX calculations, and designs interactive Power BI visuals and reports for decision-makers.',
    ),

    # Domain 2: Relational Data on Azure (2.1 - 2.6)
    'primary_key': (
        'Primary key constraint',
        'A primary key uniquely identifies each row in a relational table and implicitly forbids `NULL` and duplicate key values.',
    ),
    'foreign_key': (
        'Foreign key constraint',
        'A foreign key references the primary (or unique) key of a parent table to enforce referential integrity and prevent orphaned child rows.',
    ),
    'composite_key': (
        'Composite key (multi-column key)',
        'A composite key combines two or more columns (such as `OrderID` + `ProductID`) to uniquely identify rows in a junction or line-item table.',
    ),
    'norm_1nf': (
        'First Normal Form (1NF — atomic values and no repeating column groups)',
        '1NF requires every column cell to contain a single atomic value with no comma-separated lists or numbered repeating column groups (`Phone1`, `Phone2`).',
    ),
    'norm_2nf': (
        'Second Normal Form (2NF — full functional dependency on the entire composite key)',
        '2NF requires 1NF plus moving any non-key attribute that depends on only part of a composite primary key into its own parent table.',
    ),
    'norm_3nf': (
        'Third Normal Form (3NF — no transitive dependencies between non-key columns)',
        '3NF requires 2NF plus ensuring every non-key attribute depends directly on the primary key and never transitively on another non-key column.',
    ),
    'sql_ddl': (
        'Data Definition Language (`CREATE`, `ALTER`, `DROP`)',
        'DDL statements define, modify, or remove database schema objects such as tables, views, indexes, and constraints.',
    ),
    'sql_dml': (
        'Data Manipulation Language (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)',
        'DML statements query, add, modify, or delete row data stored inside relational tables.',
    ),
    'sql_dcl': (
        'Data Control Language (`GRANT`, `REVOKE`, `DENY`)',
        'DCL statements manage security permissions controlling which principals may read, modify, or execute database objects.',
    ),
    'sql_where_having': (
        '`WHERE` filters rows before grouping; `HAVING` filters aggregated groups after `GROUP BY`',
        '`WHERE` predicates evaluate individual source rows prior to aggregation, whereas `HAVING` filters grouped summary results such as `HAVING COUNT(*) > 5`.',
    ),
    'sql_inner_join': (
        '`INNER JOIN` matching related keys present in both tables',
        '`INNER JOIN` returns only row pairs whose join predicate matches in both the left and right tables, excluding unmatched rows.',
    ),
    'sql_left_join': (
        '`LEFT OUTER JOIN` preserving all left-table rows with `NULL` when right-table matches are absent',
        '`LEFT OUTER JOIN` keeps every row from the left table (for example, all customers) and fills `NULL` for right-table columns when no related order exists.',
    ),
    'db_view': (
        'Database view (saved virtual `SELECT` query)',
        'A standard view encapsulates a saved `SELECT` query as a virtual table to simplify complex joins or restrict column/row exposure without duplicating base table storage.',
    ),
    'stored_procedure': (
        'Stored procedure (parameterized precompiled SQL routine)',
        'A stored procedure encapsulates parameterized SQL statements and control-of-flow logic on the server so applications can invoke `EXEC` securely and consistently.',
    ),
    'clustered_index': (
        'Clustered index (defines physical leaf-level sort order; maximum one per table)',
        'A clustered index sorts and stores the actual data rows of a table in key order, so each table can have at most one clustered index.',
    ),
    'nonclustered_index': (
        'Nonclustered index (separate B-tree structure with row locators; multiple allowed per table)',
        'A nonclustered index maintains a separate sorted key structure pointing back to the base table rows, accelerating selective lookups on non-primary search columns.',
    ),
    'azure_sql_db': (
        'Azure SQL Database (fully managed single-database or elastic-pool PaaS)',
        'Azure SQL Database is a fully managed PaaS database engine with built-in high availability, automated backups, and Serverless or Hyperscale options for cloud apps.',
    ),
    'azure_sql_elastic_pool': (
        'Azure SQL Database Elastic Pool (shared eDTU or vCore compute across multi-tenant DBs)',
        'An Elastic Pool shares a pool of compute resources across multiple single databases that have unpredictable, staggered usage spikes to optimize cost.',
    ),
    'azure_sql_serverless': (
        'Azure SQL Database Serverless compute tier (auto-scaling vCores with idle auto-pause)',
        'The Serverless compute tier automatically scales vCores for intermittent workloads and can auto-pause during inactive periods so you pay only for storage while paused.',
    ),
    'azure_sql_mi': (
        'Azure SQL Managed Instance (near-100% SQL Server instance PaaS compatibility)',
        'SQL Managed Instance provides managed PaaS with instance-scoped features including SQL Server Agent, cross-database queries, Service Broker, and native `.bak` restore.',
    ),
    'sql_server_azure_vm': (
        'SQL Server on Azure Virtual Machines (IaaS with full OS and SQL engine version control)',
        'SQL Server on Azure VMs is IaaS offering complete control over the Windows/Linux OS, specific legacy SQL Server versions, SSRS/SSIS/SSAS host access, and third-party agents.',
    ),
    'azure_migrate_sql': (
        'Azure Migrate (discovery, readiness assessment, and SKU right-sizing for SQL Server)',
        'Azure Migrate discovers on-premises SQL Server instances, evaluates feature compatibility blockers, and recommends right-sized Azure SQL targets (replacing retired DMA).',
    ),
    'entra_id_sql_auth': (
        'Microsoft Entra ID centralized authentication with MFA and passwordless managed identities',
        'Microsoft Entra ID (formerly Azure AD) centralizes identity governance, conditional access, MFA, and passwordless managed-identity connections to Azure data services.',
    ),
    'azure_db_postgresql': (
        'Azure Database for PostgreSQL — Flexible Server',
        'Azure Database for PostgreSQL — Flexible Server is a managed PaaS object-relational database supporting `PL/pgSQL`, PostGIS/custom extensions, `pgAdmin`, and up to 35-day PITR.',
    ),
    'azure_db_mysql': (
        'Azure Database for MySQL — Flexible Server',
        'Azure Database for MySQL — Flexible Server is a managed PaaS relational service based on MySQL Community Edition, commonly backing Linux/Apache/MySQL/PHP (LAMP) web apps.',
    ),

    # Domain 3: Non-Relational Data on Azure (3.1 - 3.5)
    'block_blobs': (
        'Block blobs in Azure Blob Storage',
        'Block blobs store discrete objects up to ~190.7 TiB composed of independently uploaded blocks, making them ideal for documents, images, media, and Parquet/CSV files.',
    ),
    'append_blobs': (
        'Append blobs in Azure Blob Storage',
        'Append blobs optimize block appending exclusively at the end of the blob without updating or deleting existing blocks, making them ideal for immutable application audit logs.',
    ),
    'page_blobs': (
        'Page blobs in Azure Blob Storage',
        'Page blobs organize up to 8 TiB of fixed 512-byte pages for random read/write byte-offset operations, backing Azure Virtual Machine OS and data disks.',
    ),
    'blob_hot_tier': (
        'Hot access tier (highest storage rate, lowest read/write access cost)',
        'The Hot tier is online storage optimized for data that is accessed or modified frequently, carrying the lowest transaction/read cost.',
    ),
    'blob_cool_tier': (
        'Cool access tier (online, 30-day minimum retention for infrequently accessed data)',
        'The Cool tier lowers storage cost relative to Hot for data kept at least 30 days while remaining online with millisecond latency.',
    ),
    'blob_cold_tier': (
        'Cold access tier (online, 90-day minimum retention for rarely accessed data)',
        'The Cold tier provides lower storage pricing than Cool for online data rarely read over at least 90 days without requiring offline rehydration.',
    ),
    'blob_archive_tier': (
        'Archive access tier (offline lowest storage cost, 180-day minimum, requires rehydration)',
        'The Archive tier offers the lowest GB/month storage price for long-term retention (>=180 days) but stores blobs offline until rehydrated to Hot or Cool.',
    ),
    'adls_gen2': (
        'Azure Data Lake Storage Gen2 (Blob Storage with Hierarchical Namespace enabled)',
        'ADLS Gen2 adds a true POSIX-ACL directory hierarchy and atomic folder rename/delete operations atop Azure Blob Storage for big-data analytics engines.',
    ),
    'microsoft_onelake': (
        'Microsoft OneLake (single tenant-wide SaaS data lake built into Microsoft Fabric)',
        'OneLake is Microsoft Fabric’s unified ADLS Gen2-compatible logical data lake that stores Delta Parquet data once and shares it via zero-copy Shortcuts across workloads.',
    ),
    'azure_files': (
        'Azure Files (managed cloud file shares over SMB 3.0 and NFS 4.1)',
        'Azure Files provides fully managed cloud file shares mountable concurrently on Windows, Linux, and macOS via SMB or NFS, plus on-premises caching with Azure File Sync.',
    ),
    'azure_file_sync': (
        'Azure File Sync (caches Azure Files shares on Windows Server with cloud tiering)',
        'Azure File Sync turns on-premises Windows Servers into fast local caches of an Azure file share while tiering cold files to the cloud.',
    ),
    'azure_table_storage': (
        'Azure Table storage (`PartitionKey` + `RowKey` schemaless key-value entities)',
        'Azure Table storage stores denormalized property-bag entities indexed solely by a composite `PartitionKey` (logical grouping) and `RowKey` (unique ID within partition).',
    ),
    'cosmos_global_dist': (
        'Azure Cosmos DB turnkey global distribution with multi-region writes and <10 ms SLAs',
        'Azure Cosmos DB replicates data transparently across selected Azure regions with financially backed 99.999% availability and single-digit millisecond read/write latency.',
    ),
    'cosmos_ru_throughput': (
        'Request Units (RUs) normalized compute/IO currency (Provisioned, Autoscale, or Serverless)',
        'Cosmos DB measures CPU, memory, and IOPS per database operation in Request Units (RUs), billed via Provisioned/Autoscale RU/s or consumption-based Serverless.',
    ),
    'cosmos_consistency_strong': (
        'Strong consistency (linearizable reads guaranteed to return the latest committed write)',
        'Strong consistency guarantees every read returns the most recent globally committed write at the cost of higher write latency and restricted single-write-region topology.',
    ),
    'cosmos_consistency_session': (
        'Session consistency (default level guaranteeing read-your-own-writes and monotonic reads per client session)',
        'Session consistency is Cosmos DB’s default level, balancing low latency and throughput while guaranteeing each user session immediately sees its own writes in order.',
    ),
    'cosmos_consistency_eventual': (
        'Eventual consistency (lowest latency and RU cost; replicas converge without ordering guarantees)',
        'Eventual consistency delivers the lowest read/write latency and RU consumption when applications tolerate temporary stale or out-of-order replica reads.',
    ),
    'cosmos_api_nosql': (
        'Azure Cosmos DB for NoSQL (native JSON document API queried with SQL syntax)',
        'Cosmos DB for NoSQL is Microsoft’s flagship native document API storing JSON items and querying them with familiar `SELECT` SQL expressions and JavaScript triggers/sprocs.',
    ),
    'cosmos_api_mongodb': (
        'Azure Cosmos DB for MongoDB (wire-protocol compatibility for BSON document apps)',
        'Cosmos DB for MongoDB lets existing MongoDB drivers and tools store BSON documents in Cosmos DB simply by updating the connection string.',
    ),
    'cosmos_api_cassandra': (
        'Azure Cosmos DB for Apache Cassandra (wide-column keyspace/table API queried with CQL)',
        'Cosmos DB for Apache Cassandra provides wire compatibility for wide-column workloads using Cassandra Query Language (CQL) without managing Cassandra nodes.',
    ),
    'cosmos_api_gremlin': (
        'Azure Cosmos DB for Apache Gremlin (property-graph vertices and edges traversed via Gremlin)',
        'Cosmos DB for Apache Gremlin stores entities as vertices and relationships as directed edges for multi-hop graph traversals using Apache TinkerPop Gremlin queries.',
    ),
    'cosmos_api_table': (
        'Azure Cosmos DB for Table (key-value API adding global distribution and secondary indexes over Table storage)',
        'Cosmos DB for Table uses the same `PartitionKey`/`RowKey` SDK model as Azure Table storage while adding multi-region failover, automatic secondary indexing, and millisecond SLAs.',
    ),

    # Domain 4: Analytics Workload on Azure (4.1 - 4.8)
    'elt_pattern': (
        'Extract, Load, and Transform (ELT) pattern',
        'ELT extracts raw source data, loads it directly into scalable lake/warehouse storage, and runs distributed cloud compute (Spark or SQL) to cleanse and model in place.',
    ),
    'etl_pattern': (
        'Extract, Transform, and Load (ETL) pattern',
        'ETL transforms, scrubs, or redacts sensitive fields in an intermediate processing engine prior to loading only the conformed structure into the target analytical store.',
    ),
    'azure_data_factory': (
        'Azure Data Factory / Fabric Data Factory pipelines and Dataflows Gen2',
        'Data Factory orchestrates code-free data movement (90+ connectors via Copy activity) and visual Power Query transformations (Dataflows Gen2) or Spark/Mapping Data Flows.',
    ),
    'star_schema': (
        'Star schema (central numeric fact table joined directly to denormalized dimension tables)',
        'A star schema surrounds a quantitative fact table (keys + additive measures) with single-hop dimension tables (`Date`, `Product`, `Customer`) for fast, simple BI queries.',
    ),
    'snowflake_schema': (
        'Snowflake schema (star schema whose dimensions are normalized into sub-dimension tables)',
        'A snowflake schema normalizes hierarchical dimension attributes (such as `Product -> Subcategory -> Category`) into multiple linked tables.',
    ),
    'data_lakehouse': (
        'Data lakehouse (Delta Lake ACID transactions and SQL/Spark queries directly over open Parquet files)',
        'A lakehouse combines the low-cost open file flexibility of a data lake with ACID transactions, schema enforcement, and SQL warehouse performance via Delta Lake tables.',
    ),
    'microsoft_fabric': (
        'Microsoft Fabric (unified SaaS analytics platform atop OneLake)',
        'Microsoft Fabric unifies Data Factory, Data Engineering, Data Warehouse, Data Science, Real-Time Intelligence, and Power BI in one SaaS workspace sharing OneLake Delta tables.',
    ),
    'azure_databricks': (
        'Azure Databricks (collaborative Apache Spark analytics, Delta Lake, and ML platform)',
        'Azure Databricks provides managed Apache Spark clusters, collaborative Python/SQL/Scala/R notebooks, Unity Catalog governance, and Delta Lake processing on Azure.',
    ),
    'azure_synapse': (
        'Azure Synapse Analytics (serverless SQL pools, dedicated MPP SQL pools, and Spark pools)',
        'Azure Synapse Analytics integrates serverless SQL on-demand lake querying, dedicated MPP SQL warehousing, Apache Spark pools, and Synapse Pipelines in Synapse Studio.',
    ),
    'azure_hdinsight': (
        'Azure HDInsight (managed open-source Hadoop, Hive, HBase, Kafka, and Spark clusters)',
        'Azure HDInsight provisions managed clusters of open-source Apache big-data frameworks when lift-and-shift Hadoop/Hive/HBase/Kafka compatibility is required.',
    ),
    'batch_processing': (
        'Batch data processing (scheduled execution over bounded collections of accumulated records)',
        'Batch processing collects records over an interval (hourly, nightly, monthly) and processes the bounded dataset together for high-throughput reporting or billing.',
    ),
    'stream_processing': (
        'Stream data processing (continuous low-latency evaluation of unbounded events in motion)',
        'Stream processing evaluates individual events or rolling time windows continuously as telemetry arrives, powering sub-second anomaly alerts and live dashboards.',
    ),
    'tumbling_window': (
        'Tumbling window (fixed-size, contiguous, non-overlapping time intervals)',
        'A tumbling window partitions an event stream into fixed, back-to-back, non-overlapping slices (such as every 5 minutes) where each event belongs to exactly one window.',
    ),
    'hopping_window': (
        'Hopping window (fixed-size scheduled windows that jump forward by a shorter hop interval and overlap)',
        'A hopping window evaluates a fixed duration (for example, 10 minutes) scheduled every shorter hop (for example, every 2 minutes), so an event can appear in multiple windows.',
    ),
    'sliding_window': (
        'Sliding window (evaluates fixed-duration intervals only when events enter or exit the window)',
        'A sliding window outputs an aggregation over a lookback duration (such as the last 60 seconds) specifically at moments when window membership actually changes.',
    ),
    'session_window': (
        'Session window (variable-length activity bursts closed after a quiet timeout gap)',
        'A session window groups bursts of related events dynamically and closes once no new event arrives within a configured inactivity timeout (up to a max duration).',
    ),
    'azure_event_hubs': (
        'Azure Event Hubs (high-throughput partitioned event ingestion broker with Kafka support)',
        'Azure Event Hubs ingests millions of telemetry events per second into partitioned append logs (supporting native AMQP/HTTPS and Apache Kafka producers) for downstream stream consumers.',
    ),
    'azure_stream_analytics': (
        'Azure Stream Analytics (serverless SQL-like stream processing engine with windowing functions)',
        'Azure Stream Analytics runs declarative Stream Analytics Query Language (`SELECT ... GROUP BY TumblingWindow(...)`) jobs joining live streams with reference data into sinks.',
    ),
    'fabric_rti': (
        'Microsoft Fabric Real-Time Intelligence (Eventstream, Eventhouse KQL database, Real-Time Dashboards, and Activator)',
        'Fabric Real-Time Intelligence ingests and routes events via Eventstream, indexes high-volume telemetry in Eventhouse KQL databases, visualizes live tiles, and triggers Activator alerts.',
    ),
    'spark_structured_streaming': (
        'Apache Spark Structured Streaming (fault-tolerant DataFrame/SQL stream processing in Databricks and Fabric)',
        'Spark Structured Streaming treats a live event stream as an unbounded table processed via familiar Spark SQL/DataFrame APIs with checkpointed exactly-once guarantees.',
    ),
    'pbi_desktop': (
        'Microsoft Power BI Desktop (Windows authoring tool for Power Query, semantic modeling, DAX, and `.pbix` reports)',
        'Power BI Desktop is the free local authoring application where analysts connect data with Power Query, model star schemas and DAX measures, and build multi-page interactive reports.',
    ),
    'pbi_service': (
        'Microsoft Power BI Service (cloud SaaS portal for workspaces, dashboards, scheduled refresh, and Apps)',
        'Power BI Service (`app.powerbi.com` / Fabric) hosts published semantic models and reports, pins cross-report dashboard tiles, schedules gateway refreshes, and distributes governed Apps.',
    ),
    'pbi_report_builder': (
        'Power BI Report Builder (authoring tool for pixel-perfect multi-page paginated `.rdl` operational reports)',
        'Power BI Report Builder designs fixed-layout paginated (`.rdl`) reports optimized for multi-page PDF printing, invoices, and complete row-by-row regulatory statements.',
    ),
    'pbi_semantic_model': (
        'Power BI semantic model (relationships, DAX measures, hierarchies, and Import/DirectQuery/Direct Lake storage)',
        'A Power BI semantic model defines `1:*` star-schema relationships, reusable DAX measures, drill-down hierarchies, and column metadata consumed across reports.',
    ),
    'dax_measure': (
        'DAX measure (dynamic aggregation evaluated at query time in the current report filter context)',
        'Unlike calculated columns stored row-by-row at refresh time, a DAX measure (such as `SUM(Sales[Revenue])`) computes dynamically in response to slicers and visual filters.',
    ),
    'viz_bar_column': (
        'Bar or column chart (comparing discrete categorical values across items)',
        'Bar and column charts use aligned bar lengths to compare magnitudes accurately across discrete categories such as product lines or regions.',
    ),
    'viz_line': (
        'Line chart (tracking continuous trends and changes over ordered time intervals)',
        'Line charts connect ordered time points along a continuous axis to reveal trends, seasonality, and rate of change over days, months, or quarters.',
    ),
    'viz_scatter': (
        'Scatter (or bubble) chart (revealing correlation, clusters, and outliers between two or three numeric measures)',
        'Scatter charts plot two numeric measures on X and Y axes (plus optional bubble size) to expose correlation, clusters, and outliers.',
    ),
    'viz_pie_treemap': (
        'Treemap (or pie/donut chart for small category counts) showing part-to-whole proportions',
        'Pie/donut charts show part-to-whole shares for a few slices, while treemaps use nested rectangles to display proportional composition across larger hierarchical categories.',
    ),
    'viz_kpi_card': (
        'KPI visual or Card (highlighting a single headline metric or progress toward a target goal)',
        'A Card displays a single headline number, while a KPI visual pairs the current indicator value with a trend axis and color-coded distance against a target goal.',
    ),
    'viz_matrix_map': (
        'Matrix visual (cross-tabbed rows/columns with stepped drill-down subtotals) or Azure Map (geospatial coordinates)',
        'A Matrix aggregates measures across both row and column hierarchies like a pivot table, whereas Azure/Filled Maps plot spatial latitude/longitude or regional boundaries.',
    ),
    'viz_waterfall_funnel': (
        'Waterfall chart (sequential positive/negative variance steps) or Funnel chart (linear stage conversion drop-off)',
        'Waterfall charts break down cumulative gains and losses between a starting and ending total, while Funnel charts track progressive drop-off across sequential pipeline stages.',
    ),

    # Anti-pattern / Distractor Keys ('bad_*')
    'bad_archive_live_reads': (
        'Store active operational files directly in Azure Blob Archive tier for immediate millisecond web reads',
        'Archive tier blobs are stored offline and cannot be read directly until rehydrated to Hot or Cool, which takes hours.',
    ),
    'bad_table_joins_fk': (
        'Enforce server-side foreign keys and multi-table SQL `INNER JOIN` queries inside Azure Table storage',
        'Azure Table storage is a schemaless key-value store indexed only by `PartitionKey` and `RowKey` with no foreign keys or server-side table joins.',
    ),
    'bad_sqldb_sql_agent': (
        'Use a single Azure SQL Database to run native SQL Server Agent jobs and cross-database three-part queries',
        'Single Azure SQL Database is database-scoped and does not include SQL Server Agent or cross-database instance queries; those require SQL Managed Instance or SQL Server on Azure VMs.',
    ),
    'bad_pbi_desktop_dashboard': (
        'Create multi-report pinned dashboards directly inside Power BI Desktop offline',
        'Dashboards with pinned tiles across multiple reports are a cloud-only feature of Power BI Service, not Power BI Desktop.',
    ),
    'bad_retired_dma': (
        'Run the retired standalone Data Migration Assistant (DMA) desktop tool as Microsoft’s current cloud sizing service',
        'Microsoft retired Data Migration Assistant (DMA) in July 2025; Azure Migrate and the Azure SQL Migration extension handle SQL discovery, assessment, and right-sizing.',
    ),
    'bad_cosmos_change_api': (
        'Switch an existing Azure Cosmos DB account in place from the NoSQL API to Gremlin or Cassandra without recreating',
        'The Cosmos DB API is bound permanently when the account is created; targeting a different wire protocol requires provisioning a separate Cosmos DB account.',
    ),
    'bad_multiple_clustered': (
        'Create four separate clustered indexes on the same relational table to sort rows four ways physically',
        'Because a clustered index dictates the single physical leaf-level storage order of the table’s rows, a table can have at most one clustered index (plus multiple nonclustered indexes).',
    ),
    'bad_where_aggregates': (
        'Place `SUM()` or `COUNT(*)` aggregate predicates directly inside the SQL `WHERE` clause before `GROUP BY`',
        'SQL `WHERE` evaluates individual pre-grouped rows and rejects aggregate functions; group-level aggregate filters belong in the `HAVING` clause.',
    ),
    'bad_dml_grant': (
        'Use DML `SELECT` and `INSERT` statements to grant or revoke user login permissions on schemas',
        'Granting and revoking security permissions belongs to DCL (`GRANT`, `REVOKE`, `DENY`), not DML.',
    ),
    'bad_oltp_denormalized_5yr': (
        'Denormalize the live checkout table with five years of historical aggregates and disable ACID transaction locks',
        'Denormalized historical scans belong in an OLAP store; live checkout requires normalized OLTP tables with ACID guarantees to prevent lost or corrupted orders.',
    ),
    'bad_azure_queues_files': (
        'Store 20 GB CAD engineering drawings inside single Azure Queue storage messages',
        'Azure Queue storage holds small asynchronous work messages (up to 64 KB per message), not multi-gigabyte binary files.',
    ),
}

TERMS = {**BASE_TERMS, **SEQUENCES}
