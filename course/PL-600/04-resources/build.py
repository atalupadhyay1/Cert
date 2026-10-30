#!/usr/bin/env python3
"""Deterministic Udemy CSV, Markdown review key, and case-study companion generator for Exam PL-600."""
import csv
import hashlib
import random
import re
from collections import Counter
from pathlib import Path

from bank import (
    ALLOCATIONS,
    BANK,
    CASES,
    CASE_SIZE,
    CASE_STUDIES,
    CREDENTIAL_TITLE,
    DOMAINS,
    EXAM_CODE,
    EXAM_TITLE,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    PREREQUISITES,
    RETIREMENT_DATE,
    SKILLS,
    SKILL_PLAN,
    SKILL_SOURCES,
    STUDY_GUIDE_DATE,
    STUDY_GUIDE_URL,
    SUBTITLES,
    SUCCESSOR_EXAM,
    TERMS,
    TOPICS,
)

HEADER = [
    'Question',
    'Question Type',
    'Answer Option 1', 'Explanation 1',
    'Answer Option 2', 'Explanation 2',
    'Answer Option 3', 'Explanation 3',
    'Answer Option 4', 'Explanation 4',
    'Answer Option 5', 'Explanation 5',
    'Answer Option 6', 'Explanation 6',
    'Correct Answers',
    'Overall Explanation',
    'Domain',
]

ROOT = Path(__file__).resolve().parent.parent
SETS_DIR = ROOT / '03-practice-sets'
RES_DIR = ROOT / '04-resources'
SAMPLE_DIR = ROOT / '05-sample-upload'

CASE_RE = re.compile(r'^Case study \u2014 ([^:]+): (.+)$', re.S)


def _rng(tag: str) -> random.Random:
    seed = int(hashlib.sha256(tag.encode('utf-8')).hexdigest()[:16], 16)
    return random.Random(seed)


def _check_blueprint(set_num: int, items: list[dict]) -> None:
    if len(items) != ITEM_TOTAL:
        raise AssertionError(f'Set {set_num}: expected {ITEM_TOTAL} items, found {len(items)}')
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
        diff = {k: (skills.get(k, 0), SKILL_PLAN.get(k, 0)) for k in set(skills) | set(SKILL_PLAN) if skills.get(k, 0) != SKILL_PLAN.get(k, 0)}
        raise AssertionError(f'Set {set_num}: skill counts mismatch: {diff}')

    valid_cases = CASES[set_num]
    case_counts = Counter()
    for it in items:
        m = CASE_RE.match(it['question'])
        if m:
            cname = m.group(1)
            if cname not in valid_cases:
                raise AssertionError(f'Set {set_num} ({it["id"]}): unknown case study {cname!r}')
            case_counts[cname] += 1
        elif it['question'].lower().startswith('case study'):
            raise AssertionError(f'Set {set_num} ({it["id"]}): malformed Case study prefix: {it["question"][:60]!r}')
    if len(case_counts) != CASE_STUDIES or any(v != CASE_SIZE for v in case_counts.values()):
        raise AssertionError(f'Set {set_num}: expected {CASE_STUDIES} cases x {CASE_SIZE} items, got {dict(case_counts)}')


def _order_items(set_num: int, items: list[dict]) -> list[dict]:
    standalone = []
    case_groups = {}
    case_order = []
    for it in items:
        m = CASE_RE.match(it['question'])
        if not m:
            standalone.append(it)
        else:
            cname = m.group(1)
            if cname not in case_groups:
                case_groups[cname] = []
                case_order.append(cname)
            case_groups[cname].append(it)

    rng = _rng(f'{EXAM_CODE}:order:{set_num}')
    standalone_shuf = list(standalone)
    rng.shuffle(standalone_shuf)
    case_names_shuf = list(case_order)
    rng.shuffle(case_names_shuf)

    anchors = [16, 38, 60, 80]
    ordered = []
    cursor = 0
    for idx, cname in enumerate(case_names_shuf):
        take = anchors[idx] - cursor
        ordered.extend(standalone_shuf[cursor:cursor + take])
        cursor += take
        ordered.extend(case_groups[cname])
    ordered.extend(standalone_shuf[cursor:])
    assert len(ordered) == ITEM_TOTAL
    return ordered


