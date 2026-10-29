# Exam DP-600 Case Study Briefs (Sets 1–6)

Every mock exam contains 4 original Microsoft Fabric Analytics Engineering case studies of 3 questions (12 items per set, 24 scenarios total). Paste the relevant scenario into a Udemy practice-test description if uploading `practice-set-N.csv`, or upload `case-embedded-set-N.csv` where each case stem embeds the full scenario directly.

## Exam 1: Omnichannel Retail, Global Inventory Lakehouses, and Direct Lake Merchandising

### Case study — CartVerve Marketplace

CartVerve Marketplace builds a Medallion Lakehouse and Warehouse over 1.2 billion e-commerce order lines. Category reassignments on merchants must preserve historical order attribution prior to the change date, late-arriving orders occasionally arrive before new merchant IDs register, and multi-hop Category -> Subcategory -> Brand joins slow executive Direct Lake dashboards.

Questions in this block:

1. Which dimensional design on `DimMerchant` ensures orders placed before a merchant's category reassignment remain attributed to the historical category while new orders reflect the updated category? _(C)_
2. Late-arriving marketplace orders occasionally land before a newly onboarded `MerchantNaturalId` exists in `DimMerchant`. How should the Gold fact load handle those rows? _(B)_
3. How should you eliminate the slow `Category -> Subcategory -> Brand` multi-hop join chain affecting executive Direct Lake dashboards? _(C)_

### Case study — LoomCraft Home

LoomCraft Home has six analytics engineers co-authoring a flagship semantic model and 14 report pages. Binary .pbix merges in GitHub constantly conflict, executives want one slicer switching YTD, QTD, PY, and YoY% across 35 base measures with proper $ vs % formatting on bar charts, and a landing page with 38 KPI cards takes 9 seconds to render despite 40 ms DAX queries.

Questions in this block:

1. Which file format eliminates binary GitHub merge conflicts across the six analytics engineers co-authoring the flagship model and 14 report pages? _(A)_
2. You author a Calculation Item `YTD = CALCULATE(____, DATESYTD('Calendar'[Date]))` across all 35 base measures while keeping numeric bar-chart plotting for both `$` currency and `%` growth. Which modeling feature and DAX substitution mechanism satisfies this? _(D)_
3. Why does the landing page with 38 KPI cards take 9 seconds to render despite 40 ms DAX queries, and which tool confirms the bottleneck? _(B)_

### Case study — ShelfPulse POS

ShelfPulse POS streams 90,000 checkout scanner JSON events per minute from 1,100 stores into a Fabric Eventhouse KQL database. Store operations needs 5-minute anomaly buckets in KQL, while merchandising data engineers want to join those same telemetry tables with Lakehouse inventory Delta tables and expose both inside a single Direct Lake semantic model without duplicating ingestion pipelines.

Questions in this block:

1. In which order should you expose the checkout Eventhouse KQL telemetry to Lakehouse Spark joins and a unified Direct Lake semantic model without duplicating ingestion? _(C)_
2. Store operations runs `ScannerEvents | where EventTime > ago(2h) ____` in a KQL queryset to compute 99th-percentile scan latency across fixed 5-minute intervals. Which KQL clause completes the query? _(C)_
3. Merchandising wants one semantic model combining the OneLake-enabled Eventhouse table, the Inventory Lakehouse table, and an imported promotional calendar from SharePoint with regular relationships. Which design works? _(D)_

### Case study — Solstice Apparel

Solstice Apparel runs an F64 Fabric capacity serving 400 regional store managers. Store managers hold Workspace Viewer access and must see only their assigned region's rows AND never see wholesale supplier cost columns on the Gold Sales Delta table across Spark, SQL, and Direct Lake reports, without maintaining separate physical tables per region.

Questions in this block:

1. How should you configure OneLake security on the Gold Sales Delta table so regional store managers see only their assigned region's rows AND cannot read wholesale supplier cost columns? _(A)_
2. Store managers querying the Lakehouse SQL analytics endpoint currently see all regions because the endpoint runs under the Lakehouse owner's identity. Which configuration enforces their OneLake security roles on T-SQL queries? _(D)_
3. Which semantic model storage architecture lets the merchandising dashboard read the OneLake-secured Gold Sales table with in-memory Direct Lake speed and zero DirectQuery fallback? _(B)_

