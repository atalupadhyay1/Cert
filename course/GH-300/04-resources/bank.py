"""Question bank loader and blueprint constants for Microsoft / GitHub Exam GH-300: GitHub Copilot (6 x 100 = 600 questions).

Aligned to the official Microsoft Learn GH-300 Study Guide (Skills measured as of August 7, 2026;
Last updated July 9, 2026; certification page updated August 7, 2026) awarding the GitHub Copilot certification.
"""

import re
from pathlib import Path

from sources import CERT_PAGE_URL, SKILL_SOURCES, STUDY_GUIDE_URL
from terms import TERMS

EXAM_CODE = 'GH-300'
EXAM_TITLE = 'GitHub Copilot'
CREDENTIAL_TITLE = 'GitHub Copilot'
STUDY_GUIDE_DATE = 'August 7, 2026 (Last updated July 9, 2026)'
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
    1: 'Responsible AI Governance, IDE Inline/Chat Workflows & Cloud Proxy Architecture',
    2: 'GitHub Copilot CLI, Agent Mode, Sub-Agents, MCP Servers & Agent Sessions',
    3: 'Copilot Spaces, Spark, Custom Instructions (applyTo / excludeAgent), Prompt Files & Code Review',
    4: 'Context Crafting, Few-Shot Prompt Engineering, FIM Lifecycle & Chat Token Management',
    5: 'Developer Productivity, Legacy Modernization, Edge-Case Unit Testing & Security Autofix',
    6: 'Enterprise Privacy, Content Exclusions, Public-Code Filtering, IP Indemnity & REST Seat Governance',
}

DOMAINS = {
    1: 'Use GitHub Copilot responsibly',
    2: 'Use GitHub Copilot features',
    3: 'Understand GitHub Copilot data and architecture',
    4: 'Apply prompt engineering and context crafting',
    5: 'Improve developer productivity with GitHub Copilot',
    6: 'Configure privacy, content exclusions, and safeguards',
}

OFFICIAL_RANGES = {
    1: (15, 20),  # 18 per set (18.0%)
    2: (25, 30),  # 28 per set (28.0%)
    3: (10, 15),  # 14 per set (14.0%)
    4: (10, 15),  # 13 per set (13.0%)
    5: (10, 15),  # 14 per set (14.0%)
    6: (10, 15),  # 13 per set (13.0%)
}

PER_SET_ALLOC = {1: 18, 2: 28, 3: 14, 4: 13, 5: 14, 6: 13}
ALLOCATIONS = {n: dict(PER_SET_ALLOC) for n in range(1, 7)}

