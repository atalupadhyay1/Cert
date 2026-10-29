#!/usr/bin/env python3
"""Export original Claude Certified Architect – Professional (CCAR-P) mock-exam items; Python 3.10+, stdlib only.

Anthropic's CCAR-P Exam Guide (Version 1.0, Effective July 2026) publishes 63
scored multiple-choice and multiple-response items in 120 minutes across seven
domains (17 / 13 / 19 / 16 / 14 / 14 / 7 = 100%) and has no split-screen
case-study component. Each mock exam exports 48 four-option multiple-choice
items, 12 five-option Select-two items, and 3 six-option Select-three items
(63 items total, allocated 11 / 8 / 12 / 10 / 9 / 9 / 4 across Domains 1-7).
"""
import csv
import json
import random
import re
from collections import Counter
from itertools import combinations
from pathlib import Path

from bank import (ALLOCATIONS, BANK, DOMAIN_NOTES, DOMAINS, ITEM_TOTAL,
                  KIND_PLAN, MULTI_PLAN, OFFICIAL_WEIGHTS,
                  PATTERN_MATRIX_FLOOR, SKILL_PLAN, SKILLS, SUBTITLES, TERMS,
                  TOPICS, TYPE_PLAN, VALID_TASKS, is_matrix_adapted_stem)
from sources import DOCS, GUIDE

COURSE = 'Claude Certified Architect – Professional (CCAR-P)'
ROOT = Path(__file__).resolve().parents[1]
HEADER = ['Question', 'Question Type']
for i in range(1, 7):
    HEADER += [f'Answer Option {i}', f'Explanation {i}']
HEADER += ['Correct Answers', 'Overall Explanation', 'Domain']

EXPORT_PLAN = dict(TYPE_PLAN)
NEAR_DUPLICATE_LIMIT = 0.72
ALLOWED_TYPES = ('multiple-choice', 'multi-select')
MULTI = ('M2', 'M3')
BANNED_PHRASES = ('case study', 'click ', 'navigate to', 'in the console, select')


def _flat(text):
    return ' '.join(''.join(c for c in text.casefold() if c.isalnum() or c == ' ').split())


def _addition(meaning, reason):
    """Return the meaning only when it adds detail beyond the per-question reason."""
    a, b = _flat(meaning), _flat(reason)
    if not a or a == b or a in b or b in a:
        return ''
    wa = {w for w in a.split() if len(w) > 3}
    wb = {w for w in b.split() if len(w) > 3}
    if wa and wb and len(wa & wb) / len(wa | wb) > 0.6:
        return ''
    return ' ' + meaning


def expected_type(record):
    return 'multi-select' if record['kind'] in MULTI else 'multiple-choice'


def make_rows(number):
    rng = random.Random(630000 + number)
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
                row[f'Explanation {i}'] = f'Correct.{_addition(meaning, record["reason"])} In this scenario: {record["reason"]}'
            else:
                row[f'Explanation {i}'] = f'Incorrect for this scenario. {meaning} Why the keyed choice wins: {record["reason"]}'
        correct_idx = [i for i, key in enumerate(opts, 1) if key in record['answers']]
        row['Correct Answers'] = ','.join(map(str, correct_idx))
        answer_labels = '; '.join(TERMS[k][0] for k in record['answers'])
        row['Overall Explanation'] = (
            f'Answer{"s" if len(record["answers"]) > 1 else ""}: {answer_labels}. {record["reason"]} '
            + ''.join(_addition(TERMS[k][1], record['reason']) for k in record['answers'])
            + f' Local study-map skill {record["task"]} ({SKILLS[record["task"]]}), mapped to the official CCAR-P Exam Guide (v1.0): {GUIDE}. '
            f'Primary Anthropic documentation: {DOCS[record["domain"]]}.'
        )
        row['Overall Explanation'] = ' '.join(row['Overall Explanation'].split())
        row['Domain'] = DOMAINS[record['domain']]
        rows.append(row)
        mapping.append(dict(
            question=len(rows),
            id=record['id'],
            topic=TOPICS[number],
            domain=record['domain'],
            task=record['task'],
            kind=record['kind'],
            correct_terms=list(record['answers']),
            option_terms=opts,
            correct_indices=correct_idx,
        ))
    return rows, mapping


