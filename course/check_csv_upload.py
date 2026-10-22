#!/usr/bin/env python3
"""Pre-flight check for a Udemy bulk-upload CSV.

Run this before uploading any practice-set CSV. It reports the failures the
Udemy importer reports, using the same row numbering the importer uses (data
rows, with the header excluded), plus a few structural checks of our own.

Usage:
    python course/check_csv_upload.py course/AI-103/03-practice-sets/set-1/practice-set-1.csv
    python course/check_csv_upload.py --all

Exit code 0 means the file is shaped the way the importer expects.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ALLOWED_TYPES = ('multiple-choice', 'multi-select')
EXPECTED_HEADER = ['Question', 'Question Type']
for _i in range(1, 7):
    EXPECTED_HEADER += [f'Answer Option {_i}', f'Explanation {_i}']
EXPECTED_HEADER += ['Correct Answers', 'Overall Explanation', 'Domain']


def check(path):
    problems = []
    warnings = []
    with path.open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        header = reader.fieldnames or []
        rows = list(reader)

    if header != EXPECTED_HEADER:
        problems.append(f'header mismatch: expected {EXPECTED_HEADER}, found {header}')
    if not rows:
        problems.append('file has no data rows')
        return problems, warnings

    bad_type = [(n, r.get('Question Type')) for n, r in enumerate(rows, 1)
                if r.get('Question Type') not in ALLOWED_TYPES]
    if bad_type:
        rows_text = ', '.join(str(n) for n, _ in bad_type)
        values = sorted({str(v) for _, v in bad_type})
        problems.append(
            f"'Question Type' must be multiple-choice or multi-select. "
            f'It is invalid in rows {rows_text} (found {", ".join(values)})')

    seen = {}
    for n, row in enumerate(rows, 1):
        qtype = row.get('Question Type')
        if not (row.get('Question') or '').strip():
            problems.append(f'row {n}: empty question')
        if not (row.get('Overall Explanation') or '').strip():
            problems.append(f'row {n}: empty overall explanation')
        if not (row.get('Domain') or '').strip():
            problems.append(f'row {n}: empty domain')
        options = [row.get(f'Answer Option {i}', '').strip() for i in range(1, 7)]
        populated = [x for x in options if x]
        if len(populated) < 2:
            problems.append(f'row {n}: needs at least two options, found {len(populated)}')
        if options[:len(populated)] != populated:
            problems.append(f'row {n}: options must be contiguous, starting at Answer Option 1')
        for i in range(1, 7):
            has_option = bool((row.get(f'Answer Option {i}') or '').strip())
            has_explanation = bool((row.get(f'Explanation {i}') or '').strip())
            if has_option != has_explanation:
                problems.append(f'row {n}: option {i} and explanation {i} must both be present or both empty')
        raw = (row.get('Correct Answers') or '').strip()
        if not re.fullmatch(r'[1-6](,[1-6]){0,5}', raw):
            problems.append(f'row {n}: invalid Correct Answers value {raw!r}')
            continue
        indices = [int(x) for x in raw.split(',')]
        if indices != sorted(set(indices)):
            problems.append(f'row {n}: Correct Answers must be sorted and unique')
        if any(i > len(populated) for i in indices):
            problems.append(f'row {n}: Correct Answers points past the last option')
        if qtype == 'multi-select':
            if len(indices) < 2:
                problems.append(f'row {n}: multi-select needs at least two correct indices')
            else:
                word = {2: 'two', 3: 'three', 4: 'four', 5: 'five'}.get(len(indices))
                if word and f'Select {word}' not in (row.get('Question') or ''):
                    warnings.append(f'row {n}: stem does not state "Select {word}"')
        elif qtype == 'multiple-choice' and len(indices) != 1:
            problems.append(f'row {n}: multiple-choice needs exactly one correct index')
        key = re.sub(r'[^a-z0-9]+', '', (row.get('Question') or '').casefold())
        if key in seen:
            warnings.append(f'row {n}: duplicate question text (also row {seen[key]})')
        seen[key] = n
    return problems, warnings


def main(argv):
    if '--all' in argv:
        targets = sorted(ROOT.glob('*/03-practice-sets/set-*/practice-set-*.csv'))
    else:
        targets = [Path(a) for a in argv if not a.startswith('-')]
    if not targets:
        print(__doc__.strip().splitlines()[0])
        return 2
    failures = 0
    for path in targets:
        if not path.is_file():
            print(f'MISSING: {path}')
            failures += 1
            continue
        problems, warnings = check(path)
        if problems:
            failures += 1
            print(f'FAIL: {path}')
            for problem in problems:
                print(f'  - {problem}')
        else:
            print(f'OK:   {path}')
        if warnings:
            print(f'  notes for {path.name} (not importer blockers):')
            for warning in warnings:
                print(f'  - {warning}')
    print(f'\n{len(targets) - failures}/{len(targets)} file(s) ready to upload.')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
