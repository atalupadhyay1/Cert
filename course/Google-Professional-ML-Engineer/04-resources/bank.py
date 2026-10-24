"""Load 600 authored PMLE items. Source order is preserved; export shuffles options.

This course has no case studies: Google's published PMLE format is 50-60
multiple-choice and multiple-select questions with no case-study component,
so the bank carries no `Case study —` stems and the exporter has no case path.
"""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
DOMAINS={1:'Architecting low-code AI solutions',
         2:'Collaborating within and across teams to manage data and models',
         3:'Scaling prototypes into ML models',
         4:'Serving and scaling models',
         5:'Automating and orchestrating ML pipelines',
         6:'Monitoring AI solutions'}
TOPICS={1:'Full-Length Mock Exam 1',2:'Full-Length Mock Exam 2',3:'Full-Length Mock Exam 3',
        4:'Full-Length Mock Exam 4',5:'Full-Length Mock Exam 5',6:'Full-Length Mock Exam 6'}
SUBTITLES={
 1:'Low-Code AI and Foundational Models',
 2:'Data, Features, Notebooks, and Experiments',
 3:'Training at Scale and Model Choice',
 4:'Serving, Packaging, and Scaling Endpoints',
 5:'Pipelines, Retraining, and CI/CD/CT',
 6:'Responsible AI, Monitoring, and Drift',
}
# Local study-map IDs, not Google objective numbers.
SKILLS={
 '1.1':'BigQuery ML Model Building',
 '1.2':'BigQuery ML Feature Engineering and Prediction',
 '1.3':'Agent Platform AutoML',
 '1.4':'Gemini Fine-Tuning with BigQuery',
 '1.5':'Model Garden Model Selection',
 '1.6':'Industry AI APIs',
 '1.7':'Gemini Application Optimization',
 '2.1':'Preprocessing Tool Selection',
 '2.2':'Feature Store',
 '2.3':'PII Handling and Data Privacy',
 '2.4':'Notebook Environments and Security',
 '2.5':'Experiment Tracking',
 '2.6':'Development Environment Selection',
 '2.7':'Evaluation Metrics and LLM-as-a-Judge',
 '2.8':'Metadata and Lineage',
 '3.1':'Model Type Selection',
 '3.2':'Product Selection',
 '3.3':'Deployment Strategy Choice',
 '3.4':'Interpretability',
 '3.5':'Training Data Organization',
 '3.6':'Ingestion into Training Pipelines',
 '3.7':'Custom Training and SDKs',
 '3.8':'Training Failure Troubleshooting',
 '3.9':'Hyperparameter Tuning',
 '3.10':'Fine-Tuning Decisions',
 '3.11':'Hardware and Accelerator Selection',
 '3.12':'Distributed Training',
 '4.1':'Batch and Online Inference',
 '4.2':'Packaging and Custom Containers',
 '4.3':'Model Registry and Versioning',
 '4.4':'Model Rollout Strategies',
 '4.5':'Inference Preprocessing and Postprocessing',
 '4.6':'Endpoint Types and Access',
 '4.7':'Serving Hardware',
 '4.8':'Serving Throughput and Scaling',
 '4.9':'Production Tuning',
 '5.1':'Data and Model Validation',
 '5.2':'Pipeline Orchestration Choice',
 '5.3':'Train and Serve Consistency',
 '5.4':'Retraining Policy',
 '5.5':'CI/CD/CT with Cloud Build',
 '6.1':'Secure AI and Prompt Protection',
 '6.2':'Responsible AI and Bias',
 '6.3':'Explainability',
 '6.4':'Model Monitoring Configuration',
 '6.5':'Skew and Drift Types',
 '6.6':'Generative AI Monitoring',
}
VALID_TASKS=set(SKILLS)
# Google publishes one approximate weight per section; they total 101.
OFFICIAL_WEIGHTS={1:13.0,2:16.0,3:21.0,4:20.0,5:18.0,6:13.0}
# 100-item exams: the published weights with the one-point overshoot removed
# from the smallest section (12/16/21/20/18/13 = 100).
ALLOCATIONS={n:{1:12,2:16,3:21,4:20,5:18,6:13} for n in range(1,7)}
TYPE_PLAN={'multiple-choice':84,'multi-select':16}
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
