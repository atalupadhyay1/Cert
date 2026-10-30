"""Question bank loader and blueprint constants for Microsoft Exam PL-200 (6 x 100 = 600 questions).

Aligned to the final official Microsoft Learn PL-200 Study Guide (Skills measured as of December 26, 2024;
exam & credential retired August 31, 2026 and succeeded by Exam AB-410: Building Intelligent Applications).
"""

import re
from pathlib import Path

from cases import CASES
from sources import CERTIFICATION_URL, EXAM_URL, RETIREMENT_URL, SKILL_SOURCES, STUDY_GUIDE_URL
from terms import TERMS

EXAM_CODE = 'PL-200'
EXAM_TITLE = 'Microsoft Power Platform Functional Consultant'
CREDENTIAL_TITLE = 'Microsoft Certified: Power Platform Functional Consultant Associate'
STUDY_GUIDE_DATE = 'December 26, 2024'
RETIREMENT_DATE = 'August 31, 2026'
SUCCESSOR_EXAM = 'AB-410 (Microsoft Certified: Intelligent Applications Builder Associate)'
PREREQUISITES = 'None (Associate-level certification; no mandatory prerequisite exam)'

ITEM_TOTAL = 100
CASE_STUDIES = 4
CASE_SIZE = 3

TOPICS = {
    1: 'Full-Length Mock Exam 1',
    2: 'Full-Length Mock Exam 2',
    3: 'Full-Length Mock Exam 3',
    4: 'Full-Length Mock Exam 4',
    5: 'Full-Length Mock Exam 5',
    6: 'Full-Length Mock Exam 6',
}

SUBTITLES = {
    1: 'Commercial Real Estate & Leasing — Matrix BUs, Power Pages Account Scope, Modern Commanding & Solution Layers',
    2: 'Specialty Healthcare & Referrals — Dataverse Search, Multi-Step Forms, Embedded Canvas Apps & Minimal Sandbox Copy',
    3: 'Municipal & Utility Permitting — Access Team Templates, Canvas Delegation/IfError, WDL Trigger Conditions & Managed Upgrades',
    4: 'Industrial Manufacturing & Dealer Warranty — Alternate Keys, Hierarchy Security, Cross-Table BPFs & Low-Code Plug-ins',
    5: 'Wealth Advisory & Insurance — Manual N:N Intersects, Form Component Controls, Dataverse Expand Query & Solution Checker',
    6: 'Higher Education & Global Grants — Custom Activity Tables, Entra Group Teams, Page Access Rules & Word XML Templates',
}

DOMAINS = {
    1: 'Configure Microsoft Dataverse',
    2: 'Create apps by using Microsoft Power Apps',
    3: 'Create and manage logic and process automation',
    4: 'Manage environments',
}

OFFICIAL_RANGES = {
    1: (25, 30),  # 28 per set (28.0%)
    2: (25, 30),  # 28 per set (28.0%)
    3: (25, 30),  # 27 per set (27.0%)
    4: (15, 20),  # 17 per set (17.0%)
}

PER_SET_ALLOC = {1: 28, 2: 28, 3: 27, 4: 17}
ALLOCATIONS = {n: dict(PER_SET_ALLOC) for n in range(1, 7)}

