"""Question bank loader and blueprint constants for Microsoft / GitHub Exam GH-100: GitHub Enterprise Administrator (6 x 100 = 600 questions).

Aligned to the official Microsoft Learn GH-100 Study Guide (Skills measured as of July 2026;
Last updated May 5, 2026) awarding the GitHub Administration certification.
"""

import re
from pathlib import Path

from sources import (
    CERTIFICATION_URL,
    EXAM_EXPERIENCE_URL,
    LEARN_PATH_PART1_URL,
    LEARN_PATH_PART2_URL,
    SKILL_SOURCES,
    STUDY_GUIDE_URL,
)
from terms import TERMS

EXAM_CODE = 'GH-100'
EXAM_TITLE = 'GitHub Enterprise Administrator'
CREDENTIAL_TITLE = 'GitHub Administration'
STUDY_GUIDE_DATE = 'July 2026 (Last updated May 5, 2026)'
PREREQUISITES = 'None (Intermediate certification; valid for 2 years — transitioning to Microsoft Learn recertification)'

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
    1: 'Multi-Org Enterprise Identity & Access — EMUs vs Personal Accounts, SAML/SCIM, Enterprise Teams, Custom Roles & Rulesets',
    2: 'Hybrid GHEC + GHES Appliance Operations — Support Bundles (ghe-support-bundle), HA/Backups, Merge Queues & GitHub Connect Licensing',
    3: 'Secure Software Development & App Governance — Enforced Security Configurations, CodeQL/Secret Push Protection, git filter-repo & API Rate Limits',
    4: 'Enterprise GitHub Actions & Private Runner Networking — Internal Reusable Workflows, SHA Pinning, Larger Runners, Azure VNet & OIDC Vaults',
    5: 'Sovereign Data Residency & Audit Compliance — GHE.com + EMUs, Audit Log Streaming, Fine-Grained PAT Policies, GitHub Apps & ARC Runners',
    6: 'Enterprise Telemetry, API Insights & FinOps Optimization — Audit/API Analytics, Copilot & GHAS 90-Day Committers, Cost Centers & Dormant Seats',
}

DOMAINS = {
    1: 'Manage GitHub identities and access',
    2: 'Administer GitHub Enterprise environment',
    3: 'Implement secure software development and compliance',
    4: 'Manage GitHub Actions',
    5: 'Monitor and optimize GitHub usage',
}

OFFICIAL_RANGES = {
    1: (15, 20),  # 19 per set (19.0%)
    2: (10, 15),  # 14 per set (14.0%)
    3: (25, 30),  # 29 per set (29.0%)
    4: (20, 25),  # 24 per set (24.0%)
    5: (10, 15),  # 14 per set (14.0%)
}

PER_SET_ALLOC = {1: 19, 2: 14, 3: 29, 4: 24, 5: 14}
ALLOCATIONS = {n: dict(PER_SET_ALLOC) for n in range(1, 7)}

SKILLS = {
    # Domain 1: Manage GitHub identities and access (19)
    '1.1': 'Describe differences between managed users and personal accounts',
    '1.2': 'Configure and enforce SAML SSO and 2FA',
    '1.3': 'Understand SCIM and team synchronization: implementation and key differences',
    '1.4': 'Choose and configure identity providers',
    '1.5': 'Explain GitHub’s authentication and authorization model',
    '1.6': 'Configure organization and repository roles',
    '1.7': 'Define and manage enterprise teams',
    '1.8': 'Audit access and permissions',
    '1.9': 'Manage settings, policies, rulesets, and roles',

    # Domain 2: Administer GitHub Enterprise environment (14)
    '2.1': 'Identify issues resolvable by admins vs GitHub Support',
    '2.2': 'Generate support bundles and diagnostics',
    '2.3': 'Recommend standards for developer processes',
    '2.4': 'Define standards for workflows, branching, reviews, and releases',
    '2.5': 'Describe GitHub Enterprise deployment scenarios (GHEC with EMU, GHEC with Data Residency + EMU, GHEC with personal accounts, GHES)',
    '2.6': 'Explain licensing and billing models',
    '2.7': 'Monitor license usage and consumption',

    # Domain 3: Implement secure software development and compliance (29)
    '3.1': 'Define organization and enterprise policies',
    '3.2': 'Strengthen enterprise security posture and data protection',
    '3.3': 'Implement audit logging and reporting',
    '3.4': 'Configure vulnerability alerts, secret scanning, and CodeQL',
    '3.5': 'Manage Dependabot and security advisories',
    '3.6': 'Define and implement a security response plan',
    '3.7': 'Configure personal access tokens',
    '3.8': 'Understand rate limits for PATs and GitHub Apps',
    '3.9': 'Describe GitHub Apps and OAuth Apps',
    '3.10': 'Approve or deny app usage based on policy',

    # Domain 4: Manage GitHub Actions (24)
    '4.1': 'Configure and manage reuse of actions and workflows to the enterprise repository',
    '4.2': 'Apply organizational policies for GitHub Actions',
    '4.3': 'Manage runner groups and administer GitHub-hosted vs. self-hosted runner options',
    '4.4': 'Apply IP allow lists and configure networking (including Azure private networking)',
    '4.5': 'Monitor and troubleshoot runner performance',
    '4.6': 'Define scope and access for secrets',
    '4.7': 'Configure secrets at organization and repository levels',
    '4.8': 'Integrate third-party vaults',

    # Domain 5: Monitor and optimize GitHub usage (14)
    '5.1': 'Analyze audit logs and API usage',
    '5.2': 'Distinguish admin responsibilities vs. GitHub Support and generate diagnostics',
    '5.3': 'Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features',
    '5.4': 'Interpret usage reports for metered products',
    '5.5': 'Recommend strategies for license and resource optimization',
}

