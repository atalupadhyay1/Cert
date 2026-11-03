"""Question bank loader and blueprint constants for Microsoft / GitHub Exam GH-500: GitHub Advanced Security (6 x 100 = 600 questions).

Aligned to the official Microsoft Learn GH-500 Study Guide (Skills measured as of July 2026;
Last updated May 14, 2026; certification page updated May 4, 2026) awarding the GitHub Advanced Security certification.
"""

import re
from pathlib import Path

from sources import (
    BLUEPRINT_EFFECTIVE_DATE,
    CERT_PAGE_URL,
    DOMAINS as _STR_DOMAINS,
    SKILLS as _RAW_SKILLS,
    SKILL_PLAN,
    SKILL_SOURCES,
    STUDY_GUIDE_URL,
)
from terms import TERMS

EXAM_CODE = 'GH-500'
EXAM_TITLE = 'GitHub Advanced Security'
CREDENTIAL_TITLE = 'GitHub Advanced Security'
STUDY_GUIDE_DATE = BLUEPRINT_EFFECTIVE_DATE
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
    1: 'Security Suites Ecosystem, Security Overview, Prevention-First SDLC & Alert Governance',
    2: 'GitHub Secret Protection, Push Protection, Validity Checks, Delegated Bypass & Custom Patterns',
    3: 'Supply Chain Security, SPDX SBOMs, EPSS, Auto-Triage Rules, dependabot.yml & Dependency Review',
    4: 'Code Security (CodeQL), SARIF 2.1.0 Ingestion, Matrix Build Modes, Taint Dataflow & Copilot Autofix',
    5: 'Security Operations, Private Advisories (GHSA/CVE/CWE), Security Campaigns, Variant Analysis & Rulesets',
    6: 'Security Suites Administration, Security Configurations, GHEC vs GHES, Committer/AI Billing & REST APIs',
}

DOMAINS = {int(k): v for k, v in _STR_DOMAINS.items()}

OFFICIAL_RANGES = {
    1: (15, 20),  # 18 per set (18.0%)
    2: (15, 20),  # 18 per set (18.0%)
    3: (15, 20),  # 18 per set (18.0%)
    4: (10, 15),  # 14 per set (14.0%)
    5: (15, 20),  # 18 per set (18.0%)
    6: (10, 15),  # 14 per set (14.0%)
}

PER_SET_ALLOC = {1: 18, 2: 18, 3: 18, 4: 14, 5: 18, 6: 14}
ALLOCATIONS = {n: dict(PER_SET_ALLOC) for n in range(1, 7)}

SKILLS = {sk: title for sk, (_dom, title, _url) in _RAW_SKILLS.items()}

assert len(SKILLS) == 34
assert sum(SKILL_PLAN.values()) == 100
for _d, _target in PER_SET_ALLOC.items():
    assert sum(v for k, v in SKILL_PLAN.items() if int(k.split('.')[0]) == _d) == _target

VALID_TASKS = set(SKILLS)

TYPE_PLAN = {'multiple-choice': 76, 'ordering': 8, 'multi-select': 16}
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
MULTI_PLAN = {1: 3, 2: 3, 3: 3, 4: 2, 5: 3, 6: 2}
COMPLETION_FLOOR = 20
PROPOSED_SOL_FLOOR = 6
SAMPLE_TOTAL = 18  # 3 items (2 MC + 1 MS) per domain across all 6 GH-500 domains

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
