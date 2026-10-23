#!/usr/bin/env python3
"""Build one self-contained case-study sample for a Udemy practice test.

Writes 05-sample-upload/case-study-sample.csv: the three questions of one
case study, each with the scenario embedded in its stem, so the block can be
uploaded on its own to see how the player renders it.
"""
import csv
from build import HEADER, make_rows
from cases import CASES

CASE = 'Fabrikam claims'
OUT = '05-sample-upload/case-study-sample.csv'


def main():
    rows, _ = make_rows(1)
    block = [r for r in rows if r['_case'] == CASE]
    if len(block) != 3:
        raise SystemExit(f'expected 3 items for {CASE}, found {len(block)}')
    target = __import__('build').ROOT / OUT
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER, extrasaction='ignore', lineterminator='\n')
        writer.writeheader()
        for n, row in enumerate(block, 1):
            record = {k: row.get(k, '') for k in HEADER}
            record['Question'] = f'Case study — {CASE} ({n} of 3): {CASES[CASE]} {row["_stem"]}'
            writer.writerow(record)
    print(f'Wrote {OUT}')
    for n, row in enumerate(block, 1):
        print(f'  Q{n}: {row["Question Type"]:<16} key={row["Correct Answers"]}  {row["_stem"][:70]}')


if __name__ == '__main__':
    main()
