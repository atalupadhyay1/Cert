"""Load 600 individually authored questions; source keys precede shuffled export keys."""
from pathlib import Path
from terms import TERMS
HERE=Path(__file__).resolve().parent
TOPICS={
 1:'Agentic Architecture & Orchestration',
 2:'Tool Design & MCP Integration',
 3:'Claude Code Configuration & Workflows',
 4:'Prompt Engineering & Structured Output',
 5:'Context Management & Reliability',
 6:'Integrated Architecture Scenarios & Final Review',
}
VALID_TASKS={f'{d}.{t}' for d,count in [(1,7),(2,5),(3,6),(4,6),(5,6)] for t in range(1,count+1)}
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
