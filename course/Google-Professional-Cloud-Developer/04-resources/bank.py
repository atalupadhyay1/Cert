"""Load 600 authored Professional Cloud Developer items.

Google publishes 50-60 multiple choice and multiple select questions for this
exam and no case-study component, so the bank carries no case stems and the
exporter has no case path. Configuration is in scope for this exam: the guide
asks about Cloud Run and GKE deployment settings, health checks, autoscaling,
IAM boundaries and build pipelines, so items test the judgement behind a change
rather than console recall.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent
DOMAINS = {
    1: 'Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications',
    2: 'Building and Testing Applications',
    3: 'Configuring Cloud-Native Applications for Deployment',
    4: 'Integrating Applications with Google Cloud Services',
}
TOPICS = {1: 'Full-Length Mock Exam 1', 2: 'Full-Length Mock Exam 2', 3: 'Full-Length Mock Exam 3',
          4: 'Full-Length Mock Exam 4', 5: 'Full-Length Mock Exam 5', 6: 'Full-Length Mock Exam 6'}
SUBTITLES = {
    1: 'Compute Choice, APIs, and Secure Design',
    2: 'Development Environments, Builds, and Tests',
    3: 'Cloud Run and GKE Deployment Configuration',
    4: 'Data, Messaging, APIs, and Observability',
    5: 'Mixed Application Delivery Scenarios',
    6: 'Integrated Review Across All Four Sections',
}
# Local study-map IDs, not Google objective numbers.
SKILLS = {
    '1.1': 'Compute Platform Selection',
    '1.2': 'Containerizing and Refactoring Applications',
    '1.3': 'Regional Distribution and Failover',
    '1.4': 'Load Balancing and Session Affinity',
    '1.5': 'Caching with Memorystore',
    '1.6': 'API Protocol Choice: REST and gRPC',
    '1.7': 'API Management, Rate Limiting, and Versioning',
    '1.8': 'Asynchronous and Event-Driven Integration',
    '1.9': 'Resource Requirements and Cost Optimization',
    '1.10': 'Traffic Splitting and Gradual Rollout',
    '1.11': 'Orchestrating Services',
    '1.12': 'Data Retention and Organization Policy',
    '1.13': 'Secrets, Keys, and Credential Rotation',
    '1.14': 'Application Authentication',
    '1.15': 'Least Privilege and Service-to-Service Security',
    '1.16': 'Storage and Schema Selection',
    '1.17': 'Signed URLs and Time-Limited Access',
    '1.18': 'Analytics and ML Data Handoff',
    '2.1': 'Local Emulation of Cloud Services',
    '2.2': 'Developer Tooling and AI Assistance',
    '2.3': 'Container Builds with Cloud Build',
    '2.4': 'Artifact Registry and Image Storage',
    '2.5': 'Build Provenance and Admission Control',
    '2.6': 'Unit Testing Practice',
    '2.7': 'Automated Integration Testing',
    '3.1': 'Deploying Cloud Run from Source',
    '3.2': 'Cloud Run Triggers and Event Receivers',
    '3.3': 'Cloud Run Service Configuration',
    '3.4': 'API Exposure and Versioning',
    '3.5': 'Deploying Containers to GKE',
    '3.6': 'Kubernetes Health Checks',
    '3.7': 'Horizontal Pod Autoscaling',
    '4.1': 'Connecting to Datastores',
    '4.2': 'Publishing and Consuming Messages',
    '4.3': 'Calling Google Cloud APIs',
    '4.4': 'Service Accounts for API Calls',
    '4.5': 'Metrics, Logs, and Traces',
    '4.6': 'Error Reporting and Trace Correlation',
    '4.7': 'AI-Assisted Observability',
}
VALID_TASKS = set(SKILLS)
# Google publishes ~32 / ~23 / ~24 / ~21 percent. Those four weights total
# exactly 100, so the per-exam counts are the weights themselves and no rounding
# correction is applied anywhere in this course.
OFFICIAL_WEIGHTS = {1: 32.0, 2: 23.0, 3: 24.0, 4: 21.0}
ALLOCATIONS = {n: {1: 32, 2: 23, 3: 24, 4: 21} for n in range(1, 7)}
SKILL_PLAN = {
    '1.1': 3, '1.2': 1, '1.3': 2, '1.4': 2, '1.5': 2, '1.6': 2, '1.7': 2, '1.8': 2,
    '1.9': 2, '1.10': 2, '1.11': 1, '1.12': 1, '1.13': 2, '1.14': 2, '1.15': 2,
    '1.16': 2, '1.17': 1, '1.18': 1,
    '2.1': 3, '2.2': 3, '2.3': 4, '2.4': 3, '2.5': 3, '2.6': 3, '2.7': 4,
    '3.1': 4, '3.2': 4, '3.3': 4, '3.4': 2, '3.5': 4, '3.6': 3, '3.7': 3,
    '4.1': 5, '4.2': 4, '4.3': 4, '4.4': 2, '4.5': 3, '4.6': 2, '4.7': 1,
}
MULTI_PLAN = {1: 6, 2: 4, 3: 4, 4: 2}
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
