#!/usr/bin/env python3
"""Build a 14-question quick-smoke Udemy sample upload CSV (2 items per domain across all 7 GH-900 domains)."""
import csv
from collections import Counter
from pathlib import Path

from bank import DOMAINS
from build import HEADER

ROOT = Path(__file__).resolve().parents[1]
SET1_CSV = ROOT / '03-practice-sets' / 'set-1' / 'practice-set-1.csv'
SAMPLE_CSV = ROOT / '05-sample-upload' / 'sample-upload.csv'


def build_sample() -> None:
    with SET1_CSV.open('r', encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))

    picked = []
    per_dom = Counter()
    for dom_name in DOMAINS.values():
        mc_picked = 0
        ms_picked = 0
        for r in rows:
            if r['Domain'] != dom_name:
                continue
            if r['Question Type'] == 'multiple-choice' and mc_picked < 1:
                picked.append(r)
                mc_picked += 1
                per_dom[dom_name] += 1
            elif r['Question Type'] == 'multi-select' and ms_picked < 1:
                picked.append(r)
                ms_picked += 1
                per_dom[dom_name] += 1
            if per_dom[dom_name] == 2:
                break

    assert len(picked) == 14, f'Expected 14 sample rows, got {len(picked)}'
    SAMPLE_CSV.parent.mkdir(parents=True, exist_ok=True)
    with SAMPLE_CSV.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADER, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writeheader()
        writer.writerows(picked)
    print(f'Wrote {len(picked)} sample rows -> {SAMPLE_CSV}')


if __name__ == '__main__':
    build_sample()
