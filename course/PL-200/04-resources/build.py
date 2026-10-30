#!/usr/bin/env python3
"""Deterministically build PL-200 practice-set CSVs, case-embedded CSVs, sample CSV, Markdown study keys, and manifest."""
import csv
import hashlib
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from bank import (  # noqa: E402
    ALLOCATIONS,
    BANK,
    CASE_SIZE,
    CASE_STUDIES,
    CODE_FILL_FLOOR,
    CREDENTIAL_TITLE,
    DOMAINS,
    EXAM_CODE,
    EXAM_TITLE,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    OFFICIAL_RANGES,
    PROPOSED_SOL_FLOOR,
    RETIREMENT_DATE,
    SKILL_PLAN,
    SKILL_SOURCES,
    SKILLS,
    STUDY_GUIDE_DATE,
    STUDY_GUIDE_URL,
    SUBTITLES,
    SUCCESSOR_EXAM,
    TERMS,
    TOPICS,
    TYPE_PLAN,
)
from cases import CASES  # noqa: E402

ROOT = HERE.parent

HEADER = [
    'Question', 'Question Type',
    'Answer Option 1', 'Explanation 1',
    'Answer Option 2', 'Explanation 2',
    'Answer Option 3', 'Explanation 3',
    'Answer Option 4', 'Explanation 4',
    'Answer Option 5', 'Explanation 5',
    'Answer Option 6', 'Explanation 6',
    'Correct Answers', 'Overall Explanation', 'Domain',
]

ALLOWED_TYPES = {'multiple-choice', 'multi-select'}
EXPORT_TYPE = {
    'multiple-choice': 'multiple-choice',
    'ordering': 'multiple-choice',
    'multi-select': 'multi-select',
}
EXPORT_PLAN = {
    'multiple-choice': TYPE_PLAN['multiple-choice'] + TYPE_PLAN['ordering'],
    'multi-select': TYPE_PLAN['multi-select'],
}
assert sum(EXPORT_PLAN.values()) == ITEM_TOTAL

CASE_PREFIX = re.compile(r'^Case study\s*[—-]\s*([^:]+):\s*(.+)$', re.S)


def rng_for(tag: str) -> random.Random:
    seed = int.from_bytes(hashlib.sha256(tag.encode('utf-8')).digest()[:8], 'big')
    return random.Random(seed)


def case_name(question: str):
    m = CASE_PREFIX.match(question)
    return m.group(1).strip() if m else None


def strip_case_prefix(question: str) -> str:
    m = CASE_PREFIX.match(question)
    return m.group(2).strip() if m else question


def embed_case_brief(question: str) -> str:
    m = CASE_PREFIX.match(question)
    if not m:
        return question
    name, rest = m.group(1).strip(), m.group(2).strip()
    if name not in CASES:
        raise ValueError(f'Unknown case study {name!r}; expected one of {sorted(CASES)}')
    return f'Case study — {name}: {CASES[name]} {rest}'


def kind_to_type(kind: str) -> str:
    if kind == 'S':
        return 'multiple-choice'
    if kind == 'O':
        return 'ordering'
    if kind in ('M2', 'M3'):
        return 'multi-select'
    raise ValueError(f'Unknown question kind: {kind!r}')


def assert_record(rec: dict) -> None:
    qid = rec['id']
    kind = rec['kind']
    ans = rec['answers']
    dis = rec['distractors']
    keys = rec['keys']
    if len(keys) != len(set(keys)):
        raise ValueError(f'{qid}: duplicate term keys in {keys}')
    for k in keys:
        if k not in TERMS:
            raise ValueError(f'{qid}: unknown term key {k!r}')
    if kind in ('S', 'O'):
        if len(ans) != 1 or len(dis) != 3:
            raise ValueError(f'{qid}: {kind} requires 1 answer and 3 distractors')
    elif kind == 'M2':
        if len(ans) != 2 or len(dis) not in (3, 4):
            raise ValueError(f'{qid}: M2 requires 2 answers and 3-4 distractors')
    elif kind == 'M3':
        if len(ans) != 3 or len(dis) not in (2, 3):
            raise ValueError(f'{qid}: M3 requires 3 answers and 2-3 distractors')
    labels = [TERMS[k][0].strip().casefold() for k in keys]
    if len(labels) != len(set(labels)):
        raise ValueError(f'{qid}: duplicate rendered option labels among {keys}')
    if kind == 'O':
        for k in keys:
            if '→' not in TERMS[k][0]:
                raise ValueError(f'{qid}: ordering key {k!r} must render a "→" step sequence')
    else:
        for k in keys:
            if k.startswith('seq_'):
                raise ValueError(f'{qid}: sequence key {k!r} used outside ordering item')


