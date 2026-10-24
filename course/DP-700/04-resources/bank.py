"""Load 600 authored DP-700 items. Source order is preserved; export shuffles options."""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
DOMAINS={1:'Implement and manage an analytics solution',
         2:'Ingest and transform data',
         3:'Monitor and optimize an analytics solution'}
TOPICS={1:'Full-Length Mock Exam 1',2:'Full-Length Mock Exam 2',3:'Full-Length Mock Exam 3',
        4:'Full-Length Mock Exam 4',5:'Full-Length Mock Exam 5',6:'Full-Length Mock Exam 6'}
# Local study-map IDs, not Microsoft objective numbers.
SKILLS={
 '1.1':'Spark Workspace Settings',
 '1.2':'Domain and OneLake Workspace Settings',
 '1.3':'Apache Airflow Workspace Settings',
 '1.4':'Version Control and Database Projects',
 '1.5':'Deployment Pipelines',
 '1.6':'Workspace and Item-Level Access',
 '1.7':'Row, Column, Object, and File-Level Security',
 '1.8':'Dynamic Data Masking',
 '1.9':'Sensitivity Labels and Endorsement',
 '1.10':'Fabric Audit Logs',
 '1.11':'OneLake Security',
 '1.12':'Choosing Between Dataflow Gen2, Pipeline, and Notebook',
 '1.13':'Schedules, Event Triggers, and Dynamic Parameters',
 '2.1':'Full and Incremental Load Patterns',
 '2.2':'Dimensional Model Preparation',
 '2.3':'Streaming Load Patterns',
 '2.4':'Choosing a Data Store',
 '2.5':'Choosing a Transformation Engine',
 '2.6':'OneLake Shortcuts',
 '2.7':'Mirroring',
 '2.8':'Pipeline Ingestion',
 '2.9':'PySpark Transformation',
 '2.10':'T-SQL and KQL Transformation',
 '2.11':'Denormalization, Grouping, and Aggregation',
 '2.12':'Duplicate, Missing, and Late-Arriving Data',
 '2.13':'Choosing a Streaming Engine',
 '2.14':'Eventstream and Spark Structured Streaming',
 '2.15':'Windowing and Real-Time Tables',
 '3.1':'Monitoring Ingestion and Transformation',
 '3.2':'Monitoring Semantic Model Refresh',
 '3.3':'Alerts and Data Activator',
 '3.4':'Pipeline and Dataflow Gen2 Errors',
 '3.5':'Notebook Errors',
 '3.6':'Eventhouse and Eventstream Errors',
 '3.7':'T-SQL and Shortcut Errors',
 '3.8':'Optimizing Lakehouse Tables',
 '3.9':'Optimizing Pipelines',
 '3.10':'Optimizing the Data Warehouse',
 '3.11':'Optimizing Spark Performance',
 '3.12':'Optimizing Query and Real-Time Performance',
}
VALID_TASKS=set(SKILLS)
OFFICIAL_WEIGHTS={1:(30,35),2:(30,35),3:(30,35)}
# 100-item exams: 33/33/34 percent, all inside the published ranges.
ALLOCATIONS={n:{1:33,2:33,3:34} for n in range(1,7)}
TYPE_PLAN={'multiple-choice':76,'multi-select':16,'ordering':8}
CASE_STUDIES=4          # four case studies of three questions per exam
ITEM_TOTAL=sum(TYPE_PLAN.values())
BANK={}
for number in TOPICS:
    records=[]
    path=HERE/'questions'/f'{number}.txt'
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
