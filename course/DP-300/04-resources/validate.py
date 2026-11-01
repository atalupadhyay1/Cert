#!/usr/bin/env python3
"""Validate all DP-300 practice-set CSVs, case-embedded CSVs, and bank invariants."""
import argparse
import csv
import json
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
    DOMAINS,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    OFFICIAL_RANGES,
    PROPOSED_SOL_FLOOR,
    SKILL_PLAN,
    SKILLS,
    SUBTITLES,
    TERMS,
)
from build import ALLOWED_TYPES, EXPORT_PLAN, HEADER, case_name  # noqa: E402
from cases import CASES  # noqa: E402

ROOT = HERE.parent
BANNED_PHRASES = (
    'all of the above',
    'none of the above',
    'both a and b',
    'true or false',
    'lorem ipsum',
    'dummy',
    'todo',
    'tbd',
    'placeholder',
    'drag ',
    'drop ',
    'click ',
    'yes / no',
)
FORBIDDEN_MICROSOFT_COMPANIES = (
    'contoso',
    'fabrikam',
    'adventureworks',
    'adventure works',
    'northwind',
    'litware',
    'tailwind traders',
    'wide world importers',
    'woodgrove',
    'adatum',
    'vanarsdel',
    'coho winery',
    'trey research',
    'fourth coffee',
    'alpine ski house',
    'relecloud',
    'humongous insurance',
    'proseware',
    "margie's travel",
    'wingtip toys',
)

WORD_RE = re.compile(r'[a-z]{4,}')


def _stem_words(text):
    if text.startswith('Case study — ') and ':' in text:
        text = text.split(':', 1)[1]
    return set(WORD_RE.findall(text.casefold()))


