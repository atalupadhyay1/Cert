#!/usr/bin/env python3
"""Validate all PL-900 practice-set CSVs, sample-upload CSV, and bank invariants."""
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
    COMPLETION_FLOOR,
    DOMAINS,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    PROPOSED_SOL_FLOOR,
    SKILL_PLAN,
    TERMS,
)
from build import ALLOWED_TYPES, EXPORT_PLAN, HEADER  # noqa: E402

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
    'case study —',
)

FORBIDDEN_MS_NAMES = (
    'contoso', 'litware', 'vanarsdel', 'wide world importers', 'coho winery',
    'fabrikam', 'adatum', 'tailwind traders', 'adventureworks', 'adventure works',
    'northwind', 'woodgrove', 'lamna', 'trey research', 'alpine ski house',
)

WORD_RE = re.compile(r'[a-z]{4,}')


def _stem_words(text: str) -> set[str]:
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
        for ms_name in FORBIDDEN_MS_NAMES:
            if ms_name in haystack:
                errors.append(f'{path.name} Q{idx}: contains Microsoft named scenario {ms_name!r}')

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
        'file': path.relative_to(ROOT).as_posix(),
        'rows': len(rows),
        'domains': dict(domain_counts),
        'types': dict(type_counts),
        'single_slots': {chr(64 + k): slot_counts[k] for k in sorted(slot_counts)},
        'max_question_chars': max((len(r['Question']) for r in rows), default=0),
        'max_option_chars': max(
            (len(r[f'Answer Option {s}']) for r in rows for s in range(1, 7) if r[f'Answer Option {s}']),
            default=0,
        ),
        'max_overall_chars': max((len(r['Overall Explanation']) for r in rows), default=0),
    }
    return errors, stats


def validate_files(paths: list[Path]):
    all_errors = []
    summaries = []
    for path in paths:
        errs, stats = validate_csv_file(path, ITEM_TOTAL, check_balance=True)
        all_errors.extend(errs)
        summaries.append(stats)
    return all_errors, summaries


def validate_bank():
    errors = []
    seen_stems = {}
    used_terms = set()

    for n in range(1, 7):
        records = BANK[n]
        if len(records) != ITEM_TOTAL:
            errors.append(f'Set {n}: expected {ITEM_TOTAL} records, got {len(records)}')
            continue
        dom_c = Counter(r['domain'] for r in records)
        if dict(dom_c) != ALLOCATIONS[n]:
            errors.append(f'Set {n}: domain counts {dict(dom_c)} != {ALLOCATIONS[n]}')
        skill_c = Counter(r['task'] for r in records)
        if dict(skill_c) != SKILL_PLAN:
            diff = {k: (skill_c[k], SKILL_PLAN[k]) for k in SKILL_PLAN if skill_c[k] != SKILL_PLAN[k]}
            errors.append(f'Set {n}: skill plan mismatch {diff}')
        kind_c = Counter(r['kind'] for r in records)
        if dict(kind_c) != KIND_PLAN:
            errors.append(f'Set {n}: kind counts {dict(kind_c)} != {KIND_PLAN}')
        ms_dom = Counter(r['domain'] for r in records if r['kind'] in ('M2', 'M3'))
        if dict(ms_dom) != MULTI_PLAN:
            errors.append(f'Set {n}: multi-select per domain {dict(ms_dom)} != {MULTI_PLAN}')

        completions = sum(1 for r in records if '____' in r['question'])
        if completions < COMPLETION_FLOOR:
            errors.append(f'Set {n}: completion items {completions} < {COMPLETION_FLOOR}')
        prop_sols = sum(1 for r in records if 'Proposed solution:' in r['question'])
        if prop_sols < PROPOSED_SOL_FLOOR:
            errors.append(f'Set {n}: Proposed solution items {prop_sols} < {PROPOSED_SOL_FLOOR}')

        for r in records:
            if r['question'].startswith('Case study —'):
                errors.append(f'{r["id"]}: PL-900 is a Fundamentals exam with no case studies')
            norm_q = ' '.join(r['question'].casefold().split())
            if norm_q in seen_stems:
                errors.append(f'Duplicate stem between {seen_stems[norm_q]} and {r["id"]}')
            seen_stems[norm_q] = r['id']

            for k in r['keys']:
                if k not in TERMS:
                    errors.append(f'{r["id"]}: missing term key {k!r}')
                else:
                    used_terms.add(k)
            if len(r['keys']) != len(set(r['keys'])):
                errors.append(f'{r["id"]}: duplicate term key inside question')

            if r['kind'] in ('S', 'O') and (len(r['answers']) != 1 or len(r['distractors']) != 3):
                errors.append(f'{r["id"]}: kind {r["kind"]} must have 1 answer and 3 distractors')
            elif r['kind'] == 'M2' and (len(r['answers']) != 2 or len(r['distractors']) != 3):
                errors.append(f'{r["id"]}: M2 must have 2 answers and 3 distractors (5 options)')
            elif r['kind'] == 'M3' and (len(r['answers']) != 3 or len(r['distractors']) != 3):
                errors.append(f'{r["id"]}: M3 must have 3 answers and 3 distractors (6 options)')
            if r['kind'] == 'M2' and 'Select two.' not in r['question']:
                errors.append(f'{r["id"]}: M2 stem must state "Select two."')
            if r['kind'] == 'M3' and 'Select three.' not in r['question']:
                errors.append(f'{r["id"]}: M3 stem must state "Select three."')

    unused = sorted(set(TERMS) - used_terms)
    if unused:
        errors.append(f'Unused TERMS keys ({len(unused)}): {unused[:10]}')

    # Check zero exact normalized stem overlap with sibling Microsoft courses
    norm_alnum = lambda s: ''.join(c for c in s.casefold() if c.isalnum())
    my_norms = {norm_alnum(r['question']): r['id'] for rs in BANK.values() for r in rs}
    for sib in ('PL-400', 'AZ-204', 'AZ-400', 'AZ-401', 'DP-600'):
        qdir = ROOT.parent / sib / '04-resources' / 'questions'
        if qdir.is_dir():
            for qfile in qdir.glob('*.txt'):
                for line in qfile.read_text(encoding='utf-8').splitlines():
                    if line.strip() and not line.startswith('#'):
                        parts = [p.replace('\\|', '|').strip() for p in re.split(r'(?<!\\)\|', line)]
                        if len(parts) == 6 and norm_alnum(parts[4]) in my_norms:
                            errors.append(f'Exact stem overlap with {sib} on {my_norms[norm_alnum(parts[4])]}')

    return errors, len(used_terms)


