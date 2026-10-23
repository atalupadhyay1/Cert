# Sample: one case study, ready to upload

`case-study-sample.csv` contains **exactly one case study** — the three questions of the Contoso Field Service block from Mock Exam 1 — with the scenario embedded in each stem. It is a throwaway test file: upload it to a scratch practice test to see how a case study actually renders in the player before you load 100 questions.

Regenerate it any time with `python make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 3 (Q1 and Q3 are `multiple-choice`, Q2 is `multi-select`) |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |
| Stem length | 780–811 characters, because the scenario is repeated in each one |
| Answer keys | Q1 = 1 (A) · Q2 = 1,3 (A and C) · Q3 = 4 (D) |
| Domains | Q1 · Plan and configure agent solutions · Q2 · Integrate and extend agents in Copilot Studio · Q3 · Test and manage agents |

The block deliberately spans all three domains, because a real AB-620 case study rarely stays inside one: the scenario forces a planning decision, an integration decision, and a lifecycle decision. Q2 is a multi-select item, so one upload proves both the radio and checkbox render paths.

## How to see it in the engine

1. Open the course in instructor view → **Curriculum** → add a **Practice Test** named "Scratch — case study sample".
2. Inside the test, click **+** → **Bulk upload** → download Udemy's current template. Confirm your file still has 17 columns and the same header spelling; if Udemy has changed the template, re-export from `build.py` rather than editing the sample by hand.
3. **Upload CSV file** → choose `case-study-sample.csv`.
4. Open **Preview**. The first screen should look like the mock-up below.
5. Delete the scratch test once you have seen it, and keep the real 100-item uploads separate.

## What the learner sees

The player has no case-study container, so the scenario has to live inside the question text. Below is a reconstruction of the standard practice-test layout with this file's real content — not a captured screenshot, and not a claim that an upload has already been performed.

**Screen 1 — question view**

```text
  Question 1 of 3                     Plan and configure agent solutions

  Case study — Contoso Field Service (1 of 3): Contoso Field Service
  built a Copilot Studio agent for 1,200 engineers who close about nine
  thousand jobs a week. The agent must read the work order from an
  on-premises scheduling system that cannot accept inbound connections,
  and it must raise the parts request through a REST service that
  already has an OpenAPI definition. Engineers sign in with Microsoft
  Entra ID, and the parts service must apply each engineer's own
  entitlement rather than a shared account. Contoso promotes every
  change through development, test, and production, and the service desk
  wants a rolling measure of whether answers are still correct. The
  scheduling system refuses all inbound connections from the cloud.
  Which integration should the plan use for it?

  ( ) A.  Mediate the on-premises call through an on-premises data gateway
  ( ) B.  Copy the records nightly into Dataverse and answer from the copy
  ( ) C.  Batch the requests and post them to the source system on a schedule
  ( ) D.  Call the internal endpoint straight from the topic over HTTP

                                                     [ Submit answer ]
```

**Screen 2 — after submitting (the per-option explanations are what the CSV buys you)**

```text
  Correct                                               Correct answer: A

  A. Mediate the on-premises call through an on-premises data gateway
     Correct. A gateway lets a cloud agent reach an on-premises system
     without opening an inbound firewall path. It adds a component to
     install, patch, and monitor. In this case: An on-premises data
     gateway brokers the call from the cloud without opening an inbound
     firewall path, and it must be installed and monitored.

  D. Call the internal endpoint straight from the topic over HTTP
     Incorrect for this question. Direct HTTP calls are simple but
     usually fail in a locked-down network and bypass the connector
     governance the platform already provides...

  Whole-question explanation
     Answer: Mediate the on-premises call through an on-premises data
     gateway. ... Local study-map skill 1.1 (Enterprise Integration and
     Solution Planning), mapped to the official guide: Microsoft AB-620
     study guide, skills measured as of October 16, 2026...

                                             [ Next question ]
```

**Screen 3 — question 2, the multi-select item in the same block**

```text
  Question 2 of 3               Integrate and extend agents in Copilot Studio

  ... The parts service publishes an OpenAPI definition and must
  authorise each engineer individually. Which two steps connect it
  correctly? Select two.

  [ ] A.  Create a custom connector from the OpenAPI definition and add it as a tool
  [ ] B.  Call the API from an agent flow and return the parsed response to the topic
  [ ] C.  Configure connector authentication so each call uses the caller's identity
  [ ] D.  Hard-code the endpoint URL and key inside the topic
  [ ] E.  Call the REST API from a topic with a Send HTTP request action
```

The checkbox column and the "Select two" wording are what separate it from Q1 and Q3. Five options is the multi-select shape; single-answer items carry four.

**Screen 4 — the end-of-test report**

```text
  Your result            2 / 3 correct (67%)

  By domain
    Plan and configure agent solutions                     1 / 1
    Integrate and extend agents in Copilot Studio          0 / 1
    Test and manage agents                                 1 / 1
```

Because the `Domain` column is populated, the report groups the case items with the rest of the exam instead of treating them as an unlabelled block — which is why the case study does not need its own domain label.

## What this proves, and what it does not

- It proves the file shape: three rows, mixed question types, scenario inside the stem, and an answer key that the pre-flight checker accepts (`python course/check_csv_upload.py course/AB-620/05-sample-upload/case-study-sample.csv` returns `OK`).
- It does not prove that Udemy's current template still matches ours, and it is not evidence of a completed import. Re-download the template at upload time and compare headers before loading the real exams.
- A 100-item exam behaves identically, with four such blocks in it. Use `practice-set-N.csv` plus the `case-studies.md` brief for the real uploads, which keeps stems short instead of repeating an 80-word scenario in every item. If a single self-contained file is easier to manage, `case-embedded-set-N.csv` is the variant with the scenario repeated inside all 100 stems.
