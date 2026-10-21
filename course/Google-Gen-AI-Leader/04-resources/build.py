#!/usr/bin/env python3
"""Deterministically export original Google Cloud Generative AI Leader questions; Python 3.10+, stdlib only."""
import csv
import json
import random
from collections import Counter
from pathlib import Path
from bank import BANK, TERMS, TOPICS, VALID_TASKS

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = {
 1: 'Fundamentals of gen AI',
 2: "Google Cloud’s gen AI offerings",
 3: 'Techniques to improve gen AI model output',
 4: 'Business strategies for a successful gen AI solution',
}
OFFICIAL_WEIGHTS = {1: 30, 2: 35, 3: 20, 4: 15}
GUIDE = 'https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf'
HEADER = ['Question', 'Question Type']
for i in range(1,7):
    HEADER += [f'Answer Option {i}', f'Explanation {i}']
HEADER += ['Correct Answers', 'Overall Explanation', 'Domain']
STUDY = 'https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf'

def make_rows(number):
    rng = random.Random(600100 + number)
    positions = [i % 4 for i in range(100)]
    rng.shuffle(positions)
    rows, mapping = [], []
    for record in BANK[number]:
        correct = record['keys'][0]
        keys = record['keys'][1:]
        rng.shuffle(keys)
        keys.insert(positions.pop(), correct)
        row = dict.fromkeys(HEADER, '')
        row['Question'] = record['question']
        row['Question Type'] = 'multiple-choice'
        for i, key in enumerate(keys, 1):
            label, meaning = TERMS[key]
            row[f'Answer Option {i}'] = label
            status = 'Correct' if key == correct else 'Incorrect for this question'
            row[f'Explanation {i}'] = f"{status}. {meaning} In this case: {record['reason']}"
        row['Correct Answers'] = str(keys.index(correct)+1)
        row['Overall Explanation'] = (
            f"Answer: {TERMS[correct][0]}. {record['reason']} {TERMS[correct][1]} "
            f"Closest official exam-guide objective {record['task']}: {GUIDE} "
            f"Official study guide: {STUDY}")
        row['Domain'] = DOMAINS[record['domain']]
        rows.append(row)
        mapping.append(dict(question=len(rows), id=record['id'], topic=TOPICS[number],
                            domain=record['domain'], task=record['task'],
                            correct_terms=[correct], option_terms=keys))
    return rows, mapping

def render_test(number, rows):
    lines = [f'# Google Cloud Generative AI Leader — Practice Set {number}', '',
             f'{TOPICS[number]}', '',
             '100 questions · Suggested practice duration: 160 minutes · Practice target: 80%', '',
             'Topical learning test, not an exam-weighted mock. Related concepts recur across topics.', '',
             'Select ONE best answer for every question. Answer key follows all questions.', '',
             'Original educational content, not actual or recalled Google exam items.', '', '## Questions', '']
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
    questions = set()
    for number, records in BANK.items():
        if len(records) != 100:
            raise ValueError(f'Test {number}: expected 100 authored items, found {len(records)}')
        for item in records:
            if item['task'] not in VALID_TASKS:
                raise ValueError(f"Unknown objective: {item['task']}")
            if len(item['keys']) != 4 or len(set(item['keys'])) != 4:
                raise ValueError(f"Invalid options: {item['keys']}")
            for key in item['keys']:
                if key not in TERMS:
                    raise ValueError(f'Unknown term: {key}')
            if len(item['reason'].split()) < 8 or not item['question'].endswith('?'):
                raise ValueError(f"Missing rationale/question: {item['id']}")
            normalized = ''.join(c for c in item['question'].casefold() if c.isalnum())
            if normalized in questions:
                raise ValueError(f"Duplicate question: {item['id']}")
            questions.add(normalized)
    if len(questions) != 600:
        raise ValueError('Expected 600 distinct authored questions')

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
        counts = Counter(row['Domain'] for row in rows)
        (folder/'README.md').write_text(
            f'# Practice Test {number}: {TOPICS[number]}\n\n'
            '100 original single-answer, four-option questions. Select ONE best answer.\n\n'
            'Topical learning test, not an exam-weighted simulation. Concept checks and short scenarios; '
            'related concepts are reinforced across topics. Technical enrichment is not a promise of exam depth.\n\n'
            '| Closest official domain | Questions |\n|---|---:|\n' +
            '\n'.join(f'| {domain} | {count} |' for domain,count in counts.items()) +
            f'\n\nUpload `practice-set-{number}.csv`; use `practice-set-{number}.md` for offline review.\n\n'
            'Suggested duration: 160 minutes; practice target: 80%. These are custom learning settings, '
            'not official exam timing or scaled-score equivalents.\n', encoding='utf-8')
        manifest[str(number)] = mapping
        print(f'Built set {number}: {len(rows)} questions')
    (ROOT/'04-resources/answer-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')

if __name__ == '__main__':
    main()