## Exam 2: Healthcare Claims Warehousing, Clinical IoT Eventhouses, and HIPAA Governance

### Case study — AetherCare Health

AetherCare Health governs PHI clinical datasets in Microsoft Fabric. Highly Confidential Purview labels applied to Gold Warehouses must flow automatically to downstream semantic models and exported Excel files, only central HIPAA stewards may badge datasets as Certified, and engineers must notify owners across six departmental workspaces before renaming any clinical column.

Questions in this block:

1. How do you ensure `Highly Confidential — PHI` classifications applied on Gold Warehouses propagate automatically to newly created semantic models and exported Excel workbooks? _(C)_
2. Which endorsement configuration guarantees that only central HIPAA data stewards — and not arbitrary workspace Contributors — can badge clinical semantic models as officially vetted? _(D)_
3. Before renaming `PatientMRN_Code` in the core clinical Warehouse, how should engineers identify every affected model across all six departmental workspaces and alert their owners? _(D)_

### Case study — BioTrace Diagnostics

BioTrace Diagnostics ingests lab analyzer telemetry into an Eventhouse where retry bursts emit duplicate readings per SpecimenId, while reference Parquet extracts land unpredictably in a Lakehouse Files/inbound folder. Pipelines must trigger the instant new files arrive rather than polling hourly, and notebooks need full-dataset null/outlier profiling before Silver promotion.

Questions in this block:

1. Retry bursts from lab analyzers write duplicate rows per `SpecimenId` into `AnalyzerTelemetry`. Complete `AnalyzerTelemetry | where IngestionTime > ago(12h) ____` to return the single latest full reading per specimen? _(A)_
2. How should you trigger the Silver ingestion pipeline the instant new reference Parquet extracts arrive in `Files/inbound` rather than running wasteful hourly polling schedules? _(D)_
3. Which interactive notebook tool lets clinical data engineers inspect null percentages, quantiles, and outlier histograms across a Spark DataFrame and export clean PySpark code into Silver notebooks? _(C)_

### Case study — MedBridge Claims

MedBridge Claims processes multi-table ACID adjudication batches in a Fabric Data Warehouse. Claims auditors querying via T-SQL must see only rows for their assigned payer network, see only the last four digits of patient tax IDs without breaking SELECT * queries, and compare current claim reserves against exact table state from 48 hours ago before an erroneous batch ran.

Questions in this block:

1. Complete `CREATE SECURITY POLICY ClaimsPayerPolicy ____;` in the Fabric Warehouse so T-SQL claims auditors see only rows belonging to their assigned payer network? _(A)_
2. Which column definition on `PatientTaxId` (`ALTER TABLE dbo.Claims ALTER COLUMN PatientTaxId ADD ____;`) reveals only the trailing four digits to auditors while allowing `SELECT *` queries to execute without errors? _(B)_
3. Actuaries run `SELECT PayerId, SUM(ReserveAmt) FROM dbo.FactClaims ____ GROUP BY PayerId;` to compare current reserves against exact Warehouse state from 48 hours ago (`2026-10-28T06:00:00.000`). Which clause fills the blank? _(D)_

### Case study — VitalsCore Analytics

VitalsCore Analytics models hospital admissions where a single encounter maps to multiple ICD-10 diagnosis groups via a many-to-many relationship, fiscal quarters follow a 4-4-5 retail-health calendar requiring prior-period comparisons in DAX, and a 900-million-row Import claims archive refreshes over a VNet gateway with late adjustments updating `LastUpdatedUTC` on historical claims.

Questions in this block:

1. `FactEncounter` links `*:1` to `DimEncounter`, which links `1:*` to `BridgeEncounterDiag`, which links `*:1` to `DimDiagnosisGroup`. Complete `Diagnosed Encounters = ____` so diagnosis slicers filter encounter counts without global bidirectional joins? _(B)_
2. Because hospital finance uses a non-standard 4-4-5 fiscal calendar, `DATEADD` fails on period comparisons. Complete `Prior Period Revenue = ____` to fetch the preceding visible fiscal period? _(A)_
3. On the 900-million-row Import claims archive where late claim adjustments update `LastUpdatedUTC`, in which four-step order should you configure Incremental Refresh with `Detect data changes`? _(C)_

