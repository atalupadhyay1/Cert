# Udemy Publication Checklist — Exam GH-300: GitHub Copilot

1. **Create Practice-Test-Only Course on Udemy:**
   - Paste **Course Title** (`48` chars), **Course Subtitle** (`102` chars), **Course Description**, **12 What You'll Learn bullets** (`65–67` chars each), **Requirements**, and **Target Audience** from `01-landing-page/landing-page.md`.
2. **Smoke-Test Bulk Upload (`Optional`):**
   - Create a draft test and upload `05-sample-upload/sample-upload.csv` (`18` questions: `2 MC + 1 MS` across all 6 domains) to verify instant CSV import.
3. **Upload All 6 Full-Length Mock Exams (`600` Questions):**
   - Create 6 practice tests using the exact **Name** and **Full/Trimmed descriptions** in `01-landing-page/landing-page.md`.
   - Upload `03-practice-sets/set-{1..6}/practice-set-{1..6}.csv` (`100` questions each).
   - Set time limit = **`100 minutes`**, randomized question order = **On**, randomized answer order = **On** (`0` multi-question case-study blocks).
4. **Configure Automated Course Messages:**
   - Copy **Welcome Message** and **Congratulations Message** from `01-landing-page/landing-page.md` into Udemy *Course Messages*.
5. **Pre-Publish Verification Gates:**
   - `python3 course/GH-300/04-resources/validate.py --report` -> `0` errors
   - `python3 -m unittest discover -s course/GH-300/04-resources -p 'test_*.py' -v` -> `6/6` tests passing
   - `python3 course/check_csv_upload.py --all` -> all CSVs passing
   - `python3 course/check_landing_page_fields.py GH-300` -> `0` errors
