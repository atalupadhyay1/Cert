"""Load 600 authored Professional Cloud Security Engineer items.

Google publishes 50-60 multiple choice and multiple select questions for this
exam and no case-study component, so the bank carries no case stems and the
exporter has no case path.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent
DOMAINS = {
    1: 'Configuring Access',
    2: 'Securing Communications and Establishing Boundary Protection',
    3: 'Ensuring Data Protection',
    4: 'Managing Operations',
    5: 'Supporting Compliance Requirements',
}
TOPICS = {1: 'Full-Length Mock Exam 1', 2: 'Full-Length Mock Exam 2', 3: 'Full-Length Mock Exam 3',
          4: 'Full-Length Mock Exam 4', 5: 'Full-Length Mock Exam 5', 6: 'Full-Length Mock Exam 6'}
SUBTITLES = {
    1: 'Identity, Service Accounts, and the Resource Hierarchy',
    2: 'Firewalls, Perimeters, and Private Connectivity',
    3: 'Sensitive Data, Keys, and Confidential Computing',
    4: 'Automation, Detection, and Logging',
    5: 'Compliance Controls and the Shared Responsibility Model',
    6: 'Threat Detection, AI Security, and Regulatory Evidence',
}
# Local study-map IDs, not Google objective numbers.
SKILLS = {
    '1.1': 'Cloud Identity, SSO, and Directory Sync',
    '1.2': 'Super Administrator and Lifecycle Automation',
    '1.3': 'Workforce Identity Federation',
    '1.4': 'Service Account Hygiene and Default Accounts',
    '1.5': 'Service Account Keys and Short-Lived Credentials',
    '1.6': 'Workload Identity Federation',
    '1.7': 'Service Account Impersonation',
    '1.8': 'Password, Session, and 2-Step Verification Policy',
    '1.9': 'Privileged Roles, Separation of Duties, and PAM',
    '1.10': 'IAM Conditions, Deny Policies, and Access Context Manager',
    '1.11': 'Resource Hierarchy and Organization Policies',
    '2.1': 'Firewall Rules and Hierarchical Policies',
    '2.2': 'Layer 7 Inspection',
    '2.3': 'Cloud Armor Web Application Firewall',
    '2.4': 'Identity-Aware Proxy',
    '2.5': 'TLS, Load Balancing, and Certificate Authority Service',
    '2.6': 'Secure Web Proxy and Cloud DNS Security',
    '2.7': 'Private Addressing and API Restriction',
    '2.8': 'VPC Firewalls, Peering, and Shared VPC',
    '2.9': 'VPC Service Controls',
    '2.10': 'HA VPN and Cloud Interconnect',
    '2.11': 'Private Google Access and Private Service Connect',
    '2.12': 'Cloud NAT Egress',
    '3.1': 'Sensitive Data Protection Discovery',
    '3.2': 'De-identification Templates',
    '3.3': 'Access Control for BigQuery, Cloud Storage, and Cloud SQL',
    '3.4': 'Secret Manager',
    '3.5': 'Instance Metadata Protection',
    '3.6': 'Default Encryption and CMEK',
    '3.7': 'Cloud EKM and Key Import',
    '3.8': 'Key Rotation and Revocation',
    '3.9': 'Confidential Computing',
    '3.10': 'Storage Lifecycle and Retention',
    '4.1': 'CVE Scanning in CI/CD',
    '4.2': 'Binary Authorization',
    '4.3': 'Hardened Images and Patch Management',
    '4.4': 'Posture Management and Drift Detection',
    '4.5': 'Network Logs, Cloud IDS, and Packet Mirroring',
    '4.6': 'Logging Strategy and Secure Log Access',
    '4.7': 'Audit Logs and Data Access Logs',
    '4.8': 'Log Sinks and SIEM Export',
    '4.9': 'Security Command Center Findings',
    '5.1': 'Shared Responsibility Model',
    '5.2': 'Assured Workloads',
    '5.3': 'Access Transparency and Access Approval',
    '5.4': 'Regionalization of Data and Services',
    '5.5': 'Mapping Requirements to Controls',
    '5.6': 'Scoping the Compliance Boundary',
}
VALID_TASKS = set(SKILLS)
# Google publishes one approximate weight per section; these total exactly 100.
OFFICIAL_WEIGHTS = {1: 25.0, 2: 22.0, 3: 23.0, 4: 19.0, 5: 11.0}
# 100-item exams: the published weights are already whole items, so no
# rounding correction is needed anywhere in this course.
ALLOCATIONS = {n: {1: 25, 2: 22, 3: 23, 4: 19, 5: 11} for n in range(1, 7)}
# Every exam uses the same per-skill template, so the six sets are comparable
# and every local study area is exercised in each one.
SKILL_PLAN = {
    '1.1': 3, '1.2': 2, '1.3': 2, '1.4': 3, '1.5': 3, '1.6': 2, '1.7': 2, '1.8': 2, '1.9': 2, '1.10': 2, '1.11': 2,
    '2.1': 2, '2.2': 2, '2.3': 2, '2.4': 2, '2.5': 2, '2.6': 2, '2.7': 2, '2.8': 2, '2.9': 2, '2.10': 2, '2.11': 1, '2.12': 1,
    '3.1': 3, '3.2': 3, '3.3': 3, '3.4': 2, '3.5': 2, '3.6': 3, '3.7': 2, '3.8': 2, '3.9': 2, '3.10': 1,
    '4.1': 2, '4.2': 2, '4.3': 2, '4.4': 2, '4.5': 3, '4.6': 2, '4.7': 2, '4.8': 2, '4.9': 2,
    '5.1': 2, '5.2': 2, '5.3': 2, '5.4': 2, '5.5': 2, '5.6': 1,
}
# Multi-select items per official domain, 4 + 4 + 4 + 3 + 1 = 16.
MULTI_PLAN = {1: 4, 2: 4, 3: 4, 4: 3, 5: 1}
TYPE_PLAN = {'multiple-choice': 84, 'multi-select': 16}
ITEM_TOTAL = sum(TYPE_PLAN.values())
BANK = {}
for number in TOPICS:
    records = []
    path = HERE / 'questions' / f'{number}.txt'
    for line_number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip() or line.startswith('#'):
            continue
        parts = [x.strip() for x in line.split('|')]
        if len(parts) != 6:
            raise ValueError(f'{path.name}:{line_number}: expected 6 fields, got {len(parts)}')
        skill, kind, answers, distractors, question, reason = parts
        answer_keys = [x.strip() for x in answers.split(',') if x.strip()]
        distractor_keys = [x.strip() for x in distractors.split(',') if x.strip()]
        records.append(dict(id=f'T{number}-Q{len(records) + 1:03}', task=skill,
                            domain=int(skill.split('.')[0]), kind=kind,
                            answers=answer_keys, distractors=distractor_keys,
                            keys=answer_keys + distractor_keys,
                            question=question, reason=reason, line=line_number))
    BANK[number] = records
