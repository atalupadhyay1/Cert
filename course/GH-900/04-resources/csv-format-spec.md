# Udemy 17-Column Bulk Question Upload CSV Specification (`GH-900`)

All generated CSV files in `course/GH-900/` (`03-practice-sets/set-{1..6}/practice-set-{1..6}.csv` and `05-sample-upload/sample-upload.csv`) conform strictly to Udemy's 17-column practice-test import template (`UTF-8` with BOM, Unix `LF` line endings, RFC 4180 minimal quoting).

## Exact Header Row

```csv
Question,Question Type,Answer Option 1,Explanation 1,Answer Option 2,Explanation 2,Answer Option 3,Explanation 3,Answer Option 4,Explanation 4,Answer Option 5,Explanation 5,Answer Option 6,Explanation 6,Correct Answers,Overall Explanation,Domain
```

## Column-by-Column Contract & Validated Bounds (`GH-900`)

| Col # | Column Header | Contract & `GH-900` Validation Rule |
| :---: | :--- | :--- |
| `1` | `Question` | Non-empty standalone prompt (`<= 444` chars across all 600 items; zero artificial case studies). |
| `2` | `Question Type` | Exactly `multiple-choice` (`84` rows/set) or `multi-select` (`16` rows/set). |
| `3–10` | `Answer Option 1..4` & `Explanation 1..4` | Always populated (`<= 245` chars per option label; `<= 550` chars per explanation starting with `Correct.` or `Incorrect.`). |
| `11–12` | `Answer Option 5` & `Explanation 5` | Populated for all `16` `multi-select` (`M2` and `M3`) rows; empty `""` for `multiple-choice` rows. |
| `13–14` | `Answer Option 6` & `Explanation 6` | Populated for all `3` six-option `Select three.` (`M3`) rows; empty `""` for `multiple-choice` and 5-option `M2` rows. |
| `15` | `Correct Answers` | 1-based ascending comma-separated indices (`"2"` for MC balanced `21/21/21/21`; `"1,4"` for `M2`; `"2,3,6"` for `M3`). |
| `16` | `Overall Explanation` | Synthesizes why the keyed option(s) win, cites the official skill ID (`1.1`–`7.6`), and links to `https://docs.github.com/...` or `https://learn.microsoft.com/...`. |
| `17` | `Domain` | Exact official functional group name: `Understand Git and GitHub basics`, `Work with GitHub repositories`, `Collaborate using GitHub`, `Apply modern development practices`, `Manage projects with GitHub`, `Understand privacy, security, and administration`, or `Explore the GitHub community`. |
