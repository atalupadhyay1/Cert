"""Original topical question sources. One authored item per line; no stem templates.

Format: objective | correct-term,distractor,distractor,distractor | question | rationale
The correct term is first in source only; the exporter balances displayed positions.
"""
import json
from pathlib import Path
from extra_terms import extend
HERE = Path(__file__).resolve().parent
TERMS = json.loads((HERE / 'terms.json').read_text(encoding='utf-8'))
extend(TERMS)
TOPICS = {
    1: 'Generative AI Foundations, Models & Core Concepts',
    2: 'Google Cloud Services, Gemini & AI Ecosystem',
    3: 'Prompt Engineering, Grounding & Output Improvement',
    4: 'AI Applications, Agents & Business Use Cases',
    5: 'Responsible AI, Security, Privacy & Risk Management',
    6: 'Strategy, Adoption, Transformation & Business Value',
}
VALID_TASKS = {f'{d}.{i}' for d,n in [(1,4),(2,5),(3,3),(4,3)] for i in range(1,n+1)}
BANK = {}
for number in TOPICS:
    records = []
    for line_number, line in enumerate((HERE / 'questions' / f'{number}.txt').read_text(encoding='utf-8').splitlines(),1):
        if not line.strip() or line.startswith('#'):
            continue
        parts = line.split('|')
        if len(parts) != 4:
            raise ValueError(f'Test {number}, line {line_number}: expected four fields')
        task, choices, question, reason = (x.strip() for x in parts)
        records.append(dict(id=f'T{number}-Q{len(records)+1:03}', task=task,
                            domain=int(task.split('.')[0]), keys=choices.split(','),
                            question=question, reason=reason, line=line_number))
    BANK[number] = records
