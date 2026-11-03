"""Question bank loader and blueprint constants for Microsoft / GitHub Exam GH-200: GitHub Actions (6 x 100 = 600 questions).

Aligned to the official Microsoft Learn GH-200 Study Guide (Skills measured as of January 2026;
Last updated February 5, 2026; certification page updated August 7, 2026) awarding the GitHub Actions certification.
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

EXAM_CODE = 'GH-200'
EXAM_TITLE = 'GitHub Actions'
CREDENTIAL_TITLE = 'GitHub Actions'
STUDY_GUIDE_DATE = 'January 2026 (Last updated February 5, 2026)'
PREREQUISITES = 'None (Intermediate certification; valid for 2 years — 6-month transition extension toward Microsoft Learn recertification)'

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
    1: 'Polyglot Monorepo CI & Matrix Orchestration — Event Filters, YAML Anchors (&/*/<<:), Service Containers, Artifacts v4 & VS Code Extension',
    2: 'Workflow Consumption, Log Diagnostics & Reusable Pipelines — Debug Secrets, Matrix Re-Runs, Starter Templates & Nested workflow_call',
    3: 'Custom Action Engineering & Marketplace Distribution — Node 20 Bundling (@vercel/ncc), Docker vs Composite, Immutable Actions & SemVer',
    4: 'Enterprise Runner Fleet & Private Cloud Networking — Ruleset Required Workflows, Kubernetes ARC Scale Sets, Azure VNet & Secrets REST API',
    5: 'Zero-Trust Supply Chain & Passwordless Cloud Deployments — Script Injection Defense, OIDC Subject Claims, SHA Pinning & SLSA Attestations',
    6: 'High-Scale FinOps, Caching & Runner Fleet Optimization — Cache Eviction, REST Retention Pruning, OS Multipliers, ubuntu-slim & Concurrency',
}

DOMAINS = {
    1: 'Author and manage workflows',
    2: 'Consume and troubleshoot workflows',
    3: 'Author and maintain actions',
    4: 'Manage GitHub Actions for the enterprise',
    5: 'Secure and optimize automation',
}

OFFICIAL_RANGES = {
    1: (20, 25),  # 24 per set (24.0%)
    2: (15, 20),  # 19 per set (19.0%)
    3: (15, 20),  # 19 per set (19.0%)
    4: (20, 25),  # 24 per set (24.0%)
    5: (10, 15),  # 14 per set (14.0%)
}

PER_SET_ALLOC = {1: 24, 2: 19, 3: 19, 4: 24, 5: 14}
ALLOCATIONS = {n: dict(PER_SET_ALLOC) for n in range(1, 7)}

SKILLS = {
    # Domain 1: Author and manage workflows (24)
    '1.1': 'Configure workflows for scheduled, manual, and webhook events',
    '1.2': 'Define workflow scope, permissions, event filters, and concurrency controls',
    '1.3': 'Design workflows using inputs and reusable configuration patterns',
    '1.4': 'Structure jobs, steps, conditional logic, timeouts, and error-handling behavior',
    '1.5': 'Manage job dependencies and execution order',
    '1.6': 'Use workflow commands and environment files to control job execution',
    '1.7': 'Configure service containers and containerized job environments',
    '1.8': 'Implement matrix strategies to run workflows across multiple configurations',
    '1.9': 'Simplify workflow definitions using YAML anchors and aliases within a workflow file',
    '1.10': 'Reference actions and workflows using appropriate contexts and immutable references',
    '1.11': 'Write expressions using built-in functions and conditional operators',
    '1.12': 'Author and validate workflows using IDE extensions and developer tooling',
    '1.13': 'Configure dependency caching and manage workflow artifacts and retention',
    '1.14': 'Pass data between steps and jobs using outputs, environment variables, and artifacts',
    '1.15': 'Publish job summaries and configure workflow status badges',

    # Domain 2: Consume and troubleshoot workflows (19)
    '2.1': 'Predict workflow behavior based on event payloads, triggers, and configuration',
    '2.2': 'Enable and interpret step and runner diagnostic logs to identify failures',
    '2.3': 'Interpret workflows that use YAML anchors and aliases during execution',
    '2.4': 'Analyze matrix-driven runs and re-run failed or targeted jobs',
    '2.5': 'Locate workflow runs and logs via the GitHub UI, CLI, and REST API',
    '2.6': 'Access and download workflow artifacts from completed runs',
    '2.7': 'Consume organization-level reusable workflows in downstream repositories',
    '2.8': 'Use public and non-public starter workflow templates across repositories',
    '2.9': 'Manage workflow lifecycle states including disabling, enabling, and deleting workflows',

    # Domain 3: Author and maintain actions (19)
    '3.1': 'Create and configure JavaScript actions',
    '3.2': 'Create and configure Docker container and composite actions, and select the appropriate action type',
    '3.3': 'Troubleshoot action failures and adopt immutable action distribution practices',
    '3.4': 'Define action metadata, inputs, outputs, and branding in action configuration files',
    '3.5': 'Implement workflow commands, exit codes, and output handling within actions',
    '3.6': 'Select an appropriate distribution model for public, private, and enterprise actions',
    '3.7': 'Publish actions to GitHub Marketplace',
    '3.8': 'Create and manage action releases, tags, and versioning strategies for consumers',

    # Domain 4: Manage GitHub Actions for the enterprise (24)
    '4.1': 'Configure and govern enterprise-level reuse of actions and reusable workflows',
    '4.2': 'Control access and sharing policies for actions and workflows across repositories and organizations',
    '4.3': 'Enforce enterprise and organization policies for allowed actions and workflow execution',
    '4.4': 'Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners)',
    '4.5': 'Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration)',
    '4.6': 'Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance',
    '4.7': 'Customize, preconfigure, and maintain runner images and software dependencies',
    '4.8': 'Define scope, precedence, and access controls for encrypted secrets and configuration variables at enterprise, organization, repository, and environment levels',
    '4.9': 'Manage secrets programmatically and in workflows using the GitHub REST API and secure handling practices',

    # Domain 5: Secure and optimize automation (14)
    '5.1': 'Configure deployment environments, protection rules, required reviewers, and vet Marketplace actions',
    '5.2': 'Identify and mitigate untrusted input and script injection risks in workflows and actions',
    '5.3': 'Apply least-privilege permissions to GITHUB_TOKEN and manage cross-repository authentication tokens',
    '5.4': 'Configure OpenID Connect (OIDC) for federated authentication to cloud providers and external vaults',
    '5.5': 'Enforce action pinning, supply-chain security controls, and artifact attestations',
    '5.6': 'Optimize workflow execution time and storage using caching, artifact policies, and selective execution',
    '5.7': 'Reduce runner cost and resource consumption using concurrency controls, runner sizing, and matrix optimization',
}

SKILL_PLAN = {
    # Domain 1 (24)
    '1.1': 2, '1.2': 2, '1.3': 2, '1.4': 2, '1.5': 2, '1.6': 2, '1.7': 2, '1.8': 2,
    '1.9': 1, '1.10': 2, '1.11': 1, '1.12': 1, '1.13': 1, '1.14': 1, '1.15': 1,
    # Domain 2 (19)
    '2.1': 2, '2.2': 3, '2.3': 2, '2.4': 2, '2.5': 2, '2.6': 2, '2.7': 2, '2.8': 2, '2.9': 2,
    # Domain 3 (19)
    '3.1': 3, '3.2': 3, '3.3': 2, '3.4': 3, '3.5': 2, '3.6': 2, '3.7': 2, '3.8': 2,
    # Domain 4 (24)
    '4.1': 3, '4.2': 3, '4.3': 3, '4.4': 3, '4.5': 3, '4.6': 3, '4.7': 2, '4.8': 2, '4.9': 2,
    # Domain 5 (14)
    '5.1': 2, '5.2': 2, '5.3': 2, '5.4': 2, '5.5': 2, '5.6': 2, '5.7': 2,
}

assert len(SKILLS) == 48
assert sum(SKILL_PLAN.values()) == 100
for _d, _target in PER_SET_ALLOC.items():
    assert sum(v for k, v in SKILL_PLAN.items() if int(k.split('.')[0]) == _d) == _target

VALID_TASKS = set(SKILLS)

TYPE_PLAN = {'multiple-choice': 76, 'ordering': 8, 'multi-select': 16}
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
MULTI_PLAN = {1: 4, 2: 3, 3: 3, 4: 4, 5: 2}
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
