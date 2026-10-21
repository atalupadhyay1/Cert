"""Load 600 individually authored questions; source keys precede shuffled export keys."""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
DOMAINS={1:'Agents and Workflows',2:'Applications and Integration',3:'Claude Code',4:'Eval, Testing, and Debugging',5:'Model Selection and Optimization',6:'Prompt and Context Engineering',7:'Security and Safety',8:'Tools and MCPs'}
TOPICS={1:'Applications and Integration',2:'Agents, Workflows, Tools and MCPs',3:'Model Selection and Optimization',4:'Prompt and Context Engineering',5:'Security, Claude Code and Debugging',6:'Integrated Developer Scenarios and Final Review'}
# Numeric identifiers are LOCAL study-map IDs; the guide names rather than numbers skills.
SKILLS={
 '1.1':'Agent Architecture','1.2':'Agent Construction with Claude','1.3':'Agent Patterns and Frameworks',
 '2.1':'Understanding Requirements','2.2':'Systems Life Cycle','2.3':'Claude API Mechanics','2.4':'Software Engineering Foundations','2.5':'Claude Application Design','2.6':'Configuration Management',
 '3.1':'Claude Code Operation','4.1':'Debugging and Error Handling',
 '5.1':'LLM Fundamentals','5.2':'Technical Fundamentals','5.3':'Model Selection and Tradeoffs','5.4':'Cost and Token Management',
 '6.1':'Context Engineering','6.2':'Prompt Engineering','6.3':'Output Handling',
 '7.1':'AI Application Security','7.2':'Guardrails and Safe Deployment','7.3':'Claude Hooks','7.4':'Identity, Secrets, and Key Management',
 '8.1':'Tool Implementation','8.2':'MCP Server Development','8.3':'Agentic Customization'}
VALID_TASKS=set(SKILLS)
OFFICIAL_WEIGHTS={1:14.7,2:33.1,3:3.1,4:2.6,5:16.8,6:11.0,7:8.1,8:10.6}
ALLOCATIONS={1:{2:100},2:{1:50,8:50},3:{5:100},4:{6:100},5:{7:50,3:25,4:25},6:{1:15,2:33,3:3,4:3,5:17,6:11,7:8,8:10}}
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