def check_jaccard(limit: float = 0.72):
    items = []
    for n in range(1, 7):
        for r in BANK[n]:
            items.append((r['id'], _stem_words(r['question'])))
    errors = []
    max_sim = 0.0
    max_pair = ('', '')
    for i in range(len(items)):
        id1, w1 = items[i]
        if not w1:
            continue
        for j in range(i + 1, len(items)):
            id2, w2 = items[j]
            if not w2:
                continue
            inter = len(w1 & w2)
            if inter == 0:
                continue
            sim = inter / len(w1 | w2)
            if sim > max_sim:
                max_sim = sim
                max_pair = (id1, id2)
            if sim > limit:
                errors.append(f'High stem similarity {sim:.3f} between {id1} and {id2}')
    return errors, round(max_sim, 4), max_pair


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', action='store_true', help='Write validation-report.json')
    args = parser.parse_args()

    all_errors = []
    bank_errs, used_term_count = validate_bank()
    all_errors.extend(bank_errs)

    jac_errs, max_sim, max_pair = check_jaccard(0.72)
    all_errors.extend(jac_errs)

    csvs = [ROOT / f'03-practice-sets/set-{n}/practice-set-{n}.csv' for n in range(1, 7)]
    for p in csvs:
        if not p.exists():
            all_errors.append(f'Missing CSV: {p}')
    present_csvs = [p for p in csvs if p.exists()]
    csv_errs, summaries = validate_files(present_csvs)
    all_errors.extend(csv_errs)

    sample_path = ROOT / '05-sample-upload/sample-upload.csv'
    sample_stats = {}
    if not sample_path.exists():
        all_errors.append('Missing sample CSV: 05-sample-upload/sample-upload.csv')
    else:
        s_errs, sample_stats = validate_csv_file(sample_path, 10, check_balance=False)
        all_errors.extend(s_errs)

    report = {
        'exam': 'PL-900',
        'title': 'Microsoft Power Platform Fundamentals',
        'study_guide_date': 'July 24, 2026',
        'status': 'PASS' if not all_errors else 'FAIL',
        'sets': 6,
        'total_questions': sum(len(BANK[n]) for n in range(1, 7)),
        'case_studies': 0,
        'terms_defined': len(TERMS),
        'terms_used': used_term_count,
        'max_stem_jaccard': max_sim,
        'max_stem_pair': list(max_pair),
        'files': summaries,
        'sample_file': sample_stats,
        'error_count': len(all_errors),
        'errors': all_errors,
    }
    if args.report:
        out = HERE / 'validation-report.json'
        out.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        print(f'Wrote {out.relative_to(ROOT)}')

    if all_errors:
        for e in all_errors[:40]:
            print(f'ERROR: {e}', file=sys.stderr)
        sys.exit(1)

    print(
        f'PASS: 6 sets (600 questions), {len(present_csvs)} + 1 sample CSVs valid, '
        f'{used_term_count}/{len(TERMS)} terms exercised, max Jaccard={max_sim:.4f} {max_pair}'
    )


if __name__ == '__main__':
    main()
