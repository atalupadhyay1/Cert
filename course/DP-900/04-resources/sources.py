"""Official Microsoft Learn source links for Microsoft Exam DP-900 (July 21, 2026 study guide)."""

STUDY_GUIDE_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900'
CERTIFICATION_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/'
EXAM_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/exams/dp-900/'
EXPIRATION_POLICY_URL = 'https://learn.microsoft.com/en-us/credentials/support/credential-expiration-policies'
EXAM_EXPERIENCE_URL = 'https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience'

SKILL_SOURCES = {
    # Domain 1: Describe core data concepts (25-30%)
    '1.1': (
        'Explore core data concepts — Identify data formats (structured data)',
        'https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats',
    ),
    '1.2': (
        'Explore core data concepts — Identify data formats (semi-structured data)',
        'https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats',
    ),
    '1.3': (
        'Explore core data concepts — Identify data formats (unstructured data)',
        'https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats',
    ),
    '1.4': (
        'Explore core data concepts — Explore file storage (CSV, JSON, Avro, ORC, Parquet)',
        'https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage',
    ),
    '1.5': (
        'Explore core data concepts — Explore databases (relational and non-relational stores)',
        'https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases',
    ),
    '1.6': (
        'Explore data roles and services — Identify Azure data services',
        'https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services',
    ),
    '1.7': (
        'Explore core data concepts — Explore transactional data processing (OLTP and ACID)',
        'https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing',
    ),
    '1.8': (
        'Explore core data concepts — Explore analytical data processing (OLAP)',
        'https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing',
    ),
    '1.9': (
        'Explore data roles and services — Database administrator responsibilities',
        'https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles',
    ),
    '1.10': (
        'Explore data roles and services — Data engineer responsibilities',
        'https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles',
    ),
    '1.11': (
        'Explore data roles and services — Data analyst responsibilities',
        'https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles',
    ),
    # Domain 2: Identify considerations for relational data on Azure (20-25%)
    '2.1': (
        'Explore fundamental relational data concepts — Understand relational data',
        'https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data',
    ),
    '2.2': (
        'Explore fundamental relational data concepts — Understand normalization',
        'https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization',
    ),
    '2.3': (
        'Explore fundamental relational data concepts — Explore SQL statements',
        'https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql',
    ),
    '2.4': (
        'Explore fundamental relational data concepts — Describe database objects',
        'https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects',
    ),
    '2.5': (
        'Explore relational database services in Azure — Describe Azure SQL services and capabilities',
        'https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/2-azure-sql',
    ),
    '2.6': (
        'Explore relational database services in Azure — Describe Azure services for open-source databases',
        'https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/3-azure-database-open-source',
    ),
    # Domain 3: Describe considerations for working with non-relational data on Azure (15-20%)
    '3.1': (
        'Explore Azure Storage for nonrelational data — Blob storage, ADLS Gen2, and OneLake',
        'https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage',
    ),
    '3.2': (
        'Explore Azure Storage for nonrelational data — Explore Azure Files',
        'https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files',
    ),
    '3.3': (
        'Explore Azure Storage for nonrelational data — Explore Azure Tables',
        'https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables',
    ),
    '3.4': (
        'Explore fundamentals of Azure Cosmos DB — Describe Azure Cosmos DB',
        'https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/2-describe-azure-cosmos-db',
    ),
    '3.5': (
        'Explore fundamentals of Azure Cosmos DB — Identify Azure Cosmos DB APIs',
        'https://learn.microsoft.com/en-us/training/modules/explore-non-relational-data-stores-azure/3-cosmos-db-apis',
    ),
    # Domain 4: Describe an analytics workload on Azure (25-30%)
    '4.1': (
        'Explore fundamentals of large-scale analytics — Explore data ingestion pipelines',
        'https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines',
    ),
    '4.2': (
        'Explore fundamentals of large-scale analytics — Explore analytical data stores',
        'https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores',
    ),
    '4.3': (
        'Explore fundamentals of large-scale analytics — Data warehousing and Microsoft Fabric',
        'https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing',
    ),
    '4.4': (
        'Explore fundamentals of real-time analytics — Understand batch and stream processing',
        'https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream',
    ),
    '4.5': (
        'Explore fundamentals of real-time analytics — Fabric Real-Time Intelligence and Spark Structured Streaming',
        'https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/4-fabric-real-time-intelligence',
    ),
    '4.6': (
        'Explore fundamentals of data visualization with Power BI — Describe Power BI capabilities',
        'https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview',
    ),
    '4.7': (
        'Design semantic models and star schemas in Power BI',
        'https://learn.microsoft.com/en-us/power-bi/guidance/star-schema',
    ),
    '4.8': (
        'Visualization types in Power BI',
        'https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a',
    ),
}
