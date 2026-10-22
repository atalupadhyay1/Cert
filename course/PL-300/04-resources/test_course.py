"""Structural, allocation, and artifact tests for the PL-300 practice package."""
import copy
import csv
import json
import re
import unittest
import zipfile
from collections import Counter
from pathlib import Path

from bank import ALLOCATIONS, BANK, SKILLS, TOPICS, VALID_TASKS
from build import HEADER, ROOT, TYPE_PLAN, EXPORT_PLAN, ALLOWED_TYPES, make_rows, render_test
from terms import TERMS
from validate import validate_rows

ZIP = ROOT / 'PL-300-Power-BI-Data-Analyst-6x100.zip'


def header_row(csv_path):
    with csv_path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.rows, _ = make_rows(1)

    def corrupt(self, change):
        rows = copy.deepcopy(self.rows)
        change(rows)
        self.assertTrue(validate_rows(rows, self.rows))

    def test_all_six_sets_valid(self):
        for n in range(1, 7):
            rows, _ = make_rows(n)
            self.assertEqual(validate_rows(rows, rows), [], f'set {n}')

    def test_missing_row(self):
        self.corrupt(lambda r: r.pop())

    def test_out_of_bounds_answer(self):
        self.corrupt(lambda r: r[0].update({'Correct Answers': '5'}))

    def test_two_indices_on_single_choice(self):
        target = next(r for r in self.rows if r['Question Type'] == 'multiple-choice')
        self.corrupt(lambda r: next(x for x in r if x['Question'] == target['Question']).update({'Correct Answers': '1,2'}))

    def test_multi_select_without_stated_count(self):
        target = next(r for r in self.rows if r['Question Type'] == 'multi-select')
        self.corrupt(lambda r: next(x for x in r if x['Question'] == target['Question']).update({'Question': 'Which two controls apply here?'}))

    def test_multi_select_key_count_mismatch(self):
        target = next(r for r in self.rows if r['Question Type'] == 'multi-select')
        key = target['Correct Answers'].split(',')[0]
        self.corrupt(lambda r: next(x for x in r if x['Question'] == target['Question']).update({'Correct Answers': key}))

    def test_ordering_without_sequence_arrows(self):
        target = next(r for r in self.rows if '→' in r['Answer Option 4'])
        self.corrupt(lambda r: next(x for x in r if x['Question'] == target['Question']).update({'Answer Option 2': 'Plain text option'}))

    def test_duplicate_question(self):
        self.corrupt(lambda r: r[1].update({'Question': r[0]['Question']}))

    def test_duplicate_option(self):
        self.corrupt(lambda r: r[0].update({'Answer Option 2': r[0]['Answer Option 1']}))

    def test_missing_explanation(self):
        self.corrupt(lambda r: r[0].update({'Explanation 1': ''}))

    def test_missing_reference(self):
        self.corrupt(lambda r: r[0].update({'Overall Explanation': 'No source.'}))

    def test_wrong_domain(self):
        self.corrupt(lambda r: r[0].update({'Domain': 'Other'}))

    def test_wrong_answer_from_source(self):
        def change(rows):
            row = rows[0]
            indices = row['Correct Answers'].split(',')
            row['Correct Answers'] = '1' if indices[0] != '1' else '2'
        self.corrupt(change)

    def test_unexpected_sixth_option(self):
        self.corrupt(lambda r: r[0].update({'Answer Option 6': 'Extra', 'Explanation 6': 'Extra'}))

    def test_unbalanced_slots(self):
        def change(rows):
            for row in rows:
                if row['Question Type'] == 'multiple-choice':
                    row['Correct Answers'] = '1'
        self.corrupt(change)


class SourceTests(unittest.TestCase):
    def test_every_skill_is_practised(self):
        used = {r['task'] for rows in BANK.values() for r in rows}
        self.assertEqual(used, VALID_TASKS)
        self.assertEqual(len(SKILLS), 30)

    def test_term_keys_are_unique(self):
        source = (ROOT / '04-resources/terms.py').read_text(encoding='utf-8')
        keys = re.findall(r"^t\('([^']+)'", source, re.M)
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(len(keys), len(TERMS))

    def test_allocation_is_inside_official_ranges(self):
        from bank import OFFICIAL_WEIGHTS
        for n, allocation in ALLOCATIONS.items():
            self.assertEqual(sum(allocation.values()), 100)
            for domain, count in allocation.items():
                pct = count / 100 * 100
                low, high = OFFICIAL_WEIGHTS[domain]
                self.assertGreaterEqual(pct, low, f'set {n} domain {domain}')
                self.assertLessEqual(pct, high, f'set {n} domain {domain}')

    def test_every_case_study_has_a_scenario(self):
        from cases import CASES
        for n, rows in BANK.items():
            for record in rows:
                match = re.match(r'Case study — ([^:]+):', record['question'])
                if match:
                    self.assertIn(match[1], CASES, f'set {n}: {match[1]}')
                    self.assertGreater(len(CASES[match[1]].split()), 50, match[1])
        brief = (ROOT / '04-resources/case-studies.md').read_text(encoding='utf-8')
        for name, text in CASES.items():
            self.assertIn(f'### Case study — {name}', brief)
            self.assertIn(text, brief)

    def test_embedded_case_variant_repeats_scenario(self):
        from cases import CASES
        from build import render_case_embedded
        rows, _ = make_rows(1)
        embedded = render_case_embedded(1, rows)
        self.assertEqual(len(embedded), 100)
        for row in embedded:
            if row['_case']:
                self.assertIn(CASES[row['_case']], row['Question'])
                self.assertLess(len(row['Question']), 1000, row['_case'])

    def test_four_case_studies_per_exam(self):
        for n, rows in BANK.items():
            cases = Counter()
            for record in rows:
                match = re.match(r'Case study — ([^:]+):', record['question'])
                if match:
                    cases[match[1]] += 1
            self.assertEqual(len(cases), 4, f'set {n}: {cases}')
            self.assertEqual(set(cases.values()), {3}, f'set {n}: {cases}')


