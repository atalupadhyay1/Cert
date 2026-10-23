"""Load 600 authored AB-410 items. Source order is preserved; export shuffles options."""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
DOMAINS={1:'Create a foundation for intelligent applications',
         2:'Create intelligent applications',
         3:'Build business application logic and automation'}
TOPICS={1:'Full-Length Mock Exam 1',2:'Full-Length Mock Exam 2',3:'Full-Length Mock Exam 3',
        4:'Full-Length Mock Exam 4',5:'Full-Length Mock Exam 5',6:'Full-Length Mock Exam 6'}
# Local study-map IDs, not Microsoft objective numbers.
SKILLS={
 '1.1':'Requirements Analysis and Component Selection',
 '1.2':'Built-in Agents and Extensibility Options',
 '1.3':'Environment Types, Solutions, and ALM',
 '1.4':'Tables in the Data Workspace',
 '1.5':'Standard Tables and Table Properties',
 '1.6':'Columns and Table Relationships',
 '1.7':'Prompt Columns and Row Summaries',
 '1.8':'Public Views and Main Forms',
 '1.9':'Record and Column Security',
 '2.1':'Model-Driven Forms',
 '2.2':'Model-Driven Views',
 '2.3':'Generative Pages',
 '2.4':'Model-Driven App Composition and Access',
 '2.5':'Model-Driven Charts and Dashboards',
 '2.6':'Canvas Apps Built From Data',
 '2.7':'Accessibility, Performance, and Responsiveness',
 '2.8':'Reusable Components, Named Formulas, and Functions',
 '2.9':'Variables, Collections, and Error Handling',
 '2.10':'Canvas App Testing and Copilot Studio Agents',
 '3.1':'Cloud Flow Triggers',
 '3.2':'Connector Selection',
 '3.3':'Approvals in Cloud Flows',
 '3.4':'Cloud Flow Actions and Data Operations',
 '3.5':'Flow Control with Conditions and Loops',
 '3.6':'Cloud Flow Testing and Troubleshooting',
 '3.7':'Prompts in AI Hub',
 '3.8':'Prompt Inputs and Knowledge',
 '3.9':'Prompt Settings and Model Selection',
 '3.10':'Consuming Prompts and Models in Apps and Flows',
 '3.11':'Business Rules',
 '3.12':'Business Process Flows',
 '3.13':'Calculated, Rollup, and Formula Columns',
 '3.14':'Choosing the Right Business Logic',
}
VALID_TASKS=set(SKILLS)
OFFICIAL_WEIGHTS={1:(25,30),2:(25,30),3:(40,45)}
# 100-item exams: 28/28/44 percent, all inside the published ranges.
ALLOCATIONS={n:{1:28,2:28,3:44} for n in range(1,7)}
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
