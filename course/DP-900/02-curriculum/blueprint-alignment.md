# DP-900: Microsoft Azure Data Fundamentals — Blueprint Alignment Report

## Official Exam & Fundamentals Credential Metadata

- **Exam:** `DP-900: Microsoft Azure Data Fundamentals` *(Active — Retirement date: none)*
- **Credential:** `Microsoft Certified: Azure Data Fundamentals`
- **Prerequisite & Expiration Policy:** None (Beginner / Fundamentals certification; never expires and requires no annual renewal) (https://learn.microsoft.com/en-us/credentials/support/credential-expiration-policies)
- **Current Official Study Guide Baseline:** `July 21, 2026` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)
- **Certification Overview:** https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/
- **Exam Overview:** https://learn.microsoft.com/en-us/credentials/certifications/exams/dp-900/
- **Live Fundamentals Exam Format:** `45 minutes` exam time (`~65 minutes` seat duration), `40–60` standalone questions, `700 / 1000` scaled pass, `$99 USD` (US), **closed-book** (no split-screen Microsoft Learn access), **0 case studies**, **0 live labs**
- **Course Bank Volume:** `6 practice exams x 100 questions = 600 unique questions` (`0` duplicate stems, `0` duplicate explanations, `0` artificial case studies)
- **Option Library Coverage:** `143 / 143` canonical terms exercised (`100.0%`), max pairwise stem Jaccard similarity `0.542` (`E1Q045` vs `E5Q045`)

## Domain Weighting Verification (Every Practice Set = 100 Questions)

| Domain | Official Weight | Target / Set | Set 1 | Set 2 | Set 3 | Set 4 | Set 5 | Set 6 | Total (600) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Domain 1:** Describe core data concepts | 25–30% | 28% | 28 | 28 | 28 | 28 | 28 | 28 | **168** (28.0%) |
| **Domain 2:** Identify considerations for relational data on Azure | 20–25% | 24% | 24 | 24 | 24 | 24 | 24 | 24 | **144** (24.0%) |
| **Domain 3:** Describe considerations for working with non-relational data on Azure | 15–20% | 20% | 20 | 20 | 20 | 20 | 20 | 20 | **120** (20.0%) |
| **Domain 4:** Describe an analytics workload on Azure | 25–30% | 28% | 28 | 28 | 28 | 28 | 28 | 28 | **168** (28.0%) |
| **Total** | **100%** | **100** | **100** | **100** | **100** | **100** | **100** | **100** | **600** |

## Question-Format & Pattern Telemetry Across Practice Sets

| Set | Focus | Single (`S`) | Sequence (`O`) | Multi-2 (`M2`) | Multi-3 (`M3`) | `____` Completions | `Proposed solution:` | Max Q Chars | MC Key Pos `1/2/3/4` |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Omnichannel Retail & E-Commerce — Data Formats, OLTP/OLAP, Azure SQL, Cosmos DB NoSQL, OneLake & Power BI | 76 | 8 | 13 | 3 | 27 | 8 | 414 | `21/21/21/21` |
| 2 | Healthcare Clinical & Patient Telemetry — Normalization, SQL Managed Instance, Blob Tiers, Fabric RTI & Paginated Reports | 76 | 8 | 13 | 3 | 24 | 6 | 331 | `21/21/21/21` |
| 3 | Smart City Transit & Municipal Services — SQL Joins/Views, PostgreSQL Flexible Server, Azure Files, Stream Windows & Maps | 76 | 8 | 13 | 3 | 26 | 6 | 358 | `21/21/21/21` |
| 4 | Connected Manufacturing & Industrial IoT — Parquet/Avro, Indexes, ADLS Gen2, Table Storage, Cassandra/Gremlin & Eventhouse | 76 | 8 | 13 | 3 | 23 | 6 | 343 | `21/21/21/21` |
| 5 | Digital Banking & Fraud Risk Operations — ACID Guarantees, 3NF, Elastic Pools/VMs, Cosmos Consistency & Azure Databricks | 76 | 8 | 13 | 3 | 29 | 6 | 323 | `21/21/21/21` |
| 6 | Global Logistics & Clean Energy Grid — Data Roles, MySQL Flexible Server, Lifecycle Policies, Fabric Lakehouse & DAX KPIs | 76 | 8 | 13 | 3 | 26 | 6 | 332 | `21/21/21/21` |

## Granular Skill Coverage Across All 30 Official July 21, 2026 Study-Guide Skills

