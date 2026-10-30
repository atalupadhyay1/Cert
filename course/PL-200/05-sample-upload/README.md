# 🧪 Sample Bulk Upload Smoke Test (`05-sample-upload`)

Before importing all six 100-question exams into Udemy, upload `case-study-sample.csv` (`12` rows) into a temporary draft practice test to verify formatting end to end in less than 60 seconds.

## What `case-study-sample.csv` Contains

- **Rows:** `12` questions (`UTF-8 BOM`, `LF`, 17 Udemy columns) extracted deterministically from **Full-Length Mock Exam 1**.
- **Scenarios Covered:** All four 3-question Functional Consultant case studies from Exam 1 (*Harborstone Property Group*, *Crestview Tenant Portals*, *Vanguard Facility Maintenance*, and *Oakridge Lease Renewals*) with `[Scenario: ...]` context embedded directly inside every `Question` cell.
- **Patterns Exercised:** Single-answer scenario items, Power Fx / Table Permission `____` completion items (`Param("recordId")`, `Patch(WorkOrders, ...)`, `Access Type = Account`), option-level `Correct —` / `Incorrect —` explanations, and `Overall Explanation` Microsoft Learn citations.

## How to Run the Smoke Test

1. In Udemy Instructor Portal, create a draft **Practice Test** section and choose **Bulk Upload Questions (CSV)**.
2. Select `course/PL-200/05-sample-upload/case-study-sample.csv`.
3. Preview the imported questions in Student View to confirm clean rendering of backticks, `—` em-dashes, `[Scenario: ...]` headers, and explanations.
4. Delete the temporary draft section and upload `03-practice-sets/set-{1..6}/case-embedded-set-{1..6}.csv` into Practice Tests 1–6.
