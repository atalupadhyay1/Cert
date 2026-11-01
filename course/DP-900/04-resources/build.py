#!/usr/bin/env python3
"""Deterministic Udemy CSV, Markdown review key, and manifest exporter for Microsoft Exam DP-900.

Microsoft's published DP-900 Fundamentals exam is 45 minutes (~40-60 standalone questions,
closed-book, no case studies, no live labs). This exporter builds six 100-question
blueprint-weighted practice sets (UTF-8 BOM, LF, 17 columns) with multiple-choice
(including 4-step '→' sequences, '____' SQL/concept completions, and 'Proposed solution:'
evaluations) and multi-select items, with zero artificial case-study scaffolding.
"""
import csv
import hashlib
import json
import random
from collections import Counter
from pathlib import Path

from bank import (
    ALLOCATIONS,
    BANK,
    CREDENTIAL_TITLE,
    DOMAINS,
    EXAM_CODE,
    EXAM_TITLE,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    OFFICIAL_RANGES,
    SKILLS,
    SKILL_PLAN,
    SKILL_SOURCES,
    STUDY_GUIDE_DATE,
    STUDY_GUIDE_URL,
    SUBTITLES,
    TERMS,
    TOPICS,
    TYPE_PLAN,
)

ROOT = Path(__file__).resolve().parents[1]
SETS_DIR = ROOT / '03-practice-sets'
RES_DIR = ROOT / '04-resources'

HEADER = ['Question', 'Question Type']
for _i in range(1, 7):
    HEADER += [f'Answer Option {_i}', f'Explanation {_i}']
HEADER += ['Correct Answers', 'Overall Explanation', 'Domain']

SEQUENCING = TYPE_PLAN['ordering']
EXPORT_PLAN = {
    'multiple-choice': TYPE_PLAN['multiple-choice'] + SEQUENCING,
    'multi-select': TYPE_PLAN['multi-select'],
}
ALLOWED_TYPES = ('multiple-choice', 'multi-select')


def _rng(tag: str) -> random.Random:
    seed = int(hashlib.sha256(tag.encode('utf-8')).hexdigest()[:16], 16)
    return random.Random(seed)


def _check_blueprint(set_num: int, items: list[dict]) -> None:
    if len(items) != ITEM_TOTAL:
        raise AssertionError(f'Set {set_num}: expected {ITEM_TOTAL} items, got {len(items)}')
    kinds = Counter(it['kind'] for it in items)
    if dict(kinds) != KIND_PLAN:
        raise AssertionError(f'Set {set_num}: kind distribution {dict(kinds)} != {KIND_PLAN}')
    doms = Counter(it['domain'] for it in items)
    if dict(doms) != ALLOCATIONS[set_num]:
        raise AssertionError(f'Set {set_num}: domain split {dict(doms)} != {ALLOCATIONS[set_num]}')
    ms_doms = Counter(it['domain'] for it in items if it['kind'] in ('M2', 'M3'))
    if dict(ms_doms) != MULTI_PLAN:
        raise AssertionError(f'Set {set_num}: multi-select domain split {dict(ms_doms)} != {MULTI_PLAN}')
    skills = Counter(it['task'] for it in items)
    if dict(skills) != SKILL_PLAN:
        diff = {
            k: (skills.get(k, 0), SKILL_PLAN.get(k, 0))
            for k in set(skills) | set(SKILL_PLAN)
            if skills.get(k, 0) != SKILL_PLAN.get(k, 0)
        }
        raise AssertionError(f'Set {set_num}: skill counts mismatch: {diff}')


