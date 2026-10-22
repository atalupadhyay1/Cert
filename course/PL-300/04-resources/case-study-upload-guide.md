# Loading case-study questions into Udemy

Udemy has **no case-study question type**. Its practice-test builder offers **Multiple choice**, **Multiple selection**, and **Fill in the blanks**, and bulk upload accepts only `multiple-choice`, `multi-select`, and `fill-in-the-blank` in the `Question Type` column. A case study therefore has to be loaded as *ordinary questions plus the scenario text*, in one of the three routes below.

Each exam in this course has **4 case studies × 3 questions = 12 case items** out of 100.

---

## Route A — Scenario as a lecture resource, then short-stem CSV (recommended)

This is the route the package is designed around: it keeps the questions readable and gives the learner the scenario before they start, which is how a real case study behaves.

1. **Create the practice test.** Curriculum → add item → **Practice Test**. Name it after the exam (for example "Mock Exam 1 — full length"), and set the question count you plan to expose (100).
2. **Create a lecture immediately before it.** Title it "Case study briefs — read before the questions", and mark it as a non-video lecture or attach the brief as a resource. Paste in the four scenarios for that exam from `04-resources/case-studies.md` (or upload that file as a PDF resource).
3. **Upload the questions.** Inside the practice test, choose **Bulk upload** → download Udemy's current CSV template → confirm your file uses the same 17 columns and the same header spelling → **Upload CSV file** → select `03-practice-sets/set-N/practice-set-N.csv` from this package.
4. **Check the import preview.** Every row should show 4 options (5 for multi-select) and one or more ticked correct answers. A rejected file almost always has a changed header, a renamed `Question Type` value, or an unescaped quote.
5. **Verify the three case blocks.** Open each case-study question in the preview and confirm it reads as a follow-on to the brief, that the answer key matches the study copy, and that the explanation fields arrived intact.
6. **Publish.** Publish the practice test and the lecture together, so a learner never meets a case question without the scenario.

**Why the short stems.** The CSV stems restate the constraint the item tests ("…without creating a second definition of net sales") but do not repeat the whole scenario. That keeps each item short in the player and avoids showing the same paragraph three times in a row.

---

## Route B — Scenario embedded in every stem, one file, nothing else to attach

Use this when the platform (or a learner) may shuffle questions, so each item must stand alone.

1. Build the variant: `python build.py --embed-case` from `04-resources/`. It writes `03-practice-sets/set-N/case-embedded-set-N.csv`.
2. Validate it first: `python course/check_csv_upload.py course/PL-300/03-practice-sets/set-1/case-embedded-set-1.csv`. It reports `OK` only when the file matches the importer's expectations.
3. Bulk-upload it exactly as in Route A, steps 3–6.
4. Expect longer stems: case items run **552–683 characters** (PL-300) and **597–743** (AB-731). Udemy accepts them, but the question box wraps to several lines and on a phone the scenario fills most of the screen before the options appear.

Do **not** upload both files into the same practice test. They contain the same 100 items and the same answer keys, so the learner would see each question twice.

---

## Route C — Type the questions by hand (only when you need images or tables)

1. In the practice test, click **+** → choose **Multiple choice** or **Multiple selection**.
2. Paste the scenario first, then the question on a new line, then the options.
3. Tick the correct answer(s) — up to 6 options are supported, which matches this package.
4. Paste the per-option explanation into the explanation field for each option, and the overall rationale into the overall explanation box.
5. Repeat for the three items of the case, keeping the scenario wording identical in all three.

Use this only when a case study needs a table or image that a CSV cell cannot carry. It is slow, and any later edit has to be made twice.

---

## Platform and format notes

| Item | Value |
|---|---|
| Question types accepted by bulk upload | `multiple-choice`, `multi-select`, `fill-in-the-blank` |
| Options per question | up to 6 |
| Questions per practice test | up to 250 — each 100-item exam fits with room to spare |
| Case studies per exam here | 4, each with 3 scored questions |
| Bulk upload for ordinary quizzes | not available; CSV import works only for practice tests |
| Per-option explanation | one field per option; this package fills all of them |
| Domain field | free text; keep it, because Udemy's report breaks results down by domain |
| Line endings and encoding | UTF-8 with BOM, LF — do not open and re-save the CSV in Excel |

---

## Pre-flight checklist before any upload

- [ ] `python build.py` run after the last edit, so the CSV and the study copy agree.
- [ ] `python validate.py --report validation-report.json` reports 6 sets / 600 questions.
- [ ] `python course/check_csv_upload.py --all` reports every file ready.
- [ ] Header row untouched: 17 columns, exact spelling and order.
- [ ] `Question Type` contains only `multiple-choice` or `multi-select`.
- [ ] Every multi-select stem says "Select two" and its key lists two indices.
- [ ] The four case scenarios for that exam are available to the learner — brief lecture, resource, or embedded stems.
- [ ] Import preview spot-checked on at least three multi-select items and one whole case block.
- [ ] No claim of Udemy preview, endorsement, or publication until it has actually happened.
