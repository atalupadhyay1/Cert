# Instructor Publication & Maintenance Checklist — CCAR-P

- [x] `python3 04-resources/build.py` regenerates all 6 CSVs, 6 Markdown review copies, 6 set READMEs, and `04-resources/answer-manifest.json` cleanly.
- [x] `python3 04-resources/make_sample.py` regenerates `05-sample-upload/sample-upload.csv` (14 rows: 1 MC + 1 multi-select per official domain across all 7 domains).
- [x] `python3 04-resources/validate.py --report 04-resources/validation-report.json` reports `PASS: 6 sets / 378 questions` with zero errors.
- [x] `python3 04-resources/package.py` writes reproducible `CCAR-P-6x63.zip` (43 internal files, fixed 1980-01-01 timestamps).
- [x] `python3 -m unittest discover -s 04-resources -p 'test_*.py' -v` passes all unit, source, pattern, and artifact assertions.
- [x] Repo-wide `python3 course/check_csv_upload.py --all` and `python3 course/check_landing_page_fields.py CCAR-P` pass with exit code 0.
- [ ] **Account-level Udemy preview:** Import `05-sample-upload/sample-upload.csv` into a draft Udemy Practice Test first, verify formatting of backticked identifiers (`defer_loading: true`, `cache_control`, `CLAUDE.md`) and 5-/6-option `multi-select` rendering, then upload `practice-set-1.csv` through `practice-set-6.csv` with time limit **120 minutes** per test.
- [ ] **Scheduled blueprint refresh (November 17 / December 7, 2026):** Compare the revised Anthropic `CCAR-P` Exam Guide releasing November 17, 2026 against `bank.py` (`DOMAINS`, `OFFICIAL_WEIGHTS`, `SKILLS`) and update any changed domain weights or newly added platform primitives before marketing coverage of the post-December 7, 2026 exam form.
