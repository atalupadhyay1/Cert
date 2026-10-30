#!/usr/bin/env python3
"""Create the deterministic instructor release archive PL-500-6x100.zip."""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / 'PL-500-6x100.zip'
EXCLUDED_PARTS = {'__pycache__', '.DS_Store', '.pytest_cache'}
FIXED_DT = (2026, 10, 30, 0, 0, 0)


def should_include(path: Path) -> bool:
    if not path.is_file():
        return False
    if path == ARCHIVE or path.suffix == '.pyc':
        return False
    return not any(part in EXCLUDED_PARTS for part in path.relative_to(ROOT).parts)


def build_zip() -> Path:
    files = sorted(p for p in ROOT.rglob('*') if should_include(p))
    with zipfile.ZipFile(ARCHIVE, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for file_path in files:
            rel = file_path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(filename=rel, date_time=FIXED_DT)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o644 & 0xFFFF) << 16
            zf.writestr(info, file_path.read_bytes())
    return ARCHIVE


if __name__ == '__main__':
    out = build_zip()
    print(f'Packaged {out.name} ({out.stat().st_size:,} bytes)')
