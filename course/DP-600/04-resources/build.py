#!/usr/bin/env python3
"""Export original Exam DP-600 mock-exam items; Python 3.10+, standard library only."""
import csv
import json
import random
from collections import Counter
from pathlib import Path

from bank import (
    ALLOCATIONS,
    BANK,
    CASE_SIZE,
    CASE_STUDIES,
    CODE_FILL_FLOOR,
    DOMAINS,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    PROPOSED_SOL_FLOOR,
    SKILL_PLAN,
    SKILLS,
    SUBTITLES,
    TERMS,
    TOPICS,
    TYPE_PLAN,
    VALID_TASKS,
)
from cases import CASES
from sources import SKILL_SOURCES, STUDY_GUIDE_URL

ROOT = Path(__file__).resolve().parents[1]
HEADER = ['Question', 'Question Type']
for i in range(1, 7):
    HEADER += [f'Answer Option {i}', f'Explanation {i}']
HEADER += ['Correct Answers', 'Overall Explanation', 'Domain']

CASE_TAG = 'Case study — '
SEQUENCING = TYPE_PLAN['ordering']
EXPORT_PLAN = {
    'multiple-choice': TYPE_PLAN['multiple-choice'] + SEQUENCING,
    'multi-select': TYPE_PLAN['multi-select'],
}
ALLOWED_TYPES = ('multiple-choice', 'multi-select')


def case_name(text):
    if text.startswith(CASE_TAG):
        return text[len(CASE_TAG):].split(':')[0].strip()
    return ''


def _flat(text):
    return ' '.join(''.join(c for c in text.casefold() if c.isalnum() or c == ' ').split())


def _addition(meaning, reason):
    """Return the meaning only when it adds distinct information beyond reason."""
    a, b = _flat(meaning), _flat(reason)
    if not a or a == b or a in b or b in a:
        return ''
    wa = {w for w in a.split() if len(w) > 3}
    wb = {w for w in b.split() if len(w) > 3}
    if wa and wb and len(wa & wb) / len(wa | wb) > 0.6:
        return ''
    return ' ' + meaning


def expected_type(record):
    if record['kind'] in ('M2', 'M3'):
        return 'multi-select'
    return 'multiple-choice'


def make_rows(number):
    rng = random.Random(600000 + number)
    records = sorted(BANK[number], key=lambda r: (case_name(r['question']) != '', case_name(r['question'])))
    singles = [r for r in records if r['kind'] in ('S', 'O')]
    positions = [i % 4 for i in range(len(singles))]
    rng.shuffle(positions)
    rows, mapping = [], []
    for record in records:
        opts = list(record['answers']) + list(record['distractors'])
        if record['kind'] in ('S', 'O'):
            correct = record['answers'][0]
            rest = [k for k in opts if k != correct]
            rng.shuffle(rest)
            rest.insert(positions.pop(), correct)
            opts = rest
        else:
            rng.shuffle(opts)
        row = dict.fromkeys(HEADER, '')
        case = case_name(record['question'])
        stem = record['question'][len(CASE_TAG) + len(case) + 2:] if case else record['question']
        row['_case'] = case
        row['_stem'] = stem
        row['Question'] = record['question']
        row['Question Type'] = expected_type(record)
        for i, key in enumerate(opts, 1):
            label, meaning = TERMS[key]
            row[f'Answer Option {i}'] = label
            if key in record['answers']:
                row[f'Explanation {i}'] = f'Correct.{_addition(meaning, record["reason"])} In this scenario: {record["reason"]}'
            else:
                row[f'Explanation {i}'] = f'Incorrect for this requirement. {meaning} Why the keyed choice wins: {record["reason"]}'
        correct_idx = [i for i, key in enumerate(opts, 1) if key in record['answers']]
        row['Correct Answers'] = ','.join(map(str, correct_idx))
        answer_labels = '; '.join(TERMS[k][0] for k in record['answers'])
        extra_detail = _addition(TERMS[record['answers'][0]][1], record['reason']) if len(record['answers']) == 1 else ''
        ref_title, ref_url = SKILL_SOURCES[record['task']]
        row['Overall Explanation'] = (
            f'Answer{"" if len(record["answers"]) == 1 else "s"}: {answer_labels}. {record["reason"]}{extra_detail}'
            f' Local study-map skill {record["task"]} ({SKILLS[record["task"]]}), aligned to the official DP-600 study guide ({STUDY_GUIDE_URL}). '
            f'Primary reference: {ref_title} ({ref_url}).'
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
        f'# Microsoft Exam DP-600: Implementing Analytics Solutions Using Microsoft Fabric — {TOPICS[number]}',
        '',
        f'Exam DP-600 ({SUBTITLES[number]}) · {len(rows)} questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000',
        '',
        '> **Blueprint & Credential Notice:** Aligned to the official **October 19, 2026** DP-600 study guide (`Microsoft Certified: Fabric Analytics Engineer Associate`). Associate-level certification with **no prerequisite exam required**, free online annual renewal on Microsoft Learn, split-screen `learn.microsoft.com` access during non-lab exam sections, and hands-on coverage across **SQL**, **KQL**, **DAX**, **PySpark**, **Power Query M**, **TMDL**, and **TMSL**.',
        '',
        f'Blueprint-weighted mock exam: {EXPORT_PLAN["multiple-choice"]} `multiple-choice` items (including {SEQUENCING} four-step `→` sequence items, `____` SQL/KQL/DAX/PySpark/M/TMDL/TMSL completion items, and `Proposed solution:` evaluations), {EXPORT_PLAN["multi-select"]} `multi-select` items (`Select two.` / `Select three.`), and {CASE_STUDIES} original 3-question enterprise Microsoft Fabric case studies ({CASE_STUDIES * CASE_SIZE} case items).',
        '',
        'Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area SQL/KQL/DAX/TMDL dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).',
        '',
        '100% original educational content authored from official Microsoft Learn Fabric and Power BI documentation — never recalled live items or copied Microsoft sample case studies.',
        '',
        '## Questions',
        '',
    ]
    seen = None
    for n, row in enumerate(rows, 1):
        case = row['_case']
        if case and case != seen:
            lines += [
                '---',
                '',
                f'## Case study — {case}',
                '',
                CASES[case],
                '',
                f'The next {CASE_SIZE} questions refer to **{case}**. Read the scenario brief once, then answer each item independently.',
                '',
            ]
        seen = case or None
        lines += [f'### {n}. {row["_stem"]}', '', f'Domain: {row["Domain"]}', '']
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


