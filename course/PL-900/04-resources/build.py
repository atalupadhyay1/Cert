#!/usr/bin/env python3
"""Export original Exam PL-900 mock-exam items; Python 3.10+, standard library only.

Microsoft's published PL-900 Fundamentals exam is 45 minutes (~40-60 standalone questions,
closed-book, no case studies, no live labs). This exporter builds six 100-question
blueprint-weighted practice sets with multiple-choice (including 4-step '->' sequences,
'____' formula/slot completions, and 'Proposed solution:' items) and multi-select items,
with zero case-study scaffolding.
"""
import csv
import json
import random
from collections import Counter
from pathlib import Path

from bank import (
    ALLOCATIONS,
    BANK,
    COMPLETION_FLOOR,
    CREDENTIAL_TITLE,
    DOMAINS,
    EXAM_CODE,
    EXAM_TITLE,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    OFFICIAL_RANGES,
    PROPOSED_SOL_FLOOR,
    SKILL_PLAN,
    SKILLS,
    STUDY_GUIDE_DATE,
    SUBTITLES,
    TERMS,
    TOPICS,
    TYPE_PLAN,
)
from sources import SKILL_SOURCES, STUDY_GUIDE_URL

ROOT = Path(__file__).resolve().parents[1]
HEADER = ['Question', 'Question Type']
for i in range(1, 7):
    HEADER += [f'Answer Option {i}', f'Explanation {i}']
HEADER += ['Correct Answers', 'Overall Explanation', 'Domain']

SEQUENCING = TYPE_PLAN['ordering']
EXPORT_PLAN = {
    'multiple-choice': TYPE_PLAN['multiple-choice'] + SEQUENCING,
    'multi-select': TYPE_PLAN['multi-select'],
}
ALLOWED_TYPES = ('multiple-choice', 'multi-select')


def _flat(text: str) -> str:
    return ' '.join(''.join(c for c in text.casefold() if c.isalnum() or c == ' ').split())


def _addition(meaning: str, reason: str) -> str:
    a, b = _flat(meaning), _flat(reason)
    if not a or a == b or a in b or b in a:
        return ''
    wa = {w for w in a.split() if len(w) > 3}
    wb = {w for w in b.split() if len(w) > 3}
    if wa and wb and len(wa & wb) / len(wa | wb) > 0.6:
        return ''
    return ' ' + meaning


def expected_type(record: dict) -> str:
    if record['kind'] in ('M2', 'M3'):
        return 'multi-select'
    return 'multiple-choice'


def make_rows(number: int):
    rng = random.Random(900000 + number)
    records = sorted(BANK[number], key=lambda r: (r['domain'], r['task'], r['id']))
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
        row['_stem'] = record['question']
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
            f' Local study-map skill {record["task"]} ({SKILLS[record["task"]]}), aligned to the official PL-900 study guide ({STUDY_GUIDE_URL}). '
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