| Skill ID | Domain | Official Skill Measured | Per Set | 6-Set Total | Primary Microsoft Learn Reference |
| :---: | :---: | :--- | :---: | :---: | :--- |
| `1.1` | D1 | Describe the features of structured data | 2 | 12 | [Explore core data concepts — Identify data formats (structured data)](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats) |
| `1.2` | D1 | Describe the features of semi-structured data | 3 | 18 | [Explore core data concepts — Identify data formats (semi-structured data)](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats) |
| `1.3` | D1 | Describe the features of unstructured data | 2 | 12 | [Explore core data concepts — Identify data formats (unstructured data)](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats) |
| `1.4` | D1 | Describe common formats for data files | 3 | 18 | [Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet)](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage) |
| `1.5` | D1 | Describe features of common data stores including databases | 3 | 18 | [Explore core data concepts — Explore databases (relational and non-relational stores)](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases) |
| `1.6` | D1 | Identify Azure datastores for common use cases | 3 | 18 | [Explore data roles and services — Identify Azure data services](https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services) |
| `1.7` | D1 | Describe features of transactional workloads | 3 | 18 | [Explore core data concepts — Explore transactional data processing (OLTP and ACID)](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing) |
| `1.8` | D1 | Describe features of analytical workloads | 3 | 18 | [Explore core data concepts — Explore analytical data processing (OLAP)](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing) |
| `1.9` | D1 | Describe responsibilities for database administrators | 2 | 12 | [Explore data roles and services — Database administrator responsibilities](https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles) |
| `1.10` | D1 | Describe responsibilities for data engineers | 2 | 12 | [Explore data roles and services — Data engineer responsibilities](https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles) |
| `1.11` | D1 | Describe responsibilities for data analysts | 2 | 12 | [Explore data roles and services — Data analyst responsibilities](https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles) |
| `2.1` | D2 | Identify features of relational data | 4 | 24 | [Explore fundamental relational data concepts — Understand relational data](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data) |
| `2.2` | D2 | Describe normalization and why it is used | 4 | 24 | [Explore fundamental relational data concepts — Understand normalization](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization) |
| `2.3` | D2 | Identify common structured query language (SQL) statements | 4 | 24 | [Explore fundamental relational data concepts — Explore SQL statements](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql) |
| `2.4` | D2 | Identify common database objects | 4 | 24 | [Explore fundamental relational data concepts — Describe database objects](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects) |
| `2.5` | D2 | Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines | 5 | 30 | [Explore relational database services in Azure — Describe Azure SQL services and capabilities](https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql) |
| `2.6` | D2 | Identify Azure database services for open-source database systems | 3 | 18 | [Explore relational database services in Azure — Describe Azure services for open-source databases](https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source) |
| `3.1` | D3 | Describe features of Azure Blob storage | 5 | 30 | [Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake](https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage) |
| `3.2` | D3 | Describe features of Azure Files | 3 | 18 | [Explore Azure Storage for nonrelational data — Explore Azure Files](https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files) |
| `3.3` | D3 | Describe features of Azure Table storage | 3 | 18 | [Explore Azure Storage for nonrelational data — Explore Azure Tables](https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables) |
| `3.4` | D3 | Identify use cases for Azure Cosmos DB | 4 | 24 | [Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB](https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db) |
| `3.5` | D3 | Describe Azure Cosmos DB APIs | 5 | 30 | [Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs](https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis) |
| `4.1` | D4 | Describe considerations for data ingestion and processing | 3 | 18 | [Explore fundamentals of large-scale analytics — Explore data ingestion pipelines](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines) |
| `4.2` | D4 | Describe options for analytical data stores | 3 | 18 | [Explore fundamentals of large-scale analytics — Explore analytical data stores](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores) |
| `4.3` | D4 | Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric | 4 | 24 | [Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing) |
| `4.4` | D4 | Describe the difference between batch and streaming data | 4 | 24 | [Explore fundamentals of real-time analytics — Understand batch and stream processing](https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream) |
| `4.5` | D4 | Identify Microsoft cloud services for real-time analytics | 4 | 24 | [Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming](https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence) |
| `4.6` | D4 | Identify the capabilities of Power BI | 3 | 18 | [Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities](https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview) |
| `4.7` | D4 | Describe features of data models in Power BI | 4 | 24 | [Design semantic models and star schemas in Power BI](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema) |
| `4.8` | D4 | Identify appropriate visualizations for data | 3 | 18 | [Visualization types in Power BI](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a) |
