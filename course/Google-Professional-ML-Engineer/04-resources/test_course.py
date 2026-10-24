"""Structural, allocation, and artifact tests for the PMLE practice package."""
import copy
import csv
import json
import re
import unittest
import zipfile
from collections import Counter

from bank import ALLOCATIONS, BANK, ITEM_TOTAL, OFFICIAL_WEIGHTS, SKILLS, TOPICS, VALID_TASKS
from build import (ALLOWED_TYPES, EXPORT_PLAN, HEADER, ROOT, TYPE_PLAN,
                   make_rows, render_test)
from terms import TERMS
from validate import validate_rows

ZIP = ROOT / 'Google-Professional-ML-Engineer-6x100.zip'


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

    def test_case_study_wording_is_rejected(self):
        self.corrupt(lambda r: r[0].update({'Question': 'Case study — Altostrat: ' + r[0]['Question']}))


class SourceTests(unittest.TestCase):
    def test_every_skill_is_practised(self):
        used = {r['task'] for rows in BANK.values() for r in rows}
        self.assertEqual(used, VALID_TASKS)
        self.assertEqual(len(SKILLS), 47)

    def test_term_keys_are_unique(self):
        source = (ROOT / '04-resources/terms.py').read_text(encoding='utf-8')
        keys = re.findall(r"^t\('([^']+)'", source, re.M)
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(len(keys), len(TERMS))

    def test_allocation_matches_published_weights(self):
        for n, allocation in ALLOCATIONS.items():
            self.assertEqual(sum(allocation.values()), ITEM_TOTAL)
            for domain, count in allocation.items():
                # Google publishes approximate weights that total 101%; each
                # 100-item count must stay within one point of its weight.
                self.assertLessEqual(abs(count - OFFICIAL_WEIGHTS[domain]), 1.0,
                                     f'set {n} domain {domain}')

    def test_near_duplicate_gate_runs(self):
        from build import NEAR_DUPLICATE_LIMIT, check_source
        self.assertLessEqual(NEAR_DUPLICATE_LIMIT, 0.75)
        check_source()

    def test_item_type_plan_total(self):
        self.assertEqual(TYPE_PLAN, {'multiple-choice': 84, 'multi-select': 16})
        self.assertEqual(sum(TYPE_PLAN.values()), 100)
        self.assertEqual(EXPORT_PLAN, TYPE_PLAN)

    def test_no_case_studies_or_sequencing(self):
        for n, rows in BANK.items():
            for record in rows:
                self.assertNotIn('case study', record['question'].casefold(), f'set {n}')
                self.assertIn(record['kind'], ('S', 'M2'), f'set {n}')
                self.assertTrue(record['question'].endswith('?') or record['question'].endswith('Select two.'))

    def test_sample_upload_matches_builder(self):
        path = ROOT / '05-sample-upload/sample-upload.csv'
        with path.open(encoding='utf-8-sig', newline='') as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 6)
        self.assertEqual(list(rows[0]), HEADER)
        built, mapping = make_rows(1)
        by_question = {row['Question']: row for row in built}
        domains = []
        for written in rows:
            source = by_question[written['Question']]
            self.assertEqual(written['Correct Answers'], source['Correct Answers'])
            for i in range(1, 7):
                self.assertEqual(written[f'Answer Option {i}'], source[f'Answer Option {i}'])
            domains.append(written['Domain'])
        self.assertEqual(len(set(domains)), 6, 'one item per official domain')
        types = Counter(row['Question Type'] for row in rows)
        self.assertEqual(types, Counter({'multiple-choice': 4, 'multi-select': 2}))


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
            self.assertEqual(len(HEADER), 17, path.name)

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
            self.assertNotIn('Case study', text)
            self.assertIn('## Answer key and explanations', text)

    def test_set_readme_states_mix(self):
        for n in range(1, 7):
            text = (ROOT / f'03-practice-sets/set-{n}/README.md').read_text(encoding='utf-8')
            self.assertIn('100 original items', text)
            self.assertIn('16 multi-select', text)
            self.assertIn('passing score not published', text)
            self.assertIn('50-60 question range', text)
            self.assertIn('no case-study component', text)

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
                         '04-resources/SUMMARY.md', '05-sample-upload/README.md']:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_no_case_study_documents(self):
        self.assertFalse((ROOT / '04-resources/case-studies.md').exists())
        self.assertFalse((ROOT / '04-resources/case-study-upload-guide.md').exists())
        self.assertFalse(list(ROOT.glob('03-practice-sets/set-*/case-embedded-*.csv')))

    def test_landing_page_has_no_stale_counts(self):
        text = (ROOT / '01-landing-page/landing-page.md').read_text(encoding='utf-8')
        self.assertIn('600 original questions', text)
        self.assertIn('12 / 16 / 21 / 20 / 18 / 13', text)
        self.assertNotIn('50 questions', text)
        self.assertIn('Welcome Message', text)
        self.assertIn('Congratulations Message', text)
        self.assertIn('Practice percentages are not scaled scores', text)
        self.assertNotIn('PL-300', text)
        self.assertNotIn('Cloud Architect', text)
        for n in range(1, 7):
            self.assertIn(TOPICS[n], text)
            self.assertIn(f'practice-test-{n}', text)

    @unittest.skipUnless(ZIP.is_file(), 'package.py has not been run')
    def test_zip_contents_and_timestamps(self):
        with zipfile.ZipFile(ZIP) as z:
            names = z.namelist()
            for n in range(1, 7):
                self.assertIn(f'03-practice-sets/set-{n}/practice-set-{n}.csv', names)
            self.assertIn('01-landing-page/landing-page.md', names)
            self.assertIn('04-resources/answer-manifest.json', names)
            self.assertFalse(any('case-studies' in n for n in names))
            self.assertTrue(all(i.date_time == (1980, 1, 1, 0, 0, 0) for i in z.infolist()))
            self.assertFalse(any('__pycache__' in n for n in names))
            self.assertFalse(any(n.endswith('.zip') for n in names))


if __name__ == '__main__':
    unittest.main()
