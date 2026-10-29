"""Export original PCEP-30-03 mock-exam items; Python 3.10+, stdlib only.

As of October 29, 2026, the OpenEDG Python Institute lists PCEP-30-03 as Pending
Release (scheduled for October 31, 2026) and describes it as a routine exam-version
update under the PCEP-30-0x specification, while the published PCEP-30-0x syllabus
defines a 40-minute proctored exam of 30 items (plus a 5-minute NDA and tutorial) with
a cumulative passing score of 70% across four blocks weighted 18 / 29 / 25 / 28
percent. Because OpenEDG has not yet published a standalone PCEP-30-03 block-weight
table ahead of October 31, 2026, each set here baselines against those published
PCEP-30-0x block weights as an expanded 60-item bank timed at 80 minutes (~80 seconds
per item) and makes no claim about unpublished post-release blueprint changes.

Applied to 60 items, 18 / 29 / 25 / 28 percent gives 10.8 / 17.4 / 15.0 / 16.8, and the
per-exam counts are 11 / 17 / 15 / 17: largest-remainder rounding gives the two spare
items to Blocks 1 and 4, and every count stays within 0.4 items of its published
weight.

Object-oriented programming, external package management (pip), file streams, closures,
and decorators belong to the PCAP associate track rather than entry-level PCEP and are
kept out of scope. Interactive drag-and-drop, sort, and multi-slot code-insert widgets
are excluded by the CSV contract and disclosed; the published exam has no case-study
component, so the exporter has no case path.
"""
import csv
import json
import random
import re
from collections import Counter
from itertools import combinations
from pathlib import Path

from bank import (ALLOCATIONS, BANK, DOMAIN_NOTES, DOMAINS, GAP_FILL_MIN,
                  ITEM_TOTAL, MULTI_PLAN, OFFICIAL_WEIGHTS, SKILL_PLAN, SKILLS,
                  SUBTITLES, TERMS, TOPICS, TYPE_PLAN, VALID_TASKS)
from sources import DOCS, GUIDE

COURSE = 'PCEP – Certified Entry-Level Python Programmer'
ROOT = Path(__file__).resolve().parents[1]
HEADER = ['Question', 'Question Type']
for i in range(1, 7):
    HEADER += [f'Answer Option {i}', f'Explanation {i}']
HEADER += ['Correct Answers', 'Overall Explanation', 'Domain']

EXPORT_PLAN = dict(TYPE_PLAN)
NEAR_DUPLICATE_LIMIT = 0.72
ALLOWED_TYPES = ('multiple-choice', 'multi-select')
MULTI = ('M2', 'M3')


def _flat(text):
    return ' '.join(''.join(c for c in text.casefold() if c.isalnum() or c == ' ').split())


def _stem(word):
    for suffix in ('ing', 'ed', 'es', 's'):
        if len(word) > len(suffix) + 3 and word.endswith(suffix):
            word = word[:-len(suffix)]
            break
    if len(word) > 4 and word.endswith('e'):
        word = word[:-1]
    return word


def _addition(meaning, reason):
    """Return the meaning only when it says something the reason does not."""
    a, b = _flat(meaning), _flat(reason)
    if not a or a == b or a in b or b in a:
        return ''
    wa = {_stem(w) for w in a.split() if len(w) > 3}
    wb = {_stem(w) for w in b.split() if len(w) > 3}
    if wa and wb and len(wa & wb) / len(wa | wb) > 0.5:
        return ''
    return ' ' + meaning


def expected_type(record):
    return 'multi-select' if record['kind'] in MULTI else 'multiple-choice'


