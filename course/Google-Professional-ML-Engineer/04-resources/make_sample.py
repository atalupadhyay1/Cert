#!/usr/bin/env python3
"""Build one small mixed sample for a Udemy practice test.

Writes 05-sample-upload/sample-upload.csv: six items, one per official domain,
with two multi-select items and no case-study scaffolding. Upload it on its own
to see how the player renders a mixed single-answer and multi-select block
before publishing the six full 100-item sets.
"""
import csv

from bank import BANK
from build import HEADER, ROOT

OUT = '05-sample-upload/sample-upload.csv'
# One item per domain; domains 1 and 4 contribute a multi-select item.
WANTED = {1: 'M2', 2: 'S', 3: 'S', 4: 'M2', 5: 'S', 6: 'S'}


def pick(rows):
    chosen = []
    for domain, kind in WANTED.items():
        match = next(r for r in rows if r['domain'] == domain and r['kind'] == kind)
        chosen.append(match['id'])
    return chosen


def main():
    from build import make_rows
    rows, _ = make_rows(1)
    by_id = {mapping['id']: row for row, mapping in zip(rows, make_rows(1)[1])}
    ids = pick(BANK[1])
    sample = [by_id[i] for i in ids]
    target = ROOT / OUT
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER, extrasaction='ignore', lineterminator='\n')
        writer.writeheader()
        for row in sample:
            writer.writerow({k: row.get(k, '') for k in HEADER})
    print(f'Wrote {OUT}')
    for n, row in enumerate(sample, 1):
        print(f'  Q{n}: {row["Question Type"]:<16} key={row["Correct Answers"]}  {row["_stem"][:70]}')


if __name__ == '__main__':
    main()
