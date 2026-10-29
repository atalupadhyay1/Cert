"""Structural, allocation, and artifact tests for the PCEP-30-03 practice package."""
import copy
import csv
import json
import re
import unittest
import zipfile
from collections import Counter

from bank import (ALLOCATIONS, BANK, GAP_FILL_MIN, ITEM_TOTAL, MULTI_PLAN,
                  OFFICIAL_WEIGHTS, SKILLS, SKILL_PLAN, SUBTITLES, TOPICS,
                  VALID_TASKS)
from build import (ALLOWED_TYPES, EXPORT_PLAN, HEADER, ROOT, TYPE_PLAN,
                   make_rows, render_test)
from terms import TERMS
from validate import normalize, validate_rows

ZIP = ROOT / 'PCEP-30-03-6x60.zip'


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
        self.corrupt(lambda r: next(x for x in r if x['Question'] == target['Question']).update({'Question': 'Which two expressions evaluate to True?'}))

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
        self.corrupt(lambda r: r[0].update({'Question': 'Case study — Northwind: ' + r[0]['Question']}))

    def test_gap_fill_shortfall_is_rejected(self):
        def change(rows):
            for row in rows:
                if '____' in row['Question']:
                    row['Question'] = row['Question'].replace('____', 'VALUE')
        self.corrupt(change)


class SourceTests(unittest.TestCase):
    def test_every_skill_is_practised(self):
        used = {r['task'] for rows in BANK.values() for r in rows}
        self.assertEqual(used, VALID_TASKS)
        self.assertEqual(len(SKILLS), 42)

    def test_term_keys_are_unique(self):
        source = (ROOT / '04-resources/terms.py').read_text(encoding='utf-8')
        keys = re.findall(r"^t\('([^']+)'", source, re.M)
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(len(keys), len(TERMS))

    def test_all_terms_are_exercised(self):
        used = {k for rs in BANK.values() for r in rs for k in r['keys']}
        self.assertEqual(set(TERMS) - used, set())

    def test_published_weights_are_exact(self):
        # 18 + 29 + 25 + 28 = 100.
        self.assertEqual(sum(OFFICIAL_WEIGHTS.values()), 100.0)
        for n, allocation in ALLOCATIONS.items():
            self.assertEqual(sum(allocation.values()), ITEM_TOTAL)
            self.assertEqual(allocation, {1: 11, 2: 17, 3: 15, 4: 17}, f'set {n}')

    def test_each_allocation_is_within_half_an_item_of_the_weight(self):
        # Exact shares at 60 items are 10.8 / 17.4 / 15.0 / 16.8; all counts are within 0.4.
        for domain, weight in OFFICIAL_WEIGHTS.items():
            exact = weight / 100 * ITEM_TOTAL
            self.assertLessEqual(abs(ALLOCATIONS[1][domain] - exact), 0.5, domain)

    def test_skill_plan_matches_bank(self):
        self.assertEqual(set(SKILL_PLAN), set(SKILLS))
        self.assertEqual(sum(SKILL_PLAN.values()), ITEM_TOTAL)
        for domain in range(1, 5):
            planned = sum(v for k, v in SKILL_PLAN.items() if k.startswith(f'{domain}.'))
            self.assertEqual(planned, ALLOCATIONS[1][domain], f'domain {domain}')
        for n, records in BANK.items():
            self.assertEqual(Counter(r['task'] for r in records), Counter(SKILL_PLAN), f'set {n}')

    def test_multi_response_spread(self):
        self.assertEqual(sum(MULTI_PLAN.values()), 15)
        for n, records in BANK.items():
            spread = Counter(r['domain'] for r in records if r['kind'] == 'M2')
            self.assertEqual(dict(spread), MULTI_PLAN, f'set {n}')

    def test_gap_fill_approximation_count(self):
        for n, records in BANK.items():
            gaps = sum(1 for r in records if r['kind'] == 'S' and '____' in r['question'])
            self.assertGreaterEqual(gaps, GAP_FILL_MIN, f'set {n}')

    def test_near_duplicate_gate_runs(self):
        from build import NEAR_DUPLICATE_LIMIT, check_source
        self.assertLessEqual(NEAR_DUPLICATE_LIMIT, 0.75)
        check_source()

    def test_no_duplicate_stems_with_pcep_30_02(self):
        sibling = ROOT.parent / 'PCEP-30-02' / '03-practice-sets'
        if not sibling.exists():
            return
        sibling_stems = set()
        for p in sorted(sibling.glob('set-*/practice-set-*.csv')):
            with p.open(encoding='utf-8-sig', newline='') as f:
                sibling_stems.update(normalize(r['Question']) for r in csv.DictReader(f))
        own_stems = {normalize(r['question']) for rs in BANK.values() for r in rs}
        self.assertEqual(own_stems & sibling_stems, set())

    def test_item_type_plan_total(self):
        self.assertEqual(TYPE_PLAN, {'multiple-choice': 45, 'multi-select': 15})
        self.assertEqual(sum(TYPE_PLAN.values()), 60)
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
        self.assertEqual(len(rows), 12)
        self.assertEqual(list(rows[0]), HEADER)
        built, _ = make_rows(1)
        by_question = {row['Question']: row for row in built}
        domains = []
        for written in rows:
            source = by_question[written['Question']]
            self.assertEqual(written['Correct Answers'], source['Correct Answers'])
            for i in range(1, 7):
                self.assertEqual(written[f'Answer Option {i}'], source[f'Answer Option {i}'])
            domains.append(written['Domain'])
        self.assertEqual(len(set(domains)), 4, 'every official block is represented')
        types = Counter(row['Question Type'] for row in rows)
        self.assertEqual(types, Counter({'multiple-choice': 8, 'multi-select': 4}))
        self.assertEqual(sum(1 for row in rows if '____' in row['Question']), 4)


