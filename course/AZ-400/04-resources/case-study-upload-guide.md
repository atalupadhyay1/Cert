# Case-Study Upload Guide for Udemy Practice Tests (Exam AZ-400)

Microsoft Exam AZ-400 includes multi-question enterprise DevOps case studies alongside standalone YAML, CLI, and architecture items. Because Udemy's Practice Test engine randomizes question order across the entire test and does not offer a locked split-screen tabbed exhibit pane, `course/AZ-400/` ships **two synchronized CSV variants** for every set (`1..6`).

---

## Option A (Recommended): Upload `case-embedded-set-N.csv`

- **Path:** `03-practice-sets/set-{1..6}/case-embedded-set-{1..6}.csv`
- **How it works:** Each of the 12 case-study items per exam (`4` original cases × `3` questions) embeds the full ~380-character scenario brief directly inside the `Question` column (`Case study — <Name>: <Scenario Brief> <Question Stem>`).
- **Longest embedded stem:** `709` characters (well inside Udemy's `1,000`-character stem ceiling).
- **Why recommended:** Learners can enable **Randomize question order** in Udemy without ever encountering an orphaned case question whose scenario appeared 50 items away.

---

## Option B: Upload `practice-set-N.csv` + Paste Briefs from `case-studies.md`

- **Path:** `03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`
- **How it works:** Uses compact prefixes (`Case study — KestrelPay: ...`) while `04-resources/case-studies.md` provides all 24 scenario briefs in clean copy/paste Markdown.
- **When to use:** Only if question randomization is turned **OFF** and the 4 scenario briefs for that exam are pasted into the Udemy Practice Test's introductory description field.

---

## Smoke-Testing Before Full Import

Import `05-sample-upload/case-study-sample.csv` (`12` self-contained case items from Exam 1: `KestrelPay`, `MintLedger`, `VaultWire`, and `SilverCrest Treasury`) into a draft Udemy test first to preview rendering across desktop and mobile before importing all six 100-question sets.