def order_records(records: list[dict], set_number: int) -> list[dict]:
    standalone = []
    case_groups = {}
    case_order = []
    for rec in records:
        cname = case_name(rec['question'])
        if cname is None:
            standalone.append(rec)
        else:
            if cname not in case_groups:
                case_groups[cname] = []
                case_order.append(cname)
            case_groups[cname].append(rec)

    if len(case_order) != CASE_STUDIES:
        raise ValueError(f'Exam {set_number}: expected {CASE_STUDIES} case studies, got {len(case_order)}: {case_order}')
    for cname, items in case_groups.items():
        if len(items) != CASE_SIZE:
            raise ValueError(f'Exam {set_number}: case {cname!r} has {len(items)} items; expected {CASE_SIZE}')
        if cname not in CASES:
            raise ValueError(f'Exam {set_number}: case {cname!r} missing from CASES')

    rng = rng_for(f'pl200-order-set-{set_number}')
    standalone_shuffled = list(standalone)
    rng.shuffle(standalone_shuffled)
    case_names_shuffled = list(case_order)
    rng.shuffle(case_names_shuffled)

    anchors = [16, 38, 60, 80]
    ordered = []
    cursor = 0
    for idx, cname in enumerate(case_names_shuffled):
        take = anchors[idx] - cursor
        ordered.extend(standalone_shuffled[cursor:cursor + take])
        cursor += take
        ordered.extend(case_groups[cname])
    ordered.extend(standalone_shuffled[cursor:])
    assert len(ordered) == len(records)
    return ordered


def assign_balanced_slots(records: list[dict], set_number: int) -> dict[str, int]:
    singles = [r for r in records if r['kind'] in ('S', 'O')]
    if len(singles) % 4 != 0:
        raise ValueError(f'Exam {set_number}: single-answer count {len(singles)} not divisible by 4')
    per_slot = len(singles) // 4
    slots = [1] * per_slot + [2] * per_slot + [3] * per_slot + [4] * per_slot
    rng_for(f'pl200-slots-set-{set_number}').shuffle(slots)
    return {rec['id']: slot for rec, slot in zip(singles, slots)}


def overall_explanation(rec: dict, correct_letters: list[str]) -> str:
    domain_name = DOMAINS[rec['domain']]
    skill_name = SKILLS[rec['task']]
    title, url = SKILL_SOURCES[rec['task']]
    joined = ' and '.join(correct_letters) if len(correct_letters) <= 2 else ', '.join(correct_letters[:-1]) + f', and {correct_letters[-1]}'
    verb = 'is' if len(correct_letters) == 1 else 'are'
    text = (
        f'Correct answer{"s" if len(correct_letters) > 1 else ""}: {joined} ({verb} correct). '
        f'{rec["reason"]} '
        f'[PL-200 {domain_name} — {skill_name} | Ref: {title} ({url})]'
    )
    if len(text) > 1480:
        raise ValueError(f'{rec["id"]}: Overall Explanation exceeds 1480 chars ({len(text)})')
    return text


