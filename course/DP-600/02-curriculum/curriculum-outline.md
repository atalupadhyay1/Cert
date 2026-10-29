# 🗺️ Curriculum Outline — Microsoft Exam DP-600 (`6 × 100 = 600` Questions)

Course curriculum and blueprint mapping for **Microsoft Exam DP-600: Implementing Analytics Solutions Using Microsoft Fabric** (**Microsoft Certified: Fabric Analytics Engineer Associate**), aligned to Microsoft Learn's **October 19, 2026** study guide (`700 / 1000` scaled passing score · `100 minutes` exam time · core query languages **SQL**, **KQL**, and **DAX** · no prerequisite certification required).

---

## 1. Course Structure (6 Practice-Test Sections)

| Section / Practice Set | Industry Vertical & Architectural Focus | Enterprise Case Studies (`4 × 3 = 12` Qs) | Domain Split (`D1 / D2 / D3`) | `____` Fills | `Proposed solution:` | Recommended Clock & Pass Target |
|---|---|---|---:|---:|---:|---|
| **Practice Test 1** (`set-1`) | Omnichannel Retail Medallion Lakehouses, Real-Time POS KQL & Direct Lake Star Schemas | `Solstice Apparel`, `CartVerve Marketplace`, `ShelfPulse POS`, `LoomCraft Home` | `26 / 47 / 27` | 24 | 7 | `100 min` · `80%+` target |
| **Practice Test 2** (`set-2`) | Healthcare Claims Warehousing, Clinical IoT Eventhouses & HIPAA Purview Governance | `AetherCare Health`, `BioTrace Diagnostics`, `MedBridge Claims`, `VitalsCore Analytics` | `26 / 47 / 27` | 24 | 8 | `100 min` · `80%+` target |
| **Practice Test 3** (`set-3`) | Global FinTech Ledger Mirroring, Fraud KQL Streams & Enterprise XMLA ALM | `ClearLedger Bank`, `FraudShield Pay`, `Meridian Wealth`, `SwiftSettle FX` | `26 / 47 / 27` | 23 | 8 | `100 min` · `80%+` target |
| **Practice Test 4** (`set-4`) | Smart Manufacturing IoT, Cold-Chain Logistics & Supply-Chain Composite Models | `TorqueLine Motors`, `ColdHaul Logistics`, `GridWorks Components`, `HarborPort Freight` | `26 / 47 / 27` | 21 | 7 | `100 min` · `82%+` target |
| **Practice Test 5** (`set-5`) | Subscription Media Streaming QoE, Ad-Tech DAX Query View & Multi-Source Direct Lake | `CineWave Stream`, `AdPulse Attribution`, `PressLine Digital`, `SoundStage Live` | `26 / 47 / 27` | 24 | 6 | `100 min` · `85%+` target |
| **Practice Test 6** (`set-6`) | Renewable Energy Grids, Telecom Fixed-Identity RLS & Public-Sector Zero-Copy Clones | `SunGrid Renewables`, `TelcoBeam Networks`, `CivicWorks Transit`, `AquaSpan Utilities` | `26 / 47 / 27` | 23 | 6 | `100 min` · `85%+` target |
| **Course Total** | **6 Distinct Enterprise Verticals** | **24 Original Case Studies (`72` Qs)** | **`156 / 282 / 162` (`600`)** | **139** | **42** | *(Note: `700 / 1000` live score is scaled, not `%`)* |

---

## 2. Per-Exam Item-Type Architecture (Identical Across Sets 1–6)

Every 100-question set enforces the exact same item-type mix and answer-key symmetry:

- **`76` single-answer scenarios (`S`)** + **`8` four-step (`→`) ordered workflows (`O`)** = **`84` `multiple-choice` rows**, balanced strictly at **`21 A / 21 B / 21 C / 21 D`** in both `practice-set-N.csv` and `case-embedded-set-N.csv`.
- **`16` `multi-select` rows** (`13` two-answer `Select two.` + `3` three-answer `Select three.`), distributed `4` in Domain 1, `8` in Domain 2 (`6 M2 + 2 M3`), and `4` in Domain 3 (`3 M2 + 1 M3`).
- **`21–24` syntax/code completion (`____`) items per set** (`139` total) across T-SQL, Spark SQL, KQL, DAX, PySpark, Power Query M, TMDL, and TMSL.
- **`6–8` `Proposed solution:` diagnostic items per set** (`42` total) mirroring Microsoft's solution-evaluation reasoning style without non-returnable adaptive lock-in.

