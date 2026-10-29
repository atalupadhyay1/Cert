# Package Build & Validation Summary (`AZ-204`)

## Deliverable Snapshot
- **Course:** Microsoft Exam AZ-204: Developing Solutions for Microsoft Azure (`course/AZ-204/`)
- **Credential Status Disclosed:** Exam AZ-204 (`Microsoft Certified: Azure Developer Associate`) retired **July 31, 2026** and was succeeded by **Exam AI-200 (`Azure AI Cloud Developer Associate`)**; aligned to the final **January 14, 2026** study-guide baseline (`700 / 1000` scaled passing score, 100-minute exam duration).
- **Volume:** **6 Practice Sets × 100 Questions = 600 Original Questions** (`AZ-204-6x100.zip`).
- **Blueprint Allocation per Set:** `28 / 18 / 19 / 10 / 25 = 100` across the 5 official functional groups and all **37 local study-map skills**.
- **Item-Type & Pattern Mix per Set:**
  - `84` exported `multiple-choice` (`76` single-choice + `8` four-step `→` sequence items), exact **`21 / 21 / 21 / 21`** `A/B/C/D` answer-slot balance.
  - `16` exported `multi-select` (`13` five-option `Select two.` + `3` six-option `Select three.`), distributed `4 / 3 / 3 / 2 / 4` across Domains 1–5.
  - `28–33` `____` SDK/CLI/APIM-XML/JSON/KQL completion items per set (`189` across all 6 sets).
  - `6–9` `Proposed solution:` architecture/code evaluations per set (`41` across all 6 sets).
  - `4` original 3-question developer case studies per set (`24` unique case scenarios total; zero Microsoft named scenarios).
- **Quality Metrics (`validation-report.json`):**
  - `167` cataloged technical options & sequences (`0` unused keys, `0` duplicate case-insensitive labels).
  - Max pairwise stem Jaccard similarity across all 600 items: **`0.6429`** (ceiling `<= 0.72`).
  - Longest embedded case-study stem: **`751` characters** (ceiling `<= 1,000`).
  - `13 / 13` CSV files pass UTF-8 BOM, LF line endings, 16-column Udemy header, contiguous options, and banned-phrase checks.
