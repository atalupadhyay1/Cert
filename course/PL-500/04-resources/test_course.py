#!/usr/bin/env python3
"""End-to-end unit test suite for the Microsoft Exam PL-500 (6 x 100) course package."""
import csv
import json
import sys
import unittest
import zipfile
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
COURSES_DIR = ROOT.parent
sys.path.insert(0, str(HERE))

from bank import (  # noqa: E402
    ALLOCATIONS,
    BANK,
    CASE_SIZE,
    CASE_STUDIES,
    CODE_FILL_FLOOR,
    DOMAINS,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    OFFICIAL_RANGES,
    PROPOSED_SOL_FLOOR,
    SKILL_PLAN,
    SKILL_SOURCES,
    SKILLS,
    TERMS,
)
from build import EXPORT_PLAN, HEADER, case_name  # noqa: E402
from cases import CASES  # noqa: E402
from validate import check_jaccard, validate_csv_file  # noqa: E402


class TestPL500Course(unittest.TestCase):
    def test_01_blueprint_and_official_ranges(self):
        self.assertEqual(len(SKILLS), 42)
        self.assertEqual(set(SKILLS), set(SKILL_SOURCES))
        self.assertEqual(sum(SKILL_PLAN.values()), 100)
        for d, (lo, hi) in OFFICIAL_RANGES.items():
            cnt = ALLOCATIONS[1][d]
            self.assertTrue(lo <= cnt <= hi, f'Domain {d} allocation {cnt} outside {lo}-{hi}%')
        for _, url in SKILL_SOURCES.values():
            self.assertTrue(url.startswith('https://learn.microsoft.com/en-us/'))

    def test_02_six_sets_of_100_and_zero_duplicate_stems(self):
        stems = []
        for n in range(1, 7):
            self.assertEqual(len(BANK[n]), ITEM_TOTAL)
            self.assertEqual(Counter(r['task'] for r in BANK[n]), Counter(SKILL_PLAN))
            self.assertEqual(Counter(r['kind'] for r in BANK[n]), Counter(KIND_PLAN))
            self.assertEqual(
                Counter(r['domain'] for r in BANK[n] if r['kind'] in ('M2', 'M3')),
                Counter(MULTI_PLAN),
            )
            self.assertGreaterEqual(sum(1 for r in BANK[n] if '____' in r['question']), CODE_FILL_FLOOR)
            self.assertGreaterEqual(
                sum(1 for r in BANK[n] if 'Proposed solution:' in r['question']),
                PROPOSED_SOL_FLOOR,
            )
            stems.extend(r['question'].strip().casefold() for r in BANK[n])
        self.assertEqual(len(stems), 600)
        self.assertEqual(len(set(stems)), 600)

    def test_03_twenty_four_case_studies(self):
        self.assertEqual(len(CASES), 24)
        seen_cases = set()
        for n in range(1, 7):
            c = Counter(case_name(r['question']) for r in BANK[n] if case_name(r['question']))
            self.assertEqual(len(c), CASE_STUDIES)
            self.assertEqual(set(c.values()), {CASE_SIZE})
            self.assertTrue(set(c).isdisjoint(seen_cases))
            seen_cases.update(c)
        self.assertEqual(seen_cases, set(CASES))

    def test_04_all_terms_used_and_jaccard_below_threshold(self):
        used = {k for rs in BANK.values() for r in rs for k in r['keys']}
        self.assertEqual(used, set(TERMS))
        errors, max_sim, _ = check_jaccard(0.72)
        self.assertEqual(errors, [])
        self.assertLessEqual(max_sim, 0.72)

    def test_05_csv_integrity_and_balanced_answer_slots(self):
        for n in range(1, 7):
            for fname in (f'practice-set-{n}.csv', f'case-embedded-set-{n}.csv'):
                p = ROOT / f'03-practice-sets/set-{n}/{fname}'
                self.assertTrue(p.is_file(), f'Missing {p}')
                errs, stats = validate_csv_file(p, ITEM_TOTAL, check_balance=True)
                self.assertEqual(errs, [], f'{fname}: {errs}')
                self.assertEqual(stats['types'], EXPORT_PLAN)
                self.assertEqual(stats['single_slots'], {'A': 21, 'B': 21, 'C': 21, 'D': 21})

        sample = ROOT / '05-sample-upload/case-study-sample.csv'
        self.assertTrue(sample.is_file())
        errs, stats = validate_csv_file(sample, CASE_STUDIES * CASE_SIZE, check_balance=False)
        self.assertEqual(errs, [])
        self.assertEqual(stats['rows'], 12)

    def test_06_manifest_matches_csv_answers(self):
        manifest = json.loads((HERE / 'answer-manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(manifest['exam_code'], 'PL-500')
        for n in range(1, 7):
            entries = manifest['sets'][f'set-{n}']
            self.assertEqual(len(entries), ITEM_TOTAL)
            for fname in (f'practice-set-{n}.csv', f'case-embedded-set-{n}.csv'):
                with (ROOT / f'03-practice-sets/set-{n}/{fname}').open('r', encoding='utf-8-sig', newline='') as f:
                    rows = list(csv.DictReader(f))
                self.assertEqual([r['Correct Answers'] for r in rows], [e['correct_csv'] for e in entries])

    def test_07_cross_course_zero_stem_overlap(self):
        my_stems = {r['question'].strip().casefold() for rs in BANK.values() for r in rs}
        for other in ('PL-900', 'PL-200', 'PL-400', 'AZ-204', 'AZ-400', 'AZ-401', 'DP-600'):
            qdir = COURSES_DIR / other / '04-resources/questions'
            if not qdir.is_dir():
                continue
            other_stems = set()
            for qf in qdir.glob('*.txt'):
                for line in qf.read_text(encoding='utf-8').splitlines():
                    s = line.strip()
                    if s and not s.startswith('#'):
                        parts = s.split('|')
                        if len(parts) >= 5:
                            other_stems.add(parts[4].strip().casefold())
            overlap = my_stems & other_stems
            self.assertEqual(overlap, set(), f'Overlap with {other}: {overlap}')

    def test_08_required_docs_and_zip_archive(self):
        required = [
            ROOT / 'README.md',
            ROOT / '01-landing-page/landing-page.md',
            ROOT / '02-curriculum/curriculum-outline.md',
            ROOT / '04-resources/SUMMARY.md',
            ROOT / '04-resources/case-studies.md',
            ROOT / '04-resources/csv-format-spec.md',
            ROOT / '04-resources/case-study-upload-guide.md',
            ROOT / '04-resources/sources-and-coverage.md',
            ROOT / '04-resources/publication-checklist.md',
            ROOT / '04-resources/validation-report.json',
            ROOT / '04-resources/answer-manifest.json',
            ROOT / '05-sample-upload/README.md',
            ROOT / '05-sample-upload/case-study-sample.csv',
            ROOT / 'PL-500-6x100.zip',
        ]
        for p in required:
            self.assertTrue(p.is_file(), f'Missing required deliverable: {p}')

        with zipfile.ZipFile(ROOT / 'PL-500-6x100.zip', 'r') as zf:
            names = set(zf.namelist())
            self.assertIn('01-landing-page/landing-page.md', names)
            self.assertIn('03-practice-sets/set-1/practice-set-1.csv', names)
            self.assertIn('03-practice-sets/set-6/case-embedded-set-6.csv', names)
            self.assertIn('05-sample-upload/case-study-sample.csv', names)


if __name__ == '__main__':
    unittest.main(verbosity=2)
