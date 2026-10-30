"""Question bank loader and blueprint constants for Microsoft Exam PL-900 (6 x 100 = 600 questions).

Aligned to the official Microsoft Learn PL-900 Study Guide (Skills measured as of July 24, 2026)
for Microsoft Certified: Power Platform Fundamentals.
"""

import re
from pathlib import Path

from sources import CERTIFICATION_URL, EXAM_URL, EXPIRATION_POLICY_URL, SKILL_SOURCES, STUDY_GUIDE_URL
from terms import TERMS

EXAM_CODE = 'PL-900'
EXAM_TITLE = 'Microsoft Power Platform Fundamentals'
CREDENTIAL_TITLE = 'Microsoft Certified: Power Platform Fundamentals'
STUDY_GUIDE_DATE = 'July 24, 2026'
PREREQUISITES = 'None (Beginner / Fundamentals certification; never expires)'

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
    1: 'Retail Store Operations — Platform Business Value, Dataverse Tables, Canvas Apps, Approvals & Copilot Agents',
    2: 'Healthcare Clinic Onboarding — DLP Governance, Power Platform Pipelines, Model-Driven Apps & Agent Knowledge',
    3: 'Municipal Citizen Services — Power Pages Value, Accessibility, Plan Designer, Desktop Flows & Agent Channels',
    4: 'Manufacturing Field Quality — Virtual/Elastic Tables, Power Fx Logic, Power Apps Vibe & AI Document Automation',
    5: 'Financial Client Services — Security Roles, Code Apps, Copilot in Power Automate, MCP Tools & Agent 365',
    6: 'Global Logistics & HR — PPAC Monitoring, Copilot App/Flow Authoring, Autonomous Agents & Agent Evaluations',
}

DOMAINS = {
    1: 'Describe the business value of Microsoft Power Platform',
    2: 'Manage the Microsoft Power Platform environment',
    3: 'Demonstrate the capabilities of Power Apps',
    4: 'Demonstrate the capabilities of Power Automate',
    5: 'Describe features and capabilities of agents in Microsoft Copilot Studio',
}

OFFICIAL_RANGES = {
    1: (5, 10),   # 8 per set (8.0%)
    2: (20, 25),  # 23 per set (23.0%)
    3: (20, 25),  # 23 per set (23.0%)
    4: (20, 25),  # 23 per set (23.0%)
    5: (20, 25),  # 23 per set (23.0%)
}

PER_SET_ALLOC = {1: 8, 2: 23, 3: 23, 4: 23, 5: 23}
ALLOCATIONS = {n: dict(PER_SET_ALLOC) for n in range(1, 7)}

SKILLS = {
    # Domain 1: Describe the business value of Microsoft Power Platform (8)
    '1.1': 'Describe the business value of Microsoft Power Apps and Microsoft Power Automate',
    '1.2': 'Describe the business value of Microsoft Dataverse and connectors',
    '1.3': 'Describe the business value of Microsoft Power Pages to build external websites',
    '1.4': 'Describe the business value of generative AI features in Power Platform and Copilot Studio to create agents',
    # Domain 2: Manage the Microsoft Power Platform environment (23)
    '2.1': 'Describe differences between traditional databases and Microsoft Dataverse',
    '2.2': 'Describe Dataverse tables, columns, Choices, and relationships',
    '2.3': 'Describe Dataverse table forms and views',
    '2.4': 'Describe options for business logic in Dataverse, including Business Rules, Power Fx formula, and rollup columns',
    '2.5': 'Describe how to use AI (Copilot) to create and edit Dataverse tables, columns, and relationships',
    '2.6': 'Describe Power Platform environments and Managed Environments',
    '2.7': 'Describe the Microsoft Power Platform security model and Data Loss Prevention (DLP) policies',
    '2.8': 'Describe how Microsoft Power Platform supports data privacy and accessibility guidelines',
    '2.9': 'Describe monitoring and analytics capabilities of Microsoft Power Platform',
    '2.10': 'Describe application lifecycle management (ALM) with Solutions and Microsoft Power Platform pipelines',
    # Domain 3: Demonstrate the capabilities of Power Apps (23)
    '3.1': 'Describe use cases for and capabilities of canvas apps',
    '3.2': 'Describe use cases for and capabilities of model-driven apps',
    '3.3': 'Describe use cases for and capabilities of Plan designer',
    '3.4': 'Describe use cases for and capabilities of code apps',
    '3.5': 'Describe how to use AI (Copilot) to create and edit a canvas app',
    '3.6': 'Describe how to use AI (Copilot) to create and use a model-driven app',
    '3.7': 'Describe creating AI-powered apps by using the Power Apps vibe experience',
    # Domain 4: Demonstrate the capabilities of Power Automate (23)
    '4.1': 'Describe use cases for cloud flows and desktop flows (RPA and Process Mining)',
    '4.2': 'Describe Power Automate use cases for approvals, Teams, Outlook, SharePoint, Forms, and document automation',
    '4.3': 'Describe connector triggers, actions, conditions, and loops for cloud flows',
    '4.4': 'Describe how to use AI (Copilot) to create and modify cloud flows',
    '4.5': 'Describe how to use AI (Copilot) and recorder capabilities to create and modify desktop flows',
    # Domain 5: Describe features and capabilities of agents in Microsoft Copilot Studio (23)
    '5.1': 'Describe use cases for conversational and autonomous agents in Copilot Studio',
    '5.2': 'Describe how to build agent conversation paths by using topics',
    '5.3': 'Describe how to use knowledge sources in agents',
    '5.4': 'Describe how tools, including MCP servers and agent flows, are used in agents',
    '5.5': 'Describe how to publish agents by using channels',
    '5.6': 'Describe use cases and capabilities for Microsoft Agent 365',
    '5.7': 'Describe how to monitor Copilot Studio agent usage and adoption',
    '5.8': 'Describe agent evaluations in Microsoft Copilot Studio',
}

SKILL_PLAN = {
    # Domain 1 (8)
    '1.1': 2, '1.2': 2, '1.3': 2, '1.4': 2,
    # Domain 2 (23)
    '2.1': 2, '2.2': 3, '2.3': 2, '2.4': 3, '2.5': 2,
    '2.6': 2, '2.7': 3, '2.8': 2, '2.9': 2, '2.10': 2,
    # Domain 3 (23)
    '3.1': 4, '3.2': 4, '3.3': 3, '3.4': 3, '3.5': 3, '3.6': 3, '3.7': 3,
    # Domain 4 (23)
    '4.1': 5, '4.2': 5, '4.3': 5, '4.4': 4, '4.5': 4,
    # Domain 5 (23)
    '5.1': 3, '5.2': 3, '5.3': 3, '5.4': 3, '5.5': 3, '5.6': 3, '5.7': 2, '5.8': 3,
}

assert sum(SKILL_PLAN.values()) == 100
for _d, _target in PER_SET_ALLOC.items():
    assert sum(v for k, v in SKILL_PLAN.items() if int(k.split('.')[0]) == _d) == _target

VALID_TASKS = set(SKILLS)
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
TYPE_PLAN = {'multiple-choice': 76, 'ordering': 8, 'multi-select': 16}
MULTI_PLAN = {1: 1, 2: 4, 3: 4, 4: 3, 5: 4}  # 16 multi-select per set
COMPLETION_FLOOR = 12
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
