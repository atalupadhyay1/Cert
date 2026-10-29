#!/usr/bin/env python3
"""Package clean AZ-401 course deliverables into AZ-401-6x100.zip."""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'AZ-401-6x100.zip'
EXCLUDE_DIRS = {'__pycache__', '.pytest_cache'}
EXCLUDE_NAMES = {ARCHIVE.name, '.DS_Store'}


def main():
    files = []
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        if path.name in EXCLUDE_NAMES or path.suffix == '.pyc':
            continue
        files.append((path, Path('AZ-401') / rel))

    with zipfile.ZipFile(ARCHIVE, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for src, arcname in files:
            zf.write(src, arcname.as_posix())

    size_kb = ARCHIVE.stat().st_size / 1024
    print(f'Packaged {ARCHIVE.name}: {len(files)} files ({size_kb:.1f} KB)')


if __name__ == '__main__':
    main()
