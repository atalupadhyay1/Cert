#!/usr/bin/env python3
"""Build one small mixed sample for a practice test upload.

Writes 05-sample-upload/sample-upload.csv: twelve items, two from each of
the six official domains (one single-answer and one multi-select), with no
case-study scaffolding. Upload it on its own to see how the player renders a
mixed block before publishing the six full 100-item sets.
"""
import csv

from bank import BANK
from build import HEADER, ROOT

OUT = '05-sample-upload/sample-upload.csv'
# Two items per domain: a single-answer decision and a two-answer decision.
WANTED = [(d, kind) for d in range(1, 7) for kind in ('S', 'M2')]


def pick(rows):
    chosen = []
    for domain, kind in WANTED:
        match = next(r for r in rows if r['domain'] == domain and r['kind'] == kind and r['id'] not in chosen)
        chosen.append(match['id'])
    return chosen


def main():
    from build import make_rows
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
