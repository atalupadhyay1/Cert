#!/usr/bin/env python3
"""End-to-end unit test suite for Microsoft Exam PL-900 practice-test package."""
import json
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
    COMPLETION_FLOOR,
    ITEM_TOTAL,
    KIND_PLAN,
    MULTI_PLAN,
    OFFICIAL_RANGES,
    PROPOSED_SOL_FLOOR,
    SKILL_PLAN,
    SKILLS,
    TERMS,
)
from build import EXPORT_PLAN  # noqa: E402
from package import FORBIDDEN, REQUIRED, ZIP_NAME  # noqa: E402
from sequences import SEQUENCES  # noqa: E402
from validate import FORBIDDEN_MS_NAMES, check_jaccard, validate_csv_file  # noqa: E402


class TestPL900Course(unittest.TestCase):
    def test_six_sets_of_100_total_600(self):
        self.assertEqual(sorted(BANK.keys()), [1, 2, 3, 4, 5, 6])
        for n, records in BANK.items():
            self.assertEqual(len(records), 100, f'Exam {n} count != 100')
        self.assertEqual(sum(len(v) for v in BANK.values()), 600)

    def test_official_blueprint_weights_in_published_ranges(self):
        self.assertEqual(len(OFFICIAL_RANGES), 5)
        for n, alloc in ALLOCATIONS.items():
            self.assertEqual(sum(alloc.values()), 100)
            for domain, (low, high) in OFFICIAL_RANGES.items():
                self.assertGreaterEqual(alloc[domain], low, f'Exam {n} D{domain} below {low}%')
                self.assertLessEqual(alloc[domain], high, f'Exam {n} D{domain} above {high}%')

    def test_all_34_skills_covered_every_exam(self):
        self.assertEqual(len(SKILLS), 34)
        self.assertEqual(sum(SKILL_PLAN.values()), 100)
        for n, records in BANK.items():
            self.assertEqual(Counter(r['task'] for r in records), Counter(SKILL_PLAN), f'Exam {n} skill plan mismatch')

    def test_item_type_and_pattern_floors(self):
        for n, records in BANK.items():
            self.assertEqual(Counter(r['kind'] for r in records), Counter(KIND_PLAN))
            self.assertEqual(
                Counter(r['domain'] for r in records if r['kind'] in ('M2', 'M3')),
                Counter(MULTI_PLAN),
            )
            self.assertGreaterEqual(sum(1 for r in records if '____' in r['question']), COMPLETION_FLOOR)
            self.assertGreaterEqual(sum(1 for r in records if 'Proposed solution:' in r['question']), PROPOSED_SOL_FLOOR)

    def test_no_case_studies_and_zero_microsoft_named_cases(self):
        for rel in FORBIDDEN:
            self.assertFalse((ROOT / rel).exists(), f'Forbidden case-study artifact present: {rel}')
        for n, records in BANK.items():
            for r in records:
                self.assertFalse(r['question'].startswith('Case study —'), f'{r["id"]} has case prefix')
                q_low = (r['question'] + ' ' + r['reason']).casefold()
                for ms_name in FORBIDDEN_MS_NAMES:
                    self.assertNotIn(ms_name, q_low, f'{r["id"]} mentions Microsoft scenario {ms_name!r}')

    def test_term_keys_and_labels_unique_and_100pct_exercised(self):
        src = (HERE / 'terms.py').read_text(encoding='utf-8')
        raw_keys = re.findall(r"^t\('([^']+)'", src, flags=re.M)
        self.assertEqual(len(raw_keys), len(set(raw_keys)))
        labels = [v[0].casefold() for v in TERMS.values()]
        self.assertEqual(len(labels), len(set(labels)), 'Duplicate case-insensitive option label in TERMS')
        used = {k for rs in BANK.values() for r in rs for k in r['keys']}
        self.assertEqual(set(TERMS.keys()) - used, set(), f'Unused terms: {set(TERMS.keys()) - used}')

    def test_ordering_items_use_arrow_sequences_exclusively(self):
        for k, (label, _) in SEQUENCES.items():
            self.assertEqual(label.count('→'), 3, f'{k} should be a 4-step sequence with 3 arrows')
        for rs in BANK.values():
            for r in rs:
                if r['kind'] == 'O':
                    for k in r['keys']:
                        self.assertIn(k, SEQUENCES)
                else:
                    for k in r['keys']:
                        self.assertNotIn(k, SEQUENCES)

    def test_all_7_csv_files_pass_contract_and_slot_balance(self):
        for n in range(1, 7):
            path = ROOT / f'03-practice-sets/set-{n}/practice-set-{n}.csv'
            self.assertTrue(path.is_file(), f'Missing {path}')
            errs, stats = validate_csv_file(path, ITEM_TOTAL, check_balance=True)
            self.assertEqual(errs, [], f'{path.name} errors: {errs}')
            self.assertEqual(stats['single_slots'], {'A': 21, 'B': 21, 'C': 21, 'D': 21})
            self.assertEqual(stats['types'], EXPORT_PLAN)
            self.assertLessEqual(stats['max_question_chars'], 1000)

        sample = ROOT / '05-sample-upload/sample-upload.csv'
        self.assertTrue(sample.is_file())
        errs, stats = validate_csv_file(sample, 10, check_balance=False)
        self.assertEqual(errs, [])
        self.assertEqual(stats['rows'], 10)

    def test_stem_jaccard_similarity_ceiling(self):
        errs, max_sim, _ = check_jaccard(0.72)
        self.assertEqual(errs, [], f'Jaccard violations: {errs}')
        self.assertLessEqual(max_sim, 0.72)

    def test_zero_overlap_with_other_microsoft_courses(self):
        norm = lambda s: ''.join(c for c in s.casefold() if c.isalnum())
        pl900_stems = {norm(r['question']) for rs in BANK.values() for r in rs}
        self.assertEqual(len(pl900_stems), 600)
        other_stems = set()
        for sib in ('PL-400', 'AZ-204', 'AZ-400', 'AZ-401', 'DP-600'):
            qdir = ROOT.parent / sib / '04-resources' / 'questions'
            if qdir.is_dir():
                for qfile in qdir.glob('*.txt'):
                    for line in qfile.read_text(encoding='utf-8').splitlines():
                        if line.strip() and not line.startswith('#'):
                            parts = [x.replace('\\|', '|').strip() for x in re.split(r'(?<!\\)\|', line)]
                            if len(parts) == 6:
                                other_stems.add(norm(parts[4]))
        self.assertEqual(pl900_stems & other_stems, set())

    def test_landing_page_complete_with_messages_and_exam_descriptions(self):
        lp = (ROOT / '01-landing-page/landing-page.md').read_text(encoding='utf-8')
        for section in (
            'Official Exam PL-900 Overview',
            '### 1. Course Title',
            '### 2. Course Subtitle',
            '### 3. Course Description',
            '### 4. What will students learn in your course?',
            '### 5. What are the requirements or prerequisites for taking your course?',
            '### 6. Who is this course for?',
            'Welcome Message',
            'Congratulations Message',
            '### Practice test 1',
            '### Practice test 6',
        ):
            self.assertIn(section, lp, f'Landing page missing {section}')
        self.assertIn('July 24, 2026', lp)
        self.assertIn('never expire', lp.casefold())
        # Verify Field 4 bullet concise length
        f4 = lp.split('### 4. What will students learn in your course?', 1)[1].split('### 5.', 1)[0]
        bullets = [ln.lstrip('• ').strip() for ln in f4.splitlines() if ln.strip().startswith('•')]
        self.assertEqual(len(bullets), 12)
        for b in bullets:
            self.assertLessEqual(len(b), 78, f'Field 4 bullet too long ({len(b)} chars): {b}')

    def test_required_docs_and_zip_archive_valid(self):
        for rel in REQUIRED:
            self.assertTrue((ROOT / rel).is_file(), f'Missing required file {rel}')
        zpath = ROOT / ZIP_NAME
        self.assertTrue(zpath.is_file(), f'Missing zip {ZIP_NAME}')
        with zipfile.ZipFile(zpath, 'r') as zf:
            self.assertIsNone(zf.testzip())
            names = set(zf.namelist())
            for rel in REQUIRED:
                self.assertIn(rel, names)
            for n in range(1, 7):
                self.assertIn(f'03-practice-sets/set-{n}/practice-set-{n}.csv', names)
        report = json.loads((HERE / 'validation-report.json').read_text(encoding='utf-8'))
        self.assertEqual(report['status'], 'PASS')
        self.assertEqual(report['total_questions'], 600)


if __name__ == '__main__':
    unittest.main(verbosity=2)
