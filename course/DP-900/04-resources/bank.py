"""Question bank loader and blueprint constants for Microsoft Exam DP-900 (6 x 100 = 600 questions).

Aligned to the official Microsoft Learn DP-900 Study Guide (Skills measured as of July 21, 2026)
for Microsoft Certified: Azure Data Fundamentals.
"""

import re
from pathlib import Path

from sources import (
    CERTIFICATION_URL,
    EXAM_EXPERIENCE_URL,
    EXAM_URL,
    EXPIRATION_POLICY_URL,
    SKILL_SOURCES,
    STUDY_GUIDE_URL,
)
from terms import TERMS

EXAM_CODE = 'DP-900'
EXAM_TITLE = 'Microsoft Azure Data Fundamentals'
CREDENTIAL_TITLE = 'Microsoft Certified: Azure Data Fundamentals'
STUDY_GUIDE_DATE = 'July 21, 2026'
PREREQUISITES = 'None (Beginner / Fundamentals certification; never expires and requires no annual renewal)'

ITEM_TOTAL = 100

TOPICS = {
    1: 'Full-Length Mock Exam 1',
    2: 'Full-Length Mock Exam 2',
    3: 'Full-Length Mock Exam 3',
    4: 'Full-Length Mock Exam 4',
    5: 'Full-Length Mock Exam 5',
    6: 'Full-Length Mock Exam 6',
}

SUBTITLES = {
    1: 'Omnichannel Retail & E-Commerce — Data Formats, OLTP/OLAP, Azure SQL, Cosmos DB NoSQL, OneLake & Power BI',
    2: 'Healthcare Clinical & Patient Telemetry — Normalization, SQL Managed Instance, Blob Tiers, Fabric RTI & Paginated Reports',
    3: 'Smart City Transit & Municipal Services — SQL Joins/Views, PostgreSQL Flexible Server, Azure Files, Stream Windows & Maps',
    4: 'Connected Manufacturing & Industrial IoT — Parquet/Avro, Indexes, ADLS Gen2, Table Storage, Cassandra/Gremlin & Eventhouse',
    5: 'Digital Banking & Fraud Risk Operations — ACID Guarantees, 3NF, Elastic Pools/VMs, Cosmos Consistency & Azure Databricks',
    6: 'Global Logistics & Clean Energy Grid — Data Roles, MySQL Flexible Server, Lifecycle Policies, Fabric Lakehouse & DAX KPIs',
}

DOMAINS = {
    1: 'Describe core data concepts',
    2: 'Identify considerations for relational data on Azure',
    3: 'Describe considerations for working with non-relational data on Azure',
    4: 'Describe an analytics workload on Azure',
}

OFFICIAL_RANGES = {
    1: (25, 30),  # 28 per set (28.0%)
    2: (20, 25),  # 24 per set (24.0%)
    3: (15, 20),  # 20 per set (20.0%)
    4: (25, 30),  # 28 per set (28.0%)
}

PER_SET_ALLOC = {1: 28, 2: 24, 3: 20, 4: 28}
ALLOCATIONS = {n: dict(PER_SET_ALLOC) for n in range(1, 7)}

SKILLS = {
    # Domain 1: Describe core data concepts (28)
    '1.1': 'Describe the features of structured data',
    '1.2': 'Describe the features of semi-structured data',
    '1.3': 'Describe the features of unstructured data',
    '1.4': 'Describe common formats for data files',
    '1.5': 'Describe features of common data stores including databases',
    '1.6': 'Identify Azure datastores for common use cases',
    '1.7': 'Describe features of transactional workloads',
    '1.8': 'Describe features of analytical workloads',
    '1.9': 'Describe responsibilities for database administrators',
    '1.10': 'Describe responsibilities for data engineers',
    '1.11': 'Describe responsibilities for data analysts',
    # Domain 2: Identify considerations for relational data on Azure (24)
    '2.1': 'Identify features of relational data',
    '2.2': 'Describe normalization and why it is used',
    '2.3': 'Identify common structured query language (SQL) statements',
    '2.4': 'Identify common database objects',
    '2.5': 'Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines',
    '2.6': 'Identify Azure database services for open-source database systems',
    # Domain 3: Describe considerations for working with non-relational data on Azure (20)
    '3.1': 'Describe features of Azure Blob storage',
    '3.2': 'Describe features of Azure Files',
    '3.3': 'Describe features of Azure Table storage',
    '3.4': 'Identify use cases for Azure Cosmos DB',
    '3.5': 'Describe Azure Cosmos DB APIs',
    # Domain 4: Describe an analytics workload on Azure (28)
    '4.1': 'Describe considerations for data ingestion and processing',
    '4.2': 'Describe options for analytical data stores',
    '4.3': 'Describe Microsoft cloud services for large-scale analytics, including Azure Databricks and Microsoft Fabric',
    '4.4': 'Describe the difference between batch and streaming data',
    '4.5': 'Identify Microsoft cloud services for real-time analytics',
    '4.6': 'Identify the capabilities of Power BI',
    '4.7': 'Describe features of data models in Power BI',
    '4.8': 'Identify appropriate visualizations for data',
}

