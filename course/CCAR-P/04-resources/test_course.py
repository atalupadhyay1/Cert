"""Structural, blueprint-allocation, question-pattern, and artifact tests for CCAR-P."""
import copy
import csv
import json
import re
import unittest
import zipfile
from collections import Counter

from bank import (ALLOCATIONS, BANK, DOMAINS, ITEM_TOTAL, KIND_PLAN,
                  MULTI_PLAN, OFFICIAL_WEIGHTS, PATTERN_MATRIX_FLOOR,
                  SKILL_PLAN, SKILLS, TOPICS, VALID_TASKS,
                  is_matrix_adapted_stem)
from build import (ALLOWED_TYPES, EXPORT_PLAN, HEADER, ROOT, TYPE_PLAN,
                   make_rows, render_test)
from terms import TERMS
from validate import validate_rows

ZIP = ROOT / 'CCAR-P-6x63.zip'


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
        target = next(r for r in self.rows if r['Question Type'] == 'multiple-choice')
        self.corrupt(lambda r: next(x for x in r if x['Question'] == target['Question']).update({'Correct Answers': '5'}))

    def test_two_indices_on_single_choice(self):
        target = next(r for r in self.rows if r['Question Type'] == 'multiple-choice')
        self.corrupt(lambda r: next(x for x in r if x['Question'] == target['Question']).update({'Correct Answers': '1,2'}))

    def test_multi_select_without_stated_count(self):
        target = next(r for r in self.rows if r['Question Type'] == 'multi-select')
        self.corrupt(lambda r: next(x for x in r if x['Question'] == target['Question']).update({'Question': 'Which options apply here?'}))

    def test_multi_select_key_count_mismatch(self):
        target = next(r for r in self.rows if r['Question Type'] == 'multi-select')
        key = target['Correct Answers'].split(',')[0]
        self.corrupt(lambda r: next(x for x in r if x['Question'] == target['Question']).update({'Correct Answers': key}))

    def test_select_three_requires_six_options(self):
        target = next(r for r in self.rows if 'Select three.' in r['Question'])
        self.corrupt(lambda r: next(x for x in r if x['Question'] == target['Question']).update({'Answer Option 6': '', 'Explanation 6': ''}))

    def test_duplicate_question(self):
        self.corrupt(lambda r: r[1].update({'Question': r[0]['Question']}))

    def test_duplicate_option(self):
        self.corrupt(lambda r: r[0].update({'Answer Option 2': r[0]['Answer Option 1']}))

    def test_missing_explanation(self):
        self.corrupt(lambda r: r[0].update({'Explanation 1': ''}))

    def test_missing_reference(self):
        self.corrupt(lambda r: r[0].update({'Overall Explanation': 'No source link.'}))

    def test_wrong_domain(self):
        self.corrupt(lambda r: r[0].update({'Domain': 'Unknown Domain'}))

    def test_wrong_answer_from_source(self):
        def change(rows):
            row = next(x for x in rows if x['Question Type'] == 'multiple-choice')
            row['Correct Answers'] = '1' if row['Correct Answers'] != '1' else '2'
        self.corrupt(change)

    def test_unexpected_sixth_option_on_single_choice(self):
        target = next(r for r in self.rows if r['Question Type'] == 'multiple-choice')
        self.corrupt(lambda r: next(x for x in r if x['Question'] == target['Question']).update({'Answer Option 6': 'Extra', 'Explanation 6': 'Extra'}))

    def test_unbalanced_slots(self):
        def change(rows):
            for row in rows:
                if row['Question Type'] == 'multiple-choice':
                    row['Correct Answers'] = '1'
        self.corrupt(change)

    def test_case_study_wording_is_rejected(self):
        self.corrupt(lambda r: r[0].update({'Question': 'Case study — Meridian Bank: ' + r[0]['Question']}))


