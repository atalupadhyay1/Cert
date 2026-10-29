"""Load 360 authored PCEP-30-02 (PCEP - Certified Entry-Level Python Programmer) items.

The OpenEDG Python Institute publishes a 40-minute proctored exam of 30 items (plus a
5-minute NDA and tutorial) for PCEP-30-02, with a cumulative passing score of 70%
across four syllabus blocks: Computer Programming and Python Fundamentals (18%, 7 live
items), Control Flow - Conditional Blocks and Loops (29%, 8 live items), Data
Collections - Tuples, Dictionaries, Lists, and Strings (25%, 7 live items), and
Functions and Exceptions (28%, 8 live items).

Each practice exam here is an expanded 60-item bank timed at 80 minutes so a timed run
still rehearses the published pace of about 80 seconds per item. Applied to 60 items,
the published 18 / 29 / 25 / 28 percent weights give 10.8 / 17.4 / 15.0 / 16.8;
largest-remainder rounding assigns the two spare items to Blocks 1 and 4, giving exact
per-exam counts of 11 / 17 / 15 / 17, every count within 0.5 items of its published
weight.

Per exam, 45 items are single-answer multiple-choice (including 15 gap-fill-styled
items containing a `____` blank in a code snippet to mirror the live code-fill and
gap-fill tasks within the 17-column Udemy CSV contract) and 15 items are five-option
multiple-response (`Select two.`). Interactive drag-and-drop, sort, and code-insertion
widgets cannot exist in a bulk-upload CSV and are disclosed as excluded; the published
exam has no case-study component, so the exporter has no case path.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent
DOMAINS = {
    1: 'Computer Programming and Python Fundamentals',
    2: 'Control Flow – Conditional Blocks and Loops',
    3: 'Data Collections – Tuples, Dictionaries, Lists, and Strings',
    4: 'Functions and Exceptions',
}
TOPICS = {
    1: 'Full-Length Mock Exam 1',
    2: 'Full-Length Mock Exam 2',
    3: 'Full-Length Mock Exam 3',
    4: 'Full-Length Mock Exam 4',
    5: 'Full-Length Mock Exam 5',
    6: 'Full-Length Mock Exam 6',
}
# Every set covers all four blocks and the exact same 36-skill study-map plan; the sets
# differ in the small-program problem domains used in their code snippets and prompts.
SUBTITLES = {
    1: 'CLI Utilities and Number Processing',
    2: 'Text Cleaning and Log Inspection',
    3: 'Inventory Counters and Cart Totals',
    4: 'Sensor Readings and Threshold Checks',
    5: 'Gradebook Tables and Quiz Scoring',
    6: 'Schedule Parsers and Config Helpers',
}
DOMAIN_NOTES = {
    1: 'Execution model, keywords, literals, numeral bases, operators, precedence, and console I/O',
    2: 'Conditional branching, nested conditions, while/for/range loops, loop-else, break/continue/pass',
    3: 'List indexing/slicing/methods/comprehensions/aliasing, tuples, dictionaries, and string operations',
    4: 'User-defined functions, generators, recursion, argument passing, scope/global, and exception handling',
}
# Local study-map IDs aligned to PCEP-30-02 syllabus objectives 1.1-1.5, 2.1-2.2,
# 3.1-3.4, and 4.1-4.4, broken into 41 concrete testable skills.
SKILLS = {
    '1.1': 'Compilation vs Interpretation and Execution Model',
    '1.2': 'Lexis, Syntax, and Semantics Distinctions',
    '1.3': 'Keywords, Instructions, Indentation, and Comments',
    '1.4': 'Literals, Numeral Systems, and Scientific Notation',
    '1.5': 'Variable Naming Rules and PEP-8 Conventions',
    '1.6': 'Arithmetic Operators, Floor Division, Modulo, and Exponentiation',
    '1.7': 'Operator Precedence, Unary Signs, and Right-Sided Binding',
    '1.8': 'Bitwise, Relational, Boolean Operators, and Short-Circuiting',
    '1.9': 'Floating-Point Accuracy, String Operators, and Shortcut Assignments',
    '1.10': 'Console Output with print(), sep=, and end=',
    '1.11': 'Console Input with input() and Type Casting (int, float, str, bool)',
    '2.1': 'Single and Chained Branching with if, elif, and else',
    '2.2': 'Nested Conditionals and Truthiness of Built-In Values',
    '2.3': 'Compound Boolean Conditions and Chained Comparisons',
    '2.4': 'Counting and Accumulator Loops with while',
    '2.5': 'Definite Iteration with for and range(start, stop, step)',
    '2.6': 'Iterating Directly Over Sequences and Enumerated Values',
    '2.7': 'Controlling Loops with break, continue, and pass',
    '2.8': 'Post-Loop Execution with while-else and for-else Clauses',
    '2.9': 'Nested Loops Over 2D Grids and Pairwise Combinations',
    '3.1': 'List Indexing, Negative Indices, and Slicing Rules',
    '3.2': 'List Mutation Methods (append, insert, remove, pop, sort, index)',
    '3.3': 'Deleting Elements or Slices with del, len(), and sorted()',
    '3.4': 'List Aliasing vs Shallow Slicing/Copying and Nested Matrices',
    '3.5': 'List Comprehensions with Filtering and Expressions',
    '3.6': 'Membership Testing with in and not in Across Collections',
    '3.7': 'Tuple Construction, Single-Element Syntax, Unpacking, and Immutability',
    '3.8': 'Mutable Lists Inside Tuples vs Tuples Inside Lists',
    '3.9': 'Dictionary Creation, Key Lookup, Insertion, Update, and Deletion',
    '3.10': 'Dictionary Iteration with keys(), values(), items(), and get()',
    '3.11': 'String Literals, Escape Sequences, Quotes, and Multiline Strings',
    '3.12': 'String Indexing, Slicing, Immutability, and Common String Methods',
    '4.1': 'Defining Functions, Invoking Them, return Paths, and Implicit None',
    '4.2': 'Generator Functions Using yield and Lazy Iteration',
    '4.3': 'Recursive Functions, Base Cases, and Call-Stack Termination',
    '4.4': 'Positional, Keyword, and Mixed Argument Passing Rules',
    '4.5': 'Default Parameter Values and Shared-Default Pitfalls',
    '4.6': 'Name Scopes, Shadowing, and Modifying Globals with global',
    '4.7': 'Built-In Exception Hierarchy (BaseException, LookupError, ArithmeticError)',
    '4.8': 'Raising and Diagnosing Concrete Built-In Exceptions (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError)',
    '4.9': 'Handling and Propagating Exceptions with Ordered try-except Branches',
}
VALID_TASKS = set(SKILLS)
# OpenEDG Python Institute publishes 18 / 29 / 25 / 28 percent across the four blocks.
OFFICIAL_WEIGHTS = {1: 18.0, 2: 29.0, 3: 25.0, 4: 28.0}
# 60 items: exact shares are 10.8 / 17.4 / 15.0 / 16.8; largest-remainder gives 11 / 17 / 15 / 17.
ALLOCATIONS = {n: {1: 11, 2: 17, 3: 15, 4: 17} for n in range(1, 7)}
SKILL_PLAN = {
    '1.1': 1, '1.2': 1, '1.3': 1, '1.4': 1, '1.5': 1, '1.6': 1,
    '1.7': 1, '1.8': 1, '1.9': 1, '1.10': 1, '1.11': 1,
    '2.1': 2, '2.2': 2, '2.3': 2, '2.4': 2, '2.5': 2, '2.6': 1,
    '2.7': 2, '2.8': 2, '2.9': 2,
    '3.1': 2, '3.2': 2, '3.3': 1, '3.4': 1, '3.5': 1, '3.6': 1,
    '3.7': 1, '3.8': 1, '3.9': 1, '3.10': 1, '3.11': 1, '3.12': 2,
    '4.1': 2, '4.2': 1, '4.3': 2, '4.4': 2, '4.5': 2, '4.6': 2,
    '4.7': 2, '4.8': 2, '4.9': 2,
}
# Fifteen multiple-response items per set, spread across the four blocks.
MULTI_PLAN = {1: 3, 2: 4, 3: 4, 4: 4}
TYPE_PLAN = {'multiple-choice': 45, 'multi-select': 15}
GAP_FILL_MIN = 15
ITEM_TOTAL = sum(TYPE_PLAN.values())


def _load(number):
    rows = []
    path = HERE / 'questions' / f'{number}.txt'
    for n, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip() or line.startswith('#'):
            continue
        parts = line.split('|')
        if len(parts) != 6:
            raise ValueError(f'{path.name} line {n}: expected 6 fields, found {len(parts)}')
        task, kind, answers, distractors, question, reason = [p.strip() for p in parts]
        if task not in VALID_TASKS:
            raise ValueError(f'{path.name} line {n}: unknown skill {task}')
        if kind not in ('S', 'M2'):
            raise ValueError(f'{path.name} line {n}: unknown kind {kind}')
        keys = answers.split(',') + distractors.split(',')
        if any(k not in TERMS for k in keys):
            raise ValueError(f'{path.name} line {n}: unknown option key '
                             f'{[k for k in keys if k not in TERMS]}')
        rows.append(dict(
            id=f'T{number}-Q{len(rows) + 1:03d}', number=number, domain=int(task.split('.')[0]),
            task=task, kind=kind, keys=keys, answers=answers.split(','),
            distractors=distractors.split(','), question=question, reason=reason))
    return rows


BANK = {n: _load(n) for n in range(1, 7)}
