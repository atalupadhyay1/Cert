"""Blueprint constants and question-bank loader for Microsoft Exam PL-500 (6 x 100 = 600 questions)."""
from pathlib import Path

from cases import CASES
from sources import CERTIFICATION_URL, EXAM_URL, RETIREMENT_URL, SKILL_SOURCES, STUDY_GUIDE_URL
from terms import TERMS

EXAM_CODE = 'PL-500'
EXAM_TITLE = 'Microsoft Power Automate RPA Developer'
CREDENTIAL_TITLE = 'Microsoft Certified: Power Automate RPA Developer Associate'
STUDY_GUIDE_DATE = 'July 8, 2024'
RETIREMENT_DATE = 'June 30, 2026'
SUCCESSOR_EXAM = (
    'No direct 1:1 replacement exam; Microsoft shifted Business Applications AI/developer skilling '
    'to Exams AB-400 / AB-410 and Power Automate Applied Skills'
)
PREREQUISITES = 'None (Intermediate Associate-level developer exam; no prerequisite certification required)'

ITEM_TOTAL = 100
CASE_STUDIES = 4
CASE_SIZE = 3
CODE_FILL_FLOOR = 15
PROPOSED_SOL_FLOOR = 6

DOMAINS = {
    1: 'Design automations',
    2: 'Develop automations',
    3: 'Deploy and manage automations',
}

OFFICIAL_RANGES = {
    1: (25, 30),
    2: (45, 50),
    3: (20, 25),
}

ALLOCATIONS = {n: {1: 28, 2: 48, 3: 24} for n in range(1, 7)}

TYPE_PLAN = {
    'multiple-choice': 76,
    'ordering': 8,
    'multi-select': 16,
}

KIND_PLAN = {
    'S': 76,
    'O': 8,
    'M2': 13,
    'M3': 3,
}

MULTI_PLAN = {
    1: 4,
    2: 8,
    3: 4,
}

SKILLS = {
    # Domain 1: Design automations (28 items)
    '1.1': 'Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures',
    '1.2': 'Differentiate target application, browser, terminal, and virtual desktop automation options',
    '1.3': 'Differentiate desktop flow execution methods and cloud/desktop concurrency models',
    '1.4': 'Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions',
    '1.5': 'Assess Dataverse Work Queues applicability and design .NET custom actions',
    '1.6': 'Design automations integrating Canvas apps, Model-driven apps, and Microsoft Dataverse',
    '1.7': 'Design automations with connectors, custom connectors, connections, and connection references',
    '1.8': 'Differentiate AI Builder document/data models and recommend desktop OCR capabilities',
    '1.9': 'Recommend and design solutions with the Document Automation Toolkit',
    '1.10': 'Design desktop automations using PowerShell, VBScript, Python, and DOS scripts',
    '1.11': 'Recommend JavaScript web execution and design DOM CSS/XPath selector strategies',
    # Domain 2: Develop automations (48 items)
    '2.1': 'Develop solution cloud flows that invoke attended and unattended desktop flows',
    '2.2': 'Develop and call modular Child cloud flows passing inputs and returning outputs',
    '2.3': 'Call external REST APIs from cloud flows using HTTP authentication and pagination',
    '2.4': 'Implement cloud flow Trigger Conditions, Concurrency Control, and Split On',
    '2.5': 'Implement cloud flow ISO 8601 action Timeouts and Retry Policies',
    '2.6': 'Implement cloud flow Data Operations (Compose, Parse JSON, Select, Filter array, CSV/HTML)',
    '2.7': 'Parse JSON, XML (xpath/xml), and CSV payloads in cloud flows',
    '2.8': 'Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions',
    '2.9': 'Implement Datatables, Lists, and Custom Objects in Power Automate for desktop',
    '2.10': 'Implement Subflows and target application lifecycle routines in desktop flows',
    '2.11': 'Call external REST and SOAP APIs in desktop flows (Invoke web service / SOAP)',
    '2.12': 'Implement action-level On error retry policies and UI/web Wait timeouts in desktop flows',
    '2.13': 'Automate Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows',
    '2.14': 'Implement, sign, package (.cab), and upload .NET custom actions in desktop flows',
    '2.15': 'Implement loops, flow control, WDL expressions, and variables in cloud and desktop flows',
    '2.16': 'Implement cloud Secure Inputs/Outputs, desktop Sensitive variables, and run queue Priority',
    '2.17': 'Implement System Exception blocks (Scope / On block error) vs Business Exception routines',
    '2.18': 'Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue)',
    '2.19': 'Build Custom Connectors with authentication, policy templates, and C# ScriptBase code',
    '2.20': 'Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions',
    '2.21': 'Test, debug, and externalize configuration across cloud and desktop flows',
    # Domain 3: Deploy and manage automations (24 items)
    '3.1': 'Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene',
    '3.2': 'Differentiate environment-specific Credentials, Connection References, and deployment bindings',
    '3.3': 'Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution',
    '3.4': 'Assess Power Platform DLP policies and Desktop Flow module/action DLP governance',
    '3.5': 'Assess and configure DLP endpoint filtering and host rules for Custom Connectors',
    '3.6': 'Share cloud flows, desktop flows, machines, and machine groups with least privilege',
    '3.7': 'Recommend RPA security roles and implement Service Principals vs Windows Service Accounts',
    '3.8': 'Register machines via Power Automate machine runtime and manage Machine Groups',
    '3.9': 'Implement load balancing of unattended desktop flows across Machine Groups and queues',
    '3.10': 'Operate the desktop flow run queue and analyze portal run history and machine telemetry',
}

