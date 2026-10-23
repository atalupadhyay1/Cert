"""Load 600 authored AI-300 items. Source order is preserved; export shuffles options."""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
DOMAINS={1:'Design and implement an MLOps infrastructure',
         2:'Implement machine learning model lifecycle and operations',
         3:'Design and implement a GenAIOps infrastructure',
         4:'Implement generative AI quality assurance and observability',
         5:'Optimize generative AI systems and model performance'}
TOPICS={1:'Full-Length Mock Exam 1',2:'Full-Length Mock Exam 2',3:'Full-Length Mock Exam 3',
        4:'Full-Length Mock Exam 4',5:'Full-Length Mock Exam 5',6:'Full-Length Mock Exam 6'}
# Local study-map IDs, not Microsoft objective numbers.
SKILLS={
 '1.1':'Workspace, Compute, and Datastore Provisioning',
 '1.2':'Data Assets, Environments, and Component Reuse',
 '1.3':'Infrastructure as Code with Bicep',
 '1.4':'Azure CLI and Declarative Job Automation',
 '1.5':'GitHub Actions CI/CD and Workload Identity Federation',
 '1.6':'Model Registry and Environment Promotion',
 '1.7':'Network Isolation, Secrets, and Pipeline Identity',
 '2.1':'Training Pipeline Authoring and Orchestration',
 '2.2':'Job Configuration, Compute Targets, and Sweeps',
 '2.3':'Experiment Tracking with MLflow',
 '2.4':'Model Registration, Versioning, and Metadata',
 '2.5':'Managed Online Endpoint Deployment',
 '2.6':'Batch Endpoints and Controlled Traffic Rollout',
 '2.7':'Autoscaling, Health Probes, and Rollback',
 '2.8':'Data and Model Drift Monitoring',
 '3.1':'Foundry Hub, Project, and Shared Capacity',
 '3.2':'Model Catalog Selection and Deployment Capacity',
 '3.3':'Prompt Flow Authoring and DAG Composition',
 '3.4':'Flow Connections, Secrets, and Runtime Identity',
 '3.5':'Retrieval-Augmented Grounding with Azure AI Search',
 '3.6':'Chunking, Embeddings, and Index Refresh',
 '3.7':'Prompt and Flow Versioning with Evaluation Gates',
 '3.8':'Agent Orchestration and Tool Binding',
 '4.1':'Evaluation Dataset and Ground-Truth Design',
 '4.2':'Groundedness and Relevance Evaluation',
 '4.3':'Coherence, Fluency, and Similarity Metrics',
 '4.4':'Safety, Jailbreak, and Content Filter Evaluation',
 '5.1':'Token Cost, Caching, and Throughput Planning',
 '5.2':'Model Routing, Distillation, and Right-Sizing',
 '5.3':'Latency Budgets and Streaming Design',
 '5.4':'Retrieval Tuning for Relevance and Cost',
 '4.5':'Tracing, Logging, and Application Insights Observability',
 '4.6':'Online Feedback Loops and Continuous Evaluation',
 '5.5':'Prompt Compression and Context Discipline',
 '5.6':'Fine-Tuning and Distillation for Quality',
 '5.7':'Batch Inference and Provisioned Capacity Optimization',
}
VALID_TASKS=set(SKILLS)
OFFICIAL_WEIGHTS={1:(15,20),2:(25,30),3:(20,25),4:(10,15),5:(10,15)}
# 100-item exams: 18/29/23/15/15 percent, all inside the published ranges.
ALLOCATIONS={n:{1:18,2:29,3:23,4:15,5:15} for n in range(1,7)}
TYPE_PLAN={'multiple-choice':76,'multi-select':16,'ordering':8}
CASE_STUDIES=4          # four case studies of three questions per exam
ITEM_TOTAL=sum(TYPE_PLAN.values())
BANK={}
for number in TOPICS:
    records=[]
    path=HERE/'questions'/f'{number}.txt'
    if not path.is_file():
        continue
    for line_number,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip() or line.startswith('#'):continue
        parts=[x.strip() for x in line.split('|')]
        if len(parts)!=6:raise ValueError(f'{path.name}:{line_number}: expected 6 fields')
        skill,kind,answers,distractors,question,reason=parts
        answer_keys=[x.strip() for x in answers.split(',') if x.strip()]
        distractor_keys=[x.strip() for x in distractors.split(',') if x.strip()]
        records.append(dict(id=f'T{number}-Q{len(records)+1:03}',task=skill,
                            domain=int(skill.split('.')[0]),kind=kind,
                            answers=answer_keys,distractors=distractor_keys,
                            keys=answer_keys+distractor_keys,
                            question=question,reason=reason,line=line_number))
    BANK[number]=records