def make_rows(number):
    rng = random.Random(300300 + number)
    # Presentation order: grouped by block so the review copy prints one section per block.
    records = sorted(BANK[number], key=lambda r: r['domain'])
    singles = [r for r in records if r['kind'] not in MULTI]
    positions = [i % 4 for i in range(len(singles))]
    rng.shuffle(positions)
    rows, mapping = [], []
    for record in records:
        opts = list(record['answers']) + list(record['distractors'])
        if record['kind'] not in MULTI:
            correct = record['answers'][0]
            rest = [k for k in opts if k != correct]
            rng.shuffle(rest)
            rest.insert(positions.pop(), correct)
            opts = rest
        else:
            rng.shuffle(opts)
        row = dict.fromkeys(HEADER, '')
        row['_stem'] = record['question']
        row['Question'] = record['question']
        row['Question Type'] = expected_type(record)
        for i, key in enumerate(opts, 1):
            label, meaning = TERMS[key]
            row[f'Answer Option {i}'] = label
            if key in record['answers']:
                row[f'Explanation {i}'] = f'Correct.{_addition(meaning, record["reason"])} In this case: {record["reason"]}'
            else:
                row[f'Explanation {i}'] = f'Incorrect for this question. {meaning} Why the correct answer wins: {record["reason"]}'
        correct_idx = [i for i, key in enumerate(opts, 1) if key in record['answers']]
        row['Correct Answers'] = ','.join(map(str, correct_idx))
        answer_labels = '; '.join(TERMS[k][0] for k in record['answers'])
        row['Overall Explanation'] = (
            f'Answer{"s" if len(record["answers"]) > 1 else ""}: {answer_labels}. {record["reason"]} '
            + ''.join(_addition(TERMS[k][1], record['reason']) for k in record['answers'])
            + f' Local study-map skill {record["task"]} ({SKILLS[record["task"]]}), mapped to the official syllabus: {GUIDE}. '
            f'Primary reference: {DOCS[record["domain"]]}.')
        row['Overall Explanation'] = ' '.join(row['Overall Explanation'].split())
        row['Domain'] = DOMAINS[record['domain']]
        rows.append(row)
        mapping.append(dict(question=len(rows), id=record['id'], topic=TOPICS[number],
                            domain=record['domain'], task=record['task'], kind=record['kind'],
                            correct_terms=list(record['answers']), option_terms=opts,
                            correct_indices=correct_idx))
    return rows, mapping


def render_test(number, rows):
    gaps = sum(1 for r in rows if '____' in r['_stem'])
    lines = [f'# {COURSE} (PCEP-30-03) — {TOPICS[number]}', '',
             f'Entry-Level Python Programmer · {len(rows)} questions · 80 minutes · 70% cumulative passing score', '',
             f'Blueprint-weighted expanded mock exam. Item mix: {EXPORT_PLAN["multiple-choice"]} multiple-choice '
             f'(including {gaps} single-blank `____` code-fill / gap-fill items) and '
             f'{EXPORT_PLAN["multi-select"]} multiple-response items (the selection count is stated in each multi-response stem). '
             'Baseline & pre-release notice: as of October 29, 2026, OpenEDG Python Institute lists PCEP-30-03 as Pending '
             'Release (scheduled for October 31, 2026) and describes it as a routine exam-version update under PCEP-30-0x. '
             'Because OpenEDG has not yet published a standalone PCEP-30-03 block-weight table ahead of release, this set '
             'baselines against the published PCEP-30-0x specification — 30 live items in 40 minutes (+5-minute NDA/tutorial) '
             'across four blocks weighted 18 / 29 / 25 / 28 percent — as an expanded 2x bank (60 items in 80 minutes, ~80 '
             'seconds per item) and makes no claim about unpublished post-release blueprint changes. '
             'The Python Institute publishes no fixed split between single-select, multiple-select, and interactive items, so '
             'the 45 / 15 mix and single-blank `____` approximations are authoring choices within the 17-column CSV contract; '
             'interactive drag-and-drop, sort, and multi-slot code-insertion widgets are excluded and disclosed. '
             'The published format has no case-study component, so no case-study item appears here. '
             'See the README for the exact fidelity boundary.', '',
             'Original educational content verified on CPython 3.11, not actual, recalled, or copied OpenEDG exam items.', '',
             '## Questions', '']
    domain = None
    for n, row in enumerate(rows, 1):
        record_domain = next(d for d, label in DOMAINS.items() if label == row['Domain'])
        if record_domain != domain:
            domain = record_domain
            lines += ['---', '', f'## Block {domain} — {DOMAINS[domain]} ({int(OFFICIAL_WEIGHTS[domain])}%) — {DOMAIN_NOTES[domain]}', '']
        lines += [f'### {n}. {row["_stem"]}', '']
        for i in range(1, 7):
            if row[f'Answer Option {i}']:
                lines.append(f'- {chr(64 + i)}. {row[f"Answer Option {i}"]}')
        lines.append('')
    lines += ['---', '', '## Answer key and explanations', '']
    for n, row in enumerate(rows, 1):
        letters = ', '.join(chr(64 + int(x)) for x in row['Correct Answers'].split(','))
        lines += [f'### Question {n} — {letters}', '', row['Overall Explanation'], '']
        for i in range(1, 7):
            if row[f'Explanation {i}']:
                lines.append(f'- **{chr(64 + i)}:** {row[f"Explanation {i}"]}')
        lines.append('')
    return '\n'.join(lines)


