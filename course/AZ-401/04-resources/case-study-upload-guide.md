# Case Study Upload Guide (`AZ-401`)

Microsoft role-based Expert exams include multi-question enterprise case studies (`24` original 3-question Agentic DevOps scenarios across Sets 1–6 = `72` case items). Because Udemy's practice-test player randomizes question order by default and lacks split-screen tabbed case exhibits, every mock exam in `03-practice-sets/set-{1..6}/` ships in **two validated CSV variants**:

## Option A (Recommended): Upload `case-embedded-set-{1..6}.csv`

- **How it works:** Each of the 12 case-study items per set embeds the full concise scenario brief (`~330–420` chars) directly inside its `Question` cell before the specific question (`max 652` chars — well inside Udemy's limits).
- **Why choose it:** Learners can take randomized/shuffled timed exams on desktop or mobile and **never** encounter an orphaned `Case study — AegisClear Payments:` stem without its architectural context.

## Option B: Upload `practice-set-{1..6}.csv` + Instructor Description Briefs

- **How it works:** Case stems stay compact (`Case study — AegisClear Payments: Settlement engineers merge...`), and you paste the 4 scenario briefs from `04-resources/case-studies.md` into the Practice Test's introductory description field.
- **When to choose it:** Only if you disable question randomization or use the human-readable `practice-set-{1..6}.md` study guides sequentially.

## 5-Minute Smoke Test Before Uploading All 600 Items

Before importing all 6 full sets, create a draft test in Udemy and upload `05-sample-upload/case-study-sample.csv` (`12` self-contained case rows from Exam 1) to preview Markdown backticks, `→` arrows, and `multi-select` rendering in Udemy Student Preview.
