"""Load 390 authored AWS Certified Cloud Practitioner (CLF-C02) items.

The published CLF-C02 guide describes a 90-minute paper of 65 questions, of which
50 are scored and 15 unscored, mixing multiple choice (one correct answer and
three distractors) with multiple response (two or more correct answers from five
or more options). Each set here is therefore 65 items, and the answer mix of 55
multiple-choice plus 10 multiple-response items is an authoring choice, because
AWS publishes no split between the two types.

Coding, architecture design, troubleshooting, implementation and performance
testing are out of scope for this exam, so items ask the candidate to recognise a
concept or select a service, never to operate one. The guide carries no case-study
component, so no case scaffolding exists anywhere in this bank.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent
DOMAINS = {
    1: 'Cloud Concepts',
    2: 'Security and Compliance',
    3: 'Cloud Technology and Services',
    4: 'Billing, Pricing, and Support',
}
TOPICS = {1: 'Full-Length Mock Exam 1', 2: 'Full-Length Mock Exam 2', 3: 'Full-Length Mock Exam 3',
          4: 'Full-Length Mock Exam 4', 5: 'Full-Length Mock Exam 5', 6: 'Full-Length Mock Exam 6'}
# Domain notes appear in the review copy headings. Every set covers the same
# study-map skills, so the six sets share one subtitle and differ by scenario.
DOMAIN_NOTES = {
    1: 'Cloud Value, Economics, and the Shared Responsibility Model',
    2: 'Identity, Network Protection, Detection, and Compliance',
    3: 'Compute, Storage, Databases, Networking, and Managed Services',
    4: 'Pricing Models, Cost Control, and Support Plans',
}
# Every set covers all four domains and the same study-map skills; the sets differ
# in the industries used in their scenarios, which is what these subtitles name.
SUBTITLES = {
    1: 'Retail and Media Scenarios',
    2: 'Healthcare and Insurance Scenarios',
    3: 'Logistics and Manufacturing Scenarios',
    4: 'Public Sector and Financial Services Scenarios',
    5: 'Education and Travel Scenarios',
    6: 'Startup, Gaming, and Energy Scenarios',
}
# Local study-map IDs, not AWS objective numbers: AWS publishes task statements
# only inside the four domain pages, so the numbering here is this course's own.
SKILLS = {
    '1.1': 'Cloud Value Proposition',
    '1.2': 'Cloud Economics and Total Cost of Ownership',
    '1.3': 'Cloud Architecture Design Principles',
    '1.4': 'Well-Architected Framework',
    '1.5': 'Cloud Adoption Framework',
    '1.6': 'Migration Strategies',
    '1.7': 'Global Infrastructure',
    '1.8': 'Resiliency and Availability',
    '1.9': 'Shared Responsibility Model',
    '2.1': 'Identity and Access Management',
    '2.2': 'Root User and Credential Hygiene',
    '2.3': 'IAM Roles and Federation',
    '2.4': 'Network Security Controls',
    '2.5': 'Encryption and Key Management',
    '2.6': 'Secrets and Certificate Handling',
    '2.7': 'Threat Detection and Monitoring',
    '2.8': 'Data Protection and Classification',
    '2.9': 'Compliance and Audit Evidence',
    '2.10': 'Shared Responsibility Boundaries',
    '2.11': 'Governance Guardrails',
    '3.1': 'Compute Services',
    '3.2': 'Storage Services',
    '3.3': 'Database Services',
    '3.4': 'Networking and Content Delivery',
    '3.5': 'Management and Governance Services',
    '3.6': 'Integration and Messaging',
    '3.7': 'Analytics and Machine Learning',
    '3.8': 'Developer Tooling',
    '3.9': 'Deployment and Provisioning',
    '3.10': 'Monitoring and Observability',
    '3.11': 'Hybrid and Edge Services',
    '4.1': 'Pricing Models',
    '4.2': 'Cost Management Tools',
    '4.3': 'Billing and Account Structures',
    '4.4': 'Support Plans',
    '4.5': 'Guidance and Self-Service Resources',
    '4.6': 'Free Tier and Discounts',
}
VALID_TASKS = set(SKILLS)
# AWS publishes 24 / 30 / 34 / 12 percent. Those four weights total exactly 100,
# so no rounding correction is needed anywhere in this course.
OFFICIAL_WEIGHTS = {1: 24.0, 2: 30.0, 3: 34.0, 4: 12.0}
# 65 items per set: 24% of 65 is 15.6, so the closest integers are used and they
# happen to total exactly 65 (16 + 19 + 22 + 8). The bank holds six of each.
ALLOCATIONS = {n: {1: 16, 2: 19, 3: 22, 4: 8} for n in range(1, 7)}
SKILL_PLAN = {
    '1.1': 2, '1.2': 2, '1.3': 2, '1.4': 2, '1.5': 2, '1.6': 2, '1.7': 1, '1.8': 2, '1.9': 1,
    '2.1': 2, '2.2': 2, '2.3': 2, '2.4': 2, '2.5': 2, '2.6': 1, '2.7': 2, '2.8': 2, '2.9': 2,
    '2.10': 1, '2.11': 1,
    '3.1': 2, '3.2': 2, '3.3': 2, '3.4': 2, '3.5': 2, '3.6': 2, '3.7': 2, '3.8': 2, '3.9': 2,
    '3.10': 2, '3.11': 2,
    '4.1': 2, '4.2': 2, '4.3': 1, '4.4': 1, '4.5': 1, '4.6': 1,
}
# Ten multiple-response items per set, spread across the four domains.
MULTI_PLAN = {1: 2, 2: 3, 3: 4, 4: 1}
TYPE_PLAN = {'multiple-choice': 55, 'multi-select': 10}
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