def render_case_brief():
    """Single Markdown reference compiling all 24 original DP-600 case-study briefs."""
    lines = [
        '# Exam DP-600 Case Study Briefs (Sets 1–6)',
        '',
        f'Every mock exam contains {CASE_STUDIES} original Microsoft Fabric Analytics Engineering case studies of {CASE_SIZE} questions ({CASE_STUDIES * CASE_SIZE} items per set, 24 scenarios total). '
        'Paste the relevant scenario into a Udemy practice-test description if uploading `practice-set-N.csv`, or upload `case-embedded-set-N.csv` where each case stem embeds the full scenario directly.',
        '',
    ]
    for number in range(1, 7):
        rows, _ = make_rows(number)
        cases = [r['_case'] for r in rows if r['_case']]
        lines += [f'## Exam {number}: {SUBTITLES[number]}', '']
        for case in dict.fromkeys(cases):
            lines += [f'### Case study — {case}', '', CASES[case], '', 'Questions in this block:', '']
            n = 0
            for row in rows:
                if row['_case'] != case:
                    continue
                n += 1
                letters = ', '.join(chr(64 + int(x)) for x in row['Correct Answers'].split(','))
                lines.append(f'{n}. {row["_stem"]} _({letters})_')
            lines.append('')
    return '\n'.join(lines)


def render_case_embedded(rows):
    """Self-contained CSV variant repeating the scenario brief inside every case-item stem."""
    embedded = []
    for row in rows:
        row = dict(row)
        if row['_case']:
            c = row['_case']
            row['Question'] = f'Case study — {c}: {CASES[c]} {row["_stem"]}'
        embedded.append(row)
    return embedded