SKILLS = {
    # Domain 1: Configure Microsoft Dataverse (28)
    '1.1': 'Create or modify standard, activity, or virtual tables and configure table properties',
    '1.2': 'Determine and implement 1:N and N:N (native vs manual intersect) relationships',
    '1.3': 'Configure table relationship behaviors and cascading rules',
    '1.4': 'Create or modify columns, Alternate Keys, Rollup columns, and Power Fx Formula columns',
    '1.5': 'Configure Dataverse search, Quick Find views, and search index columns',
    '1.6': 'Manage environment, table, and column-level auditing and retention',
    '1.7': 'Describe and configure options for importing and exporting data (Excel, Dataflows, Synapse/Fabric Link)',
    '1.8': 'Configure duplicate detection rules and scheduled bulk record deletion jobs',
    '1.9': 'Manage Business Units and Modernized Business Units (matrix data access)',
    '1.10': 'Create and manage custom Security Roles (privilege depth, Append/Append To, inheritance)',
    '1.11': 'Create and manage Users, Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams',
    '1.12': 'Configure Column Security Profiles and Hierarchy Security (Manager vs Position)',
    # Domain 2: Create apps by using Microsoft Power Apps (28)
    '2.1': 'Create and configure model-driven sitemaps and multiple form types (form order & fallback)',
    '2.2': 'Use specialized controls in the modern form designer (Editable Grid, Form Component Control, Subgrids)',
    '2.3': 'Create and configure Dataverse Views (Public, Quick Find, Lookup, Associated, Personal)',
    '2.4': 'Configure Custom Pages in model-driven apps (responsive containers & Param("recordId"))',
    '2.5': 'Configure Modern Commanding by using Power Fx and Component Libraries',
    '2.6': 'Embed a Canvas app in a model-driven form and add Power BI dashboards and reports',
    '2.7': 'Describe Canvas app structure, responsive containers, galleries, forms, themes, and components',
    '2.8': 'Configure Canvas navigation, Power Fx formulas, variables, collections, delegation, and error handling',
    '2.9': 'Call Microsoft Power Automate cloud flows from a Canvas app and handle responses',
    '2.10': 'Configure Power Pages webpages, Basic Forms, Lists, navigation, and Design Studio workspaces',
    '2.11': 'Configure advanced Power Pages features (Multi-Step Forms, SharePoint documents, search, Power BI)',
    '2.12': 'Configure Power Pages website security (Table Permissions, Web Roles, Page Access Rules) and authentication',
    # Domain 3: Create and manage logic and process automation (27)
    '3.1': 'Select cloud flow types, classic Dataverse workflows, and Business Process Flows per use case',
    '3.2': 'Describe connector triggers, actions, polling/webhooks, and Connection References',
    '3.3': 'Implement cloud flow logic controls (Conditions, Concurrency, Scope Configure run after, Terminate, variables)',
    '3.4': 'Implement Dynamic Content, WDL expressions, and Trigger Conditions',
    '3.5': 'Work with the Microsoft Dataverse connector (Select columns, Filter rows, Expand Query, Relate rows, child flows)',
    '3.6': 'Manage, share (Run-only vs Co-owner), test with static results, and troubleshoot cloud flows',
    '3.7': 'Configure Business Process Flows (stages, branching, up to 5 cross-tables, roles, ordering)',
    '3.8': 'Add classic workflows and cloud flow steps to a BPF and manage the BPF Dataverse table',
    '3.9': 'Configure synchronous (Real-time) and asynchronous (Background) classic Dataverse workflows',
    '3.10': 'Troubleshoot classic workflows (System Jobs, loops) and manage workflow job log retention',
    '3.11': 'Configure Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins in Dataverse Accelerator)',
    '3.12': 'Create and configure Dataverse Business Rules (scopes & limitations) and Power Fx functions',
    # Domain 4: Manage environments (17)
    '4.1': 'Describe use cases and findings for App Checker and Solution Checker',
    '4.2': 'Create and manage Dataverse Solutions (custom Publishers, segmented tables, patches/clones)',
    '4.3': 'Distinguish Managed vs Unmanaged Solutions, inspect Solution Layers, and apply Upgrade vs Update',
    '4.4': 'Manage Sandbox environments (Full vs Minimal Copy, Reset), Backups, DLP, and Managed Environments',
    '4.5': 'Import and export Dataverse Solutions with Environment Variables, Connection References, and pipelines',
    '4.6': 'Configure Email Integration (Server-Side Synchronization, Mailboxes, Queues, App for Outlook)',
    '4.7': 'Configure SharePoint Document Management and Microsoft Word Templates',
}

SKILL_PLAN = {
    # Domain 1 (28)
    '1.1': 3, '1.2': 2, '1.3': 3, '1.4': 3,
    '1.5': 2, '1.6': 2, '1.7': 2, '1.8': 3,
    '1.9': 2, '1.10': 2, '1.11': 2, '1.12': 2,
    # Domain 2 (28)
    '2.1': 3, '2.2': 2, '2.3': 2, '2.4': 2, '2.5': 3, '2.6': 2,
    '2.7': 2, '2.8': 3, '2.9': 2,
    '2.10': 2, '2.11': 2, '2.12': 3,
    # Domain 3 (27)
    '3.1': 2, '3.2': 2, '3.3': 3, '3.4': 3, '3.5': 3, '3.6': 2,
    '3.7': 2, '3.8': 2,
    '3.9': 2, '3.10': 2,
    '3.11': 2, '3.12': 2,
    # Domain 4 (17)
    '4.1': 2, '4.2': 3, '4.3': 3, '4.4': 2, '4.5': 3,
    '4.6': 2, '4.7': 2,
}

assert len(SKILLS) == 43
assert sum(SKILL_PLAN.values()) == 100
for _d, _target in PER_SET_ALLOC.items():
    assert sum(v for k, v in SKILL_PLAN.items() if int(k.split('.')[0]) == _d) == _target

VALID_TASKS = set(SKILLS)
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
TYPE_PLAN = {'multiple-choice': 76, 'ordering': 8, 'multi-select': 16}
MULTI_PLAN = {1: 4, 2: 5, 3: 4, 4: 3}  # 16 multi-select per set
CODE_FILL_FLOOR = 14
PROPOSED_SOL_FLOOR = 6
QUESTIONS_DIR = Path(__file__).resolve().parent / 'questions'


def load_set(set_number: int) -> list[dict]:
    path = QUESTIONS_DIR / f'{set_number}.txt'
    if not path.exists():
        return []
    rows = []
    for line_number, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        parts = [p.replace('\\|', '|').strip() for p in re.split(r'(?<!\\)\|', line)]
        if len(parts) != 6:
            raise ValueError(f'{path.name}:{line_number}: expected 6 fields, got {len(parts)}')
        task, kind, answers_raw, distractors_raw, question, reason = parts
        if task not in VALID_TASKS:
            raise ValueError(f'{path.name}:{line_number}: unknown skill {task!r}')
        if kind not in KIND_PLAN:
            raise ValueError(f'{path.name}:{line_number}: unknown kind {kind!r}')
        answers = [a.strip() for a in answers_raw.split(',') if a.strip()]
        distractors = [d.strip() for d in distractors_raw.split(',') if d.strip()]
        domain = int(task.split('.')[0])
        rows.append({
            'id': f'T{set_number}-Q{len(rows) + 1:03d}',
            'task': task,
            'domain': domain,
            'kind': kind,
            'answers': answers,
            'distractors': distractors,
            'keys': answers + distractors,
            'question': question,
            'reason': reason,
            'line': line_number,
        })
    return rows


BANK = {n: load_set(n) for n in range(1, 7)}