def _render_set(set_num: int, raw_items: list[dict]) -> tuple[list[dict], list[dict]]:
    _check_blueprint(set_num, raw_items)
    records = sorted(raw_items, key=lambda r: (r['domain'], [int(x) for x in r['task'].split('.')], r['id']))

    singles = [r for r in records if r['kind'] in ('S', 'O')]
    assert len(singles) == 84
    slots = [1] * 21 + [2] * 21 + [3] * 21 + [4] * 21
    _rng(f'{EXAM_CODE}:slots:{set_num}').shuffle(slots)
    slot_map = {r['id']: slot for r, slot in zip(singles, slots)}

    rows, manifest = [], []
    for q_idx, rec in enumerate(records, start=1):
        qid = rec['id']
        kind = rec['kind']
        answers = list(rec['answers'])
        distractors = list(rec['distractors'])
        keys = answers + distractors

        if kind == 'S':
            if len(answers) != 1 or len(keys) != 4 or any(k.startswith('seq_') for k in keys):
                raise AssertionError(f'{qid}: invalid S keys {keys}')
            qtype = 'multiple-choice'
        elif kind == 'O':
            if len(answers) != 1 or len(keys) != 4 or not all(k.startswith('seq_') for k in keys):
                raise AssertionError(f'{qid}: invalid O keys {keys}')
            qtype = 'multiple-choice'
        elif kind == 'M2':
            if len(answers) != 2 or len(keys) not in (5, 6) or any(k.startswith('seq_') for k in keys):
                raise AssertionError(f'{qid}: invalid M2 keys {keys}')
            if 'Select two.' not in rec['question']:
                raise AssertionError(f'{qid}: M2 stem must contain "Select two."')
            qtype = 'multi-select'
        elif kind == 'M3':
            if len(answers) != 3 or len(keys) != 6 or any(k.startswith('seq_') for k in keys):
                raise AssertionError(f'{qid}: invalid M3 keys {keys}')
            if 'Select three.' not in rec['question']:
                raise AssertionError(f'{qid}: M3 stem must contain "Select three."')
            qtype = 'multi-select'
        else:
            raise AssertionError(f'{qid}: unknown kind {kind!r}')

        if len(set(keys)) != len(keys):
            raise AssertionError(f'{qid}: duplicate option keys {keys}')
        for k in keys:
            if k not in TERMS:
                raise AssertionError(f'{qid}: unknown term key {k!r}')
        for a in answers:
            if a.startswith('bad_'):
                raise AssertionError(f'{qid}: anti-pattern key {a!r} cannot be a correct answer')

        stem = rec['question']
        if len(stem) > 520:
            raise AssertionError(f'{qid}: stem length {len(stem)} > 520')

        rng = _rng(f'{EXAM_CODE}:opts:{qid}')
        if kind in ('S', 'O'):
            dis_shuf = list(distractors)
            rng.shuffle(dis_shuf)
            ordered_keys = list(dis_shuf)
            ordered_keys.insert(slot_map[qid] - 1, answers[0])
        else:
            ordered_keys = list(keys)
            rng.shuffle(ordered_keys)

        row = dict.fromkeys(HEADER, '')
        row['Question'] = stem
        row['Question Type'] = qtype
        ans_set = set(answers)
        correct_indices, correct_letters = [], []

        for idx, k in enumerate(ordered_keys, start=1):
            label, note = TERMS[k]
            if len(label) > 255:
                raise AssertionError(f'{qid} ({k}): option label length {len(label)} > 255')
            is_ok = k in ans_set
            prefix = 'Correct.' if is_ok else 'Incorrect.'
            exp = f'{prefix} {note}'
            if len(exp) > 550:
                raise AssertionError(f'{qid} ({k}): option explanation length {len(exp)} > 550')
            row[f'Answer Option {idx}'] = label
            row[f'Explanation {idx}'] = exp
            if is_ok:
                correct_indices.append(idx)
                correct_letters.append(chr(64 + idx))

        row['Correct Answers'] = ','.join(str(i) for i in correct_indices)
        src_title, src_url = SKILL_SOURCES[rec['task']]
        joined = (
            ' and '.join(correct_letters)
            if len(correct_letters) <= 2
            else ', '.join(correct_letters[:-1]) + f', and {correct_letters[-1]}'
        )
        verb = 'is' if len(correct_letters) == 1 else 'are'
        overall = (
            f"Correct answer{'s' if len(correct_letters) > 1 else ''}: {joined} ({verb} correct). "
            f"{rec['reason']} "
            f"[Skill {rec['task']}: {SKILLS[rec['task']]} | Source: {src_title} ({src_url})]"
        )
        if len(overall) > 1250:
            raise AssertionError(f'{qid}: overall explanation length {len(overall)} > 1250')
        row['Overall Explanation'] = overall
        row['Domain'] = DOMAINS[rec['domain']]
        rows.append(row)

        manifest.append({
            'set': set_num,
            'question': q_idx,
            'id': qid,
            'domain': rec['domain'],
            'task': rec['task'],
            'kind': kind,
            'correct_terms': answers,
            'option_terms': ordered_keys,
            'correct_indices': correct_indices,
        })
    return rows, manifest


