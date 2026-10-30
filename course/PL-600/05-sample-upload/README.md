# Sample Upload Smoke Test — Exam PL-600 (`case-study-sample.csv`)

`case-study-sample.csv` contains **12 self-contained case-study questions** (`1` header row + `12` data rows) extracted directly from **Practice Exam 1** (`case-embedded-set-1.csv`):

1. **SovereignCrest Private Bank** (`3` questions — Swiss/EU Multi-Geo residency, Well-Architected `Security`, Modernized Business Units & Access Team Templates)
2. **Alderbrook Commercial Leasing** (`3` questions — `Alternate Keys` + `CMT`, manual `N:N` guarantor intersect modeling, and 5-minute `6,000` req / `20m` Service Protection S2S pooling)
3. **Vespera Wealth Portal** (`3` questions — SharePoint Document Management ACL gap remediation via `File` columns, `POA` sharing hygiene, and `Power Pages` `Entra External ID` + `Table Permissions` for 180,000 retail investors)
4. **Monarch Clearing Services** (`3` questions — refactoring 45s synchronous HTTP plug-ins to async Azure Service Bus, Power Platform `VNet` subnet delegation for private endpoints, and Quick Find / Canvas `N+1` tuning)

## 2-Minute Udemy Import Verification

1. Create a draft Practice Test in Udemy Instructor Studio.
2. Choose **Bulk Question Upload (CSV)** and select `05-sample-upload/case-study-sample.csv`.
3. Confirm all **12 questions** import with zero errors, inline `[Case Study — <Name>]` briefs render cleanly above each stem, per-option explanations appear under every choice, and the `Domain` badge populates properly.
4. Once verified, delete the draft test or replace its contents with the full 100-question `03-practice-sets/set-{1..6}/case-embedded-set-{1..6}.csv` files.
