# 📄 Udemy Practice-Test CSV Format Specification (`GH-100`)

All six full-length practice exams (`03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`) and the 15-row smoke-test sample (`05-sample-upload/sample-upload.csv`) conform strictly to Udemy's **17-column bulk practice-test CSV upload schema**.

---

## 🧱 Exact 17-Column Header Contract

```csv
Question,Question Type,Answer Option 1,Explanation 1,Answer Option 2,Explanation 2,Answer Option 3,Explanation 3,Answer Option 4,Explanation 4,Answer Option 5,Explanation 5,Answer Option 6,Explanation 6,Correct Answers,Overall Explanation,Domain
```

| Col # | Column Name | Rules Enforced in `GH-100` (`build.py` + `validate.py` + `check_csv_upload.py`) |
|---:|---|---|
| **1** | `Question` | Self-contained scenario (`<= 540` chars); ends with `Select two.` (`M2`) or `Select three.` (`M3`) on all `multi-select` items |
| **2** | `Question Type` | Exact lowercase `multiple-choice` (`84`/set: `76` `S` + `8` `O`) or `multi-select` (`16`/set: `13` `M2` + `3` `M3`) |
| **3–10** | `Answer Option 1..4` & `Explanation 1..4` | Populated on **100%** of items; options `<= 245` chars; every option has an explicit `Correct — ...` or `Incorrect — ...` rationale |
| **11–12** | `Answer Option 5` & `Explanation 5` | Populated on `M2` (5-option) and `M3` (6-option) items; empty `""` on 4-option `multiple-choice` items |
| **13–14** | `Answer Option 6` & `Explanation 6` | Populated on `M3` (6-option) items; empty `""` on 4-option and 5-option items |
| **15** | `Correct Answers` | 1-indexed comma-separated integers sorted ascending (`"1"`–`"4"` balanced `21/21/21/21` on MC; `"2,4"` or `"1,3,6"` on MS) |
| **16** | `Overall Explanation` | Concise architectural synthesis + `Official skill X.Y — ... Reference: https://...` (`<= 1,200` chars) |
| **17** | `Domain` | Exact July 2026 official GH-100 domain name (`Manage GitHub identities and access`, etc.) |

---

## 🔄 Interactive Microsoft Item Approximations

Because Udemy's CSV bulk uploader supports `multiple-choice` and `multi-select` only (and live GH-100 has **zero case studies** and **zero live labs**), Pearson VUE interactive item patterns are faithfully represented as:

- **Ordered 4-step workflows (`→`):** `8` single-select items per exam testing exact administrative execution order (`Step 1 → Step 2 → Step 3 → Step 4`).
- **CLI / API / Policy slot completions (`____`):** `21–33` items per exam (`143` total) testing exact GHES CLI utilities, YAML keys, Audit Log qualifiers, and rate limits.
- **`Proposed solution:` evaluations:** `6–8` items per exam (`42` total) mirroring Microsoft's Yes/No architectural adequacy pattern without unreviewable lock screens.
