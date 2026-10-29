"""Load 360 authored PCEP-30-03 (PCEP - Certified Entry-Level Python Programmer) items.

As of October 29, 2026, the OpenEDG Python Institute lists PCEP-30-03 as Pending
Release (scheduled for October 31, 2026) and describes it as a routine exam-version
update under the PCEP-30-0x specification, while the published PCEP-30-0x syllabus
defines a 40-minute proctored exam of 30 items (plus a 5-minute NDA and tutorial) with
a cumulative passing score of 70% across four syllabus blocks: Computer Programming and
Python Fundamentals (18%, 7 live items), Control Flow - Conditional Blocks and Loops
(29%, 8 live items), Data Collections - Tuples, Dictionaries, Lists, and Strings (25%,
7 live items), and Functions and Exceptions (28%, 8 live items). Because OpenEDG has
not yet published a standalone PCEP-30-03 syllabus table ahead of October 31, 2026,
this bank baselines against those published PCEP-30-0x block weights and makes no claim
about unpublished post-release blueprint changes.

Each practice exam here is an expanded 60-item bank timed at 80 minutes so a timed run
rehearses the published pace of about 80 seconds per item while covering all 42 local
study-map skills on every sitting. Applied to 60 items, the published 18 / 29 / 25 / 28
percent weights give 10.8 / 17.4 / 15.0 / 16.8; largest-remainder rounding assigns the
two spare items to Blocks 1 and 4, giving exact per-exam counts of 11 / 17 / 15 / 17,
every count within 0.4 items of its published weight.

Per exam, 45 items are single-answer multiple-choice (including at least 15
gap-fill-styled items containing a `____` blank in a Python snippet to approximate live
code-fill and gap-fill tasks within the 17-column Udemy CSV contract) and 15 items are
five-option multiple-response (`Select two.`). Interactive drag-and-drop, sort, and
multi-slot code-insertion widgets cannot exist in a bulk-upload CSV and are disclosed
as excluded; the published exam has no case-study component, so the exporter has no
case path.
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
# Every set covers all four blocks and the exact same 42-skill study-map plan; the sets
# differ in the everyday Python small-program domains used in their snippets.
SUBTITLES = {
    1: 'Budget Trackers and Currency Calculators',
    2: 'URL Builders and Input Validators',
    3: 'Ticket Queues and Seat Booking',
    4: 'Weather Stations and Unit Converters',
    5: 'Workout Timers and Pace Trackers',
    6: 'Recipe Scalers and Pantry Audits',
}
DOMAIN_NOTES = {
    1: 'Bytecode execution, keywords, literals, numeral bases, operators, precedence, and console I/O',
    2: 'if/elif/else branching, conditional expressions, truthiness, while/for/range, loop-else, break/continue/pass',
    3: 'List slicing/mutators/comprehensions/copies, tuple packing and immutability, dictionary views, and strings',
    4: 'def/return/None, yield generators, recursion, positional/keyword defaults, LEGB/global, and exception trees',
}
# Local study-map IDs aligned to the published PCEP-30-0x syllabus blocks 1-4,
# decomposed into 42 concrete testable Python 3 skills.
SKILLS = {
    '1.1': 'Interpreter Bytecode Pipeline vs Ahead-of-Time Compilation',
    '1.2': 'Lexical, Syntactic, and Semantic Error Classification',
    '1.3': 'Reserved Keywords, Indentation Rules, and Line Comments',
    '1.4': 'Binary, Octal, Hexadecimal, Underscored, and Scientific Literals',
    '1.5': 'Identifier Validity and PEP-8 Naming Style',
    '1.6': 'True Division, Floor Division, Modulo, and Power Operators',
    '1.7': 'Operator Precedence Tiers, Unary Operators, and Associativity',
    '1.8': 'Bitwise Masks, Shifts, Relational Checks, and Short-Circuit Logic',
    '1.9': 'IEEE-754 Float Behaviour, Sequence Operators, and Augmented Assignment',
    '1.10': 'Formatted Console Output with print(), sep=, and end=',
    '1.11': 'Reading Strings with input() and Explicit Type Conversions',
    '2.1': 'Exclusive Multi-Way Branching with if, elif, and else',
    '2.2': 'Independent if Chains vs Conditional Expressions',
    '2.3': 'Truthiness of Built-In Containers, Numbers, Strings, and None',
    '2.4': 'Logical Precedence (not, and, or) and Chained Comparisons',
    '2.5': 'State-Driven Iteration and Termination with while',
    '2.6': 'Definite Iteration with for and range(start, stop, step)',
    '2.7': 'Direct Sequence and Character Iteration',
    '2.8': 'Loop Interruption and Stubs with break, continue, and pass',
    '2.9': 'Loop Completion Semantics with for-else and while-else',
    '2.10': 'Nested Loops Over Grids, Pairs, and Sublists',
    '3.1': 'List Indexing, Negative Offsets, and Stride Slicing',
    '3.2': 'In-Place List Mutators (append, extend, insert, remove, pop, sort)',
    '3.3': 'Slice Deletion with del vs Non-Mutating sorted() and len()',
    '3.4': 'List Aliasing, Shallow Copying, and Shared Inner Rows',
    '3.5': 'List Comprehensions with Transforms and Conditional Filters',
    '3.6': 'Membership Operators in and not in Across Sequences and Dicts',
    '3.7': 'Tuple Packing, Single-Element Commas, Unpacking, and Immutability',
    '3.8': 'Nested Mutability — Lists Inside Tuples and Tuples Inside Lists',
    '3.9': 'Dictionary Literals, Key Updates, del, and Safe get() / pop()',
    '3.10': 'Dictionary Views and Iteration (keys(), values(), items())',
    '3.11': 'String Quoting, Escape Sequences, and Multiline Literals',
    '3.12': 'String Slicing, Immutability, Searching, Joining, and Case Methods',
    '4.1': 'Function Definitions (def), Invocation, return Paths, and None',
    '4.2': 'Lazy Iteration with yield Generator Functions and StopIteration',
    '4.3': 'Recursive Functions, Base Cases, and RecursionError',
    '4.4': 'Positional, Keyword, and Mixed Call-Site Argument Rules',
    '4.5': 'Default Parameter Ordering and Mutable-Default Lifetime Traps',
    '4.6': 'LEGB Lookup, Local Shadowing, UnboundLocalError, and global',
    '4.7': 'Built-In Exception Tree (BaseException, Exception, LookupError, ArithmeticError)',
    '4.8': 'Diagnosing and Raising Concrete Built-In Exceptions',
    '4.9': 'Structured try / except / else / finally Ordering and Propagation',
}
VALID_TASKS = set(SKILLS)
# Published PCEP-30-0x block weights: 18 / 29 / 25 / 28 percent (total 100%).
OFFICIAL_WEIGHTS = {1: 18.0, 2: 29.0, 3: 25.0, 4: 28.0}
# 60 items: exact shares are 10.8 / 17.4 / 15.0 / 16.8; largest-remainder gives 11 / 17 / 15 / 17.
ALLOCATIONS = {n: {1: 11, 2: 17, 3: 15, 4: 17} for n in range(1, 7)}
SKILL_PLAN = {
    '1.1': 1, '1.2': 1, '1.3': 1, '1.4': 1, '1.5': 1, '1.6': 1,
    '1.7': 1, '1.8': 1, '1.9': 1, '1.10': 1, '1.11': 1,
    '2.1': 2, '2.2': 2, '2.3': 2, '2.4': 2, '2.5': 2,
    '2.6': 2, '2.7': 1, '2.8': 2, '2.9': 1, '2.10': 1,
    '3.1': 2, '3.2': 2, '3.3': 1, '3.4': 1, '3.5': 1, '3.6': 1,
    '3.7': 1, '3.8': 1, '3.9': 1, '3.10': 1, '3.11': 1, '3.12': 2,
    '4.1': 2, '4.2': 2, '4.3': 2, '4.4': 2, '4.5': 2,
    '4.6': 2, '4.7': 2, '4.8': 2, '4.9': 1,
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