def validate_csv_file(path: Path, expected_rows: int = ITEM_TOTAL, check_balance: bool = True):
    errors = []
    raw = path.read_bytes()
    if not raw.startswith(b'\xef\xbb\xbf'):
        errors.append(f'{path.name}: missing UTF-8 BOM')
    if b'\r\n' in raw:
        errors.append(f'{path.name}: contains CRLF line endings; expected LF')
    with path.open('r', encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != HEADER:
            errors.append(f'{path.name}: header mismatch {reader.fieldnames}')
            return errors, {}
        rows = list(reader)
    if len(rows) != expected_rows:
        errors.append(f'{path.name}: expected {expected_rows} rows, got {len(rows)}')

    domain_counts = Counter()
    type_counts = Counter()
    slot_counts = Counter()
    valid_domains = set(DOMAINS.values())

    for idx, row in enumerate(rows, 1):
        q = row['Question']
        qtype = row['Question Type']
        domain = row['Domain']
        overall = row['Overall Explanation']
        if qtype not in ALLOWED_TYPES:
            errors.append(f'{path.name} Q{idx}: invalid Question Type {qtype!r}')
        type_counts[qtype] += 1
        if domain not in valid_domains:
            errors.append(f'{path.name} Q{idx}: invalid Domain {domain!r}')
        domain_counts[domain] += 1
        if not q or len(q) > 1000:
            errors.append(f'{path.name} Q{idx}: Question length {len(q)} out of 1..1000 bounds')
        if not overall or len(overall) > 1500:
            errors.append(f'{path.name} Q{idx}: Overall Explanation length {len(overall)} out of 1..1500 bounds')

        opts, exps = [], []
        seen_empty = False
        for slot in range(1, 7):
            opt = row[f'Answer Option {slot}']
            exp = row[f'Explanation {slot}']
            if opt:
                if seen_empty:
                    errors.append(f'{path.name} Q{idx}: non-contiguous Answer Option at slot {slot}')
                opts.append(opt)
                if not exp:
                    errors.append(f'{path.name} Q{idx}: missing Explanation {slot}')
                if len(opt) > 280:
                    errors.append(f'{path.name} Q{idx}: Option {slot} length {len(opt)} > 280')
                if len(exp) > 650:
                    errors.append(f'{path.name} Q{idx}: Explanation {slot} length {len(exp)} > 650')
                exps.append(exp)
            else:
                seen_empty = True
                if exp:
                    errors.append(f'{path.name} Q{idx}: Explanation {slot} populated for empty option')

        lowered = [o.casefold() for o in opts]
        if len(lowered) != len(set(lowered)):
            errors.append(f'{path.name} Q{idx}: duplicate option labels within row')

        ans_parts = [x.strip() for x in row['Correct Answers'].split(',') if x.strip()]
        try:
            ans_nums = [int(x) for x in ans_parts]
        except ValueError:
            errors.append(f'{path.name} Q{idx}: non-integer Correct Answers {row["Correct Answers"]!r}')
            continue
        if any(a < 1 or a > len(opts) for a in ans_nums) or len(ans_nums) != len(set(ans_nums)):
            errors.append(f'{path.name} Q{idx}: out-of-range or duplicate Correct Answers {ans_nums}')
        if ans_nums != sorted(ans_nums):
            errors.append(f'{path.name} Q{idx}: Correct Answers not sorted ascending {ans_nums}')

        if qtype == 'multiple-choice':
            if len(opts) != 4 or len(ans_nums) != 1:
                errors.append(f'{path.name} Q{idx}: multiple-choice requires 4 options and 1 answer')
            else:
                slot_counts[ans_nums[0]] += 1
        elif qtype == 'multi-select':
            if len(opts) not in (5, 6) or len(ans_nums) not in (2, 3):
                errors.append(f'{path.name} Q{idx}: multi-select requires 5-6 options and 2-3 answers')

        haystack = ' '.join([q, overall] + opts + exps).casefold()
        for phrase in BANNED_PHRASES:
            if phrase in haystack:
                errors.append(f'{path.name} Q{idx}: contains banned phrase {phrase!r}')
        for company in FORBIDDEN_MICROSOFT_COMPANIES:
            if company in haystack:
                errors.append(f'{path.name} Q{idx}: contains forbidden Microsoft company {company!r}')

    if check_balance:
        expected_domains = {DOMAINS[d]: cnt for d, cnt in ALLOCATIONS[1].items()}
        if dict(domain_counts) != expected_domains:
            errors.append(f'{path.name}: domain mismatch {dict(domain_counts)} vs {expected_domains}')
        if dict(type_counts) != EXPORT_PLAN:
            errors.append(f'{path.name}: type mix mismatch {dict(type_counts)} vs {EXPORT_PLAN}')
        expected_per_slot = EXPORT_PLAN['multiple-choice'] // 4
        if dict(slot_counts) != {1: expected_per_slot, 2: expected_per_slot, 3: expected_per_slot, 4: expected_per_slot}:
            errors.append(f'{path.name}: uneven A/B/C/D slot distribution {dict(slot_counts)}')

    stats = {
        'rows': len(rows),
        'domains': dict(domain_counts),
        'types': dict(type_counts),
        'single_slots': {chr(64 + k): slot_counts[k] for k in sorted(slot_counts)},
        'max_question_chars': max((len(r['Question']) for r in rows), default=0),
        'code_fills': sum(1 for r in rows if '____' in r['Question']),
        'proposed_solutions': sum(1 for r in rows if 'Proposed solution:' in r['Question']),
    }
    return errors, stats


def check_jaccard(threshold: float = 0.72):
    errors = []
    all_items = [(r['id'], _stem_words(r['question'])) for rs in BANK.values() for r in rs]
    max_sim = 0.0
    max_pair = None
    for i in range(len(all_items)):
        id_a, wa = all_items[i]
        if not wa:
            continue
        for j in range(i + 1, len(all_items)):
            id_b, wb = all_items[j]
            if not wb:
                continue
            inter = len(wa & wb)
            if inter == 0:
                continue
            sim = inter / len(wa | wb)
            if sim > max_sim:
                max_sim = sim
                max_pair = (id_a, id_b)
            if sim > threshold:
                errors.append(f'High stem similarity {sim:.3f} (> {threshold}) between {id_a} and {id_b}')
    return errors, round(max_sim, 3), max_pair


def write_reports(report_data):
    bp_dir = ROOT / '02-curriculum'
    bp_dir.mkdir(parents=True, exist_ok=True)
    lines = [
        '# Official Exam DP-300 Blueprint Alignment & Telemetry (`October 27, 2026` Study Guide)',
        '',
        '| Domain # | Official Functional Group | Published Weight | Items / Set | Multi-Select / Set | 6-Set Total |',
        '| :---: | :--- | :---: | :---: | :---: | :---: |',
    ]
    for d in range(1, 6):
        lo, hi = OFFICIAL_RANGES[d]
        cnt = ALLOCATIONS[1][d]
        ms = MULTI_PLAN[d]
        lines.append(f'| `{d}` | **{DOMAINS[d]}** | `{lo}–{hi}%` | `{cnt}` (`{cnt}%`) | `{ms}` | `{cnt * 6}` |')
    lines += [
        f'| **Total** | **All 5 Functional Groups · {len(SKILLS)} Study-Map Skills** | **100%** | **100** | **16** | **600** |',
        '',
        '## Per-Set Telemetry',
        '',
        '| Set | Theme | MC (`S`+`O`) | MS (`M2`+`M3`) | `____` Fills | `Proposed solution:` | Case Items | Max Embedded Q Chars |',
        '| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |',
    ]
    for n in range(1, 7):
        s_std = report_data['sets'][f'set-{n}']['standard']
        s_emb = report_data['sets'][f'set-{n}']['case_embedded']
        lines.append(
            f'| `{n}` | {SUBTITLES[n]} | `{s_std["types"]["multiple-choice"]}` (`21/21/21/21`) | '
            f'`{s_std["types"]["multi-select"]}` | `{s_std["code_fills"]}` | `{s_std["proposed_solutions"]}` | '
            f'`{CASE_STUDIES * CASE_SIZE}` | `{s_emb["max_question_chars"]}` |'
        )
    lines += [
        '',
        '## Bank-Wide Uniqueness & Term Coverage',
        '',
        f'- **Total authored questions:** `{report_data["total_questions"]}` (`0` duplicate stems, `0` duplicate overall explanations)',
        f'- **Canonical `TERMS` exercised:** `{report_data["terms_used"]} / {report_data["terms_total"]}` (`100.0%`)',
        f'- **Max pairwise stem Jaccard similarity:** `{report_data["max_jaccard"]}` (`{report_data["max_jaccard_pair"][0]}` vs `{report_data["max_jaccard_pair"][1]}`, ceiling `<= 0.72`)',
        f'- **Original enterprise case studies:** `{len(CASES)}` (`4` × `3` questions per exam; `0` Microsoft fictional company names)',
        '',
    ]
    (bp_dir / 'blueprint-alignment.md').write_text('\n'.join(lines), encoding='utf-8')
    (HERE / 'SUMMARY.md').write_text('\n'.join(lines), encoding='utf-8')
    (HERE / 'validation-report.json').write_text(json.dumps(report_data, indent=2) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description='Validate DP-300 course CSVs and question bank.')
    parser.add_argument('--report', action='store_true', help='Write SUMMARY.md, blueprint-alignment.md, and validation-report.json')
    args = parser.parse_args()

    errors = []
    used_terms = {k for rs in BANK.values() for r in rs for k in r['keys']}
    unused_terms = sorted(set(TERMS) - used_terms)
    if unused_terms:
        errors.append(f'Unused TERMS ({len(unused_terms)}): {unused_terms}')

    labels = [v[0].casefold() for v in TERMS.values()]
    if len(labels) != len(set(labels)):
        dups = [lbl for lbl, c in Counter(labels).items() if c > 1]
        errors.append(f'Duplicate case-insensitive option labels in TERMS: {dups}')

    overall_seen = set()
    set_reports = {}
    for n in range(1, 7):
        std_path = ROOT / f'03-practice-sets/set-{n}/practice-set-{n}.csv'
        emb_path = ROOT / f'03-practice-sets/set-{n}/case-embedded-set-{n}.csv'
        e1, s1 = validate_csv_file(std_path, ITEM_TOTAL, check_balance=True)
        e2, s2 = validate_csv_file(emb_path, ITEM_TOTAL, check_balance=True)
        errors.extend(e1)
        errors.extend(e2)
        with std_path.open('r', encoding='utf-8-sig', newline='') as f:
            for idx, r in enumerate(csv.DictReader(f), 1):
                ov = r['Overall Explanation'].strip().casefold()
                if ov in overall_seen:
                    errors.append(f'practice-set-{n}.csv Q{idx}: duplicate Overall Explanation across bank')
                overall_seen.add(ov)
        set_reports[f'set-{n}'] = {'standard': s1, 'case_embedded': s2}

    sample_path = ROOT / '05-sample-upload/case-study-sample.csv'
    es, ss = validate_csv_file(sample_path, CASE_STUDIES * CASE_SIZE, check_balance=False)
    errors.extend(es)

    jac_errs, max_sim, max_pair = check_jaccard(0.72)
    errors.extend(jac_errs)

    if errors:
        for err in errors:
            print(f'ERROR: {err}', file=sys.stderr)
        sys.exit(1)

    report_data = {
        'exam': 'DP-300',
        'study_guide_date': '2026-10-27',
        'total_questions': sum(len(v) for v in BANK.values()),
        'terms_used': len(used_terms),
        'terms_total': len(TERMS),
        'max_jaccard': max_sim,
        'max_jaccard_pair': list(max_pair) if max_pair else [],
        'sample_rows': ss['rows'],
        'sets': set_reports,
    }
    if args.report:
        write_reports(report_data)
        print(
            f'Wrote {ROOT / "02-curriculum/blueprint-alignment.md"}, '
            f'{HERE / "SUMMARY.md"}, and {HERE / "validation-report.json"}'
        )
    print(
        f'OK: DP-300 validated — {report_data["total_questions"]} unique questions across 6 sets, '
        f'{len(used_terms)}/{len(TERMS)} terms used, max Jaccard {max_sim}'
    )


if __name__ == '__main__':
    main()
