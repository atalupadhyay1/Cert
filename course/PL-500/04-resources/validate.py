#!/usr/bin/env python3
"""Validate all PL-500 practice-set CSVs, case-embedded CSVs, sample CSV, and bank invariants."""
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
    CREDENTIAL_TITLE,
    DOMAINS,
    EXAM_CODE,
    EXAM_TITLE,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    PREREQUISITES,
    PROPOSED_SOL_FLOOR,
    RETIREMENT_DATE,
    SKILL_PLAN,
    SKILLS,
    STUDY_GUIDE_DATE,
    SUCCESSOR_EXAM,
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
    'sample question',
)

MS_BANNED_COMPANIES = (
    'contoso',
    'litware',
    'vanarsdel',
    'wide world importers',
    'coho winery',
    'fabrikam',
    'adatum',
    'tailwind traders',
    'adventureworks',
    'adventure works',
    'northwind',
    'woodgrove',
    'lamna healthcare',
    'trey research',
    'alpine ski house',
)

WORD_RE = re.compile(r'[a-z]{4,}')


def _stem_words(text: str) -> set[str]:
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
                if len(exp) > 600:
                    errors.append(f'{path.name} Q{idx}: Explanation {slot} length {len(exp)} > 600')
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
        for ms_co in MS_BANNED_COMPANIES:
            if ms_co in haystack:
                errors.append(f'{path.name} Q{idx}: contains copyrighted Microsoft sample company {ms_co!r}')

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
    return errors, round(max_sim, 4), max_pair


def main():
    parser = argparse.ArgumentParser(description='Validate PL-500 course CSVs and question bank.')
    parser.add_argument('--report', type=Path, help='Optional JSON report output path')
    args = parser.parse_args()

    errors = []
    set_reports = {}

    all_stems = [r['question'].strip().casefold() for rs in BANK.values() for r in rs]
    if len(all_stems) != len(set(all_stems)):
        errors.append('Duplicate question stems found inside PL-500 bank')

    used_terms = {k for rs in BANK.values() for r in rs for k in r['keys']}
    unused_terms = sorted(set(TERMS) - used_terms)
    if unused_terms:
        errors.append(f'Unused TERMS keys ({len(unused_terms)}): {unused_terms[:10]}')

    for n in range(1, 7):
        records = BANK.get(n, [])
        if Counter(r['task'] for r in records) != Counter(SKILL_PLAN):
            errors.append(f'Exam {n}: SKILL_PLAN mismatch')
        if Counter(r['kind'] for r in records) != Counter(KIND_PLAN):
            errors.append(f'Exam {n}: KIND_PLAN mismatch')
        if Counter(r['domain'] for r in records if r['kind'] in ('M2', 'M3')) != Counter(MULTI_PLAN):
            errors.append(f'Exam {n}: MULTI_PLAN mismatch')
        if sum(1 for r in records if '____' in r['question']) < CODE_FILL_FLOOR:
            errors.append(f'Exam {n}: fewer than {CODE_FILL_FLOOR} ____ items')
        if sum(1 for r in records if 'Proposed solution:' in r['question']) < PROPOSED_SOL_FLOOR:
            errors.append(f'Exam {n}: fewer than {PROPOSED_SOL_FLOOR} Proposed solution: items')
        cases = Counter(case_name(r['question']) for r in records if case_name(r['question']))
        if len(cases) != CASE_STUDIES or set(cases.values()) != {CASE_SIZE}:
            errors.append(f'Exam {n}: invalid case block counts {dict(cases)}')

        p_csv = ROOT / f'03-practice-sets/set-{n}/practice-set-{n}.csv'
        e_csv = ROOT / f'03-practice-sets/set-{n}/case-embedded-set-{n}.csv'
        e1, s1 = validate_csv_file(p_csv, ITEM_TOTAL, check_balance=True)
        e2, s2 = validate_csv_file(e_csv, ITEM_TOTAL, check_balance=True)
        errors.extend(e1)
        errors.extend(e2)
        set_reports[f'set-{n}'] = {
            'practice_csv': s1,
            'case_embedded_csv': s2,
            'code_completion_items': sum(1 for r in records if '____' in r['question']),
            'proposed_solution_items': sum(1 for r in records if 'Proposed solution:' in r['question']),
            'cases': list(cases.keys()),
        }

    sample_csv = ROOT / '05-sample-upload/case-study-sample.csv'
    if sample_csv.is_file():
        es, ss = validate_csv_file(sample_csv, CASE_STUDIES * CASE_SIZE, check_balance=False)
        errors.extend(es)
        set_reports['sample'] = ss
    else:
        errors.append('Missing 05-sample-upload/case-study-sample.csv')

    j_errors, max_jaccard, max_pair = check_jaccard(0.72)
    errors.extend(j_errors)

    report = {
        'exam': EXAM_CODE,
        'title': EXAM_TITLE,
        'credential': CREDENTIAL_TITLE,
        'study_guide_baseline': STUDY_GUIDE_DATE,
        'retirement_and_transition': f'Exam {EXAM_CODE} retired {RETIREMENT_DATE}; {SUCCESSOR_EXAM}',
        'prerequisites': PREREQUISITES,
        'total_questions': sum(len(v) for v in BANK.values()),
        'sets': 6,
        'questions_per_set': ITEM_TOTAL,
        'skills_covered': len(SKILLS),
        'domain_allocation_per_set': {DOMAINS[d]: cnt for d, cnt in ALLOCATIONS[1].items()},
        'export_type_plan': EXPORT_PLAN,
        'total_terms': len(TERMS),
        'used_terms': len(used_terms),
        'unused_terms': len(unused_terms),
        'total_cases': len(CASES),
        'max_stem_jaccard': max_jaccard,
        'max_jaccard_pair': list(max_pair) if max_pair else None,
        'set_reports': set_reports,
        'error_count': len(errors),
        'errors': errors,
    }

    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        print(f'Wrote validation report to {args.report}')

    if errors:
        for err in errors[:30]:
            print(f'ERROR: {err}', file=sys.stderr)
        sys.exit(1)
    print(f'OK: 600 PL-500 questions, 13 CSV files, {len(used_terms)}/{len(TERMS)} terms used, max Jaccard {max_jaccard}')


if __name__ == '__main__':
    main()