class SourceTests(unittest.TestCase):
    def test_every_skill_is_practised(self):
        used = {r['task'] for rows in BANK.values() for r in rows}
        self.assertEqual(used, VALID_TASKS)
        self.assertEqual(len(SKILLS), 38)

    def test_term_keys_and_labels_are_unique_and_exercised(self):
        source = (ROOT / '04-resources/terms.py').read_text(encoding='utf-8')
        keys = re.findall(r"^t\('([^']+)'", source, re.M)
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(len(keys), len(TERMS))
        labels = [v[0].casefold() for v in TERMS.values()]
        self.assertEqual(len(labels), len(set(labels)), 'all TERMS labels must be case-insensitively unique')
        exercised = {k for rows in BANK.values() for r in rows for k in r['keys']}
        self.assertEqual(exercised, set(TERMS), 'unused TERMS keys present')

    def test_published_weights_and_exact_63_item_allocation(self):
        self.assertEqual(sum(OFFICIAL_WEIGHTS.values()), 100.0)
        self.assertEqual(ITEM_TOTAL, 63)
        for n, allocation in ALLOCATIONS.items():
            self.assertEqual(sum(allocation.values()), 63)
            self.assertEqual(allocation, {1: 11, 2: 8, 3: 12, 4: 10, 5: 9, 6: 9, 7: 4})
            for domain, count in allocation.items():
                exact = OFFICIAL_WEIGHTS[domain] * ITEM_TOTAL / 100.0
                self.assertLessEqual(abs(count - exact), 0.42, f'set {n} domain {domain}')

    def test_skill_plan_matches_bank(self):
        self.assertEqual(set(SKILL_PLAN), set(SKILLS))
        self.assertEqual(sum(SKILL_PLAN.values()), ITEM_TOTAL)
        for domain in range(1, 8):
            planned = sum(v for k, v in SKILL_PLAN.items() if k.startswith(f'{domain}.'))
            self.assertEqual(planned, ALLOCATIONS[1][domain], f'domain {domain}')
        for n, records in BANK.items():
            self.assertEqual(Counter(r['task'] for r in records), Counter(SKILL_PLAN), f'set {n}')

    def test_multi_select_spread_and_arity(self):
        self.assertEqual(sum(MULTI_PLAN.values()), 15)
        self.assertEqual(KIND_PLAN, {'S': 48, 'M2': 12, 'M3': 3})
        for n, records in BANK.items():
            spread = Counter(r['domain'] for r in records if r['kind'] in ('M2', 'M3'))
            self.assertEqual(dict(spread), MULTI_PLAN, f'set {n}')
            self.assertEqual(dict(Counter(r['kind'] for r in records)), KIND_PLAN, f'set {n}')

    def test_exam_pattern_adaptations_present_in_every_set(self):
        for n, records in BANK.items():
            adapted = [r for r in records if is_matrix_adapted_stem(r['question'])]
            self.assertGreaterEqual(len(adapted), PATTERN_MATRIX_FLOOR, f'set {n}')
            stage = [r for r in records if 'pre-processing' in r['question'].casefold() and 'model stage' in r['question'].casefold()]
            suit = [r for r in records if 'candidate use cases' in r['question'].casefold() or 'candidate workflows' in r['question'].casefold()]
            prac = [r for r in records if 'sound architectural practice' in r['question'].casefold()]
            self.assertGreaterEqual(len(stage), 2, f'set {n} stage mapping')
            self.assertGreaterEqual(len(suit), 2, f'set {n} suitability')
            self.assertGreaterEqual(len(prac), 2, f'set {n} sound practice')

    def test_near_duplicate_gate_runs(self):
        from build import NEAR_DUPLICATE_LIMIT, check_source
        self.assertLessEqual(NEAR_DUPLICATE_LIMIT, 0.72)
        check_source()

    def test_item_type_plan_total_and_exact_slot_balance(self):
        self.assertEqual(TYPE_PLAN, {'multiple-choice': 48, 'multi-select': 15})
        self.assertEqual(sum(TYPE_PLAN.values()), 63)
        self.assertEqual(EXPORT_PLAN, TYPE_PLAN)
        for n in range(1, 7):
            rows, _ = make_rows(n)
            slots = Counter(int(r['Correct Answers']) for r in rows if r['Question Type'] == 'multiple-choice')
            self.assertEqual(dict(slots), {1: 12, 2: 12, 3: 12, 4: 12}, f'set {n}')

    def test_no_case_studies_or_click_paths(self):
        for n, rows in BANK.items():
            for record in rows:
                q = record['question'].casefold()
                self.assertNotIn('case study', q, f'set {n}')
                self.assertNotIn('click ', q, f'set {n}')
                self.assertNotIn('navigate to', q, f'set {n}')
                self.assertIn(record['kind'], ('S', 'M2', 'M3'), f'set {n}')
                self.assertTrue(
                    record['question'].endswith('?')
                    or record['question'].endswith('Select two.')
                    or record['question'].endswith('Select three.')
                )

    def test_sample_upload_matches_builder(self):
        path = ROOT / '05-sample-upload/sample-upload.csv'
        with path.open(encoding='utf-8-sig', newline='') as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 14)
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
        self.assertEqual(set(domains), set(DOMAINS.values()), 'all 7 official domains represented')
        types = Counter(row['Question Type'] for row in rows)
        self.assertEqual(types, Counter({'multiple-choice': 7, 'multi-select': 7}))


