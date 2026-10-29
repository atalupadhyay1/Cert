# PCEP – Certified Entry-Level Python Programmer (PCEP-30-03) — Full-Length Mock Exam 2

Entry-Level Python Programmer · 60 questions · 80 minutes · 70% cumulative passing score

Blueprint-weighted expanded mock exam. Item mix: 45 multiple-choice (including 16 single-blank `____` code-fill / gap-fill items) and 15 multiple-response items (the selection count is stated in each multi-response stem). Baseline & pre-release notice: as of October 29, 2026, OpenEDG Python Institute lists PCEP-30-03 as Pending Release (scheduled for October 31, 2026) and describes it as a routine exam-version update under PCEP-30-0x. Because OpenEDG has not yet published a standalone PCEP-30-03 block-weight table ahead of release, this set baselines against the published PCEP-30-0x specification — 30 live items in 40 minutes (+5-minute NDA/tutorial) across four blocks weighted 18 / 29 / 25 / 28 percent — as an expanded 2x bank (60 items in 80 minutes, ~80 seconds per item) and makes no claim about unpublished post-release blueprint changes. The Python Institute publishes no fixed split between single-select, multiple-select, and interactive items, so the 45 / 15 mix and single-blank `____` approximations are authoring choices within the 17-column CSV contract; interactive drag-and-drop, sort, and multi-slot code-insertion widgets are excluded and disclosed. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content verified on CPython 3.11, not actual, recalled, or copied OpenEDG exam items.

## Questions

---

## Block 1 — Computer Programming and Python Fundamentals (18%) — Bytecode execution, keywords, literals, numeral bases, operators, precedence, and console I/O

### 1. A web-form validator script `check_form.py` has `print('Booting validator')` on line 1 and an unclosed parenthesis on line 48. When an engineer runs `python3 check_form.py`, what happens?

- A. When an unhandled runtime error occurs, CPython automatically rolls back earlier `print()` calls and file writes
- B. CPython parses the entire `.py` file for syntax errors before executing even the first top-level statement
- C. CPython runs lines 1 through 49 first and reports a `SyntaxError` on line 50 only if control reaches line 50
- D. CPython links `.py` source ahead of time into a standalone native CPU executable that runs without a Python runtime

### 2. In a URL query builder, the line `slug = 'items' + * 'v2'` uses only legal Python tokens (`slug`, `=`, `'items'`, `+`, `*`, `'v2'`), yet fails before execution starts because `*` cannot immediately follow binary `+`. Which error category does this represent?

- A. A lexical error because the character or token itself does not belong to valid Python token forms
- B. A syntactic error because valid Python tokens are arranged in a sequence that violates Python grammar rules
- C. A PEP-8 style violation that causes CPython to refuse compilation before execution begins
- D. A semantic runtime error because a grammatically valid statement attempts an operation with no valid runtime meaning

### 3. A team standardizing an input-sanitization script reviews Python's block-layout and comment rules. Which two statements accurately describe Python 3 syntax and PEP-8 style? Select two.

- A. C-style `/* ... */` delimiters comment out multi-line blocks in Python
- B. Curly braces `{ ... }` around `if` and `for` bodies so whitespace is completely ignored
- C. Everything after `#` outside a string literal to the end of that physical line is ignored by the parser
- D. A PEP-8 style violation that causes CPython to refuse compilation before execution begins
- E. Consistent 4-space indentation for each nested suite without mixing tabs and spaces in the same block

### 4. A rate-limit validator defines `max_requests = 4e2` and inspects `max_requests`. Which value does `4e2` evaluate to in Python 3?

- A. `SyntaxError`
- B. `400`
- C. `42`
- D. `400.0`

### 5. A developer is naming helper variables inside a URL slug parser. Which two names are valid variable identifiers in Python 3.10+? Select two.

- A. `lambda`
- B. `user@host`
- C. `fx-rate`
- D. `_cached_slug`
- E. `case`

### 6. Complete the token checksum expression `check_digit = code_sum ____ 10` so `check_digit` receives the base-10 remainder (`7` when `code_sum` is `47`). Which arithmetic operator fills the blank?

- A. `**`
- B. `/`
- C. `//`
- D. `%`

### 7. An exponential retry expression in an endpoint poller evaluates `backoff_ms = 2 ** 2 ** 3`. What integer is bound to `backoff_ms`?

- A. `16`
- B. `256`
- C. `64`
- D. `32`

### 8. An IPv4 subnet helper manipulates integer bitmasks bit by bit. Which two tokens are bitwise integer operators in Python 3? Select two.

- A. `&`
- B. `**`
- C. `^`
- D. `//`
- E. `and`

### 9. Complete `pad = '-'; pad ____ 4` in a CLI form border helper so `pad` becomes `'----'` by repeating the hyphen four times. Which augmented assignment operator fills the blank?

- A. `*=`
- B. `+=`
- C. `//=`
- D. `**`

### 10. Complete `print('https://api.local', 'v2', 'users', ____)` so the URL builder prints `https://api.local/v2/users` on one line. Which keyword argument fills the blank?

- A. `end=', '`
- B. `end='!'`
- C. `sep='/'`
- D. `sep=':'`

### 11. Complete `endpoint = '/users/' + ____(account_id)` when `account_id = 408` so concatenation builds `'/users/408'` instead of raising `TypeError`. Which built-in callable fills the blank?

- A. `int`
- B. `bool`
- C. `float`
- D. `str`

---

## Block 2 — Control Flow – Conditional Blocks and Loops (29%) — if/elif/else branching, conditional expressions, truthiness, while/for/range, loop-else, break/continue/pass

### 12. Complete the HTTP status classifier `if status == 200: tag = 'OK'` / `elif status == 404: tag = 'MISSING'` / `____:` / `    tag = 'OTHER'` so every unmatched code falls into the final catch-all suite. Which keyword fills the blank?

- A. `else`
- B. `pass`
- C. `elif`
- D. `for`

### 13. A port-range checker sets `port = 443` and runs `if port < 0: print('CRIT')` / `elif port < 1024: print('OK')` / `elif port < 49152: print('WARN')` / `else: print('ALERT')`. What is printed?

- A. `OK`
- B. `ALERT`
- C. `CRIT`
- D. `WARN`

### 14. A form fee validator sets `subtotal = 75` and evaluates `fee = 0 if subtotal >= 50 else 5`. What integer is assigned to `fee`?

- A. `True`
- B. `0`
- C. `SyntaxError`
- D. `5`

### 15. A username checker sets `length = 14; tag = 'IDLE'` and runs two sequential `if` blocks: `if length >= 6: tag = 'OK'` followed by `if length >= 12: tag = 'WARN'`, then prints `tag`. What is printed?

- A. `GOLD` followed by `SILVER`
- B. `OK`
- C. `ALERT`
- D. `WARN`

### 16. A query-string sanitizer tests `if raw_param:` on parsed values. Which two values of `raw_param` evaluate to `True` in a Boolean context? Select two.

- A. `'False'`
- B. `()`
- C. `None`
- D. `''`
- E. `['']`

### 17. A form checkbox parser receives the string `'0'` from a hidden field and evaluates `flag = bool('0')`. What value is assigned to `flag`?

- A. `False`
- B. `True`
- C. `0`
- D. `ValueError`

### 18. A network config validator must return `True` if and only if integer `port` is between `1024` and `65535` inclusive. Which two Python expressions implement that check accurately? Select two.

- A. `port >= 1024 && port <= 65535`
- B. `port >= 1024 & port <= 65535`
- C. `port >= 1024 or port <= 65535`
- D. `1024 <= port <= 65535`
- E. `port >= 1024 and port <= 65535`

### 19. Complete the blank-field guard `if ____ username.strip(): print('Empty username')` so the warning prints whenever `username.strip()` returns the falsy empty string `''`. Which unary logical operator fills the blank?

- A. `and`
- B. `not`
- C. `in`
- D. `or`

### 20. Complete the leading-slash trimmer `path = '///v2'` / `____ path.startswith('/'):` / `    path = path[1:]` so slashes are removed one by one until none remain at index `0`. Which keyword fills the blank?

- A. `elif`
- B. `with`
- C. `for`
- D. `while`

### 21. An input-buffer reader reviews five `while` loop snippets to avoid hanging the validation service. Which two snippets are guaranteed to terminate after a finite number of iterations? Select two.

- A. `n = 6` followed by `while n > 0: n -= 2`
- B. `n = 5` followed by `while n > 0: pass`
- C. `n = 1` followed by `while n > 0: n += 1`
- D. `n = 4` followed by `while n % 2 == 0: n += 2`
- E. `n = 16` followed by `while n >= 2: n //= 2`

### 22. A retry validator needs a `for` loop that runs exactly three times. Which two `range()` calls generate exactly three integers? Select two.

- A. `range(3, 12, 3)`
- B. `range(8, 2)`
- C. `range(2, 10, 2)`
- D. `range(9, 0, -3)`
- E. `range(3, 9, 3)`

### 23. An input chunker evaluates `print(list(range(8, 2)))` using Python's default step of `+1`. What is printed?

- A. `[]`
- B. `ValueError`
- C. `[40, 30, 20, 10]`
- D. `0`

### 24. A URL path counter runs `slashes = 0` / `for ch in '/api/v2/ok':` / `    if ch == '/': slashes += 1` / `print(slashes)`. What integer is printed?

- A. `3`
- B. `1`
- C. `2`
- D. `9`

### 25. Complete the banned-character scanner `for ch in token:` / `    if ch == ' ': valid = False; ____` so the loop stops immediately at the first space instead of scanning the rest of `token`. Which keyword fills the blank?

- A. `pass`
- B. `continue`
- C. `break`
- D. `else`

### 26. Complete the header sanitizer `for line in raw_lines:` / `    if line.startswith('#'): ____` / `    cleaned.append(line)` so comment lines are skipped while remaining lines are still collected. Which keyword fills the blank?

- A. `pass`
- B. `break`
- C. `return`
- D. `continue`

### 27. A slug validator runs `for ch in 'api_v2':` / `    if ch == '@': print('HALT'); break` / `else: print('CLEAN')`. What does it print?

- A. Nothing is printed
- B. `SyntaxError`
- C. `CLEAN`
- D. `HALT`

### 28. An endpoint matrix builder sets `routes = 0` and runs `for ver in ['v1', 'v2']:` / `    for verb in ['GET', 'POST', 'DELETE']: routes += 1` / `print(routes)`. What integer is printed?

- A. `8`
- B. `2`
- C. `5`
- D. `6`

---

## Block 3 — Data Collections – Tuples, Dictionaries, Lists, and Strings (25%) — List slicing/mutators/comprehensions/copies, tuple packing and immutability, dictionary views, and strings

### 29. A breadcrumb trail stores `steps = [10, 20, 30, 40]`. What list does `steps[::-1]` return?

- A. `IndexError`
- B. `[20, 30]`
- C. `[40, 50]`
- D. `[40, 30, 20, 10]`

### 30. Given `steps = [10, 20, 30, 40]`, what happens when a pagination helper evaluates `steps[2:99]`?

- A. `[40, 30, 20, 10]`
- B. `[]`
- C. `[30, 40]`
- D. `IndexError`

### 31. Complete `parts = ['v2', 'users']; parts.____(0, 'api')` so `'api'` is placed at index `0` and `parts` becomes `['api', 'v2', 'users']`. Which list method name fills the blank?

- A. `remove`
- B. `append`
- C. `insert`
- D. `extend`

### 32. A validator maintains `items = ['id', 'email']`. Which two expressions mutate the existing `items` list object in place? Select two.

- A. `sorted(items)`
- B. `items[:]`
- C. `items.append(x)`
- D. `items.extend(seq)`
- E. `items + [x]`

### 33. Complete `ordered = ____(params)` so `ordered` receives a new alphabetically ordered `list` while the original `params` list stays in its unsorted order. Which built-in callable fills the blank?

- A. `pop`
- B. `sorted`
- C. `remove`
- D. `insert`

### 34. An input pipeline holds `items = ['host', 'port']` and needs an independent outer list copy before adding test fields. Which two expressions create a shallow copy of `items`? Select two.

- A. `backup = items`
- B. `list(items)`
- C. `items.sort()`
- D. `items.remove(x)`
- E. `items.copy()`

### 35. An integer sanitizer wants a new list doubling only positive entries from `nums`. Which list comprehension has valid Python 3 syntax?

- A. `[n * 2 for n in nums if n > 0]`
- B. `[n * 2 if n > 0 for n in nums]`
- C. `0 if subtotal >= 50`
- D. `subtotal >= 50 ? 0 : 5`

### 36. Complete `if '@' ____ email_addr: errors.append('missing_at')` so the error records whenever `'@'` does not appear anywhere in `email_addr`. Which membership operator fills the blank?

- A. `from`
- B. `is`
- C. `not in`
- D. `elif`

### 37. A route definition stores `route = ('GET', '/health')` and a bug executes `route[0] = 'POST'`. Which exception does Python raise?

- A. `IndexError`
- B. `None`
- C. `TypeError`
- D. `KeyError`

### 38. A router caches responses in a dictionary keyed by route metadata. Which two statements accurately describe using tuples vs lists as Python `dict` keys? Select two.