def render_test(number, rows):
    lines = [
        f'# {COURSE} — {TOPICS[number]}',
        '',
        f'CCAR-P · {len(rows)} questions · 120-minute live exam length (~114 seconds/item) · scaled passing score 720 on 100–1,000',
        '',
        f'Blueprint-weighted mock exam matching the official 63-item paper (11 / 8 / 12 / 10 / 9 / 9 / 4 across Domains 1–7). '
        f'Item mix: {EXPORT_PLAN["multiple-choice"]} four-option multiple-choice items and {EXPORT_PLAN["multi-select"]} '
        f'multiple-response items ({KIND_PLAN["M2"]} five-option Select-two and {KIND_PLAN["M3"]} six-option Select-three items). '
        'Interactive Pearson VUE Hotspot / matrix grids cannot render natively in Udemy CSV imports, so candidate use-case suitability, '
        'sound architectural practice review, and Pre-Processing / Model Stage / Post-Processing execution-layer classification are '
        'tested through structured multiple-choice and multi-select scenarios. No multi-question split-screen block is included because '
        'CCAR-P publishes 63 standalone items.',
        '',
        'Original educational content authored from official Anthropic documentation — not actual, recalled, or copied Anthropic exam items.',
        '',
        '## Questions',
        '',
    ]
    domain = None
    for n, row in enumerate(rows, 1):
        record_domain = next(d for d, label in DOMAINS.items() if label == row['Domain'])
        if record_domain != domain:
            domain = record_domain
            lines += ['---', '', f'## Domain {domain} — {DOMAINS[domain]} ({DOMAIN_NOTES[domain]})', '']
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
    adapted = sum(1 for row in rows if is_matrix_adapted_stem(row['Question']))
    return (
        f'# {TOPICS[number]}: {SUBTITLES[number]}\n\n'
        f'{len(rows)} original items · 120 minutes (~114 s/item) · matches live CCAR-P length · blueprint-weighted.\n\n'
        '| Official domain | Blueprint weight | Exact share (×63) | Questions |\n|---|---:|---:|---:|\n'
        + '\n'.join(
            f'| {DOMAINS[d]} | {int(OFFICIAL_WEIGHTS[d])}% | {OFFICIAL_WEIGHTS[d] * ITEM_TOTAL / 100:.2f} | {counts[DOMAINS[d]]} |'
            for d in DOMAINS
        )
        + f'\n\nItem mix: {types["multiple-choice"]} four-option multiple-choice and {types["multi-select"]} multiple-response '
        f'({KIND_PLAN["M2"]} five-option `Select two.` and {KIND_PLAN["M3"]} six-option `Select three.` items), including '
        f'{adapted} structured suitability / sound-practice / execution-layer categorization scenarios adapting interactive '
        'matrix patterns to Udemy CSV. CCAR-P publishes 63 standalone items in 120 minutes with no split-screen multi-question block.\n\n'
        f'Upload `practice-set-{number}.csv` (configure 120 minutes in Udemy); use `practice-set-{number}.md` for offline review.\n\n'
        'Anthropic reports CCAR-P on a 100–1,000 scaled score (cut score 720); practice percentages are raw scores, not scaled conversions.\n'
    )


