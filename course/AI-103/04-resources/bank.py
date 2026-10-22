"""Load 600 authored AI-103 items. Source order is preserved; export shuffles options."""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
DOMAINS={1:'Plan and manage an Azure AI solution',2:'Implement generative AI and agentic solutions',
         3:'Implement computer vision solutions',4:'Implement text analysis solutions',
         5:'Implement information extraction solutions'}
TOPICS={1:'Full-Length Mock Exam 1',2:'Full-Length Mock Exam 2',3:'Full-Length Mock Exam 3',
        4:'Full-Length Mock Exam 4',5:'Full-Length Mock Exam 5',6:'Full-Length Mock Exam 6'}
# Local study-map IDs, not Microsoft objective numbers.
SKILLS={
 '1.1':'Selecting Foundry Models and Services','1.2':'Retrieval, Memory, Tool, and Knowledge Services',
 '1.3':'Infrastructure, Deployment, and CI/CD','1.4':'Quotas, Scaling, and Cost',
 '1.5':'Monitoring Performance, Drift, Safety, and Grounding','1.6':'Security, Identity, and Networking',
 '1.7':'Responsible AI Controls and Oversight',
 '2.1':'Building Generative Applications','2.2':'Foundry SDK and Project Integration',
 '2.3':'Evaluating Models and Applications','2.4':'Agent Roles, Goals, and Tool Schemas',
 '2.5':'Agent Tools, Retrieval, Memory, and Function Calling','2.6':'Multi-Agent Orchestration and Safeguards',
 '2.7':'Agent Monitoring and Error Analysis','2.8':'Generation Tuning and Observability',
 '3.1':'Image Generation and Editing','3.2':'Video Generation and Editing',
 '3.3':'Multimodal Understanding and Accessibility','3.4':'Visual Extraction and Video Analysis',
 '3.5':'Multimodal Responsible AI',
 '4.1':'Language Model Text Analysis','4.2':'Translation','4.3':'Speech Solutions','4.4':'Domain Customization',
 '5.1':'Content Ingestion and Indexing','5.2':'Search and Grounding Configuration','5.3':'Enrichment Skills',
 '5.4':'RAG Ingestion and OCR','5.5':'Retrieval Integration with Agents','5.6':'Document and Content Extraction'}
VALID_TASKS=set(SKILLS)
OFFICIAL_WEIGHTS={1:(25,30),2:(30,35),3:(10,15),4:(10,15),5:(10,15)}
# 100-item tests: 28/33/13/13/13 percent, all inside the published ranges.
ALLOCATIONS={n:{1:28,2:33,3:13,4:13,5:13} for n in range(1,7)}
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
