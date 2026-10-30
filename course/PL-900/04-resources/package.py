#!/usr/bin/env python3
"""Create a reproducible PL-900-6x100.zip distributable after CSV and companion validation."""
import json
import zipfile

from build import HEADER, ROOT, make_rows, render_test  # noqa: F401
from validate import validate_files

ZIP_NAME = 'PL-900-6x100.zip'

REQUIRED = [
    'README.md',
    '01-landing-page/landing-page.md',
    '02-curriculum/curriculum-outline.md',
    '04-resources/validation-report.json',
    '04-resources/publication-checklist.md',
    '04-resources/sources-and-coverage.md',
    '04-resources/csv-format-spec.md',
    '04-resources/SUMMARY.md',
    '04-resources/answer-manifest.json',
    '05-sample-upload/README.md',
    '05-sample-upload/sample-upload.csv',
]

FORBIDDEN = [
    '04-resources/cases.py',
    '04-resources/case-studies.md',
    '04-resources/case-study-upload-guide.md',
    '05-sample-upload/case-study-sample.csv',
]


def check_companion_files():
    manifest = json.loads((ROOT / '04-resources/answer-manifest.json').read_text(encoding='utf-8'))
    for n in range(1, 7):
        rows, mapping = make_rows(n)
        if manifest.get(str(n)) != mapping:
            raise ValueError(f'Stale answer manifest for set {n}; rerun build.py')
        review = ROOT / f'03-practice-sets/set-{n}/practice-set-{n}.md'
        if review.read_text(encoding='utf-8') != render_test(n, rows):
            raise ValueError(f'Stale review copy for set {n}; rerun build.py')
        if (ROOT / f'03-practice-sets/set-{n}/case-embedded-set-{n}.csv').exists():
            raise ValueError(f'Unexpected case-embedded CSV in set-{n} for no-case-study exam PL-900')
    csvs = sorted((ROOT / '03-practice-sets').glob('set-*/practice-set-*.csv'))
    errors, summaries = validate_files(csvs)
    if len(csvs) != 6 or errors:
        raise ValueError('CSV content failed validation: ' + '; '.join(errors))
    report = json.loads((ROOT / '04-resources/validation-report.json').read_text(encoding='utf-8'))
    if report.get('files') != summaries:
        raise ValueError('Stale validation-report.json; rerun validate.py --report')
    if report.get('status') != 'PASS' or report.get('sets') != 6 or report.get('total_questions') != 600:
        raise ValueError('Expected a passing 6-set / 600-question validation report')


def main():
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            raise SystemExit(f'Package rejected: missing {rel}')
    for rel in FORBIDDEN:
        if (ROOT / rel).exists():
            raise SystemExit(f'Package rejected: {rel} belongs to a case-study exam and PL-900 has none')
    check_companion_files()
    target = ROOT / ZIP_NAME
    with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in sorted(ROOT.rglob('*')):
            if not file.is_file() or file == target or '__pycache__' in file.parts:
                continue
            if file.suffix not in {'.md', '.csv', '.json', '.py', '.txt'}:
                continue
            info = zipfile.ZipInfo(file.relative_to(ROOT).as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, file.read_bytes())
    print(f'Created {target.name}: {target.stat().st_size:,} bytes')


if __name__ == '__main__':
    main()
