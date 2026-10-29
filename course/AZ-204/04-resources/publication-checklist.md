# Instructor Publication Checklist (`AZ-204`)

Use this pre-flight checklist when publishing **AZ-204 Azure Developer: 6 Full-Length Practice Exams (600 Q)** on Udemy:

- [x] **1. Landing Page Metadata (`01-landing-page/landing-page.md`):**
  - Copy Title, Subtitle, Description, 10 short Learning Objectives, Prerequisites, and Target Audience.
  - Keep the **July 31, 2026 AZ-204 retirement / Exam AI-200 transition notice** visible in the description so learners have full transparency before enrolling.
  - Pass `python3 course/check_landing_page_fields.py AZ-204`.
- [x] **2. Smoke-Test CSV Import (`05-sample-upload/case-study-sample.csv`):**
  - Create Practice Test 1 as a draft and upload `05-sample-upload/case-study-sample.csv` (12 embedded case rows) first to verify clean rendering of backticks, `→` arrows, and case briefs.
- [x] **3. Upload Six Full-Length Practice Tests (`03-practice-sets/set-{1..6}/`):**
  - Upload `case-embedded-set-{1..6}.csv` (recommended when question randomization is enabled) **or** `practice-set-{1..6}.csv` (with `04-resources/case-studies.md` pasted into the test description).
  - Configure **100 minutes** per test (matching Microsoft's published 100-minute exam duration) and a **75%–80%** study mastery bar (noting in instructions that Microsoft's `700 / 1000` scaled score is not a raw percentage).
- [x] **4. Automated Verification Gates:**
  - `validate.py --report 04-resources/validation-report.json` -> `passed: true`, `0` errors, `0` unused terms, max Jaccard `<= 0.72`.
  - `unittest discover -s course/AZ-204/04-resources -p 'test_*.py'` -> all tests green.
  - `check_csv_upload.py` -> `13/13` AZ-204 CSVs ready to upload.
