"""Load 600 authored AB-620 items. Source order is preserved; export shuffles options."""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
DOMAINS={1:'Plan and configure agent solutions',
         2:'Integrate and extend agents in Copilot Studio',
         3:'Test and manage agents'}
TOPICS={1:'Full-Length Mock Exam 1',2:'Full-Length Mock Exam 2',3:'Full-Length Mock Exam 3',
        4:'Full-Length Mock Exam 4',5:'Full-Length Mock Exam 5',6:'Full-Length Mock Exam 6'}
# Local study-map IDs, not Microsoft objective numbers.
SKILLS={
 '1.1':'Enterprise Integration and Solution Planning','1.2':'Identity Strategy and Authentication',
 '1.3':'Channels, Deployment, and Audience Design','1.4':'Responsible AI, Security, and Governance',
 '1.5':'Reusable Agent Components and Solutions','1.6':'Agent Flows, Actions, and Connectors',
 '1.7':'Human-in-the-Loop Agent Flows','1.8':'Flow Parameters, Error Handling, and Monitoring',
 '1.9':'Topics, Response Formatting, and Variables','1.10':'Custom Prompts, Adaptive Cards, and Generative Answers',
 '2.1':'Copilot Connectors and Power Platform Connectors','2.2':'Azure AI Search Grounding',
 '2.3':'Computer Use Agents','2.4':'MCP Tools','2.5':'Custom Connectors and REST APIs',
 '2.6':'Multi-Agent Design in Copilot Studio','2.7':'Foundry Agent Integration',
 '2.8':'Connected and Existing Agents','2.9':'Fabric Data Agents','2.10':'A2A Protocol Solutions',
 '2.11':'Foundry Model Catalog and Custom Prompts','2.12':'Application Insights Monitoring',
 '3.1':'Test Set Design','3.2':'Evaluation Methods','3.3':'Reviewing and Acting on Results',
 '3.4':'Solution Packaging for Agents','3.5':'Environment Variables and Configuration',
 '3.6':'Power Platform Pipelines','3.7':'Extending Pipelines and Deployment Controls',
 '3.8':'Production Quality Monitoring and Continuous Evaluation'}
VALID_TASKS=set(SKILLS)
OFFICIAL_WEIGHTS={1:(30,35),2:(40,45),3:(20,25)}
# 100-item exams: 33/42/25 percent, all inside the published ranges.
ALLOCATIONS={n:{1:33,2:42,3:25} for n in range(1,7)}
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
        records.append(dict(id=f'T{number}-Q{len(records)+1:03d}',task=skill,
                            domain=int(skill.split('.')[0]),kind=kind,
                            answers=answer_keys,distractors=distractor_keys,
                            keys=answer_keys+distractor_keys,
                            question=question,reason=reason,line=line_number))
    BANK[number]=records