SKILL_PLAN = {
    # Domain 1 (28)
    '1.1': 2, '1.2': 3, '1.3': 2,
    '1.4': 3, '1.5': 3, '1.6': 3,
    '1.7': 3, '1.8': 3,
    '1.9': 2, '1.10': 2, '1.11': 2,
    # Domain 2 (24)
    '2.1': 4, '2.2': 4, '2.3': 4, '2.4': 4, '2.5': 5, '2.6': 3,
    # Domain 3 (20)
    '3.1': 5, '3.2': 3, '3.3': 3, '3.4': 4, '3.5': 5,
    # Domain 4 (28)
    '4.1': 3, '4.2': 3, '4.3': 4,
    '4.4': 4, '4.5': 4,
    '4.6': 3, '4.7': 4, '4.8': 3,
}

assert sum(SKILL_PLAN.values()) == 100
for _d, _target in PER_SET_ALLOC.items():
    assert sum(v for k, v in SKILL_PLAN.items() if int(k.split('.')[0]) == _d) == _target

VALID_TASKS = set(SKILLS)
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
TYPE_PLAN = {'multiple-choice': 76, 'ordering': 8, 'multi-select': 16}
MULTI_PLAN = {1: 5, 2: 4, 3: 3, 4: 4}  # 16 multi-select per set
COMPLETION_FLOOR = 15
PROPOSED_SOL_FLOOR = 6
QUESTIONS_DIR = Path(__file__).resolve().parent / 'questions'


def load_set(set_number: int) -> list[dict]:
    path = QUESTIONS_DIR / f'{set_number}.txt'
    if not path.exists():
        return []
    rows = []
    for line_number, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        parts = [p.replace('\\|', '|').strip() for p in re.split(r'(?<!\\)\|', line)]
        if len(parts) != 6:
            raise ValueError(f'{path.name}:{line_number}: expected 6 fields, got {len(parts)}')
        task, kind, answers_raw, distractors_raw, question, reason = parts
        if task not in VALID_TASKS:
            raise ValueError(f'{path.name}:{line_number}: unknown skill {task!r}')
        if kind not in KIND_PLAN:
            raise ValueError(f'{path.name}:{line_number}: unknown kind {kind!r}')
        answers = [a.strip() for a in answers_raw.split(',') if a.strip()]
        distractors = [d.strip() for d in distractors_raw.split(',') if d.strip()]
        domain = int(task.split('.')[0])
        rows.append({
            'id': f'E{set_number}Q{len(rows) + 1:03d}',
            'task': task,
            'domain': domain,
            'kind': kind,
            'answers': answers,
            'distractors': distractors,
            'keys': answers + distractors,
            'question': question,
            'reason': reason,
            'line': line_number,
        })
    return rows


BANK = {n: load_set(n) for n in range(1, 7)}

__all__ = [
    'ALLOCATIONS',
    'BANK',
    'CERTIFICATION_URL',
    'COMPLETION_FLOOR',
    'CREDENTIAL_TITLE',
    'DOMAINS',
    'EXAM_CODE',
    'EXAM_EXPERIENCE_URL',
    'EXAM_TITLE',
    'EXAM_URL',
    'EXPIRATION_POLICY_URL',
    'ITEM_TOTAL',
    'KIND_PLAN',
    'MULTI_PLAN',
    'OFFICIAL_RANGES',
    'PER_SET_ALLOC',
    'PREREQUISITES',
    'PROPOSED_SOL_FLOOR',
    'SKILLS',
    'SKILL_PLAN',
    'SKILL_SOURCES',
    'STUDY_GUIDE_DATE',
    'STUDY_GUIDE_URL',
    'SUBTITLES',
    'TERMS',
    'TOPICS',
    'TYPE_PLAN',
]