class ArtifactTests(unittest.TestCase):
    def test_each_exam_has_60_rows_and_17_columns(self):
        for n in range(1, 7):
            path = ROOT / f'03-practice-sets/set-{n}/practice-set-{n}.csv'
            rows = header_row(path)
            self.assertEqual(len(rows), 60, path.name)
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
            self.assertEqual(len(re.findall(r'^### \d+\. ', text, re.M)), 60)
            self.assertNotIn('Case study', text)
            self.assertIn('## Answer key and explanations', text)

    def test_set_readme_states_mix(self):
        for n in range(1, 7):
            text = (ROOT / f'03-practice-sets/set-{n}/README.md').read_text(encoding='utf-8')
            self.assertIn('60 original items', text)
            self.assertIn('15 multiple-response', text)
            self.assertIn('70% cumulative passing score', text)
            self.assertIn('expanded 2x bank', text)
            self.assertIn('October 31, 2026', text)
            self.assertIn('Pending Release', text)
            self.assertIn('no case-study component', text)
            self.assertIn(SUBTITLES[n], text)
            self.assertIn(TOPICS[n], text)

    def test_set_readmes_state_the_time_pressure(self):
        for n in range(1, 7):
            text = (ROOT / f'03-practice-sets/set-{n}/README.md').read_text(encoding='utf-8')
            self.assertIn('80 seconds per item', text)
            self.assertIn('cumulative average score of at least 70%', text)
            self.assertIn('30 items in 40 minutes', text)

    def test_stems_stay_inside_the_published_scope(self):
        banned = ('click ', 'navigate to', 'in the console, select',
                  'pip install ', 'class __init__', 'metaclass')
        for n, records in BANK.items():
            for record in records:
                text = f"{record['question']} {record['reason']}".casefold()
                for phrase in banned:
                    self.assertNotIn(phrase, text, f'set {n} {record["id"]}')

    def test_manifest_matches_builder(self):
        manifest = json.loads((ROOT / '04-resources/answer-manifest.json').read_text(encoding='utf-8'))
        for n in range(1, 7):
            _, mapping = make_rows(n)
            self.assertEqual(manifest[str(n)], mapping, f'set {n}')
        self.assertEqual(sum(len(v) for v in manifest.values()), 360)

    def test_validation_report_passes(self):
        report = json.loads((ROOT / '04-resources/validation-report.json').read_text(encoding='utf-8'))
        self.assertEqual(report['status'], 'PASS')
        self.assertEqual(report['sets'], 6)
        self.assertEqual(report['total_questions'], 360)
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

    def test_landing_page_has_the_mandatory_publishing_fields(self):
        text = (ROOT / '01-landing-page/landing-page.md').read_text(encoding='utf-8')
        for heading in ('### 4. What will students learn in your course?',
                        '### 5. What are the requirements or prerequisites for taking your course?',
                        '### 6. Who is this course for?'):
            self.assertIn(heading, text)
            block = text.split(heading, 1)[1].split('\n### ', 1)[0]
            self.assertGreaterEqual(block.count('\n• '), 3, heading)
        self.assertNotIn('TODO', text)
        self.assertNotIn('PLACEHOLDER', text)

    def test_landing_page_has_no_stale_counts(self):
        text = (ROOT / '01-landing-page/landing-page.md').read_text(encoding='utf-8')
        self.assertIn('360 original questions', text)
        self.assertIn('18 / 29 / 25 / 28', text)
        self.assertIn('30 questions', text)
        self.assertIn('70%', text)
        self.assertIn('October 31, 2026', text)
        self.assertIn('Pending Release', text)
        self.assertNotIn('600 questions', text)
        self.assertNotIn('450 original questions', text)
        self.assertIn('Welcome Message', text)
        self.assertIn('Congratulations Message', text)
        self.assertIn('cumulative average score of at least 70%', text)
        for other in ('PL-300', 'Professional Cloud', 'Cloud Digital Leader',
                      'AWS Solutions Architect', 'AI-102', 'DP-700', 'Cloud Practitioner',
                      'Machine Learning Engineer', 'AIP-C01', 'MLA-C02'):
            self.assertNotIn(other, text)
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
