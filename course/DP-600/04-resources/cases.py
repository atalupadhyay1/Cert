"""Twenty-four original Microsoft Fabric Analytics Engineering case studies (four 3-question cases per mock exam).

Every scenario captures concrete October 19, 2026 DP-600 constraints — OneLake security,
Git/PBIP/Deployment Pipeline ALM, Lakehouse/Warehouse/Eventhouse store selection,
Star Schema & SCD Type 2, T-SQL/KQL/DAX querying, and Direct Lake on OneLake vs SQL
optimization — in under 430 characters so embedded stems stay well below Udemy's
1,000-character limit. Official Microsoft sample company names (Contoso, Fabrikam,
AdventureWorks, Wide World Importers, Tailwind Traders, Northwind, Litware, VanArsdel,
Coho Winery, Adatum) are never used.
"""

CASES = {
    # --- Exam 1: Omnichannel Retail, Global Inventory Lakehouses & Direct Lake Merchandising ---
    'Solstice Apparel': (
        'Solstice Apparel runs an F64 Fabric capacity serving 400 regional store managers. Store managers hold '
        'Workspace Viewer access and must see only their assigned region\'s rows AND never see wholesale supplier '
        'cost columns on the Gold Sales Delta table across Spark, SQL, and Direct Lake reports, without maintaining '
        'separate physical tables per region.'
    ),
    'CartVerve Marketplace': (
        'CartVerve Marketplace builds a Medallion Lakehouse and Warehouse over 1.2 billion e-commerce order lines. '
        'Category reassignments on merchants must preserve historical order attribution prior to the change date, '
        'late-arriving orders occasionally arrive before new merchant IDs register, and multi-hop Category -> '
        'Subcategory -> Brand joins slow executive Direct Lake dashboards.'
    ),
    'ShelfPulse POS': (
        'ShelfPulse POS streams 90,000 checkout scanner JSON events per minute from 1,100 stores into a Fabric '
        'Eventhouse KQL database. Store operations needs 5-minute anomaly buckets in KQL, while merchandising '
        'data engineers want to join those same telemetry tables with Lakehouse inventory Delta tables and expose '
        'both inside a single Direct Lake semantic model without duplicating ingestion pipelines.'
    ),
    'LoomCraft Home': (
        'LoomCraft Home has six analytics engineers co-authoring a flagship semantic model and 14 report pages. '
        'Binary .pbix merges in GitHub constantly conflict, executives want one slicer switching YTD, QTD, PY, and '
        'YoY% across 35 base measures with proper $ vs % formatting on bar charts, and a landing page with 38 KPI '
        'cards takes 9 seconds to render despite 40 ms DAX queries.'
    ),

    # --- Exam 2: Healthcare Claims Warehousing, Clinical IoT Eventhouses & HIPAA Governance ---
    'AetherCare Health': (
        'AetherCare Health governs PHI clinical datasets in Microsoft Fabric. Highly Confidential Purview labels '
        'applied to Gold Warehouses must flow automatically to downstream semantic models and exported Excel files, '
        'only central HIPAA stewards may badge datasets as Certified, and engineers must notify owners across six '
        'departmental workspaces before renaming any clinical column.'
    ),
    'BioTrace Diagnostics': (
        'BioTrace Diagnostics ingests lab analyzer telemetry into an Eventhouse where retry bursts emit duplicate '
        'readings per SpecimenId, while reference Parquet extracts land unpredictably in a Lakehouse Files/inbound '
        'folder. Pipelines must trigger the instant new files arrive rather than polling hourly, and notebooks need '
        'full-dataset null/outlier profiling before Silver promotion.'
    ),
    'MedBridge Claims': (
        'MedBridge Claims processes multi-table ACID adjudication batches in a Fabric Data Warehouse. Claims '
        'auditors querying via T-SQL must see only rows for their assigned payer network, see only the last four '
        'digits of patient tax IDs without breaking SELECT * queries, and compare current claim reserves against '
        'exact table state from 48 hours ago before an erroneous batch ran.'
    ),
    'VitalsCore Analytics': (
        'VitalsCore Analytics models hospital admissions where a single encounter maps to multiple ICD-10 diagnosis '
        'groups via a many-to-many relationship, fiscal quarters follow a 4-4-5 retail-health calendar requiring '
        'prior-period comparisons in DAX, and a 900-million-row Import claims archive refreshes over a VNet gateway '
        'with late adjustments updating `LastUpdatedUTC` on historical claims.'
    ),

    # --- Exam 3: Global FinTech Ledger Mirroring, Fraud KQL Streams & Enterprise XMLA ALM ---
    'ClearLedger Bank': (
        'ClearLedger Bank consolidates operational accounts from Azure SQL Database inside a private Azure VNet and '
        'cloud risk scores from Snowflake into Microsoft Fabric with minimal ETL maintenance. Analysts need '
        'near-real-time OneLake Delta availability for operational accounts and zero-copy T-SQL queries joining '
        'the Warehouse risk mart with a sibling Lakehouse in the same workspace.'
    ),
    'FraudShield Pay': (
        'FraudShield Pay streams card authorization events into an Eventhouse and curates settled transactions into '
        'a 2-billion-row Gold Lakehouse table. Fraud analysts query p99 latency and gap-filled 1-minute time series '
        'in KQL, while the Direct Lake semantic model consumes 72% of capacity RAM due to an unused `TransactionGUID` '
        'column and a millisecond `EventTimestamp` column.'
    ),
    'Meridian Wealth': (
        'Meridian Wealth promotes analytics across Development, Test, and Production workspaces on an F128 capacity. '
        'A 28 GB Import/Direct Lake enterprise semantic model exceeds standard size limits, emergency DAX measure '
        'hotfixes must deploy from Dev to Prod without wiping 7 years of processed partitions, and nightly ETL only '
        'needs to reload a single modified monthly partition.'
    ),
    'SwiftSettle FX': (
        'SwiftSettle FX tracks foreign-exchange trades carrying TradeDate, ValueDate, and SettlementDate keys '
        'against one Calendar table. Multi-currency revenue must multiply each trade\'s notional amount by its daily '
        'spot rate row-by-row without adding calculated columns, and portfolio managers want one slicer to switch '
        'matrix rows dynamically between Desk, CurrencyPair, and Counterparty.'
    ),

    # --- Exam 4: Smart Manufacturing, Connected Fleet Telemetry & Supply-Chain Composite Models ---
    'TorqueLine Motors': (
        'TorqueLine Motors mounts existing plant Parquet lakes from ADLS Gen2 and supplier quality logs from Amazon '
        'S3 into a Fabric Lakehouse without copying files. Micro-batch Spark writes generate 45,000 tiny Parquet '
        'files per Gold table, causing Direct Lake queries to degrade and fall back, while row-by-row Python `@udf` '
        'string cleanups bottleneck Silver notebooks.'
    ),
    'ColdHaul Logistics': (
        'ColdHaul Logistics discovers live Azure IoT Hub reefer-truck temperature streams through the Fabric '
        'Real-Time hub. Supply-chain business analysts who do not write T-SQL want a browser diagram interface on '
        'the Warehouse to join shipments with carrier dimensions and save reusable SQL views, while raw CSV '
        'feeds occasionally contain `"N/A"` strings in numeric sensor columns.'
    ),
    'GridWorks Components': (
        'GridWorks Components serves plant operations from a 6-billion-row real-time DirectQuery Warehouse fact '
        'table alongside conformed Product, Plant, and Date dimensions. Ninety-five percent of executive visuals '
        'group by Date, Plant, and ProductCategory, while plant engineers occasionally drill down to individual '
        'serial-number events.'
    ),
    'HarborPort Freight': (
        'HarborPort Freight maintains one Certified golden Supply Chain semantic model in a locked data workspace '
        'while 12 regional teams build thin reports in their own workspaces. External partner analysts must never '
        'discover that `ContractMargin` or `CarrierRebate` columns/measures even exist in metadata, and field '
        'offices receive a zero-data parameterized Power BI file to connect to local ports.'
    ),

    # --- Exam 5: Subscription Media Streaming, Ad-Tech Attribution & Multi-Source Direct Lake ---
    'CineWave Stream': (
        'CineWave Stream stores 4 billion playback events in a Gold Lakehouse, subscription invoices in a separate '
        'Fabric Warehouse, and quarterly ad-sales targets in SharePoint Online Excel sheets. Architects want one '
        'semantic model reading both Fabric Delta sources via Direct Lake plus imported Excel targets with regular '
        'relationships and strict zero-fallback guarantees.'
    ),
    'AdPulse Attribution': (
        'AdPulse Attribution manages 180 DAX measures across campaign semantic models. Analytics engineers want to '
        'author and validate three candidate attribution measures side-by-side in a grid without committing broken '
        'DAX to the model, export a live inventory of all model measures and expressions via DAX, and fix a measure '
        'that accidentally overrides report `Channel` slicer selections.'
    ),
    'PressLine Digital': (
        'PressLine Digital ingests 600 GB of raw nightly CDN Parquet logs from Blob Storage and 35 tables from '
        'PostgreSQL requiring low-code M lookups and column splits. A junior analyst added an `Index Column` step '
        'before date filtering in Dataflow Gen2, causing refreshes to jump from 4 minutes to 52 minutes.'
    ),
    'SoundStage Live': (
        'SoundStage Live links its Fabric workspaces to Azure DevOps Git using `.pbip` projects. One developer '
        'accidentally staged a 650 MB `cache.abf` file in a PR, another developer wants to discard broken '
        'uncommitted notebook edits in their feature workspace, and the team lead notices merged PR commits on '
        '`main` have not appeared in the shared Dev workspace yet.'
    ),

    # --- Exam 6: Renewable Energy Grids, Telecom Network Analytics & Public-Sector Open Data ---
    'SunGrid Renewables': (
        'SunGrid Renewables streams inverter telemetry payloads containing nested JSON `PhaseReadings` arrays into '
        'an Eventhouse and archives hourly generation in a Warehouse. Grid engineers need KQL queries expanding '
        'each phase element into rows, T-SQL queries comparing each hour\'s megawatt output to the prior hour\'s '
        'output per substation, and sargable date predicates that preserve Parquet file skipping.'
    ),
    'TelcoBeam Networks': (
        'TelcoBeam Networks publishes a Direct Lake subscriber-churn report to 1,500 retail store leads who hold '
        'Read + Build on the semantic model via an App, but security policy forbids granting store leads any direct '
        'access to the underlying Lakehouse or SQL analytics endpoint. Each store lead must see only rows matching '
        'their Microsoft Entra email address.'
    ),
    'CivicWorks Transit': (
        'CivicWorks Transit operates a public-transit Fabric Warehouse refreshed every night by Data Factory '
        'pipelines. Before running complex stored-procedure fare recalculations, engineers need an instant zero-copy '
        'backup copy of `dbo.FactRidership` inside the Warehouse, plus a single SQL summary query producing '
        'route, borough, and grand-total ridership subtotals in one pass.'
    ),
    'AquaSpan Utilities': (
        'AquaSpan Utilities created an early Direct Lake semantic model from a Lakehouse SQL analytics endpoint '
        'that suffers unexpected DirectQuery fallbacks and cannot add tables from a second Warehouse. Engineers '
        'plan to convert the model to Direct Lake on OneLake via Power BI Desktop, convert legacy `MeterBinaryHash` '
        'columns to supported types, and optimize DirectQuery detail joins on validated non-null keys.'
    ),
}
