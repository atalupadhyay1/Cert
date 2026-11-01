"""32 four-step ('→') workflow sequence options for Microsoft Exam DP-900 (8 groups x 4 options)."""

SEQUENCES = {
    # 1.6 — Operational-to-Analytical Azure Datastore Flow
    'seq_d1_datastore_ok': (
        'Capture OLTP writes in Azure SQL Database → Extract changes via Data Factory pipeline → Land Parquet files in ADLS Gen2 / OneLake → Serve star-schema visuals in Power BI',
        'Operational transactions commit in an ACID relational store first, pipelines land history in columnar lake storage, and analytical models serve BI reports without taxing OLTP.',
    ),
    'seq_d1_datastore_w1': (
        'Capture OLTP writes directly in Archive Blob tier → Run live checkout queries in Power BI Desktop → Copy rows to Azure Files SMB → Normalize into Azure Table storage',
        'Archive blobs are offline and unreadable for live OLTP writes, Power BI Desktop is an authoring tool rather than an OLTP engine, and Table storage is schemaless key-value.',
    ),
    'seq_d1_datastore_w2': (
        'Serve live checkout writes in Power BI Service → Export dashboards to CSV → Load CSVs into Azure SQL Database → Archive active rows to Azure Queue storage',
        'Power BI Service is a read-optimized BI platform rather than a transactional database, and Queue storage buffers small messages rather than archiving relational rows.',
    ),
    'seq_d1_datastore_w3': (
        'Land raw checkout clicks in Paginated Reports → Transform via SMB file locks → Commit ACID transactions in Azure Blob Cold tier → Query via Gremlin graph vertices',
        'Paginated reports render formatted output rather than ingesting transactions, and Blob Cold tier does not execute multi-row ACID relational transactions.',
    ),

    # 1.10 — Data Role Handoff Across a Cloud Data Estate
    'seq_d1_roles_ok': (
        'DBA provisions & secures operational Azure SQL → Data engineer builds ELT pipelines into Fabric Lakehouse → Data engineer curates Gold star-schema tables → Data analyst models DAX KPIs & publishes Power BI reports',
        'DBAs govern operational database engines, data engineers build ingestion/transformation pipelines into curated analytical stores, and data analysts model KPIs and visual reports.',
    ),
    'seq_d1_roles_w1': (
        'Data analyst configures SQL Server failover clusters → DBA authors Spark ELT notebooks in Databricks → Data engineer designs executive Power BI visuals → DBA schedules workspace app audiences',
        'Cluster HA belongs to the DBA, Spark ELT pipelines belong to the data engineer, and visual storytelling/app distribution belongs to the data analyst.',
    ),
    'seq_d1_roles_w2': (
        'Data engineer grants T-SQL row permissions on OLTP → Data analyst provisions Azure VNet private endpoints → DBA builds Power Query Dataflows Gen2 → Data analyst runs point-in-time DB restores',
        'Operational DB security and PITR restores are DBA duties, network/pipeline plumbing belongs to infra/data engineering, and analysts focus on semantic models and visuals.',
    ),
    'seq_d1_roles_w3': (
        'DBA designs executive KPI scorecards → Data analyst writes Spark Structured Streaming checkpoints → Data engineer tunes OLTP clustered indexes → DBA publishes paginated sales packs',
        'KPI scorecards and sales packs are data analyst outputs, whereas Spark streaming pipelines belong to data engineers and OLTP index maintenance belongs to DBAs.',
    ),

    # 2.2 — Relational Normalization Progression (1NF -> 2NF -> 3NF)
    'seq_d2_norm_ok': (
        'Split repeating groups into atomic columns (1NF) → Assign a unique primary key → Move partial composite-key dependencies to parent tables (2NF) → Extract transitive non-key dependencies into lookup tables (3NF)',
        'Normalization progresses sequentially: 1NF enforces atomic values and row uniqueness, 2NF removes partial dependencies on composite keys, and 3NF eliminates transitive non-key dependencies.',
    ),
    'seq_d2_norm_w1': (
        'Remove transitive non-key dependencies (3NF) → Merge comma-separated phone lists into one column → Delete all primary keys to speed inserts → Duplicate customer addresses across every order line',
        'You cannot achieve 3NF before 1NF/2NF, comma-separated lists violate 1NF atomicity, and duplicating addresses reintroduces update anomalies.',
    ),
    'seq_d2_norm_w2': (
        'Create foreign keys on unsplit multi-value columns → Denormalize all lookup tables into one wide sheet → Remove partial dependencies (2NF) → Split atomic columns into repeating groups (1NF)',
        'Foreign keys require atomic primary keys first, and 1NF eliminates repeating groups rather than creating them.',
    ),
    'seq_d2_norm_w3': (
        'Cluster-index raw JSON blobs → Delete primary keys on parent tables → Copy supplier city into every invoice item (2NF) → Combine product names into pipe-delimited strings (3NF)',
        'Copying supplier attributes into invoice items creates transitive redundancy, and pipe-delimited multi-value strings violate 1NF.',
    ),

    # 2.5 — On-Premises SQL Server to Azure SQL Migration Workflow
    'seq_d2_migrate_ok': (
        'Assess SQL Server readiness and SKU sizing in Azure Migrate → Select Azure SQL Database or Managed Instance → Provision target with Entra auth and TLS firewall rules → Migrate schema/data and cut over connection strings',
        'Azure Migrate discovers workloads, flags compatibility blockers, and recommends right-sized Azure SQL targets before secure provisioning, data sync, and connection cutover.',
    ),
    'seq_d2_migrate_w1': (
        'Point production apps to an empty Azure SQL server → Open firewall `0.0.0.0-255.255.255.255` to the public internet → Assess SQL Agent blockers after cutover → Export tables manually as JPEG screenshots',
        'Cutting over before data migration breaks production, opening all public IPs violates security, and assessments must run before selecting the target SKU.',
    ),
    'seq_d2_migrate_w2': (
        'Convert relational tables into Azure Queue messages → Provision SQL Managed Instance without VNet planning → Run compatibility assessment last → Remove all primary keys before cutover',
        'Queue storage is not a relational migration vehicle, SQL Managed Instance requires VNet subnet sizing upfront, and removing primary keys corrupts relational integrity.',
    ),
    'seq_d2_migrate_w3': (
        'Disable TLS encryption on SQL Server → Copy `.mdf` files directly into Azure Table storage → Provision Azure SQL Database Basic tier for cross-DB SQL Agent jobs → Run Azure Migrate discovery',
        'Azure Table storage cannot mount `.mdf` database files, and single Azure SQL Database does not host SQL Server Agent or cross-database instance queries.',
    ),

    # 3.1 — Azure Blob Storage Lifecycle Cost-Optimization Flow
    'seq_d3_blob_ok': (
        'Ingest active files into Hot access tier → Transition 30-day infrequent blobs to Cool tier → Move 90-day rarely read blobs to Cold tier → Transition 365-day compliance blobs to offline Archive tier (rehydrating when needed)',
        'Lifecycle management policies automatically age blobs from lowest-read-cost Hot through Cool and Cold down to lowest-storage-cost offline Archive.',
    ),
    'seq_d3_blob_w1': (
        'Ingest active operational files directly into Archive tier → Serve millisecond web downloads from Archive without rehydration → Move 90-day files to Hot tier → Delete storage account container metadata',
        'Archive tier is offline and cannot serve direct reads until rehydrated to Hot or Cool, which takes hours.',
    ),
    'seq_d3_blob_w2': (
        'Mount Archive blobs as an SMB network drive → Stream live append logs into Page blobs in Cold tier → Transition 1-year compliance archives to Hot tier → Rehydrate Hot blobs before every read',
        'Blob tiers are object storage rather than SMB shares, Archive rather than Hot minimizes 1-year retention storage cost, and Hot blobs require no rehydration.',
    ),
    'seq_d3_blob_w3': (
        'Write unstructured video files into Azure Table `RowKey` cells → Age rows from Cool to Hot after 180 days → Convert Page blobs into SQL views → Rehydrate Cool blobs for 12 hours before reading',
        'Table storage entities hold small key-value properties rather than large video files, and Cool/Cold tiers remain online with immediate millisecond read access.',
    ),

    # 3.5 — Azure Cosmos DB Provisioning and Partitioned Query Flow
    'seq_d3_cosmos_ok': (
        'Create a Cosmos DB account choosing the target API → Create a database and container with a high-cardinality partition key → Configure RU/s or serverless and consistency → Insert items and run partition-scoped queries',
        'API selection happens at account creation, partition key design happens at container creation to distribute storage/RU evenly, and partition-scoped queries avoid cross-partition fan-out.',
    ),
    'seq_d3_cosmos_w1': (
        'Create a container without a partition key → Switch the existing account between Cassandra, Gremlin, and NoSQL APIs daily → Enforce 3NF foreign-key joins across containers → Store 500 MB MP4 blobs inside single JSON items',
        'Every Cosmos DB container requires a partition key, the API is fixed per account, Cosmos DB does not enforce cross-container foreign keys, and item size is capped at 2 MB.',
    ),
    'seq_d3_cosmos_w2': (
        'Install OS patches on Cosmos DB virtual machines → Format NTFS volumes for JSON items → Assign a constant single-value partition key to all 100 million documents → Query exclusively with T-SQL stored procedures',
        'Cosmos DB is fully managed PaaS with no OS patching, a single-value partition key creates a 20 GB logical-partition bottleneck, and triggers/sprocs use JavaScript rather than T-SQL.',
    ),
    'seq_d3_cosmos_w3': (
        'Provision an Azure Files SMB share → Enable Strong consistency across 5 multi-write regions simultaneously → Omit databases and write JSON straight to subscription tags → Query vertices using `SMB2` locks',
        'Cosmos DB sits under an account -> database -> container -> item hierarchy, not SMB shares or subscription tags.',
    ),

    # 4.1 — Modern ELT Lakehouse Medallion Pipeline Flow
    'seq_d4_elt_ok': (
        'Extract source data via Data Factory pipeline → Land raw files into OneLake / ADLS Gen2 (Bronze) → Cleanse and conform Delta tables via Spark or SQL (Silver) → Model star-schema fact/dimension tables (Gold) for BI',
        'Modern ELT lands raw data in scalable lake storage first, then leverages cloud compute to cleanse Silver tables and publish Gold star schemas for analytics.',
    ),
    'seq_d4_elt_w1': (
        'Build Power BI visuals directly against uncleaned CSV attachments → Delete raw source history immediately → Normalize Gold tables into 3NF OLTP row stores → Export final aggregates back into email inboxes',
        'Skipping cleansing degrades report accuracy, deleting raw Bronze files prevents replayability, and Gold analytical layers favor denormalized star schemas over 3NF.',
    ),
    'seq_d4_elt_w2': (
        'Transform terabytes on the client laptop in Notepad → Upload screenshots to Archive Blob tier → Query offline blobs live with DAX → Store fact tables inside Azure Queue messages',
        'ELT executes transformations in scalable cloud engines rather than client laptops, and Archive blobs/Queues cannot back live BI queries.',
    ),
    'seq_d4_elt_w3': (
        'Publish Gold star schema before ingesting source data → Run OLTP checkout locks inside Power BI Mobile → Overwrite source ERP primary keys during read → Store Parquet files in DNS TXT records',
        'Analytical ingestion is read-only against operational sources and builds Bronze -> Silver -> Gold sequentially.',
    ),

    # 4.6 — End-to-End Microsoft Power BI Authoring and Distribution Flow
    'seq_d4_pbi_ok': (
        'Shape source data with Power Query in Power BI Desktop → Relate star-schema tables, write DAX, and build report pages → Publish model and report to Power BI Service → Pin dashboard tiles, schedule refresh, and share an App',
        'Power BI Desktop handles Power Query prep, semantic modeling, and report design, while Power BI Service hosts scheduled refresh, multi-report dashboards, and governed App distribution.',
    ),
    'seq_d4_pbi_w1': (
        'Author multi-report dashboards inside Power BI Mobile → Export `.pbix` files to Azure Table storage → Schedule dataset refresh inside Windows Notepad → Email raw database passwords to report viewers',
        'Dashboards are created in Power BI Service rather than Power BI Mobile, and dataset refresh plus secure sharing are managed in Power BI Service workspaces.',
    ),
    'seq_d4_pbi_w2': (
        'Pin dashboard tiles in Power BI Desktop offline → Write Power Query M transformations inside Power BI Mobile → Store semantic models on SMB floppy shares → Require every executive viewer to edit DAX in Desktop',
        'Dashboards exist only in Power BI Service (not Power BI Desktop), Power BI Mobile is for consumption, and viewers consume shared Apps/reports in browser or mobile.',
    ),
    'seq_d4_pbi_w3': (
        'Design `.rdl` pixel-perfect invoices in Azure Stream Analytics → Publish directly to unmanaged personal OneDrive as an OLTP database → Disable table relationships → Share via anonymous firewall port `1433`',
        'Paginated `.rdl` reports are authored in Power BI Report Builder, Stream Analytics processes event streams, and port `1433` is SQL Server TDS rather than BI sharing.',
    ),
}