SKILL_PLAN = {
    # Domain 1 (19)
    '1.1': 2, '1.2': 2, '1.3': 2, '1.4': 2, '1.5': 2, '1.6': 2, '1.7': 3, '1.8': 2, '1.9': 2,
    # Domain 2 (14)
    '2.1': 2, '2.2': 2, '2.3': 2, '2.4': 2, '2.5': 2, '2.6': 2, '2.7': 2,
    # Domain 3 (29)
    '3.1': 3, '3.2': 3, '3.3': 3, '3.4': 3, '3.5': 3, '3.6': 3, '3.7': 3, '3.8': 3, '3.9': 3, '3.10': 2,
    # Domain 4 (24)
    '4.1': 3, '4.2': 3, '4.3': 3, '4.4': 3, '4.5': 3, '4.6': 3, '4.7': 3, '4.8': 3,
    # Domain 5 (14)
    '5.1': 3, '5.2': 3, '5.3': 3, '5.4': 3, '5.5': 2,
}

assert sum(SKILL_PLAN.values()) == 100
for _d, _target in PER_SET_ALLOC.items():
    assert sum(v for k, v in SKILL_PLAN.items() if int(k.split('.')[0]) == _d) == _target

VALID_TASKS = set(SKILLS)

TYPE_PLAN = {'multiple-choice': 76, 'ordering': 8, 'multi-select': 16}
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
MULTI_PLAN = {1: 3, 2: 2, 3: 5, 4: 4, 5: 2}
COMPLETION_FLOOR = 20
PROPOSED_SOL_FLOOR = 6

QUESTIONS_DIR = Path(__file__).resolve().parent / 'questions'
SPLIT_RE = re.compile(r'(?<!\\)\|')


def _load(number: int) -> list[dict]:
    path = QUESTIONS_DIR / f'{number}.txt'
    if not path.is_file():
        return []
    out = []
    for line_no, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), start=1):
        s = raw.strip()
        if not s or s.startswith('#'):
            continue
        parts = [p.replace(r'\|', '|').strip() for p in SPLIT_RE.split(s)]
        if len(parts) != 6:
            raise ValueError(f'{path.name}:{line_no}: expected 6 pipe fields, got {len(parts)}: {raw[:90]}')
        task, kind, ans_raw, dis_raw, question, reason = parts
        if task not in VALID_TASKS:
            raise ValueError(f'{path.name}:{line_no}: unknown skill {task!r}')
        answers = [k.strip() for k in ans_raw.split(',') if k.strip()]
        distractors = [k.strip() for k in dis_raw.split(',') if k.strip()]
        out.append({
            'id': f'E{number}Q{len(out) + 1:03d}',
            'task': task,
            'domain': int(task.split('.')[0]),
            'kind': kind,
            'answers': answers,
            'distractors': distractors,
            'keys': answers + distractors,
            'question': question,
            'reason': reason,
        })
    return out


BANK = {n: _load(n) for n in range(1, 7)}
