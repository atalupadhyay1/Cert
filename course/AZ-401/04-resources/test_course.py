#!/usr/bin/env python3
"""End-to-end unit test suite for Microsoft Exam AZ-401 practice-test package."""
import csv
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
from build import EXPORT_PLAN, HEADER, case_name  # noqa: E402
from cases import CASES  # noqa: E402
from sequences import SEQUENCES  # noqa: E402
from validate import check_jaccard, validate_csv_file  # noqa: E402


class TestAZ401Course(unittest.TestCase):
    def test_six_sets_of_100_total_600(self):
        self.assertEqual(sorted(BANK.keys()), [1, 2, 3, 4, 5, 6])
        for n, records in BANK.items():
            self.assertEqual(len(records), 100, f'Exam {n} count != 100')
        self.assertEqual(sum(len(v) for v in BANK.values()), 600)

    def test_official_blueprint_weights_in_published_ranges(self):
        for n, alloc in ALLOCATIONS.items():
            self.assertEqual(sum(alloc.values()), 100)
            for domain, (low, high) in OFFICIAL_RANGES.items():
                self.assertGreaterEqual(alloc[domain], low, f'Exam {n} D{domain} below {low}%')
                self.assertLessEqual(alloc[domain], high, f'Exam {n} D{domain} above {high}%')

    def test_all_27_skills_covered_every_exam(self):
        self.assertEqual(len(SKILLS), 27)
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
            self.assertGreaterEqual(sum(1 for r in records if '____' in r['question']), CODE_FILL_FLOOR)
            self.assertGreaterEqual(sum(1 for r in records if 'Proposed solution:' in r['question']), PROPOSED_SOL_FLOOR)

    def test_24_original_case_studies_and_zero_microsoft_named_cases(self):
        self.assertEqual(len(CASES), 24)
        forbidden = (
            'contoso', 'litware', 'vanarsdel', 'wide world importers', 'coho winery',
            'fabrikam', 'adatum', 'tailwind traders', 'parts unlimited', 'mercury health', 'smarthotel360',
        )
        full_text = ' '.join(list(CASES.keys()) + list(CASES.values())).casefold()
        for name in forbidden:
            self.assertNotIn(name, full_text, f'Microsoft named scenario {name!r} must not appear')
        seen_cases = set()
        for n, records in BANK.items():
            c = Counter(case_name(r['question']) for r in records if case_name(r['question']))
            self.assertEqual(len(c), CASE_STUDIES)
            self.assertEqual(set(c.values()), {CASE_SIZE})
            seen_cases.update(c.keys())
        self.assertEqual(seen_cases, set(CASES.keys()))

    def test_zero_overlap_with_az400_and_az204_stems(self):
        az401_stems = {
            ''.join(c for c in r['question'].casefold() if c.isalnum())
            for rs in BANK.values() for r in rs
        }
        for sibling in ('AZ-400', 'AZ-204'):
            qdir = ROOT.parent / sibling / '04-resources' / 'questions'
            if not qdir.is_dir():
                continue
            other_stems = set()
            for qfile in sorted(qdir.glob('*.txt')):
                for line in qfile.read_text(encoding='utf-8').splitlines():
                    if not line.strip() or line.startswith('#'):
                        continue
                    parts = [x.strip() for x in line.split('|')]
                    if len(parts) == 6:
                        other_stems.add(''.join(c for c in parts[4].casefold() if c.isalnum()))
            self.assertEqual(az401_stems & other_stems, set(), f'Overlap found with {sibling}')

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

    def test_all_13_csv_files_pass_contract_and_slot_balance(self):
        for n in range(1, 7):
            for prefix in ('practice-set', 'case-embedded-set'):
                path = ROOT / f'03-practice-sets/set-{n}/{prefix}-{n}.csv'
                self.assertTrue(path.is_file(), f'Missing {path}')
                errs, stats = validate_csv_file(path, ITEM_TOTAL, check_balance=True)
                self.assertEqual(errs, [], f'{path.name} errors: {errs}')
                self.assertEqual(stats['single_slots'], {'A': 21, 'B': 21, 'C': 21, 'D': 21})
                self.assertEqual(stats['types'], EXPORT_PLAN)
                self.assertLessEqual(stats['max_question_chars'], 1000)

        sample = ROOT / '05-sample-upload/case-study-sample.csv'
        self.assertTrue(sample.is_file())
        errs, stats = validate_csv_file(sample, CASE_STUDIES * CASE_SIZE, check_balance=False)
        self.assertEqual(errs, [])
        self.assertEqual(stats['rows'], 12)

    def test_stem_jaccard_similarity_ceiling(self):
        errs, max_sim, _ = check_jaccard(0.72)
        self.assertEqual(errs, [])
        self.assertLessEqual(max_sim, 0.72)

    def test_answer_manifest_matches_csv_rows(self):
        manifest = json.loads((HERE / 'answer-manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(sorted(manifest.keys()), ['1', '2', '3', '4', '5', '6'])
        for n in range(1, 7):
            with (ROOT / f'03-practice-sets/set-{n}/practice-set-{n}.csv').open('r', encoding='utf-8-sig') as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(len(manifest[str(n)]), 100)
            for entry, row in zip(manifest[str(n)], rows):
                self.assertEqual(','.join(map(str, entry['correct_indices'])), row['Correct Answers'])
                self.assertEqual(DOMAINS[entry['domain']], row['Domain'])

    def test_blueprint_prereq_and_beta_disclosed_across_docs(self):
        for rel in (
            'README.md',
            '01-landing-page/landing-page.md',
            '02-curriculum/curriculum-outline.md',
            '04-resources/sources-and-coverage.md',
            '04-resources/SUMMARY.md',
        ):
            txt = (ROOT / rel).read_text(encoding='utf-8')
            self.assertIn('October 13, 2026', txt, f'{rel} must disclose October 13, 2026 study-guide baseline')
            self.assertIn('GH-300', txt, f'{rel} must disclose GH-300 prerequisite option')
            self.assertIn('AZ-104', txt, f'{rel} must disclose AZ-104 prerequisite option')
            self.assertIn('AZ-400', txt, f'{rel} must disclose predecessor Exam AZ-400 retirement context')
            self.assertIn('700', txt, f'{rel} must state 700 / 1000 scaled passing score')

    def test_required_docs_and_zip_archive_present(self):
        required = [
            'README.md',
            '01-landing-page/landing-page.md',
            '02-curriculum/curriculum-outline.md',
            '04-resources/csv-format-spec.md',
            '04-resources/case-study-upload-guide.md',
            '04-resources/case-studies.md',
            '04-resources/sources-and-coverage.md',
            '04-resources/publication-checklist.md',
            '04-resources/SUMMARY.md',
            '04-resources/validation-report.json',
            '04-resources/answer-manifest.json',
            '05-sample-upload/README.md',
            '05-sample-upload/case-study-sample.csv',
            'AZ-401-6x100.zip',
        ]
        for rel in required:
            self.assertTrue((ROOT / rel).is_file(), f'Missing {rel}')
        with zipfile.ZipFile(ROOT / 'AZ-401-6x100.zip') as zf:
            names = set(zf.namelist())
            for n in range(1, 7):
                self.assertIn(f'AZ-401/03-practice-sets/set-{n}/practice-set-{n}.csv', names)
                self.assertIn(f'AZ-401/03-practice-sets/set-{n}/case-embedded-set-{n}.csv', names)
                self.assertIn(f'AZ-401/03-practice-sets/set-{n}/practice-set-{n}.md', names)
            self.assertEqual(
                zf.read('AZ-401/01-landing-page/landing-page.md'),
                (ROOT / '01-landing-page/landing-page.md').read_bytes(),
                'ZIP landing-page.md is stale; re-run package.py',
            )

    def test_landing_page_exam_descriptions_and_messages_complete(self):
        lp = (ROOT / '01-landing-page/landing-page.md').read_text(encoding='utf-8')
        for heading in ('Welcome Message', 'Congratulations Message', 'Blueprint Allocation', 'Frequently Asked Questions'):
            self.assertIn(heading, lp)
        for n in range(1, 7):
            self.assertIn(f'practice-test-{n}', lp)
        full_blocks = re.findall(r'\*\*Full description\*\*\s+```text\n(.*?)\n```', lp, re.S)
        trimmed_blocks = re.findall(r'\*\*Trimmed description\*\*\s+```text\n(.*?)\n```', lp, re.S)
        self.assertEqual(len(full_blocks), 6)
        self.assertEqual(len(trimmed_blocks), 6)
        for idx, t in enumerate(trimmed_blocks, 1):
            self.assertLessEqual(len(t), 200, f'Trimmed description {idx} exceeds 200 chars ({len(t)})')


if __name__ == '__main__':
    unittest.main()
