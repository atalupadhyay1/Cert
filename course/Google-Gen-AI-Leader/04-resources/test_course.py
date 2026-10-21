"""Regression checks for the topical rewrite; not independent factual certification."""
import re
import unittest
from collections import Counter
from bank import BANK, TERMS, TOPICS, VALID_TASKS
from build import ROOT, OFFICIAL_WEIGHTS, GUIDE, check_source, make_rows

class CourseTests(unittest.TestCase):
    def test_source_and_topical_structure(self):
        check_source()
        self.assertEqual(set(BANK),set(range(1,7)))
        self.assertTrue(all(len(records)==100 for records in BANK.values()))
        self.assertEqual(OFFICIAL_WEIGHTS,{1:30,2:35,3:20,4:15})
        for number in BANK:
            # Topical tests must not silently regress to mixed-domain forms.
            self.assertNotEqual(Counter(r['domain'] for r in BANK[number]),Counter(OFFICIAL_WEIGHTS))
        self.assertEqual(len({r['id'] for records in BANK.values() for r in records}),600)

    def test_metadata_and_template_sections(self):
        text=(ROOT/'01-landing-page/landing-page.md').read_text(encoding='utf-8')
        for number,limit in [(1,60),(2,120)]:
            part=text.split(f'### {number}. ',1)[1]
            value=re.search(r'```text\n(.*?)\n```',part,re.S)[1]
            self.assertLessEqual(len(value),limit)
        for number in range(1,7):self.assertIn(f'### {number}. ',text)
        for heading in ['Welcome Message','Congratulations Message','Frequently Asked Questions']:
            self.assertIn(heading,text)
        self.assertIn('not six mixed exam-weighted mocks',text)
        self.assertNotIn('6 mixed-domain practice tests',text)

    def test_financial_answers(self):
        expected={21:'pay3',22:'roi25',23:'time25',24:'total900',25:'accepta',
                  26:'net14',27:'capacity100',28:'pct60',29:'costdouble',30:'budget80'}
        labels={21:f'{24000//8000} months',22:f'{(150000-120000)*100//120000}%',
                23:f'{(12-9)*100//12}% time reduction',24:f'${500+250+150} per month',
                26:f'${20000-6000:,} monthly net benefit',
                27:f'{5*1200//60} hours of released capacity per month',
                28:f'{600*100//1000}% successful completion rate',
                30:f'{int(4000/.05):,} requests per month'}
        self.assertLess(.03/.9,.02/.5)
        self.assertEqual(3*(2/3),2)
        rows,mapping=make_rows(6)
        for question,key in expected.items():
            with self.subTest(question=question):
                self.assertEqual(BANK[6][question-1]['keys'][0],key)
                row=rows[question-1]
                self.assertEqual(row[f"Answer Option {row['Correct Answers']}"],TERMS[key][0])
                if question in labels:self.assertEqual(TERMS[key][0],labels[question])

    def test_objective_reference_coverage(self):
        self.assertEqual({r['task'] for records in BANK.values() for r in records},VALID_TASKS)
        for number in range(1,7):
            rows,mapping=make_rows(number)
            for row,entry in zip(rows,mapping):
                self.assertIn(f"objective {entry['task']}: {GUIDE}",row['Overall Explanation'])
                self.assertEqual(entry['topic'],TOPICS[number])

    def test_source_specific_rationale_in_feedback(self):
        for number,records in BANK.items():
            rows,_=make_rows(number)
            for row,record in zip(rows,records):
                for i in range(1,5):
                    self.assertIn(record['reason'],row[f'Explanation {i}'])
                self.assertEqual(sum(row[f'Explanation {i}'].startswith('Correct.') for i in range(1,5)),1)

    def test_material_accuracy_disclosures(self):
        text=(ROOT/'04-resources/sources-and-coverage.md').read_text()
        for phrase in ['Frozen inference weights','overflow behavior','technical detail',
                       'not a new live verification','not Google prices']:
            # Specific wording maintained in source documentation.
            if phrase=='not a new live verification':phrase='does not claim a new live verification'
            self.assertIn(phrase,text)

    def test_build_is_deterministic(self):
        for n in range(1,7):self.assertEqual(make_rows(n),make_rows(n))

if __name__=='__main__':unittest.main()
