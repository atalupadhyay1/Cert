"""Course-specific blueprint, metadata, and arithmetic regression checks."""
import re
import unittest
from bank import ITEMS, OVERRIDES, TERMS
from build import ROOT, WEIGHTS, RANGES, check_source, make_rows

class CourseTests(unittest.TestCase):
    def test_source_invariants(self):
        check_source()
        self.assertEqual(len(OVERRIDES),18)
        self.assertEqual(sum(WEIGHTS.values()),100)
        for domain,count in WEIGHTS.items():
            low,high=RANGES[domain]
            self.assertTrue(low<=count<=high)

    def test_metadata_lengths(self):
        text=(ROOT/'01-landing-page/landing-page.md').read_text(encoding='utf-8')
        for number,limit in [(1,60),(2,120)]:
            section=text.split(f'### {number}. ',1)[1]
            value=re.search(r'```text\n(.*?)\n```',section,re.S)[1]
            self.assertLessEqual(len(value),limit)
        for number in range(1,7):
            self.assertIn(f'### {number}. ',text)
        self.assertIn('Welcome Message',text)
        self.assertIn('Congratulations Message',text)

    def test_calculation_answers(self):
        calculations = {
            (1,61): f'{max(4,7,5)+3} seconds',
            (2,62): f'{90//3} tasks per minute',
            (3,68): f'{10000*(100-99)//100} unsuccessful runs',
            (4,70): f'{(8000+2000)*120:,} tokens',
            (5,54): str(4/5),
            (6,72): f'A decrease of {(180-170)*100//200} percentage points',
        }
        for coordinates,answer in calculations.items():
            with self.subTest(case=coordinates):
                record=OVERRIDES[coordinates]
                self.assertEqual(TERMS[record['keys'][0]][0],answer)
                rows,mapping=make_rows(coordinates[0])
                index=next(i for i,m in enumerate(mapping) if m['objective']==coordinates[1])
                self.assertEqual(rows[index][f"Answer Option {rows[index]['Correct Answers']}"],answer)

    def test_reference_task_coverage(self):
        self.assertEqual(len({i['task'] for i in ITEMS}),12)
        for number in range(1,7):
            rows,mapping=make_rows(number)
            for row,entry in zip(rows,mapping):
                self.assertIn('study-guides/ai-500#'+entry['task'],row['Overall Explanation'])

if __name__=='__main__':
    unittest.main()
