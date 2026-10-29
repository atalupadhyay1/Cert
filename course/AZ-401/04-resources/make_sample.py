#!/usr/bin/env python3
"""Generate 05-sample-upload/case-study-sample.csv from Exam 1 case studies."""
import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from build import HEADER, make_rows, render_case_embedded  # noqa: E402

ROOT = HERE.parent


def main():
    rows, _ = make_rows(1)
    embedded = render_case_embedded(rows)
    case_rows = [r for r in embedded if r.get('_case')]
    out_dir = ROOT / '05-sample-upload'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / 'case-study-sample.csv'
    with out_path.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, lineterminator='\n', extrasaction='ignore')
        writer.writeheader()
        for row in case_rows:
            writer.writerow({k: row.get(k, '') for k in HEADER})
    print(f'Wrote {out_path.relative_to(ROOT)} ({len(case_rows)} self-contained case-study rows)')


if __name__ == '__main__':
    main()
