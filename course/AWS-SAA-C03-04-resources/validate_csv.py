#!/usr/bin/env python3
"""
validate_csv.py — Validates AWS-SAA-C03 / AB-100 / AB-900 / AZ-900 practice
test CSVs against the Udemy v2 Bulk Question Uploader template format.

Supports:
  - AWS SAA-C03: AWS Certified Solutions Architect - Associate
  - AB-100: Agentic AI Business Solutions Architect
  - AB-900: Microsoft 365 Copilot and Agent Administration Fundamentals
  - AZ-900: Microsoft Azure Fundamentals

Template columns (in order, total 17):
  Question, Question Type,
  Answer Option 1, Explanation 1,
  Answer Option 2, Explanation 2,
  Answer Option 3, Explanation 3,
  Answer Option 4, Explanation 4,
  Answer Option 5, Explanation 5,
  Answer Option 6, Explanation 6,
  Correct Answers,
  Overall Explanation,
  Domain

Usage:
  python validate_csv.py practice-set-1.csv
  python validate_csv.py path/to/*.csv
"""

import csv
import sys
from collections import Counter
from pathlib import Path

REQUIRED_HEADERS = [
    "Question",
    "Question Type",
    "Answer Option 1", "Explanation 1",
    "Answer Option 2", "Explanation 2",
    "Answer Option 3", "Explanation 3",
    "Answer Option 4", "Explanation 4",
    "Answer Option 5", "Explanation 5",
    "Answer Option 6", "Explanation 6",
    "Correct Answers",
    "Overall Explanation",
    "Domain",
]
# Total: 17 columns
VALID_TYPES = {"multiple-choice", "multi-select"}
VALID_DOMAINS = {
    # AWS SAA-C03 domains
    "Design Secure Architectures",
    "Design Resilient Architectures",
    "Design High-Performing Architectures",
    "Design Cost-Optimized Architectures",
    # AB-100 domains
    "Plan AI-powered Business Solutions",
    "Design AI-powered Business Solutions",
    "Deploy AI-powered Business Solutions",
    # AB-900 domains
    "Identify the Core Features and Objects of Microsoft 365 Services",
    "Understand Data Protection and Governance Tasks for Microsoft 365 and Copilot",
    "Perform Basic Administrative Tasks for Copilot and Agents",
    # AZ-900 domains
    "Describe Cloud Concepts",
    "Describe Azure Architecture and Services",
    "Describe Azure Management and Governance",
}
# Acceptable documentation URLs per course
ALLOWED_DOC_HOSTS = (
    "docs.aws.amazon.com",  # AWS
    "aws.amazon.com",       # AWS marketing
    "learn.microsoft.com",  # Microsoft Learn
    "learn.aws.amazon.com", # AWS Skill Builder
    "docs.microsoft.com",   # Microsoft docs
)


def validate_file(path: Path) -> bool:
    print(f"\n{'=' * 70}\nValidating: {path}\n{'=' * 70}")
    errors = []
    type_counter = Counter()
    domain_counter = Counter()

    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.reader(fh)
        try:
            header = next(reader)
        except StopIteration:
            print("❌ File is empty.")
            return False

        if header != REQUIRED_HEADERS:
            errors.append(f"Header mismatch.\n  Expected: {REQUIRED_HEADERS}\n  Got:      {header}")

        for row_num, row in enumerate(reader, start=2):
            if len(row) < len(REQUIRED_HEADERS):
                errors.append(f"Row {row_num}: only {len(row)} columns (need {len(REQUIRED_HEADERS)}).")
                continue

            question = row[0]
            qtype = row[1]
            opts = [row[2], row[4], row[6], row[8], row[10], row[12]]
            expls = [row[3], row[5], row[7], row[9], row[11], row[13]]
            correct_raw = row[14]
            overall = row[15]
            domain = row[16]

            # Question Type
            qtype_norm = qtype.strip().lower()
            if qtype_norm not in VALID_TYPES:
                errors.append(f"Row {row_num}: invalid Question Type '{qtype}'.")
            else:
                type_counter[qtype_norm] += 1

            # Correct Answers
            try:
                indices = [int(x.strip()) for x in correct_raw.split(",") if x.strip()]
            except ValueError:
                errors.append(f"Row {row_num}: Correct Answers '{correct_raw}' is not numeric.")
                indices = []

            # Cross-check: Question Type must match Correct Answers shape
            if qtype_norm == "multiple-choice" and len(indices) != 1:
                errors.append(
                    f"Row {row_num}: Question Type is 'multiple-choice' but Correct Answers has "
                    f"{len(indices)} entries ({correct_raw!r}); expected exactly 1."
                )
            if qtype_norm == "multi-select" and len(indices) < 2:
                errors.append(
                    f"Row {row_num}: Question Type is 'multi-select' but Correct Answers has "
                    f"{len(indices)} entries ({correct_raw!r}); expected 2 or more."
                )

            for i in indices:
                if i < 1 or i > 6:
                    errors.append(f"Row {row_num}: Correct Answers index {i} out of range (1-6).")
                elif not opts[i - 1].strip():
                    errors.append(f"Row {row_num}: Correct option {i} is empty.")

            # Options 1-4 must be non-empty
            for idx in range(4):
                if not opts[idx].strip():
                    errors.append(f"Row {row_num}: Option {idx + 1} is empty.")

            # At least one documentation reference URL required
            has_doc = any(host in overall for host in ALLOWED_DOC_HOSTS)
            if not has_doc:
                for e in expls:
                    if any(host in e for host in ALLOWED_DOC_HOSTS):
                        has_doc = True
                        break
            if not has_doc:
                errors.append(
                    f"Row {row_num}: No documentation reference URL (AWS or Microsoft) found in Overall Explanation or per-option explanations."
                )

            # Domain
            if domain not in VALID_DOMAINS:
                errors.append(f"Row {row_num}: Domain '{domain}' not in valid set.")
            else:
                domain_counter[domain] += 1

    total_rows = sum(type_counter.values())
    print(f"\nTotal questions: {total_rows}")
    print(f"\nBy Question Type:")
    for t, c in sorted(type_counter.items()):
        print(f"  {t}: {c}")
    print(f"\nBy Domain:")
    for d, c in sorted(domain_counter.items()):
        print(f"  {d}: {c}")

    if errors:
        print(f"\n❌ {len(errors)} ERRORS FOUND:")
        for e in errors[:50]:
            print(f"  - {e}")
        if len(errors) > 50:
            print(f"  ... and {len(errors) - 50} more")
        return False

    print("\n✅ All validation checks passed.")
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_csv.py <file1.csv> [file2.csv ...]")
        sys.exit(1)

    all_ok = True
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"❌ File not found: {arg}")
            all_ok = False
            continue
        if not validate_file(path):
            all_ok = False

    sys.exit(0 if all_ok else 2)


if __name__ == "__main__":
    main()
