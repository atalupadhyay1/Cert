"""Load 600 authored Professional Cloud DevOps Engineer items.

Google publishes 50-60 multiple choice and multiple select questions for this
exam and no case-study component, so the bank carries no case stems and the
exporter has no case path. Configuration is in scope for this exam: the guide
asks about pipeline definitions, alerting policies, log routing, and IAM, so
items test the judgement behind a change rather than console recall.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent
DOMAINS = {
    1: 'Bootstrapping and Maintaining a Google Cloud Organization',
    2: 'Building and Implementing CI/CD Pipelines',
    3: 'Applying Site Reliability Engineering Practices',
    4: 'Implementing Observability Practices and Troubleshooting',
    5: 'Optimizing Performance and Cost',
}
TOPICS = {1: 'Full-Length Mock Exam 1', 2: 'Full-Length Mock Exam 2', 3: 'Full-Length Mock Exam 3',
          4: 'Full-Length Mock Exam 4', 5: 'Full-Length Mock Exam 5', 6: 'Full-Length Mock Exam 6'}
SUBTITLES = {
    1: 'Hierarchy, Infrastructure as Code, and Pipeline Foundations',
    2: 'Delivery Pipelines and Software Supply Chain',
    3: 'Reliability Engineering in Practice',
    4: 'Telemetry, Alerting, and Diagnosis',
    5: 'FinOps and Performance Tuning',
    6: 'Integrated Review Across All Five Sections',
}
# Local study-map IDs, not Google objective numbers.
SKILLS = {
    '1.1': 'Resource Hierarchy and Project Organization',
    '1.2': 'Shared Networking for Multi-Project Estates',
    '1.3': 'Multi-Project Monitoring and Logging',
    '1.4': 'IAM Roles and Organization Policies',
    '1.5': 'Service Account Management',
    '1.6': 'Data Residency in the Hierarchy',
    '1.7': 'Infrastructure-as-Code Tool Selection',
    '1.8': 'Blueprints and Controlled Infrastructure Change',
    '1.9': 'Automation with Scripting and APIs',
    '1.10': 'CI/CD Architecture Stack Design',
    '1.11': 'Third-Party Tooling in the Pipeline',
    '1.12': 'Multiple Environment Management',
    '1.13': 'Fleets, Patching, and Cluster Upgrades',
    '1.14': 'Secure Development Environments and AI Assistance',
    '2.1': 'Pipeline Triggers and Design',
    '2.2': 'Artifact Management',
    '2.3': 'Hybrid and Multicloud Deployment Targets',
    '2.4': 'Approval Flows and Deployment Process',
    '2.5': 'Deployment Auditing and Tracking',
    '2.6': 'Deployment Strategies',
    '2.7': 'Deployment Success Metrics',
    '2.8': 'Troubleshooting Deployment Issues',
    '2.9': 'Key Management',
    '2.10': 'Configuration and Secret Management',
    '2.11': 'Build-Time versus Runtime Secret Injection',
    '2.12': 'Vulnerability Scanning and Artifact Analysis',
    '2.13': 'Supply Chain Security and Binary Authorization',
    '2.14': 'Per-Environment IAM Policy',
    '3.1': 'SLIs, SLOs, and SLAs',
    '3.2': 'Error Budgets',
    '3.3': 'Cost of Reliability and Nines',
    '3.4': 'Service Lifecycle Management',
    '3.5': 'Capacity Planning and Quotas',
    '3.6': 'Autoscaling',
    '3.7': 'Traffic Draining and Redirection',
    '3.8': 'Incident Capacity',
    '3.9': 'Rollback Strategies',
    '4.1': 'Log Collection and Ingestion',
    '4.2': 'Log Optimization and Cost',
    '4.3': 'Logs Explorer and Query Language',
    '4.4': 'Log Export and Retention',
    '4.5': 'Sensitive Data Redaction',
    '4.6': 'Gemini Cloud Assist for Log Analysis',
    '4.7': 'Metrics Collection',
    '4.8': 'Custom and Log-Based Metrics',
    '4.9': 'Synthetic Monitors',
    '4.10': 'Metrics Explorer and Dashboards',
    '4.11': 'Alerting Policies',
    '4.12': 'Third-Party Alerting Integration',
    '4.13': 'Distributed Tracing with OpenTelemetry',
    '4.14': 'Trace Analysis and Log Correlation',
    '4.15': 'Infrastructure and Pipeline Troubleshooting',
    '4.16': 'Application and Latency Troubleshooting',
    '5.1': 'Application Performance Monitoring',
    '5.2': 'Active Assist and Recommenders',
    '5.3': 'Observability Cost Management',
    '5.4': 'Spot Virtual Machines',
    '5.5': 'Infrastructure Cost Planning',
    '5.6': 'Workload-Level Cost Optimization',
}
VALID_TASKS = set(SKILLS)
# Google publishes ~20 / ~25 / ~18 / ~25 / ~12 percent. Those five weights total
# exactly 100, so the per-exam counts are the weights themselves and no rounding
# correction is applied anywhere in this course.
OFFICIAL_WEIGHTS = {1: 20.0, 2: 25.0, 3: 18.0, 4: 25.0, 5: 12.0}
ALLOCATIONS = {n: {1: 20, 2: 25, 3: 18, 4: 25, 5: 12} for n in range(1, 7)}
SKILL_PLAN = {
    '1.1': 2, '1.2': 2, '1.3': 1, '1.4': 2, '1.5': 1, '1.6': 1, '1.7': 2,
    '1.8': 1, '1.9': 1, '1.10': 2, '1.11': 1, '1.12': 1, '1.13': 1, '1.14': 2,
    '2.1': 3, '2.2': 2, '2.3': 2, '2.4': 1, '2.5': 2, '2.6': 3, '2.7': 1,
    '2.8': 2, '2.9': 2, '2.10': 2, '2.11': 1, '2.12': 1, '2.13': 2, '2.14': 1,
    '3.1': 3, '3.2': 2, '3.3': 2, '3.4': 2, '3.5': 2, '3.6': 2, '3.7': 2,
    '3.8': 1, '3.9': 2,
    '4.1': 2, '4.2': 2, '4.3': 2, '4.4': 2, '4.5': 1, '4.6': 1, '4.7': 2,
    '4.8': 1, '4.9': 1, '4.10': 2, '4.11': 2, '4.12': 1, '4.13': 2, '4.14': 1,
    '4.15': 1, '4.16': 2,
    '5.1': 2, '5.2': 2, '5.3': 2, '5.4': 2, '5.5': 2, '5.6': 2,
}
MULTI_PLAN = {1: 3, 2: 4, 3: 3, 4: 4, 5: 2}
TYPE_PLAN = {'multiple-choice': 84, 'multi-select': 16}
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
            raise ValueError(f'{path.name} line {n}: unknown option key')
        rows.append(dict(
            id=f'T{number}-Q{len(rows) + 1:03d}', number=number, domain=int(task.split('.')[0]),
            task=task, kind=kind, keys=keys, answers=answers.split(','),
            distractors=distractors.split(','), question=question, reason=reason))
    return rows


BANK = {n: _load(n) for n in range(1, 7)}