def _write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def _render_md(set_num: int, rows: list[dict]) -> str:
    lines = [
        f'# Microsoft Exam {EXAM_CODE}: {EXAM_TITLE} — {TOPICS[set_num]}',
        '',
        f'**Theme:** {SUBTITLES[set_num]}  ',
        f'**Credential:** `{CREDENTIAL_TITLE}` *(Beginner / Fundamentals · **no prerequisite** · **never expires**)*  ',
        f'**Study guide baseline:** `{STUDY_GUIDE_DATE}` ({STUDY_GUIDE_URL})  ',
        f'**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  ',
        f'**Recommended timing:** `75 minutes` (`45 sec/question`, matching live 45-minute / 60-question pace; `45 minutes` optional speed drill · **closed-book**)',
        '',
        '> **Disclaimer:** Independent educational material authored from public Microsoft Learn documentation — not affiliated with or endorsed by Microsoft Corporation. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.',
        '',
        '## Questions',
        '',
    ]
    current_dom = None
    for idx, row in enumerate(rows, start=1):
        rec_dom = next(d for d, label in DOMAINS.items() if label == row['Domain'])
        if rec_dom != current_dom:
            current_dom = rec_dom
            lo, hi = OFFICIAL_RANGES[rec_dom]
            lines += [
                '---',
                '',
                f'## Domain {rec_dom} — {DOMAINS[rec_dom]} ({lo}–{hi}% official weight · {ALLOCATIONS[set_num][rec_dom]} questions)',
                '',
            ]
        lines += [f"### {idx}. {row['Question']}", '']
        for opt_i in range(1, 7):
            val = row[f'Answer Option {opt_i}']
            if val:
                lines.append(f'- **{chr(64 + opt_i)}.** {val}')
        lines.append('')

    lines += ['---', '', '## Answer Key and Explanations', '']
    for idx, row in enumerate(rows, start=1):
        letters = ', '.join(chr(64 + int(x)) for x in row['Correct Answers'].split(','))
        lines += [
            f"### Question {idx} — `{letters}` ({row['Domain']})",
            '',
            row['Overall Explanation'],
            '',
        ]
        for opt_i in range(1, 7):
            exp = row[f'Explanation {opt_i}']
            if exp:
                lines.append(f'- **{chr(64 + opt_i)}:** {exp}')
        lines.append('')
    return '\n'.join(lines)


def _render_set_readme(set_num: int, rows: list[dict]) -> str:
    dom_counts = Counter(r['Domain'] for r in rows)
    type_counts = Counter(r['Question Type'] for r in rows)
    slot_counts = Counter(int(r['Correct Answers']) for r in rows if r['Question Type'] == 'multiple-choice')
    cf = sum(1 for r in rows if '____' in r['Question'])
    ps = sum(1 for r in rows if 'Proposed solution:' in r['Question'])
    return '\n'.join([
        f'# Practice Set {set_num} — {TOPICS[set_num]}',
        '',
        f'**Theme:** {SUBTITLES[set_num]}',
        '',
        '## Files in This Folder',
        '',
        f'- `practice-set-{set_num}.csv` — 100-question Udemy bulk-upload CSV (UTF-8 with BOM, LF line endings, 17 columns).',
        f'- `practice-set-{set_num}.md` — Human-readable review copy with full per-option rationales and official Microsoft Learn links.',
        '',
        '## Recommended Udemy Practice-Test Settings',
        '',
        '- **Question count:** `100` (comprehensive Fundamentals bank; live DP-900 contains zero case studies and zero live labs)',
        '- **Recommended timer:** `75 minutes` (`45 sec/question`, matching live 45-minute / 60-question pace; `45 minutes` optional speed drill)',
        '- **Minimum Score to Pass (Udemy):** `75%` (practice benchmark only; live DP-900 uses a `700 / 1000` criterion-referenced scaled score)',
        '- **Randomize Question & Answer Order:** Enabled (every question is self-contained)',
        '- **Open-book rule:** Take **closed-book** — split-screen Microsoft Learn access is **not** available on Microsoft Fundamentals exams',
        '',
        '## Blueprint & Format Summary',
        '',
        f"- **Domain 1 (`25–30%`):** `{dom_counts[DOMAINS[1]]}` questions",
        f"- **Domain 2 (`20–25%`):** `{dom_counts[DOMAINS[2]]}` questions",
        f"- **Domain 3 (`15–20%`):** `{dom_counts[DOMAINS[3]]}` questions",
        f"- **Domain 4 (`25–30%`):** `{dom_counts[DOMAINS[4]]}` questions",
        f"- **Question Formats:** `{type_counts['multiple-choice']}` `multiple-choice` (balanced `{slot_counts[1]}/{slot_counts[2]}/{slot_counts[3]}/{slot_counts[4]}` across A–D, including `8` four-step `→` sequences) + `{type_counts['multi-select']}` `multi-select` (`13` `Select two.` + `3` `Select three.`)",
        f"- **Completion (`____`) Items:** `{cf}` · **`Proposed solution:` Items:** `{ps}`",
        '',
    ])


def build_all() -> None:
    all_manifest = []
    for set_num in range(1, 7):
        rows, manifest = _render_set(set_num, BANK[set_num])
        all_manifest.extend(manifest)
        sdir = SETS_DIR / f'set-{set_num}'
        _write_csv(sdir / f'practice-set-{set_num}.csv', rows)
        (sdir / f'practice-set-{set_num}.md').write_text(_render_md(set_num, rows), encoding='utf-8')
        (sdir / 'README.md').write_text(_render_set_readme(set_num, rows), encoding='utf-8')

    (RES_DIR / 'answer-manifest.json').write_text(
        json.dumps(all_manifest, indent=2, ensure_ascii=False) + '\n',
        encoding='utf-8',
    )
    print(f'Built 6 DP-900 practice sets (CSV + MD + README) and answer-manifest.json under {ROOT}')


if __name__ == '__main__':
    build_all()