class ArtifactTests(unittest.TestCase):
    def test_each_exam_has_100_rows_and_17_columns(self):
        for n in range(1, 7):
            path = ROOT / f'03-practice-sets/set-{n}/practice-set-{n}.csv'
            rows = header_row(path)
            self.assertEqual(len(rows), 100, path.name)
            self.assertEqual(list(rows[0]), HEADER, path.name)
            types = Counter(r['Question Type'] for r in rows)
            self.assertEqual(types, Counter(EXPORT_PLAN), path.name)
            self.assertLessEqual(set(types), set(ALLOWED_TYPES), path.name)

    def test_csv_bytes_are_bom_and_lf(self):
        for n in range(1, 7):
            raw = (ROOT / f'03-practice-sets/set-{n}/practice-set-{n}.csv').read_bytes()
            self.assertTrue(raw.startswith(b'\xef\xbb\xbf'), f'set {n} BOM')
            self.assertNotIn(b'\r\n', raw, f'set {n} line endings')
            self.assertTrue(raw.endswith(b'\n'), f'set {n} trailing newline')

    def test_markdown_review_matches_builder(self):
        for n in range(1, 7):
            rows, _ = make_rows(n)
            path = ROOT / f'03-practice-sets/set-{n}/practice-set-{n}.md'
            text = path.read_text(encoding='utf-8')
            self.assertEqual(text, render_test(n, rows), path.name)
            self.assertEqual(len(re.findall(r'^### \d+\. ', text, re.M)), 100)
            self.assertEqual(text.count('## Case study — '), 4)
            self.assertIn('## Answer key and explanations', text)

    def test_set_readme_states_mix(self):
        for n in range(1, 7):
            text = (ROOT / f'03-practice-sets/set-{n}/README.md').read_text(encoding='utf-8')
            self.assertIn('100 original items', text)
            self.assertIn('16 multi-select', text)
            self.assertIn('700/1000', text)

    def test_manifest_matches_builder(self):
        manifest = json.loads((ROOT / '04-resources/answer-manifest.json').read_text(encoding='utf-8'))
        for n in range(1, 7):
            _, mapping = make_rows(n)
            self.assertEqual(manifest[str(n)], mapping, f'set {n}')
        self.assertEqual(sum(len(v) for v in manifest.values()), 600)

    def test_validation_report_passes(self):
        report = json.loads((ROOT / '04-resources/validation-report.json').read_text(encoding='utf-8'))
        self.assertEqual(report['status'], 'PASS')
        self.assertEqual(report['sets'], 6)
        self.assertEqual(report['total_questions'], 600)
        self.assertEqual(report['errors'], [])

    def test_documents_exist(self):
        for relative in ['README.md', '01-landing-page/landing-page.md',
                         '02-curriculum/curriculum-outline.md',
                         '04-resources/sources-and-coverage.md',
                         '04-resources/csv-format-spec.md',
                         '04-resources/publication-checklist.md',
                         '04-resources/SUMMARY.md', '04-resources/case-studies.md']:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_landing_page_has_no_stale_counts(self):
        text = (ROOT / '01-landing-page/landing-page.md').read_text(encoding='utf-8')
        self.assertIn('600 original questions', text)
        self.assertIn('28 / 28 / 28 / 16', text)
        self.assertIn('100 minutes', text)
        self.assertNotIn('50 questions', text)
        self.assertIn('Welcome Message', text)
        self.assertIn('Congratulations Message', text)
        self.assertIn('Practice percentages are not scaled scores', text)
        self.assertNotIn('AI-103', text)
        self.assertNotIn('AB-731', text)

    @unittest.skipUnless(ZIP.is_file(), 'package.py has not been run')
    def test_zip_contents_and_timestamps(self):
        with zipfile.ZipFile(ZIP) as z:
            names = z.namelist()
            for n in range(1, 7):
                self.assertIn(f'03-practice-sets/set-{n}/practice-set-{n}.csv', names)
            self.assertIn('01-landing-page/landing-page.md', names)
            self.assertIn('04-resources/answer-manifest.json', names)
            self.assertTrue(all(i.date_time == (1980, 1, 1, 0, 0, 0) for i in z.infolist()))
            self.assertFalse(any('__pycache__' in n for n in names))
            self.assertFalse(any(n.endswith('.zip') for n in names))


if __name__ == '__main__':
    unittest.main()
