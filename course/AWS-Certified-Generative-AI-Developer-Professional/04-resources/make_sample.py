#!/usr/bin/env python3
"""Build one small mixed sample for a practice test upload.

Writes 05-sample-upload/sample-upload.csv: fifteen items, three from each of the
five published domains (two multiple-choice and one multiple-response in each),
with no case-study scaffolding. Upload it on its own to see how the player
renders a mixed block before publishing the six full 75-item sets.
"""
import csv

from bank import BANK
from build import HEADER, ROOT, make_rows

OUT = '05-sample-upload/sample-upload.csv'


def pick(rows):
    """Two single-answer items and one multi-response item from each domain."""
    chosen = []
    for domain in range(1, 6):
        singles = [r['id'] for r in rows if r['domain'] == domain and r['kind'] == 'S']
        multis = [r['id'] for r in rows if r['domain'] == domain and r['kind'] == 'M2']
        chosen.extend(singles[:2] + multis[:1])
    return chosen


def main():
    rows, mapping = make_rows(1)
    by_id = {entry['id']: row for row, entry in zip(rows, mapping)}
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
