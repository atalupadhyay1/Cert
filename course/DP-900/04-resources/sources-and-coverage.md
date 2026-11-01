# Official Microsoft Learn Sources & 30-Skill Coverage (`Exam DP-900`)

## Primary Exam & Credential Sources (Verified November 1, 2026)

1. **Official Study Guide (`July 21, 2026` Baseline):** <https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900>
2. **Certification Overview (`Microsoft Certified: Azure Data Fundamentals`):** <https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/>
3. **Exam Overview (`Exam DP-900`):** <https://learn.microsoft.com/en-us/credentials/certifications/exams/dp-900/>
4. **Course DP-900T00-A (`Introduction to Microsoft Azure Data`):** <https://learn.microsoft.com/en-us/training/courses/dp-900t00/>
5. **Credential Expiration Policies (Fundamentals Never Expire):** <https://learn.microsoft.com/en-us/credentials/support/credential-expiration-policies>
6. **Exam Duration & Closed-Book Fundamentals Experience:** <https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience>

---

## Domain-Level Microsoft Learn Documentation Anchors

### Domain 1 — Describe core data concepts (`25–30%` → `28` items/set, `168` total)
- **Explore core data concepts (`structured`, `semi-structured`, `unstructured`, file formats, databases, `OLTP`, `OLAP`):** <https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/>
- **Explore data roles and services (`DBA`, `Data Engineer`, `Data Analyst`, Azure data services):** <https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/>

### Domain 2 — Identify considerations for relational data on Azure (`20–25%` → `24` items/set, `144` total)
- **Explore fundamental relational data concepts (keys, `1NF`/`2NF`/`3NF`, `DDL`/`DML`/`DCL`, views, stored procedures, indexes):** <https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/>
- **Explore relational database services in Azure (`Azure SQL Database`, `SQL Managed Instance`, `SQL Server on Azure VMs`, `Azure Migrate`, `PostgreSQL` & `MySQL` Flexible Server):** <https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/>

### Domain 3 — Describe considerations for working with non-relational data on Azure (`15–20%` → `20` items/set, `120` total)
- **Explore Azure Storage for nonrelational data (`Blob Storage` types & `Hot`/`Cool`/`Cold`/`Archive` tiers, `ADLS Gen2`, `Microsoft OneLake`, `Azure Files` & `File Sync`, `Azure Table storage`):** <https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/>
- **Explore fundamentals of Azure Cosmos DB (global distribution, `RU/s` & Serverless, 5 consistency levels, `NoSQL`/`MongoDB`/`Cassandra`/`Gremlin`/`Table` APIs):** <https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/>

### Domain 4 — Describe an analytics workload on Azure (`25–30%` → `28` items/set, `168` total)
- **Explore fundamentals of large-scale analytics (`ELT` vs `ETL`, `Data Factory`/`Dataflows Gen2`, `star`/`snowflake` schemas, `Delta Lake` lakehouses, `Microsoft Fabric`, `Azure Databricks`, `Azure Synapse`, `HDInsight`):** <https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/>
- **Explore fundamentals of real-time analytics (batch vs streaming, window functions, `Event Hubs`, `Stream Analytics`, `Microsoft Fabric Real-Time Intelligence`, `Spark Structured Streaming`):** <https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/>
- **Power BI capabilities, star-schema semantic modeling, `DAX`, and visualizations:** <https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview> & <https://learn.microsoft.com/en-us/power-bi/guidance/star-schema>

---

## Originality & Modern Accuracy Safeguards

- **Zero Recalled Content & Zero Microsoft Fictional Companies:** All 600 questions use six original industry organizations (`VeloMart Retail`, `CarePulse Hospitals`, `MetroPulse Transit`, `ForgeWorks Manufacturing`, `CrestVault Digital Bank`, `NordGrid Logistics`) — never `Contoso`, `Fabrikam`, `AdventureWorks`, `Northwind`, `Litware`, `Tailwind Traders`, `Wide World Importers`, `Woodgrove`, `Adatum`, `VanArsdel`, `Coho`, or `Trey Research`.
- **Zero Cross-Course Overlap:** `test_course.py` verifies `0` stem overlap across all `5,400` questions in the repository's nine sibling Microsoft courses (`PL-900`, `PL-200`, `PL-400`, `PL-500`, `PL-600`, `AZ-204`, `AZ-400`, `AZ-401`, `DP-600`).
- **100% Term Utilization:** All `143 / 143` canonical option and sequence definitions in `terms.py` and `sequences.py` are exercised across the 600-item bank, with maximum pairwise stem Jaccard similarity `0.542` (`< 0.72` threshold).
