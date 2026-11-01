# Curriculum Outline — Microsoft Exam DP-900: Microsoft Azure Data Fundamentals

## Course Structure Overview

- **Course Format:** Udemy Practice Test-Only Course (`6` full-length practice exams × `100` questions = `600` unique questions)
- **Target Credential:** `Microsoft Certified: Azure Data Fundamentals` (`Beginner` / Fundamentals · **no prerequisite** · **never expires**)
- **Official Study-Guide Baseline:** **July 21, 2026** ([Microsoft Learn DP-900 Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900))
- **Certification Status:** **Active** (`Retirement date: none`)
- **Timing & Closed-Book Guidance:** Live DP-900 gives **45 minutes** for **40–60 standalone questions** (`~45–67.5 sec/question`), is **strictly closed-book** (no split-screen Microsoft Learn access), and contains **zero case studies and zero live labs**. Set Udemy's timer to **75 minutes** per 100-question exam (`45 sec/question` live pace) or **45 minutes** for a high-speed recall drill.

---

## What Changed in the July 21, 2026 DP-900 Study Guide & Modern Learn Modules

1. **Describe ways to represent data (`1.1`–`1.3`):** Clarified distinctions across structured tabular schemas, semi-structured self-describing formats (`JSON`, `XML`, `Avro`), and unstructured binary blobs.
2. **Describe the capabilities of Azure storage (`3.1`–`3.3`):** Alongside **Azure Blob Storage** (`Block`, `Append`, `Page` blobs; online `Hot`, `Cool`, `Cold` tiers vs offline `Archive` tier), **Azure Data Lake Storage Gen2** (`Hierarchical Namespace`), **Azure Files** (`SMB 3.0` / `NFS 4.1` + `Azure File Sync`), and **Azure Table storage** (`PartitionKey` + `RowKey`), DP-900 training explicitly introduces **Microsoft OneLake in Fabric** (`Shortcuts`, unified tenant SaaS data lake).
3. **Large-Scale & Real-Time Analytics (`4.1`–`4.5`):** Emphasizes **Microsoft Fabric** (`Lakehouse`, `Warehouse`, `Data Factory` / `Dataflows Gen2`, `OneLake`, `Direct Lake`) and **Microsoft Fabric Real-Time Intelligence** (`Eventstream`, `Eventhouse` `KQL` databases, `Real-Time Dashboards`, `Activator`) alongside **Azure Databricks**, **Azure Synapse Analytics**, **Azure HDInsight**, **Azure Event Hubs**, **Azure Stream Analytics**, and **Apache Spark Structured Streaming**.
4. **Retired Legacy Services Removed:** Uses **Microsoft Entra ID** (replacing legacy Azure AD naming), **Azure Migrate** (replacing standalone Data Migration Assistant retired July 2025), **Azure Database for PostgreSQL — Flexible Server** and **Azure Database for MySQL — Flexible Server** (reflecting retirement of Single Server and MariaDB), and the five active **Azure Cosmos DB APIs** (`NoSQL`, `MongoDB`, `Apache Cassandra`, `Apache Gremlin`, `Table`).

---

## Six-Exam Progression & Industry Themes