## Exam 3: Global FinTech Ledger Mirroring, Fraud KQL Streams, and Enterprise XMLA ALM

### Case study — ClearLedger Bank

ClearLedger Bank consolidates operational accounts from Azure SQL Database inside a private Azure VNet and cloud risk scores from Snowflake into Microsoft Fabric with minimal ETL maintenance. Analysts need near-real-time OneLake Delta availability for operational accounts and zero-copy T-SQL queries joining the Warehouse risk mart with a sibling Lakehouse in the same workspace.

Questions in this block:

1. Which Fabric capability continuously replicates operational account tables from Azure SQL Database and risk tables from Snowflake into OneLake Delta Parquet format with zero ETL code? _(A)_
2. How should Fabric connect securely to the private-endpoint Azure SQL Database inside ClearLedger's Azure VNet without deploying or patching IaaS gateway VMs? _(A)_
3. Complete `SELECT r.AccountId, l.KycTier FROM dbo.RiskScores r JOIN ____ l ON r.AccountId = l.AccountId;` inside `RiskWarehouse` to join `KycLakehouse` in the same workspace with zero data movement? _(D)_

### Case study — FraudShield Pay

FraudShield Pay streams card authorization events into an Eventhouse and curates settled transactions into a 2-billion-row Gold Lakehouse table. Fraud analysts query p99 latency and gap-filled 1-minute time series in KQL, while the Direct Lake semantic model consumes 72% of capacity RAM due to an unused `TransactionGUID` column and a millisecond `EventTimestamp` column.

Questions in this block:

1. Complete `AuthEvents ____` in the Eventhouse KQL queryset to produce gap-filled 1-minute authorization count arrays (`0` when quiet) per merchant region over the last 6 hours? _(A)_
2. Fraud SREs run `AuthEvents | where EventTime > ago(1h) ____` to monitor 99th-percentile authorization latency in 5-minute buckets. Which KQL clause fills the blank? _(D)_
3. Which optimization slashes the 72% capacity RAM footprint caused by unused `TransactionGUID` and millisecond `EventTimestamp` columns on the 2-billion-row Direct Lake model? _(C)_

### Case study — Meridian Wealth

Meridian Wealth promotes analytics across Development, Test, and Production workspaces on an F128 capacity. A 28 GB Import/Direct Lake enterprise semantic model exceeds standard size limits, emergency DAX measure hotfixes must deploy from Dev to Prod without wiping 7 years of processed partitions, and nightly ETL only needs to reload a single modified monthly partition.

Questions in this block:

1. Which semantic model configuration is mandatory so the 28 GB enterprise wealth model can load and refresh on the F128 capacity above the standard compressed size cap? _(B)_
2. In which four-step order should engineers push emergency DAX measure fixes from `Wealth-Dev` to `Wealth-Prod` without wiping 7 years of processed historical partitions? _(B)_
3. Nightly wealth ETL modifies only partition `2026M10` of `FactPositions` and sends TMSL payload `____` over `powerbi://api.powerbi.com/v1.0/myorg/Wealth-Prod`. Which two elements are required? Select two. _(D, E)_

### Case study — SwiftSettle FX

SwiftSettle FX tracks foreign-exchange trades carrying TradeDate, ValueDate, and SettlementDate keys against one Calendar table. Multi-currency revenue must multiply each trade's notional amount by its daily spot rate row-by-row without adding calculated columns, and portfolio managers want one slicer to switch matrix rows dynamically between Desk, CurrencyPair, and Counterparty.

Questions in this block:

1. With `Calendar[DateKey]` actively joined to `FactTrades[TradeDateKey]` and inactively joined to `SettlementDateKey`, complete `Settled FX Volume = ____` without duplicating `Calendar`? _(C)_
2. How should you compute USD revenue (`____(FactFXTrades, FactFXTrades[LocalNotional] * FactFXTrades[DailySpotRate])`) accurately across currencies without adding calculated columns? _(B)_
3. Which feature lets portfolio managers switch matrix rows dynamically between `Desk`, `CurrencyPair` (`NAMEOF('DimTrade'[CurrencyPair])`), and `Counterparty` from a single slicer? _(B)_

