# 5-Minute Udemy Bulk-Upload Smoke Test (`AZ-401`)

`case-study-sample.csv` contains **12 self-contained case-study questions** (`4` enterprise Agentic DevOps scenarios × `3` questions) exported directly from Mock Exam 1 (`AegisClear Payments`, `QuantLedger Cloud`, `NovaPay Treasury`, `CrestVault Risk`).

## How to Verify Before Full Import

1. Open your draft Practice Test course on Udemy -> **Curriculum** -> **+ Practice Test** -> **Upload CSV**.
2. Select `course/AZ-401/05-sample-upload/case-study-sample.csv`.
3. Confirm all `12` questions import cleanly with:
   - Inline backticks (`` `copilot-setup-steps` ``, `` `Fixes AB#4812` ``, `` `-a azcli` ``),
   - 4-step ordered `→` sequences (`seq_ado2gh_ok`, `seq_obs_agent_ok`),
   - Full embedded case briefs inside every stem so question randomization preserves context, and
   - Complete per-option and overall explanations with Microsoft Learn / GitHub Docs links.
4. Delete the smoke-test draft and upload `03-practice-sets/set-{1..6}/case-embedded-set-{1..6}.csv` (`6 × 100 = 600` questions).