def render_set_readme(number, rows):
    counts = Counter(row['Domain'] for row in rows)
    types = Counter(row['Question Type'] for row in rows)
    gaps = sum(1 for r in rows if '____' in r['_stem'])
    return (f'# {TOPICS[number]}: {SUBTITLES[number]}\n\n'
            f'{len(rows)} original items · 80 minutes · 70% cumulative passing score · blueprint-weighted expanded bank.\n\n'
            '| Official PCEP-30-0x syllabus block | Weight | Questions |\n|---|---:|---:|\n'
            + '\n'.join(f'| {DOMAINS[d]} | {int(OFFICIAL_WEIGHTS[d])}% | {counts[DOMAINS[d]]} |'
                        for d in DOMAINS)
            + f'\n\nItem mix: {types["multiple-choice"]} multiple-choice (including {gaps} single-blank `____` '
            f'gap-fill / code-fill items) and {types["multi-select"]} multiple-response. '
            'The published PCEP-30-0x exam delivers 30 items in 40 minutes (plus a 5-minute NDA and tutorial), so this 60-item '
            'set is an expanded 2x bank timed at 80 minutes to match the published pace of about 80 seconds per item. '
            'The Python Institute publishes no split between single-select, multiple-select, and interactive formats, so '
            'the 45 / 15 split is an authoring choice; drag-and-drop, sort, and code-insertion widgets cannot be expressed '
            'in a 17-column CSV and are excluded. The published format has no case-study component, so none is imitated here.\n\n'
            'Passing requires a **cumulative average score of at least 70% across all four syllabus blocks**, with no '
            'separate per-block pass mark; on the live exam each item carries up to 40 raw points normalized to a percentage, '
            'whereas Udemy scores one point per item with all-or-nothing credit on multiple-select items.\n\n'
            'Pre-release baseline notice: as of October 29, 2026, OpenEDG Python Institute lists PCEP-30-03 as Pending '
            'Release (scheduled for October 31, 2026) and describes it as a routine exam-version update under PCEP-30-0x '
            'that does not affect the five-year validity of credentials already earned. Because no standalone PCEP-30-03 '
            'block-weight table has been published ahead of October 31, 2026, this set uses the published PCEP-30-0x '
            '18 / 29 / 25 / 28 baseline and makes no claim about unpublished future blueprint changes.\n\n'
            f'Upload `practice-set-{number}.csv`; use `practice-set-{number}.md` for offline review.\n')


