import re
import unittest
from bank import ITEMS,OVERRIDES,TERMS
from build import ROOT,WEIGHTS,GUIDE,check_source,make_rows

class CourseTests(unittest.TestCase):
    def test_source_and_blueprint(self):
        check_source()
        self.assertEqual(WEIGHTS,{1:30,2:35,3:20,4:15})
        self.assertEqual(len(OVERRIDES),24)
        self.assertTrue(all(i['correct']==1 for i in ITEMS))

    def test_metadata_and_template_sections(self):
        text=(ROOT/'01-landing-page/landing-page.md').read_text(encoding='utf-8')
        for number,limit in [(1,60),(2,120)]:
            part=text.split(f'### {number}. ',1)[1]
            value=re.search(r'```text\n(.*?)\n```',part,re.S)[1]
            self.assertLessEqual(len(value),limit)
        for number in range(1,7): self.assertIn(f'### {number}. ',text)
        for heading in ['Welcome Message','Congratulations Message','Frequently Asked Questions']:
            self.assertIn(heading,text)

    def test_financial_answers(self):
        values={
          1:f'{24000//(12000-4000)} months',
          2:f'{(100000-80000)*100//80000}%',
          3:'The $0.03 option, at about $0.033 per accepted output',
          4:f'{(20-15)*100//20}%',
          5:f'{100000/(60000-20000)} years',
          6:f'${10000*.01+300+500:,.0f}',
        }
        self.assertLess(.03/.9,.02/.5)
        for number,answer in values.items():
            with self.subTest(set=number):
                record=OVERRIDES[(number,88)]
                self.assertEqual(TERMS[record['keys'][0]][0],answer)
                rows,mapping=make_rows(number)
                index=next(i for i,m in enumerate(mapping) if m['objective']==88)
                row=rows[index]
                self.assertEqual(row[f"Answer Option {row['Correct Answers']}"],answer)

    def test_objective_reference_coverage(self):
        expected={'1.1','1.2','1.3','1.4','2.1','2.2','2.3','2.4','2.5','3.1','3.2','3.3','4.1','4.2','4.3'}
        self.assertEqual({i['task'] for i in ITEMS},expected)
        for number in range(1,7):
            rows,mapping=make_rows(number)
            for row,entry in zip(rows,mapping):
                self.assertIn(f"objective {entry['task']}: {GUIDE}",row['Overall Explanation'])

if __name__=='__main__': unittest.main()
