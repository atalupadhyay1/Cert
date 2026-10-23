"""Load 600 authored AB-731 items. Source order is preserved; export shuffles options."""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
DOMAINS={1:'Identify the business value of generative AI solutions',
         2:"Identify benefits, capabilities, and opportunities for Microsoft's AI apps and services",
         3:"Identify an implementation and adoption strategy for Microsoft's AI apps and services"}
TOPICS={1:'Full-Length Mock Exam 1',2:'Full-Length Mock Exam 2',3:'Full-Length Mock Exam 3',
        4:'Full-Length Mock Exam 4',5:'Full-Length Mock Exam 5',6:'Full-Length Mock Exam 6'}
# Local study-map IDs, not Microsoft objective numbers.
SKILLS={
 '1.1':'Generative AI Versus Other Types of AI','1.2':'Selecting a Generative AI Solution for a Business Need',
 '1.3':'Pretrained Versus Fine-Tuned Models','1.4':'Token Economics, Cost Drivers, and ROI',
 '1.5':'Fabrications, Reliability, and Bias','1.6':'Business Value, Scalability, and Automation',
 '1.7':'Prompt Engineering Impact and Techniques','1.8':'Grounding Requirements and Retrieval-Augmented Generation',
 '1.9':'Data Type, Data Quality, and Representative Datasets','1.10':'Secure AI and AI Security Considerations',
 '1.11':'When Machine Learning Adds Value and the ML Lifecycle',
 '2.1':'Mapping Business Processes to Copilot','2.2':'Copilot Editions and Capability Differences',
 '2.3':'Copilot Chat Web and Mobile Experiences','2.4':'Copilot in Microsoft 365 Apps',
 '2.5':'Microsoft Copilot Studio','2.6':'Microsoft Graph and Organizational Grounding',
 '2.7':'Integrated AI Solutions, Risk Mitigation, and Safety','2.8':'Researcher and Analyst in Copilot',
 '2.9':'Build, Buy, or Extend and the Extensibility Framework','2.10':'Foundry Tools: Microsoft Foundry, Azure Vision, and Azure AI Search',
 '2.11':'Matching an AI Model to a Business Need',
 '3.1':'Responsible AI and Governance Principles','3.2':'The AI Council and Cross-Functional Oversight',
 '3.3':'Responsible AI Standards in Practice','3.4':'Adoption Team and AI Champions Program',
 '3.5':'Barriers to Adoption and Change Management','3.6':'Data, Security, Privacy, and Cost Impacts',
 '3.7':'Copilot License Types','3.8':'Foundry Tools Subscription and Commitment Models'}
VALID_TASKS=set(SKILLS)
OFFICIAL_WEIGHTS={1:(35,40),2:(35,40),3:(20,25)}
# 100-item exams: 37/38/25 percent, all inside the published ranges.
ALLOCATIONS={n:{1:37,2:38,3:25} for n in range(1,7)}
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