| Exam | Udemy Practice-Test Title | Industry Context & Core Focus | Questions | Recommended Timer |
| :---: | :--- | :--- | :---: | :---: |
| **1** | `Full-Length Mock Exam 1: Omnichannel Retail & E-Commerce` | `VeloMart Retail` — Data formats, ACID OLTP vs star OLAP, Azure SQL SKUs, OneLake, Cosmos DB APIs & Power BI | `100` | `75 min` |
| **2** | `Full-Length Mock Exam 2: Healthcare Clinical & Telemetry` | `CarePulse Hospitals` — FHIR/HL7 semi-structured data, 3NF, Azure Migrate, SQL MI, Cold/Archive tiers, Fabric RTI & `.rdl` reports | `100` | `75 min` |
| **3** | `Full-Length Mock Exam 3: Smart City Transit & Municipal` | `MetroPulse Transit` — SQL joins/views/sprocs, PostgreSQL PostGIS, Azure Files SMB/NFS, stream windows & map/waterfall visuals | `100` | `75 min` |
| **4** | `Full-Length Mock Exam 4: Connected Manufacturing & IIoT` | `ForgeWorks Manufacturing` — Parquet/Avro, clustered/nonclustered indexes, ADLS Gen2, Cassandra/Gremlin & Fabric Eventhouse KQL | `100` | `75 min` |
| **5** | `Full-Length Mock Exam 5: Digital Banking & Fraud Risk` | `CrestVault Digital Bank` — ACID guarantees, DCL permissions, Elastic Pools vs VMs, Cosmos consistency SLAs & Databricks Spark | `100` | `75 min` |
| **6** | `Full-Length Mock Exam 6: Global Logistics & Clean Energy` | `NordGrid Logistics` — Data roles, MySQL Flexible Server, Blob lifecycle rules, Fabric Lakehouse ELT & Power BI Direct Lake / DAX | `100` | `75 min` |

---

## Complete 30-Skill Blueprint Allocation (Identical Across Every Exam)

### Domain 1 — Describe core data concepts (`25–30%` Official → `28` Questions / Exam)
- **Describe ways to represent data (`7` items):** `1.1` Structured data (`2`), `1.2` Semi-structured data (`3`), `1.3` Unstructured data (`2`)
- **Identify options for data storage (`9` items):** `1.4` Common data file formats (`3`), `1.5` Common data stores & databases (`3`), `1.6` Azure datastores for common use cases (`3`)
- **Describe common data workloads (`6` items):** `1.7` Transactional OLTP & ACID workloads (`3`), `1.8` Analytical OLAP workloads (`3`)
- **Identify roles and responsibilities for data workloads (`6` items):** `1.9` Database administrators (`2`), `1.10` Data engineers (`2`), `1.11` Data analysts (`2`)

### Domain 2 — Identify considerations for relational data on Azure (`20–25%` Official → `24` Questions / Exam)
- **Describe relational concepts (`16` items):** `2.1` Features of relational data & keys (`4`), `2.2` Normalization 1NF/2NF/3NF (`4`), `2.3` Common SQL statements DDL/DML/DCL/Joins (`4`), `2.4` Common database objects views/sprocs/indexes (`4`)
- **Describe relational Azure data services (`8` items):** `2.5` Azure SQL Database, SQL Managed Instance & SQL Server on Azure VMs (`5`), `2.6` Open-source PostgreSQL & MySQL Flexible Server (`3`)

### Domain 3 — Describe considerations for working with non-relational data on Azure (`15–20%` Official → `20` Questions / Exam)
- **Describe the capabilities of Azure storage (`11` items):** `3.1` Azure Blob storage, access tiers, ADLS Gen2 & OneLake (`5`), `3.2` Azure Files & Azure File Sync (`3`), `3.3` Azure Table storage (`3`)
- **Describe the capabilities and features of Azure Cosmos DB (`9` items):** `3.4` Azure Cosmos DB global distribution, RUs & consistency (`4`), `3.5` Azure Cosmos DB APIs (`5`)

### Domain 4 — Describe an analytics workload on Azure (`25–30%` Official → `28` Questions / Exam)
- **Describe common elements of large-scale analytics (`10` items):** `4.1` Data ingestion & ELT/ETL processing (`3`), `4.2` Analytical data stores, lakehouses & star/snowflake schemas (`3`), `4.3` Microsoft Fabric, Azure Databricks, Synapse & HDInsight (`4`)
- **Describe considerations for real-time data analytics (`8` items):** `4.4` Batch vs streaming & windowing functions (`4`), `4.5` Event Hubs, Stream Analytics, Fabric Real-Time Intelligence & Spark Structured Streaming (`4`)
- **Describe data visualization in Microsoft Power BI (`10` items):** `4.6` Power BI Desktop, Service & Report Builder capabilities (`3`), `4.7` Power BI semantic models, relationships & DAX (`4`), `4.8` Appropriate Power BI visualizations (`3`)