## Exam 4: Smart Manufacturing, Connected Fleet Telemetry, and Supply-Chain Composite Models

### Case study — ColdHaul Logistics

ColdHaul Logistics discovers live Azure IoT Hub reefer-truck temperature streams through the Fabric Real-Time hub. Supply-chain business analysts who do not write T-SQL want a browser diagram interface on the Warehouse to join shipments with carrier dimensions and save reusable SQL views, while raw CSV feeds occasionally contain `"N/A"` strings in numeric sensor columns.

Questions in this block:

1. Where in Microsoft Fabric do reefer-fleet engineers discover live Azure IoT Hub temperature streams alongside workspace events and attach Activator temperature-breach alerts? _(A)_
2. Which browser experience lets non-SQL supply-chain analysts visually join `FactShipments` with `DimCarrier` on the Warehouse, filter late loads, and persist reusable SQL views? _(A)_
3. Reefer CSV feeds occasionally emit `"N/A"` inside numeric `ReeferTempC` columns (`____(ReeferTempC AS DECIMAL(6,2))`). Which conversion approach quarantines `"N/A"` as `NULL` instead of aborting nightly loads? _(C)_

### Case study — GridWorks Components

GridWorks Components serves plant operations from a 6-billion-row real-time DirectQuery Warehouse fact table alongside conformed Product, Plant, and Date dimensions. Ninety-five percent of executive visuals group by Date, Plant, and ProductCategory, while plant engineers occasionally drill down to individual serial-number events.

Questions in this block:

1. How should you serve 95% of executive visuals grouped by `Date`, `Plant`, and `ProductCategory` in sub-second memory while routing serial-number drills to the 6-billion-row `DirectQuery` Warehouse table? _(D)_
2. Which storage mode must be set on `DimProduct`, `DimPlant`, and `DimDate` so both the in-memory aggregation table and the 6-billion-row `DirectQuery` detail table join cleanly without cross-source penalties? _(B)_
3. Plant ERP stores `Part -> SubAssembly -> AssemblyFamily -> ProductLine` in four normalized tables. How should you structure `Gold.DimProduct`? _(D)_

### Case study — HarborPort Freight

HarborPort Freight maintains one Certified golden Supply Chain semantic model in a locked data workspace while 12 regional teams build thin reports in their own workspaces. External partner analysts must never discover that `ContractMargin` or `CarrierRebate` columns/measures even exist in metadata, and field offices receive a zero-data parameterized Power BI file to connect to local ports.

Questions in this block:

1. How should the 12 regional teams build customized logistics reports in their own workspaces while reusing the single Certified golden `SupplyChain` semantic model? _(A)_
2. Which security control guarantees external partner analysts cannot even discover that `ContractMargin` or `CarrierRebate` columns and referencing measures exist in model metadata? _(A)_
3. Which zero-data file format should you ship to field port offices so opening it prompts for their `PortTerminalCode` parameter and populates visuals against local data? _(A)_

### Case study — TorqueLine Motors

TorqueLine Motors mounts existing plant Parquet lakes from ADLS Gen2 and supplier quality logs from Amazon S3 into a Fabric Lakehouse without copying files. Micro-batch Spark writes generate 45,000 tiny Parquet files per Gold table, causing Direct Lake queries to degrade and fall back, while row-by-row Python `@udf` string cleanups bottleneck Silver notebooks.

Questions in this block:

1. How should you expose existing plant Parquet lakes in ADLS Gen2 and supplier quality logs in Amazon S3 inside your Fabric Lakehouse without duplicating files or scheduling copy pipelines? _(D)_
2. Micro-batch Spark writes produced 45,000 tiny Parquet files on `gold.fact_orders` / `gold.fact_assembly`, triggering Direct Lake guardrail degradation. Complete the maintenance command `____;` to compact rowgroups and optimize columnar compression? _(B)_
3. How should Silver notebooks replace the slow row-by-row Python `@udf` string cleanups (`df.____("CleanVIN", F.upper(F.trim("RawVIN")))`) across hundreds of millions of assembly records? _(A)_

