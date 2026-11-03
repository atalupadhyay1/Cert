"""Question bank loader and blueprint constants for Microsoft Exam GH-900: GitHub Foundations (6 x 100 = 600 questions).

Aligned to the official Microsoft Learn GH-900 Study Guide (Skills at a glance as of January 2026;
Last updated February 19, 2026) for GitHub Foundations.
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

EXAM_CODE = 'GH-900'
EXAM_TITLE = 'GitHub Foundations'
CREDENTIAL_TITLE = 'Microsoft Certified: GitHub Foundations'
STUDY_GUIDE_DATE = 'January 2026 (Last updated February 19, 2026)'
PREREQUISITES = 'None (Beginner / Fundamentals certification; does not require renewal / never expires)'

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
    1: 'Product Engineering & Web Platform Teams — Git vs GitHub, GitHub Flow, Key Repo Files, Issues/PRs, Actions, Copilot Agents & 2FA/Passkeys',
    2: 'Design, Documentation & Developer Advocacy — GFM Markdown, GitHub Desktop/Mobile, Wikis/Gists/Pages, github.dev, Saved Replies & Sponsors',
    3: 'Cloud SaaS & Platform Engineering — Branch Rulesets, CODEOWNERS, Dev Containers in Codespaces, Copilot Business vs Enterprise, EMUs & Teams',
    4: 'Agile Product Management & Release Operations — GitHub Projects (Table/Board/Roadmap), Iterations, Milestones, Project Workflows & Insights',
    5: 'Regulated FinTech & Enterprise Governance — SECURITY.md, Dependency Insights, Secret Protection, Multi-Model Copilot Policies, EMUs & InnerSource',
    6: 'Open-Source Ecosystems & Global Collaboration — Fork-and-PR Workflows, Repository Templates, Discussions, Marketplace, Following & Archiving',
}

DOMAINS = {
    1: 'Understand Git and GitHub basics',
    2: 'Work with GitHub repositories',
    3: 'Collaborate using GitHub',
    4: 'Apply modern development practices',
    5: 'Manage projects with GitHub',
    6: 'Understand privacy, security, and administration',
    7: 'Explore the GitHub community',
}

OFFICIAL_RANGES = {
    1: (25, 30),  # 28 per set (28.0%)
    2: (10, 15),  # 14 per set (14.0%)
    3: (10, 15),  # 14 per set (14.0%)
    4: (10, 15),  # 14 per set (14.0%)
    5: (5, 10),   # 8 per set (8.0%)
    6: (10, 15),  # 14 per set (14.0%)
    7: (5, 10),   # 8 per set (8.0%)
}

PER_SET_ALLOC = {1: 28, 2: 14, 3: 14, 4: 14, 5: 8, 6: 14, 7: 8}
ALLOCATIONS = {n: dict(PER_SET_ALLOC) for n in range(1, 7)}

SKILLS = {
    # Domain 1: Understand Git and GitHub basics (28)
    '1.1': 'Describe the purpose and benefits of version control',
    '1.2': 'Explain the difference between Git and GitHub',
    '1.3': 'Identify key Git concepts such as repositories, commits, and branches',
    '1.4': 'Describe GitHub accounts, organizations, and enterprise options',
    '1.5': 'Explain the GitHub Flow for collaboration',
    '1.6': 'Identify uses of Markdown for clear communication in issues and pull requests',
    '1.7': 'Recognize when to use GitHub Desktop and GitHub Mobile',

    # Domain 2: Work with GitHub repositories (14)
    '2.1': 'Describe the structure and key files of a GitHub repository (README, LICENSE, CONTRIBUTING, CODEOWNERS, SECURITY)',
    '2.2': 'Identify how to create, organize, and maintain repositories using templates and branches',
    '2.3': 'Explain how to add and manage files within a repository',
    '2.4': 'Describe repository insights, stars, feature previews, repository metrics dashboards, and dependency insights for improved visibility',
    '2.5': 'Recognize best practices for repository maintenance and collaboration',

    # Domain 3: Collaborate using GitHub (14)
    '3.1': 'Describe how to use issues, pull requests, and discussions for collaboration',
    '3.2': 'Explain how to link pull requests to issues and manage templates, filters, and assignments',
    '3.3': 'Identify the purpose of notifications and how to configure them for workflow management',
    '3.4': 'Describe how to use Gists, Wikis, and GitHub Pages to document and share information',

    # Domain 4: Apply modern development practices (14)
    '4.1': 'Describe the purpose and capabilities of GitHub Actions',
    '4.2': 'Identify how GitHub Copilot assists with AI-powered code suggestions, including Copilot agents, Agent Mode, and multi-model support',
    '4.3': 'Explain the differences between GitHub Copilot for Individuals, Business, and Enterprise',
    '4.4': 'Describe GitHub Codespaces and how to set up, customize, and use dev containers',
    '4.5': 'Explain when to use the github.dev editor and how it differs from Codespaces',

    # Domain 5: Manage projects with GitHub (8)
    '5.1': 'Describe GitHub Projects and layout options',
    '5.2': 'Explain how to configure projects, labels, milestones, and workflows',
    '5.3': 'Identify how to use saved replies and assignees to streamline communication',
    '5.4': 'Describe how project insights can be used to track progress and productivity',

    # Domain 6: Understand privacy, security, and administration (14)
    '6.1': 'Describe how to secure accounts with two-factor authentication (2FA) and passkeys',
    '6.2': 'Identify access permissions and roles for repositories and organizations',
    '6.3': 'Explain the purpose of Enterprise Managed Users (EMUs) and organization-wide Copilot policy management',
    '6.4': 'Describe repository privacy options, visibility settings, and branch protection rules',
    '6.5': 'Recognize how to manage organization settings, teams, and roles',

    # Domain 7: Explore the GitHub community (8)
    '7.1': 'Describe the benefits of open source and GitHub Sponsors',
    '7.2': 'Explain how GitHub supports and advances open-source projects',
    '7.3': 'Identify how to follow users and organizations to stay informed about activity',
    '7.4': 'Describe the GitHub Marketplace and its purpose',
    '7.5': 'Explain how InnerSource applies open-source principles within organizations',
    '7.6': 'Recognize when to use forks, templates, and discoverable repositories to promote collaboration',
}

SKILL_PLAN = {
    # Domain 1 (28)
    '1.1': 4, '1.2': 4, '1.3': 5, '1.4': 4, '1.5': 4, '1.6': 4, '1.7': 3,
    # Domain 2 (14)
    '2.1': 4, '2.2': 3, '2.3': 2, '2.4': 3, '2.5': 2,
    # Domain 3 (14)
    '3.1': 4, '3.2': 4, '3.3': 3, '3.4': 3,
    # Domain 4 (14)
    '4.1': 3, '4.2': 3, '4.3': 3, '4.4': 3, '4.5': 2,
    # Domain 5 (8)
    '5.1': 2, '5.2': 2, '5.3': 2, '5.4': 2,
    # Domain 6 (14)
    '6.1': 3, '6.2': 3, '6.3': 3, '6.4': 3, '6.5': 2,
    # Domain 7 (8)
    '7.1': 1, '7.2': 1, '7.3': 1, '7.4': 1, '7.5': 2, '7.6': 2,
}

assert sum(SKILL_PLAN.values()) == 100
for _d, _target in PER_SET_ALLOC.items():
    assert sum(v for k, v in SKILL_PLAN.items() if int(k.split('.')[0]) == _d) == _target

VALID_TASKS = set(SKILLS)

TYPE_PLAN = {'multiple-choice': 76, 'ordering': 8, 'multi-select': 16}
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
MULTI_PLAN = {1: 4, 2: 2, 3: 2, 4: 3, 5: 1, 6: 3, 7: 1}
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
