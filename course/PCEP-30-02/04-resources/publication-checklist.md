# Publication checklist — PCEP-30-02

## Sources and version currency

- [ ] Re-open `https://pythoninstitute.org/pcep` and `https://pythoninstitute.org/pcep-exam-syllabus` before publishing. Check whether **PCEP-30-03** (scheduled for October 31, 2026) has launched and whether PCEP-30-02 retirement dates or block weights have changed.
- [ ] Confirm the published PCEP-30-02 parameters: 30 questions, 40 minutes (+5 min NDA/tutorial), 18 / 29 / 25 / 28 percent weights, cumulative 70% passing score, pricing from $69, five languages, no prerequisites, and 5-year validity.
- [ ] Confirm the listing discloses that 60 items in 80 minutes is an **expanded 2× bank** matching the live ~80-second-per-item pace rather than the live 30-item count.
- [ ] Confirm the listing states 70% as a **cumulative average across all blocks**, never as a separate pass mark on every block.
- [ ] Confirm interactive drag-and-drop, sort, and multi-slot code-insertion widgets are disclosed as excluded, while single-blank `____` code-fill items are described accurately as multiple-choice approximations.

## Structure and CPython verification

- [ ] Confirm six CSVs each have 60 rows allocated 11 / 17 / 15 / 17 across Blocks 1–4.
- [ ] Confirm each CSV has 45 `multiple-choice` (with at least 15 containing `____`) and 15 `multi-select` rows (spread 3 / 4 / 4 / 4).
- [ ] Confirm every code-trace output and exception type has been verified on Python 3 (`CPython 3.11+`).
- [ ] Confirm `python3 validate.py --report validation-report.json` reports `PASS: 6 sets / 360 questions`.
- [ ] Confirm `python3 -m unittest test_course` passes all 39 tests.
- [ ] Confirm `python3 course/check_csv_upload.py --all` and `python3 course/check_landing_page_fields.py` pass across the repository.

## Import and packaging

- [ ] Upload `05-sample-upload/sample-upload.csv` (12 items: 4 code-trace MC, 4 `____` gap-fill MC, 4 `multi-select`) to verify backtick code formatting and 5-option rendering in Udemy's player.
- [ ] Set each practice test timer in Udemy to **80 minutes** and passing percentage to **70%**.
- [ ] Run `python3 package.py` last to produce `PCEP-30-02-6x60.zip` with clean companions and deterministic timestamps.
