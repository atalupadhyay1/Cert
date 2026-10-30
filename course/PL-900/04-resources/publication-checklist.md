# Publication Checklist — Microsoft Exam PL-900 (Udemy Practice-Test Course)

## 1. Pre-Upload Verification Gates

- [x] `python3 course/PL-900/04-resources/build.py` — regenerates all 6 CSVs, review Markdown files, set READMEs, `answer-manifest.json`, and `SUMMARY.md`.
- [x] `python3 course/PL-900/04-resources/make_sample.py` — regenerates `05-sample-upload/sample-upload.csv` (`10` standalone questions across all `5` domains).
- [x] `python3 course/PL-900/04-resources/validate.py --report` — confirms `PASS`, `600` unique questions, `0` case studies, `106/106` terms exercised, max Jaccard `<= 0.72`, and zero overlap with sibling Microsoft courses (`PL-400`, `AZ-204`, `AZ-400`, `AZ-401`, `DP-600`).
- [x] `python3 course/PL-900/04-resources/package.py` — builds reproducible `PL-900-6x100.zip` and verifies no stale companion files or forbidden case-study artifacts exist.
- [x] `python3 course/PL-900/04-resources/test_course.py` — passes all automated `unittest` checks.
- [x] `python3 course/check_csv_upload.py --all` — passes repo-wide Udemy CSV importer simulation.
- [x] `python3 course/check_landing_page_fields.py PL-900` — passes mandatory Udemy landing-page field checks.

## 2. Udemy Publishing Form Steps

1. **Create Practice-Test-Only Course** -> Category: *IT & Software -> IT Certifications -> Microsoft Power Platform*.
2. **Course Landing Page** (`01-landing-page/landing-page.md`):
   - Paste **Course Title** (`59` chars), **Course Subtitle** (`103` chars), and **Course Description**.
   - Paste the 12 concise bullets in **What will students learn in your course?**, **Requirements**, and **Who is this course for?**.
3. **Course Messages**:
   - Paste **Welcome Message** and **Congratulations Message** from `01-landing-page/landing-page.md`.
4. **Optional Smoke Test**:
   - Upload `05-sample-upload/sample-upload.csv` (`10` items) into a draft practice test to preview `→` sequences, `____` completions, and `multi-select` rendering; delete the draft test once verified.
5. **Upload the Six Full-Length Mock Exams**:
   - Create Practice Tests 1 through 6 using the **Name** and **Full** (or **Trimmed**) descriptions in `01-landing-page/landing-page.md`.
   - Bulk-upload `03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`.
   - Set **Time Limit** = `75` minutes, **Minimum Score to Pass** = `75%`, and **Randomize Question and Answer Order** = **On**.
