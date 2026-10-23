import copy
import unittest
from build import make_rows
from validate import validate_rows

class ValidatorTests(unittest.TestCase):
    def setUp(self): self.rows,_=make_rows(1)
    def corrupt(self,change):
        rows=copy.deepcopy(self.rows)
        change(rows)
        self.assertTrue(validate_rows(rows,self.rows))
    def test_all_six_sets(self):
        for n in range(1,7):
            rows,_=make_rows(n)
            self.assertEqual(validate_rows(rows,rows),[])
    def test_missing_row(self): self.corrupt(lambda r:r.pop())
    def test_out_of_bounds_answer(self): self.corrupt(lambda r:r[0].update({'Correct Answers':'5'}))
    def test_multiple_answer_indices(self): self.corrupt(lambda r:r[0].update({'Correct Answers':'1,2'}))
    def test_duplicate_question(self): self.corrupt(lambda r:r[1].update({'Question':r[0]['Question']}))
    def test_duplicate_option(self): self.corrupt(lambda r:r[0].update({'Answer Option 2':r[0]['Answer Option 1']}))
    def test_missing_explanation(self): self.corrupt(lambda r:r[0].update({'Explanation 1':''}))
    def test_missing_reference(self): self.corrupt(lambda r:r[0].update({'Overall Explanation':'No source.'}))
    def test_wrong_domain(self): self.corrupt(lambda r:r[0].update({'Domain':'Other'}))
    def test_wrong_answer_from_source(self):
        self.corrupt(lambda r:r[0].update({'Correct Answers':str(int(r[0]['Correct Answers'])%4+1)}))
    def test_unexpected_multiselect(self): self.corrupt(lambda r:r[0].update({'Question Type':'multi-select'}))
    def test_unused_option(self): self.corrupt(lambda r:r[0].update({'Answer Option 5':'Extra'}))

if __name__=='__main__': unittest.main()
