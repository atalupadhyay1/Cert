#!/usr/bin/env python3
"""Offline export checks for the Professional Cloud Security Engineer practice sets.

These checks confirm structural consistency, not independent factual or
difficulty certification against the live Google exam.
"""
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

from build import (ALLOWED_TYPES, DOMAINS, EXPORT_PLAN, GUIDE, HEADER, ROOT,
                   TYPE_PLAN, make_rows)

TYPE_TOTAL = sum(TYPE_PLAN.values())


def normalize(text):
    return re.sub(r'\W+', ' ', text.casefold()).strip()


def answer_indices(row):
    raw = row.get('Correct Answers', '')
    if not re.fullmatch(r'[1-6](,[1-6]){0,2}', raw):
        return None
    values = [int(x) for x in raw.split(',')]
    if values != sorted(set(values)):
        return None
    return values


def validate_rows(rows, expected=None):
    errors = []
    if len(rows) != TYPE_TOTAL:
        errors.append(f'Expected {TYPE_TOTAL} rows, found {len(rows)}')
    if any(r.get('Domain') not in DOMAINS.values() for r in rows):
        errors.append('Unknown official domain label')
    if expected is not None and Counter(r.get('Domain') for r in rows) != Counter(r.get('Domain') for r in expected):
        errors.append('Domain counts differ from the authored blueprint allocation')
    types = Counter(r.get('Question Type') for r in rows)
    if set(types) - set(ALLOWED_TYPES):
        errors.append(f'Question Type must be one of {ALLOWED_TYPES}; found {sorted(set(types) - set(ALLOWED_TYPES))}')
    if types != Counter(EXPORT_PLAN):
        errors.append(f'Item-type mix {dict(types)} does not match {EXPORT_PLAN}')

    seen = set()
    positions = Counter()
    for n, row in enumerate(rows, 1):
        tag = f'Question {n}'
        internal = {'_stem'}
        if set(HEADER) - set(row) or set(row) - set(HEADER) - internal:
            errors.append(f'{tag}: unexpected or missing columns')
        question = normalize(row.get('Question', ''))
        if not question or question in seen:
            errors.append(f'{tag}: empty or duplicate question')
        seen.add(question)

        qtype = row.get('Question Type')
        options = [row.get(f'Answer Option {i}', '').strip() for i in range(1, 7)]
        populated = [x for x in options if x]
        expected_options = 5 if qtype == 'multi-select' else 4
        if len(populated) != expected_options or any(not x for x in options[:expected_options]) or any(options[expected_options:]):
            errors.append(f'{tag}: {qtype} needs exactly {expected_options} contiguous options')
        if len({x.casefold() for x in populated}) != len(populated):
            errors.append(f'{tag}: duplicate option text')

        for i in range(1, 7):
            if bool(options[i - 1]) != bool(row.get(f'Explanation {i}', '').strip()):
                errors.append(f'{tag}: option/explanation mismatch at {i}')

        indices = answer_indices(row)
        if indices is None:
            errors.append(f'{tag}: invalid Correct Answers value {row.get("Correct Answers")!r}')
        else:
            if any(i > expected_options for i in indices):
                errors.append(f'{tag}: answer index points past the last option')
            if qtype == 'multi-select':
                if len(indices) not in (2, 3):
                    errors.append(f'{tag}: multi-select needs two or three correct indices')
                else:
                    word = {2: 'two', 3: 'three'}[len(indices)]
                    if f'Select {word}' not in row.get('Question', ''):
                        errors.append(f'{tag}: multi-select must state "Select {word}"')
            else:
                if len(indices) != 1:
                    errors.append(f'{tag}: {qtype} needs exactly one correct index')
                if indices[0] > 4:
                    errors.append(f'{tag}: single-answer key must fall in slots 1-4')
                positions[indices[0]] += 1
            if '→' in ''.join(populated):
                errors.append(f'{tag}: no sequencing options are published for this exam')

        overall = row.get('Overall Explanation', '')
        if GUIDE not in overall:
            errors.append(f'{tag}: missing official exam-guide reference')
        if 'case study' in row.get('Question', '').casefold() or 'case study' in overall.casefold():
            errors.append(f'{tag}: this exam publishes no case-study component')
        if expected is not None and n <= len(expected):
            wanted = {k: expected[n - 1][k] for k in HEADER}
            if {k: row.get(k) for k in HEADER} != wanted:
                errors.append(f'{tag}: differs from authored source/build output')

    singles = sum(positions.values())
    if singles != TYPE_PLAN['multiple-choice']:
        errors.append(f'Expected {TYPE_PLAN["multiple-choice"]} single-answer keys, counted {singles}')
    elif max(positions.values()) - min(positions.values()) > 1:
        errors.append(f'Single-answer slots are unbalanced: {dict(positions)}')
    if positions.get(5) or positions.get(6):
        errors.append('Single-answer key must fall in slots 1-4')
    return errors


def validate_files(paths):
    failures, summaries, all_questions = [], [], []
    for path in paths:
        match = re.fullmatch(r'practice-set-([1-6])\.csv', path.name)
        number = int(match[1]) if match else None
        with path.open(encoding='utf-8-sig', newline='') as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames
            rows = list(reader)
        errors = [] if header == HEADER else ['CSV header/order differs from 17-column template']
        errors.extend(validate_rows(rows, make_rows(number)[0] if number else None))
        failures.extend(f'{path.name}: {e}' for e in errors)
        all_questions.extend(normalize(r.get('Question', '')) for r in rows)
        summaries.append(dict(
            file=str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
            questions=len(rows), status='FAIL' if errors else 'PASS',
            types=dict(Counter(r.get('Question Type') for r in rows)),
            domains=dict(Counter(r.get('Domain') for r in rows))))
    if len(set(all_questions)) != len(all_questions):
        failures.append('Duplicate normalized question wording across supplied files')
    return failures, summaries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='*', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    paths = args.files or sorted((ROOT / '03-practice-sets').glob('set-*/practice-set-*.csv'))
    if not paths:
        parser.error('No CSV files found')
    failures, summaries = validate_files(paths)
    if not args.files and len(paths) != 6:
        failures.append('Expected six CSV files')
    report = dict(
        status='FAIL' if failures else 'PASS', sets=len(paths),
        total_questions=sum(x['questions'] for x in summaries),
        checks=['17-column header', f'{TYPE_TOTAL} items per set',
                'blueprint domain allocation per set (25 / 22 / 23 / 19 / 11)',
                'four-option single-answer items',
                'Question Type restricted to multiple-choice or multi-select',
                'five-option multi-select items with stated selection count',
                'two correct indices for multi-select', 'per-option explanations',
                'official exam-guide references', 'source consistency',
                'no case-study wording', 'no sequencing items',
                'cross-exam near-duplicate stems (token overlap <= 0.72)',
                'bank-wide stem uniqueness',
                'normalized duplicate wording', 'balanced single-answer slots'],
        limitations=['No independent factual certification',
                     'No difficulty calibration against the live exam',
                     'No exhaustive semantic duplicate detection',
                     'No Udemy account import performed',
                     'Lab tasks and any interactive item format are not reproduced',
                     'No continuous live URL verification'],
        files=summaries, errors=failures)
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    for entry in summaries:
        print(f"{entry['status']}: {entry['file']} — {entry['questions']} questions")
    if failures:
        for failure in failures:
            print('ERROR:', failure)
        raise SystemExit(1)
    print(f"PASS: {report['sets']} sets / {report['total_questions']} questions")


if __name__ == '__main__':
    main()
