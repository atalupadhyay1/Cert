"""Load 600 authored Associate Data Practitioner items.

Google publishes 50-60 multiple choice and multiple select questions for this
exam and no case-study component, so the bank carries no case stems and the
exporter has no case path.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent
DOMAINS = {
    1: 'Data Preparation and Ingestion',
    2: 'Data Analysis and Presentation',
    3: 'Data Pipeline Orchestration',
    4: 'Data Management',
}
TOPICS = {1: 'Full-Length Mock Exam 1', 2: 'Full-Length Mock Exam 2', 3: 'Full-Length Mock Exam 3',
          4: 'Full-Length Mock Exam 4', 5: 'Full-Length Mock Exam 5', 6: 'Full-Length Mock Exam 6'}
SUBTITLES = {
    1: 'Ingestion, Reporting, Pipelines, and Access',
    2: 'Files, Formats, Dashboards, and Governance',
    3: 'Streaming, Scheduling, Modelling, and Recovery',
    4: 'Warehouse Analytics, Orchestration, and Key Management',
    5: 'Landing Zones, Visualisation, and Data Sharing',
    6: 'Integration, Machine Learning, and Lifecycle Control',
}
# Local study-map IDs, not Google objective numbers.
SKILLS = {
    '1.1': 'ETL, ELT, and ETLT Methodologies',
    '1.2': 'Data Quality Assessment and Cleaning',
    '1.3': 'Transfer Tool Selection',
    '1.4': 'Data Formats',
    '1.5': 'Extraction Tool Selection',
    '1.6': 'Storage Solution Selection',
    '1.7': 'Storage Location Types',
    '1.8': 'Structured, Semi-Structured, and Unstructured Data',
    '1.9': 'Loading with CLIs and Client Libraries',
    '2.1': 'BigQuery SQL for Reporting',
    '2.2': 'Colab Enterprise and Jupyter Notebooks',
    '2.3': 'Business Question Analysis',
    '2.4': 'Looker Dashboards',
    '2.5': 'Looker and Looker Studio Comparison',
    '2.6': 'LookML Parameters',
    '2.7': 'BigQuery ML and AutoML Use Cases',
    '2.8': 'Remote Gemini Models in BigQuery',
    '2.9': 'ML Project Planning',
    '2.10': 'BigQuery ML Training and Evaluation',
    '2.11': 'BigQuery ML Inference',
    '2.12': 'Model Registry',
    '3.1': 'Transformation Tool Selection',
    '3.2': 'ELT and ETL Pipeline Design',
    '3.3': 'Scheduled Queries and Job Scheduling',
    '3.4': 'Dataflow Job Monitoring',
    '3.5': 'Logs and Monitoring Review',
    '3.6': 'Orchestration Solution Selection',
    '3.7': 'Event-Driven Ingestion with Pub/Sub',
    '3.8': 'Eventarc Triggers',
    '4.1': 'IAM Least Privilege',
    '4.2': 'Basic, Predefined, and Custom Roles',
    '4.3': 'Cloud Storage Access Control',
    '4.4': 'Analytics Hub Data Sharing',
    '4.5': 'Cloud Storage Classes',
    '4.6': 'Lifecycle Rules and Expiration',
    '4.7': 'Archiving Services',
    '4.8': 'Backup and Recovery',
    '4.9': 'Replication',
    '4.10': 'Primary and Secondary Locations',
    '4.11': 'CMEK, CSEK, and GMEK',
    '4.12': 'Cloud KMS',
    '4.13': 'Encryption in Transit and at Rest',
}
VALID_TASKS = set(SKILLS)
# Google publishes one approximate weight per section; these total exactly 100.
OFFICIAL_WEIGHTS = {1: 30.0, 2: 27.0, 3: 18.0, 4: 25.0}
# 100-item exams: the published weights are already whole items, so no
# rounding correction is needed anywhere in this course.
ALLOCATIONS = {n: {1: 30, 2: 27, 3: 18, 4: 25} for n in range(1, 7)}
# Every exam uses the same per-skill template, so the six sets are comparable
# and every local study area is exercised in each one.
SKILL_PLAN = {
    '1.1': 4, '1.2': 4, '1.3': 4, '1.4': 4, '1.5': 3, '1.6': 4, '1.7': 3, '1.8': 2, '1.9': 2,
    '2.1': 4, '2.2': 2, '2.3': 2, '2.4': 3, '2.5': 2, '2.6': 3, '2.7': 3, '2.8': 2, '2.9': 2,
    '2.10': 2, '2.11': 1, '2.12': 1,
    '3.1': 4, '3.2': 2, '3.3': 3, '3.4': 2, '3.5': 2, '3.6': 3, '3.7': 1, '3.8': 1,
    '4.1': 3, '4.2': 2, '4.3': 2, '4.4': 2, '4.5': 3, '4.6': 2, '4.7': 2, '4.8': 2, '4.9': 2,
    '4.10': 1, '4.11': 2, '4.12': 1, '4.13': 1,
}
# Multi-select items per official domain, 5 + 4 + 3 + 4 = 16.
MULTI_PLAN = {1: 5, 2: 4, 3: 3, 4: 4}
TYPE_PLAN = {'multiple-choice': 84, 'multi-select': 16}
ITEM_TOTAL = sum(TYPE_PLAN.values())
BANK = {}
for number in TOPICS:
    records = []
    path = HERE / 'questions' / f'{number}.txt'
    for line_number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip() or line.startswith('#'):
            continue
        parts = [x.strip() for x in line.split('|')]
        if len(parts) != 6:
            raise ValueError(f'{path.name}:{line_number}: expected 6 fields, got {len(parts)}')
        skill, kind, answers, distractors, question, reason = parts
        answer_keys = [x.strip() for x in answers.split(',') if x.strip()]
        distractor_keys = [x.strip() for x in distractors.split(',') if x.strip()]
        records.append(dict(id=f'T{number}-Q{len(records) + 1:03}', task=skill,
                            domain=int(skill.split('.')[0]), kind=kind,
                            answers=answer_keys, distractors=distractor_keys,
                            keys=answer_keys + distractor_keys,
                            question=question, reason=reason, line=line_number))
    BANK[number] = records
