# CSV format specification — PCEP-30-02

## File shape

- Four official syllabus blocks: `Computer Programming and Python Fundamentals`, `Control Flow – Conditional Blocks and Loops`, `Data Collections – Tuples, Dictionaries, Lists, and Strings`, and `Functions and Exceptions`.
- One file per mock exam: `practice-set-1.csv` through `practice-set-6.csv`. There is no case-embedded variant because PCEP-30-02 has no case studies.
- UTF-8 with BOM, LF line endings, comma-delimited, 17 columns, 60 data rows per exam (360 total).
- Header order is fixed and validated; reordering is rejected.

## Columns

| # | Column | Content |
|---:|---|---|
| 1 | Question | Question stem (including `____` blank on code-fill approximations); ends in `?` or `Select two.` |
| 2 | Question Type | `multiple-choice` or `multi-select` only (Udemy importer constraint) |
| 3–4 | Answer Option 1 / Explanation 1 | First populated option and its explanation |
| 5–6 | Answer Option 2 / Explanation 2 | Second populated option and its explanation |
| 7–8 | Answer Option 3 / Explanation 3 | Third populated option and its explanation |
| 9–10 | Answer Option 4 / Explanation 4 | Fourth populated option and its explanation |
| 11–12 | Answer Option 5 / Explanation 5 | Fifth option for `multi-select` items; blank otherwise |
| 13–14 | Answer Option 6 / Explanation 6 | Reserved; blank in this package |
| 15 | Correct Answers | One index (`1`–`4`) or a sorted comma-separated pair (`1,4`) |
| 16 | Overall Explanation | Answer label, rationale, option meanings, official syllabus reference, local skill, primary Python 3 reference |
| 17 | Domain | Exact official syllabus block name |

## Item-type rules enforced

| Type | Count / exam | Options | Correct Answers | Extra rule |
|---|---:|---:|---|---|
| `multiple-choice` | 45 | 4 | one index, `1`–`4` | balanced across slots 1–4; at least 15 stems include `____` |
| `multi-select` | 15 | 5 | two comma-separated indices | stem ends with `Select two.`; spread 3 / 4 / 4 / 4 across Blocks 1–4 |

Interactive drag-and-drop, sort, and multi-slot code-insertion widgets cannot be expressed in this 17-column contract and are disclosed as excluded.

## Content rules enforced

- Four or five contiguous non-empty options; no gaps and no sixth option.
- No duplicate option text inside an item.
- Every populated option has an explanation; correct explanations start `Correct.` and distractors start `Incorrect for this question.`.
- Overall explanation cites `PCEP-30-02 exam syllabus (OpenEDG Python Institute)` and the block reference URL.
- No stem or explanation may contain `case study`, console-click recipes (`click `, `navigate to`), or out-of-scope PCAP constructs (`pip install `, `class __init__`, `metaclass`).
- Stems are unique across all 360 items and pass a 0.72 content-word Jaccard near-duplicate gate.

## Regenerating

```bash
cd course/PCEP-30-02/04-resources
python3 build.py                                      # writes the six CSVs, review copies, set READMEs, manifest
python3 make_sample.py                                # rebuilds the 12-item mixed sample
python3 validate.py --report validation-report.json   # rewrites the validation report
python3 -m unittest test_course
python3 package.py
```
