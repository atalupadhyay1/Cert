"""Load 600 authored AB-730 items. Source order is preserved; export shuffles options."""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
DOMAINS={1:'Understand generative AI fundamentals',
         2:'Manage prompts and chats by using Microsoft 365 Copilot',
         3:'Manage business content and collaboration by using Microsoft 365 Copilot',
         4:'Drive business outcomes by using agents'}
TOPICS={1:'Full-Length Mock Exam 1',2:'Full-Length Mock Exam 2',3:'Full-Length Mock Exam 3',
        4:'Full-Length Mock Exam 4',5:'Full-Length Mock Exam 5',6:'Full-Length Mock Exam 6'}
# Local study-map IDs, not Microsoft objective numbers.
SKILLS={
 '1.1':'Copilot Data Protection and the Tenant Boundary',
 '1.2':'Context Sources: Work IQ, Web, and App Context',
 '1.3':'Choosing Copilot Chat, Agents, and Copilot Cowork',
 '1.4':'Capability Differences Across Copilot Experiences',
 '1.5':'Inaccuracy, Prompt Injection, and Over-Reliance',
 '1.6':'Verification, Citations, and Human Review',
 '1.7':'Sensitive Data and Oversharing Risk',
 '1.8':'How Data Protection Controls Restrict Results',
 '2.1':'Anatomy of an Effective Prompt and Model Choice',
 '2.2':'Referencing Files, Meetings, People, and the Web',
 '2.3':'Saving Prompts',
 '2.4':'Scheduling Prompts',
 '2.5':'Sharing Prompts',
 '2.6':'Refining Prompts from Responses',
 '2.7':'Copilot Memory and Instructions',
 '2.8':'Finding, Renaming, and Deleting Chats',
 '2.9':'Organizing Work in Notebooks',
 '3.1':'Connectors Beyond Microsoft 365',
 '3.2':'Generating Content from Business Context',
 '3.3':'Images, Visuals, and Charts',
 '3.4':'Content Across Word, Excel, and PowerPoint',
 '3.5':'Deriving Insights Across Work IQ',
 '3.6':'Validating AI Content Against Business Goals',
 '3.7':'Preparing for Meetings',
 '3.8':'The Facilitator Agent',
 '3.9':'Real-Time Catchup',
 '3.10':'Intelligent Recap',
 '3.11':'Collaborating in Copilot Pages',
 '4.1':'Identifying Prebuilt Agent Scenarios',
 '4.2':'Prebuilt Versus Custom Agents',
 '4.3':'Applying Agents Across Copilot Experiences',
 '4.4':'Filtering Chats by Agent',
 '4.5':'Multi-Step Work with Copilot Cowork',
 '4.6':'Prebuilt and Custom Cowork Skills',
 '4.7':'Cowork Security and Known Limitations',
 '4.8':'Delegating Work to Cowork',
 '4.9':'Reviewing Cowork Plans, Progress, and Results',
 '4.10':'Managing Scheduled Tasks in Cowork'}
VALID_TASKS=set(SKILLS)
OFFICIAL_WEIGHTS={1:(25,30),2:(20,25),3:(20,25),4:(20,25)}
# 100-item exams: 28/24/24/24 percent, all inside the published ranges.
ALLOCATIONS={n:{1:28,2:24,3:24,4:24} for n in range(1,7)}
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
