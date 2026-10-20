"""Regression checks for validator acceptance and common corruption cases."""
import copy
import unittest
from build import make_rows
from validate import validate_rows

class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.rows, _ = make_rows(1)

    def test_all_six_sets(self):
        for n in range(1, 7):
            with self.subTest(set=n):
                rows, _ = make_rows(n)
                self.assertEqual(validate_rows(rows, rows), [])

    def corrupt(self, mutate):
        changed = copy.deepcopy(self.rows)
        mutate(changed)
        self.assertTrue(validate_rows(changed, self.rows))

    def test_missing_row(self):
        self.corrupt(lambda rows: rows.pop())

    def test_out_of_bounds_answer(self):
        self.corrupt(lambda rows: rows[0].update({'Correct Answers': '6'}))

    def test_duplicate_answer_indices(self):
        self.corrupt(lambda rows: next(r for r in rows if r['Question Type'] == 'multi-select').update({'Correct Answers': '1,1'}))

    def test_duplicate_question(self):
        self.corrupt(lambda rows: rows[1].update({'Question': rows[0]['Question']}))

    def test_duplicate_option(self):
        self.corrupt(lambda rows: rows[0].update({'Answer Option 2': rows[0]['Answer Option 1']}))

    def test_missing_explanation(self):
        self.corrupt(lambda rows: rows[0].update({'Explanation 1': ''}))

    def test_missing_reference(self):
        self.corrupt(lambda rows: rows[0].update({'Overall Explanation': 'No reference.'}))

    def test_wrong_domain(self):
        self.corrupt(lambda rows: rows[0].update({'Domain': 'Other'}))

    def test_source_key_drift(self):
        def mutate(rows):
            row = next(r for r in rows if r['Question Type'] == 'multiple-choice')
            row['Correct Answers'] = str(int(row['Correct Answers']) % 4 + 1)
        self.corrupt(mutate)

    def test_missing_multi_instruction(self):
        self.corrupt(lambda rows: next(r for r in rows if r['Question Type'] == 'multi-select').update({'Question': 'Choose some controls.'}))

if __name__ == '__main__':
    unittest.main()
