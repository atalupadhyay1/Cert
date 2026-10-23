#!/usr/bin/env python3
"""Export original AB-620 mock-exam items; Python 3.10+, standard library only."""
import csv, json, random, sys
from collections import Counter
from pathlib import Path
from bank import BANK, TERMS, TOPICS, VALID_TASKS, DOMAINS, ALLOCATIONS, SKILLS, TYPE_PLAN, CASE_STUDIES, ITEM_TOTAL
ROOT=Path(__file__).resolve().parents[1]
from sources import GUIDE, DOCS
from cases import CASES
HEADER=['Question','Question Type']
for i in range(1,7): HEADER += [f'Answer Option {i}',f'Explanation {i}']
HEADER += ['Correct Answers','Overall Explanation','Domain']

CASE_TAG='Case study — '
CASE_SIZE=3

def case_name(text):
    if text.startswith(CASE_TAG):
        return text[len(CASE_TAG):].split(':')[0].strip()
    return ''

SEQUENCING = TYPE_PLAN['ordering']
# Udemy's bulk importer accepts only these two labels. Sequencing items are
# authored as 'ordering' internally and exported as multiple-choice, because
# each one already offers four candidate sequences with a single key.
EXPORT_PLAN = {'multiple-choice': TYPE_PLAN['multiple-choice'] + SEQUENCING,
               'multi-select': TYPE_PLAN['multi-select']}
ALLOWED_TYPES = ('multiple-choice', 'multi-select')

def expected_type(record):
    if record['kind'] in ('M2','M3'): return 'multi-select'
    return 'multiple-choice'

def make_rows(number):
    rng=random.Random(103000+number)
    records=sorted(BANK[number],key=lambda r:(case_name(r['question'])!='',case_name(r['question'])))
    singles=[r for r in records if r['kind'] in ('S','O')]
    positions=[]
    slots=[i%4 for i in range(len(singles))]
    positions=slots[:]
    rng.shuffle(positions)
    rows,mapping=[],[]
    for record in records:
        opts=list(record['answers'])+list(record['distractors'])
        if record['kind'] in ('S','O'):
            correct=record['answers'][0]
            rest=[k for k in opts if k!=correct]
            rng.shuffle(rest)
            rest.insert(positions.pop(),correct)
            opts=rest
        else:
            rng.shuffle(opts)
        row=dict.fromkeys(HEADER,'')
        case=case_name(record['question'])
        stem=record['question'][len(CASE_TAG)+len(case)+2:] if case else record['question']
        row['_case']=case
        row['_stem']=stem
        row['Question']=record['question']
        row['Question Type']=expected_type(record)
        for i,key in enumerate(opts,1):
            label,meaning=TERMS[key]
            row[f'Answer Option {i}']=label
            if key in record['answers']:
                row[f'Explanation {i}']=f'Correct. {meaning} In this case: {record["reason"]}'
            else:
                row[f'Explanation {i}']=f'Incorrect for this question. {meaning} Why the correct answer wins: {record["reason"]}'
        correct_idx=[i for i,key in enumerate(opts,1) if key in record['answers']]
        row['Correct Answers']=','.join(map(str,correct_idx))
        letters=', '.join(chr(64+i) for i in correct_idx)
        answer_labels='; '.join(TERMS[k][0] for k in record['answers'])
        row['Overall Explanation']=(f'Answer{"" if len(record["answers"])==1 else "s"}: {answer_labels}. {record["reason"]} '
            + ' '.join(TERMS[k][1] for k in record['answers'])
            + f' Local study-map skill {record["task"]} ({SKILLS[record["task"]]}), mapped to the official guide: {GUIDE} '
            f'Primary reference: {DOCS[record["domain"]]}')
        row['Domain']=DOMAINS[record['domain']]
        rows.append(row)
        mapping.append(dict(question=len(rows),id=record['id'],topic=TOPICS[number],
                            domain=record['domain'],task=record['task'],kind=record['kind'],
                            correct_terms=list(record['answers']),option_terms=opts,
                            correct_indices=correct_idx))
    return rows,mapping

