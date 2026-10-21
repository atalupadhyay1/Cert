"""Course-specific regression checks; factual and psychometric review remain separate."""
import codecs
import csv
import re
import unittest
from collections import Counter
from bank import BANK, TERMS, TOPICS, VALID_TASKS
from build import ROOT, OFFICIAL_WEIGHTS, HEADER, check_source, make_rows
from sources import GUIDE

class CourseTests(unittest.TestCase):
    def test_source_scope(self):
        check_source()
        self.assertEqual(set(BANK),set(range(1,7)))
        self.assertEqual(sum(len(rs) for rs in BANK.values()),600)
        ids=[r['id'] for rs in BANK.values() for r in rs]
        self.assertEqual(len(set(ids)),600)
        self.assertTrue(all(len(rs)==100 for rs in BANK.values()))

    def test_focused_domains_and_integrated_blueprint(self):
        self.assertEqual(OFFICIAL_WEIGHTS,{1:27,2:18,3:20,4:20,5:15})
        for n in range(1,6):
            self.assertEqual(Counter(r['domain'] for r in BANK[n]),{n:100})
        self.assertEqual(Counter(r['domain'] for r in BANK[6]),Counter(OFFICIAL_WEIGHTS))

    def test_all_thirty_objectives(self):
        self.assertEqual(len(VALID_TASKS),30)
        self.assertEqual({r['task'] for rs in BANK.values() for r in rs},VALID_TASKS)

    def test_metadata_and_reference_template(self):
        text=(ROOT/'01-landing-page/landing-page.md').read_text(encoding='utf-8')
        for n,limit in [(1,60),(2,120)]:
            part=text.split(f'### {n}. ',1)[1]
            value=re.search(r'```text\n(.*?)\n```',part,re.S)[1]
            self.assertLessEqual(len(value),limit)
        for n in range(1,7):self.assertIn(f'### {n}. ',text)
        for phrase in ['Welcome Message','Congratulations Message','Frequently Asked Questions',
                       'multiple-response','200 minutes','80%','not a raw percentage conversion']:
            self.assertIn(phrase,text)
        self.assertNotIn('six identical weighted mocks',text)

    def test_source_reason_and_guide_reference_in_exports(self):
        for n,records in BANK.items():
            by_id={r['id']:r for r in records}
            rows,mapping=make_rows(n)
            for row,entry in zip(rows,mapping):
                source=by_id[entry['id']]
                self.assertEqual(entry['topic'],TOPICS[n])
                self.assertIn(f"objective {source['task']}: {GUIDE}",row['Overall Explanation'])
                self.assertEqual(row[f"Answer Option {row['Correct Answers']}"],TERMS[source['keys'][0]][0])
                for i in range(1,5):self.assertIn(source['reason'],row[f'Explanation {i}'])
                self.assertEqual(sum(row[f'Explanation {i}'].startswith('Correct.') for i in range(1,5)),1)

    def test_illustrative_arithmetic(self):
        rows,mapping=make_rows(4)
        expected={'cost60':f'${120*.5:.0f}', 'hours6':f'{30-24} hours',
                  'retry25':f'{100-75} items'}
        for key,label in expected.items():
            matches=[(row,entry) for row,entry in zip(rows,mapping) if entry['correct_terms']==[key]]
            self.assertEqual(len(matches),1)
            row,entry=matches[0]
            self.assertEqual(row[f"Answer Option {row['Correct Answers']}"],label)
        source=(ROOT/'04-resources/questions/4.txt').read_text()
        self.assertIn('not live prices',source)
        self.assertIn('does not establish a service SLA',source)

    def test_current_version_and_safety_notes(self):
        text=(ROOT/'04-resources/sources-and-coverage.md').read_text()
        for phrase in ['**Task**','**Agent**','/memory','/context','Post-tool normalization',
                       'schema validity','permission','not a provider latency guarantee']:
            if phrase=='schema validity':phrase='Schema validity'
            if phrase=='not a provider latency guarantee':phrase='not current provider prices or guaranteed delivery'
            self.assertIn(phrase,text)

    def test_csv_bytes_and_header(self):
        for n in range(1,7):
            path=ROOT/f'03-practice-sets/set-{n}/practice-set-{n}.csv'
            data=path.read_bytes()
            self.assertTrue(data.startswith(codecs.BOM_UTF8))
            self.assertNotIn(b'\r\n',data)
            with path.open(encoding='utf-8-sig',newline='') as f:
                reader=csv.reader(f)
                self.assertEqual(next(reader),HEADER)
                rows=list(reader)
            self.assertEqual(len(rows),100)
            self.assertTrue(all(len(row)==17 for row in rows))

    def test_local_markdown_links(self):
        for path in ROOT.rglob('*.md'):
            for link in re.findall(r'\]\(([^)]+)\)',path.read_text()):
                if '://' not in link and not link.startswith('#'):
                    self.assertTrue((path.parent/link.split('#')[0]).exists(),f'{path}: {link}')

    def test_deterministic_exports_and_mixed_final_order(self):
        for n in range(1,7):self.assertEqual(make_rows(n),make_rows(n))
        _,mapping=make_rows(6)
        self.assertNotEqual([x['id'] for x in mapping],[r['id'] for r in BANK[6]])
        self.assertEqual({x['id'] for x in mapping},{r['id'] for r in BANK[6]})

if __name__=='__main__':unittest.main()