- A. Membership `k in d` checks both keys and values simultaneously
- B. A tuple containing a `list` (`(10, [20])`) cannot be used as a `dict` key and raises `TypeError`
- C. A tuple of immutable values (`(10, 20)`) can be used as a `dict` key, whereas a `list` (`[10, 20]`) raises `TypeError`
- D. Curly braces `{ ... }` around `if` and `for` bodies so whitespace is completely ignored
- E. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects

### 39. A header dictionary literal evaluates `headers = {'Accept': 'text', 'Host': 'local', 'Accept': 'json'}` and prints `len(headers)`. What integer is printed?

- A. `KeyError`
- B. `2`
- C. `3`
- D. `1`

### 40. A query-parameter validator iterates over a dictionary `d`. Which two statements accurately describe Python 3 dictionary membership and view methods? Select two.

- A. Membership `k in d` checks only dictionary keys, not dictionary values
- B. `backup = items`
- C. Membership `k in d` checks both keys and values simultaneously
- D. `.items()` yields `(key, value)` 2-tuples suitable for `for k, v in d.items():` unpacking
- E. `(42)`

### 41. A multi-line header helper sets `line = 'a\nb'` and evaluates `len(line)`. What does `len(line)` return and why?

- A. `3`, because `\n` is stored as one newline character rather than two separate characters
- B. `None`
- C. `4`, because Python counts `\` and `n` separately in every string literal
- D. `SyntaxError`

### 42. Complete `clean_token = raw_token.____()` so `'  token-42\n'` becomes `'token-42'` with leading spaces and trailing newline removed while keeping the internal hyphen. Which string method name fills the blank?

- A. `index`
- B. `strip`
- C. `split`
- D. `find`

### 43. A URL splitter evaluates `'https://example.org/docs'.split('/')`. What list is returned?

- A. `[]`
- B. `ValueError`
- C. `['https:', '', 'example.org', 'docs']`
- D. `'token-42'`

---

## Block 4 — Functions and Exceptions (28%) — def/return/None, yield generators, recursion, positional/keyword defaults, LEGB/global, and exception trees

### 44. Which two statements accurately describe `return` behaviour inside an ordinary Python function (with no `yield`)? Select two.

- A. `None`, because reaching the end of a function body or a bare `return` implicitly returns `None`
- B. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects
- C. Declaring every parameter `global` inside the function header
- D. Replacing every `return` statement with `break` inside the `def` body
- E. The first executed `return` exits the function immediately and skips all remaining statements in its body

### 45. A beginner writes `def clean_host(h): print(h.lower())` with no `return`, then runs `host = clean_host('API.LOCAL')`. What happens?

- A. `True`
- B. `NameError`
- C. `SyntaxError`
- D. It prints the text inside the function and then assigns `None` to the caller variable because `print()` returns `None`

### 46. Complete `tokens = token_stream(); first_tok = ____(tokens)` so `tokens` advances to its first `yield` expression and returns that single yielded item. Which built-in function name fills the blank?

- A. `int`
- B. `sorted`
- C. `len`
- D. `next`

### 47. Which two statements accurately describe Python generator functions defined with `yield`? Select two.

- A. `yield` suspends the function frame with its local variables intact and resumes right after `yield` on the next `next()` call
- B. Calling a function whose body contains `yield` returns a generator iterator object without executing the body yet
- C. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects
- D. CPython links `.py` source ahead of time into a standalone native CPU executable that runs without a Python runtime
- E. Replacing every `return` statement with `break` inside the `def` body

### 48. To count ordered header arrangements, a validator defines `def perms(k):` returning `1` when `k <= 1` and `k * perms(k - 1)` otherwise. Calling `perms(4)` evaluates to which integer?

- A. `24`
- B. `10`
- C. `120`
- D. `RecursionError`

### 49. A developer writes `def descend(k): return descend(k - 1)` with no `if` check and calls `descend(3)`. What happens at runtime?

- A. `RecursionError` because without a reachable base case the call stack exceeds Python's recursion limit
- B. `SyntaxError`
- C. `0`
- D. `None`

### 50. An API builder defines `def build_url(host, port=443): return f'{host}:{port}'` and a caller writes `build_url(port=8080, 'api.local')`. What happens?

- A. `20`
- B. `TypeError` because the same parameter receives both a positional argument and a keyword argument
- C. `SyntaxError` because a positional argument cannot follow a keyword argument at a call site
- D. `None`

### 51. Given `def build_url(host, port=443): return host`, what happens at runtime when a caller executes `build_url('api.local', host='backup.local')`?

- A. `TypeError` because the same parameter receives both a positional argument and a keyword argument
- B. `SyntaxError` because a positional argument cannot follow a keyword argument at a call site
- C. `20`
- D. `KeyError`

### 52. A validator defines `def add_err(msg, errs=[]): errs.append(msg); return errs` and notices old errors leaking across separate requests. Which two statements explain the bug and its idiomatic Python fix? Select two.

- A. Membership `k in d` checks both keys and values simultaneously
- B. Declaring every parameter `global` inside the function header
- C. Default values are evaluated once at `def` time, so one shared list accumulates items across calls that omit the argument
- D. Use `buf=None` in the signature and initialize `if buf is None: buf = []` inside the function body
- E. It prints `True` because Python automatically converts float literals to exact base-10 `Decimal` objects

### 53. Which function header obeys Python 3's rule for ordering required parameters and default-valued parameters?

- A. `subtotal >= 50 ? 0 : 5`
- B. `def quote(amount, rate=1.1, fee=0):`
- C. `def quote(rate=1.1, amount, fee=0):`
- D. `calc(base=100, 0.2)`

### 54. A config module sets `timeout = 10`, defines `def override(): timeout = 42`, calls `override()`, and then prints `timeout` at module level. What integer is printed?

- A. `10`
- B. `42`
- C. `UnboundLocalError`
- D. `NameError`

### 55. A request counter sets `hits = 10` at module level, defines `def bump(): print(hits); hits = hits + 1`, and calls `bump()`. Which exception is raised?

- A. `10`
- B. `KeyError`
- C. `11`
- D. `UnboundLocalError`

### 56. In Python 3's exception hierarchy, which two concrete built-in exceptions are direct subclasses of `LookupError`? Select two.

- A. `TypeError`
- B. `KeyError`
- C. `ZeroDivisionError`
- D. `ValueError`
- E. `IndexError`

### 57. Which built-in class sits at the very root of Python 3's entire exception class hierarchy, above `Exception`, `SystemExit`, and `KeyboardInterrupt`?

- A. `ValueError`
- B. `LookupError`
- C. `BaseException`
- D. `ArithmeticError`

### 58. A query-builder bug calls `parts = ['v2', 'users']; slug = parts.join('/')` instead of `'/'.join(parts)`. Which exception is raised?

- A. `AttributeError`
- B. `ValueError`
- C. `KeyError`
- D. `IndexError`

### 59. Complete `____ len(slug) > 0, 'slug cannot be empty'` so a development sanity check raises `AssertionError` whenever `len(slug) > 0` evaluates to `False`. Which keyword fills the blank?

- A. `with`
- B. `assert`
- C. `raise`
- D. `except`

### 60. Complete `try: parse_url(raw)` / `except ValueError: bad += 1` / `____:` / `    audit_count += 1` so `audit_count += 1` executes whether `parse_url(raw)` succeeds, raises `ValueError`, or raises an uncaught `TypeError`. Which keyword fills the blank?

- A. `else`
- B. `pass`
- C. `finally`
- D. `except`

---

## Answer key and explanations

### Question 1 — B

Answer: CPython parses the entire `.py` file for syntax errors before executing even the first top-level statement. CPython parses and compiles the entire script file to bytecode before executing top-level code, so the `SyntaxError` on line 48 aborts startup before line 1 prints anything. Because CPython compiles a script unit to bytecode before running it, a `SyntaxError` on line 50 prevents line 1 from executing at all. Local study-map skill 1.1 (Interpreter Bytecode Pipeline vs Ahead-of-Time Compilation), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Python has no automatic transaction rollback for console output or completed side effects when a later statement raises an exception. Why the correct answer wins: CPython parses and compiles the entire script file to bytecode before executing top-level code, so the `SyntaxError` on line 48 aborts startup before line 1 prints anything.
- **B:** Correct. Because CPython compiles a script unit to bytecode before running it, a `SyntaxError` on line 50 prevents line 1 from executing at all. In this case: CPython parses and compiles the entire script file to bytecode before executing top-level code, so the `SyntaxError` on line 48 aborts startup before line 1 prints anything.
- **C:** Incorrect for this question. Unlike runtime exceptions (`ZeroDivisionError`, `NameError`), `SyntaxError` happens during the parsing pass before execution begins. Why the correct answer wins: CPython parses and compiles the entire script file to bytecode before executing top-level code, so the `SyntaxError` on line 48 aborts startup before line 1 prints anything.
- **D:** Incorrect for this question. Ahead-of-time native binary linking describes C, C++, or Rust toolchains, whereas standard CPython requires the Python runtime. Why the correct answer wins: CPython parses and compiles the entire script file to bytecode before executing top-level code, so the `SyntaxError` on line 48 aborts startup before line 1 prints anything.

### Question 2 — B

Answer: A syntactic error because valid Python tokens are arranged in a sequence that violates Python grammar rules. Every individual token is lexically valid, so placing two binary operators side by side violates Python's grammar rules — a syntactic error. Syntax governs how valid tokens combine into grammatically well-formed expressions and compound statements. Local study-map skill 1.2 (Lexical, Syntactic, and Semantic Error Classification), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Lexis governs how characters group into valid tokens such as literals, identifiers, operators, and delimiters. Why the correct answer wins: Every individual token is lexically valid, so placing two binary operators side by side violates Python's grammar rules — a syntactic error.
- **B:** Correct. Syntax governs how valid tokens combine into grammatically well-formed expressions and compound statements. In this case: Every individual token is lexically valid, so placing two binary operators side by side violates Python's grammar rules — a syntactic error.
- **C:** Incorrect for this question. PEP-8 naming and spacing conventions are advisory style guidelines and never halt the CPython parser. Why the correct answer wins: Every individual token is lexically valid, so placing two binary operators side by side violates Python's grammar rules — a syntactic error.
- **D:** Incorrect for this question. Semantics governs what a grammatically legal construct means when executed, such as dividing by zero or indexing past a sequence boundary. Why the correct answer wins: Every individual token is lexically valid, so placing two binary operators side by side violates Python's grammar rules — a syntactic error.

### Question 3 — C, E

Answers: Consistent 4-space indentation for each nested suite without mixing tabs and spaces in the same block; Everything after `#` outside a string literal to the end of that physical line is ignored by the parser. Python groups compound suites by indentation (with PEP-8 recommending 4 spaces per level and disallowing mixed tabs/spaces) and ignores `#` comments outside string literals through the end of the line. Python defines compound block structure by indentation level, and PEP-8 specifies 4 spaces per level while Python 3 raises `TabError` on inconsistent tab/space mixing. Python uses `#` for single-line comments; `#` inside quotes stays an ordinary character in the string. Local study-map skill 1.3 (Reserved Keywords, Indentation Rules, and Line Comments), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Python has no `/* ... */` comment syntax and raises `SyntaxError` if those tokens appear as code. Why the correct answer wins: Python groups compound suites by indentation (with PEP-8 recommending 4 spaces per level and disallowing mixed tabs/spaces) and ignores `#` comments outside string literals through the end of the line.
- **B:** Incorrect for this question. In Python, `{ ... }` builds dictionaries or sets rather than delimiting statement suites. Why the correct answer wins: Python groups compound suites by indentation (with PEP-8 recommending 4 spaces per level and disallowing mixed tabs/spaces) and ignores `#` comments outside string literals through the end of the line.
- **C:** Correct. Python uses `#` for single-line comments; `#` inside quotes stays an ordinary character in the string. In this case: Python groups compound suites by indentation (with PEP-8 recommending 4 spaces per level and disallowing mixed tabs/spaces) and ignores `#` comments outside string literals through the end of the line.
- **D:** Incorrect for this question. PEP-8 naming and spacing conventions are advisory style guidelines and never halt the CPython parser. Why the correct answer wins: Python groups compound suites by indentation (with PEP-8 recommending 4 spaces per level and disallowing mixed tabs/spaces) and ignores `#` comments outside string literals through the end of the line.
- **E:** Correct. Python defines compound block structure by indentation level, and PEP-8 specifies 4 spaces per level while Python 3 raises `TabError` on inconsistent tab/space mixing. In this case: Python groups compound suites by indentation (with PEP-8 recommending 4 spaces per level and disallowing mixed tabs/spaces) and ignores `#` comments outside string literals through the end of the line.

### Question 4 — D