def render_test(number: int, rows: list[dict]) -> str:
    lines = [
        f'# Microsoft Exam {EXAM_CODE}: {EXAM_TITLE} — {TOPICS[number]}',
        '',
        f'Exam {EXAM_CODE} ({SUBTITLES[number]}) · {len(rows)} questions · 75-minute recommended timing (45-minute speed drill) · Microsoft scaled passing score 700 / 1000',
        '',
        f'> **Blueprint & Fundamentals Exam Notice:** Aligned to the official **{STUDY_GUIDE_DATE}** Microsoft Learn {EXAM_CODE} study guide (`{CREDENTIAL_TITLE}` — Beginner / Fundamentals credential with **no prerequisite** and **lifetime validity / never expires**). The live {EXAM_CODE} exam provides **45 minutes** for **40–60 standalone questions** (`~45–67.5 sec/question`), is **closed-book** (Microsoft Learn split-screen access is **not** available on Fundamentals exams), and contains **no case studies and no live labs**. A 75-minute timer on this expanded 100-question set matches the live 45-second-per-question upper pace.',
        '',
        f'Blueprint-weighted mock exam: {EXPORT_PLAN["multiple-choice"]} `multiple-choice` items (including {SEQUENCING} four-step `→` sequence items, `____` Power Fx / UI / flow / agent completion items, and `Proposed solution:` evaluations) and {EXPORT_PLAN["multi-select"]} `multi-select` items (`Select two.` / `Select three.`).',
        '',
        'Original educational material authored from public Microsoft Learn documentation — not recalled, actual, or reproduced Microsoft exam items.',
        '',
        '## Questions',
        '',
    ]
    current_domain = None
    for idx, row in enumerate(rows, 1):
        rec_domain = next(d for d, label in DOMAINS.items() if label == row['Domain'])
        if rec_domain != current_domain:
            current_domain = rec_domain
            lo, hi = OFFICIAL_RANGES[rec_domain]
            lines += [
                '---',
                '',
                f'## Domain {rec_domain} — {DOMAINS[rec_domain]} ({lo}–{hi}% official weight · {ALLOCATIONS[number][rec_domain]} questions)',
                '',
            ]
        lines += [f'### {idx}. {row["_stem"]}', '']
        for opt_idx in range(1, 7):
            opt_val = row[f'Answer Option {opt_idx}']
            if opt_val:
                lines.append(f'- {chr(64 + opt_idx)}. {opt_val}')
        lines.append('')

    lines += ['---', '', '## Answer Key and Explanations', '']
    for idx, row in enumerate(rows, 1):
        letters = ', '.join(chr(64 + int(x)) for x in row['Correct Answers'].split(','))
        lines += [
            f'### Question {idx} — {letters} ({row["Domain"]})',
            '',
            row['Overall Explanation'],
            '',
        ]
        for opt_idx in range(1, 7):
            exp_val = row[f'Explanation {opt_idx}']
            if exp_val:
                lines.append(f'- **{chr(64 + opt_idx)}:** {exp_val}')
        lines.append('')
    return '\n'.join(lines)


def render_set_readme(number: int, rows: list[dict]) -> str:
    dom_counts = Counter(r['Domain'] for r in rows)
    type_counts = Counter(r['Question Type'] for r in rows)
    return '\n'.join([
        f'# Practice Set {number} — {TOPICS[number]}',
        '',
        f'**Theme:** {SUBTITLES[number]}',
        '',
        '## Files in This Folder',
        '',
        f'- `practice-set-{number}.csv` — 100-question Udemy bulk-upload CSV (UTF-8 with BOM, LF line endings, 17 columns).',
        f'- `practice-set-{number}.md` — Human-readable review copy with full per-option rationales and official Microsoft Learn links.',
        '',
        '## Recommended Udemy Practice-Test Settings',
        '',
        '- **Question count:** `100` (expanded comprehensive Fundamentals bank; no case studies on live PL-900)',
        '- **Recommended timer:** `75 minutes` (`45 sec/question`, matching the live 45-minute / 60-question pace; use `45 minutes` for a high-speed drill)',
        '- **Minimum Score to Pass (Udemy):** `75%` (practice benchmark only; live PL-900 uses a `700 / 1000` criterion-referenced scaled score)',
        '- **Randomize Question & Answer Order:** Enabled (every question is self-contained with zero case-study ordering dependencies)',
        '- **Open-book rule:** Take **closed-book** — Microsoft Learn split-screen access is **not** available on Microsoft Fundamentals exams',
        '',
        '## Domain Breakdown',
        '',
        '| Domain | Official Weight | Questions | Share |',
        '|---|---:|---:|---:|',
        f'| 1. {DOMAINS[1]} | 5–10% | {dom_counts[DOMAINS[1]]} | {dom_counts[DOMAINS[1]]}% |',
        f'| 2. {DOMAINS[2]} | 20–25% | {dom_counts[DOMAINS[2]]} | {dom_counts[DOMAINS[2]]}% |',
        f'| 3. {DOMAINS[3]} | 20–25% | {dom_counts[DOMAINS[3]]} | {dom_counts[DOMAINS[3]]}% |',
        f'| 4. {DOMAINS[4]} | 20–25% | {dom_counts[DOMAINS[4]]} | {dom_counts[DOMAINS[4]]}% |',
        f'| 5. {DOMAINS[5]} | 20–25% | {dom_counts[DOMAINS[5]]} | {dom_counts[DOMAINS[5]]}% |',
        f'| **Total** | **100%** | **{len(rows)}** | **100%** |',
        '',
        '## Format Mix',
        '',
        f'- `multiple-choice`: **{type_counts["multiple-choice"]}** (`{TYPE_PLAN["multiple-choice"]}` single-answer + `{SEQUENCING}` four-step `→` sequences)',
        f'- `multi-select`: **{type_counts["multi-select"]}** (`{KIND_PLAN["M2"]}` five-option `Select two.` + `{KIND_PLAN["M3"]}` six-option `Select three.`)',
        '',
    ])


