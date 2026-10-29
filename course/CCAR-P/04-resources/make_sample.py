#!/usr/bin/env python3
"""Write a 14-question sample upload CSV (1 MC + 1 multi-select per official domain from Set 1)."""
import csv
from bank import DOMAINS
from build import HEADER, ROOT, make_rows


def main():
    rows, _ = make_rows(1)
    sample = []
    for domain_num in sorted(DOMAINS):
        domain_label = DOMAINS[domain_num]
        mc = next(r for r in rows if r['Domain'] == domain_label and r['Question Type'] == 'multiple-choice')
        ms = next(r for r in rows if r['Domain'] == domain_label and r['Question Type'] == 'multi-select')
        sample.extend([mc, ms])
    out = ROOT / '05-sample-upload' / 'sample-upload.csv'
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, lineterminator='\n', extrasaction='ignore')
        writer.writeheader()
        writer.writerows(sample)
    print(f'Wrote {out.relative_to(ROOT)} ({len(sample)} rows across {len(DOMAINS)} domains)')


if __name__ == '__main__':
    main()
