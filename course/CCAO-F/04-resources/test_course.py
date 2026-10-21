"""CCAO-F scope and delivered-artifact regression checks, not psychometric certification."""
import codecs
import csv
import re
import unittest
from collections import Counter
from bank import BANK, TERMS, TOPICS, VALID_TASKS, SKILLS, ALLOCATIONS, DOMAINS, OFFICIAL_WEIGHTS
from build import ROOT, HEADER, check_source, make_rows
from sources import GUIDE

class CourseTests(unittest.TestCase):
    def test_source_scope(self):
        check_source()
        self.assertEqual(set(BANK), set(range(1,7)))
        self.assertEqual(sum(map(len,BANK.values())),600)
        ids=[r['id'] for rs in BANK.values() for r in rs]
        self.assertEqual(len(set(ids)),600)

    def test_allocations_and_official_weights(self):
        self.assertEqual(OFFICIAL_WEIGHTS,{1:14,2:21,3:12,4:16,5:12,6:15,7:10})
        self.assertEqual(sum(OFFICIAL_WEIGHTS.values()),100)
        self.assertEqual(ALLOCATIONS[6],OFFICIAL_WEIGHTS)
        self.assertEqual(ALLOCATIONS[3],{3:50,5:50})
        self.assertEqual(ALLOCATIONS[5],{6:60,7:40})
        for n in BANK:
            self.assertEqual(Counter(r['domain'] for r in BANK[n]),Counter(ALLOCATIONS[n]))
        self.assertEqual(len(DOMAINS),7)

    def test_all_local_skills_are_used_and_documented(self):
        self.assertEqual(len(VALID_TASKS),32)
        self.assertEqual(set(SKILLS),VALID_TASKS)
        self.assertEqual({r['task'] for rs in BANK.values() for r in rs},VALID_TASKS)
        text=(ROOT/'04-resources/sources-and-coverage.md').read_text()
        for k,v in SKILLS.items():
            self.assertIn(f'| {k} |',text)
            self.assertIn(v,text)
        for phrase in ['local study-map IDs','not official numbers','all 32 local study areas']:
            self.assertIn(phrase,text.lower() if phrase=='all 32 local study areas' else text)

    def test_landing_metadata_and_required_copy(self):
        text=(ROOT/'01-landing-page/landing-page.md').read_text()
        blocks={}
        for n in range(1,7):
            self.assertIn(f'### {n}. ',text)
            for heading in ['## 📣 Welcome Message','## 🎉 Congratulations Message','## ❓ Frequently Asked Questions']:
                self.assertIn(heading,text)
        for n,limit in [(1,60),(2,120)]:
            value=re.search(r'```text\n(.*?)\n```',text.split(f'### {n}. ',1)[1],re.S)[1]
            self.assertLessEqual(len(value),limit)
        for phrase in ['multiple-choice and multiple-response','60 items in 120 minutes','$99','720 on a 100–1,000 scaled range',
                       'not a raw percentage conversion','12 months','no mandatory prerequisites','December 7, 2026','November 17, 2026',
                       'not an exact exam replica','32 local study-map skills']:
            self.assertIn(phrase,text)

    def test_source_mappings_and_case_explanations(self):
        for n,records in BANK.items():
            sources={r['id']:r for r in records}
            rows,mapping=make_rows(n)
            for row,entry in zip(rows,mapping):
                source=sources[entry['id']]
                self.assertEqual(entry['topic'],TOPICS[n])
                self.assertIn('Local study-map skill '+source['task'],row['Overall Explanation'])
                self.assertIn(SKILLS[source['task']],row['Overall Explanation'])
                self.assertIn(GUIDE,row['Overall Explanation'])
                self.assertEqual(row[f"Answer Option {row['Correct Answers']}"],TERMS[source['keys'][0]][0])
                for i in range(1,5):
                    self.assertIn(source['reason'],row[f'Explanation {i}'])
                self.assertEqual(sum(row[f'Explanation {i}'].startswith('Correct.') for i in range(1,5)),1)

    def test_illustrative_workflow_arithmetic(self):
        baseline,drafting,review,rework=50,20,10,5
        self.assertEqual(baseline-(drafting+review+rework),15)
        rows,mapping=make_rows(4)
        match=[row for row,entry in zip(rows,mapping) if entry['correct_terms']==['time15']]
        self.assertEqual(len(match),1)
        self.assertEqual(match[0][f"Answer Option {match[0]['Correct Answers']}"],TERMS['time15'][0])
        text=(ROOT/'04-resources/questions/4.txt').read_text()
        self.assertIn('net time saved',text)
        self.assertIn('35 minutes',TERMS['time15'][1])

    def test_version_format_and_scoring_notes(self):
        text=(ROOT/'04-resources/sources-and-coverage.md').read_text()
        for phrase in ['July 2026','December 7, 2026','November 17, 2026','60','120 minutes',
                       'multiple-response','720','100–1,000','$99','12 months',
                       'must not be described as 72% correct','multiple-response items and 60 items in 120 minutes']:
            self.assertIn(phrase,text)
        self.assertIn('Not endorsed by Anthropic or Udemy',text)
        for path in ROOT.rglob('*.py'):
            self.assertNotIn('CC'+'DV-F',path.read_text())

    def test_csv_bytes_and_header(self):
        for n in range(1,7):
            path=ROOT/f'03-practice-sets/set-{n}/practice-set-{n}.csv'
            data=path.read_bytes()
            self.assertTrue(data.startswith(codecs.BOM_UTF8))
            self.assertNotIn(b'\r\n',data)
            with path.open(encoding='utf-8-sig',newline='') as f:
                reader=csv.reader(f);self.assertEqual(next(reader),HEADER);rows=list(reader)
            self.assertEqual(len(rows),100)
            self.assertTrue(all(len(row)==17 for row in rows))

    def test_local_markdown_links(self):
        for path in ROOT.rglob('*.md'):
            for link in re.findall(r'\]\(([^)]+)\)',path.read_text()):
                if '://' not in link and not link.startswith('#'):
                    self.assertTrue((path.parent/link.split('#')[0]).exists(),f'{path}: {link}')

    def test_deterministic_exports_and_mixed_order(self):
        for n in BANK:self.assertEqual(make_rows(n),make_rows(n))
        _,mapping=make_rows(6)
        self.assertNotEqual([x['id'] for x in mapping],[r['id'] for r in BANK[6]])
        self.assertEqual({x['id'] for x in mapping},{r['id'] for r in BANK[6]})

if __name__=='__main__':unittest.main()
