# Sources and syllabus coverage — PCEP-30-03

## Official baseline sources (checked October 29, 2026)

1. **OpenEDG Python Institute — PCEP™ Certification Overview:** `https://pythoninstitute.org/pcep`
   - Lists `PCEP-30-02` as Active and `PCEP-30-03` as **Pending Release (scheduled for October 31, 2026)**, explicitly noting that `PCEP-30-03` is a routine exam-version update under `PCEP-30-0x` and does not affect the five-year validity of credentials already earned.
2. **OpenEDG Python Institute — PCEP-30-0x Exam Syllabus:** `https://pythoninstitute.org/pcep-exam-syllabus`
   - Defines the four syllabus blocks (`18%`, `29%`, `25%`, `28%`), 30 live items, 40-minute exam duration (+5 minutes NDA/tutorial), 40 raw points max per item normalized to a percentage, and a **70% cumulative average passing score** across all blocks.
3. **OpenEDG Python Institute — PCEP Testing Policies (TestNow™):** `https://pythoninstitute.org/pcep-testing-policies`
   - Specifies browser-based TestNow™ delivery (desktop/laptop only), no scheduled breaks, mandatory NDA acceptance, **7-day retake waiting period** with unlimited retakes, candidate eligibility (18+, or 13–17 with parent/guardian consent), and approved disability time extensions.
4. **Python 3.11 Official Documentation & PEP 8:**
   - Lexical analysis, keywords, soft keywords (`match`/`case`), literals, and operator precedence: `https://docs.python.org/3/reference/lexical_analysis.html` and `https://docs.python.org/3/reference/expressions.html`
   - Compound control-flow statements (`if`, `while`, `for`, `try`) and `range()`: `https://docs.python.org/3/tutorial/controlflow.html`
   - Built-in sequence, mapping, and text types (`list`, `tuple`, `dict`, `str`): `https://docs.python.org/3/library/stdtypes.html`
   - Functions, generators, LEGB scope, and built-in exception hierarchy: `https://docs.python.org/3/tutorial/errors.html` and `https://docs.python.org/3/library/exceptions.html`
   - Style Guide for Python Code (PEP 8): `https://peps.python.org/pep-0008/`

## Pre-release baseline boundary

Because OpenEDG Python Institute had not yet published a standalone `PCEP-30-03` syllabus URL or altered block-weight table as of October 29, 2026, this package baselines against the published `PCEP-30-0x` 4-block specification above and makes no claim about unpublished post-release changes.

## 42-skill study map and per-exam item counts

