# AI-500: Designing and Implementing Multi-Agent AI Solutions

**6 sets × 100 questions = 600 questions**, prepared as an independent Udemy practice-test package.

## Download and import

Download **[AI-500-Udemy-6x100.zip](AI-500-Udemy-6x100.zip)** and extract it. Upload each CSV separately into its corresponding practice test; do not upload the ZIP as a question file.

| Test | Udemy CSV | Offline questions and answer explanations |
|---|---|---|
| 1 | [Set 1 CSV](03-practice-sets/set-1/practice-set-1.csv) | [Set 1 review](03-practice-sets/set-1/practice-set-1.md) |
| 2 | [Set 2 CSV](03-practice-sets/set-2/practice-set-2.csv) | [Set 2 review](03-practice-sets/set-2/practice-set-2.md) |
| 3 | [Set 3 CSV](03-practice-sets/set-3/practice-set-3.csv) | [Set 3 review](03-practice-sets/set-3/practice-set-3.md) |
| 4 | [Set 4 CSV](03-practice-sets/set-4/practice-set-4.csv) | [Set 4 review](03-practice-sets/set-4/practice-set-4.md) |
| 5 | [Set 5 CSV](03-practice-sets/set-5/practice-set-5.csv) | [Set 5 review](03-practice-sets/set-5/practice-set-5.md) |
| 6 | [Set 6 CSV](03-practice-sets/set-6/practice-set-6.csv) | [Set 6 review](03-practice-sets/set-6/practice-set-6.md) |

## Course setup material

- [Landing page](01-landing-page/landing-page.md): matches the existing course template with six copy/paste metadata fields, welcome and congratulations messages, set overview, domain table, study schedule, pre-study, and FAQs.
- [Curriculum and study strategy](02-curriculum/curriculum-outline.md).
- [Instructor publication checklist](04-resources/publication-checklist.md).
- [CSV specification](04-resources/csv-format-spec.md).
- [Sources and coverage](04-resources/sources-and-coverage.md).
- [Automated validation report](04-resources/validation-report.json).

## Counts and formats

Each set contains **90 single-answer questions with four options** and **10 select-two questions with five options**. Every option has feedback; each question has an overall rationale and a Microsoft Learn study-guide task reference plus a related official learning-path link.

| Official domain | Official range | Per set | Across six sets |
|---|---:|---:|---:|
| Architect multi-agent solutions | 15–20% | 18 | 108 |
| Develop multi-agent solutions in Azure | 30–35% | 33 | 198 |
| Evaluate, optimize, and monitor multi-agent solutions | 20–25% | 24 | 144 |
| Secure, govern, and deploy multi-agent solutions | 20–25% | 25 | 150 |
| **Total** | | **100** | **600** |

Order and options are deterministically shuffled. Single-answer correct positions are balanced at 23/23/22/22. Markdown review copies place the full question section before the answer key.

## Scope and limitations

The official title is **AI-500: Designing and Implementing Multi-Agent AI Solutions**, associated with **Microsoft Certified: Multi-Agent AI Solutions Expert**. The study guide describes an expert-level audience with Python, Azure, and production agent experience. These questions are not an introductory AI course or a substitute for practical work.

The delivered files contain 600 normalized-distinct question texts. Core objective families recur with different scenarios, and options and explanations intentionally repeat. Eighteen set-specific code/pseudocode and calculation cases add implementation depth. **This does not mean 600 unrelated concepts or six independent psychometric exam forms.** See the coverage map for scope and limitations.

Suggested settings: **180 minutes** and an **80% practice target**. These are custom learning settings, not official exam timing, scaled-score equivalents, or a passing guarantee. The package uses single-answer and multiple-select formats, not every possible Microsoft exam interaction.

No Udemy upload, publication, or account-level import test has been performed. Review technical accuracy and current documentation and compare the files with the latest template from your instructor account before publication. The automated validator checks structure and source consistency, not independent factual correctness or teaching quality.

## Rebuild and verify

Python **3.10+**; standard library only. Run from the repository root:

```bash
python course/AI-500/04-resources/build.py
python course/AI-500/04-resources/validate.py --report course/AI-500/04-resources/validation-report.json
python -m unittest discover -s course/AI-500/04-resources -p 'test_*.py' -v
python course/AI-500/04-resources/package.py
```

Edit `04-resources/bank.py` and regenerate rather than editing shuffled answer keys manually. The answer manifest maps displayed options to authored concepts. Packaging rejects stale review copies or answer manifests and invalid CSVs.

Original educational content, not actual or recalled exam questions. Not affiliated with or endorsed by Microsoft or Udemy. Product names and certification marks belong to their respective owners. Existing course packages remain unchanged.
