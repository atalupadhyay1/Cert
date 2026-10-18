# Set 6 — SAA-C03 Full Exam Practice Simulation

200 original practice questions in Udemy v2 bulk-upload format. The domain weights match SAA-C03; the question count is expanded for practice, not a reproduction of the 65-question exam. These are independent study materials, not actual exam questions.

## Distribution

| Domain | Questions | Weight |
|---|---:|---:|
| Design Secure Architectures | 60 | 30% |
| Design Resilient Architectures | 52 | 26% |
| Design High-Performing Architectures | 48 | 24% |
| Design Cost-Optimized Architectures | 40 | 20% |
| **Total** | **200** | **100%** |

- **160 multiple-choice**, **40 multi-select (20%)**.
- **20 GameDay case-study questions are included in the 200**, and count toward their respective domains.
- Topics and answer positions are deterministically mixed; multi-select prompts state how many answers to choose.
- Every option has an explanation, with an overall explanation and AWS reference for each question.

## How to use

Read `case-study.md` before attempting questions beginning **“In the GameDay scenario”**. Complete the set without viewing answer explanations, then review missed questions by domain. For proportional pacing, allow approximately 400 minutes for all 200 questions, or split into shorter sessions. This suggested practice time is not an official exam duration. The real exam allows 130 minutes for 65 questions; its scaled passing score cannot be inferred from a raw percentage on this bank.

Coverage includes IAM and cross-account access, encryption, network controls, security monitoring, Multi-AZ and multi-Region recovery, queues and event-driven design, compute and container selection, storage performance, caching, analytics, pricing commitments, lifecycle management, and cost governance.

## Files

- `practice-set-6.csv` — 200 questions, exact 17-column Udemy v2 header, all fields quoted.
- `set6_builder.py` — self-contained question bank and reproducible builder. Retain it for maintenance.
- `case-study.md` — GameDay background, requirements, and scoped extensions used in questions.

## Rebuild and validate

```bash
cd course/AWS-SAA-C03-03-practice-sets/set-6
python set6_builder.py
python ../../AWS-SAA-C03-04-resources/validate_csv.py practice-set-6.csv
```

The builder asserts total, domain distribution, multi-select count, case-study count, unique prompts, and answer-index consistency. CSV output uses UTF-8, `csv.QUOTE_ALL`, and LF line endings. Correct answers use comma-separated, 1-based indices.