def check_source():
    stems = set()
    if {r['task'] for rs in BANK.values() for r in rs} != VALID_TASKS:
        raise ValueError('Source must cover every local study-map skill')
    for number, records in BANK.items():
        if len(records) != ITEM_TOTAL:
            raise ValueError(f'Test {number}: expected {ITEM_TOTAL} authored items, found {len(records)}')
        if Counter(r['domain'] for r in records) != Counter(ALLOCATIONS[number]):
            raise ValueError(f'Test {number}: wrong domain allocation {Counter(r["domain"] for r in records)}')
        if Counter(r['task'] for r in records) != Counter(SKILL_PLAN):
            diff = {k: (Counter(r['task'] for r in records)[k], SKILL_PLAN[k])
                    for k in VALID_TASKS if Counter(r['task'] for r in records)[k] != SKILL_PLAN[k]}
            raise ValueError(f'Test {number}: skill plan mismatch {diff}')
        if Counter(r['kind'] for r in records) != Counter(KIND_PLAN):
            raise ValueError(f'Test {number}: kind plan mismatch {Counter(r["kind"] for r in records)}')
        ms_by_domain = Counter(r['domain'] for r in records if r['kind'] in ('M2', 'M3'))
        if ms_by_domain != Counter(MULTI_PLAN):
            raise ValueError(f'Test {number}: multi-select domain spread mismatch {ms_by_domain}')
        code_fills = sum(1 for r in records if '____' in r['question'])
        if code_fills < CODE_FILL_FLOOR:
            raise ValueError(f'Test {number}: expected >= {CODE_FILL_FLOOR} ____ completion items, found {code_fills}')
        proposed = sum(1 for r in records if 'Proposed solution:' in r['question'])
        if proposed < PROPOSED_SOL_FLOOR:
            raise ValueError(f'Test {number}: expected >= {PROPOSED_SOL_FLOOR} Proposed solution: items, found {proposed}')
        cases = Counter(case_name(r['question']) for r in records if case_name(r['question']))
        if len(cases) != CASE_STUDIES or set(cases.values()) != {CASE_SIZE}:
            raise ValueError(f'Test {number}: expected {CASE_STUDIES} case studies of {CASE_SIZE} questions, found {dict(cases)}')
        for item in records:
            if item['task'] not in VALID_TASKS:
                raise ValueError(f'Unknown skill: {item["task"]}')
            n_answers = len(item['answers'])
            if item['kind'] == 'S' and (n_answers != 1 or len(item['distractors']) != 3):
                raise ValueError(f'{item["id"]}: single-choice needs 1 answer and 3 distractors')
            if item['kind'] == 'M2' and (n_answers != 2 or len(item['distractors']) != 3):
                raise ValueError(f'{item["id"]}: M2 needs 2 answers and 3 distractors')
            if item['kind'] == 'M3' and (n_answers != 3 or len(item['distractors']) != 3):
                raise ValueError(f'{item["id"]}: M3 needs 3 answers and 3 distractors')
            if item['kind'] == 'O' and (n_answers != 1 or len(item['distractors']) != 3):
                raise ValueError(f'{item["id"]}: ordering needs 1 correct sequence and 3 alternatives')
            if len(item['keys']) != len(set(item['keys'])):
                raise ValueError(f'{item["id"]}: duplicate option key')
            for key in item['keys']:
                if key not in TERMS:
                    raise ValueError(f'{item["id"]}: unknown term {key}')
            if item['kind'] == 'O' and not all('→' in TERMS[k][0] for k in item['keys']):
                raise ValueError(f'{item["id"]}: ordering options must all contain →')
            if item['kind'] != 'O' and any('→' in TERMS[k][0] for k in item['keys']):
                raise ValueError(f'{item["id"]}: non-ordering item uses sequence option')
            stem_ok = (
                item['question'].endswith('?')
                or item['question'].endswith('Select two.')
                or item['question'].endswith('Select three.')
            )
            if len(item['reason'].split()) < 8 or not stem_ok:
                raise ValueError(f'Missing rationale or malformed question ending: {item["id"]}')
            if n_answers > 1:
                words = {2: 'two', 3: 'three'}[n_answers]
                if f'Select {words}.' not in item['question']:
                    raise ValueError(f'{item["id"]}: multi-select must state "Select {words}."')
            norm = ''.join(c for c in item['question'].casefold() if c.isalnum())
            if norm in stems:
                raise ValueError(f'Duplicate question: {item["id"]}')
            stems.add(norm)
    names = {case_name(r['question']) for rs in BANK.values() for r in rs if case_name(r['question'])}
    if names != set(CASES):
        raise ValueError(f'Case-study scenarios do not match CASES: {sorted(names ^ set(CASES))}')
    if len(stems) != ITEM_TOTAL * len(BANK):
        raise ValueError(f'Expected {ITEM_TOTAL * len(BANK)} distinct stems, found {len(stems)}')