def _assign_mc_slots(set_num: int, items: list[dict]) -> dict[str, int]:
    singles = [it for it in items if it['kind'] in ('S', 'O')]
    assert len(singles) == 84
    slots = [1] * 21 + [2] * 21 + [3] * 21 + [4] * 21
    _rng(f'{EXAM_CODE}:slots:{set_num}').shuffle(slots)
    return {it['id']: slot for it, slot in zip(singles, slots)}


def _render_item(set_num: int, item: dict, target_slot: int | None) -> dict:
    qid = item['id']
    kind = item['kind']
    answers = list(item['answers'])
    distractors = list(item['distractors'])
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
        if 'Select two.' not in item['question']:
            raise AssertionError(f'{qid}: M2 stem must contain "Select two."')
        qtype = 'multi-select'
    elif kind == 'M3':
        if len(answers) != 3 or len(keys) != 6 or any(k.startswith('seq_') for k in keys):
            raise AssertionError(f'{qid}: invalid M3 keys {keys}')
        if 'Select three.' not in item['question']:
            raise AssertionError(f'{qid}: M3 stem must contain "Select three."')
        qtype = 'multi-select'
    else:
        raise AssertionError(f'{qid}: unknown kind {kind!r}')

    if len(set(keys)) != len(keys):
        raise AssertionError(f'{qid}: duplicate option keys {keys}')
    for k in keys:
        if k not in TERMS:
            raise AssertionError(f'{qid}: unknown term key {k!r}')

    stem = item['question']
    if len(stem) > 520:
        raise AssertionError(f'{qid}: standalone stem length {len(stem)} > 520')

    m = CASE_RE.match(stem)
    cname = m.group(1) if m else None
    if m:
        brief = CASES[set_num][cname]
        emb_stem = f'[Case Study \u2014 {cname}] {brief}\n\nQuestion: {m.group(2)}'
        if len(emb_stem) > 995:
            raise AssertionError(f'{qid}: embedded case stem length {len(emb_stem)} > 995')
    else:
        emb_stem = stem

    rng = _rng(f'{EXAM_CODE}:opts:{qid}')
    if kind in ('S', 'O'):
        assert target_slot in (1, 2, 3, 4)
        dis_shuf = list(distractors)
        rng.shuffle(dis_shuf)
        ordered_keys = list(dis_shuf)
        ordered_keys.insert(target_slot - 1, answers[0])
    else:
        ordered_keys = list(keys)
        rng.shuffle(ordered_keys)

    ans_set = set(answers)
    options = []
    correct_indices = []
    correct_letters = []
    for idx, k in enumerate(ordered_keys, start=1):
        label, note = TERMS[k]
        if len(label) > 255:
            raise AssertionError(f'{qid} ({k}): option label length {len(label)} > 255')
        is_ok = k in ans_set
        prefix = 'Correct.' if is_ok else 'Incorrect.'
        exp = f'{prefix} {note}'
        if len(exp) > 550:
            raise AssertionError(f'{qid} ({k}): option explanation length {len(exp)} > 550')
        options.append((label, exp, is_ok))
        if is_ok:
            correct_indices.append(idx)
            correct_letters.append(chr(64 + idx))

    src_title, src_url = SKILL_SOURCES[item['task']]
    joined = ' and '.join(correct_letters) if len(correct_letters) <= 2 else ', '.join(correct_letters[:-1]) + f', and {correct_letters[-1]}'
    verb = 'is' if len(correct_letters) == 1 else 'are'
    overall = (
        f"Correct answer{'s' if len(correct_letters) > 1 else ''}: {joined} ({verb} correct). "
        f"{item['reason']} "
        f"[Skill {item['task']}: {SKILLS[item['task']]} | Source: {src_title} ({src_url})]"
    )
    if len(overall) > 1250:
        raise AssertionError(f'{qid}: overall explanation length {len(overall)} > 1250')

    return {
        'id': qid,
        'task': item['task'],
        'kind': kind,
        'qtype': qtype,
        'domain_num': item['domain'],
        'domain': DOMAINS[item['domain']],
        'case': cname,
        'question': stem,
        'embedded_question': emb_stem,
        'options': options,
        'correct_indices': correct_indices,
        'correct_letters': correct_letters,
        'overall': overall,
    }


