"""Integration checks against the actual delivered files, not only in-memory rows."""
import csv
import json
import tempfile
import unittest
from pathlib import Path
from build import ROOT, HEADER, make_rows, render_test
from package import check_companion_files
from validate import validate_files


class ArtifactTests(unittest.TestCase):
    def test_delivered_csvs(self):
        paths = sorted((ROOT / '03-practice-sets').glob('set-*/practice-set-*.csv'))
        self.assertEqual(len(paths), 6)
        errors, summaries = validate_files(paths)
        self.assertEqual(errors, [])
        self.assertEqual(sum(s['questions'] for s in summaries), 600)

    def test_companion_files_are_current(self):
        check_companion_files()

    def test_readable_copies_match_sources(self):
        for number in range(1, 7):
            rows, _ = make_rows(number)
            path = ROOT / f'03-practice-sets/set-{number}/practice-set-{number}.md'
            self.assertEqual(path.read_text(encoding='utf-8'), render_test(number, rows))

    def test_manifest_tracks_displayed_answers(self):
        manifest = json.loads((ROOT / '04-resources/answer-manifest.json').read_text(encoding='utf-8'))
        for number in range(1, 7):
            path = ROOT / f'03-practice-sets/set-{number}/practice-set-{number}.csv'
            with path.open(encoding='utf-8-sig', newline='') as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(len(manifest[str(number)]), len(rows))
            for row, entry in zip(rows, manifest[str(number)]):
                actual = {entry['option_terms'][int(i)-1] for i in row['Correct Answers'].split(',')}
                self.assertEqual(actual, set(entry['correct_terms']))

    def test_reordered_header_rejected(self):
        rows, _ = make_rows(1)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'practice-set-1.csv'
            with path.open('w', encoding='utf-8-sig', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=list(reversed(HEADER)))
                writer.writeheader()
                writer.writerows(rows)
            errors, _ = validate_files([path])
            self.assertTrue(any('header/order' in error for error in errors))


if __name__ == '__main__':
    unittest.main()
