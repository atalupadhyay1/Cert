# PL-500 Sample Upload (`case-study-sample.csv`)

This folder provides a **12-question dry-run sample CSV** (`case-study-sample.csv`) extracted from the four 3-question RPA Developer case studies in **Practice Exam 1**:

1. **MeridianFirst Retail Bank** (`IBM 3270` mainframe terminal emulation, Azure Key Vault rotating `Credentials`, and Dataverse `Work Queues`)
2. **Crestline Mortgage Servicing** (`Document Automation Toolkit`, dynamic Web UI selectors, and `Invoke web service` with `Encode request body = Off`)
3. **HarborTrust Custody Ops** (`Run JavaScript function on web page`, PAD `Sensitive` variables, and Custom Connector C# `ScriptBase`)
4. **SummitVault ATM Logistics** (`Hosted Machine Groups`, Desktop Flow `PowerShell` DLP blocks, and Run Queue `High` priority + `Move to top`)

## How to Use in Udemy

1. Create a draft Practice Test in Udemy Instructor Dashboard.
2. Use **Bulk Question Upload** and select `05-sample-upload/case-study-sample.csv`.
3. Preview how self-contained `[Scenario: ...]` briefs render inline inside each `Question` prompt (`<= 629` chars, well within Udemy's `1,000`-character cell comfort zone) even when Udemy randomizes question order.
4. Once verified, replace or create the six production exams using `03-practice-sets/set-{1..6}/case-embedded-set-{1..6}.csv`.