def check_source():
    stems = set()
    if {r['task'] for rs in BANK.values() for r in rs} != VALID_TASKS:
        missing = sorted(VALID_TASKS - {r['task'] for rs in BANK.values() for r in rs})
        raise ValueError(f'Source must cover every local study-map skill; missing {missing}')
    for number, records in BANK.items():
        if len(records) != ITEM_TOTAL:
            raise ValueError(f'Test {number}: expected {ITEM_TOTAL} authored items, found {len(records)}')
        if Counter(r['domain'] for r in records) != Counter(ALLOCATIONS[number]):
            raise ValueError(f'Test {number}: wrong domain allocation {Counter(r["domain"] for r in records)}')
        skills = Counter(r['task'] for r in records)
        if dict(skills) != {k: v for k, v in SKILL_PLAN.items() if v}:
            diff = {
                k: (skills.get(k, 0), SKILL_PLAN.get(k, 0))
                for k in sorted(set(skills) | set(SKILL_PLAN))
                if skills.get(k, 0) != SKILL_PLAN.get(k, 0)
            }
            raise ValueError(f'Test {number}: per-skill counts differ from SKILL_PLAN: {diff}')
        raw_kinds = Counter(r['kind'] for r in records)
        if dict(raw_kinds) != KIND_PLAN:
            raise ValueError(f'Test {number}: kind mix {dict(raw_kinds)} != {KIND_PLAN}')
        kinds = Counter(expected_type(r) for r in records)
        if kinds != Counter(TYPE_PLAN):
            raise ValueError(f'Test {number}: wrong item-type mix {kinds}')
        multi = Counter(r['domain'] for r in records if r['kind'] in MULTI)
        if dict(multi) != MULTI_PLAN:
            raise ValueError(f'Test {number}: multi-select spread {dict(multi)} != {MULTI_PLAN}')
        matrix_count = sum(1 for r in records if is_matrix_adapted_stem(r['question']))
        if matrix_count < PATTERN_MATRIX_FLOOR:
            raise ValueError(
                f'Test {number}: expected >= {PATTERN_MATRIX_FLOOR} matrix/categorization-adapted items, found {matrix_count}'
            )
        stage_items = sum(
            1 for r in records
            if 'pre-processing' in r['question'].casefold()
            and 'model stage' in r['question'].casefold()
            and 'post-processing' in r['question'].casefold()
        )
        suitability_items = sum(
            1 for r in records
            if 'candidate use cases' in r['question'].casefold() or 'candidate workflows' in r['question'].casefold()
        )
        practice_items = sum(1 for r in records if 'sound architectural practice' in r['question'].casefold())
        if stage_items < 2 or suitability_items < 2 or practice_items < 2:
            raise ValueError(
                f'Test {number}: need >=2 each of stage-mapping ({stage_items}), suitability ({suitability_items}), '
                f'and sound-practice ({practice_items}) items'
            )
        for item in records:
            if item['task'] not in VALID_TASKS:
                raise ValueError(f'Unknown skill: {item["task"]}')
            n_answers = len(item['answers'])
            if item['kind'] == 'S' and (n_answers != 1 or len(item['distractors']) != 3):
                raise ValueError(f'{item["id"]}: S needs 1 answer and 3 distractors')
            if item['kind'] == 'M2' and (n_answers != 2 or len(item['distractors']) != 3):
                raise ValueError(f'{item["id"]}: M2 needs 2 answers and 3 distractors')
            if item['kind'] == 'M3' and (n_answers != 3 or len(item['distractors']) != 3):
                raise ValueError(f'{item["id"]}: M3 needs 3 answers and 3 distractors')
            if item['kind'] not in ('S', 'M2', 'M3'):
                raise ValueError(f'{item["id"]}: unsupported item kind {item["kind"]}')
            if len(item['keys']) != len(set(item['keys'])):
                raise ValueError(f'{item["id"]}: duplicate option key')
            for key in item['keys']:
                if key not in TERMS:
                    raise ValueError(f'{item["id"]}: unknown term {key}')
                if '→' in TERMS[key][0]:
                    raise ValueError(f'{item["id"]}: arrow glyph not permitted in option label {key}')
            if len({TERMS[k][0].casefold() for k in item['keys']}) != len(item['keys']):
                raise ValueError(f'{item["id"]}: case-insensitive duplicate option label')
            if item['kind'] == 'S':
                stem_ok = item['question'].endswith('?')
            elif item['kind'] == 'M2':
                stem_ok = item['question'].endswith('Select two.')
            else:
                stem_ok = item['question'].endswith('Select three.')
            if len(item['reason'].split()) < 10 or not stem_ok:
                raise ValueError(f'Invalid stem ending or short rationale: {item["id"]}')
            low_q = item['question'].casefold()
            low_r = item['reason'].casefold()
            for phrase in BANNED_PHRASES:
                if phrase in low_q or phrase in low_r:
                    raise ValueError(f'{item["id"]}: banned phrase {phrase!r}')
            norm = ''.join(c for c in low_q if c.isalnum())
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
        score = len(a & b) / len(a | b)
        if score > NEAR_DUPLICATE_LIMIT:
            raise ValueError(f'Near-duplicate stems ({score:.3f}): {id_a} and {id_b}')


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
