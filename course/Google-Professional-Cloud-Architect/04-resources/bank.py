"""Load 600 authored PCA items. Source order is preserved; export shuffles options."""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
DOMAINS={1:'Designing and planning a cloud solution architecture',
         2:'Managing and provisioning a solution infrastructure',
         3:'Designing for security and compliance',
         4:'Analyzing and optimizing technical and business processes',
         5:'Managing implementation',
         6:'Ensuring solution and operations excellence'}
TOPICS={1:'Full-Length Mock Exam 1',2:'Full-Length Mock Exam 2',3:'Full-Length Mock Exam 3',
        4:'Full-Length Mock Exam 4',5:'Full-Length Mock Exam 5',6:'Full-Length Mock Exam 6'}
SUBTITLES={
 1:'Design Foundations and Workload Placement',
 2:'Provisioning, Networking, and Platform Engineering',
 3:'Security, Compliance, and AI Safety',
 4:'Optimization, Cost, and Continuity',
 5:'Implementation, Delivery, and Migration',
 6:'Reliability, Operations, and Cross-Industry Capstone',
}
# Local study-map IDs, not Google objective numbers.
SKILLS={
 '1.1':'Business Requirements and Success Metrics',
 '1.2':'Non-Functional Requirements and Trade-offs',
 '1.3':'High Availability and Failover Design',
 '1.4':'Network Design',
 '1.5':'Storage and Data Store Selection',
 '1.6':'Compute Platform Selection',
 '1.7':'Data Processing and Analytics Selection',
 '1.8':'AI and ML Solution Design',
 '1.9':'Migration Planning and Future Improvement',
 '2.1':'Hybrid and Multicloud Connectivity',
 '2.2':'Storage Configuration and Lifecycle',
 '2.3':'Compute Provisioning and Patch Management',
 '2.4':'Container Orchestration',
 '2.5':'Serverless Configuration',
 '2.6':'Infrastructure as Code',
 '2.7':'Agent Platform ML Workflows',
 '2.8':'Prebuilt AI APIs and Model Garden',
 '3.1':'IAM and Least Privilege',
 '3.2':'Resource Hierarchy and Organization Policy',
 '3.3':'Encryption, CMEK, and Secrets',
 '3.4':'VPC Service Controls and Network Security',
 '3.5':'Secure Remote Access and Zero Trust',
 '3.6':'Software Supply Chain Security',
 '3.7':'Securing AI Workloads',
 '3.8':'Compliance, Residency, and Audit Logging',
 '4.1':'SDLC and CI/CD Design',
 '4.2':'Root Cause Analysis',
 '4.3':'Testing and Validation',
 '4.4':'Disaster Recovery and Business Continuity',
 '4.5':'Cost Optimization',
 '4.6':'Stakeholder and Change Management',
 '4.7':'Service Catalog and Provisioning',
 '5.1':'Deployment and Release Strategy',
 '5.2':'API Management',
 '5.3':'Data and System Migration Tooling',
 '5.4':'Programmatic Access and Emulators',
 '5.5':'Client Libraries and API Practices',
 '6.1':'Observability Design',
 '6.2':'Alerting and Service Level Objectives',
 '6.3':'Release Management and Support',
 '6.4':'Reliability Testing',
 '6.5':'Operational Excellence and Quality Control',
}
VALID_TASKS=set(SKILLS)
# Google publishes one approximate weight per domain, not a range.
OFFICIAL_WEIGHTS={1:25.0,2:17.5,3:17.5,4:15.0,5:12.5,6:12.5}
# 100-item exams: the published weights rounded to whole items (25/18/17/15/12/13).
ALLOCATIONS={n:{1:25,2:18,3:17,4:15,5:12,6:13} for n in range(1,7)}
TYPE_PLAN={'multiple-choice':76,'multi-select':16,'ordering':8}
CASE_STUDIES=4          # four case studies per exam
CASE_SIZE=5             # five questions each = 20% of the exam
ITEM_TOTAL=sum(TYPE_PLAN.values())
BANK={}
for number in TOPICS:
    records=[]
    path=HERE/'questions'/f'{number}.txt'
    for line_number,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip() or line.startswith('#'):continue
        parts=[x.strip() for x in line.split('|')]
        if len(parts)!=6:raise ValueError(f'{path.name}:{line_number}: expected 6 fields, got {len(parts)}')
        skill,kind,answers,distractors,question,reason=parts
        answer_keys=[x.strip() for x in answers.split(',') if x.strip()]
        distractor_keys=[x.strip() for x in distractors.split(',') if x.strip()]
        records.append(dict(id=f'T{number}-Q{len(records)+1:03}',task=skill,
                            domain=int(skill.split('.')[0]),kind=kind,
                            answers=answer_keys,distractors=distractor_keys,
                            keys=answer_keys+distractor_keys,
                            question=question,reason=reason,line=line_number))
    BANK[number]=records
