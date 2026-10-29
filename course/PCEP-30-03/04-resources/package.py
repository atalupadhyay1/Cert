#!/usr/bin/env python3
"""Create a deterministic distribution archive after running the local export checks."""
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZIP_NAME = 'PCEP-30-03-6x60.zip'
EXCLUDED_PARTS = {'__pycache__', '.pytest_cache', '.DS_Store'}
EXCLUDED_SUFFIXES = {'.pyc', '.pyo', '.zip'}


def iter_files():
    for path in sorted(ROOT.rglob('*')):
        rel = path.relative_to(ROOT)
        if not path.is_file():
            continue
        if any(part in EXCLUDED_PARTS for part in rel.parts) or path.suffix in EXCLUDED_SUFFIXES:
            continue
        yield path, rel


def main():
    subprocess.run([sys.executable, str(ROOT / '04-resources/validate.py')], check=True)
    archive = ROOT / ZIP_NAME
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path, rel in iter_files():
            info = zipfile.ZipInfo(rel.as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, path.read_bytes())
    print(f'Wrote {archive.name} ({archive.stat().st_size:,} bytes)')


if __name__ == '__main__':
    main()