## Exam 5: Subscription Media Streaming, Ad-Tech Attribution, and Multi-Source Direct Lake

### Case study — AdPulse Attribution

AdPulse Attribution manages 180 DAX measures across campaign semantic models. Analytics engineers want to author and validate three candidate attribution measures side-by-side in a grid without committing broken DAX to the model, export a live inventory of all model measures and expressions via DAX, and fix a measure that accidentally overrides report `Channel` slicer selections.

Questions in this block:

1. Which Power BI authoring surface lets engineers write and compare three candidate attribution measures side-by-side in a grid (`DEFINE MEASURE ... EVALUATE SUMMARIZECOLUMNS(...)`) before saving to the model? _(D)_
2. Complete the DAX Query View command `____` to export a live catalog of all 180 model measures, formulas, display folders, and format strings? _(D)_
3. `Paid Social Conversions = CALCULATE([Conversions], 'DimChannel'[Channel] = "Paid Social")` overwrites the user's report slicer when `"Search"` is selected. Wrapping the predicate in `____` fixes this? _(A)_

### Case study — CineWave Stream

CineWave Stream stores 4 billion playback events in a Gold Lakehouse, subscription invoices in a separate Fabric Warehouse, and quarterly ad-sales targets in SharePoint Online Excel sheets. Architects want one semantic model reading both Fabric Delta sources via Direct Lake plus imported Excel targets with regular relationships and strict zero-fallback guarantees.

Questions in this block:

1. Which Direct Lake mode lets one semantic model read both the 4-billion-row `PlaybackLakehouse` and the separate `BillingWarehouse` while guaranteeing zero DirectQuery fallback? _(A)_
2. How can engineers add the SharePoint Online Excel ad-sales target sheets into that same `Direct Lake on OneLake` semantic model with fast regular `1:*` relationships? _(A)_
3. Hourly Spark jobs finish compacting playback Delta tables at `:05` past the hour, and CineWave disables automatic updates so partial mid-job writes never appear. What operation at `:06` exposes the completed batch? _(B)_

### Case study — PressLine Digital

PressLine Digital ingests 600 GB of raw nightly CDN Parquet logs from Blob Storage and 35 tables from PostgreSQL requiring low-code M lookups and column splits. A junior analyst added an `Index Column` step before date filtering in Dataflow Gen2, causing refreshes to jump from 4 minutes to 52 minutes.

Questions in this block:

1. Which Fabric tool should ingest the 600 GB of nightly raw CDN Parquet logs from Blob Storage into `BronzeLakehouse` at lowest CU consumption when no M transformations are needed? _(A)_
2. Which configuration optimizes ingesting and splitting the 35 PostgreSQL tables requiring visual Power Query M lookups into `EditorialWarehouse`? _(D)_
3. Why did adding `Index Column` before the date filter jump Dataflow Gen2 duration from 4 minutes to 52 minutes, and how do you restore speed? _(C)_

### Case study — SoundStage Live

SoundStage Live links its Fabric workspaces to Azure DevOps Git using `.pbip` projects. One developer accidentally staged a 650 MB `cache.abf` file in a PR, another developer wants to discard broken uncommitted notebook edits in their feature workspace, and the team lead notices merged PR commits on `main` have not appeared in the shared Dev workspace yet.

Questions in this block:

1. How do you prevent developers from staging 650 MB `cache.abf` VertiPaq data files and personal `localSettings.json` files in `.pbip` pull requests? _(D)_
2. Which Source control pane action lets the developer cleanly discard broken uncommitted notebook edits in their isolated feature workspace back to the last synced commit? _(C)_
3. Why haven't merged PR commits on `main` appeared in `SoundStage-Dev` yet, and which four-step end-to-end Git + Deployment Pipeline sequence completes promotion? _(B)_

## Exam 6: Renewable Energy Grids, Telecom Network Analytics, and Public-Sector Open Data

### Case study — AquaSpan Utilities

