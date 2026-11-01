#!/usr/bin/env python3
"""End-to-end unit test suite for Microsoft Exam DP-300 practice-test package."""
import csv
import re
import sys
import unittest
import zipfile
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
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
    SKILLS,
    TERMS,
)
from build import EXPORT_PLAN, case_name  # noqa: E402
from cases import CASES  # noqa: E402
from sequences import SEQUENCES  # noqa: E402
from validate import FORBIDDEN_MICROSOFT_COMPANIES, check_jaccard, validate_csv_file  # noqa: E402


class TestDP300Course(unittest.TestCase):
    def test_01_six_sets_of_100_and_official_oct2026_weights(self):
        self.assertEqual(sorted(BANK.keys()), [1, 2, 3, 4, 5, 6])
        self.assertEqual(len(DOMAINS), 5)
        self.assertEqual(len(SKILLS), 59)
        self.assertEqual(sum(SKILL_PLAN.values()), 100)
        for n, records in BANK.items():
            self.assertEqual(len(records), 100)
            for d, (lo, hi) in OFFICIAL_RANGES.items():
                self.assertGreaterEqual(ALLOCATIONS[n][d], lo)
                self.assertLessEqual(ALLOCATIONS[n][d], hi)
            self.assertEqual(Counter(r['domain'] for r in records), Counter(ALLOCATIONS[n]))
            self.assertEqual(Counter(r['task'] for r in records), Counter(SKILL_PLAN))

    def test_02_item_types_multi_spread_and_pattern_floors(self):
        for n, records in BANK.items():
            self.assertEqual(Counter(r['kind'] for r in records), Counter(KIND_PLAN))
            self.assertEqual(
                Counter(r['domain'] for r in records if r['kind'] in ('M2', 'M3')),
                Counter(MULTI_PLAN),
            )
            self.assertGreaterEqual(sum(1 for r in records if '____' in r['question']), CODE_FILL_FLOOR)
            self.assertGreaterEqual(sum(1 for r in records if 'Proposed solution:' in r['question']), PROPOSED_SOL_FLOOR)

    def test_03_24_original_case_studies_and_zero_microsoft_companies(self):
        self.assertEqual(len(CASES), 24)
        full_text = ' '.join(list(CASES.keys()) + list(CASES.values())).casefold()
        for name in FORBIDDEN_MICROSOFT_COMPANIES:
            self.assertNotIn(name, full_text)
        seen = set()
        for n, records in BANK.items():
            c = Counter(case_name(r['question']) for r in records if case_name(r['question']))
            self.assertEqual(len(c), CASE_STUDIES)
            self.assertEqual(set(c.values()), {CASE_SIZE})
            seen.update(c.keys())
        self.assertEqual(seen, set(CASES.keys()))

    def test_04_terms_sequences_and_jaccard_ceiling(self):
        src = (HERE / 'terms.py').read_text(encoding='utf-8')
        raw_keys = re.findall(r"^t\(\s*'([^']+)'", src, flags=re.M)
        self.assertEqual(len(raw_keys), len(set(raw_keys)))
        labels = [v[0].casefold() for v in TERMS.values()]
        self.assertEqual(len(labels), len(set(labels)))
        used = {k for rs in BANK.values() for r in rs for k in r['keys']}
        self.assertEqual(set(TERMS.keys()) - used, set())
        for k, (lbl, _) in SEQUENCES.items():
            self.assertEqual(lbl.count('→'), 3)
        errs, max_sim, _ = check_jaccard(0.72)
        self.assertEqual(errs, [])
        self.assertLessEqual(max_sim, 0.72)

    def test_05_all_13_csvs_and_zip_archive(self):
        for n in range(1, 7):
            for prefix in ('practice-set', 'case-embedded-set'):
                path = ROOT / f'03-practice-sets/set-{n}/{prefix}-{n}.csv'
                self.assertTrue(path.is_file(), f'Missing {path}')
                errs, stats = validate_csv_file(path, ITEM_TOTAL, check_balance=True)
                self.assertEqual(errs, [], f'{path.name}: {errs}')
                self.assertEqual(stats['single_slots'], {'A': 21, 'B': 21, 'C': 21, 'D': 21})
                self.assertEqual(stats['types'], EXPORT_PLAN)
                self.assertLessEqual(stats['max_question_chars'], 1000)

        sample = ROOT / '05-sample-upload/case-study-sample.csv'
        errs, stats = validate_csv_file(sample, CASE_STUDIES * CASE_SIZE, check_balance=False)
        self.assertEqual(errs, [])
        self.assertEqual(stats['rows'], 12)

        archive = ROOT / 'DP-300-6x100.zip'
        self.assertTrue(archive.is_file())
        with zipfile.ZipFile(archive) as zf:
            names = set(zf.namelist())
            self.assertIn('DP-300/README.md', names)
            self.assertIn('DP-300/01-landing-page/landing-page.md', names)
            self.assertIn('DP-300/03-practice-sets/set-6/case-embedded-set-6.csv', names)

    def test_06_zero_stem_overlap_with_all_10_sibling_microsoft_courses(self):
        norm = lambda s: ''.join(c for c in s.casefold() if c.isalnum())
        dp300_stems = {norm(r['question']) for rs in BANK.values() for r in rs}
        siblings = (
            'AZ-204', 'AZ-400', 'AZ-401', 'DP-600', 'DP-900',
            'PL-200', 'PL-400', 'PL-500', 'PL-600', 'PL-900',
        )
        other_stems = set()
        for sib in siblings:
            for csv_path in (ROOT.parent / sib / '03-practice-sets').rglob('practice-set-*.csv'):
                with csv_path.open('r', encoding='utf-8-sig', newline='') as f:
                    for row in csv.DictReader(f):
                        other_stems.add(norm(row['Question']))
        self.assertGreaterEqual(len(other_stems), 6000)
        self.assertEqual(dp300_stems & other_stems, set())

    def test_07_required_docs_and_landing_page_completeness(self):
        required = [
            ROOT / 'README.md',
            ROOT / '01-landing-page/landing-page.md',
            ROOT / '02-curriculum/curriculum-outline.md',
            ROOT / '02-curriculum/blueprint-alignment.md',
            ROOT / '04-resources/SUMMARY.md',
            ROOT / '04-resources/case-studies.md',
            ROOT / '04-resources/case-study-upload-guide.md',
            ROOT / '04-resources/csv-format-spec.md',
            ROOT / '04-resources/sources-and-coverage.md',
            ROOT / '04-resources/publication-checklist.md',
            ROOT / '05-sample-upload/README.md',
        ]
        for p in required:
            self.assertTrue(p.is_file(), f'Missing {p}')
        lp = (ROOT / '01-landing-page/landing-page.md').read_text(encoding='utf-8')
        for marker in (
            'October 27, 2026',
            'Welcome Message',
            'Congratulations Message',
            '700 / 1000',
            'What will students learn in your course?',
            'What are the requirements or prerequisites for taking your course?',
            'Who is this course for?',
        ):
            self.assertIn(marker, lp)


if __name__ == '__main__':
    unittest.main(verbosity=2)
