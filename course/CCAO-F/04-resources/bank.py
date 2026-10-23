"""Load 600 individually authored CCAO-F questions; source keys precede shuffled export keys."""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
DOMAINS={1:'Prompting and Task Execution',2:'Output Evaluation and Validation',3:'Product and Model Selection',
         4:'Workflow Integration and Solution Design',5:'Configuration and Knowledge Management',
         6:'Governance, Risk, and Responsible Use',7:'Troubleshooting and Optimization'}
TOPICS={1:'Prompting and Task Execution',2:'Output Evaluation and Validation',
        3:'Product, Model, and Configuration Decisions',4:'Workflow Integration and Solution Design',
        5:'Governance, Risk, and Troubleshooting',6:'Integrated Associate Scenarios and Final Review'}
# Numeric identifiers are LOCAL study-map IDs. The guide names objectives rather than numbering skills.
SKILLS={
 '1.1':'Prompt Construction','1.2':'Task Decomposition','1.3':'Prompt Iteration','1.4':'Task-Type Strategy',
 '2.1':'Accuracy and Completeness','2.2':'Hallucinations, Inconsistency, and Bias','2.3':'Fact-Checking and Validation',
 '2.4':'Human Review Decisions','2.5':'Audience Adaptation and Comparison','2.6':'Information Organization and Output Formats',
 '3.1':'Product Feature Selection','3.2':'Model Family Differentiation','3.3':'Quality, Speed, and Cost Alignment','3.4':'Context and Memory Management',
 '4.1':'Requirements and Use-Case Analysis','4.2':'Research, Planning, and Process Optimization','4.3':'Solution Design and Iteration',
 '4.4':'Workflow Integration and Redesign','4.5':'Communicating Value and Limitations',
 '5.1':'Project Instructions','5.2':'Knowledge Sources and Connectors','5.3':'System-Level Instructions','5.4':'Configuration Maintenance',
 '6.1':'Appropriate and Inappropriate Use Cases','6.2':'Data Sensitivity, Regulatory, and Privacy','6.3':'Organizational AI Policy and Governance','6.4':'Ethical Implications','6.5':'Escalation and Unsafe Requests',
 '7.1':'Diagnosing Underperforming Prompts and Outputs','7.2':'Adjusting Approach from Feedback','7.3':'Limited or Conflicting Information','7.4':'Workflow Efficiency and Effectiveness'}
VALID_TASKS=set(SKILLS)
OFFICIAL_WEIGHTS={1:14,2:21,3:12,4:16,5:12,6:15,7:10}
ALLOCATIONS={1:{1:100},2:{2:100},3:{3:50,5:50},4:{4:100},5:{6:60,7:40},6:{1:14,2:21,3:12,4:16,5:12,6:15,7:10}}
BANK={}
for number in TOPICS:
    records=[]
    path=HERE/'questions'/f'{number}.txt'
    for line_number,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip() or line.startswith('#'):continue
        parts=[x.strip() for x in line.split('|')]
        if len(parts)!=4:raise ValueError(f'{path.name}:{line_number}: expected 4 fields')
        task,choices,question,reason=parts
        records.append(dict(id=f'T{number}-Q{len(records)+1:03}',task=task,
                            domain=int(task.split('.')[0]),keys=choices.split(','),
                            question=question,reason=reason,line=line_number))
    BANK[number]=records
