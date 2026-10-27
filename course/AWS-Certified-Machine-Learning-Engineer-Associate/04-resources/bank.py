"""Load 390 authored AWS Certified Machine Learning Engineer – Associate (MLA-C02) items.

AWS publishes a 130-minute paper of 65 questions for MLA-C02, of which 50 are scored
and 15 are unscored, mixing multiple choice (one correct answer plus three
distractors) with multiple response (two or more correct answers from five or more
options). Each set here is therefore 65 items, so pace per item matches the published
paper at about 120 seconds; the mix of 50 multiple-choice and 15 multiple-response
items per set is an authoring choice, because AWS publishes no split between the two
types.

The published domain weights are 28 / 24 / 24 / 24 percent. Applied to 65 items they
give 18.2 / 15.6 / 15.6 / 15.6. Largest-remainder rounding would give 18 / 16 / 16 / 16
and overshoot the paper by one item, so one item is dropped from Domain 4 and the
per-exam counts are 18 / 16 / 16 / 15, each within 0.6 items of its published weight.

Designing end-to-end solutions, setting ML strategy, integrating a wide array of new
tools and working deeply in two or more ML domains are out of scope for this exam, so
items ask the candidate to select, configure or diagnose an implementation decision
rather than to architect a whole platform. The published format has no case-study
component, so the exporter has no case path.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent
DOMAINS = {
    1: 'Data Preparation for ML and AI',
    2: 'ML Model and Foundation Model (FM) Development',
    3: 'Deployment and Orchestration of ML and AI Workflows',
    4: 'Operating, Monitoring, and Securing ML and AI Solutions',
}
TOPICS = {1: 'Full-Length Mock Exam 1', 2: 'Full-Length Mock Exam 2', 3: 'Full-Length Mock Exam 3',
          4: 'Full-Length Mock Exam 4', 5: 'Full-Length Mock Exam 5', 6: 'Full-Length Mock Exam 6'}
# Every set covers all four domains and the same study-map skills; the sets differ
# in the industries used in their scenarios, which is what these subtitles name.
SUBTITLES = {
    1: 'Retail and E-Commerce Scenarios',
    2: 'Financial Services and Insurance Scenarios',
    3: 'Healthcare and Life Sciences Scenarios',
    4: 'Manufacturing and IoT Scenarios',
    5: 'Media, Search, and RAG Assistants',
    6: 'Logistics and Support Agent Scenarios',
}
DOMAIN_NOTES = {
    1: 'Ingestion, storage, feature engineering, embeddings, and data quality',
    2: 'Model and FM selection, tuning, customisation, and evaluation',
    3: 'Inference infrastructure, scaling, CI/CD, and orchestration',
    4: 'Monitoring, cost control, identity, network isolation, and guardrails',
}
# Local study-map IDs, not AWS objective numbers: AWS publishes task statements and
# skills inside each domain page rather than as numbered objectives.
SKILLS = {
    '1.1': 'Ingestion Sources and Storage Choice',
    '1.2': 'Streaming Ingestion',
    '1.3': 'Storage Class and Retention',
    '1.4': 'Data Formats and Partitioning',
    '1.5': 'Merge and Transform Tooling',
    '1.6': 'Feature Store',
    '1.7': 'Feature Engineering and Scaling',
    '1.8': 'Vector Stores and Embeddings',
    '1.9': 'Text Pre-processing and Chunking',
    '1.10': 'Data Quality Validation',
    '1.11': 'Labelling and Annotation',
    '1.12': 'Bias Detection and Mitigation',
    '1.13': 'Cleaning and Class Imbalance',
    '2.1': 'Model and Algorithm Selection',
    '2.2': 'Foundation Model Selection',
    '2.3': 'Fine-tuning and Customisation',
    '2.4': 'RAG Architecture Patterns',
    '2.5': 'Managed AI Services',
    '2.6': 'Built-in Algorithms and Script Mode',
    '2.7': 'Hyperparameter Tuning',
    '2.8': 'Training Efficiency and Regularisation',
    '2.9': 'Classic Model Evaluation',
    '2.10': 'GenAI and NLP Evaluation',
    '2.11': 'Experiment Tracking and Baselines',
    '3.1': 'Inference Strategy',
    '3.2': 'Endpoint Architecture',
    '3.3': 'Foundation Model Deployment',
    '3.4': 'Agents and Retrieval Runtime',
    '3.5': 'Containers and Compute Provisioning',
    '3.6': 'Autoscaling and Concurrency',
    '3.7': 'VPC Networking for Endpoints',
    '3.8': 'CI/CD Pipelines',
    '3.9': 'Model Registry and Versioning',
    '3.10': 'Deployment Strategy and Rollback',
    '3.11': 'Orchestration and Retraining',
    '4.1': 'Drift and Model Monitoring',
    '4.2': 'Metrics and Dashboards',
    '4.3': 'GenAI Observability',
    '4.4': 'Cost Optimisation and Purchasing',
    '4.5': 'Inference Cost and Token Usage',
    '4.6': 'IAM and Credentials',
    '4.7': 'Network Isolation',
    '4.8': 'Encryption and Secrets',
    '4.9': 'Guardrails and Responsible AI',
    '4.10': 'Audit and Vulnerability Scanning',
}
VALID_TASKS = set(SKILLS)
# AWS publishes 28 / 24 / 24 / 24 percent, which totals exactly 100.
OFFICIAL_WEIGHTS = {1: 28.0, 2: 24.0, 3: 24.0, 4: 24.0}
# 65 items: 18 / 16 / 16 / 15. Largest-remainder rounding gives 18 / 16 / 16 / 16 = 66,
# so the spare item is removed from Domain 4 and every count stays within 0.6 of its weight.
ALLOCATIONS = {n: {1: 18, 2: 16, 3: 16, 4: 15} for n in range(1, 7)}
SKILL_PLAN = {
    '1.1': 2, '1.2': 1, '1.3': 1, '1.4': 2, '1.5': 2, '1.6': 1, '1.7': 2,
    '1.8': 2, '1.9': 1, '1.10': 1, '1.11': 1, '1.12': 1, '1.13': 1,
    '2.1': 2, '2.2': 2, '2.3': 2, '2.4': 1, '2.5': 1, '2.6': 1, '2.7': 2,
    '2.8': 1, '2.9': 2, '2.10': 1, '2.11': 1,
    '3.1': 2, '3.2': 1, '3.3': 2, '3.4': 1, '3.5': 1, '3.6': 2, '3.7': 1,
    '3.8': 2, '3.9': 1, '3.10': 2, '3.11': 1,
    '4.1': 2, '4.2': 2, '4.3': 1, '4.4': 2, '4.5': 2, '4.6': 2, '4.7': 1,
    '4.8': 1, '4.9': 1, '4.10': 1,
}
# Fifteen multiple-response items per set, spread across the four domains.
MULTI_PLAN = {1: 4, 2: 4, 3: 4, 4: 3}
TYPE_PLAN = {'multiple-choice': 50, 'multi-select': 15}
ITEM_TOTAL = sum(TYPE_PLAN.values())


def _load(number):
    rows = []
    path = HERE / 'questions' / f'{number}.txt'
    for n, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip() or line.startswith('#'):
            continue
        parts = line.split('|')
        if len(parts) != 6:
            raise ValueError(f'{path.name} line {n}: expected 6 fields, found {len(parts)}')
        task, kind, answers, distractors, question, reason = [p.strip() for p in parts]
        if task not in VALID_TASKS:
            raise ValueError(f'{path.name} line {n}: unknown skill {task}')
        if kind not in ('S', 'M2'):
            raise ValueError(f'{path.name} line {n}: unknown kind {kind}')
        keys = answers.split(',') + distractors.split(',')
        if any(k not in TERMS for k in keys):
            raise ValueError(f'{path.name} line {n}: unknown option key '
                             f'{[k for k in keys if k not in TERMS]}')
        rows.append(dict(
            id=f'T{number}-Q{len(rows) + 1:03d}', number=number, domain=int(task.split('.')[0]),
            task=task, kind=kind, keys=keys, answers=answers.split(','),
            distractors=distractors.split(','), question=question, reason=reason))
    return rows


BANK = {n: _load(n) for n in range(1, 7)}
