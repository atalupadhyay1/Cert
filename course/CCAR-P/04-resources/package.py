#!/usr/bin/env python3
"""Create a reproducible offline distribution ZIP for the CCAR-P course package."""
import json
import zipfile
from pathlib import Path

from build import ROOT, make_rows, render_set_readme, render_test
from validate import validate_files

ARCHIVE = ROOT / 'CCAR-P-6x63.zip'
EXCLUDED_DIRS = {'__pycache__', '.tmpcheck'}
FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def verify_tree():
    csvs = [ROOT / f'03-practice-sets/set-{n}/practice-set-{n}.csv' for n in range(1, 7)]
    failures, _ = validate_files(csvs)
    if failures:
        raise RuntimeError(f'CSV validation failed: {failures}')
    manifest = json.loads((ROOT / '04-resources/answer-manifest.json').read_text(encoding='utf-8'))
    for n in range(1, 7):
        rows, mapping = make_rows(n)
        md_path = ROOT / f'03-practice-sets/set-{n}/practice-set-{n}.md'
        readme_path = ROOT / f'03-practice-sets/set-{n}/README.md'
        if md_path.read_text(encoding='utf-8') != render_test(n, rows):
            raise RuntimeError(f'Stale Markdown review copy: {md_path}')
        if readme_path.read_text(encoding='utf-8') != render_set_readme(n, rows):
            raise RuntimeError(f'Stale set README: {readme_path}')
        if manifest.get(str(n)) != mapping:
            raise RuntimeError(f'Stale answer manifest for set {n}')
    report = json.loads((ROOT / '04-resources/validation-report.json').read_text(encoding='utf-8'))
    if report.get('status') != 'PASS':
        raise RuntimeError('validation-report.json status is not PASS')
    if not (ROOT / '05-sample-upload/sample-upload.csv').is_file():
        raise RuntimeError('Missing 05-sample-upload/sample-upload.csv')
    if list(ROOT.rglob('*case-stud*')):
        raise RuntimeError('Unexpected case-study artifact found in CCAR-P tree')


def main():
    verify_tree()
    files = sorted(
        p for p in ROOT.rglob('*')
        if p.is_file()
        and p != ARCHIVE
        and not p.name.endswith('.zip')
        and not p.name.endswith('.pyc')
        and not (set(p.relative_to(ROOT).parts) & EXCLUDED_DIRS)
    )
    with zipfile.ZipFile(ARCHIVE, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            rel = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(rel, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, path.read_bytes())
    print(f'Packaged {len(files)} files -> {ARCHIVE.name} ({ARCHIVE.stat().st_size:,} bytes)')


if __name__ == '__main__':
    main()