def render_item(rec: dict, target_slot: int | None) -> dict:
    assert_record(rec)
    rng = rng_for(f'pl200-options-{rec["id"]}')
    internal_type = kind_to_type(rec['kind'])
    csv_type = EXPORT_TYPE[internal_type]
    ans = list(rec['answers'])
    dis = list(rec['distractors'])

    if rec['kind'] in ('S', 'O'):
        assert target_slot in (1, 2, 3, 4)
        rng.shuffle(dis)
        ordered_keys = list(dis)
        ordered_keys.insert(target_slot - 1, ans[0])
    else:
        ordered_keys = ans + dis
        rng.shuffle(ordered_keys)

    options = []
    correct_indices = []
    correct_letters = []
    ans_set = set(ans)
    for idx, key in enumerate(ordered_keys, start=1):
        label, detail = TERMS[key]
        is_ok = key in ans_set
        prefix = 'Correct — ' if is_ok else 'Incorrect — '
        exp = f'{prefix}{detail}'
        if len(label) > 280:
            raise ValueError(f'{rec["id"]}: option {key!r} label > 280 chars ({len(label)})')
        if len(exp) > 580:
            raise ValueError(f'{rec["id"]}: option {key!r} explanation > 580 chars ({len(exp)})')
        options.append((label, exp, is_ok))
        if is_ok:
            correct_indices.append(idx)
            correct_letters.append(chr(64 + idx))

    stem = rec['question']
    embedded_stem = embed_case_brief(stem)
    if len(embedded_stem) > 995:
        raise ValueError(f'{rec["id"]}: case-embedded Question > 995 chars ({len(embedded_stem)})')

    return {
        'id': rec['id'],
        'task': rec['task'],
        'domain_num': rec['domain'],
        'domain': DOMAINS[rec['domain']],
        'kind': rec['kind'],
        'internal_type': internal_type,
        'csv_type': csv_type,
        'case': case_name(stem),
        'question': stem,
        'embedded_question': embedded_stem,
        'bare_question': strip_case_prefix(stem),
        'options': options,
        'correct_indices': correct_indices,
        'correct_letters': correct_letters,
        'overall': overall_explanation(rec, correct_letters),
        'reason': rec['reason'],
        'source_title': SKILL_SOURCES[rec['task']][0],
        'source_url': SKILL_SOURCES[rec['task']][1],
    }


def item_to_csv_row(item: dict, embed_case: bool = False) -> list[str]:
    q_text = item['embedded_question'] if embed_case else item['question']
    cells = [q_text, item['csv_type']]
    for slot in range(6):
        if slot < len(item['options']):
            cells.extend([item['options'][slot][0], item['options'][slot][1]])
        else:
            cells.extend(['', ''])
    cells.append(','.join(str(i) for i in item['correct_indices']))
    cells.append(item['overall'])
    cells.append(item['domain'])
    return cells


