#!/usr/bin/env python3
"""Create a reproducible distributable after CSV validation. No external packages."""
import json
import zipfile
from build import ROOT, make_rows, render_test
from validate import validate_files


def check_companion_files():
    """Reject stale answer manifests, review copies, and validation reports."""
    manifest = json.loads((ROOT / '04-resources/answer-manifest.json').read_text(encoding='utf-8'))
    for number in range(1, 7):
        rows, mapping = make_rows(number)
        if manifest.get(str(number)) != mapping:
            raise ValueError(f'Stale answer manifest for set {number}; run build.py')
        review = ROOT / f'03-practice-sets/set-{number}/practice-set-{number}.md'
        if review.read_text(encoding='utf-8') != render_test(number, rows):
            raise ValueError(f'Stale review copy for set {number}; run build.py')
    csvs = sorted((ROOT / '03-practice-sets').glob('set-*/practice-set-*.csv'))
    errors, summaries = validate_files(csvs)
    if len(csvs) != 6 or errors:
        raise ValueError('CSV content does not match current source')
    report = json.loads((ROOT / '04-resources/validation-report.json').read_text(encoding='utf-8'))
    if report.get('files') != summaries:
        raise ValueError('Stale validation report; rerun validate.py --report')
    if report.get('status') != 'PASS' or report.get('sets') != 6 or report.get('total_questions') != 600:
        raise ValueError('Expected a passing six-set validation report; run validate.py --report')


def main():
    required = ['README.md', '01-landing-page/landing-page.md',
                '02-curriculum/curriculum-outline.md', '04-resources/validation-report.json',
                '04-resources/publication-checklist.md', '04-resources/answer-manifest.json']
    for relative in required:
        if not (ROOT / relative).is_file():
            raise SystemExit(f'Package rejected: missing {relative}')
    csvs = sorted((ROOT / '03-practice-sets').glob('set-*/practice-set-*.csv'))
    errors, _ = validate_files(csvs)
    if len(csvs) != 6 or errors:
        raise SystemExit('Package rejected: expected six valid CSVs. ' + '; '.join(errors))
    check_companion_files()
    target = ROOT / 'Google-Cloud-Professional-Agentic-Architect-Udemy-6x100.zip'
    with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for file in sorted(ROOT.rglob('*')):
            if not file.is_file() or file == target or '__pycache__' in file.parts:
                continue
            if file.suffix not in {'.md', '.csv', '.json', '.py', '.txt'}:
                continue
            info = zipfile.ZipInfo(file.relative_to(ROOT).as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, file.read_bytes())
    print(f'Created {target.name}: {target.stat().st_size:,} bytes')

if __name__ == '__main__':
    main()
