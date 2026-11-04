# Udemy Publication Checklist (`Agentic-AI`)

Follow these steps to publish **Agentic AI (NCP-AAI & MCP/A2A): 6 Practice Exams (600 Qs)** smoothly on Udemy:

- [x] **1. Smoke-Test Import First (`18` Rows):** In Udemy's curriculum builder, create a scratch practice test and upload `05-sample-upload/sample-upload.csv` (`3` items per domain: `2` `multiple-choice` + `1` `multi-select`) to verify UTF-8 BOM rendering, `→` arrows, backticks, and `Domain` pills. Delete the scratch test once verified.
- [x] **2. Create Six Practice Tests (`100` Questions Each):**
  - Upload `03-practice-sets/set-1/practice-set-1.csv` → paste **Practice test 1** title & description from `01-landing-page/landing-page.md` (`QuantaPay Autonomous Disputes`).
  - Upload `03-practice-sets/set-2/practice-set-2.csv` → paste **Practice test 2** title & description (`HelixVax Discovery Labs`).
  - Upload `03-practice-sets/set-3/practice-set-3.csv` → paste **Practice test 3** title & description (`CloudPulse Autonomous SRE`).
  - Upload `03-practice-sets/set-4/practice-set-4.csv` → paste **Practice test 4** title & description (`StrataLaw Contract Intelligence`).
  - Upload `03-practice-sets/set-5/practice-set-5.csv` → paste **Practice test 5** title & description (`VeloceCart Commerce Concierge`).
  - Upload `03-practice-sets/set-6/practice-set-6.csv` → paste **Practice test 6** title & description (`AegisCyber SOC Copilot`).
- [x] **3. Configure Exam Timer & Passing Threshold:** Set each practice test timer to **`120 minutes`** (`matching NVIDIA NCP-AAI & GitHub GH-600 duration`), set the target mastery score to **`80%`**, and **enable both Question and Answer Randomization** (`0` multi-question case-study blocks exist).
- [x] **4. Populate Course Landing Page Fields (`1`–`6`):** Copy/paste Title (`57` chars), Subtitle (`95` chars), Course Description, the 12 `What will students learn` bullets (`60–64` chars each), Prerequisites, and Target Audience from `01-landing-page/landing-page.md`.
- [x] **5. Add Automated Course Messages:** Paste the **Welcome Message** and **Congratulations Message** from `01-landing-page/landing-page.md` under *Course Messages*.
- [x] **6. Pre-Commit Reproducibility Verification:**
  ```bash
  python3 course/Agentic-AI/04-resources/build.py
  python3 course/Agentic-AI/04-resources/make_sample.py
  python3 course/Agentic-AI/04-resources/validate.py --report
  python3 course/Agentic-AI/04-resources/package.py
  python3 -m unittest course/Agentic-AI/04-resources/test_course.py -v
  python3 course/check_landing_page_fields.py Agentic-AI
  python3 course/check_csv_upload.py course/Agentic-AI
  ```
