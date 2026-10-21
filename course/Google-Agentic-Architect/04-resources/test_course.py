"""PAA scope and delivered-artifact regression checks, not psychometric certification."""
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
        self.assertEqual(OFFICIAL_WEIGHTS,{1:13,2:17,3:33,4:22,5:15})
        self.assertEqual(sum(OFFICIAL_WEIGHTS.values()),100)
        self.assertEqual(ALLOCATIONS[6],{1:13,2:17,3:33,4:22,5:15})
        self.assertEqual(ALLOCATIONS[1],{1:50,2:50})
        self.assertEqual(ALLOCATIONS[2],{3:100})
        self.assertEqual(ALLOCATIONS[3],{3:100})
        for n in BANK:
            self.assertEqual(Counter(r['domain'] for r in BANK[n]),Counter(ALLOCATIONS[n]))
        self.assertEqual(len(DOMAINS),5)

    def test_all_local_skills_used_and_documented(self):
        self.assertEqual(len(VALID_TASKS),32)
        self.assertEqual(set(SKILLS),VALID_TASKS)
        self.assertEqual({r['task'] for rs in BANK.values() for r in rs},VALID_TASKS)
        text=(ROOT/'04-resources/sources-and-coverage.md').read_text()
        for k,v in SKILLS.items():
            self.assertIn(f'| {k} |',text)
            self.assertIn(v,text)
        for phrase in ['local study-map IDs','not official numbers','All 32 local study areas']:
            self.assertIn(phrase,text)

    def test_landing_metadata_and_required_copy(self):
        text=(ROOT/'01-landing-page/landing-page.md').read_text()
        for n in range(1,7):
            self.assertIn(f'### {n}. ',text)
        for heading in ['## 📣 Welcome Message','## 🎉 Congratulations Message','## ❓ Frequently Asked Questions']:
            self.assertIn(heading,text)
        for n,limit in [(1,60),(2,120)]:
            value=re.search(r'```text\n(.*?)\n```',text.split(f'### {n}. ',1)[1],re.S)[1]
            self.assertLessEqual(len(value),limit)
        for phrase in ['roughly 80 questions','3 hours','$120','mid-November 2026','2-hour',
                       '$200','1 year','no prerequisites','hands-on labs',
                       'does not earn the credential','13%','17%','33%','22%','15%',
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

    def test_version_and_hybrid_format_notes(self):
        text=(ROOT/'04-resources/sources-and-coverage.md').read_text()
        for phrase in ['September 8–30, 2026','mid-November 2026','3 hours','roughly 80 questions',
                       '$120','$200','2-hour session','1 year','does **not** grant certification',
                       'raw percentage pass threshold','31 considerations','28 in-scope tools']:
            self.assertIn(phrase,text)
        self.assertIn('Not endorsed by Google',text)
        for path in ROOT.rglob('*.py'):
            body=path.read_text()
            self.assertNotIn('CC'+'DV-F',body)
            self.assertNotIn('CC'+'AO-F',body)

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