def main():
    check_source()
    manifest = {}
    for number in range(1, 7):
        rows, mapping = make_rows(number)
        folder = ROOT / '03-practice-sets' / f'set-{number}'
        folder.mkdir(parents=True, exist_ok=True)
        csv_path = folder / f'practice-set-{number}.csv'
        with csv_path.open('w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=HEADER, lineterminator='\n', extrasaction='ignore')
            writer.writeheader()
            writer.writerows(rows)

        embedded = render_case_embedded(rows)
        emb_path = folder / f'case-embedded-set-{number}.csv'
        with emb_path.open('w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=HEADER, lineterminator='\n', extrasaction='ignore')
            writer.writeheader()
            for row in embedded:
                writer.writerow({k: row.get(k, '') for k in HEADER})

        (folder / f'practice-set-{number}.md').write_text(render_test(number, rows), encoding='utf-8')
        counts = Counter(row['Domain'] for row in rows)
        types = Counter(row['Question Type'] for row in rows)
        code_fills = sum(1 for r in rows if '____' in r['Question'])
        proposed = sum(1 for r in rows if 'Proposed solution:' in r['Question'])
        longest_emb = max(len(r['Question']) for r in embedded)
        (folder / 'README.md').write_text(
            f'# {TOPICS[number]}: {SUBTITLES[number]}\n\n'
            f'{len(rows)} original items · 100-minute recommended timing · Microsoft scaled passing score `700 / 1000` · October 19, 2026 DP-600 blueprint.\n\n'
            '> **Credential & Blueprint Notice:** Aligned to the official **October 19, 2026** Microsoft Learn study guide for `Microsoft Certified: Fabric Analytics Engineer Associate` (`Exam DP-600`). Associate-level credential with **no prerequisite exam required**, annual free online renewal, and practical coverage across **SQL**, **KQL**, **DAX**, **PySpark**, **Power Query M**, **TMDL**, and **TMSL**.\n\n'
            '| Official DP-600 Functional Group | Published Weight | Questions |\n|---|---:|---:|\n'
            f'| {DOMAINS[1]} | 25–30% | {counts[DOMAINS[1]]} |\n'
            f'| {DOMAINS[2]} | 45–50% | {counts[DOMAINS[2]]} |\n'
            f'| {DOMAINS[3]} | 25–30% | {counts[DOMAINS[3]]} |\n\n'
            f'## Item-Type & Pattern Mix\n\n'
            f'- `{types["multiple-choice"]}` `multiple-choice` items (`76` single-answer scenarios + `{SEQUENCING}` four-step `→` ordered sequence items), including `{code_fills}` `____` SQL/KQL/DAX/PySpark/M/TMDL/TMSL completion items and `{proposed}` `Proposed solution:` evaluations.\n'
            f'- `{types["multi-select"]}` `multi-select` items (`13` five-option `Select two.` + `3` six-option `Select three.`).\n'
            f'- `{CASE_STUDIES}` original enterprise Microsoft Fabric case studies × `{CASE_SIZE}` questions = `{CASE_STUDIES * CASE_SIZE}` case items.\n\n'
            f'## Upload Choice\n\n'
            f'- **`case-embedded-set-{number}.csv` (recommended for randomized Udemy tests):** embeds the full scenario inside each case question (longest stem `{longest_emb}` chars) so question shuffling never orphans context.\n'
            f'- **`practice-set-{number}.csv`:** compact case stems (`Case study — <Name>: ...`) for sequential review alongside `04-resources/case-studies.md`.\n'
            f'- **`practice-set-{number}.md`:** full human-readable study key with rationales and Microsoft Learn references.\n\n'
            'Microsoft reports DP-600 on a `100–1000` scaled score (`700` to pass), which does not equal `70%` raw accuracy.\n',
            encoding='utf-8',
        )
        manifest[str(number)] = mapping
        print(f'Built set {number}: {len(rows)} questions (longest embedded stem {longest_emb} chars)')

    # Also build 05-sample-upload/case-study-sample.csv from Exam 1's 12 case items
    sample_folder = ROOT / '05-sample-upload'
    sample_folder.mkdir(parents=True, exist_ok=True)
    rows_1, _ = make_rows(1)
    emb_1 = [r for r in render_case_embedded(rows_1) if r['_case']]
    with (sample_folder / 'case-study-sample.csv').open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, lineterminator='\n', extrasaction='ignore')
        writer.writeheader()
        for row in emb_1:
            writer.writerow({k: row.get(k, '') for k in HEADER})

    (ROOT / '04-resources/answer-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    (ROOT / '04-resources/case-studies.md').write_text(render_case_brief(), encoding='utf-8')
    print('Wrote 04-resources/answer-manifest.json, 04-resources/case-studies.md, and 05-sample-upload/case-study-sample.csv')


if __name__ == '__main__':
    main()