def write_csv(path: Path, rows: list[list[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8-sig', newline='\n') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(HEADER)
        writer.writerows(rows)


def write_markdown_set(path: Path, set_number: int, items: list[dict]) -> None:
    lines = [
        f'# Microsoft Exam {EXAM_CODE}: {TOPICS[set_number]} — Reviewer Study Key',
        '',
        f'**Theme:** {SUBTITLES[set_number]}  ',
        f'**Credential:** {CREDENTIAL_TITLE}  ',
        f'**Study guide baseline:** {STUDY_GUIDE_DATE} ({STUDY_GUIDE_URL})  ',
        f'**Lifecycle notice:** Exam {EXAM_CODE} retired on {RETIREMENT_DATE} and was replaced by Exam {SUCCESSOR_EXAM}.  ',
        f'**Questions:** {len(items)} (`{EXPORT_PLAN["multiple-choice"]}` multiple-choice + `{EXPORT_PLAN["multi-select"]}` multi-select; `{CASE_STUDIES}` case studies × `{CASE_SIZE}` questions = `{CASE_STUDIES * CASE_SIZE}` case-based items)',
        '',
        '> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice scores do not equate to Microsoft’s 700/1000 scaled score.',
        '',
        '---',
        '',
    ]
    seen_cases = set()
    for qnum, item in enumerate(items, start=1):
        cname = item['case']
        if cname and cname not in seen_cases:
            seen_cases.add(cname)
            lines.extend([
                f'## Case Study Vignette — {cname}',
                '',
                f'> {CASES[cname]}',
                '',
            ])
        badge = {
            'S': 'Single-Answer Multiple Choice',
            'O': 'Ordered Sequence (Multiple Choice)',
            'M2': 'Multi-Select (Select 2)',
            'M3': 'Multi-Select (Select 3)',
        }[item['kind']]
        lines.append(f'### Q{qnum:03d} (`{item["id"]}`) — {item["domain"]} [{item["task"]}] · *{badge}*')
        lines.append('')
        lines.append(item['question'])
        lines.append('')
        for idx, (label, _exp, _ok) in enumerate(item['options'], start=1):
            letter = chr(64 + idx)
            lines.append(f'- **{letter}.** {label}')
        lines.append('')
        lines.append('<details><summary><strong>Answer &amp; Explanation</strong></summary>')
        lines.append('')
        lines.append(f'**Correct:** `{", ".join(item["correct_letters"])}` (`CSV: {",".join(str(i) for i in item["correct_indices"])}`)')
        lines.append('')
        lines.append(item['overall'])
        lines.append('')
        for idx, (_label, exp, _ok) in enumerate(item['options'], start=1):
            letter = chr(64 + idx)
            lines.append(f'- **{letter}:** {exp}')
        lines.append('')
        lines.append('</details>')
        lines.append('')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines), encoding='utf-8')


def write_set_readme(path: Path, set_number: int, items: list[dict]) -> None:
    dom_counts = Counter(it['domain_num'] for it in items)
    kind_counts = Counter(it['kind'] for it in items)
    slot_counts = Counter(it['correct_indices'][0] for it in items if it['csv_type'] == 'multiple-choice')
    case_names_ordered = []
    for it in items:
        if it['case'] and it['case'] not in case_names_ordered:
            case_names_ordered.append(it['case'])
    code_count = sum(1 for it in items if '____' in it['question'])
    prop_count = sum(1 for it in items if 'Proposed solution:' in it['question'])

    lines = [
        f'# {TOPICS[set_number]} (`set-{set_number}`)',
        '',
        f'**Theme:** {SUBTITLES[set_number]}  ',
        f'**Target Blueprint:** Microsoft Exam {EXAM_CODE} — *{EXAM_TITLE}* (`{STUDY_GUIDE_DATE}` official outline; retired `{RETIREMENT_DATE}`, succeeded by `{SUCCESSOR_EXAM}`)  ',
        f'**Recommended Timing:** `100 minutes` (`100 questions`, aligned to the 100-minute Microsoft Associate exam window)',
        '',
        '## Files in This Folder',
        '',
        '| File | Purpose | Upload to Udemy? |',
        '|---|---|---|',
        f'| `practice-set-{set_number}.csv` | Standard 100-question Udemy bulk-import CSV (`UTF-8 BOM`, 17 columns). Pair with `04-resources/case-studies.md` as a downloadable section resource. | **Option A — Standard Upload** |',
        f'| `case-embedded-set-{set_number}.csv` | Self-contained 100-question Udemy CSV that prepends each full case-study scenario brief directly into its 3 associated `Question` cells (`<= 1,000` chars). | **Option B — Self-Contained Upload (Recommended)** |',
        f'| `practice-set-{set_number}.md` | Human-readable reviewer and self-study answer key with collapsible rationales and official Microsoft Learn links. | Do not upload as CSV |',
        '',
        '## Domain Distribution',
        '',
        '| Domain | Official Weight | Questions | Share |',
        '|---|---:|---:|---:|',
    ]
    for d in sorted(DOMAINS):
        lo, hi = OFFICIAL_RANGES[d]
        cnt = dom_counts[d]
        lines.append(f'| {d}. {DOMAINS[d]} | {lo}–{hi}% | {cnt} | {cnt:.1f}% |')
    lines.extend([
        f'| **Total** | **100%** | **{len(items)}** | **100.0%** |',
        '',
        '## Question Type & Pattern Mix',
        '',
        f'- **Single-Answer Multiple Choice (`multiple-choice`):** `{kind_counts["S"] + kind_counts["O"]}` (`{kind_counts["S"]}` scenario single-choice + `{kind_counts["O"]}` four-step ordered-sequence `→` items)',
        f'- **Multi-Select (`multi-select`):** `{kind_counts["M2"] + kind_counts["M3"]}` (`{kind_counts["M2"]}` Select-2 + `{kind_counts["M3"]}` Select-3 items)',
        f'- **Single-Answer Slot Balance (`A / B / C / D`):** `{slot_counts[1]} / {slot_counts[2]} / {slot_counts[3]} / {slot_counts[4]}`',
        f'- **Power Fx / WDL / OData / Config Completion (`____`) Items:** `{code_count}`',
        f'- **Repeated-Scenario (`Proposed solution:`) Evaluation Items:** `{prop_count}`',
        f'- **Case Studies (`{CASE_STUDIES} × {CASE_SIZE} = {CASE_STUDIES * CASE_SIZE}` items):** ' + ', '.join(f'*{c}*' for c in case_names_ordered),
        '',
    ])
    path.write_text('\n'.join(lines), encoding='utf-8')


def write_case_studies_doc(path: Path, all_items_by_set: dict[int, list[dict]]) -> None:
    lines = [
        f'# Microsoft Exam {EXAM_CODE} — Companion Case Study Scenarios (24 Vignettes)',
        '',
        'Attach this document as a downloadable resource when uploading `practice-set-{1..6}.csv` (Option A), or upload `case-embedded-set-{1..6}.csv` (Option B) so every case-linked question embeds its full scenario brief inline inside the Udemy question prompt.',
        '',
        '> All 24 organizations and scenarios below are 100% original fictional Functional Consultant case studies authored for independent exam preparation. None reproduce Microsoft’s copyrighted exam case studies.',
        '',
    ]
    for n in range(1, 7):
        lines.append(f'## {TOPICS[n]} — {SUBTITLES[n]}')
        lines.append('')
        seen = {}
        for qnum, it in enumerate(all_items_by_set[n], start=1):
            if it['case']:
                seen.setdefault(it['case'], []).append(f'Q{qnum:03d}')
        for cname, qnums in seen.items():
            lines.append(f'### {cname} ({", ".join(qnums)})')
            lines.append('')
            lines.append(CASES[cname])
            lines.append('')
    path.write_text('\n'.join(lines), encoding='utf-8')


def write_summary(path: Path, all_items_by_set: dict[int, list[dict]]) -> None:
    total_q = sum(len(v) for v in all_items_by_set.values())
    lines = [
        f'# {EXAM_CODE} Build Summary (`6 × 100 = {total_q}` Questions)',
        '',
        f'- **Exam:** Microsoft Exam `{EXAM_CODE}` — *{EXAM_TITLE}*',
        f'- **Credential:** `{CREDENTIAL_TITLE}`',
        f'- **Official Study Guide Baseline:** `{STUDY_GUIDE_DATE}` ({STUDY_GUIDE_URL})',
        f'- **Retirement & Replacement Notice:** Retired `{RETIREMENT_DATE}`; succeeded by `{SUCCESSOR_EXAM}`',
        f'- **Total Questions Built:** `{total_q}` across `6` full-length 100-question exams',
        f'- **Skills Covered per Exam:** `{len(SKILLS)}` skills across `4` domains (`28 / 28 / 27 / 17`)',
        f'- **Case Studies:** `{len(CASES)}` original case studies (`4` per exam × `3` questions = `12` case items/exam, `72` total)',
        '',
        '## Per-Exam Verification Matrix',
        '',
        '| Exam | Total | D1 (25–30%) | D2 (25–30%) | D3 (25–30%) | D4 (15–20%) | MC (`S`+`O`) | MS (`M2`+`M3`) | `A/B/C/D` Slots | `____` | `Proposed solution:` |',
        '|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|',
    ]
    for n, items in all_items_by_set.items():
        dc = Counter(it['domain_num'] for it in items)
        kc = Counter(it['kind'] for it in items)
        sc = Counter(it['correct_indices'][0] for it in items if it['csv_type'] == 'multiple-choice')
        cf = sum(1 for it in items if '____' in it['question'])
        ps = sum(1 for it in items if 'Proposed solution:' in it['question'])
        lines.append(
            f'| Exam {n} | {len(items)} | {dc[1]} | {dc[2]} | {dc[3]} | {dc[4]} | '
            f'{kc["S"] + kc["O"]} ({kc["S"]}+{kc["O"]}) | {kc["M2"] + kc["M3"]} ({kc["M2"]}+{kc["M3"]}) | '
            f'{sc[1]}/{sc[2]}/{sc[3]}/{sc[4]} | {cf} | {ps} |'
        )
    lines.append('')
    path.write_text('\n'.join(lines), encoding='utf-8')


def build_all() -> dict:
    manifest = {
        'exam_code': EXAM_CODE,
        'exam_title': EXAM_TITLE,
        'credential': CREDENTIAL_TITLE,
        'study_guide_date': STUDY_GUIDE_DATE,
        'retirement_date': RETIREMENT_DATE,
        'successor_exam': SUCCESSOR_EXAM,
        'sets': {},
    }
    all_items_by_set = {}

    for set_number in range(1, 7):
        records = BANK[set_number]
        if len(records) != ITEM_TOTAL:
            raise ValueError(f'Exam {set_number}: expected {ITEM_TOTAL} questions, found {len(records)}')

        skill_counts = Counter(r['task'] for r in records)
        if skill_counts != Counter(SKILL_PLAN):
            diffs = {
                k: (skill_counts[k], SKILL_PLAN.get(k, 0))
                for k in sorted(set(skill_counts) | set(SKILL_PLAN))
                if skill_counts[k] != SKILL_PLAN.get(k, 0)
            }
            raise ValueError(f'Exam {set_number}: SKILL_PLAN mismatch {diffs}')

        kind_counts = Counter(r['kind'] for r in records)
        if kind_counts != Counter(KIND_PLAN):
            raise ValueError(f'Exam {set_number}: KIND_PLAN mismatch {dict(kind_counts)} != {KIND_PLAN}')

        ms_by_domain = Counter(r['domain'] for r in records if r['kind'] in ('M2', 'M3'))
        if ms_by_domain != Counter(MULTI_PLAN):
            raise ValueError(f'Exam {set_number}: MULTI_PLAN mismatch {dict(ms_by_domain)} != {MULTI_PLAN}')

        dom_counts = Counter(r['domain'] for r in records)
        if dom_counts != Counter(ALLOCATIONS[set_number]):
            raise ValueError(f'Exam {set_number}: domain allocation mismatch {dict(dom_counts)}')

        code_fills = sum(1 for r in records if '____' in r['question'])
        if code_fills < CODE_FILL_FLOOR:
            raise ValueError(f'Exam {set_number}: expected >= {CODE_FILL_FLOOR} ____ items, got {code_fills}')

        prop_sols = sum(1 for r in records if 'Proposed solution:' in r['question'])
        if prop_sols < PROPOSED_SOL_FLOOR:
            raise ValueError(f'Exam {set_number}: expected >= {PROPOSED_SOL_FLOOR} Proposed solution: items, got {prop_sols}')

        ordered = order_records(records, set_number)
        slot_map = assign_balanced_slots(ordered, set_number)
        items = [render_item(rec, slot_map.get(rec['id'])) for rec in ordered]
        all_items_by_set[set_number] = items

        set_dir = ROOT / f'03-practice-sets/set-{set_number}'
        write_csv(set_dir / f'practice-set-{set_number}.csv', [item_to_csv_row(it, embed_case=False) for it in items])
        write_csv(set_dir / f'case-embedded-set-{set_number}.csv', [item_to_csv_row(it, embed_case=True) for it in items])
        write_markdown_set(set_dir / f'practice-set-{set_number}.md', set_number, items)
        write_set_readme(set_dir / 'README.md', set_number, items)

        manifest['sets'][f'set-{set_number}'] = [
            {
                'q': idx,
                'id': it['id'],
                'skill': it['task'],
                'domain': it['domain'],
                'kind': it['kind'],
                'csv_type': it['csv_type'],
                'case': it['case'],
                'correct_letters': it['correct_letters'],
                'correct_csv': ','.join(str(i) for i in it['correct_indices']),
                'source_url': it['source_url'],
            }
            for idx, it in enumerate(items, start=1)
        ]

    sample_items = [it for it in all_items_by_set[1] if it['case'] is not None]
    assert len(sample_items) == CASE_STUDIES * CASE_SIZE
    write_csv(ROOT / '05-sample-upload/case-study-sample.csv', [item_to_csv_row(it, embed_case=True) for it in sample_items])

    write_case_studies_doc(HERE / 'case-studies.md', all_items_by_set)
    write_summary(HERE / 'SUMMARY.md', all_items_by_set)
    (HERE / 'answer-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    return manifest


if __name__ == '__main__':
    build_all()
    print('Built 6 x 100 = 600 PL-200 questions, 12 full CSVs, 1 sample CSV, 6 study keys, case-studies.md, SUMMARY.md, and answer-manifest.json.')
