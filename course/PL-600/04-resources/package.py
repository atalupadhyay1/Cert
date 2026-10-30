#!/usr/bin/env python3
"""Deterministic distribution archive packager for Microsoft Exam PL-600."""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / 'PL-600-6x100.zip'
FIXED_DT = (2026, 1, 1, 0, 0, 0)

INCLUDE_GLOBS = [
    'README.md',
    '01-landing-page/*.md',
    '02-curriculum/*.md',
    '03-practice-sets/set-*/*',
    '04-resources/*.md',
    '04-resources/*.py',
    '04-resources/questions/*.txt',
    '05-sample-upload/*',
]


def build_zip() -> None:
    files: list[Path] = []
    for pat in INCLUDE_GLOBS:
        files.extend(sorted(ROOT.glob(pat)))
    unique_files = []
    seen = set()
    for p in sorted(files):
        if p.is_file() and p not in seen and '__pycache__' not in p.parts:
            seen.add(p)
            unique_files.append(p)

    with zipfile.ZipFile(ARCHIVE, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in unique_files:
            rel = p.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(filename=f'PL-600/{rel}', date_time=FIXED_DT)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, p.read_bytes())

    size_kb = ARCHIVE.stat().st_size / 1024
    print(f'Packaged {len(unique_files)} files -> {ARCHIVE.name} ({size_kb:.1f} KB)')


if __name__ == '__main__':
    build_zip()