class ArtifactTests(unittest.TestCase):
    def test_each_exam_has_63_rows_and_17_columns(self):
        for n in range(1, 7):
            path = ROOT / f'03-practice-sets/set-{n}/practice-set-{n}.csv'
            rows = header_row(path)
            self.assertEqual(len(rows), 63, path.name)
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
            self.assertEqual(len(re.findall(r'^### \d+\. ', text, re.M)), 63)
            self.assertNotIn('Case study', text)
            self.assertIn('## Answer key and explanations', text)

    def test_set_readme_states_mix_and_policies(self):
        for n in range(1, 7):
            text = (ROOT / f'03-practice-sets/set-{n}/README.md').read_text(encoding='utf-8')
            self.assertIn('63 original items', text)
            self.assertIn('120 minutes', text)
            self.assertIn('720', text)
            self.assertIn('no split-screen multi-question block', text)

    def test_manifest_matches_builder(self):
        manifest = json.loads((ROOT / '04-resources/answer-manifest.json').read_text(encoding='utf-8'))
        for n in range(1, 7):
            _, mapping = make_rows(n)
            self.assertEqual(manifest[str(n)], mapping, f'set {n}')
        self.assertEqual(sum(len(v) for v in manifest.values()), 378)

    def test_validation_report_passes(self):
        report = json.loads((ROOT / '04-resources/validation-report.json').read_text(encoding='utf-8'))
        self.assertEqual(report['status'], 'PASS')
        self.assertEqual(report['sets'], 6)
        self.assertEqual(report['total_questions'], 378)
        self.assertEqual(report['errors'], [])

    def test_documents_exist(self):
        for relative in [
            'README.md',
            '01-landing-page/landing-page.md',
            '02-curriculum/curriculum-outline.md',
            '04-resources/sources-and-coverage.md',
            '04-resources/csv-format-spec.md',
            '04-resources/publication-checklist.md',
            '04-resources/SUMMARY.md',
            '05-sample-upload/README.md',
        ]:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_no_case_study_documents(self):
        self.assertFalse((ROOT / '04-resources/case-studies.md').exists())
        self.assertFalse((ROOT / '04-resources/case-study-upload-guide.md').exists())
        self.assertFalse(list(ROOT.glob('03-practice-sets/set-*/case-embedded-*.csv')))

    def test_landing_page_has_no_stale_counts_or_foreign_exams(self):
        text = (ROOT / '01-landing-page/landing-page.md').read_text(encoding='utf-8')
        self.assertIn('378 original questions', text)
        self.assertIn('11 / 8 / 12 / 10 / 9 / 9 / 4', text)
        self.assertIn('December 7, 2026', text)
        self.assertIn('November 17, 2026', text)
        self.assertIn('Welcome Message', text)
        self.assertIn('Congratulations Message', text)
        self.assertIn('scaled score', text)
        for foreign in ('PL-300', 'PCEP-30', 'MLA-C02', 'AIP-C01', 'Cloud Architect', 'Data Practitioner'):
            self.assertNotIn(foreign, text)
        for n in range(1, 7):
            self.assertIn(TOPICS[n], text)
            self.assertIn(f'practice-test-{n}', text)

    @unittest.skipUnless(ZIP.is_file(), 'package.py has not been run')
    def test_zip_contents_and_timestamps(self):
        with zipfile.ZipFile(ZIP) as z:
            names = z.namelist()
            self.assertEqual(len(names), 43, f'expected 43 files inside ZIP (44 total with ZIP), found {len(names)}')
            for n in range(1, 7):
                self.assertIn(f'03-practice-sets/set-{n}/practice-set-{n}.csv', names)
            self.assertIn('01-landing-page/landing-page.md', names)
            self.assertIn('04-resources/answer-manifest.json', names)
            self.assertFalse(any('case-stud' in n for n in names))
            self.assertTrue(all(i.date_time == (1980, 1, 1, 0, 0, 0) for i in z.infolist()))
            self.assertFalse(any('__pycache__' in n for n in names))
            self.assertFalse(any(n.endswith('.zip') for n in names))


if __name__ == '__main__':
    unittest.main()