def _to_csv_row(rendered: dict, embed_case: bool) -> list[str]:
    q_text = rendered['embedded_question'] if embed_case else rendered['question']
    opt_cells = []
    for slot in range(6):
        if slot < len(rendered['options']):
            opt_cells.extend([rendered['options'][slot][0], rendered['options'][slot][1]])
        else:
            opt_cells.extend(['', ''])
    return [
        q_text,
        rendered['qtype'],
        *opt_cells,
        ','.join(str(i) for i in rendered['correct_indices']),
        rendered['overall'],
        rendered['domain'],
    ]


def _write_csv(path: Path, rows: list[list[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(HEADER)
        writer.writerows(rows)


def _write_review_md(path: Path, set_num: int, rendered_items: list[dict]) -> None:
    lines = [
        f'# Microsoft Exam {EXAM_CODE}: {TOPICS[set_num]} — Reviewer Study Key',
        '',
        f'**Theme:** {SUBTITLES[set_num]}  ',
        f'**Credential:** {CREDENTIAL_TITLE} (`{PREREQUISITES}`)  ',
        f'**Study guide baseline:** {STUDY_GUIDE_DATE} ({STUDY_GUIDE_URL})  ',
        f'**Lifecycle notice:** Exam {EXAM_CODE} retired on {RETIREMENT_DATE}; succeeded by `{SUCCESSOR_EXAM}`.  ',
        f'**Questions:** `100` (`84` multiple-choice + `16` multi-select; `{CASE_STUDIES}` case studies × `{CASE_SIZE}` questions = `{CASE_STUDIES * CASE_SIZE}` case items)',
        '',
        '> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice percentages do not equate to Microsoft’s 700/1000 scaled score.',
        '',
        '---',
        '',
    ]
    seen_cases = set()
    for qnum, it in enumerate(rendered_items, start=1):
        cname = it['case']
        if cname and cname not in seen_cases:
            seen_cases.add(cname)
            lines.extend([
                f'## Case Study Vignette — {cname}',
                '',
                f'> {CASES[set_num][cname]}',
                '',
            ])
        badge = {
            'S': 'Single-Answer Multiple Choice',
            'O': 'Ordered Sequence (Multiple Choice)',
            'M2': 'Multi-Select (Select 2)',
            'M3': 'Multi-Select (Select 3)',
        }[it['kind']]
        lines.extend([
            f"### Q{qnum:03d} (`{it['id']}`) — {it['domain']} [{it['task']}] · *{badge}*",
            '',
            it['question'],
            '',
        ])
        for idx, (lbl, _exp, _ok) in enumerate(it['options'], start=1):
            lines.append(f'- **{chr(64 + idx)}.** {lbl}')
        lines.extend([
            '',
            '<details><summary><strong>Answer &amp; Explanation</strong></summary>',
            '',
            f"**Correct:** `{', '.join(it['correct_letters'])}` (`CSV: {','.join(str(i) for i in it['correct_indices'])}`)",
            '',
            it['overall'],
            '',
        ])
        for idx, (_lbl, exp, _ok) in enumerate(it['options'], start=1):
            lines.append(f'- **{chr(64 + idx)}:** {exp}')
        lines.extend(['', '</details>', ''])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def _write_set_readme(path: Path, set_num: int, rendered_items: list[dict]) -> None:
    dom_counts = Counter(it['domain_num'] for it in rendered_items)
    kind_counts = Counter(it['kind'] for it in rendered_items)
    slot_counts = Counter(it['correct_indices'][0] for it in rendered_items if it['qtype'] == 'multiple-choice')
    cf = sum(1 for it in rendered_items if '____' in it['question'])
    ps = sum(1 for it in rendered_items if 'Proposed solution:' in it['question'])
    cnames = list(CASES[set_num].keys())
    lines = [
        f'# {TOPICS[set_num]} (`set-{set_num}`)',
        '',
        f'**Theme:** {SUBTITLES[set_num]}  ',
        f'**Target Blueprint:** Microsoft Exam {EXAM_CODE} — *{EXAM_TITLE}* (`{STUDY_GUIDE_DATE}` final published outline; retired `{RETIREMENT_DATE}`, succeeded by `{SUCCESSOR_EXAM}`)  ',
        f'**Recommended Timing:** `100 minutes` (`100 questions`; raw practice percentages do not equate to Microsoft’s `700 / 1000` scaled score)',
        '',
        '## Files in This Folder',
        '',
        '| File | Purpose | Upload to Udemy? |',
        '|---|---|---|',
        f'| `practice-set-{set_num}.csv` | Standard 100-question Udemy bulk-import CSV (17 columns). Pair with `04-resources/case-studies.md` if question shuffling is disabled. | **Option A — Standard Upload** |',
        f'| `case-embedded-set-{set_num}.csv` | Self-contained 100-question Udemy CSV prepending each full case-study scenario brief directly into its 3 associated `Question` cells (`<= 995` chars). | **Option B — Self-Contained Upload (Recommended)** |',
        f'| `practice-set-{set_num}-review.md` | Offline Markdown Reviewer Study Key with collapsible `<details>` explanations. | Reference / Offline Review |',
        '',
        '## Blueprint & Format Summary',
        '',
        f'- **Domain 1 (`45–50%`):** `{dom_counts[1]}` questions',
        f'- **Domain 2 (`35–40%`):** `{dom_counts[2]}` questions',
        f'- **Domain 3 (`15–20%`):** `{dom_counts[3]}` questions',
        f"- **Question Formats:** `{kind_counts['S']}` single-choice + `{kind_counts['O']}` 4-step sequences (`84` MC balanced `{slot_counts[1]}/{slot_counts[2]}/{slot_counts[3]}/{slot_counts[4]}` across slots A–D) + `{kind_counts['M2']}` `Select two.` + `{kind_counts['M3']}` `Select three.` (`16` MS)",
        f'- **Completion (`____`) Items:** `{cf}` · **`Proposed solution:` Items:** `{ps}`',
        f'- **Four 3-Question Case Studies (`12` Items):** `{cnames[0]}`, `{cnames[1]}`, `{cnames[2]}`, `{cnames[3]}`',
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def _write_case_studies_companion() -> None:
    lines = [
        f'# {EXAM_CODE}: {EXAM_TITLE} — Companion Case-Study Scenario Briefs (24 Original Case Studies)',
        '',
        'Attach this document as a downloadable lecture/section resource if uploading compact `practice-set-{1..6}.csv` files, or upload `case-embedded-set-{1..6}.csv` so every randomized case question includes its scenario brief inline.',
        '',
    ]
    for s in range(1, 7):
        lines.extend([f'## Practice Exam {s} — {SUBTITLES[s]}', ''])
        for cname, brief in CASES[s].items():
            lines.extend([f'### {cname}', '', brief, ''])
    (RES_DIR / 'case-studies.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def build_all() -> None:
    sample_rows = []
    for set_num in range(1, 7):
        raw_items = BANK[set_num]
        _check_blueprint(set_num, raw_items)
        ordered = _order_items(set_num, raw_items)
        slots = _assign_mc_slots(set_num, ordered)
        rendered = [_render_item(set_num, it, slots.get(it['id'])) for it in ordered]

        std_rows = [_to_csv_row(r, embed_case=False) for r in rendered]
        emb_rows = [_to_csv_row(r, embed_case=True) for r in rendered]

        sdir = SETS_DIR / f'set-{set_num}'
        _write_csv(sdir / f'practice-set-{set_num}.csv', std_rows)
        _write_csv(sdir / f'case-embedded-set-{set_num}.csv', emb_rows)
        _write_review_md(sdir / f'practice-set-{set_num}-review.md', set_num, rendered)
        _write_set_readme(sdir / 'README.md', set_num, rendered)

        if set_num == 1:
            for r, row in zip(rendered, emb_rows):
                if r['case'] and len(sample_rows) < 12:
                    sample_rows.append(row)

    if len(sample_rows) != 12:
        raise AssertionError(f'Expected 12 sample rows from Set 1 cases, got {len(sample_rows)}')
    _write_csv(SAMPLE_DIR / 'case-study-sample.csv', sample_rows)
    _write_case_studies_companion()
    print(f'Built 6 practice sets (CSV + case-embedded CSV + review MD + README), case-studies.md, and sample CSV under {ROOT}')


if __name__ == '__main__':
    build_all()