AquaSpan Utilities created an early Direct Lake semantic model from a Lakehouse SQL analytics endpoint that suffers unexpected DirectQuery fallbacks and cannot add tables from a second Warehouse. Engineers plan to convert the model to Direct Lake on OneLake via Power BI Desktop, convert legacy `MeterBinaryHash` columns to supported types, and optimize DirectQuery detail joins on validated non-null keys.

Questions in this block:

1. While migrating the semantic model from `Direct Lake on SQL` to `Direct Lake on OneLake` in Power BI Desktop TMDL view, which M expression (`____`) replaces `Sql.Database(...)`? _(A)_
2. Why did `MeterBinaryHash` (`BINARY`) fail to load into the Direct Lake semantic model, and how should Gold ETL prepare it? _(D)_
3. For a companion `DirectQuery` meter-outage detail table whose foreign keys to `DimTransformer` are validated non-null in ETL, which relationship property switches SQL joins from `LEFT OUTER JOIN` to `INNER JOIN`? _(C)_

### Case study — CivicWorks Transit

CivicWorks Transit operates a public-transit Fabric Warehouse refreshed every night by Data Factory pipelines. Before running complex stored-procedure fare recalculations, engineers need an instant zero-copy backup copy of `dbo.FactRidership` inside the Warehouse, plus a single SQL summary query producing route, borough, and grand-total ridership subtotals in one pass.

Questions in this block:

1. Complete `____;` (conceptually cloning `dbo.FactRidership`) to create an instantaneous zero-copy Warehouse backup table before running nightly fare recalculations? _(A)_
2. How should Data Factory pipelines encapsulate and execute the multi-step fare recalculation `MERGE` and audit-logging T-SQL transaction inside `TransitWarehouse`? _(B)_
3. Complete `SELECT RouteId, Borough, SUM(Riders) AS TotalRiders FROM gold.FactRidership ____;` to compute `(RouteId, Borough)` subtotals, `(Borough)` subtotals, and the citywide grand total `()` in one scan? _(A)_

### Case study — SunGrid Renewables

SunGrid Renewables streams inverter telemetry payloads containing nested JSON `PhaseReadings` arrays into an Eventhouse and archives hourly generation in a Warehouse. Grid engineers need KQL queries expanding each phase element into rows, T-SQL queries comparing each hour's megawatt output to the prior hour's output per substation, and sargable date predicates that preserve Parquet file skipping.

Questions in this block:

1. Solar inverters stream JSON payloads containing nested `PhaseReadings` arrays into `GridEventhouse`. Complete `InverterEvents ____ | summarize avg(toreal(PhaseReading.voltage)) by InverterId` to expand each phase element into its own row? _(B)_
2. Complete `SELECT SubstationId, ReadingHour, MegawattOutput, MegawattOutput - ____ AS HourlyRampMW FROM gold.FactGeneration;` in the Warehouse to compare each hour's output against the immediately preceding hour per substation? _(B)_
3. Why should grid engineers write `WHERE ReadingDate >= '2026-10-01' AND ReadingDate < '2026-11-01'` rather than `WHERE CONVERT(VARCHAR(7), ReadingDate, 120) = '2026-10'` on `gold.FactGeneration`? _(C)_

### Case study — TelcoBeam Networks

TelcoBeam Networks publishes a Direct Lake subscriber-churn report to 1,500 retail store leads who hold Read + Build on the semantic model via an App, but security policy forbids granting store leads any direct access to the underlying Lakehouse or SQL analytics endpoint. Each store lead must see only rows matching their Microsoft Entra email address.

Questions in this block:

1. How must the `SubscriberChurn` Direct Lake semantic model connect to `ChurnLakehouse` so the 1,500 store leads can query reports and build thin visuals without holding any permissions on `ChurnLakehouse` or its SQL endpoint? _(B)_
2. Complete the dynamic DAX RLS predicate `____` on `'DimStoreLead'` so each store lead sees only rows matching their signed-in Microsoft Entra email? _(B)_
3. Before publishing the App to all 1,500 store leads, how do you verify both the DAX RLS predicate and effective workspace/item permissions for `lead42@telcobeam.com`? _(B)_