def check_source():
    stems = set()
    if {r['task'] for rs in BANK.values() for r in rs} != VALID_TASKS:
        raise ValueError('Source must cover every local study-map skill')
    for number, records in BANK.items():
        if len(records) != ITEM_TOTAL:
            raise ValueError(f'Test {number}: expected {ITEM_TOTAL} authored items, found {len(records)}')
        if Counter(r['domain'] for r in records) != Counter(ALLOCATIONS[number]):
            raise ValueError(f'Test {number}: wrong domain allocation')
        skills = Counter(r['task'] for r in records)
        if dict(skills) != {k: v for k, v in SKILL_PLAN.items() if v}:
            raise ValueError(f'Test {number}: per-skill counts differ from the study-map plan')
        kinds = Counter(expected_type(r) for r in records)
        if kinds != Counter(TYPE_PLAN):
            raise ValueError(f'Test {number}: wrong item-type mix {kinds}')
        multi = Counter(r['domain'] for r in records if r['kind'] in MULTI)
        if dict(multi) != MULTI_PLAN:
            raise ValueError(f'Test {number}: multi-response spread {dict(multi)} != {MULTI_PLAN}')
        gaps = sum(1 for r in records if r['kind'] == 'S' and '____' in r['question'])
        if gaps < GAP_FILL_MIN:
            raise ValueError(f'Test {number}: expected at least {GAP_FILL_MIN} gap-fill (____) single-choice items, found {gaps}')
        for item in records:
            if item['task'] not in VALID_TASKS:
                raise ValueError(f'Unknown skill: {item["task"]}')
            n_answers = len(item['answers'])
            if item['kind'] == 'S' and (n_answers != 1 or len(item['distractors']) != 3):
                raise ValueError(f'{item["id"]}: single-choice needs 1 answer and 3 distractors')
            if item['kind'] == 'M2' and (n_answers != 2 or len(item['distractors']) != 3):
                raise ValueError(f'{item["id"]}: M2 needs 2 answers and 3 distractors')
            if item['kind'] not in ('S', 'M2'):
                raise ValueError(f'{item["id"]}: unsupported item kind {item["kind"]}')
            if len(item['keys']) != len(set(item['keys'])):
                raise ValueError(f'{item["id"]}: duplicate option key')
            for key in item['keys']:
                if key not in TERMS:
                    raise ValueError(f'Unknown term: {key}')
            stem_ok = item['question'].endswith('?') or item['question'].endswith('Select two.')
            if len(item['reason'].split()) < 6 or not stem_ok:
                raise ValueError(f'Missing rationale/question: {item["id"]}')
            if 'case study' in item['question'].casefold() or 'case study' in item['reason'].casefold():
                raise ValueError(f'{item["id"]}: this exam publishes no case-study component')
            if n_answers > 1:
                words = {2: 'two', 3: 'three'}[n_answers]
                if f'Select {words}' not in item['question']:
                    raise ValueError(f'{item["id"]}: multi-response must state "Select {words}"')
            norm = ''.join(c for c in item['question'].casefold() if c.isalnum())
            if norm in stems:
                raise ValueError(f'Duplicate question: {item["id"]}')
            stems.add(norm)
    if len(stems) != ITEM_TOTAL * len(BANK):
        raise ValueError(f'Expected {ITEM_TOTAL * len(BANK)} distinct stems, found {len(stems)}')
    items = [(r['id'], r['question']) for rs in BANK.values() for r in rs]
    bags = [(i, {w for w in re.findall(r'[a-z]+', q.casefold()) if len(w) > 3}) for i, q in items]
    for (id_a, a), (id_b, b) in combinations(bags, 2):
        if not a or not b:
            continue
        if len(a & b) / len(a | b) > NEAR_DUPLICATE_LIMIT:
            raise ValueError(f'Near-duplicate stems: {id_a} and {id_b}')


def main():
    check_source()
    manifest = {}
    for number in range(1, 7):
        rows, mapping = make_rows(number)
        folder = ROOT / '03-practice-sets' / f'set-{number}'
        folder.mkdir(parents=True, exist_ok=True)
        with (folder / f'practice-set-{number}.csv').open('w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=HEADER, lineterminator='\n', extrasaction='ignore')
            writer.writeheader()
            writer.writerows(rows)
        (folder / f'practice-set-{number}.md').write_text(render_test(number, rows), encoding='utf-8')
        (folder / 'README.md').write_text(render_set_readme(number, rows), encoding='utf-8')
        manifest[str(number)] = mapping
        print(f'Built set {number}: {len(rows)} questions')
    (ROOT / '04-resources/answer-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print('Wrote 04-resources/answer-manifest.json')


if __name__ == '__main__':
    main()
