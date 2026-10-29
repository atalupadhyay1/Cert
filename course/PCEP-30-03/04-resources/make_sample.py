#!/usr/bin/env python3
"""Write a 12-question sample CSV covering all four blocks and all three supported formats."""
import csv
from pathlib import Path

from bank import DOMAINS

ROOT = Path(__file__).resolve().parents[1]

with (ROOT / '03-practice-sets/set-1/practice-set-1.csv').open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    rows = list(reader)

sample = []
for block in DOMAINS.values():
    sample.append(next(r for r in rows
                       if r['Domain'] == block and r['Question Type'] == 'multiple-choice'
                       and '____' not in r['Question']))
    sample.append(next(r for r in rows
                       if r['Domain'] == block and r['Question Type'] == 'multiple-choice'
                       and '____' in r['Question']))
    sample.append(next(r for r in rows
                       if r['Domain'] == block and r['Question Type'] == 'multi-select'))

out = ROOT / '05-sample-upload/sample-upload.csv'
out.parent.mkdir(parents=True, exist_ok=True)
with out.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header, lineterminator='\n')
    writer.writeheader()
    writer.writerows(sample)

print(f'Wrote {out.relative_to(ROOT)} ({len(sample)} questions)')