SKILL_PLAN = {
    # Domain 1 (28)
    '1.1': 3, '1.2': 3, '1.3': 2, '1.4': 3, '1.5': 3, '1.6': 2,
    '1.7': 2, '1.8': 3, '1.9': 2, '1.10': 2, '1.11': 3,
    # Domain 2 (48)
    '2.1': 2, '2.2': 2, '2.3': 2, '2.4': 2, '2.5': 2, '2.6': 2, '2.7': 2,
    '2.8': 3, '2.9': 2, '2.10': 2, '2.11': 2, '2.12': 2, '2.13': 2, '2.14': 2,
    '2.15': 2, '2.16': 2, '2.17': 3, '2.18': 3, '2.19': 3, '2.20': 3, '2.21': 3,
    # Domain 3 (24)
    '3.1': 3, '3.2': 2, '3.3': 3, '3.4': 3, '3.5': 2,
    '3.6': 3, '3.7': 2, '3.8': 2, '3.9': 2, '3.10': 2,
}

assert sum(SKILL_PLAN.values()) == ITEM_TOTAL
assert set(SKILLS) == set(SKILL_PLAN) == set(SKILL_SOURCES)
for _d in DOMAINS:
    assert sum(v for k, v in SKILL_PLAN.items() if int(k.split('.')[0]) == _d) == ALLOCATIONS[1][_d]

TOPICS = {
    1: 'Practice Exam 1 — Banking, Mainframe 3270 & Mortgage Servicing RPA',
    2: 'Practice Exam 2 — Healthcare Citrix VDI, HL7 Labs & Hosted RPA',
    3: 'Practice Exam 3 — Customs Brokerage, Freight Gateways & Custom Actions',
    4: 'Practice Exam 4 — Automotive AS/400 5250, COM Scripting & Custom Connectors',
    5: 'Practice Exam 5 — Smart-Grid Work Queues, OCR Selectors & RPA Debugging',
    6: 'Practice Exam 6 — Public-Sector Document Automation, DLP & Enterprise ALM',
}

SUBTITLES = {
    1: 'Mainframe terminal emulation, Key Vault credentials, Document Automation Toolkit, dynamic selectors, and run queue priority',
    2: 'Citrix Virtual Desktop Agent, XML/XPath cloud flows, Windows Server RDSH concurrency, webpage JavaScript, and Hosted Machine Groups',
    3: 'On-Premises Data Gateway, Business vs System exceptions, ms-powerautomate URLs, signed .NET CAB custom actions, and VM session hygiene',
    4: 'IBM 5250 terminal sessions, Datatables, VBScript/PowerShell COM automation, Custom Connector C# ScriptBase, and Portal Monitor telemetry',
    5: 'Dataverse Work Queues with SLAs/requeue, Tesseract OCR + regex fallback selectors, PAD Breakpoints/Static Result, and CyberArk/Solution Layers',
    6: 'Raw JSON Invoke web service, multi-page CSS table scraping, solution Child Flows, Desktop Flow module DLP, and Managed pipeline upgrades',
}

QUESTIONS_DIR = Path(__file__).resolve().parent / 'questions'
SPLIT_PIPE = __import__('re').compile(r'(?<!\\)\|')


def _load_set(set_number: int) -> list[dict]:
    qfile = QUESTIONS_DIR / f'{set_number}.txt'
    if not qfile.is_file():
        return []
    records = []
    for lineno, raw in enumerate(qfile.read_text(encoding='utf-8').splitlines(), start=1):
        s = raw.strip()
        if not s or s.startswith('#'):
            continue
        parts = [p.replace(r'\|', '|').strip() for p in SPLIT_PIPE.split(s)]
        if len(parts) != 8:
            raise ValueError(f'{qfile.name}:{lineno}: expected 8 pipe-separated fields, got {len(parts)}: {raw!r}')
        qid, task, kind, domain_s, question, ans_s, dis_s, reason = parts
        domain = int(domain_s)
        if task not in SKILLS:
            raise ValueError(f'{qfile.name}:{lineno} ({qid}): unknown skill {task!r}')
        if int(task.split('.')[0]) != domain:
            raise ValueError(f'{qfile.name}:{lineno} ({qid}): skill {task} mismatches domain {domain}')
        answers = [x.strip() for x in ans_s.split(',') if x.strip()]
        distractors = [x.strip() for x in dis_s.split(',') if x.strip()]
        records.append({
            'id': qid,
            'task': task,
            'kind': kind,
            'domain': domain,
            'question': question,
            'answers': answers,
            'distractors': distractors,
            'keys': answers + distractors,
            'reason': reason,
        })
    return records


BANK = {n: _load_set(n) for n in range(1, 7)}

__all__ = [
    'ALLOCATIONS',
    'BANK',
    'CASES',
    'CASE_SIZE',
    'CASE_STUDIES',
    'CERTIFICATION_URL',
    'CODE_FILL_FLOOR',
    'CREDENTIAL_TITLE',
    'DOMAINS',
    'EXAM_CODE',
    'EXAM_TITLE',
    'EXAM_URL',
    'ITEM_TOTAL',
    'KIND_PLAN',
    'MULTI_PLAN',
    'OFFICIAL_RANGES',
    'PREREQUISITES',
    'PROPOSED_SOL_FLOOR',
    'RETIREMENT_DATE',
    'RETIREMENT_URL',
    'SKILLS',
    'SKILL_PLAN',
    'SKILL_SOURCES',
    'STUDY_GUIDE_DATE',
    'STUDY_GUIDE_URL',
    'SUBTITLES',
    'SUCCESSOR_EXAM',
    'TERMS',
    'TOPICS',
    'TYPE_PLAN',
]
