#!/usr/bin/env python3
"""End-to-end unit test suite for Microsoft Exam GH-900: GitHub Foundations Udemy practice-test course."""
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
    COMPLETION_FLOOR,
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


class TestGH900Course(unittest.TestCase):
    def test_01_blueprint_constants(self):
        self.assertEqual(EXAM_CODE, 'GH-900')
        self.assertEqual(ITEM_TOTAL, 100)
        self.assertEqual(sum(SKILL_PLAN.values()), 100)
        self.assertEqual(len(SKILLS), 36)
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
        self.assertLessEqual(stats['max_jaccard'], 0.72)

    def test_03_every_set_quotas_and_zero_case_studies(self):
        for n in range(1, 7):
            items = BANK[n]
            self.assertEqual(len(items), 100)
            completions = sum(1 for it in items if '____' in it['question'])
            prop_sols = sum(1 for it in items if 'Proposed solution:' in it['question'])
            case_qs = sum(1 for it in items if 'case study' in it['question'].lower())
            self.assertGreaterEqual(completions, COMPLETION_FLOOR)
            self.assertGreaterEqual(prop_sols, PROPOSED_SOL_FLOOR)
            self.assertEqual(case_qs, 0)
            self.assertEqual(sum(KIND_PLAN.values()), 100)
            self.assertEqual(sum(MULTI_PLAN.values()), KIND_PLAN['M2'] + KIND_PLAN['M3'])

    def test_04_csv_contracts_sets_sample_and_zip(self):
        for n in range(1, 7):
            sdir = COURSE_DIR / '03-practice-sets' / f'set-{n}'
            p = sdir / f'practice-set-{n}.csv'
            self.assertTrue(p.is_file(), f'Missing {p}')
            rows = list(csv.reader(p.read_text(encoding='utf-8-sig').splitlines()))
            self.assertEqual(rows[0], HEADER)
            self.assertEqual(len(rows), 101)
            for r in rows[1:]:
                self.assertEqual(len(r), 17)
                self.assertIn(r[1], ('multiple-choice', 'multi-select'))
                self.assertIn(r[16], DOMAINS.values())
                self.assertTrue(
                    any(u in r[15] for u in ('https://docs.github.com/', 'https://learn.microsoft.com/')),
                    f'Missing official reference URL in Overall Explanation: {r[15][:120]}',
                )
            self.assertTrue((sdir / f'practice-set-{n}.md').is_file())
            self.assertTrue((sdir / 'README.md').is_file())
        sample = COURSE_DIR / '05-sample-upload' / 'sample-upload.csv'
        srows = list(csv.reader(sample.read_text(encoding='utf-8-sig').splitlines()))
        self.assertEqual(srows[0], HEADER)
        self.assertEqual(len(srows), 15)  # Header + 14 rows (2 per domain across 7 domains)

        zpath = COURSE_DIR / 'GH-900-6x100.zip'
        self.assertTrue(zpath.is_file())
        with zipfile.ZipFile(zpath) as zf:
            names = set(zf.namelist())
            for n in range(1, 7):
                self.assertIn(f'GH-900/03-practice-sets/set-{n}/practice-set-{n}.csv', names)

    def test_05_zero_stem_overlap_with_all_11_sibling_microsoft_courses(self):
        gh900_stems = {
            re.sub(r'\s+', ' ', it['question'].strip().lower())
            for items in BANK.values()
            for it in items
        }
        self.assertEqual(len(gh900_stems), 600)
        checked_files = 0
        for other in ('PL-900', 'PL-200', 'PL-400', 'PL-500', 'PL-600', 'AZ-204', 'AZ-400', 'AZ-401', 'DP-300', 'DP-600', 'DP-900'):
            other_dir = REPO_COURSES_DIR / other / '03-practice-sets'
            for csv_path in sorted(other_dir.glob('set-*/practice-set-*.csv')):
                checked_files += 1
                rows = list(csv.reader(csv_path.read_text(encoding='utf-8-sig').splitlines()))[1:]
                for r in rows:
                    norm = re.sub(r'\s+', ' ', r[0].strip().lower())
                    self.assertNotIn(norm, gh900_stems, f'Overlap with {other}/{csv_path.name}: {r[0][:80]}')
        self.assertEqual(checked_files, 66)

    def test_06_required_docs_and_landing_page_completeness(self):
        required = [
            COURSE_DIR / 'README.md',
            COURSE_DIR / '01-landing-page' / 'landing-page.md',
            COURSE_DIR / '02-curriculum' / 'curriculum-outline.md',
            COURSE_DIR / '02-curriculum' / 'blueprint-alignment.md',
            COURSE_DIR / '04-resources' / 'SUMMARY.md',
            COURSE_DIR / '04-resources' / 'answer-manifest.json',
            COURSE_DIR / '04-resources' / 'validation-report.json',
            COURSE_DIR / '04-resources' / 'csv-format-spec.md',
            COURSE_DIR / '04-resources' / 'sources-and-coverage.md',
            COURSE_DIR / '04-resources' / 'publication-checklist.md',
            COURSE_DIR / '05-sample-upload' / 'README.md',
            COURSE_DIR / 'GH-900-6x100.zip',
        ]
        for p in required:
            self.assertTrue(p.is_file(), f'Missing required deliverable: {p}')

        lp = (COURSE_DIR / '01-landing-page' / 'landing-page.md').read_text(encoding='utf-8')
        for marker in (
            'January 2026',
            '100 minutes',
            'does not require renewal',
            'closed-book',
            'Welcome Message',
            'Congratulations Message',
            '700',
            'Agent Mode',
            'Enterprise Managed Users',
        ):
            self.assertIn(marker, lp)


if __name__ == '__main__':
    unittest.main()
