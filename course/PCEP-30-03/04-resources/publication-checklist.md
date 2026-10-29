# Udemy publication checklist — PCEP-30-03

1. **Smoke-test the importer first:** Create a draft Practice Test course on Udemy and bulk-upload `05-sample-upload/sample-upload.csv` (12 questions: 3 per block covering plain `multiple-choice`, `____` gap-fill `multiple-choice`, and 5-option `multi-select`). Confirm code backticks, `____` blanks, and explanations render cleanly, then delete the sample practice test before uploading the six full exams.
2. **Create six Practice Tests:** Add six practice-test sections using the titles and full/trimmed descriptions in `01-landing-page/landing-page.md`:
   - Practice Test 1: `03-practice-sets/set-1/practice-set-1.csv` — *Full-Length Mock Exam 1: Budget Trackers and Currency Calculators*
   - Practice Test 2: `03-practice-sets/set-2/practice-set-2.csv` — *Full-Length Mock Exam 2: URL Builders and Input Validators*
   - Practice Test 3: `03-practice-sets/set-3/practice-set-3.csv` — *Full-Length Mock Exam 3: Ticket Queues and Seat Booking*
   - Practice Test 4: `03-practice-sets/set-4/practice-set-4.csv` — *Full-Length Mock Exam 4: Weather Stations and Unit Converters*
   - Practice Test 5: `03-practice-sets/set-5/practice-set-5.csv` — *Full-Length Mock Exam 5: Workout Timers and Pace Trackers*
   - Practice Test 6: `03-practice-sets/set-6/practice-set-6.csv` — *Full-Length Mock Exam 6: Recipe Scalers and Pantry Audits*
3. **Configure each practice-test timer and pass mark:**
   - Question count: **60**
   - Time limit: **80 minutes** (matches the published `PCEP-30-0x` pace of ~80 seconds per item across 30 live items in 40 minutes)
   - Minimum score to pass: **70%** (matches the published cumulative 70% passing threshold)
   - Randomize question and answer order: **Enabled** (or keep block order for study mode)
4. **Paste landing-page metadata:** Copy Course Title, Course Subtitle, Course Description, What Students Will Learn, Requirements, Target Audience, Welcome Message, and Congratulations Message from `01-landing-page/landing-page.md`.
5. **Post-October 31, 2026 release verification:** Re-check `https://pythoninstitute.org/pcep` once OpenEDG transitions `PCEP-30-03` from Pending Release to Active; if OpenEDG publishes a dedicated `PCEP-30-03` syllabus URL or updates any block percentage, update `04-resources/sources.py`, `bank.py`, and the version notice in `landing-page.md` and `README.md`, then re-run `build.py`, `validate.py`, and `package.py`.
