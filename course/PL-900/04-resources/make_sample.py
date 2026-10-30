#!/usr/bin/env python3
"""Build a 10-question mixed sample upload CSV for Exam PL-900.

Writes 05-sample-upload/sample-upload.csv with 10 standalone items: 2 from each
of the 5 official PL-900 domains (1 single-answer and 1 two-answer multi-select),
with zero case-study scaffolding (matching the live PL-900 Fundamentals format).
"""
import csv

from bank import BANK
from build import HEADER, ROOT, make_rows

OUT = '05-sample-upload/sample-upload.csv'
WANTED = [(d, kind) for d in range(1, 6) for kind in ('S', 'M2')]


def pick(records: list[dict]) -> list[str]:
    chosen = []
    for domain, kind in WANTED:
        match = next(
            r for r in records
            if r['domain'] == domain and r['kind'] == kind and r['id'] not in chosen
        )
        chosen.append(match['id'])
    return chosen


def main():
    rows, mapping = make_rows(1)
    by_id = {entry['id']: row for row, entry in zip(rows, mapping)}
    ids = pick(BANK[1])
    sample = [by_id[i] for i in ids]
    target = ROOT / OUT
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, extrasaction='ignore', lineterminator='\n')
        writer.writeheader()
        for row in sample:
            writer.writerow({k: row.get(k, '') for k in HEADER})
    print(f'Wrote {OUT} ({len(sample)} rows)')
    for idx, row in enumerate(sample, 1):
        print(f'  Q{idx:02d}: {row["Question Type"]:<16} key={row["Correct Answers"]:<5} [{row["Domain"][:28]}]')


if __name__ == '__main__':
    main()
