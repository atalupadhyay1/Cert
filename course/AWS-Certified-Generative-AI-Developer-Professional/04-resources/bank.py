"""Load 450 authored AWS Certified Generative AI Developer - Professional (AIP-C01) items.

AWS publishes a 180-minute paper of 75 questions for AIP-C01, of which 65 are scored
and 10 are unscored, mixing multiple choice (one correct answer plus three
distractors) with multiple response (two or more correct answers from five or more
options). Each set here is therefore 75 items, so pace per item matches the published
paper at about 144 seconds; the mix of 60 multiple-choice and 15 multiple-response
items per set is an authoring choice, because AWS publishes no split between the two
types.

The published domain weights are 31 / 26 / 20 / 12 / 11 percent. Applied to 75 items
they give 23.25 / 19.5 / 15 / 9 / 8.25. Largest-remainder rounding gives 23 / 20 / 15 /
9 / 8, so Domain 2 takes the extra item and every count lands within 0.5 items of its
published weight.

Model development and training, advanced ML techniques, and data engineering and
feature engineering are out of scope for this exam, so items ask the candidate to
integrate, secure, evaluate or operate a generative AI application rather than to
train a model. The published format has no case-study component, so the exporter has
no case path.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent
DOMAINS = {
    1: 'Foundation Model Integration, Data Management, and Compliance',
    2: 'Implementation and Integration',
    3: 'AI Safety, Security, and Governance',
    4: 'Operational Efficiency and Optimization for GenAI Applications',
    5: 'Testing, Validation, and Troubleshooting',
}
TOPICS = {1: 'Full-Length Mock Exam 1', 2: 'Full-Length Mock Exam 2', 3: 'Full-Length Mock Exam 3',
          4: 'Full-Length Mock Exam 4', 5: 'Full-Length Mock Exam 5', 6: 'Full-Length Mock Exam 6'}
# Every set covers all five domains and the same study-map skills; the sets differ in
# the industries used in their scenarios, which is what these subtitles name.
SUBTITLES = {
    1: 'Retail and Customer Service Scenarios',
    2: 'Financial Services and Insurance Scenarios',
    3: 'Healthcare and Life Sciences Scenarios',
    4: 'Media, Publishing, and Marketing Scenarios',
    5: 'Manufacturing and Field Operations Scenarios',
    6: 'Software Delivery and Internal Platform Scenarios',
}
DOMAIN_NOTES = {
    1: 'Model integration, data pipelines, vector stores, retrieval, and prompts',
    2: 'Agents, deployment, enterprise integration, APIs, and developer tooling',
    3: 'Safety controls, privacy, governance, and responsible AI',
    4: 'Token cost, latency, throughput, and observability',
    5: 'Evaluation, validation, regression testing, and diagnosis',
}
# Local study-map IDs, not AWS objective numbers: AWS publishes task statements and
# skills inside each domain page rather than as numbered objectives.
SKILLS = {
    '1.1': 'GenAI Solution Architecture',
    '1.2': 'Proof-of-Concept Validation',
    '1.3': 'Foundation Model Selection and Benchmarking',
    '1.4': 'Model Routing and Provider Abstraction',
    '1.5': 'Resilience and Cross-Region Inference',
    '1.6': 'Customisation Lifecycle and Rollback',
    '1.7': 'Data Validation for Model Inputs',
    '1.8': 'Multimodal Ingestion and Processing',
    '1.9': 'Request Formatting and Enrichment',
    '1.10': 'Vector Store Architecture',
    '1.11': 'Metadata Frameworks and Index Maintenance',
    '1.12': 'Chunking and Embedding Strategy',
    '1.13': 'Hybrid Retrieval and Reranking',
    '1.14': 'Query Transformation and Handling',
    '1.15': 'Prompt Engineering and Governance',
    '2.1': 'Agent Memory and State',
    '2.2': 'Agent Orchestration Patterns',
    '2.3': 'Tool Reliability and Safeguards',
    '2.4': 'Foundation Model Deployment and Capacity',
    '2.5': 'Enterprise Integration Patterns',
    '2.6': 'Identity for Model Access',
    '2.7': 'CI/CD and GenAI Gateway',
    '2.8': 'Streaming and Asynchronous APIs',
    '2.9': 'API Resilience and Backoff',
    '2.10': 'Application Integration and Low Code',
    '2.11': 'Developer Productivity Tooling',
    '2.12': 'Integration Troubleshooting',
    '3.1': 'Content Safety Controls',
    '3.2': 'Grounding and Hallucination Reduction',
    '3.3': 'Prompt Injection Defence',
    '3.4': 'Privacy and PII Protection',
    '3.5': 'Network and Data Isolation',
    '3.6': 'Governance, Lineage, and Audit',
    '3.7': 'Responsible AI and Transparency',
    '3.8': 'Fairness and Compliance Monitoring',
    '4.1': 'Token Cost Efficiency',
    '4.2': 'Model Tiering and Caching',
    '4.3': 'Throughput and Latency Optimisation',
    '4.4': 'GenAI Observability',
    '4.5': 'Cost Attribution and Governance',
    '5.1': 'GenAI Evaluation Metrics',
    '5.2': 'Model Comparison and Traffic Testing',
    '5.3': 'Regression Testing and Quality Gates',
    '5.4': 'Retrieval and Agent Evaluation',
    '5.5': 'GenAI Troubleshooting',
}
VALID_TASKS = set(SKILLS)
# AWS publishes 31 / 26 / 20 / 12 / 11 percent, which totals exactly 100.
OFFICIAL_WEIGHTS = {1: 31.0, 2: 26.0, 3: 20.0, 4: 12.0, 5: 11.0}
# 75 items: 23 / 20 / 15 / 9 / 8. Largest remainder gives the surplus item to Domain 2,
# whose exact share is 19.5, and every count stays within 0.5 of its weight.
ALLOCATIONS = {n: {1: 23, 2: 20, 3: 15, 4: 9, 5: 8} for n in range(1, 7)}
SKILL_PLAN = {
    '1.1': 2, '1.2': 1, '1.3': 2, '1.4': 1, '1.5': 2, '1.6': 1, '1.7': 2, '1.8': 1,
    '1.9': 2, '1.10': 1, '1.11': 2, '1.12': 1, '1.13': 2, '1.14': 1, '1.15': 2,
    '2.1': 2, '2.2': 2, '2.3': 2, '2.4': 2, '2.5': 2, '2.6': 1, '2.7': 2, '2.8': 1,
    '2.9': 2, '2.10': 2, '2.11': 1, '2.12': 1,
    '3.1': 2, '3.2': 2, '3.3': 2, '3.4': 2, '3.5': 2, '3.6': 2, '3.7': 2, '3.8': 1,
    '4.1': 2, '4.2': 2, '4.3': 2, '4.4': 2, '4.5': 1,
    '5.1': 2, '5.2': 1, '5.3': 2, '5.4': 2, '5.5': 1,
}
# Fifteen multiple-response items per set, three in each of the five domains.
MULTI_PLAN = {1: 3, 2: 3, 3: 3, 4: 3, 5: 3}
# Multi-response skills: one per skill except 1.1, which carries both of its items.
MULTI_SKILLS = {'1.1': 2, '1.13': 1,
                '2.2': 1, '2.4': 1, '2.7': 1,
                '3.1': 1, '3.4': 1, '3.6': 1,
                '4.2': 1, '4.3': 1, '4.4': 1,
                '5.1': 1, '5.3': 1, '5.4': 1}
TYPE_PLAN = {'multiple-choice': 60, 'multi-select': 15}
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
