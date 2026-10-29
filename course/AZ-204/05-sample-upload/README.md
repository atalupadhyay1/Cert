# Sample Case-Study Upload (`AZ-204`)

`case-study-sample.csv` contains the **12 self-contained case-study questions** (`4` cases × `3` items: `Vespera Retail`, `Kova Footwear`, `BriskCart Loyalty`, and `Cinder Coffee Roasters`) from **Full-Length Mock Exam 1**.

## Purpose
Upload `case-study-sample.csv` into a scratch Udemy Practice Test before importing the six 100-question sets (`03-practice-sets/set-{1..6}/case-embedded-set-{1..6}.csv`) to verify:
1. UTF-8 BOM rendering of inline code backticks and `→` four-step sequence arrows (`Question 11`).
2. Self-contained scenario readability on desktop and mobile when Udemy shuffles question order.
3. Exact 5-domain mapping under Udemy's Knowledge Areas summary.

Regenerate anytime with:
```bash
python3 course/AZ-204/04-resources/make_sample.py
```
