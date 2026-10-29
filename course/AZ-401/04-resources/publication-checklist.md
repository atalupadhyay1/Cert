# Udemy Instructor Publication Checklist (`AZ-401`)

Follow these steps to publish **AZ-401 Agentic DevOps: 6 Full-Length Practice Exams (600 Q)** cleanly on Udemy:

- [ ] **1. Create Practice-Test-Only Course:** Select **Practice Test** course type in Udemy Instructor Dashboard and paste Title, Subtitle, Description, Learning Objectives (`10` concise ~60–65 char bullets), Prerequisites (`GH-300` or `AZ-104` disclosed), and Target Audience from `01-landing-page/landing-page.md`.
- [ ] **2. Run 5-Minute Sample Import First:** Create a draft practice test, upload `05-sample-upload/case-study-sample.csv` (`12` rows), and verify `→` arrows, backticks, and `multi-select` checkboxes in Student Preview (`delete draft section afterward`).
- [ ] **3. Upload All 6 Full-Length Mock Exams (`6 × 100 = 600` Qs):**
  - Practice Test 1 -> `03-practice-sets/set-1/case-embedded-set-1.csv` (`100` Qs, `100` min timer)
  - Practice Test 2 -> `03-practice-sets/set-2/case-embedded-set-2.csv` (`100` Qs, `100` min timer)
  - Practice Test 3 -> `03-practice-sets/set-3/case-embedded-set-3.csv` (`100` Qs, `100` min timer)
  - Practice Test 4 -> `03-practice-sets/set-4/case-embedded-set-4.csv` (`100` Qs, `100` min timer)
  - Practice Test 5 -> `03-practice-sets/set-5/case-embedded-set-5.csv` (`100` Qs, `100` min timer)
  - Practice Test 6 -> `03-practice-sets/set-6/case-embedded-set-6.csv` (`100` Qs, `100` min timer)
- [ ] **4. Configure Timing & Passing Guidance:** Set `100 minutes` per test and e.g. `80%` Udemy completion bar while noting in test descriptions that Microsoft scores AZ-401 on a `100–1000` scaled score (`700` to pass, not `70%`).
- [ ] **5. Keep Question Randomization Enabled:** Because `case-embedded-set-{1..6}.csv` embeds full case context inside each of the 72 case questions, question and answer shuffling work safely.
- [ ] **6. Re-Verify Automated Gates Anytime After Edits:**
  ```bash
  python3 course/AZ-401/04-resources/build.py && python3 course/AZ-401/04-resources/validate.py
  python3 -m unittest discover -s course/AZ-401/04-resources -p "test_*.py" -v
  ```