| Skill ID | Official Block | Local study-map skill | Items / exam | Bank total (×6) |
|---|---|---|---:|---:|
| `1.1` | Block 1 (18%) | Interpreter Bytecode Pipeline vs Ahead-of-Time Compilation | 1 | 6 |
| `1.2` | Block 1 (18%) | Lexical, Syntactic, and Semantic Error Classification | 1 | 6 |
| `1.3` | Block 1 (18%) | Reserved Keywords, Indentation Rules, and Line Comments | 1 | 6 |
| `1.4` | Block 1 (18%) | Binary, Octal, Hexadecimal, Underscored, and Scientific Literals | 1 | 6 |
| `1.5` | Block 1 (18%) | Identifier Validity and PEP-8 Naming Style | 1 | 6 |
| `1.6` | Block 1 (18%) | True Division, Floor Division, Modulo, and Power Operators | 1 | 6 |
| `1.7` | Block 1 (18%) | Operator Precedence Tiers, Unary Operators, and Associativity | 1 | 6 |
| `1.8` | Block 1 (18%) | Bitwise Masks, Shifts, Relational Checks, and Short-Circuit Logic | 1 | 6 |
| `1.9` | Block 1 (18%) | IEEE-754 Float Behaviour, Sequence Operators, and Augmented Assignment | 1 | 6 |
| `1.10` | Block 1 (18%) | Formatted Console Output with `print()`, `sep=`, and `end=` | 1 | 6 |
| `1.11` | Block 1 (18%) | Reading Strings with `input()` and Explicit Type Conversions | 1 | 6 |
| `2.1` | Block 2 (29%) | Exclusive Multi-Way Branching with `if`, `elif`, and `else` | 2 | 12 |
| `2.2` | Block 2 (29%) | Independent `if` Chains vs Conditional Expressions | 2 | 12 |
| `2.3` | Block 2 (29%) | Truthiness of Built-In Containers, Numbers, Strings, and `None` | 2 | 12 |
| `2.4` | Block 2 (29%) | Logical Precedence (`not`, `and`, `or`) and Chained Comparisons | 2 | 12 |
| `2.5` | Block 2 (29%) | State-Driven Iteration and Termination with `while` | 2 | 12 |
| `2.6` | Block 2 (29%) | Definite Iteration with `for` and `range(start, stop, step)` | 2 | 12 |
| `2.7` | Block 2 (29%) | Direct Sequence and Character Iteration | 1 | 6 |
| `2.8` | Block 2 (29%) | Loop Interruption and Stubs with `break`, `continue`, and `pass` | 2 | 12 |
| `2.9` | Block 2 (29%) | Loop Completion Semantics with `for-else` and `while-else` | 1 | 6 |
| `2.10` | Block 2 (29%) | Nested Loops Over Grids, Pairs, and Sublists | 1 | 6 |
| `3.1` | Block 3 (25%) | List Indexing, Negative Offsets, and Stride Slicing | 2 | 12 |
| `3.2` | Block 3 (25%) | In-Place List Mutators (`append`, `extend`, `insert`, `remove`, `pop`, `sort`) | 2 | 12 |
| `3.3` | Block 3 (25%) | Slice Deletion with `del` vs Non-Mutating `sorted()` and `len()` | 1 | 6 |
| `3.4` | Block 3 (25%) | List Aliasing, Shallow Copying, and Shared Inner Rows | 1 | 6 |
| `3.5` | Block 3 (25%) | List Comprehensions with Transforms and Conditional Filters | 1 | 6 |
| `3.6` | Block 3 (25%) | Membership Operators `in` and `not in` Across Sequences and Dicts | 1 | 6 |
| `3.7` | Block 3 (25%) | Tuple Packing, Single-Element Commas, Unpacking, and Immutability | 1 | 6 |
| `3.8` | Block 3 (25%) | Nested Mutability — Lists Inside Tuples and Tuples Inside Lists | 1 | 6 |
| `3.9` | Block 3 (25%) | Dictionary Literals, Key Updates, `del`, and Safe `get()` / `pop()` | 1 | 6 |
| `3.10` | Block 3 (25%) | Dictionary Views and Iteration (`keys()`, `values()`, `items()`) | 1 | 6 |
| `3.11` | Block 3 (25%) | String Quoting, Escape Sequences, and Multiline Literals | 1 | 6 |
| `3.12` | Block 3 (25%) | String Slicing, Immutability, Searching, Joining, and Case Methods | 2 | 12 |
| `4.1` | Block 4 (28%) | Function Definitions (`def`), Invocation, `return` Paths, and `None` | 2 | 12 |
| `4.2` | Block 4 (28%) | Lazy Iteration with `yield` Generator Functions and `StopIteration` | 2 | 12 |
| `4.3` | Block 4 (28%) | Recursive Functions, Base Cases, and `RecursionError` | 2 | 12 |
| `4.4` | Block 4 (28%) | Positional, Keyword, and Mixed Call-Site Argument Rules | 2 | 12 |
| `4.5` | Block 4 (28%) | Default Parameter Ordering and Mutable-Default Lifetime Traps | 2 | 12 |
| `4.6` | Block 4 (28%) | LEGB Lookup, Local Shadowing, `UnboundLocalError`, and `global` | 2 | 12 |
| `4.7` | Block 4 (28%) | Built-In Exception Tree (`BaseException`, `Exception`, `LookupError`, `ArithmeticError`) | 2 | 12 |
| `4.8` | Block 4 (28%) | Diagnosing and Raising Concrete Built-In Exceptions | 2 | 12 |
| `4.9` | Block 4 (28%) | Structured `try` / `except` / `else` / `finally` Ordering and Propagation | 1 | 6 |
| **Total** | **Blocks 1–4 (100%)** | **42 testable Python 3 skills** | **60** | **360** |
