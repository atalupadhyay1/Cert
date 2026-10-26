"""Load 600 authored Professional Cloud Database Engineer items.

Google publishes 50-60 multiple choice and multiple select questions for this
exam and no case-study component, so the bank carries no case stems and the
exporter has no case path. Configuration is in scope for this exam: the guide
asks about HA topology, connection paths, backup and PITR settings, replication
and provisioning automation, so items test the judgement behind a change rather
than console recall.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent
DOMAINS = {
    1: 'Design Innovative, Scalable, and Highly Available Cloud Database Solutions',
    2: 'Manage a Solution That Can Span Multiple Database Technologies',
    3: 'Migrate Data Solutions',
    4: 'Deploy Scalable and Highly Available Databases in Google Cloud',
}
TOPICS = {1: 'Full-Length Mock Exam 1', 2: 'Full-Length Mock Exam 2', 3: 'Full-Length Mock Exam 3',
          4: 'Full-Length Mock Exam 4', 5: 'Full-Length Mock Exam 5', 6: 'Full-Length Mock Exam 6'}
SUBTITLES = {
    1: 'Sizing, Availability Design, and Database Selection',
    2: 'Operations, Access, Backup, and Performance',
    3: 'Migration Strategy, Conversion, and Cutover',
    4: 'Deployment, High Availability, and Disaster Recovery',
    5: 'Mixed Operations and Cost Control',
    6: 'Integrated Review Across All Four Sections',
}
# Local study-map IDs, not Google objective numbers.
SKILLS = {
    '1.1': 'Workload Sizing From Current Metrics',
    '1.2': 'Compute and Storage Sizing Tradeoffs',
    '1.3': 'Machine Type and Storage Type Selection',
    '1.4': 'Zonal, Regional, and Multi-Regional Tradeoffs',
    '1.5': 'Maintenance Windows and Notification',
    '1.6': 'Network Connectivity and Private Access',
    '1.7': 'Key Management and Encryption',
    '1.8': 'Session Pooling and Connection Management',
    '1.9': 'Auditing Policies for Managed Services',
    '1.10': 'Managed, Self-Managed, and Partner Offerings',
    '1.11': 'SQL and NoSQL Data Model Fit',
    '1.12': 'Vector and Generative AI Requirements',
    '1.13': 'Comparative Cost Analysis Across Databases',
    '1.14': 'Application and Database Dependencies',
    '1.15': 'Regulatory, Compliance, and Organization Policy',
    '1.16': 'Federation, Exports, and Hybrid Spans',
    '2.1': 'IAM for Database Connectivity',
    '2.2': 'Database Users and Authentication',
    '2.3': 'Slow Queries and Missing Indexes',
    '2.4': 'Locking and Resource Contention',
    '2.5': 'Database Vitals Monitoring',
    '2.6': 'Quotas and Limits',
    '2.7': 'Alerts for Errors and Performance',
    '2.8': 'Backup and Recovery Option Selection',
    '2.9': 'Export and Import Configuration',
    '2.10': 'RTO, RPO, and Point-in-Time Recovery',
    '2.11': 'Data Retention Management',
    '2.12': 'Scaling Up Versus Scaling Out',
    '2.13': 'Replication Strategies',
    '2.14': 'Query Optimization for Cost and Performance',
    '2.15': 'Automated Maintenance and Scheduled Exports',
    '2.16': 'Managed Upgrades and SLA Monitoring',
    '3.1': 'Migration Strategy and Downtime Budget',
    '3.2': 'Migration Tool Selection',
    '3.3': 'Heterogeneous Schema and DDL Conversion',
    '3.4': 'DML and Application Code Conversion',
    '3.5': 'Initial Load and Change Replication',
    '3.6': 'Validation and Reconciliation',
    '3.7': 'Cutover and Fallback Planning',
    '3.8': 'Reverse Replication to the Source',
    '3.9': 'Minimizing Downtime During Migration',
    '3.10': 'Source Decommissioning',
    '4.1': 'Provisioning Highly Available Instances',
    '4.2': 'Testing High Availability and Disaster Recovery',
    '4.3': 'Multi-Regional Replication Setup',
    '4.4': 'Read Replicas and Read Pools',
    '4.5': 'Automating Database Provisioning',
    '4.6': 'Monitoring Highly Available Databases',
    '4.7': 'Regional Failover Mechanics',
    '4.8': 'Connection Routing and Load Balancing',
    '4.9': 'Failover Capacity Headroom',
}
VALID_TASKS = set(SKILLS)
# Google publishes ~32 / ~25 / ~23 / ~20 percent. Those four weights total
# exactly 100, so the per-exam counts are the weights themselves and no rounding
# correction is applied anywhere in this course.
OFFICIAL_WEIGHTS = {1: 32.0, 2: 25.0, 3: 23.0, 4: 20.0}
ALLOCATIONS = {n: {1: 32, 2: 25, 3: 23, 4: 20} for n in range(1, 7)}
SKILL_PLAN = {
    '1.1': 2, '1.2': 2, '1.3': 2, '1.4': 3, '1.5': 2, '1.6': 2, '1.7': 2, '1.8': 2,
    '1.9': 2, '1.10': 2, '1.11': 3, '1.12': 2, '1.13': 2, '1.14': 1, '1.15': 2, '1.16': 1,
    '2.1': 2, '2.2': 1, '2.3': 2, '2.4': 2, '2.5': 2, '2.6': 1, '2.7': 2, '2.8': 2,
    '2.9': 1, '2.10': 2, '2.11': 1, '2.12': 2, '2.13': 1, '2.14': 1, '2.15': 2, '2.16': 1,
    '3.1': 3, '3.2': 3, '3.3': 2, '3.4': 2, '3.5': 2, '3.6': 2, '3.7': 3, '3.8': 2,
    '3.9': 2, '3.10': 2,
    '4.1': 3, '4.2': 3, '4.3': 3, '4.4': 2, '4.5': 2, '4.6': 2, '4.7': 2, '4.8': 1, '4.9': 2,
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
