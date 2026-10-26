#!/usr/bin/env python3
"""Check every course landing page answers the three mandatory Udemy fields.

Udemy will not publish a course until these three questions are answered:
what students will learn, the requirements or prerequisites, and who the
course is for. This checker fails when a landing page is missing any of them,
when a field is empty or placeholder-only, or when a field has fewer than
three concrete items, so a course cannot ship with a blank publishing form.

Usage:
    python3 course/check_landing_page_fields.py            # all courses
    python3 course/check_landing_page_fields.py CCAO-F     # one course
"""
import re
import sys
from pathlib import Path

COURSE_ROOT = Path(__file__).resolve().parent
FIELDS = (
    ('learn', re.compile(r'^#{2,3}\s*(?:\d+\.\s*)?what (?:will students learn|you will learn)', re.I | re.M),
     'What will students learn in your course?'),
    ('requirements', re.compile(r'^#{2,3}\s*(?:\d+\.\s*)?(?:course requirements|requirements|what are the requirements)', re.I | re.M),
     'What are the requirements or prerequisites for taking your course?'),
    ('audience', re.compile(r'^#{2,3}\s*(?:\d+\.\s*)?who (?:is )?this course (?:is )?for', re.I | re.M),
     'Who is this course for?'),
)
PLACEHOLDERS = ('TODO', 'TBD', 'PLACEHOLDER', 'lorem ipsum')


def section_body(text, match):
    start = match.start()
    remainder = text[match.end():]
    stop = re.search(r'^#{2,3} ', remainder, re.M)
    return remainder[:stop.start()] if stop else remainder


def check(path):
    text = path.read_text(encoding='utf-8', errors='strict')
    problems = []
    for name, pattern, label in FIELDS:
        match = pattern.search(text)
        if not match:
            problems.append(f'missing field: {label}')
            continue
        body = section_body(text, match)
        if not body.strip():
            problems.append(f'empty field: {label}')
            continue
        for placeholder in PLACEHOLDERS:
            if placeholder.casefold() in body.casefold():
                problems.append(f'placeholder {placeholder!r} in: {label}')
        items = len(re.findall(r'^\s*(?:[•\-*]|\d+\.)\s+\S', body, re.M))
        if items < 3:
            problems.append(f'only {items} item(s) in: {label} (need at least 3)')
    return problems


def main(argv):
    wanted = {a.upper() for a in argv}
    pages = sorted(COURSE_ROOT.glob('*/01-landing-page/landing-page.md'))
    if wanted:
        pages = [p for p in pages if p.parts[-3].upper() in wanted]
    if not pages:
        print('No landing pages found')
        return 1
    failures = 0
    for page in pages:
        problems = check(page)
        slug = page.parts[-3]
        if problems:
            failures += 1
            for problem in problems:
                print(f'FAIL {slug}: {problem}')
        else:
            print(f'PASS {slug}')
    print(f'{len(pages) - failures}/{len(pages)} landing page(s) answer all three mandatory fields.')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