---

## 3. Complete 41-Skill Allocation Matrix (`October 19, 2026` Study Guide)

| Skill ID | Official DP-600 Skill Measured | Domain | Items / Set | Total (6 Sets) |
|---|---|---|---:|---:|
| `1.1` | Implement and manage workspace roles (`Admin`, `Member`, `Contributor`, `Viewer`) | D1 | 3 | 18 |
| `1.2` | Implement and manage item-level permissions (`Build`, `Read`, `ReadData`, `ReadAll`, SSO vs fixed identity) | D1 | 2 | 12 |
| `1.3` | Implement data access controls (OneLake security, SQL RLS/CLS/OLS/DDM, Semantic Model RLS/OLS, `View as`) | D1 | 4 | 24 |
| `1.4` | Implement Microsoft Purview sensitivity labels, inheritance, encryption, and mandatory policies | D1 | 2 | 12 |
| `1.5` | Endorse items (`Promoted`, `Certified`, and `Master data`) | D1 | 2 | 12 |
| `1.6` | Configure and manage workspace Git integration (`Connect`, `Branch out`, `Commit`, `Update all`, `Undo`) | D1 | 2 | 12 |
| `1.7` | Implement Power BI Desktop projects (`.pbip`, `TMDL`, `PBIR`, `.gitignore`) | D1 | 2 | 12 |
| `1.8` | Configure and manage Deployment Pipelines, deployment rules, and `Variable library` | D1 | 3 | 18 |
| `1.9` | Perform impact analysis and end-to-end lineage triage across workspaces | D1 | 2 | 12 |
| `1.10` | Deploy and manage semantic models using XMLA endpoints (`Read Write`, ALM Toolkit, TMSL `dataOnly`) | D1 | 2 | 12 |
| `1.11` | Create and manage reusable analytics assets (`.pbit`, `.pbids`, shared Certified semantic models) | D1 | 2 | 12 |
| `2.1` | Create and manage data connections, HA On-premises gateways, and VNet data gateways | D2 | 2 | 12 |
| `2.2` | Discover data using `OneLake catalog` (`Explore` & `Govern`) and `Real-Time hub` | D2 | 2 | 12 |
| `2.3` | Ingest data using shortcuts, Database Mirroring, pipelines, Dataflow Gen2 (`Fast Copy`), and Eventstreams | D2 | 4 | 24 |
| `2.4` | Choose an analytical or operational store (`Lakehouse`, `Warehouse`, `Eventhouse`, `SQL DB in Fabric`) | D2 | 3 | 18 |
| `2.5` | Implement OneLake integration for Eventhouses (`OneLake availability`) and Import semantic models | D2 | 2 | 12 |
| `2.6` | Create views, Materialized Lake Views, functions, and Warehouse stored procedures | D2 | 3 | 18 |
| `2.7` | Enrich data by adding surrogate keys, Calendar dimensions, and vectorized PySpark columns | D2 | 3 | 18 |
| `2.8` | Implement a star schema and Slowly Changing Dimensions (Medallion, uniform grain, SCD Type 1 & Type 2) | D2 | 4 | 24 |
| `2.9` | Denormalize snowflaked dimensions into flattened Gold star tables | D2 | 2 | 12 |
| `2.10` | Aggregate data (Gold summary tables, T-SQL `GROUPING SETS`, folded Power Query `Group by`) | D2 | 3 | 18 |
| `2.11` | Merge or join data (`MERGE INTO`, `Left Anti Join`, PySpark `F.broadcast()`) | D2 | 3 | 18 |
| `2.12` | Identify and resolve duplicate data (`ROW_NUMBER()`), missing/late-arriving `-1` keys, and Data Wrangler profiling | D2 | 3 | 18 |
| `2.13` | Convert data types (`TRY_CAST` / fixed decimal) and ensure Direct Lake Delta type compatibility | D2 | 2 | 12 |
| `2.14` | Filter data preserving Power Query folding (`View Native Query`) and sargable Delta partition/file pruning | D2 | 2 | 12 |
| `2.15` | Transform data with the `Visual query editor` (`Save as view`) | D2 | 2 | 12 |
| `2.16` | Query relational data using SQL (`LAG`, three-part cross-DB queries, Time Travel `FOR TIMESTAMP AS OF`, `CLONE OF`) | D2 | 3 | 18 |
| `2.17` | Query streaming data using KQL (`summarize`, `arg_max`, `bin`, `percentile`, `parse_json`, `mv-expand`, `make-series`) | D2 | 3 | 18 |
| `2.18` | Explore and validate data using DAX (`DAX Query View`, `COLUMNSTATISTICS`, `INFO.VIEW.*`) | D2 | 2 | 12 |
| `3.1` | Choose a storage mode (`Import`, `DirectQuery`, `Dual`, `Direct Lake`) | D3 | 2 | 12 |
| `3.2` | Implement a star schema for a semantic model (`Mark as date table`, disable `Auto date/time`, `Sort by Column`) | D3 | 2 | 12 |
| `3.3` | Implement relationships (`USERELATIONSHIP`, M:M bridge `CROSSFILTER`, `Assume referential integrity`) | D3 | 3 | 18 |
| `3.4` | Write calculations that use DAX (`VAR`, `SUMX`, `KEEPFILTERS`, `OFFSET`/`WINDOW`/`INDEX`, `ISINSCOPE`) | D3 | 4 | 24 |
| `3.5` | Implement Calculation Groups (`SELECTEDMEASURE`), Dynamic Format Strings, and Field Parameters (`NAMEOF`) | D3 | 3 | 18 |
| `3.6` | Implement and manage `Large semantic model storage format` | D3 | 2 | 12 |
| `3.7` | Design and build composite models (`Direct Lake on OneLake + Import`, aggregations, `DQ for PBI models`) | D3 | 2 | 12 |
| `3.8` | Optimize report performance (`Performance Analyzer`, `Query reduction` slicer `Apply` buttons) | D3 | 2 | 12 |
| `3.9` | Improve DAX performance using DAX Studio (`Server Timings` FE/SE, `CallbackDataID`, `Clear Cache`) & VertiPaq | D3 | 2 | 12 |
| `3.10` | Optimize Direct Lake (`V-Order`, `OPTIMIZE`, `framing`, guardrails, `DirectLakeBehavior`) | D3 | 2 | 12 |
| `3.11` | Choose and migrate between `Direct Lake on OneLake` (`AzureStorage.DataLake`) and `Direct Lake on SQL` | D3 | 2 | 12 |
| `3.12` | Implement Incremental Refresh (`RangeStart`/`RangeEnd` half-open filters, `Detect data changes`, hybrid real-time) | D3 | 1 | 6 |

---

## 4. Recommended 3-Week Exam Study Plan

1. **Days 1–5 (Untimed Diagnostic & Deep Review — Mock Exams 1 & 2):** Complete Exams 1 and 2 in review mode. Read every distractor rationale and open linked `learn.microsoft.com` articles on missed skills so you also practice navigating Microsoft Learn fast (mirroring Pearson VUE's split-screen open-book feature).
2. **Days 6–12 (Syntax & Architecture Mastery — Mock Exams 3 & 4):** Focus on exact query/TMDL syntax (`____` completions across SQL, KQL, DAX, PySpark, Power Query M, and TMDL) and ordered 4-step operational workflows (`→`).
3. **Days 13–21 (Timed Dress Rehearsal — Mock Exams 5 & 6):** Sit Exams 5 and 6 under a strict **100-minute** clock (`1` minute per item — tougher pacing than the live exam's `40–60` items in `100` minutes), targeting **85%+** first-attempt accuracy.