def render_test(number,rows):
    lines=[f'# Microsoft AB-620 — {TOPICS[number]}', '',
           f'AI Agent Builder Associate · {len(rows)} questions · 120 minutes · passing target 700/1000', '',
           f'Blueprint-weighted mock exam. Item mix: {EXPORT_PLAN["multiple-choice"]} multiple-choice (selection count stated where needed), '
           f'{EXPORT_PLAN["multi-select"]} multi-select, and {CASE_STUDIES} case studies of {CASE_SIZE} questions. '
           f'{SEQUENCING} of the multiple-choice items ask you to choose the correct candidate sequence. '
           'Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.', '',
           'Original educational content, not actual, recalled, or copied Microsoft exam items.', '',
           '## Questions','']
    seen=None
    for n,row in enumerate(rows,1):
        case=row['_case']
        if case and case!=seen:
            lines += ['---', '', f'## Case study — {case}', '',
                      f'The next {CASE_SIZE} questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.', '']
        seen=case or None
        stem=row['_stem']
        lines += [f'### {n}. {stem}', '', f'Domain: {row["Domain"]}', '']
        for i in range(1,7):
            if row[f'Answer Option {i}']:
                lines.append(f'- {chr(64+i)}. {row[f"Answer Option {i}"]}')
        lines.append('')
    lines += ['---','','## Answer key and explanations','']
    for n,row in enumerate(rows,1):
        letters=', '.join(chr(64+int(x)) for x in row['Correct Answers'].split(','))
        lines += [f'### Question {n} — {letters}', '', row['Overall Explanation'], '']
        for i in range(1,7):
            if row[f'Explanation {i}']:
                lines.append(f'- **{chr(64+i)}:** {row[f"Explanation {i}"]}')
        lines.append('')
    return '\n'.join(lines)

def render_case_brief():
    """One document with every case-study scenario and its three questions."""
    lines=['# AB-620 case study briefs','',
           'Every mock exam contains four case studies of three questions. The scenario below is the shared context;',
           'the three items that follow it are scored individually. Paste the relevant section into a Udemy lecture,',
           'a downloadable resource, or the practice-test description when you want the scenario available before the questions.','']
    for number in range(1,7):
        rows,_=make_rows(number)
        cases=[r['_case'] for r in rows if r['_case']]
        lines += [f'## Exam {number}','']
        for case in dict.fromkeys(cases):
            lines += [f'### Case study — {case}','',CASES[case],'','Questions in this block','']
            n=0
            for row in rows:
                if row['_case']!=case: continue
                n+=1
                letters=', '.join(chr(64+int(x)) for x in row['Correct Answers'].split(','))
                lines.append(f'{n}. {row["_stem"]} _({letters})_')
            lines.append('')
    return '\n'.join(lines)

def render_case_embedded(number, rows):
    """Self-contained variant: the scenario is repeated inside every case-item stem."""
    embedded=[]
    for row in rows:
        row=dict(row)
        if row['_case']:
            row['Question']=f'Case study — {row["_case"]}: {CASES[row["_case"]]} {row["_stem"]}'
        embedded.append(row)
    return embedded

def check_source():
    stems=set()
    if {r['task'] for rs in BANK.values() for r in rs} != VALID_TASKS:
        raise ValueError('Source must cover every local study-map skill')
    for number,records in BANK.items():
        if len(records)!=ITEM_TOTAL:
            raise ValueError(f'Test {number}: expected {ITEM_TOTAL} authored items, found {len(records)}')
        if Counter(r['domain'] for r in records)!=Counter(ALLOCATIONS[number]):
            raise ValueError(f'Test {number}: wrong domain allocation')
        kinds=Counter('ordering' if r['kind']=='O' else ('multi-select' if r['kind'] in ('M2','M3') else 'multiple-choice') for r in records)
        if kinds!=Counter(TYPE_PLAN):
            raise ValueError(f'Test {number}: wrong item-type mix {kinds}')
        cases=Counter(case_name(r['question']) for r in records if case_name(r['question']))
        if len(cases)!=CASE_STUDIES or set(cases.values())!={CASE_SIZE}:
            raise ValueError(f'Test {number}: expected {CASE_STUDIES} case studies of {CASE_SIZE} questions, found {dict(cases)}')
        for item in records:
            if item['task'] not in VALID_TASKS:
                raise ValueError(f'Unknown skill: {item["task"]}')
            n_answers=len(item['answers'])
            if item['kind']=='S' and (n_answers!=1 or len(item['distractors'])!=3):
                raise ValueError(f'{item["id"]}: single-choice needs 1 answer and 3 distractors')
            if item['kind']=='M2' and (n_answers!=2 or len(item['distractors'])!=3):
                raise ValueError(f'{item["id"]}: M2 needs 2 answers and 3 distractors')
            if item['kind']=='M3' and (n_answers!=3 or len(item['distractors'])!=3):
                raise ValueError(f'{item["id"]}: M3 needs 3 answers and 3 distractors')
            if item['kind']=='O' and (n_answers!=1 or len(item['distractors'])!=3):
                raise ValueError(f'{item["id"]}: ordering needs 1 correct sequence and 3 alternatives')
            if len(item['keys'])!=len(set(item['keys'])):
                raise ValueError(f'{item["id"]}: duplicate option key')
            for key in item['keys']:
                if key not in TERMS:
                    raise ValueError(f'Unknown term: {key}')
            stem_ok=item['question'].endswith('?') or item['question'].endswith('Select two.') or item['question'].endswith('Select three.')
            if len(item['reason'].split())<6 or '?' not in item['question'] or not stem_ok:
                raise ValueError(f'Missing rationale/question: {item["id"]}')
            if n_answers>1:
                words={2:'two',3:'three'}[n_answers]
                if f'Select {words}' not in item['question'] and f'select {words}' not in item['question']:
                    raise ValueError(f'{item["id"]}: multi-select must state "Select {words}"')
            norm=''.join(c for c in item['question'].casefold() if c.isalnum())
            if norm in stems:
                raise ValueError(f'Duplicate question: {item["id"]}')
            stems.add(norm)
    names={case_name(r['question']) for rs in BANK.values() for r in rs if case_name(r['question'])}
    if names!=set(CASES):
        raise ValueError(f'Case-study scenarios do not match the bank: {sorted(names^set(CASES))}')
    if len(stems)!=ITEM_TOTAL*len(BANK):
        raise ValueError(f'Expected {ITEM_TOTAL*len(BANK)} distinct stems, found {len(stems)}')

