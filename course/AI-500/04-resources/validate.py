#!/usr/bin/env python3
"""Offline structural and source-consistency checks. Not a factual-review oracle."""
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from bank import ITEMS, OVERRIDES, TERMS
from build import ROOT, HEADER, DOMAINS, WEIGHTS, make_rows


def validate_rows(rows, expected=None):
    errors = []
    if len(rows) != 100:
        errors.append(f'Expected 100 rows, found {len(rows)}')
    distribution = Counter(row.get('Domain') for row in rows)
    if distribution != Counter({DOMAINS[d]: n for d, n in WEIGHTS.items()}):
        errors.append('Domain distribution differs from 18/33/24/25')
    types = Counter(row.get('Question Type') for row in rows)
    if types != Counter({'multiple-choice': 90, 'multi-select': 10}):
        errors.append('Expected 90 multiple-choice and 10 multi-select')
    seen = set()
    positions = Counter()
    for n, row in enumerate(rows, 1):
        tag = f'Question {n}'
        if set(row) != set(HEADER):
            errors.append(f'{tag}: unexpected or missing columns')
        question = row.get('Question', '').strip()
        normalized = re.sub(r'\W+', ' ', question.casefold()).strip()
        if not normalized or normalized in seen:
            errors.append(f'{tag}: empty or duplicate question')
        seen.add(normalized)
        multi = row.get('Question Type') == 'multi-select'
        count = 5 if multi else 4
        options = [row.get(f'Answer Option {i}', '').strip() for i in range(1, 7)]
        if any(not s for s in options[:count]) or any(options[count:]):
            errors.append(f'{tag}: expected {count} contiguous options')
        if len(set(o.casefold() for o in options[:count])) != count:
            errors.append(f'{tag}: duplicate options')
        for i in range(1, 7):
            explanation = row.get(f'Explanation {i}', '').strip()
            if bool(options[i-1]) != bool(explanation):
                errors.append(f'{tag}: option/explanation mismatch at {i}')
        correct = row.get('Correct Answers', '')
        indices = [int(i) for i in correct.split(',')] if re.fullmatch(r'[1-6](,[1-6])*', correct) else []
        if len(indices) != (2 if multi else 1) or len(indices) != len(set(indices)) or any(i > count for i in indices):
            errors.append(f'{tag}: invalid correct-answer indices')
        if not multi and indices:
            positions[indices[0]] += 1
        if multi and '(Select TWO.)' not in question:
            errors.append(f'{tag}: missing selection count')
        if not row.get('Overall Explanation', '').strip() or not re.search(r'https://learn\.microsoft\.com/', row.get('Overall Explanation', '')):
            errors.append(f'{tag}: missing overall explanation or Microsoft Learn reference')
        if expected is not None and n <= len(expected) and row != expected[n-1]:
            errors.append(f'{tag}: differs from authored source/build output')
    if positions and (set(positions) != {1, 2, 3, 4} or max(positions.values()) - min(positions.values()) > 1):
        errors.append('Single-answer positions are not balanced')
    return errors


def validate_files(paths):
    failures, all_questions, summaries = [], [], []
    for path in paths:
        match = re.fullmatch(r'practice-set-([1-6])\.csv', path.name)
        number = int(match[1]) if match else None
        with path.open(encoding='utf-8-sig', newline='') as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames
            rows = list(reader)
        errors = [] if header == HEADER else ['CSV header/order differs from 17-column template']
        expected = make_rows(number)[0] if number else None
        errors.extend(validate_rows(rows, expected))
        failures.extend(f'{path.name}: {error}' for error in errors)
        all_questions.extend(re.sub(r'\W+', ' ', r.get('Question', '').casefold()).strip() for r in rows)
        summaries.append({'file': str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
                          'questions': len(rows), 'status': 'FAIL' if errors else 'PASS',
                          'types': dict(Counter(r.get('Question Type') for r in rows)),
                          'domains': dict(Counter(r.get('Domain') for r in rows))})
    if len(all_questions) != len(set(all_questions)):
        failures.append('Duplicate question wording across supplied files')
    return failures, summaries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', type=Path, nargs='*')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    paths = args.files or sorted((ROOT / '03-practice-sets').glob('set-*/practice-set-*.csv'))
    if not paths:
        parser.error('No CSV files found')
    failures, summaries = validate_files(paths)
    if not args.files and len(paths) != 6:
        failures.append(f'Expected six CSV files, found {len(paths)}')
    for row in summaries:
        print(f"{row['status']}: {row['file']} — {row['questions']} questions")
    report = {'status': 'FAIL' if failures else 'PASS', 'sets': len(paths),
              'total_questions': sum(s['questions'] for s in summaries),
              'checks': ['17-column header', '100 questions/set', 'domain weighting',
                         'question types', 'answer bounds/cardinality', 'unique options',
                         'option explanations', 'Microsoft Learn references', 'source consistency',
                         'exact normalized duplicate wording', 'balanced single-answer slots'],
              'limitations': ['No independent factual certification', 'No live URL availability check',
                              'No semantic duplicate detector', 'Udemy account import not performed'],
              'files': summaries, 'errors': failures}
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    if failures:
        for failure in failures:
            print(f'ERROR: {failure}')
        raise SystemExit(1)
    print(f"PASS: {report['sets']} sets / {report['total_questions']} questions")

if __name__ == '__main__':
    main()