def render_summary(manifest: dict) -> str:
    lines = [
        f'# {EXAM_CODE}: {EXAM_TITLE} — Bank Summary',
        '',
        f'- **Credential:** `{CREDENTIAL_TITLE}` (Beginner / Fundamentals — **never expires**, no prerequisite)',
        f'- **Official Study Guide Baseline:** `{STUDY_GUIDE_DATE}` ({STUDY_GUIDE_URL})',
        '- **Total Sets:** `6` (`100` questions each, **`600` unique questions**)',
        f'- **Per-Set Format Mix:** `{EXPORT_PLAN["multiple-choice"]}` `multiple-choice` (`{KIND_PLAN["S"]}` single-answer + `{KIND_PLAN["O"]}` ordered `→` sequences) + `{EXPORT_PLAN["multi-select"]}` `multi-select` (`{KIND_PLAN["M2"]}` `Select two.` + `{KIND_PLAN["M3"]}` `Select three.`)',
        f'- **Fundamentals Pattern Floors per Set:** `>= {COMPLETION_FLOOR}` formula/UI/flow/agent `____` completions, `>= {PROPOSED_SOL_FLOOR}` `Proposed solution:` evaluations, `0` case studies (matches live 45-minute Fundamentals format)',
        '',
        '## Per-Set Allocation',
        '',
        '| Set | Theme | D1 (5–10%) | D2 (20–25%) | D3 (20–25%) | D4 (20–25%) | D5 (20–25%) | Total |',
        '|---|---|---:|---:|---:|---:|---:|---:|',
    ]
    for n in range(1, 7):
        a = ALLOCATIONS[n]
        lines.append(f'| Set {n} | {SUBTITLES[n]} | {a[1]} | {a[2]} | {a[3]} | {a[4]} | {a[5]} | {sum(a.values())} |')
    lines += [
        f'| **6-Set Total** | **All 6 Full-Length Mock Exams** | **{6*ALLOCATIONS[1][1]}** | **{6*ALLOCATIONS[1][2]}** | **{6*ALLOCATIONS[1][3]}** | **{6*ALLOCATIONS[1][4]}** | **{6*ALLOCATIONS[1][5]}** | **600** |',
        '',
        '## 34-Skill Coverage Plan (Identical Across Every Set)',
        '',
        '| Skill | Description | Per Set | 6-Set Total |',
        '|---|---|---:|---:|',
    ]
    for skill, desc in SKILLS.items():
        cnt = SKILL_PLAN[skill]
        lines.append(f'| `{skill}` | {desc} | {cnt} | {cnt * 6} |')
    lines.append('')
    return '\n'.join(lines)


def write_csv(path: Path, rows: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, extrasaction='ignore', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    manifest = {}
    for n in range(1, 7):
        if len(BANK[n]) != ITEM_TOTAL:
            raise SystemExit(f'Set {n} has {len(BANK[n])} items; expected {ITEM_TOTAL}')
        rows, mapping = make_rows(n)
        manifest[str(n)] = mapping
        set_dir = ROOT / f'03-practice-sets/set-{n}'
        write_csv(set_dir / f'practice-set-{n}.csv', rows)
        (set_dir / f'practice-set-{n}.md').write_text(render_test(n, rows), encoding='utf-8')
        (set_dir / 'README.md').write_text(render_set_readme(n, rows), encoding='utf-8')
        print(f'Built Set {n}: {len(rows)} rows -> {set_dir.relative_to(ROOT)}')

    res_dir = ROOT / '04-resources'
    (res_dir / 'answer-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    (res_dir / 'SUMMARY.md').write_text(render_summary(manifest), encoding='utf-8')
    print('Wrote 04-resources/answer-manifest.json and 04-resources/SUMMARY.md')


if __name__ == '__main__':
    main()
