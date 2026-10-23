"""Load 600 authored PAA questions; source keys precede shuffled export keys."""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
DOMAINS={1:'Building Agents Using Low-Code Tools',2:'Using Coding Agents for Application Development',
         3:'Developing Custom Agents',4:'Evaluating and Deploying Agentic Workflows',
         5:'Securing and Governing Agentic Workflows'}
TOPICS={1:'Low-Code Agents and Coding Agents',2:'Custom Agents: Models, ADK, Memory, RAG, and Retrieval',
        3:'Custom Agents: Identity, Orchestration, and Registry',4:'Evaluating and Deploying Agentic Workflows',
        5:'Securing and Governing Agentic Workflows',6:'Integrated Architect Scenarios and Final Review'}
# Numeric IDs are LOCAL study-map identifiers, not official objective numbers.
SKILLS={
 '1.1':'State-Based Workflow Design','1.2':'Agent Instructions and Prompt Templates',
 '1.3':'Enterprise Data Connection','1.4':'Low-Code Change and Release Control',
 '2.1':'Coding Agent Configuration and Tooling','2.2':'Customization Primitives',
 '2.3':'Secure Sandboxes','2.4':'Code Modernization and Vulnerability Remediation',
 '2.5':'Coding Agent Operations and Oversight',
 '3.1':'Model Selection and Tradeoffs','3.2':'ADK Agent Construction','3.3':'Sessions, State, and Memory',
 '3.4':'RAG Pipeline Design','3.5':'Vector Search and Managed Retrieval',
 '3.6':'Retrieval Authorization and Evidence Quality','3.7':'Agent Identity and Permissions',
 '3.8':'Registry and Capability Integration','3.9':'Agent-to-Agent Protocols',
 '3.10':'Multi-Agent Workflow Patterns','3.11':'Runtime Coordination and Policies',
 '4.1':'Evaluation Test Sets','4.2':'Evaluation Metrics and Tooling','4.3':'Continuous Evaluation and Regression',
 '4.4':'Runtime Selection','4.5':'Troubleshooting Agent Failures','4.6':'Monitoring and Optimization',
 '5.1':'Authentication and Secure Tool Execution','5.2':'Principal Access Boundaries',
 '5.3':'Agent Gateway and Traffic Governance','5.4':'Registry and Policy Enforcement',
 '5.5':'Guardrails and Human-in-the-Loop','5.6':'Secure Data Access and Identity Propagation'}
VALID_TASKS=set(SKILLS)
OFFICIAL_WEIGHTS={1:13,2:17,3:33,4:22,5:15}
ALLOCATIONS={1:{1:50,2:50},2:{3:100},3:{3:100},4:{4:100},5:{5:100},6:{1:13,2:17,3:33,4:22,5:15}}
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
