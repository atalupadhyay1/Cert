"""Load 600 authored AI-200 items. Source order is preserved; export shuffles options."""
from pathlib import Path
from terms import TERMS
HERE = Path(__file__).resolve().parent
DOMAINS = {
    1: 'Develop containerized solutions on Azure',
    2: 'Develop AI solutions by using Azure data management services',
    3: 'Connect to and consume Azure services',
    4: 'Secure, monitor, troubleshoot Azure solutions',
}
TOPICS = {
    1: 'Full-Length Mock Exam 1', 2: 'Full-Length Mock Exam 2', 3: 'Full-Length Mock Exam 3',
    4: 'Full-Length Mock Exam 4', 5: 'Full-Length Mock Exam 5', 6: 'Full-Length Mock Exam 6',
}
# Local study-map IDs, not Microsoft objective numbers.
SKILLS = {
    '1.1': 'Container Image Lifecycle in Azure Container Registry',
    '1.2': 'Automated Image Builds with ACR Tasks',
    '1.3': 'Container Deployment to Azure App Service',
    '1.4': 'Container Apps Deployment and Revisions',
    '1.5': 'Event-Driven Scaling with KEDA',
    '1.6': 'AKS Deployment with Manifests',
    '1.7': 'Container Logs, Events, and Connectivity',
    '2.1': 'Cosmos DB SDK Access and Queries',
    '2.2': 'Cosmos DB Indexing Policies and Request Units',
    '2.3': 'Cosmos DB Consistency Levels',
    '2.4': 'Cosmos DB Vector Search and Embeddings',
    '2.5': 'Cosmos DB Change Feed Processing',
    '2.6': 'PostgreSQL Connection and Schema Modeling',
    '2.7': 'pgvector Indexing and Query Latency',
    '2.8': 'PostgreSQL Compute, Memory, and Storage Sizing',
    '2.9': 'PostgreSQL RAG with Metadata Filters',
    '2.10': 'PostgreSQL Connection Optimization',
    '2.11': 'Azure Managed Redis Caching and Invalidation',
    '2.12': 'Azure Managed Redis Vector Indexing',
    '3.1': 'Service Bus Queues and Sessions',
    '3.2': 'Service Bus Topics, Subscriptions, and Filters',
    '3.3': 'Service Bus Dead-Lettering and Retries',
    '3.4': 'Event Grid Filters, Custom Events, and Retries',
    '3.5': 'Azure Functions Triggers and Bindings',
    '3.6': 'Function App Configuration and Deployment',
    '4.1': 'Key Vault Secret Storage, Rotation, and Retrieval',
    '4.2': 'App Configuration Settings and Feature Flags',
    '4.3': 'Distributed Tracing with OpenTelemetry',
    '4.4': 'KQL Queries for Logs and Metrics',
    '4.5': 'Identity-Based Access for Application Services',
}
VALID_TASKS = set(SKILLS)
# The published page states 25-30% in the domain heading and 30-35% in the
# skills-at-a-glance list; its change log records that the data domain's share
# increased. 30% is the only value inside both statements, so it is enforced.
OFFICIAL_WEIGHTS = {1: (20, 25), 2: (30, 30), 3: (20, 25), 4: (20, 25)}
# 100-item exams: 24/30/24/22 percent, inside every published range.
ALLOCATIONS = {n: {1: 24, 2: 30, 3: 24, 4: 22} for n in range(1, 7)}
TYPE_PLAN = {'multiple-choice': 76, 'multi-select': 16, 'ordering': 8}
CASE_STUDIES = 4
BANK = {}
for number in TOPICS:
    records = []
    path = HERE / 'questions' / f'{number}.txt'
    for line_number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip() or line.startswith('#'):
            continue
        parts = [x.strip() for x in line.split('|')]
        if len(parts) != 6:
            raise ValueError(f'{path.name}:{line_number}: expected 6 fields')
        skill, kind, answers, distractors, question, reason = parts
        answer_keys = [x.strip() for x in answers.split(',') if x.strip()]
        distractor_keys = [x.strip() for x in distractors.split(',') if x.strip()]
        records.append(dict(id=f'T{number}-Q{len(records) + 1:03}', task=skill,
                            domain=int(skill.split('.')[0]), kind=kind,
                            answers=answer_keys, distractors=distractor_keys,
                            keys=answer_keys + distractor_keys,
                            question=question, reason=reason, line=line_number))
    BANK[number] = records
