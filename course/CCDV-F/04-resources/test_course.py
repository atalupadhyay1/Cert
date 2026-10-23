"""Developer scope and delivered-artifact regression checks, not psychometric certification."""
import codecs
import csv
import re
import unittest
from collections import Counter
from bank import BANK, TERMS, TOPICS, VALID_TASKS, SKILLS, ALLOCATIONS, DOMAINS
from build import ROOT, OFFICIAL_WEIGHTS, HEADER, check_source, make_rows
from sources import GUIDE

class CourseTests(unittest.TestCase):
    def test_source_scope(self):
        check_source()
        self.assertEqual(set(BANK), set(range(1,7)))
        self.assertEqual(sum(map(len,BANK.values())),600)
        ids=[r['id'] for rs in BANK.values() for r in rs]
        self.assertEqual(len(set(ids)),600)

    def test_allocations_and_weights(self):
        self.assertEqual(OFFICIAL_WEIGHTS,{1:14.7,2:33.1,3:3.1,4:2.6,5:16.8,6:11.0,7:8.1,8:10.6})
        self.assertAlmostEqual(sum(OFFICIAL_WEIGHTS.values()),100)
        self.assertEqual(ALLOCATIONS[6],{1:15,2:33,3:3,4:3,5:17,6:11,7:8,8:10})
        for n in BANK:self.assertEqual(Counter(r['domain'] for r in BANK[n]),Counter(ALLOCATIONS[n]))
        self.assertEqual(len(DOMAINS),8)

    def test_all_twenty_five_named_skills(self):
        self.assertEqual(len(VALID_TASKS),25)
        self.assertEqual(set(SKILLS),VALID_TASKS)
        self.assertEqual({r['task'] for rs in BANK.values() for r in rs},VALID_TASKS)
        text=(ROOT/'04-resources/sources-and-coverage.md').read_text()
        for k,v in SKILLS.items():self.assertIn(f'| {k} | {v} |',text)
        self.assertIn('local study-map IDs',text)

    def test_metadata_matches_reference_structure(self):
        text=(ROOT/'01-landing-page/landing-page.md').read_text()
        for n,limit in [(1,60),(2,120)]:
            value=re.search(r'```text\n(.*?)\n```',text.split(f'### {n}. ',1)[1],re.S)[1]
            self.assertLessEqual(len(value),limit)
        for n in range(1,7):self.assertIn(f'### {n}. ',text)
        for phrase in ['Welcome Message','Congratulations Message','Frequently Asked Questions',
                       'multiple-response','200 minutes','80%','not a raw percentage conversion']:
            self.assertIn(phrase,text)

    def test_source_mappings_and_case_explanations(self):
        for n,records in BANK.items():
            sources={r['id']:r for r in records}
            rows,mapping=make_rows(n)
            for row,entry in zip(rows,mapping):
                source=sources[entry['id']]
                self.assertEqual(entry['topic'],TOPICS[n])
                self.assertIn(f"Local study-map skill {source['task']} ({SKILLS[source['task']]}), mapped to the official guide: {GUIDE}",row['Overall Explanation'])
                self.assertEqual(row[f"Answer Option {row['Correct Answers']}"],TERMS[source['keys'][0]][0])
                for i in range(1,5):self.assertIn(source['reason'],row[f'Explanation {i}'])
                self.assertEqual(sum(row[f'Explanation {i}'].startswith('Correct.') for i in range(1,5)),1)

    def test_illustrative_arithmetic(self):
        self.assertAlmostEqual(300000/1e6*2+200000/1e6*6,1.8)
        self.assertEqual(16000-3000-2000,11000)
        self.assertLess(.02/.8,.015/.5)
        self.assertEqual(60000/100000,.6)
        rows,mapping=make_rows(3)
        for key in ['bill180','reserve11','acceptdev','cache60']:
            matches=[row for row,entry in zip(rows,mapping) if entry['correct_terms']==[key]]
            self.assertEqual(len(matches),1)
            self.assertEqual(matches[0][f"Answer Option {matches[0]['Correct Answers']}"],TERMS[key][0])
        text=(ROOT/'04-resources/questions/3.txt').read_text()
        for phrase in ['hypothetical rates','shared 16,000-token budget','Ignoring other costs','not automatically savings']:
            self.assertIn(phrase,text)

    def test_version_and_safety_notes(self):
        text=(ROOT/'04-resources/sources-and-coverage.md').read_text()
        for phrase in ['July 2026','December 7, 2026','November 17, 2026','53 items','12 months',
                       '**SSE**','**Post-tool normalization**','allowed-tools','not a raw percentage conversion']:
            self.assertIn(phrase,text)
        for path in ROOT.rglob('*.py'):
            self.assertNotIn('CC'+'AR-F',path.read_text())

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
