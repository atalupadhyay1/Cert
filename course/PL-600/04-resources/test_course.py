#!/usr/bin/env python3
"""End-to-end unit test suite for Microsoft Exam PL-600 Udemy practice-test course."""
import csv
import re
import sys
import unittest
import zipfile
from pathlib import Path

RES_DIR = Path(__file__).resolve().parent
COURSE_DIR = RES_DIR.parent
REPO_COURSES_DIR = COURSE_DIR.parent
sys.path.insert(0, str(RES_DIR))

from bank import (  # noqa: E402
    ALLOCATIONS,
    BANK,
    CASES,
    CASE_SIZE,
    CASE_STUDIES,
    CODE_FILL_FLOOR,
    DOMAINS,
    EXAM_CODE,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    OFFICIAL_RANGES,
    PROPOSED_SOL_FLOOR,
    SKILLS,
    SKILL_PLAN,
    SKILL_SOURCES,
)
from build import HEADER  # noqa: E402
from validate import validate_all  # noqa: E402


class TestPL600Course(unittest.TestCase):
    def test_01_blueprint_constants(self):
        self.assertEqual(EXAM_CODE, 'PL-600')
        self.assertEqual(ITEM_TOTAL, 100)
        self.assertEqual(sum(SKILL_PLAN.values()), 100)
        self.assertEqual(len(SKILLS), 43)
        self.assertEqual(set(SKILLS), set(SKILL_PLAN))
        self.assertEqual(set(SKILLS), set(SKILL_SOURCES))
        for d, (lo, hi) in OFFICIAL_RANGES.items():
            cnt = ALLOCATIONS[1][d]
            self.assertGreaterEqual(cnt, lo)
            self.assertLessEqual(cnt, hi)

    def test_02_validator_zero_errors(self):
        errors, stats = validate_all()
        self.assertEqual(errors, [], f'Validator errors: {errors}')
        self.assertEqual(stats['total_questions'], 600)
        self.assertEqual(stats['terms_used'], stats['terms_total'])
        self.assertLess(stats['max_jaccard'], 0.72)

    def test_03_every_set_quotas(self):
        for n in range(1, 7):
            items = BANK[n]
            self.assertEqual(len(items), 100)
            self.assertEqual(len(CASES[n]), CASE_STUDIES)
            code_fills = sum(1 for it in items if '____' in it['question'])
            prop_sols = sum(1 for it in items if 'Proposed solution:' in it['question'])
            case_qs = sum(1 for it in items if it['question'].startswith('Case study \u2014 '))
            self.assertGreaterEqual(code_fills, CODE_FILL_FLOOR)
            self.assertGreaterEqual(prop_sols, PROPOSED_SOL_FLOOR)
            self.assertEqual(case_qs, CASE_STUDIES * CASE_SIZE)
            self.assertEqual(sum(KIND_PLAN.values()), 100)
            self.assertEqual(sum(MULTI_PLAN.values()), KIND_PLAN['M2'] + KIND_PLAN['M3'])

    def test_04_csv_contracts_standard_embedded_and_sample(self):
        for n in range(1, 7):
            sdir = COURSE_DIR / '03-practice-sets' / f'set-{n}'
            for prefix in ('practice-set-', 'case-embedded-set-'):
                p = sdir / f'{prefix}{n}.csv'
                self.assertTrue(p.is_file(), f'Missing {p}')
                rows = list(csv.reader(p.read_text(encoding='utf-8').splitlines()))
                self.assertEqual(rows[0], HEADER)
                self.assertEqual(len(rows), 101)
                for r in rows[1:]:
                    self.assertEqual(len(r), 17)
                    self.assertIn(r[1], ('multiple-choice', 'multi-select'))
                    self.assertIn(r[16], DOMAINS.values())
                    self.assertIn('https://learn.microsoft.com/', r[15])
            self.assertTrue((sdir / f'practice-set-{n}-review.md').is_file())
            self.assertTrue((sdir / 'README.md').is_file())
        sample = COURSE_DIR / '05-sample-upload' / 'case-study-sample.csv'
        srows = list(csv.reader(sample.read_text(encoding='utf-8').splitlines()))
        self.assertEqual(srows[0], HEADER)
        self.assertEqual(len(srows), 13)

    def test_05_zero_stem_overlap_with_other_microsoft_courses(self):
        pl600_stems = {
            re.sub(r'\s+', ' ', it['question'].strip().lower())
            for items in BANK.values()
            for it in items
        }
        self.assertEqual(len(pl600_stems), 600)
        checked_files = 0
        for other in ('PL-900', 'PL-200', 'PL-400', 'PL-500', 'AZ-204', 'AZ-400', 'AZ-401', 'DP-600'):
            other_dir = REPO_COURSES_DIR / other / '03-practice-sets'
            for csv_path in sorted(other_dir.glob('set-*/practice-set-*.csv')):
                checked_files += 1
                rows = list(csv.reader(csv_path.read_text(encoding='utf-8-sig').splitlines()))[1:]
                for r in rows:
                    norm = re.sub(r'\s+', ' ', r[0].strip().lower())
                    self.assertNotIn(norm, pl600_stems, f'Overlap with {other}/{csv_path.name}: {r[0][:80]}')
        self.assertEqual(checked_files, 48)

    def test_06_required_docs_and_retirement_disclosures(self):
        required = [
            COURSE_DIR / 'README.md',
            COURSE_DIR / '01-landing-page' / 'landing-page.md',
            COURSE_DIR / '02-curriculum' / 'curriculum-outline.md',
            COURSE_DIR / '02-curriculum' / 'blueprint-alignment.md',
            COURSE_DIR / '04-resources' / 'case-studies.md',
            COURSE_DIR / '04-resources' / 'csv-format-spec.md',
            COURSE_DIR / '04-resources' / 'case-study-upload-guide.md',
            COURSE_DIR / '04-resources' / 'sources-and-coverage.md',
            COURSE_DIR / '04-resources' / 'publication-checklist.md',
            COURSE_DIR / '05-sample-upload' / 'README.md',
            COURSE_DIR / 'PL-600-6x100.zip',
        ]
        for p in required:
            self.assertTrue(p.is_file(), f'Missing required deliverable: {p}')

        lp = (COURSE_DIR / '01-landing-page' / 'landing-page.md').read_text(encoding='utf-8')
        for marker in (
            'September 23, 2024',
            'June 30, 2026',
            'AB-100',
            'PL-200',
            'PL-400',
            'Well-Architected',
            '700',
            'Welcome Message',
            'Congratulations Message',
        ):
            self.assertIn(marker, lp)

        with zipfile.ZipFile(COURSE_DIR / 'PL-600-6x100.zip') as zf:
            names = set(zf.namelist())
            self.assertIn('PL-600/03-practice-sets/set-1/practice-set-1.csv', names)
            self.assertIn('PL-600/03-practice-sets/set-6/case-embedded-set-6.csv', names)
            self.assertIn('PL-600/05-sample-upload/case-study-sample.csv', names)


if __name__ == '__main__':
    unittest.main(verbosity=2)
