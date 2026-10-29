#!/usr/bin/env python3
"""Build one small mixed sample for a practice test upload.

Writes 05-sample-upload/sample-upload.csv: twelve items, three from each of the
four published syllabus blocks (one code-trace multiple-choice, one `____`
gap-fill multiple-choice, and one multiple-response in each block), with no
case-study scaffolding. Upload it on its own to see how the player renders a
mixed block before publishing the six full 60-item sets.
"""
import csv

from bank import BANK
from build import HEADER, ROOT, make_rows

OUT = '05-sample-upload/sample-upload.csv'


def pick(rows):
    """One non-blank single, one `____` gap-fill single, and one M2 item per block."""
    chosen = []
    for domain in range(1, 5):
        plain = [r['id'] for r in rows if r['domain'] == domain and r['kind'] == 'S' and '____' not in r['question']]
        gaps = [r['id'] for r in rows if r['domain'] == domain and r['kind'] == 'S' and '____' in r['question']]
        multis = [r['id'] for r in rows if r['domain'] == domain and r['kind'] == 'M2']
        chosen.extend(plain[:1] + gaps[:1] + multis[:1])
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
