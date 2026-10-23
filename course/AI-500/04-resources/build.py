#!/usr/bin/env python3
"""Deterministically export original AI-500 questions; Python 3.10+, stdlib only."""
import csv
import json
import random
from collections import Counter
from pathlib import Path
from bank import ITEMS, TERMS, OVERRIDES

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = {
 1: 'Architect multi-agent solutions',
 2: 'Develop multi-agent solutions in Azure',
 3: 'Evaluate, optimize, and monitor multi-agent solutions',
 4: 'Secure, govern, and deploy multi-agent solutions',
}
WEIGHTS = {1: 18, 2: 33, 3: 24, 4: 25}
RANGES = {1: (15,20), 2: (30,35), 3: (20,25), 4: (20,25)}
GUIDE = 'https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500'
HEADER = ['Question', 'Question Type']
for i in range(1,7):
    HEADER += [f'Answer Option {i}', f'Explanation {i}']
HEADER += ['Correct Answers', 'Overall Explanation', 'Domain']
LEARNING_PATHS = {
 1: 'https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/',
 2: 'https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/',
 3: 'https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/',
 4: 'https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/',
}

def is_multi(record):
    return record['correct'] == 2

def make_rows(number):
    rng = random.Random(500100 + number)
    records = list(enumerate(ITEMS, 1))
    rng.shuffle(records)
    positions = [i % 4 for i in range(90)]
    rng.shuffle(positions)
    rows, mapping = [], []
    for objective, base in records:
        record = OVERRIDES.get((number, objective), base)
        keys = record['keys'][:]
        correct = set(keys[:record['correct']])
        if is_multi(record):
            rng.shuffle(keys)
        else:
            answer = keys.pop(0)
            rng.shuffle(keys)
            keys.insert(positions.pop(), answer)
        row = dict.fromkeys(HEADER, '')
        row['Question'] = record['prompts'][number-1]
        row['Question Type'] = 'multi-select' if is_multi(record) else 'multiple-choice'
        for i, key in enumerate(keys, 1):
            label, meaning = TERMS[key]
            row[f'Answer Option {i}'] = label
            status = 'Correct' if key in correct else 'Incorrect for this requirement'
            row[f'Explanation {i}'] = f'{status}. {meaning}'
        row['Correct Answers'] = ','.join(str(i) for i,k in enumerate(keys,1) if k in correct)
        labels = '; '.join(TERMS[k][0] for k in record['keys'][:record['correct']])
        reason = record['reason'].removeprefix('Select TWO. ')
        row['Overall Explanation'] = (f"Answer: {labels}. {reason} "
            f"Microsoft Learn reference: {GUIDE}#{record['task']} "
            f"Related learning path: {LEARNING_PATHS[record['domain']]}")
        row['Domain'] = DOMAINS[record['domain']]
        rows.append(row)
        mapping.append(dict(question=len(rows), objective=objective, domain=record['domain'],
                            task=record['task'], correct_terms=sorted(correct), option_terms=keys))
    return rows, mapping

def render_test(number, rows):
    lines = [f'# AI-500 — Practice Set {number}', '',
             '100 questions · Suggested practice duration: 180 minutes · Practice target: 80%', '',
             'Select one answer unless the question says Select TWO. Answer key follows all questions.', '',
             'Original educational content, not actual or recalled Microsoft exam items.', '', '## Questions', '']
    for n,row in enumerate(rows,1):
        lines += [f"### {n}. {row['Question']}", '', f"Domain: {row['Domain']}", '']
        for i in range(1,7):
            if row[f'Answer Option {i}']:
                lines.append(f"- {chr(64+i)}. {row[f'Answer Option {i}']}")
        lines.append('')
    lines += ['---', '', '## Answer key and explanations', '']
    for n,row in enumerate(rows,1):
        letters = ', '.join(chr(64+int(x)) for x in row['Correct Answers'].split(','))
        lines += [f'### Question {n} — {letters}', '', row['Overall Explanation'], '']
        for i in range(1,7):
            if row[f'Explanation {i}']:
                lines.append(f"- **{chr(64+i)}:** {row[f'Explanation {i}']}")
        lines.append('')
    return '\n'.join(lines)

def check_source():
    if len(ITEMS) != 100 or Counter(i['domain'] for i in ITEMS) != Counter(WEIGHTS):
        raise ValueError('Expected 100 objectives with 18/33/24/25 distribution')
    for key, record in OVERRIDES.items():
        number, objective = key
        if not 1 <= number <= 6 or not 1 <= objective <= 100:
            raise ValueError('Invalid override coordinates')
        base = ITEMS[objective-1]
        if (record['domain'],record['correct']) != (base['domain'],base['correct']):
            raise ValueError('Override changed blueprint/type')
    for item in [*ITEMS, *OVERRIDES.values()]:
        if len(item['prompts']) != 6 or item['correct'] not in {1,2}:
            raise ValueError('Invalid prompt or correct-answer count')
        count = 5 if is_multi(item) else 4
        if len(item['keys']) != count or len(set(item['keys'])) != count:
            raise ValueError(f"Invalid options: {item['keys']}")
        for key in item['keys']:
            if key not in TERMS:
                raise ValueError(f'Unknown term: {key}')
        if not item['task']:
            raise ValueError('Missing source task')
    questions = [row['Question'].strip().casefold() for n in range(1,7) for row in make_rows(n)[0]]
    if len(set(questions)) != 600:
        raise ValueError('Duplicate final question wording')

def main():
    check_source()
    manifest = {}
    for number in range(1,7):
        rows, mapping = make_rows(number)
        folder = ROOT / '03-practice-sets' / f'set-{number}'
        folder.mkdir(parents=True,exist_ok=True)
        with (folder/f'practice-set-{number}.csv').open('w',encoding='utf-8-sig',newline='') as f:
            writer = csv.DictWriter(f,fieldnames=HEADER,lineterminator='\n')
            writer.writeheader()
            writer.writerows(rows)
        (folder/f'practice-set-{number}.md').write_text(render_test(number,rows),encoding='utf-8')
        (folder/'README.md').write_text(
            f'# AI-500 Practice Set {number}\n\n100 questions: 90 single-answer + 10 select-two.\n\n'
            '| Domain | Questions |\n|---|---:|\n'+
            '\n'.join(f'| {DOMAINS[d]} | {n} |' for d,n in WEIGHTS.items())+
            f'\n\nUpload `practice-set-{number}.csv`; review offline with `practice-set-{number}.md`.\n'
            '\nSuggested duration: 180 minutes; practice target: 80%. These are custom learning settings, not official exam timing or scaled-score equivalents.\n'
            '\nCore objectives and explanations recur in different scenarios across sets. These are not independent psychometric exam forms.\n',encoding='utf-8')
        manifest[str(number)] = mapping
        print(f'Built set {number}: {len(rows)} questions')
    (ROOT/'04-resources/answer-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')

if __name__ == '__main__':
    main()