SKILLS = {
    # Domain 1: Use GitHub Copilot responsibly (18)
    '1.1': 'Describe risks and limitations of Generative AI tools',
    '1.2': 'Describe ethical and responsible AI usage',
    '1.3': 'Identify potential harms and mitigation strategies of AI usage',
    '1.4': 'Explain the need to validate AI output',
    '1.5': 'Identify how to operate GitHub Copilot responsibly',

    # Domain 2: Use GitHub Copilot features (28)
    '2.1': 'Enable Copilot in the IDE',
    '2.2': 'Trigger Copilot through inline suggestions, chat, CLI, and agent mode',
    '2.3': 'Configure content exclusions for specific files or repositories (app knowledge)',
    '2.4': 'Define GitHub Copilot CLI and how it benefits developers',
    '2.5': 'Identify the steps for installing GitHub Copilot CLI',
    '2.6': 'Describe key GitHub Copilot CLI features and commands',
    '2.7': 'Use GitHub Copilot CLI interactively and in sessions',
    '2.8': 'Generate scripts and manage files with GitHub Copilot CLI',
    '2.9': 'Use Agent Mode, Copilot Edits, and MCP for enhanced development and workflows; manage Agent Sessions and delegate tasks to Sub-Agents for optimized context usage',
    '2.10': 'Use Copilot for code review and coding assistance',
    '2.11': 'Utilize Spaces, Spark, Pull Request summaries, and customizable review standards via instructions files',
    '2.12': 'Understand the limits, options, feedback, and commands of GitHub Copilot Chat; include prompt file reuse for consistent responses',
    '2.13': 'Configure organization-wide policy management; enable Copilot Code Review policies and manage feature availability across IDEs and github.com',
    '2.14': 'Utilize audit log events',
    '2.15': 'Manage subscriptions using the REST API',

    # Domain 3: Understand GitHub Copilot data and architecture (14)
    '3.1': 'Explain data usage, flow, and sharing',
    '3.2': 'Describe input processing and prompt building',
    '3.3': 'Explain proxy filtering and post-processing',
    '3.4': 'Visualize code suggestion lifecycle',
    '3.5': 'Describe limitations of LLMs and Copilot',

    # Domain 4: Apply prompt engineering and context crafting (13)
    '4.1': 'Describe prompt structure and context',
    '4.2': 'Understand how context is determined',
    '4.3': 'Use zero-shot and few-shot prompting',
    '4.4': 'Apply best practices for prompt crafting',
    '4.5': 'Explain prompt engineering principles',
    '4.6': 'Describe prompt process flow and chat history usage',

    # Domain 5: Improve developer productivity with GitHub Copilot (14)
    '5.1': 'Use Copilot for code generation, refactoring, and documentation',
    '5.2': 'Accelerate learning and reduce context switching',
    '5.3': 'Generate sample data and modernize legacy code',
    '5.4': 'Generate unit and integration tests',
    '5.5': 'Identify edge cases and write assertions',
    '5.6': 'Suggest security improvements and performance optimizations',

    # Domain 6: Configure privacy, content exclusions, and safeguards (13)
    '6.1': 'Configure content exclusions and editor settings',
    '6.2': 'Describe ownership and limitations of outputs',
    '6.3': 'Enable suggestions matching public code filtering',
    '6.4': 'Resolve issues with suggestions and content exclusions',
}

SKILL_PLAN = {
    # Domain 1 (18)
    '1.1': 4, '1.2': 4, '1.3': 3, '1.4': 4, '1.5': 3,
    # Domain 2 (28)
    '2.1': 2, '2.2': 2, '2.3': 2, '2.4': 1, '2.5': 2, '2.6': 2, '2.7': 2, '2.8': 2,
    '2.9': 3, '2.10': 2, '2.11': 3, '2.12': 2, '2.13': 1, '2.14': 1, '2.15': 1,
    # Domain 3 (14)
    '3.1': 3, '3.2': 3, '3.3': 3, '3.4': 2, '3.5': 3,
    # Domain 4 (13)
    '4.1': 2, '4.2': 3, '4.3': 2, '4.4': 2, '4.5': 2, '4.6': 2,
    # Domain 5 (14)
    '5.1': 3, '5.2': 2, '5.3': 3, '5.4': 2, '5.5': 2, '5.6': 2,
    # Domain 6 (13)
    '6.1': 4, '6.2': 3, '6.3': 3, '6.4': 3,
}

assert len(SKILLS) == 41
assert sum(SKILL_PLAN.values()) == 100
for _d, _target in PER_SET_ALLOC.items():
    assert sum(v for k, v in SKILL_PLAN.items() if int(k.split('.')[0]) == _d) == _target

VALID_TASKS = set(SKILLS)

TYPE_PLAN = {'multiple-choice': 76, 'ordering': 8, 'multi-select': 16}
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
MULTI_PLAN = {1: 3, 2: 5, 3: 2, 4: 2, 5: 2, 6: 2}
COMPLETION_FLOOR = 20
PROPOSED_SOL_FLOOR = 6
SAMPLE_TOTAL = 18  # 3 items (2 MC + 1 MS) per domain across all 6 GH-300 domains

assert sum(MULTI_PLAN.values()) == 16
assert CERT_PAGE_URL and STUDY_GUIDE_URL

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