Answer: `400.0`. Scientific-notation literals with `e` or `E` always produce a `float` in Python 3, so `4e2` evaluates to `400.0` rather than the integer `400`. Scientific literal `4e2` evaluates to the `float` `400.0`. Local study-map skill 1.4 (Binary, Octal, Hexadecimal, Underscored, and Scientific Literals), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: Scientific-notation literals with `e` or `E` always produce a `float` in Python 3, so `4e2` evaluates to `400.0` rather than the integer `400`.
- **B:** Incorrect for this question. The integer `400` (`int`), whereas exponent literals like `4e2` produce `float` `400.0`. Why the correct answer wins: Scientific-notation literals with `e` or `E` always produce a `float` in Python 3, so `4e2` evaluates to `400.0` rather than the integer `400`.
- **C:** Incorrect for this question. Evaluates to the integer `42`. Why the correct answer wins: Scientific-notation literals with `e` or `E` always produce a `float` in Python 3, so `4e2` evaluates to `400.0` rather than the integer `400`.
- **D:** Correct. Scientific literal `4e2` evaluates to the `float` `400.0`. In this case: Scientific-notation literals with `e` or `E` always produce a `float` in Python 3, so `4e2` evaluates to `400.0` rather than the integer `400`.

### Question 5 — D, E

Answers: `_cached_slug`; `case`. `_cached_slug` starts with an underscore and `case` is only a soft keyword in Python 3.10+, whereas `user@host` and `fx-rate` contain illegal operator characters and `lambda` is a hard keyword. `_cached_slug` begins with an underscore and contains only letters and underscores, making it a valid Python identifier. `case` is a soft keyword in Python 3.10+, so assigning `case = 1` remains legal outside `match` headers. Local study-map skill 1.5 (Identifier Validity and PEP-8 Naming Style), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `lambda` is a hard reserved keyword in Python 3 that creates an anonymous single-expression function. Why the correct answer wins: `_cached_slug` starts with an underscore and `case` is only a soft keyword in Python 3.10+, whereas `user@host` and `fx-rate` contain illegal operator characters and `lambda` is a hard keyword.
- **B:** Incorrect for this question. `@` is the matrix-multiplication / decorator token and cannot appear inside an identifier. Why the correct answer wins: `_cached_slug` starts with an underscore and `case` is only a soft keyword in Python 3.10+, whereas `user@host` and `fx-rate` contain illegal operator characters and `lambda` is a hard keyword.
- **C:** Incorrect for this question. `fx-rate` is parsed as subtraction `fx - rate` because hyphens are illegal in Python identifiers. Why the correct answer wins: `_cached_slug` starts with an underscore and `case` is only a soft keyword in Python 3.10+, whereas `user@host` and `fx-rate` contain illegal operator characters and `lambda` is a hard keyword.
- **D:** Correct. `_cached_slug` begins with an underscore and contains only letters and underscores, making it a valid Python identifier. In this case: `_cached_slug` starts with an underscore and `case` is only a soft keyword in Python 3.10+, whereas `user@host` and `fx-rate` contain illegal operator characters and `lambda` is a hard keyword.
- **E:** Correct. `case` is a soft keyword in Python 3.10+, so assigning `case = 1` remains legal outside `match` headers. In this case: `_cached_slug` starts with an underscore and `case` is only a soft keyword in Python 3.10+, whereas `user@host` and `fx-rate` contain illegal operator characters and `lambda` is a hard keyword.

### Question 6 — D

Answer: `%`. Modulo `%` computes the division remainder (`47 % 10 == 7`), whereas `//` computes the floored quotient `4` and `/` computes `4.7`. Modulo `%` returns the remainder whose sign matches the divisor in Python (`a == (a // b) * b + (a % b)`). Local study-map skill 1.6 (True Division, Floor Division, Modulo, and Power Operators), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Exponentiation `**` raises the left operand to the power of the right operand and binds right-to-left. Why the correct answer wins: Modulo `%` computes the division remainder (`47 % 10 == 7`), whereas `//` computes the floored quotient `4` and `/` computes `4.7`.
- **B:** Incorrect for this question. True division `/` always returns a `float` in Python 3, even when both operands divide evenly (`8 / 2 == 4.0`). Why the correct answer wins: Modulo `%` computes the division remainder (`47 % 10 == 7`), whereas `//` computes the floored quotient `4` and `/` computes `4.7`.
- **C:** Incorrect for this question. Floor division `//` rounds the quotient down toward negative infinity (`math.floor`). Why the correct answer wins: Modulo `%` computes the division remainder (`47 % 10 == 7`), whereas `//` computes the floored quotient `4` and `/` computes `4.7`.
- **D:** Correct. Modulo `%` returns the remainder whose sign matches the divisor in Python (`a == (a // b) * b + (a % b)`). In this case: Modulo `%` computes the division remainder (`47 % 10 == 7`), whereas `//` computes the floored quotient `4` and `/` computes `4.7`.

### Question 7 — B

Answer: `256`. Exponentiation `**` binds from right to left, so Python computes `2 ** 3` (`8`) first and then `2 ** 8`, yielding `256` instead of `(2 ** 2) ** 3 == 64`. Evaluates to the integer `256`. Local study-map skill 1.7 (Operator Precedence Tiers, Unary Operators, and Associativity), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. Evaluates to the integer `16`. Why the correct answer wins: Exponentiation `**` binds from right to left, so Python computes `2 ** 3` (`8`) first and then `2 ** 8`, yielding `256` instead of `(2 ** 2) ** 3 == 64`.
- **B:** Correct. Evaluates to the integer `256`. In this case: Exponentiation `**` binds from right to left, so Python computes `2 ** 3` (`8`) first and then `2 ** 8`, yielding `256` instead of `(2 ** 2) ** 3 == 64`.
- **C:** Incorrect for this question. Evaluates to the integer `64`. Why the correct answer wins: Exponentiation `**` binds from right to left, so Python computes `2 ** 3` (`8`) first and then `2 ** 8`, yielding `256` instead of `(2 ** 2) ** 3 == 64`.
- **D:** Incorrect for this question. Evaluates to the integer `32`. Why the correct answer wins: Exponentiation `**` binds from right to left, so Python computes `2 ** 3` (`8`) first and then `2 ** 8`, yielding `256` instead of `(2 ** 2) ** 3 == 64`.

### Question 8 — A, C

Answers: `&`; `^`. `&` performs bitwise AND and `^` performs bitwise XOR on integers, whereas `**` is exponentiation, `and` is Boolean short-circuit logic, and `//` is floor division. Bitwise AND `&` sets each output bit to `1` only where both integer operands have `1`. Bitwise XOR `^` sets each output bit to `1` where the two integer operands differ (it is NOT exponentiation in Python). Local study-map skill 1.8 (Bitwise Masks, Shifts, Relational Checks, and Short-Circuit Logic), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. Bitwise AND `&` sets each output bit to `1` only where both integer operands have `1`. In this case: `&` performs bitwise AND and `^` performs bitwise XOR on integers, whereas `**` is exponentiation, `and` is Boolean short-circuit logic, and `//` is floor division.
- **B:** Incorrect for this question. Exponentiation `**` raises the left operand to the power of the right operand and binds right-to-left. Why the correct answer wins: `&` performs bitwise AND and `^` performs bitwise XOR on integers, whereas `**` is exponentiation, `and` is Boolean short-circuit logic, and `//` is floor division.
- **C:** Correct. Bitwise XOR `^` sets each output bit to `1` where the two integer operands differ (it is NOT exponentiation in Python). In this case: `&` performs bitwise AND and `^` performs bitwise XOR on integers, whereas `**` is exponentiation, `and` is Boolean short-circuit logic, and `//` is floor division.
- **D:** Incorrect for this question. Floor division `//` rounds the quotient down toward negative infinity (`math.floor`). Why the correct answer wins: `&` performs bitwise AND and `^` performs bitwise XOR on integers, whereas `**` is exponentiation, `and` is Boolean short-circuit logic, and `//` is floor division.
- **E:** Incorrect for this question. `and` is Python's short-circuit logical conjunction operator. Why the correct answer wins: `&` performs bitwise AND and `^` performs bitwise XOR on integers, whereas `**` is exponentiation, `and` is Boolean short-circuit logic, and `//` is floor division.

### Question 9 — A

Answer: `*=`. Sequence repetition with `*=` repeats string `'pad'` four times to bind `'----'`, whereas `+=` raises `TypeError` with an `int`. `*=` scales a number or repeats a sequence in place / by rebinding. Local study-map skill 1.9 (IEEE-754 Float Behaviour, Sequence Operators, and Augmented Assignment), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Correct. `*=` scales a number or repeats a sequence in place / by rebinding. In this case: Sequence repetition with `*=` repeats string `'pad'` four times to bind `'----'`, whereas `+=` raises `TypeError` with an `int`.
- **B:** Incorrect for this question. `+=` performs augmented addition (`x += y`), mutating mutable sequences in place or rebinding immutable targets. Why the correct answer wins: Sequence repetition with `*=` repeats string `'pad'` four times to bind `'----'`, whereas `+=` raises `TypeError` with an `int`.
- **C:** Incorrect for this question. `//=` floor-divides a variable by the right-hand operand and stores the floored quotient back into the variable. Why the correct answer wins: Sequence repetition with `*=` repeats string `'pad'` four times to bind `'----'`, whereas `+=` raises `TypeError` with an `int`.
- **D:** Incorrect for this question. Exponentiation `**` raises the left operand to the power of the right operand and binds right-to-left. Why the correct answer wins: Sequence repetition with `*=` repeats string `'pad'` four times to bind `'----'`, whereas `+=` raises `TypeError` with an `int`.

### Question 10 — C

Answer: `sep='/'`. `sep='/'` joins the three positional string arguments with forward slashes while preserving the default trailing newline. `sep='/'` joins multiple `print()` arguments with a forward slash instead of the default single space. Local study-map skill 1.10 (Formatted Console Output with print(), sep=, and end=), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `end=', '` replaces the trailing newline of `print()` with a comma and space so the next `print()` continues on the same line. Why the correct answer wins: `sep='/'` joins the three positional string arguments with forward slashes while preserving the default trailing newline.
- **B:** Incorrect for this question. `end='!'` finishes the printed line with `!` instead of `'\n'`. Why the correct answer wins: `sep='/'` joins the three positional string arguments with forward slashes while preserving the default trailing newline.
- **C:** Correct. `sep='/'` joins multiple `print()` arguments with a forward slash instead of the default single space. In this case: `sep='/'` joins the three positional string arguments with forward slashes while preserving the default trailing newline.
- **D:** Incorrect for this question. `sep=':'` places a colon between consecutive positional arguments passed to `print()`. Why the correct answer wins: `sep='/'` joins the three positional string arguments with forward slashes while preserving the default trailing newline.

### Question 11 — D