def main():
    check_source()
    manifest={}
    for number in range(1,7):
        rows,mapping=make_rows(number)
        folder=ROOT/'03-practice-sets'/f'set-{number}'
        folder.mkdir(parents=True,exist_ok=True)
        with (folder/f'practice-set-{number}.csv').open('w',encoding='utf-8-sig',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=HEADER,lineterminator='\n',extrasaction='ignore')
            writer.writeheader(); writer.writerows(rows)
        (folder/f'practice-set-{number}.md').write_text(render_test(number,rows),encoding='utf-8')
        counts=Counter(row['Domain'] for row in rows)
        types=Counter(row['Question Type'] for row in rows)
        (folder/'README.md').write_text(
            f'# {TOPICS[number]}: AB-620 mock exam\n\n'
            f'{len(rows)} original items · 120 minutes · passing target 700/1000 · blueprint-weighted.\n\n'
            '| Official domain | Questions |\n|---|---:|\n'
            + '\n'.join(f'| {DOMAINS[d]} | {counts[DOMAINS[d]]} |' for d in DOMAINS)
            + f'\n\nItem mix: {types["multiple-choice"]} multiple-choice (including {SEQUENCING} sequencing items), {types["multi-select"]} multi-select; '
            f'{CASE_STUDIES} case studies of {CASE_SIZE} questions. '
            f'Microsoft does not publish an item count for AB-620; reviewers report 40–60 questions in 120 minutes. This practice set is {len(rows)}, an expanded bank for broader coverage. '
            'Hot-area, drag-and-drop, labs, and adaptive problem-solution sets are not reproduced.\n\n'
            f'Upload `practice-set-{number}.csv`; use `practice-set-{number}.md` for offline review.\n\n'
            'Practice target 700/1000 mirrors the published passing score, but a practice percentage is not a scaled exam score.\n',encoding='utf-8')
        manifest[str(number)]=mapping
        print(f'Built set {number}: {len(rows)} questions')
    (ROOT/'04-resources/answer-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')

    (ROOT/'04-resources/case-studies.md').write_text(render_case_brief(),encoding='utf-8')
    if '--embed-case' in sys.argv[1:]:
        for number in range(1,7):
            rows,mapping=make_rows(number)
            embedded=render_case_embedded(number,rows)
            path=ROOT/f'03-practice-sets/set-{number}/case-embedded-set-{number}.csv'
            with path.open('w',encoding='utf-8-sig',newline='') as f:
                writer=csv.DictWriter(f,fieldnames=HEADER,extrasaction='ignore',lineterminator='\n')
                writer.writeheader()
                for row in embedded:
                    writer.writerow({k:row.get(k,'') for k in HEADER})
            longest=max(len(r['Question']) for r in embedded)
            print(f'Wrote {path.name} (self-contained case stems, longest {longest} characters)')
    print('Wrote 04-resources/case-studies.md')

if __name__=='__main__': main()
