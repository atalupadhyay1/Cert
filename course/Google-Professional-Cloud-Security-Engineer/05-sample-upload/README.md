# Sample: ten mixed questions, ready to upload

`sample-upload.csv` contains **ten questions — two from each official domain** — drawn from Mock Exam 1, five single-answer and five multi-select. It is a throwaway test file: upload it to a scratch practice test to see how the player renders the format before you load 100 questions.

Regenerate it any time with `python3 make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 10 — five `multiple-choice`, five `multi-select` |
| Domains | two items per official domain (one single-answer, one multi-select), in domain order |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |

| Question | Domain | Type | Correct Answers |
|---:|---|---|---|
| 1 | Configuring Access | multiple-choice | 3 |
| 2 | Configuring Access | multi-select | 4,5 |
| 3 | Securing communications and boundary protection | multiple-choice | 2 |
| 4 | Securing communications and boundary protection | multi-select | 1,5 |
| 5 | Ensuring Data Protection | multiple-choice | 3 |
| 6 | Ensuring Data Protection | multi-select | 3,5 |
| 7 | Managing Operations | multiple-choice | 1 |
| 8 | Managing Operations | multi-select | 1,4 |
| 9 | Supporting Compliance Requirements | multiple-choice | 1 |
| 10 | Supporting Compliance Requirements | multi-select | 1,3 |

Q2, Q4, Q6, Q8 and Q10 are the multi-select items, so one upload proves both single-answer and two-key rendering in every domain, including that the player shows five options for a multi-select item and four for a single-answer item. If a rebuild reorders an option, change the keys in this table too — the file itself is always the authority.

There is no case-study sample in this folder, because the Professional Cloud Security Engineer exam has no case-study component. A case block here would test a format the exam does not use.

## How to see it in the engine

1. Open the course in instructor view → **Curriculum** → add a **Practice Test** named "Scratch — format sample".
2. Inside the test, click **+** → **Bulk upload** → download the current template. Confirm it is still the 17-column layout; if the platform has changed the template, re-export from `build.py` rather than editing this file by hand.
3. **Upload CSV file** → choose `sample-upload.csv`.
4. Open **Preview**. Each question should render four options, or five for Q2, Q4, Q6, Q8 and Q10, with no empty sixth option.
5. Delete the scratch test once you have seen it, and keep the real 100-item uploads separate.

## What the learner sees

Below is a reconstruction of the standard practice-test layout using this file's shape — not a captured screenshot, and not a claim that an upload has already been performed.

**Screen 1 — question view (Q4)**

```text
  Question 4 of 10       Securing communications and boundary protection

  Outbound web traffic must be allowlisted by host and inspected before it
  leaves. Which two services apply? Select two.

  ☐ A. Enable layer 7 inspection on the firewall policy
  ☐ B. Filter on address and port only and allow the rest
  ☐ C. Allow all egress and rely on the application to be careful
  ☐ D. Route the egress through a NAT instance
  ☐ E. Route the egress through Secure Web Proxy
```

**Screen 2 — after answering**

```text
  ✓ Correct

  A. Correct. Layer 7 inspection reads the application protocol, so a rule can
     act on the URL or the TLS server name…
  B. Incorrect for this question. A layer 4 rule cannot see the destination
     host name inside an allowed connection…
  C. Incorrect for this question. Unrestricted egress lets a compromised
     workload reach anything the internet offers…
  D. Incorrect for this question. A NAT instance translates addresses and does
     not apply a destination allowlist…
  E. Correct. Secure Web Proxy applies an allowlist and TLS inspection to
     outbound web traffic…
```

The question text and option labels above are copied from the CSV, so the letters match `Correct Answers = 1,5`. The explanations below are abridged to their first sentence; the file holds the full text and the full rationale.

## Multi-select scoring in this file

`Correct Answers = 1,5` means options A and E are both required. There is no partial credit, and the stem states "Select two" so a learner cannot under-select by accident. If the platform rejects the comma-separated key, the course CSV is not the problem — check that the importer template has not renamed the `Correct Answers` column.

## What this file does not prove

It does not prove that the platform accepts every item in the package, that the live exam uses these questions, or that a practice test will be published. It answers one question: **does the player render four-option and five-option items, with a two-key answer, cleanly?**