Answer: `str`. Python does not implicitly concatenate `str` and `int`; `str(408)` converts the integer to `'408'` so `+` concatenates two strings cleanly. `str(...)` converts an arbitrary object such as an `int` or `float` into its printable text form so it can concatenate with strings. Local study-map skill 1.11 (Reading Strings with input() and Explicit Type Conversions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 1 (Computer Programming and Python Fundamentals, 18 percent): https://pythoninstitute.org/pcep-exam-syllabus#block1 — and Python 3 documentation, Built-in Types and Functions: https://docs.python.org/3/library/stdtypes.html.

- **A:** Incorrect for this question. `int(...)` converts a base-10 digit string or truncates a float toward zero into an integer. Why the correct answer wins: Python does not implicitly concatenate `str` and `int`; `str(408)` converts the integer to `'408'` so `+` concatenates two strings cleanly.
- **B:** Incorrect for this question. `bool(...)` tests truthiness; for ANY non-empty string — including `'0'` and `'False'` — `bool(...)` returns `True`. Why the correct answer wins: Python does not implicitly concatenate `str` and `int`; `str(408)` converts the integer to `'408'` so `+` concatenates two strings cleanly.
- **C:** Incorrect for this question. `float(...)` parses a numeric string such as `'19.95'` into a floating-point number. Why the correct answer wins: Python does not implicitly concatenate `str` and `int`; `str(408)` converts the integer to `'408'` so `+` concatenates two strings cleanly.
- **D:** Correct. `str(...)` converts an arbitrary object such as an `int` or `float` into its printable text form so it can concatenate with strings. In this case: Python does not implicitly concatenate `str` and `int`; `str(408)` converts the integer to `'408'` so `+` concatenates two strings cleanly.

### Question 12 — A

Answer: `else`. `else` takes no condition expression and executes whenever the initial `if` and every `elif` evaluated to `False`. `else` is a hard reserved keyword in Python 3 used on conditionals, loops, and `try` blocks. Local study-map skill 2.1 (Exclusive Multi-Way Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `else` is a hard reserved keyword in Python 3 used on conditionals, loops, and `try` blocks. In this case: `else` takes no condition expression and executes whenever the initial `if` and every `elif` evaluated to `False`.
- **B:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `else` takes no condition expression and executes whenever the initial `if` and every `elif` evaluated to `False`.
- **C:** Incorrect for this question. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Why the correct answer wins: `else` takes no condition expression and executes whenever the initial `if` and every `elif` evaluated to `False`.
- **D:** Incorrect for this question. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. Why the correct answer wins: `else` takes no condition expression and executes whenever the initial `if` and every `elif` evaluated to `False`.

### Question 13 — A

Answer: `OK`. `port < 0` is `False`, the first matching condition `port < 1024` prints `OK`, and Python skips `elif port < 49152` even though `443 < 49152` is also true. Local study-map skill 2.1 (Exclusive Multi-Way Branching with if, elif, and else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. In this case: `port < 0` is `False`, the first matching condition `port < 1024` prints `OK`, and Python skips `elif port < 49152` even though `443 < 49152` is also true.
- **B:** Incorrect for this question. Prints `ALERT`. Why the correct answer wins: `port < 0` is `False`, the first matching condition `port < 1024` prints `OK`, and Python skips `elif port < 49152` even though `443 < 49152` is also true.
- **C:** Incorrect for this question. Prints `CRIT`. Why the correct answer wins: `port < 0` is `False`, the first matching condition `port < 1024` prints `OK`, and Python skips `elif port < 49152` even though `443 < 49152` is also true.
- **D:** Incorrect for this question. Prints `WARN`. Why the correct answer wins: `port < 0` is `False`, the first matching condition `port < 1024` prints `OK`, and Python skips `elif port < 49152` even though `443 < 49152` is also true.

### Question 14 — B

Answer: `0`. Because `subtotal >= 50` (`75 >= 50`) is `True`, Python's conditional expression evaluates and returns the left branch `0` without evaluating the `else` branch. Evaluates to the integer `0`. Local study-map skill 2.2 (Independent if Chains vs Conditional Expressions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to Boolean `True`. Why the correct answer wins: Because `subtotal >= 50` (`75 >= 50`) is `True`, Python's conditional expression evaluates and returns the left branch `0` without evaluating the `else` branch.
- **B:** Correct. Evaluates to the integer `0`. In this case: Because `subtotal >= 50` (`75 >= 50`) is `True`, Python's conditional expression evaluates and returns the left branch `0` without evaluating the `else` branch.
- **C:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: Because `subtotal >= 50` (`75 >= 50`) is `True`, Python's conditional expression evaluates and returns the left branch `0` without evaluating the `else` branch.
- **D:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: Because `subtotal >= 50` (`75 >= 50`) is `True`, Python's conditional expression evaluates and returns the left branch `0` without evaluating the `else` branch.

### Question 15 — D

Answer: `WARN`. Because the second statement is an independent `if` rather than `elif`, both suites run in order and the second assignment overwrites `tag` with `'WARN'`. Prints `WARN`. Local study-map skill 2.2 (Independent if Chains vs Conditional Expressions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints both `GOLD` and `SILVER` when two independent `if` statements both match. Why the correct answer wins: Because the second statement is an independent `if` rather than `elif`, both suites run in order and the second assignment overwrites `tag` with `'WARN'`.
- **B:** Incorrect for this question. Prints `OK`. Why the correct answer wins: Because the second statement is an independent `if` rather than `elif`, both suites run in order and the second assignment overwrites `tag` with `'WARN'`.
- **C:** Incorrect for this question. Prints `ALERT`. Why the correct answer wins: Because the second statement is an independent `if` rather than `elif`, both suites run in order and the second assignment overwrites `tag` with `'WARN'`.
- **D:** Correct. Prints `WARN`. In this case: Because the second statement is an independent `if` rather than `elif`, both suites run in order and the second assignment overwrites `tag` with `'WARN'`.

### Question 16 — A, E

Answers: `'False'`; `['']`. `'False'` has five characters and `['']` is a 1-element list, so both have non-zero length and evaluate to `True`, whereas `''`, `()`, and `None` are falsy. `'False'` is a 5-character non-empty string, so `bool('False')` evaluates to `True`. `['']` is a 1-element list containing an empty string, so the list itself has length `1` and is truthy. Local study-map skill 2.3 (Truthiness of Built-In Containers, Numbers, Strings, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `'False'` is a 5-character non-empty string, so `bool('False')` evaluates to `True`. In this case: `'False'` has five characters and `['']` is a 1-element list, so both have non-zero length and evaluate to `True`, whereas `''`, `()`, and `None` are falsy.
- **B:** Incorrect for this question. An empty tuple `()` has length `0` and evaluates to `False` in a Boolean context. Why the correct answer wins: `'False'` has five characters and `['']` is a 1-element list, so both have non-zero length and evaluate to `True`, whereas `''`, `()`, and `None` are falsy.
- **C:** Incorrect for this question. `None` always evaluates to `False` in a Boolean context. Why the correct answer wins: `'False'` has five characters and `['']` is a 1-element list, so both have non-zero length and evaluate to `True`, whereas `''`, `()`, and `None` are falsy.
- **D:** Incorrect for this question. An empty string `''` has length `0` and evaluates to `False` in a Boolean context. Why the correct answer wins: `'False'` has five characters and `['']` is a 1-element list, so both have non-zero length and evaluate to `True`, whereas `''`, `()`, and `None` are falsy.
- **E:** Correct. `['']` is a 1-element list containing an empty string, so the list itself has length `1` and is truthy. In this case: `'False'` has five characters and `['']` is a 1-element list, so both have non-zero length and evaluate to `True`, whereas `''`, `()`, and `None` are falsy.

### Question 17 — B

Answer: `True`. For `str` objects, `bool(s)` is `False` only when `s == ''`; `'0'` has length `1`, so `bool('0')` evaluates to `True`. Evaluates to Boolean `True`. Local study-map skill 2.3 (Truthiness of Built-In Containers, Numbers, Strings, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to Boolean `False`. Why the correct answer wins: For `str` objects, `bool(s)` is `False` only when `s == ''`; `'0'` has length `1`, so `bool('0')` evaluates to `True`.
- **B:** Correct. Evaluates to Boolean `True`. In this case: For `str` objects, `bool(s)` is `False` only when `s == ''`; `'0'` has length `1`, so `bool('0')` evaluates to `True`.
- **C:** Incorrect for this question. Evaluates to the integer `0`. Why the correct answer wins: For `str` objects, `bool(s)` is `False` only when `s == ''`; `'0'` has length `1`, so `bool('0')` evaluates to `True`.
- **D:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: For `str` objects, `bool(s)` is `False` only when `s == ''`; `'0'` has length `1`, so `bool('0')` evaluates to `True`.

### Question 18 — D, E

Answers: `1024 <= port <= 65535`; `port >= 1024 and port <= 65535`. Both `1024 <= port <= 65535` and `port >= 1024 and port <= 65535` enforce both bounds; `or` matches every integer, `&` binds tighter than comparisons, and `&&` is invalid syntax. Chained comparison `1024 <= port <= 65535` evaluates `port` once and requires both `1024 <= port` and `port <= 65535` to hold. Combining both relational checks with `and` returns `True` exclusively when `port` lies inside `[1024, 65535]`. Local study-map skill 2.4 (Logical Precedence (not, and, or) and Chained Comparisons), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `&&` is not a valid operator in Python and raises `SyntaxError`; Python uses the keyword `and`. Why the correct answer wins: Both `1024 <= port <= 65535` and `port >= 1024 and port <= 65535` enforce both bounds; `or` matches every integer, `&` binds tighter than comparisons, and `&&` is invalid syntax.
- **B:** Incorrect for this question. Because `&` binds tighter than `>=` and `<=`, Python parses `port >= (1024 & port) <= 65535`, which does NOT test the port range. Why the correct answer wins: Both `1024 <= port <= 65535` and `port >= 1024 and port <= 65535` enforce both bounds; `or` matches every integer, `&` binds tighter than comparisons, and `&&` is invalid syntax.
- **C:** Incorrect for this question. Using `or` here evaluates to `True` for EVERY integer because every number is either `>= 1024` or `<= 65535`. Why the correct answer wins: Both `1024 <= port <= 65535` and `port >= 1024 and port <= 65535` enforce both bounds; `or` matches every integer, `&` binds tighter than comparisons, and `&&` is invalid syntax.
- **D:** Correct. Chained comparison `1024 <= port <= 65535` evaluates `port` once and requires both `1024 <= port` and `port <= 65535` to hold. In this case: Both `1024 <= port <= 65535` and `port >= 1024 and port <= 65535` enforce both bounds; `or` matches every integer, `&` binds tighter than comparisons, and `&&` is invalid syntax.
- **E:** Correct. Combining both relational checks with `and` returns `True` exclusively when `port` lies inside `[1024, 65535]`. In this case: Both `1024 <= port <= 65535` and `port >= 1024 and port <= 65535` enforce both bounds; `or` matches every integer, `&` binds tighter than comparisons, and `&&` is invalid syntax.

### Question 19 — B

Answer: `not`. `not` inverts the truthiness of `username.strip()`, returning `True` when the stripped string is `''`. `not` is Python's unary logical negation operator and returns `True` or `False`. Local study-map skill 2.4 (Logical Precedence (not, and, or) and Chained Comparisons), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `and` is Python's short-circuit logical conjunction operator. Why the correct answer wins: `not` inverts the truthiness of `username.strip()`, returning `True` when the stripped string is `''`.
- **B:** Correct. `not` is Python's unary logical negation operator and returns `True` or `False`. In this case: `not` inverts the truthiness of `username.strip()`, returning `True` when the stripped string is `''`.
- **C:** Incorrect for this question. `in` is a hard reserved keyword in Python 3 used for membership tests and `for` headers. Why the correct answer wins: `not` inverts the truthiness of `username.strip()`, returning `True` when the stripped string is `''`.
- **D:** Incorrect for this question. `or` is Python's short-circuit logical disjunction operator. Why the correct answer wins: `not` inverts the truthiness of `username.strip()`, returning `True` when the stripped string is `''`.

### Question 20 — D

Answer: `while`. `while` repeats `path = path[1:]` as long as `path.startswith('/')` evaluates to `True`. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. Local study-map skill 2.5 (State-Driven Iteration and Termination with while), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Why the correct answer wins: `while` repeats `path = path[1:]` as long as `path.startswith('/')` evaluates to `True`.
- **B:** Incorrect for this question. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Why the correct answer wins: `while` repeats `path = path[1:]` as long as `path.startswith('/')` evaluates to `True`.
- **C:** Incorrect for this question. `for` is a hard reserved keyword in Python 3 that iterates over items produced by an iterable. Why the correct answer wins: `while` repeats `path = path[1:]` as long as `path.startswith('/')` evaluates to `True`.
- **D:** Correct. `while` is a hard reserved keyword in Python 3 that repeats a suite while its condition stays truthy. In this case: `while` repeats `path = path[1:]` as long as `path.startswith('/')` evaluates to `True`.

### Question 21 — A, E

Answers: `n = 6` followed by `while n > 0: n -= 2`; `n = 16` followed by `while n >= 2: n //= 2`. `n = 6` with `n -= 2` reaches `0` in three steps and `n = 16` with `n //= 2` reaches `1` in four steps, whereas the other three loops never make their conditions falsy. Starting at `6` and subtracting `2` visits `6, 4, 2, 0` and terminates after three iterations. Halving `16` via integer floor division visits `16, 8, 4, 2, 1` and terminates after four iterations. Local study-map skill 2.5 (State-Driven Iteration and Termination with while), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Starting at `6` and subtracting `2` visits `6, 4, 2, 0` and terminates after three iterations. In this case: `n = 6` with `n -= 2` reaches `0` in three steps and `n = 16` with `n //= 2` reaches `1` in four steps, whereas the other three loops never make their conditions falsy.
- **B:** Incorrect for this question. Because `pass` never updates `n`, `n > 0` remains `True` indefinitely. Why the correct answer wins: `n = 6` with `n -= 2` reaches `0` in three steps and `n = 16` with `n //= 2` reaches `1` in four steps, whereas the other three loops never make their conditions falsy.
- **C:** Incorrect for this question. Incrementing a positive integer keeps `n > 0` forever, producing an infinite loop. Why the correct answer wins: `n = 6` with `n -= 2` reaches `0` in three steps and `n = 16` with `n //= 2` reaches `1` in four steps, whereas the other three loops never make their conditions falsy.
- **D:** Incorrect for this question. Adding `2` to an even integer keeps `n` even on every step, so `n % 2 == 0` never turns `False`. Why the correct answer wins: `n = 6` with `n -= 2` reaches `0` in three steps and `n = 16` with `n //= 2` reaches `1` in four steps, whereas the other three loops never make their conditions falsy.
- **E:** Correct. Halving `16` via integer floor division visits `16, 8, 4, 2, 1` and terminates after four iterations. In this case: `n = 6` with `n -= 2` reaches `0` in three steps and `n = 16` with `n //= 2` reaches `1` in four steps, whereas the other three loops never make their conditions falsy.

### Question 22 — A, D

Answers: `range(3, 12, 3)`; `range(9, 0, -3)`. `range(3, 12, 3)` generates `3, 6, 9` and `range(9, 0, -3)` generates `9, 6, 3`, whereas `range(3, 9, 3)` yields two items, `range(8, 2)` yields zero, and `range(2, 10, 2)` yields four. `range(3, 12, 3)` generates `3, 6, 9` (three integers). `range(9, 0, -3)` generates `9, 6, 3` (three integers). Local study-map skill 2.6 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. `range(3, 12, 3)` generates `3, 6, 9` (three integers). In this case: `range(3, 12, 3)` generates `3, 6, 9` and `range(9, 0, -3)` generates `9, 6, 3`, whereas `range(3, 9, 3)` yields two items, `range(8, 2)` yields zero, and `range(2, 10, 2)` yields four.
- **B:** Incorrect for this question. `range(8, 2)` uses default step `+1` with `start > stop`, yielding zero items. Why the correct answer wins: `range(3, 12, 3)` generates `3, 6, 9` and `range(9, 0, -3)` generates `9, 6, 3`, whereas `range(3, 9, 3)` yields two items, `range(8, 2)` yields zero, and `range(2, 10, 2)` yields four.
- **C:** Incorrect for this question. `range(2, 10, 2)` generates `2, 4, 6, 8` (four integers). Why the correct answer wins: `range(3, 12, 3)` generates `3, 6, 9` and `range(9, 0, -3)` generates `9, 6, 3`, whereas `range(3, 9, 3)` yields two items, `range(8, 2)` yields zero, and `range(2, 10, 2)` yields four.
- **D:** Correct. `range(9, 0, -3)` generates `9, 6, 3` (three integers). In this case: `range(3, 12, 3)` generates `3, 6, 9` and `range(9, 0, -3)` generates `9, 6, 3`, whereas `range(3, 9, 3)` yields two items, `range(8, 2)` yields zero, and `range(2, 10, 2)` yields four.
- **E:** Incorrect for this question. `range(3, 9, 3)` stops before `9`, yielding only `3, 6` (two integers). Why the correct answer wins: `range(3, 12, 3)` generates `3, 6, 9` and `range(9, 0, -3)` generates `9, 6, 3`, whereas `range(3, 9, 3)` yields two items, `range(8, 2)` yields zero, and `range(2, 10, 2)` yields four.

### Question 23 — A

Answer: `[]`. When `start >= stop` with positive step `+1`, `range(8, 2)` contains zero elements, so `list(range(8, 2))` prints `[]`. The empty list `[]`. Local study-map skill 2.6 (Definite Iteration with for and range(start, stop, step)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. The empty list `[]`. In this case: When `start >= stop` with positive step `+1`, `range(8, 2)` contains zero elements, so `list(range(8, 2))` prints `[]`.
- **B:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: When `start >= stop` with positive step `+1`, `range(8, 2)` contains zero elements, so `list(range(8, 2))` prints `[]`.
- **C:** Incorrect for this question. Reversing `[10, 20, 30, 40]` with `[::-1]` returns `[40, 30, 20, 10]`. Why the correct answer wins: When `start >= stop` with positive step `+1`, `range(8, 2)` contains zero elements, so `list(range(8, 2))` prints `[]`.
- **D:** Incorrect for this question. Evaluates to the integer `0`. Why the correct answer wins: When `start >= stop` with positive step `+1`, `range(8, 2)` contains zero elements, so `list(range(8, 2))` prints `[]`.

### Question 24 — A

Answer: `3`. Iterating character by character over `'/api/v2/ok'` visits `'/'` three times, incrementing `slashes` to `3`. Evaluates to the integer `3`. Local study-map skill 2.7 (Direct Sequence and Character Iteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Correct. Evaluates to the integer `3`. In this case: Iterating character by character over `'/api/v2/ok'` visits `'/'` three times, incrementing `slashes` to `3`.
- **B:** Incorrect for this question. Evaluates to the integer `1`. Why the correct answer wins: Iterating character by character over `'/api/v2/ok'` visits `'/'` three times, incrementing `slashes` to `3`.
- **C:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: Iterating character by character over `'/api/v2/ok'` visits `'/'` three times, incrementing `slashes` to `3`.
- **D:** Incorrect for this question. Evaluates to the integer `9`. Why the correct answer wins: Iterating character by character over `'/api/v2/ok'` visits `'/'` three times, incrementing `slashes` to `3`.

### Question 25 — C

Answer: `break`. `break` terminates the enclosing `for` loop immediately upon finding the first space character. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. Local study-map skill 2.8 (Loop Interruption and Stubs with break, continue, and pass), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `break` terminates the enclosing `for` loop immediately upon finding the first space character.
- **B:** Incorrect for this question. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. Why the correct answer wins: `break` terminates the enclosing `for` loop immediately upon finding the first space character.
- **C:** Correct. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. In this case: `break` terminates the enclosing `for` loop immediately upon finding the first space character.
- **D:** Incorrect for this question. `else` is a hard reserved keyword in Python 3 used on conditionals, loops, and `try` blocks. Why the correct answer wins: `break` terminates the enclosing `for` loop immediately upon finding the first space character.

### Question 26 — D

Answer: `continue`. `continue` jumps straight to the next element of `raw_lines` without executing `cleaned.append(line)`. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. Local study-map skill 2.8 (Loop Interruption and Stubs with break, continue, and pass), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: `continue` jumps straight to the next element of `raw_lines` without executing `cleaned.append(line)`.
- **B:** Incorrect for this question. `break` is a hard reserved keyword in Python 3 that exits the innermost enclosing `for` or `while` loop. Why the correct answer wins: `continue` jumps straight to the next element of `raw_lines` without executing `cleaned.append(line)`.
- **C:** Incorrect for this question. `return` is a hard reserved keyword in Python 3 that exits a function and hands back a value. Why the correct answer wins: `continue` jumps straight to the next element of `raw_lines` without executing `cleaned.append(line)`.
- **D:** Correct. `continue` is a hard reserved keyword in Python 3 that skips the rest of the current loop iteration. In this case: `continue` jumps straight to the next element of `raw_lines` without executing `cleaned.append(line)`.

### Question 27 — C

Answer: `CLEAN`. Because `'@'` never occurs in `'api_v2'`, `break` never runs; when the `for` loop finishes normally, its `else:` suite executes and prints `CLEAN`. Prints `CLEAN` from the loop `else` suite. Local study-map skill 2.9 (Loop Completion Semantics with for-else and while-else), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Prints nothing to standard output. Why the correct answer wins: Because `'@'` never occurs in `'api_v2'`, `break` never runs; when the `for` loop finishes normally, its `else:` suite executes and prints `CLEAN`.
- **B:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: Because `'@'` never occurs in `'api_v2'`, `break` never runs; when the `for` loop finishes normally, its `else:` suite executes and prints `CLEAN`.
- **C:** Correct. Prints `CLEAN` from the loop `else` suite. In this case: Because `'@'` never occurs in `'api_v2'`, `break` never runs; when the `for` loop finishes normally, its `else:` suite executes and prints `CLEAN`.
- **D:** Incorrect for this question. Prints `HALT` before `break` skips the loop `else` suite. Why the correct answer wins: Because `'@'` never occurs in `'api_v2'`, `break` never runs; when the `for` loop finishes normally, its `else:` suite executes and prints `CLEAN`.

### Question 28 — D

Answer: `6`. For each of the `2` versions, the inner loop runs `3` times, incrementing `routes` `2 * 3 == 6` times. Evaluates to the integer `6`. Local study-map skill 2.10 (Nested Loops Over Grids, Pairs, and Sublists), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 2 (Control Flow - Conditional Blocks and Loops, 29 percent): https://pythoninstitute.org/pcep-exam-syllabus#block2 — and Python 3 tutorial, More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html.

- **A:** Incorrect for this question. Evaluates to the integer `8`. Why the correct answer wins: For each of the `2` versions, the inner loop runs `3` times, incrementing `routes` `2 * 3 == 6` times.
- **B:** Incorrect for this question. Evaluates to the integer `2`. Why the correct answer wins: For each of the `2` versions, the inner loop runs `3` times, incrementing `routes` `2 * 3 == 6` times.
- **C:** Incorrect for this question. Evaluates to the integer `5`. Why the correct answer wins: For each of the `2` versions, the inner loop runs `3` times, incrementing `routes` `2 * 3 == 6` times.
- **D:** Correct. Evaluates to the integer `6`. In this case: For each of the `2` versions, the inner loop runs `3` times, incrementing `routes` `2 * 3 == 6` times.

### Question 29 — D

Answer: `[40, 30, 20, 10]`. Slice `[::-1]` steps backward from the end to the beginning by `-1`, returning the reversed copy `[40, 30, 20, 10]`. Reversing `[10, 20, 30, 40]` with `[::-1]` returns `[40, 30, 20, 10]`. Local study-map skill 3.1 (List Indexing, Negative Offsets, and Stride Slicing), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Slice `[::-1]` steps backward from the end to the beginning by `-1`, returning the reversed copy `[40, 30, 20, 10]`.
- **B:** Incorrect for this question. Slice `[1:3]` returns elements at indices `1` and `2`: `[20, 30]`. Why the correct answer wins: Slice `[::-1]` steps backward from the end to the beginning by `-1`, returning the reversed copy `[40, 30, 20, 10]`.
- **C:** Incorrect for this question. Slice `[-2:]` returns the last two items `[40, 50]`. Why the correct answer wins: Slice `[::-1]` steps backward from the end to the beginning by `-1`, returning the reversed copy `[40, 30, 20, 10]`.
- **D:** Correct. Reversing `[10, 20, 30, 40]` with `[::-1]` returns `[40, 30, 20, 10]`. In this case: Slice `[::-1]` steps backward from the end to the beginning by `-1`, returning the reversed copy `[40, 30, 20, 10]`.

### Question 30 — C

Answer: `[30, 40]`. Unlike single-element indexing, slice stop bounds past `len(steps)` clamp silently to the end of the list and return `[30, 40]`. Slicing past `len(seq)` such as `seq[2:99]` clamps safely without raising `IndexError`. Local study-map skill 3.1 (List Indexing, Negative Offsets, and Stride Slicing), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Reversing `[10, 20, 30, 40]` with `[::-1]` returns `[40, 30, 20, 10]`. Why the correct answer wins: Unlike single-element indexing, slice stop bounds past `len(steps)` clamp silently to the end of the list and return `[30, 40]`.
- **B:** Incorrect for this question. The empty list `[]`. Why the correct answer wins: Unlike single-element indexing, slice stop bounds past `len(steps)` clamp silently to the end of the list and return `[30, 40]`.
- **C:** Correct. Slicing past `len(seq)` such as `seq[2:99]` clamps safely without raising `IndexError`. In this case: Unlike single-element indexing, slice stop bounds past `len(steps)` clamp silently to the end of the list and return `[30, 40]`.
- **D:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Unlike single-element indexing, slice stop bounds past `len(steps)` clamp silently to the end of the list and return `[30, 40]`.

### Question 31 — C

Answer: `insert`. `parts.insert(0, 'api')` shifts existing items right and places `'api'` at index `0` in place. `.insert(index, item)` places `item` before `index` in the list. Local study-map skill 3.2 (In-Place List Mutators (append, extend, insert, remove, pop, sort)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `.remove(value)` removes the first matching `value` by equality. Why the correct answer wins: `parts.insert(0, 'api')` shifts existing items right and places `'api'` at index `0` in place.
- **B:** Incorrect for this question. `.append(item)` adds `item` as a single element at the end of a list. Why the correct answer wins: `parts.insert(0, 'api')` shifts existing items right and places `'api'` at index `0` in place.
- **C:** Correct. `.insert(index, item)` places `item` before `index` in the list. In this case: `parts.insert(0, 'api')` shifts existing items right and places `'api'` at index `0` in place.
- **D:** Incorrect for this question. `.extend(iterable)` appends each element yielded by `iterable` to the list. Why the correct answer wins: `parts.insert(0, 'api')` shifts existing items right and places `'api'` at index `0` in place.

### Question 32 — C, D

Answers: `items.append(x)`; `items.extend(seq)`. `items.append(x)` and `items.extend(seq)` both modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` leave `items` untouched and return new lists. `.append(x)` mutates `items` in place by adding `x` at the end and returns `None`. `.extend(seq)` mutates `items` in place by appending every element of `seq` and returns `None`. Local study-map skill 3.2 (In-Place List Mutators (append, extend, insert, remove, pop, sort)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `sorted(items)` builds and returns a brand-new sorted `list`, leaving `items` unchanged. Why the correct answer wins: `items.append(x)` and `items.extend(seq)` both modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` leave `items` untouched and return new lists.
- **B:** Incorrect for this question. `items[:]` creates a shallow copy as a new outer list object. Why the correct answer wins: `items.append(x)` and `items.extend(seq)` both modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` leave `items` untouched and return new lists.
- **C:** Correct. `.append(x)` mutates `items` in place by adding `x` at the end and returns `None`. In this case: `items.append(x)` and `items.extend(seq)` both modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` leave `items` untouched and return new lists.
- **D:** Correct. `.extend(seq)` mutates `items` in place by appending every element of `seq` and returns `None`. In this case: `items.append(x)` and `items.extend(seq)` both modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` leave `items` untouched and return new lists.
- **E:** Incorrect for this question. `items + [x]` allocates and returns a new concatenated list without mutating `items`. Why the correct answer wins: `items.append(x)` and `items.extend(seq)` both modify `items` directly in place, whereas `sorted(items)`, `items + [x]`, and `items[:]` leave `items` untouched and return new lists.

### Question 33 — B

Answer: `sorted`. Built-in `sorted(params)` returns a new sorted list without mutating `params`, whereas `params.sort()` mutates `params` in place and returns `None`. Built-in `sorted(iterable)` returns a new sorted list without mutating its input. Local study-map skill 3.3 (Slice Deletion with del vs Non-Mutating sorted() and len()), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `.pop([index])` removes and returns the element at `index` (default `-1`). Why the correct answer wins: Built-in `sorted(params)` returns a new sorted list without mutating `params`, whereas `params.sort()` mutates `params` in place and returns `None`.
- **B:** Correct. Built-in `sorted(iterable)` returns a new sorted list without mutating its input. In this case: Built-in `sorted(params)` returns a new sorted list without mutating `params`, whereas `params.sort()` mutates `params` in place and returns `None`.
- **C:** Incorrect for this question. `.remove(value)` removes the first matching `value` by equality. Why the correct answer wins: Built-in `sorted(params)` returns a new sorted list without mutating `params`, whereas `params.sort()` mutates `params` in place and returns `None`.
- **D:** Incorrect for this question. `.insert(index, item)` places `item` before `index` in the list. Why the correct answer wins: Built-in `sorted(params)` returns a new sorted list without mutating `params`, whereas `params.sort()` mutates `params` in place and returns `None`.

### Question 34 — B, E

Answers: `items.copy()`; `list(items)`. `items.copy()` and `list(items)` each allocate a new outer `list` containing the same element references, whereas `backup = items` aliases the original list. `items.copy()` creates a shallow copy of the outer list so top-level appends do not affect the original. `list(items)` constructs a new outer list containing the same element references (a shallow copy). Local study-map skill 3.4 (List Aliasing, Shallow Copying, and Shared Inner Rows), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. Plain assignment `backup = items` binds a second name to the exact same list object (an alias, not a copy). Why the correct answer wins: `items.copy()` and `list(items)` each allocate a new outer `list` containing the same element references, whereas `backup = items` aliases the original list.
- **B:** Correct. `list(items)` constructs a new outer list containing the same element references (a shallow copy). In this case: `items.copy()` and `list(items)` each allocate a new outer `list` containing the same element references, whereas `backup = items` aliases the original list.
- **C:** Incorrect for this question. `items.sort()` sorts the list in place and returns `None` rather than a new list. Why the correct answer wins: `items.copy()` and `list(items)` each allocate a new outer `list` containing the same element references, whereas `backup = items` aliases the original list.
- **D:** Incorrect for this question. `items.remove(x)` deletes the first element equal to `x` in place and raises `ValueError` if absent. Why the correct answer wins: `items.copy()` and `list(items)` each allocate a new outer `list` containing the same element references, whereas `backup = items` aliases the original list.
- **E:** Correct. `items.copy()` creates a shallow copy of the outer list so top-level appends do not affect the original. In this case: `items.copy()` and `list(items)` each allocate a new outer `list` containing the same element references, whereas `backup = items` aliases the original list.

### Question 35 — A

Answer: `[n * 2 for n in nums if n > 0]`. A filtering `if n > 0` without `else` belongs after `for n in nums`, making `[n * 2 for n in nums if n > 0]` valid. In a filtering list comprehension, `if <cond>` comes AFTER the `for` clause. Local study-map skill 3.5 (List Comprehensions with Transforms and Conditional Filters), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. In a filtering list comprehension, `if <cond>` comes AFTER the `for` clause. In this case: A filtering `if n > 0` without `else` belongs after `for n in nums`, making `[n * 2 for n in nums if n > 0]` valid.
- **B:** Incorrect for this question. Putting `if n > 0` before `for` without an `else` branch raises `SyntaxError`. Why the correct answer wins: A filtering `if n > 0` without `else` belongs after `for n in nums`, making `[n * 2 for n in nums if n > 0]` valid.
- **C:** Incorrect for this question. A conditional expression (unlike a list comprehension filter) requires an `else` clause or raises `SyntaxError`. Why the correct answer wins: A filtering `if n > 0` without `else` belongs after `for n in nums`, making `[n * 2 for n in nums if n > 0]` valid.
- **D:** Incorrect for this question. C/JavaScript `? :` ternary syntax raises `SyntaxError` in Python. Why the correct answer wins: A filtering `if n > 0` without `else` belongs after `for n in nums`, making `[n * 2 for n in nums if n > 0]` valid.

### Question 36 — C

Answer: `not in`. `not in` tests substring non-membership on strings and returns `True` when `'@'` is absent from `email_addr`. `not in` tests non-membership and evaluates to `True` when the left operand is absent from the container. Local study-map skill 3.6 (Membership Operators in and not in Across Sequences and Dicts), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `from` is a hard reserved keyword in Python 3 used in selective imports and `yield from` / `raise ... from`. Why the correct answer wins: `not in` tests substring non-membership on strings and returns `True` when `'@'` is absent from `email_addr`.
- **B:** Incorrect for this question. `is` tests object identity (`id(a) == id(b)`) rather than value equality (`==`) or container membership (`in`). Why the correct answer wins: `not in` tests substring non-membership on strings and returns `True` when `'@'` is absent from `email_addr`.
- **C:** Correct. `not in` tests non-membership and evaluates to `True` when the left operand is absent from the container. In this case: `not in` tests substring non-membership on strings and returns `True` when `'@'` is absent from `email_addr`.
- **D:** Incorrect for this question. `elif` is a hard reserved keyword in Python 3 that introduces an exclusive secondary branch. Why the correct answer wins: `not in` tests substring non-membership on strings and returns `True` when `'@'` is absent from `email_addr`.

### Question 37 — C

Answer: `TypeError`. Tuples are immutable sequences, so attempting to assign to `route[0]` raises `TypeError`. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Local study-map skill 3.7 (Tuple Packing, Single-Element Commas, Unpacking, and Immutability), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Tuples are immutable sequences, so attempting to assign to `route[0]` raises `TypeError`.
- **B:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Tuples are immutable sequences, so attempting to assign to `route[0]` raises `TypeError`.
- **C:** Correct. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. In this case: Tuples are immutable sequences, so attempting to assign to `route[0]` raises `TypeError`.
- **D:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Tuples are immutable sequences, so attempting to assign to `route[0]` raises `TypeError`.

### Question 38 — B, C

Answers: A tuple of immutable values (`(10, 20)`) can be used as a `dict` key, whereas a `list` (`[10, 20]`) raises `TypeError`; A tuple containing a `list` (`(10, [20])`) cannot be used as a `dict` key and raises `TypeError`. A tuple of immutable objects like `(10, 20)` is hashable and valid as a `dict` key, whereas a list `[10, 20]` or a tuple containing an inner list `(10, [20])` is unhashable and raises `TypeError`. Tuples containing only hashable objects are hashable, whereas lists are mutable and unhashable. A tuple is hashable only when every element inside it is also hashable. Local study-map skill 3.8 (Nested Mutability — Lists Inside Tuples and Tuples Inside Lists), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `x in d` never searches values; a value present only on the right side of `:` returns `False` for `x in d`. Why the correct answer wins: A tuple of immutable objects like `(10, 20)` is hashable and valid as a `dict` key, whereas a list `[10, 20]` or a tuple containing an inner list `(10, [20])` is unhashable and raises `TypeError`.
- **B:** Correct. A tuple is hashable only when every element inside it is also hashable. In this case: A tuple of immutable objects like `(10, 20)` is hashable and valid as a `dict` key, whereas a list `[10, 20]` or a tuple containing an inner list `(10, [20])` is unhashable and raises `TypeError`.
- **C:** Correct. Tuples containing only hashable objects are hashable, whereas lists are mutable and unhashable. In this case: A tuple of immutable objects like `(10, 20)` is hashable and valid as a `dict` key, whereas a list `[10, 20]` or a tuple containing an inner list `(10, [20])` is unhashable and raises `TypeError`.
- **D:** Incorrect for this question. In Python, `{ ... }` builds dictionaries or sets rather than delimiting statement suites. Why the correct answer wins: A tuple of immutable objects like `(10, 20)` is hashable and valid as a `dict` key, whereas a list `[10, 20]` or a tuple containing an inner list `(10, [20])` is unhashable and raises `TypeError`.
- **E:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: A tuple of immutable objects like `(10, 20)` is hashable and valid as a `dict` key, whereas a list `[10, 20]` or a tuple containing an inner list `(10, [20])` is unhashable and raises `TypeError`.

### Question 39 — B

Answer: `2`. Repeating `'Accept'` in a dictionary literal overwrites its earlier value with `'json'`, leaving `2` unique keys (`'Accept'` and `'Host'`). Evaluates to the integer `2`. Local study-map skill 3.9 (Dictionary Literals, Key Updates, del, and Safe get() / pop()), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Repeating `'Accept'` in a dictionary literal overwrites its earlier value with `'json'`, leaving `2` unique keys (`'Accept'` and `'Host'`).
- **B:** Correct. Evaluates to the integer `2`. In this case: Repeating `'Accept'` in a dictionary literal overwrites its earlier value with `'json'`, leaving `2` unique keys (`'Accept'` and `'Host'`).
- **C:** Incorrect for this question. Evaluates to the integer `3`. Why the correct answer wins: Repeating `'Accept'` in a dictionary literal overwrites its earlier value with `'json'`, leaving `2` unique keys (`'Accept'` and `'Host'`).
- **D:** Incorrect for this question. Evaluates to the integer `1`. Why the correct answer wins: Repeating `'Accept'` in a dictionary literal overwrites its earlier value with `'json'`, leaving `2` unique keys (`'Accept'` and `'Host'`).

### Question 40 — A, D

Answers: `.items()` yields `(key, value)` 2-tuples suitable for `for k, v in d.items():` unpacking; Membership `k in d` checks only dictionary keys, not dictionary values. `k in d` checks keys only (never values), and `d.items()` yields `(key, value)` 2-tuples suitable for unpacking in a `for` loop. `d.items()` returns a dynamic view of `(key, value)` pairs. Iterating `d` or testing `x in d` inspects the dictionary's keys (`d.keys()`); checking values requires `x in d.values()`. Local study-map skill 3.10 (Dictionary Views and Iteration (keys(), values(), items())), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Iterating `d` or testing `x in d` inspects the dictionary's keys (`d.keys()`); checking values requires `x in d.values()`. In this case: `k in d` checks keys only (never values), and `d.items()` yields `(key, value)` 2-tuples suitable for unpacking in a `for` loop.
- **B:** Incorrect for this question. Plain assignment `backup = items` binds a second name to the exact same list object (an alias, not a copy). Why the correct answer wins: `k in d` checks keys only (never values), and `d.items()` yields `(key, value)` 2-tuples suitable for unpacking in a `for` loop.
- **C:** Incorrect for this question. `x in d` never searches values; a value present only on the right side of `:` returns `False` for `x in d`. Why the correct answer wins: `k in d` checks keys only (never values), and `d.items()` yields `(key, value)` 2-tuples suitable for unpacking in a `for` loop.
- **D:** Correct. `d.items()` returns a dynamic view of `(key, value)` pairs. In this case: `k in d` checks keys only (never values), and `d.items()` yields `(key, value)` 2-tuples suitable for unpacking in a `for` loop.
- **E:** Incorrect for this question. Parentheses without a comma simply group the arithmetic expression `42` (`type((42)) is int`). Why the correct answer wins: `k in d` checks keys only (never values), and `d.items()` yields `(key, value)` 2-tuples suitable for unpacking in a `for` loop.

### Question 41 — A

Answer: `3`, because `\n` is stored as one newline character rather than two separate characters. In a standard string literal, `\n` is parsed as a single newline character (ASCII `10`), so `'a'`, `'\n'`, and `'b'` give length `3`. Inside a normal string literal, `\n` (and `\t` or `\\`) represents one character, so `'a\nb'` has length `3`. Local study-map skill 3.11 (String Quoting, Escape Sequences, and Multiline Literals), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Correct. Inside a normal string literal, `\n` (and `\t` or `\\`) represents one character, so `'a\nb'` has length `3`. In this case: In a standard string literal, `\n` is parsed as a single newline character (ASCII `10`), so `'a'`, `'\n'`, and `'b'` give length `3`.
- **B:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: In a standard string literal, `\n` is parsed as a single newline character (ASCII `10`), so `'a'`, `'\n'`, and `'b'` give length `3`.
- **C:** Incorrect for this question. Only raw strings (`r'a\nb'`) keep both `\` and `n` as two characters (`len == 4`). Why the correct answer wins: In a standard string literal, `\n` is parsed as a single newline character (ASCII `10`), so `'a'`, `'\n'`, and `'b'` give length `3`.
- **D:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: In a standard string literal, `\n` is parsed as a single newline character (ASCII `10`), so `'a'`, `'\n'`, and `'b'` give length `3`.

### Question 42 — B

Answer: `strip`. `str.strip()` removes leading and trailing whitespace characters (`' '`, `'\t'`, `'\n'`) and leaves internal characters untouched. `s.strip()` returns a new string with leading and trailing whitespace removed. Local study-map skill 3.12 (String Slicing, Immutability, Searching, Joining, and Case Methods), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. `s.index(sub)` returns the lowest index of `sub`, or raises `ValueError` if `sub` is absent. Why the correct answer wins: `str.strip()` removes leading and trailing whitespace characters (`' '`, `'\t'`, `'\n'`) and leaves internal characters untouched.
- **B:** Correct. `s.strip()` returns a new string with leading and trailing whitespace removed. In this case: `str.strip()` removes leading and trailing whitespace characters (`' '`, `'\t'`, `'\n'`) and leaves internal characters untouched.
- **C:** Incorrect for this question. `s.split(sep)` splits a string around `sep` and returns a `list` of substrings. Why the correct answer wins: `str.strip()` removes leading and trailing whitespace characters (`' '`, `'\t'`, `'\n'`) and leaves internal characters untouched.
- **D:** Incorrect for this question. `s.find(sub)` returns the lowest index of `sub`, or `-1` if `sub` is absent. Why the correct answer wins: `str.strip()` removes leading and trailing whitespace characters (`' '`, `'\t'`, `'\n'`) and leaves internal characters untouched.

### Question 43 — C

Answer: `['https:', '', 'example.org', 'docs']`. Splitting on an explicit delimiter `'/'` does not merge adjacent slashes, so the empty segment between `'https:'` and `'example.org'` is preserved as `''` in `['https:', '', 'example.org', 'docs']`. `'https://example.org/docs'.split('/')` preserves the empty string between the two consecutive slashes. Local study-map skill 3.12 (String Slicing, Immutability, Searching, Joining, and Case Methods), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 3 (Data Collections - Tuples, Dictionaries, Lists, and Strings, 25 percent): https://pythoninstitute.org/pcep-exam-syllabus#block3 — and Python 3 tutorial, Data Structures: https://docs.python.org/3/tutorial/datastructures.html.

- **A:** Incorrect for this question. The empty list `[]`. Why the correct answer wins: Splitting on an explicit delimiter `'/'` does not merge adjacent slashes, so the empty segment between `'https:'` and `'example.org'` is preserved as `''` in `['https:', '', 'example.org', 'docs']`.
- **B:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: Splitting on an explicit delimiter `'/'` does not merge adjacent slashes, so the empty segment between `'https:'` and `'example.org'` is preserved as `''` in `['https:', '', 'example.org', 'docs']`.
- **C:** Correct. `'https://example.org/docs'.split('/')` preserves the empty string between the two consecutive slashes. In this case: Splitting on an explicit delimiter `'/'` does not merge adjacent slashes, so the empty segment between `'https:'` and `'example.org'` is preserved as `''` in `['https:', '', 'example.org', 'docs']`.
- **D:** Incorrect for this question. `.strip()` removes leading and trailing whitespace characters while leaving internal hyphens intact. Why the correct answer wins: Splitting on an explicit delimiter `'/'` does not merge adjacent slashes, so the empty segment between `'https:'` and `'example.org'` is preserved as `''` in `['https:', '', 'example.org', 'docs']`.

### Question 44 — A, E

Answers: `None`, because reaching the end of a function body or a bare `return` implicitly returns `None`; The first executed `return` exits the function immediately and skips all remaining statements in its body. Executing `return` exits the function immediately, and reaching the end of the body or executing bare `return` returns `None`. Every normal Python function without `yield` returns `None` whenever execution falls off the end or hits bare `return`. Code after an executed `return` inside the same branch does not run (except an enclosing `finally:` block). Local study-map skill 4.1 (Function Definitions (def), Invocation, return Paths, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Every normal Python function without `yield` returns `None` whenever execution falls off the end or hits bare `return`. In this case: Executing `return` exits the function immediately, and reaching the end of the body or executing bare `return` returns `None`.
- **B:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: Executing `return` exits the function immediately, and reaching the end of the body or executing bare `return` returns `None`.
- **C:** Incorrect for this question. Each recursive invocation gets its own independent local stack frame; `global` parameters are invalid syntax. Why the correct answer wins: Executing `return` exits the function immediately, and reaching the end of the body or executing bare `return` returns `None`.
- **D:** Incorrect for this question. `break` is valid only inside loops and raises `SyntaxError` if used directly inside a function to exit recursion. Why the correct answer wins: Executing `return` exits the function immediately, and reaching the end of the body or executing bare `return` returns `None`.
- **E:** Correct. Code after an executed `return` inside the same branch does not run (except an enclosing `finally:` block). In this case: Executing `return` exits the function immediately, and reaching the end of the body or executing bare `return` returns `None`.

### Question 45 — D

Answer: It prints the text inside the function and then assigns `None` to the caller variable because `print()` returns `None`. Inside `clean_host`, `print('api.local')` writes to the console and returns `None`, and falling off the end of `clean_host` assigns `None` to `host`. Confusing `print(x)` with `return x` leaves the function returning `None` after displaying `x` to stdout. Local study-map skill 4.1 (Function Definitions (def), Invocation, return Paths, and None), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to Boolean `True`. Why the correct answer wins: Inside `clean_host`, `print('api.local')` writes to the console and returns `None`, and falling off the end of `clean_host` assigns `None` to `host`.
- **B:** Incorrect for this question. `NameError` is raised when code reads an identifier that is not bound in local, enclosing, global, or built-in scope. Why the correct answer wins: Inside `clean_host`, `print('api.local')` writes to the console and returns `None`, and falling off the end of `clean_host` assigns `None` to `host`.
- **C:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: Inside `clean_host`, `print('api.local')` writes to the console and returns `None`, and falling off the end of `clean_host` assigns `None` to `host`.
- **D:** Correct. Confusing `print(x)` with `return x` leaves the function returning `None` after displaying `x` to stdout. In this case: Inside `clean_host`, `print('api.local')` writes to the console and returns `None`, and falling off the end of `clean_host` assigns `None` to `host`.

### Question 46 — D

Answer: `next`. Built-in `next(tokens)` resumes a generator iterator up to its next `yield` and returns the yielded value. Built-in `next(gen)` advances a generator to its next `yield` expression and returns the yielded value. Local study-map skill 4.2 (Lazy Iteration with yield Generator Functions and StopIteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `int(...)` converts a base-10 digit string or truncates a float toward zero into an integer. Why the correct answer wins: Built-in `next(tokens)` resumes a generator iterator up to its next `yield` and returns the yielded value.
- **B:** Incorrect for this question. Built-in `sorted(iterable)` returns a new sorted list without mutating its input. Why the correct answer wins: Built-in `next(tokens)` resumes a generator iterator up to its next `yield` and returns the yielded value.
- **C:** Incorrect for this question. Built-in `len(s)` returns the element count of collection `s`. Why the correct answer wins: Built-in `next(tokens)` resumes a generator iterator up to its next `yield` and returns the yielded value.
- **D:** Correct. Built-in `next(gen)` advances a generator to its next `yield` expression and returns the yielded value. In this case: Built-in `next(tokens)` resumes a generator iterator up to its next `yield` and returns the yielded value.

### Question 47 — A, B

Answers: Calling a function whose body contains `yield` returns a generator iterator object without executing the body yet; `yield` suspends the function frame with its local variables intact and resumes right after `yield` on the next `next()` call. Calling a generator function returns a lazy generator iterator before running the body, and each `yield` suspends the local frame so `next()` resumes right where it paused. Even if `yield` is unreachable at runtime, its presence in a `def` body compiles the function as a generator factory. Unlike `return`, which destroys the local frame permanently, `yield` preserves local state across resumption. Local study-map skill 4.2 (Lazy Iteration with yield Generator Functions and StopIteration), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Unlike `return`, which destroys the local frame permanently, `yield` preserves local state across resumption. In this case: Calling a generator function returns a lazy generator iterator before running the body, and each `yield` suspends the local frame so `next()` resumes right where it paused.
- **B:** Correct. Even if `yield` is unreachable at runtime, its presence in a `def` body compiles the function as a generator factory. In this case: Calling a generator function returns a lazy generator iterator before running the body, and each `yield` suspends the local frame so `next()` resumes right where it paused.
- **C:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: Calling a generator function returns a lazy generator iterator before running the body, and each `yield` suspends the local frame so `next()` resumes right where it paused.
- **D:** Incorrect for this question. Ahead-of-time native binary linking describes C, C++, or Rust toolchains, whereas standard CPython requires the Python runtime. Why the correct answer wins: Calling a generator function returns a lazy generator iterator before running the body, and each `yield` suspends the local frame so `next()` resumes right where it paused.
- **E:** Incorrect for this question. `break` is valid only inside loops and raises `SyntaxError` if used directly inside a function to exit recursion. Why the correct answer wins: Calling a generator function returns a lazy generator iterator before running the body, and each `yield` suspends the local frame so `next()` resumes right where it paused.

### Question 48 — A

Answer: `24`. `perms(4)` multiplies `4 * 3 * 2 * 1`, stopping at the base condition `k <= 1` and returning `24`. Evaluates to the integer `24`. Local study-map skill 4.3 (Recursive Functions, Base Cases, and RecursionError), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Evaluates to the integer `24`. In this case: `perms(4)` multiplies `4 * 3 * 2 * 1`, stopping at the base condition `k <= 1` and returning `24`.
- **B:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: `perms(4)` multiplies `4 * 3 * 2 * 1`, stopping at the base condition `k <= 1` and returning `24`.
- **C:** Incorrect for this question. Evaluates to the integer `120`. Why the correct answer wins: `perms(4)` multiplies `4 * 3 * 2 * 1`, stopping at the base condition `k <= 1` and returning `24`.
- **D:** Incorrect for this question. `RecursionError` (a subclass of `RuntimeError`) is raised when maximum recursion depth is exceeded. Why the correct answer wins: `perms(4)` multiplies `4 * 3 * 2 * 1`, stopping at the base condition `k <= 1` and returning `24`.

### Question 49 — A

Answer: `RecursionError` because without a reachable base case the call stack exceeds Python's recursion limit. Without a terminating base case, `descend` calls itself until exceeding Python's call-stack limit and raises `RecursionError`. Unbounded self-calls hit `sys.getrecursionlimit()` and raise `RecursionError` (a subclass of `RuntimeError`). Local study-map skill 4.3 (Recursive Functions, Base Cases, and RecursionError), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Unbounded self-calls hit `sys.getrecursionlimit()` and raise `RecursionError` (a subclass of `RuntimeError`). In this case: Without a terminating base case, `descend` calls itself until exceeding Python's call-stack limit and raises `RecursionError`.
- **B:** Incorrect for this question. `SyntaxError` is raised when the parser encounters invalid Python grammar or illegal token structure before execution starts. Why the correct answer wins: Without a terminating base case, `descend` calls itself until exceeding Python's call-stack limit and raises `RecursionError`.
- **C:** Incorrect for this question. Evaluates to the integer `0`. Why the correct answer wins: Without a terminating base case, `descend` calls itself until exceeding Python's call-stack limit and raises `RecursionError`.
- **D:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Without a terminating base case, `descend` calls itself until exceeding Python's call-stack limit and raises `RecursionError`.

### Question 50 — C

Answer: `SyntaxError` because a positional argument cannot follow a keyword argument at a call site. Python grammar forbids placing a positional argument (`'api.local'`) after a keyword argument (`port=8080`), raising `SyntaxError` at parse time. In Python call syntax, all positional arguments must appear before any `name=value` keyword arguments. Local study-map skill 4.4 (Positional, Keyword, and Mixed Call-Site Argument Rules), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `20`. Why the correct answer wins: Python grammar forbids placing a positional argument (`'api.local'`) after a keyword argument (`port=8080`), raising `SyntaxError` at parse time.
- **B:** Incorrect for this question. Passing a value positionally to the first parameter and ALSO passing that parameter name by keyword raises `TypeError: got multiple values for argument`. Why the correct answer wins: Python grammar forbids placing a positional argument (`'api.local'`) after a keyword argument (`port=8080`), raising `SyntaxError` at parse time.
- **C:** Correct. In Python call syntax, all positional arguments must appear before any `name=value` keyword arguments. In this case: Python grammar forbids placing a positional argument (`'api.local'`) after a keyword argument (`port=8080`), raising `SyntaxError` at parse time.
- **D:** Incorrect for this question. Evaluates to `None`, Python's singleton null value. Why the correct answer wins: Python grammar forbids placing a positional argument (`'api.local'`) after a keyword argument (`port=8080`), raising `SyntaxError` at parse time.

### Question 51 — A

Answer: `TypeError` because the same parameter receives both a positional argument and a keyword argument. `'api.local'` binds `host` positionally and `host='backup.local'` supplies a second value for `host`, raising `TypeError`. Passing a value positionally to the first parameter and ALSO passing that parameter name by keyword raises `TypeError: got multiple values for argument`. Local study-map skill 4.4 (Positional, Keyword, and Mixed Call-Site Argument Rules), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Passing a value positionally to the first parameter and ALSO passing that parameter name by keyword raises `TypeError: got multiple values for argument`. In this case: `'api.local'` binds `host` positionally and `host='backup.local'` supplies a second value for `host`, raising `TypeError`.
- **B:** Incorrect for this question. In Python call syntax, all positional arguments must appear before any `name=value` keyword arguments. Why the correct answer wins: `'api.local'` binds `host` positionally and `host='backup.local'` supplies a second value for `host`, raising `TypeError`.
- **C:** Incorrect for this question. Evaluates to the integer `20`. Why the correct answer wins: `'api.local'` binds `host` positionally and `host='backup.local'` supplies a second value for `host`, raising `TypeError`.
- **D:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: `'api.local'` binds `host` positionally and `host='backup.local'` supplies a second value for `host`, raising `TypeError`.

### Question 52 — C, D

Answers: Default values are evaluated once at `def` time, so one shared list accumulates items across calls that omit the argument; Use `buf=None` in the signature and initialize `if buf is None: buf = []` inside the function body. Default values are evaluated once when `def` executes so `errs=[]` shares one list across calls; defaulting `errs=None` and assigning `errs = []` when `errs is None` creates a fresh list per call. A mutable default like `buf=[]` is bound once on `def` execution and reused on every call that relies on the default. Using `None` as a sentinel creates a fresh list on each call that omits `buf`. Local study-map skill 4.5 (Default Parameter Ordering and Mutable-Default Lifetime Traps), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `x in d` never searches values; a value present only on the right side of `:` returns `False` for `x in d`. Why the correct answer wins: Default values are evaluated once when `def` executes so `errs=[]` shares one list across calls; defaulting `errs=None` and assigning `errs = []` when `errs is None` creates a fresh list per call.
- **B:** Incorrect for this question. Each recursive invocation gets its own independent local stack frame; `global` parameters are invalid syntax. Why the correct answer wins: Default values are evaluated once when `def` executes so `errs=[]` shares one list across calls; defaulting `errs=None` and assigning `errs = []` when `errs is None` creates a fresh list per call.
- **C:** Correct. A mutable default like `buf=[]` is bound once on `def` execution and reused on every call that relies on the default. In this case: Default values are evaluated once when `def` executes so `errs=[]` shares one list across calls; defaulting `errs=None` and assigning `errs = []` when `errs is None` creates a fresh list per call.
- **D:** Correct. Using `None` as a sentinel creates a fresh list on each call that omits `buf`. In this case: Default values are evaluated once when `def` executes so `errs=[]` shares one list across calls; defaulting `errs=None` and assigning `errs = []` when `errs is None` creates a fresh list per call.
- **E:** Incorrect for this question. Standard float literals use binary IEEE-754 `float`; exact base-10 arithmetic requires importing `decimal.Decimal` explicitly. Why the correct answer wins: Default values are evaluated once when `def` executes so `errs=[]` shares one list across calls; defaulting `errs=None` and assigning `errs = []` when `errs is None` creates a fresh list per call.

### Question 53 — B

Answer: `def quote(amount, rate=1.1, fee=0):`. Required parameter `amount` precedes defaulted parameters `rate=1.1` and `fee=0` in `def quote(amount, rate=1.1, fee=0):`. Placing required parameter `amount` before defaulted parameters `rate=1.1` and `fee=0` is valid Python signature order. Local study-map skill 4.5 (Default Parameter Ordering and Mutable-Default Lifetime Traps), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. C/JavaScript `? :` ternary syntax raises `SyntaxError` in Python. Why the correct answer wins: Required parameter `amount` precedes defaulted parameters `rate=1.1` and `fee=0` in `def quote(amount, rate=1.1, fee=0):`.
- **B:** Correct. Placing required parameter `amount` before defaulted parameters `rate=1.1` and `fee=0` is valid Python signature order. In this case: Required parameter `amount` precedes defaulted parameters `rate=1.1` and `fee=0` in `def quote(amount, rate=1.1, fee=0):`.
- **C:** Incorrect for this question. Placing non-default `amount` after default `rate=1.1` raises `SyntaxError`. Why the correct answer wins: Required parameter `amount` precedes defaulted parameters `rate=1.1` and `fee=0` in `def quote(amount, rate=1.1, fee=0):`.
- **D:** Incorrect for this question. Placing positional `0.2` after keyword `base=100` raises `SyntaxError`. Why the correct answer wins: Required parameter `amount` precedes defaulted parameters `rate=1.1` and `fee=0` in `def quote(amount, rate=1.1, fee=0):`.

### Question 54 — A

Answer: `10`. Without `global timeout`, `timeout = 42` binds a separate local variable inside `override()`, leaving module-level `timeout` equal to `10`. Evaluates to the integer `10`. Local study-map skill 4.6 (LEGB Lookup, Local Shadowing, UnboundLocalError, and global), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. Evaluates to the integer `10`. In this case: Without `global timeout`, `timeout = 42` binds a separate local variable inside `override()`, leaving module-level `timeout` equal to `10`.
- **B:** Incorrect for this question. Evaluates to the integer `42`. Why the correct answer wins: Without `global timeout`, `timeout = 42` binds a separate local variable inside `override()`, leaving module-level `timeout` equal to `10`.
- **C:** Incorrect for this question. `UnboundLocalError` (a subclass of `NameError`) is raised when a local variable is referenced before assignment inside a function. Why the correct answer wins: Without `global timeout`, `timeout = 42` binds a separate local variable inside `override()`, leaving module-level `timeout` equal to `10`.
- **D:** Incorrect for this question. `NameError` is raised when code reads an identifier that is not bound in local, enclosing, global, or built-in scope. Why the correct answer wins: Without `global timeout`, `timeout = 42` binds a separate local variable inside `override()`, leaving module-level `timeout` equal to `10`.

### Question 55 — D

Answer: `UnboundLocalError`. `hits = hits + 1` marks `hits` as local throughout `bump()`, so reading `hits` in `print(hits)` before local assignment raises `UnboundLocalError`. `UnboundLocalError` (a subclass of `NameError`) is raised when a local variable is referenced before assignment inside a function. Local study-map skill 4.6 (LEGB Lookup, Local Shadowing, UnboundLocalError, and global), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. Evaluates to the integer `10`. Why the correct answer wins: `hits = hits + 1` marks `hits` as local throughout `bump()`, so reading `hits` in `print(hits)` before local assignment raises `UnboundLocalError`.
- **B:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: `hits = hits + 1` marks `hits` as local throughout `bump()`, so reading `hits` in `print(hits)` before local assignment raises `UnboundLocalError`.
- **C:** Incorrect for this question. Evaluates to the integer `11`. Why the correct answer wins: `hits = hits + 1` marks `hits` as local throughout `bump()`, so reading `hits` in `print(hits)` before local assignment raises `UnboundLocalError`.
- **D:** Correct. `UnboundLocalError` (a subclass of `NameError`) is raised when a local variable is referenced before assignment inside a function. In this case: `hits = hits + 1` marks `hits` as local throughout `bump()`, so reading `hits` in `print(hits)` before local assignment raises `UnboundLocalError`.

### Question 56 — B, E

Answers: `IndexError`; `KeyError`. `IndexError` (sequence index out of range) and `KeyError` (missing mapping key) both inherit directly from `LookupError`, so `except LookupError:` catches either one. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Local study-map skill 4.7 (Built-In Exception Tree (BaseException, Exception, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `TypeError` is raised when an operator or function is applied to an object of an inappropriate type, or called with the wrong argument count. Why the correct answer wins: `IndexError` (sequence index out of range) and `KeyError` (missing mapping key) both inherit directly from `LookupError`, so `except LookupError:` catches either one.
- **B:** Correct. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. In this case: `IndexError` (sequence index out of range) and `KeyError` (missing mapping key) both inherit directly from `LookupError`, so `except LookupError:` catches either one.
- **C:** Incorrect for this question. `ZeroDivisionError` (a subclass of `ArithmeticError`) is raised when dividing or taking modulo by `0` or `0.0`. Why the correct answer wins: `IndexError` (sequence index out of range) and `KeyError` (missing mapping key) both inherit directly from `LookupError`, so `except LookupError:` catches either one.
- **D:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: `IndexError` (sequence index out of range) and `KeyError` (missing mapping key) both inherit directly from `LookupError`, so `except LookupError:` catches either one.
- **E:** Correct. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. In this case: `IndexError` (sequence index out of range) and `KeyError` (missing mapping key) both inherit directly from `LookupError`, so `except LookupError:` catches either one.

### Question 57 — C

Answer: `BaseException`. `BaseException` is the root base class of all built-in exceptions in Python 3. `BaseException` sits at the root of the entire exception tree; `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` rather than `Exception`. Local study-map skill 4.7 (Built-In Exception Tree (BaseException, Exception, LookupError, ArithmeticError)), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: `BaseException` is the root base class of all built-in exceptions in Python 3.
- **B:** Incorrect for this question. `LookupError` is the common superclass of both `IndexError` and `KeyError` under `Exception`. Why the correct answer wins: `BaseException` is the root base class of all built-in exceptions in Python 3.
- **C:** Correct. `BaseException` sits at the root of the entire exception tree; `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException` rather than `Exception`. In this case: `BaseException` is the root base class of all built-in exceptions in Python 3.
- **D:** Incorrect for this question. `ArithmeticError` is the parent class of `ZeroDivisionError`, `OverflowError`, and `FloatingPointError`. Why the correct answer wins: `BaseException` is the root base class of all built-in exceptions in Python 3.

### Question 58 — A

Answer: `AttributeError`. Python `list` objects have no `.join` attribute (`join` is a method on `str`), so `parts.join('/')` raises `AttributeError`. `AttributeError` is raised when accessing a method or attribute name that does not exist on that object's type. Local study-map skill 4.8 (Diagnosing and Raising Concrete Built-In Exceptions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Correct. `AttributeError` is raised when accessing a method or attribute name that does not exist on that object's type. In this case: Python `list` objects have no `.join` attribute (`join` is a method on `str`), so `parts.join('/')` raises `AttributeError`.
- **B:** Incorrect for this question. `ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int('12.5')` or `int('abc')`). Why the correct answer wins: Python `list` objects have no `.join` attribute (`join` is a method on `str`), so `parts.join('/')` raises `AttributeError`.
- **C:** Incorrect for this question. `KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key. Why the correct answer wins: Python `list` objects have no `.join` attribute (`join` is a method on `str`), so `parts.join('/')` raises `AttributeError`.
- **D:** Incorrect for this question. `IndexError` (a subclass of `LookupError`) is raised when a sequence subscript `seq[i]` is out of range. Why the correct answer wins: Python `list` objects have no `.join` attribute (`join` is a method on `str`), so `parts.join('/')` raises `AttributeError`.

### Question 59 — B

Answer: `assert`. `assert <condition>, <message>` evaluates `<condition>` and raises `AssertionError` when it is falsy. `assert` is a hard reserved keyword in Python 3 used for debugging assertions. Local study-map skill 4.8 (Diagnosing and Raising Concrete Built-In Exceptions), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `with` is a hard reserved keyword in Python 3 for context-managed execution blocks. Why the correct answer wins: `assert <condition>, <message>` evaluates `<condition>` and raises `AssertionError` when it is falsy.
- **B:** Correct. `assert` is a hard reserved keyword in Python 3 used for debugging assertions. In this case: `assert <condition>, <message>` evaluates `<condition>` and raises `AssertionError` when it is falsy.
- **C:** Incorrect for this question. `raise` is a hard reserved keyword in Python 3 that triggers or re-raises an exception. Why the correct answer wins: `assert <condition>, <message>` evaluates `<condition>` and raises `AssertionError` when it is falsy.
- **D:** Incorrect for this question. `except` is a hard reserved keyword in Python 3 that catches exceptions raised in a `try` block. Why the correct answer wins: `assert <condition>, <message>` evaluates `<condition>` and raises `AssertionError` when it is falsy.

### Question 60 — C

Answer: `finally`. A `finally:` suite always executes on exit from the `try` statement regardless of whether an exception occurred or was caught. `finally` is a hard reserved keyword in Python 3 whose suite runs whether an exception occurred or not. Local study-map skill 4.9 (Structured try / except / else / finally Ordering and Propagation), mapped to the official syllabus: PCEP-30-0x exam syllabus (OpenEDG Python Institute, baseline for PCEP-30-03). Primary reference: PCEP-30-0x exam syllabus, Block 4 (Functions and Exceptions, 28 percent): https://pythoninstitute.org/pcep-exam-syllabus#block4 — and Python 3 tutorial, Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html.

- **A:** Incorrect for this question. `else` is a hard reserved keyword in Python 3 used on conditionals, loops, and `try` blocks. Why the correct answer wins: A `finally:` suite always executes on exit from the `try` statement regardless of whether an exception occurred or was caught.
- **B:** Incorrect for this question. `pass` is a hard reserved keyword in Python 3 that acts as a syntactic no-op statement. Why the correct answer wins: A `finally:` suite always executes on exit from the `try` statement regardless of whether an exception occurred or was caught.
- **C:** Correct. `finally` is a hard reserved keyword in Python 3 whose suite runs whether an exception occurred or not. In this case: A `finally:` suite always executes on exit from the `try` statement regardless of whether an exception occurred or was caught.
- **D:** Incorrect for this question. `except` is a hard reserved keyword in Python 3 that catches exceptions raised in a `try` block. Why the correct answer wins: A `finally:` suite always executes on exit from the `try` statement regardless of whether an exception occurred or was caught.
