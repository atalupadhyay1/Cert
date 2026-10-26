"""Load 600 authored Cloud Digital Leader items.

Google publishes 50-60 multiple choice and multiple select questions for this
exam and no case-study component, so the bank carries no case stems and the
exporter has no case path.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent
DOMAINS = {
    1: 'Digital Transformation with Google Cloud',
    2: 'Exploring Data Transformation with Google Cloud',
    3: 'Innovating with Google Cloud Artificial Intelligence',
    4: 'Modernize Infrastructure and Applications with Google Cloud',
    5: 'Trust and Security with Google Cloud',
    6: 'Scaling with Google Cloud Operations',
}
TOPICS = {1: 'Full-Length Mock Exam 1', 2: 'Full-Length Mock Exam 2', 3: 'Full-Length Mock Exam 3',
          4: 'Full-Length Mock Exam 4', 5: 'Full-Length Mock Exam 5', 6: 'Full-Length Mock Exam 6'}
SUBTITLES = {
    1: 'Transformation Drivers, Cloud Models, and Business Value',
    2: 'Data Value, Storage Choice, and Analytics',
    3: 'AI Concepts, Model Choice, and Responsible Use',
    4: 'Migration, Compute Choice, and APIs',
    5: 'Threats, Controls, and Earned Trust',
    6: 'Cost Control, Hierarchy, and Reliability',
}
# Local study-map IDs, not Google objective numbers.
SKILLS = {
    '1.1': 'Cloud Terminology and Transformation Concepts',
    '1.2': 'Business Benefits of Cloud',
    '1.3': 'Transformation Drivers and Challenges',
    '1.4': 'Google Cloud Differentiators',
    '1.5': 'Private, Hybrid, and Multicloud Architectures',
    '1.6': 'Networking Fundamentals and Service Models',
    '2.1': 'Value of Data and the Data Supply Chain',
    '2.2': 'Databases, Warehouses, Lakes, and Data Types',
    '2.3': 'Data Governance and Interoperability',
    '2.4': 'Data Management Product Selection',
    '2.5': 'Cloud Storage Classes',
    '2.6': 'Database Migration and Modernization',
    '2.7': 'Smart Analytics, Looker, and Streaming',
    '3.1': 'AI, ML, Generative AI, and Agentic AI',
    '3.2': 'ML Use Cases and Data Quality Dimensions',
    '3.3': 'Responsible and Explainable AI',
    '3.4': 'Selecting an AI Approach',
    '3.5': 'Agent Platform, Agent Studio, and AutoML',
    '3.6': 'Pre-trained APIs and Foundation Models',
    '3.7': 'AI Hypercomputer and BigQuery ML',
    '4.1': 'Migration Strategies',
    '4.2': 'Compute Fundamentals and Elasticity',
    '4.3': 'Compute Engine Business Value',
    '4.4': 'GKE and Container Business Value',
    '4.5': 'Serverless Application Options',
    '4.6': 'Multicloud and Hybrid Products',
    '4.7': 'APIs and Apigee',
    '5.1': 'Cyber Threats and Business Impact',
    '5.2': 'Security Fundamentals and Principles',
    '5.3': 'Encryption States, IAM, and Auditing',
    '5.4': 'Defense in Depth and SecOps',
    '5.5': 'Threat Intelligence, SCC, and SecOps Platform',
    '5.6': 'AI Security and Model Protection',
    '5.7': 'Network and Data Security Products',
    '5.8': 'Trust, Sovereignty, and Compliance',
    '6.1': 'CapEx, OpEx, and Total Cost of Ownership',
    '6.2': 'Cloud Financial Governance',
    '6.3': 'Resource Hierarchy and Inheritance',
    '6.4': 'Consumption Controls and Discounts',
    '6.5': 'Observability and Resilience',
    '6.6': 'SLIs, SLOs, SLAs, and DevOps',
}
VALID_TASKS = set(SKILLS)
# Google publishes one approximate weight per section; these total exactly 100.
OFFICIAL_WEIGHTS = {1: 18.0, 2: 18.0, 3: 18.0, 4: 18.0, 5: 18.0, 6: 10.0}
# 100-item exams: the published weights are already whole items, so no
# rounding correction is needed anywhere in this course.
ALLOCATIONS = {n: {1: 18, 2: 18, 3: 18, 4: 18, 5: 18, 6: 10} for n in range(1, 7)}
# Every exam uses the same per-skill template, so the six sets are comparable
# and every local study area is exercised in each one.
SKILL_PLAN = {
    '1.1': 3, '1.2': 3, '1.3': 3, '1.4': 3, '1.5': 3, '1.6': 3,
    '2.1': 3, '2.2': 3, '2.3': 2, '2.4': 3, '2.5': 2, '2.6': 2, '2.7': 3,
    '3.1': 3, '3.2': 3, '3.3': 2, '3.4': 3, '3.5': 3, '3.6': 2, '3.7': 2,
    '4.1': 3, '4.2': 3, '4.3': 2, '4.4': 3, '4.5': 2, '4.6': 2, '4.7': 3,
    '5.1': 2, '5.2': 2, '5.3': 3, '5.4': 2, '5.5': 3, '5.6': 2, '5.7': 2, '5.8': 2,
    '6.1': 2, '6.2': 2, '6.3': 2, '6.4': 2, '6.5': 1, '6.6': 1,
}
# Multi-select items per official domain, 3 x 5 + 1 = 16. Domain 6 carries a
# single multi-select item because it is only ten items wide.
MULTI_PLAN = {1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1}
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
