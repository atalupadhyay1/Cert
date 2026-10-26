"""Load 600 authored Professional Cloud Network Engineer items.

Google publishes 50-60 multiple choice and multiple select questions for this
exam and no case-study component, so the bank carries no case stems and the
exporter has no case path. Configuration is unavoidably in scope for this exam:
the guide asks about VPC design, routing, load balancing, NAT, DNS, interconnects
and firewall policy, so items test the judgement behind a change rather than
console recall.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent
DOMAINS = {
    1: 'Designing and Planning a Google Cloud VPC Network',
    2: 'Implementing a VPC Network',
    3: 'Configuring Managed Network Services',
    4: 'Configuring and Implementing Hybrid and Multicloud Interconnectivity',
    5: 'Managing, Monitoring, and Troubleshooting Network Operations',
    6: 'Configuring, Implementing, and Managing a Cloud Network Security Solution',
}
TOPICS = {1: 'Full-Length Mock Exam 1', 2: 'Full-Length Mock Exam 2', 3: 'Full-Length Mock Exam 3',
          4: 'Full-Length Mock Exam 4', 5: 'Full-Length Mock Exam 5', 6: 'Full-Length Mock Exam 6'}
SUBTITLES = {
    1: 'VPC Design, IP Planning, and Load Balancer Choice',
    2: 'VPC Implementation, Routing, and GKE Networking',
    3: 'Load Balancing, Cloud CDN, and Cloud DNS',
    4: 'Interconnect, VPN, and Cloud Router',
    5: 'Observability, Troubleshooting, and Traffic Movement',
    6: 'Cloud Armor, Cloud NGFW, NAT, and Egress Security',
}
# Local study-map IDs, not Google objective numbers.
SKILLS = {
    '1.1': 'Network Service Tier Choice',
    '1.2': 'High Availability, Failover, and DR Design',
    '1.3': 'Hybrid DNS Topology',
    '1.4': 'Load Balancer Selection',
    '1.5': 'GKE Network Planning',
    '1.6': 'IAM for Network Roles',
    '1.7': 'Private Service Connectivity',
    '1.8': 'VPC Type and Interconnect Topology',
    '1.9': 'IP Address Management',
    '1.10': 'MTU Sizing',
    '1.11': 'Third-Party Appliance Insertion',
    '2.1': 'VPC and Subnet Configuration',
    '2.2': 'VPC Network Peering',
    '2.3': 'Shared VPC',
    '2.4': 'Private Google Access and APIs',
    '2.5': 'VPC Service Controls Perimeters',
    '2.6': 'Static and Dynamic Routing',
    '2.7': 'Policy-Based Routing',
    '2.8': 'Internal Load Balancer as Next Hop',
    '2.9': 'Network Connectivity Center',
    '2.10': 'GKE Cluster Networking',
    '2.11': 'VPC Flow Logs',
    '3.1': 'Load Balancer Backend Configuration',
    '3.2': 'Traffic Management and URL Maps',
    '3.3': 'Network Endpoint Groups and Autoscaling',
    '3.4': 'GKE Ingress and Gateway',
    '3.5': 'Cloud CDN',
    '3.6': 'Cloud DNS Zones and Records',
    '3.7': 'DNS Routing Policies',
    '3.8': 'DNSSEC',
    '4.1': 'Dedicated Interconnect',
    '4.2': 'Partner and Cross-Cloud Interconnect',
    '4.3': 'HA VPN',
    '4.4': 'Classic VPN',
    '4.5': 'Cloud Router BGP',
    '4.6': 'BFD and Failover Timers',
    '4.7': 'Route Advertisement and Priority',
    '4.8': 'Interconnect Encryption and SLA',
    '5.1': 'Logging for Network Components',
    '5.2': 'Network Metrics and Dashboards',
    '5.3': 'Connectivity Tests',
    '5.4': 'Performance Dashboard and Packet Loss',
    '5.5': 'Firewall Insights and Network Analyzer',
    '5.6': 'Flow Analyzer and Network Topology',
    '5.7': 'BGP and VPN Troubleshooting',
    '5.8': 'Traffic Draining and Migration',
    '6.1': 'Cloud Armor Policies',
    '6.2': 'WAF and Bot Management',
    '6.3': 'DDoS and Rate Limiting',
    '6.4': 'NGFW Tiers and Policies',
    '6.5': 'Firewall Rules and Micro-Segmentation',
    '6.6': 'Cloud NAT and Port Allocation',
    '6.7': 'Secure Web Proxy',
    '6.8': 'Multi-NIC Appliances and Packet Mirroring',
}
VALID_TASKS = set(SKILLS)
# Google publishes ~21 / ~20 / ~16 / ~16 / ~14 / ~13 percent. Those six weights
# total exactly 100, so the per-exam counts are the weights themselves and no
# rounding correction is applied anywhere in this course.
OFFICIAL_WEIGHTS = {1: 21.0, 2: 20.0, 3: 16.0, 4: 16.0, 5: 14.0, 6: 13.0}
ALLOCATIONS = {n: {1: 21, 2: 20, 3: 16, 4: 16, 5: 14, 6: 13} for n in range(1, 7)}
SKILL_PLAN = {
    '1.1': 2, '1.2': 2, '1.3': 2, '1.4': 2, '1.5': 3, '1.6': 2, '1.7': 2, '1.8': 2,
    '1.9': 2, '1.10': 1, '1.11': 1,
    '2.1': 2, '2.2': 2, '2.3': 2, '2.4': 1, '2.5': 1, '2.6': 3, '2.7': 2, '2.8': 1,
    '2.9': 2, '2.10': 3, '2.11': 1,
    '3.1': 3, '3.2': 2, '3.3': 2, '3.4': 2, '3.5': 2, '3.6': 2, '3.7': 2, '3.8': 1,
    '4.1': 3, '4.2': 2, '4.3': 3, '4.4': 1, '4.5': 3, '4.6': 1, '4.7': 2, '4.8': 1,
    '5.1': 2, '5.2': 2, '5.3': 2, '5.4': 2, '5.5': 2, '5.6': 2, '5.7': 1, '5.8': 1,
    '6.1': 2, '6.2': 2, '6.3': 1, '6.4': 3, '6.5': 2, '6.6': 1, '6.7': 1, '6.8': 1,
}
MULTI_PLAN = {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1}
TYPE_PLAN = {'multiple-choice': 84, 'multi-select': 16}
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
