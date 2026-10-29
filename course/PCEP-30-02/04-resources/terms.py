"""Option bank for the PCEP-30-02 (Certified Entry-Level Python Programmer) practice sets.

Every option is a concrete CPython output, runtime or syntax exception, filler token for
a `____` gap-fill snippet, operator, collection expression, or Python language rule, paired
with a one-sentence explanation of what that option means or produces so every distractor
teaches why it does not fit the question. Keys are authoring identifiers only and never
appear in an exported CSV or review copy.
"""

TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'duplicate option key: {key}')
    TERMS[key] = (label, meaning)


# --- Block 1: Execution model, lexis/syntax/semantics, keywords & naming ---
t('interp_bytecode', 'CPython compiles source to bytecode and executes it in a virtual machine line by line at runtime',
  'An interpreter translates and executes source through bytecode at runtime without producing a standalone native executable.')
t('compiler_native', 'CPython links source directly into a standalone machine-code binary before the user runs the script',
  'Ahead-of-time native machine-code compilation is what a C or Rust compiler performs, not standard CPython.')
t('source_file_py', 'The plain-text file holding Python instructions written by the programmer',
  'A source file stores human-readable Python statements before translation begins.')
t('linker_static', 'A static linker merges Python modules into firmware without needing a runtime interpreter',
  'Standard Python scripts still require a Python runtime rather than a static hardware linker.')

t('lexis_word_dict', 'Lexis defines the set of valid tokens and words recognized by the language',
  'Lexis is the vocabulary layer governing legal identifiers, literals, operators, and keywords.')
t('syntax_grammar', 'Syntax defines the grammar rules for combining tokens into legal statements',
  'Syntax checks whether tokens appear in a structurally valid arrangement such as matching parentheses and colons.')
t('semantics_meaning', 'Semantics determines whether a syntactically valid statement makes sense and what it computes',
  'Semantics governs runtime meaning, so dividing a number by zero is syntactically legal yet fails semantically at runtime.')
t('pragmatics_pep20', 'Style formatting comments automatically bypass syntax checking during parsing',
  'Comments are ignored by the parser and never disable syntax checking on surrounding code.')

t('kw_elif', '`elif`',
  '`elif` is a reserved Python keyword that introduces an additional conditional branch.')
t('kw_lambda', '`lambda`',
  '`lambda` is a reserved Python keyword and therefore cannot be used as a variable identifier.')
t('kw_global', '`global`',
  '`global` is a reserved Python keyword that binds a name inside a function to module scope.')
t('kw_yield', '`yield`',
  '`yield` is a reserved Python keyword that turns a function into a generator.')
t('kw_assert', '`assert`',
  '`assert` is a reserved Python keyword used for debugging checks.')
t('kw_nonlocal', '`nonlocal`',
  '`nonlocal` is a reserved Python keyword and cannot name an ordinary variable.')
t('kw_pass', '`pass`',
  '`pass` is a reserved null-operation keyword required where syntax expects an indented suite.')
t('kw_break', '`break`',
  '`break` exits the innermost enclosing `for` or `while` loop immediately and skips its `else` branch.')
t('kw_continue', '`continue`',
  '`continue` abandons the rest of the current iteration and jumps to the next cycle of the enclosing loop.')
t('kw_return', '`return`',
  '`return` exits the current function immediately and sends a value back to the caller.')
t('kw_raise', '`raise`',
  '`raise` triggers an exception or re-raises the active exception when used bare inside `except`.')
t('kw_del', '`del`',
  '`del` is a statement keyword (not a function) that unbinds a name, slice, index, or dictionary key.')
t('kw_in', '`in`',
  '`in` tests element or substring membership and also binds loop targets in `for` headers.')
t('kw_not_in', '`not in`',
  '`not in` evaluates to `True` when the left operand is absent from the right-hand container.')
t('kw_is', '`is`',
  '`is` compares object identity rather than value equality.')

t('id_valid_snake', '`total_count_2`',
  'Identifiers may contain letters, digits, and underscores provided they do not start with a digit or match a keyword.')
t('id_valid_leading_under', '`_temp_value`',
  'A leading underscore is a legal identifier start in Python and signals an internal helper by convention.')
t('id_valid_unicode', '`item_price_usd`',
  'Lowercase words separated by underscores (`snake_case`) follow PEP-8 variable naming recommendations.')
t('id_invalid_digit', '`2nd_total`',
  'An identifier cannot begin with a decimal digit, so `2nd_total` fails lexical analysis with `SyntaxError`.')
t('id_invalid_hyphen', '`user-count`',
  'A hyphen is parsed as the subtraction operator rather than part of an identifier.')
t('id_invalid_space', '`raw score`',
  'Whitespace separates tokens and is illegal inside a Python variable name.')
t('id_builtin_print', '`print`',
  '`print` is a built-in function name rather than a hard keyword, though shadowing it is poor practice.')
t('id_builtin_list', '`list`',
  '`list` names a built-in type rather than a reserved keyword, so Python permits (but discourages) rebinding it.')
t('id_case_True', '`true`',
  'Keywords are case-sensitive: `True` is reserved, whereas lowercase `true` is an ordinary identifier.')
t('id_case_None', '`none`',
  'Only capitalized `None` is a keyword; lowercase `none` is not reserved by Python.')

t('indent_consistent', 'Every statement in the same suite must share the exact same indentation width',
  'Python groups blocks by indentation level, and PEP-8 recommends four spaces per level.')
t('hash_comment', 'Text after `#` outside string literals is ignored until the end of the physical line',
  '`#` starts a single-line comment; Python has no dedicated multi-line `/* ... */` comment delimiter.')

# --- Literals, bases, floats, and numeric values ---------------------------
t('num_0', '`0`', 'Evaluates to the integer zero.')
t('num_1', '`1`', 'Evaluates to the integer `1`.')
t('num_2', '`2`', 'Evaluates to the integer `2`.')
t('num_3', '`3`', 'Evaluates to the integer `3`.')
t('num_4', '`4`', 'Evaluates to the integer `4`.')
t('num_5', '`5`', 'Evaluates to the integer `5`.')
t('num_6', '`6`', 'Evaluates to the integer `6`.')
t('num_7', '`7`', 'Evaluates to the integer `7`.')
t('num_8', '`8`', 'Evaluates to the integer `8`.')
t('num_9', '`9`', 'Evaluates to the integer `9`.')
t('num_10', '`10`', 'Evaluates to the integer `10`.')
t('num_11', '`11`', 'Evaluates to the integer `11`.')
t('num_12', '`12`', 'Evaluates to the integer `12`.')
t('num_13', '`13`', 'Evaluates to the integer `13`.')
t('num_14', '`14`', 'Evaluates to the integer `14`.')
t('num_15', '`15`', 'Evaluates to the integer `15`.')
t('num_16', '`16`', 'Evaluates to the integer `16`.')
t('num_17', '`17`', 'Evaluates to the integer `17`.')
t('num_18', '`18`', 'Evaluates to the integer `18`.')
t('num_19', '`19`', 'Evaluates to the integer `19`.')
t('num_20', '`20`', 'Evaluates to the integer `20`.')
t('num_21', '`21`', 'Evaluates to the integer `21`.')
t('num_23', '`23`', 'Evaluates to the integer `23`.')
t('num_24', '`24`', 'Evaluates to the integer `24`.')
t('num_25', '`25`', 'Evaluates to the integer `25`.')
t('num_26', '`26`', 'Evaluates to the integer `26`.')
t('num_27', '`27`', 'Evaluates to the integer `27`.')
t('num_29', '`29`', 'Evaluates to the integer `29`.')
t('num_30', '`30`', 'Evaluates to the integer `30`.')
t('num_32', '`32`', 'Evaluates to the integer `32`.')
t('num_42', '`42`', 'Evaluates to the integer `42`.')
t('num_45', '`45`', 'Evaluates to the integer `45`.')
t('num_64', '`64`', 'Evaluates to the integer `64`.')
t('num_100', '`100`', 'Evaluates to the integer `100`.')
t('num_256', '`256`', 'Evaluates to the integer `256`.')
t('num_512', '`512`', 'Evaluates to the integer `512`.')
t('num_neg1', '`-1`', 'Evaluates to the negative integer `-1`.')
t('num_neg2', '`-2`', 'Evaluates to the negative integer `-2`.')
t('num_neg3', '`-3`', 'Evaluates to the negative integer `-3`.')
t('num_neg4', '`-4`', 'Evaluates to the negative integer `-4`.')
t('num_neg5', '`-5`', 'Evaluates to the negative integer `-5`.')
t('num_neg8', '`-8`', 'Evaluates to the negative integer `-8`.')
t('num_neg9', '`-9`', 'Evaluates to the negative integer `-9`.')
t('num_neg16', '`-16`', 'Evaluates to the negative integer `-16`.')

t('flt_0_0', '`0.0`', 'Evaluates to the floating-point value `0.0`; true division `/` and scientific notation always yield `float`.')
t('flt_0_5', '`0.5`', 'Evaluates to the floating-point value `0.5`.')
t('flt_1_0', '`1.0`', 'Evaluates to the floating-point value `1.0`.')
t('flt_1_5', '`1.5`', 'Evaluates to the floating-point value `1.5`.')
t('flt_2_0', '`2.0`', 'Evaluates to the floating-point value `2.0` because `/` always produces a `float` even on exact division.')
t('flt_2_5', '`2.5`', 'Evaluates to the floating-point value `2.5`.')
t('flt_3_0', '`3.0`', 'Evaluates to the floating-point value `3.0` because any float operand promotes arithmetic output to `float`.')
t('flt_3_5', '`3.5`', 'Evaluates to the floating-point value `3.5`.')
t('flt_4_0', '`4.0`', 'Evaluates to the floating-point value `4.0`.')
t('flt_4_5', '`4.5`', 'Evaluates to the floating-point value `4.5`.')
t('flt_5_0', '`5.0`', 'Evaluates to the floating-point value `5.0`.')
t('flt_6_0', '`6.0`', 'Evaluates to the floating-point value `6.0`.')
t('flt_neg2_0', '`-2.0`', 'Evaluates to the floating-point value `-2.0`; floor division with a float operand returns a floored `float`.')
t('flt_neg3_0', '`-3.0`', 'Evaluates to the floating-point value `-3.0` because floor division rounds toward negative infinity.')
t('flt_300_0', '`300.0`', 'Scientific notation such as `3e2` always creates a `float` (`300.0`), never an `int`.')
t('flt_0_025', '`0.025`', 'Scientific notation with a negative exponent such as `2.5e-2` produces the `float` `0.025`.')
t('flt_inexact_bool', '`False`, because binary IEEE-754 floats cannot represent `0.1` and `0.2` exactly',
  '`0.1 + 0.2` produces `0.30000000000000004` in binary floating point, so `0.1 + 0.2 == 0.3` evaluates to `False`.')
t('flt_exact_myth', '`True`, because Python stores decimal fractions exactly to two decimal places',
  'Standard Python `float` uses binary IEEE-754 rather than exact base-10 representation.')

t('lit_bin_valid', '`0b1011`', 'Prefix `0b` or `0B` denotes a base-2 integer literal (`11` in decimal).')
t('lit_oct_valid', '`0o17`', 'Prefix `0o` or `0O` denotes a base-8 integer literal (`15` in decimal).')
t('lit_hex_valid', '`0x1F`', 'Prefix `0x` or `0X` denotes a base-16 integer literal (`31` in decimal).')
t('lit_underscored_int', '`1_000_000`', 'Single underscores between digits are legal visual separators in Python numeric literals.')
t('lit_invalid_oct8', '`0o18`', 'Digit `8` is out of range for base-8 octal literals (`0` through `7`), causing `SyntaxError`.')
t('lit_invalid_leading0', '`017`', 'Leading zeros on non-zero decimal integers are illegal in Python 3 and raise `SyntaxError`.')
t('lit_sci_float', '`4e3`', 'Scientific-notation literals like `4e3` are always of type `float` (`4000.0`).')

# --- Booleans, None, types, operators, and gap-fill tokens -----------------
t('val_true', '`True`', 'Evaluates to Boolean `True`.')
t('val_false', '`False`', 'Evaluates to Boolean `False`.')
t('val_none', '`None`', 'Evaluates to `None`, the singleton returned by functions and in-place mutator methods that return no explicit value.')
t('val_empty_str', "`''` (the empty string)", 'Evaluates to an empty `str` of length `0`, which is falsy in Boolean contexts.')
t('val_empty_list', '`[]`', 'Evaluates to an empty `list` of length `0`.')
t('val_empty_tuple', '`()`', 'Evaluates to an empty `tuple` of length `0`.')
t('val_empty_dict', '`{}`', 'An empty `{}` literal creates an empty `dict` (not a `set`).')

t('type_int', "`<class 'int'>`", 'Represents Python arbitrary-precision integers (note that `bool` is a subclass of `int`).')
t('type_float', "`<class 'float'>`", 'Represents double-precision IEEE-754 floating-point numbers.')
t('type_str', "`<class 'str'>`", 'Represents immutable Unicode text sequences; `input()` always returns `str`.')
t('type_bool', "`<class 'bool'>`", 'Represents truth values `True` and `False`.')
t('type_list', "`<class 'list'>`", 'Represents mutable ordered sequences.')
t('type_tuple', "`<class 'tuple'>`", 'Represents immutable ordered sequences created by commas.')
t('type_dict', "`<class 'dict'>`", 'Represents mutable key-to-value mappings.')
t('type_none', "`<class 'NoneType'>`", 'Represents the sole type of the `None` singleton.')
t('type_generator', "`<class 'generator'>`", 'Calling a function whose body contains `yield` returns a generator iterator object.')

t('op_floordiv', '`//`', 'Floor division rounds the quotient down toward negative infinity (`math.floor`).')
t('op_truediv', '`/`', 'True division always returns a `float`, even when the numerator is an exact multiple of the denominator.')
t('op_mod', '`%`', 'Modulo returns the remainder `a - (a // b) * b`, taking the sign of the divisor `b` in Python.')
t('op_pow', '`**`', 'Exponentiation has higher precedence than unary minus on its left and binds right-to-left (`2 ** 3 ** 2 == 512`).')
t('op_bit_and', '`&`', 'Bitwise AND sets each bit to `1` only where both integer operands have `1`.')
t('op_bit_or', '`|` (bitwise OR)', 'Bitwise OR sets each bit to `1` where at least one integer operand has `1`.')
t('op_bit_xor', '`^`', 'Bitwise XOR sets each bit to `1` where the two integer operands differ (it is NOT exponentiation in Python).')
t('op_bit_not', '`~`', 'Bitwise inversion computes `-(x + 1)` in two-complement integer arithmetic.')
t('op_lshift', '`<<`', 'Left bit-shift multiplies a non-negative integer by `2 ** n`.')
t('op_rshift', '`>>`', 'Right bit-shift floor-divides an integer by `2 ** n`.')
t('op_and', '`and`', 'Logical `and` short-circuits: it returns the first falsy operand, or the right operand if the left is truthy.')
t('op_or', '`or`', 'Logical `or` short-circuits: it returns the first truthy operand, or the right operand if the left is falsy.')
t('op_not', '`not`', 'Logical `not` always returns a `bool` (`True` or `False`) and has lower precedence than relational operators.')
t('op_eq', '`==`', '`==` tests value equality rather than assignment (`=`) or object identity (`is`).')
t('op_ne', '`!=`', '`!=` evaluates to `True` when two operands do not compare equal.')

# --- Console I/O and type casting ------------------------------------------
t('io_sep_dash', "`sep='-'`", 'The `sep` keyword argument sets the string placed between positional arguments passed to `print()`.')
t('io_end_space', "`end=' '`", 'The `end` keyword argument replaces the default trailing newline `\\n` emitted after `print()`.')
t('io_sep_empty', "`sep=''`", 'Passing an empty separator concatenates `print()` arguments with no intervening space.')
t('io_out_a_b_c', '`a-b-c!`', 'Joining three arguments with `-` and ending with `!` prints `a-b-c!`.')
t('io_out_ab_space', '`a b`', 'Default `sep` in `print()` is a single space and default `end` is `\\n`.')
t('io_out_joined_line', '`10:20#30`', 'Custom `sep` joins items within one `print()` call while `end` joins consecutive `print()` calls on the same line.')
t('io_out_two_prints', '`OK-DONE`', 'Setting `end="-"` on the first `print()` keeps the second `print()` output on the same line right after `-`.')
t('cast_int_call', '`int()`', '`int()` converts a base-10 integer string or truncates a `float` toward zero (`int(-3.9) == -3`).')
t('cast_float_call', '`float()`', '`float()` parses numeric strings (including decimal points or scientific notation) into `float`.')
t('cast_str_call', '`str()`', '`str()` converts numbers or collections to text so `+` can concatenate them with strings without `TypeError`.')
t('cast_bool_call', '`bool()`', '`bool()` returns `False` only for `0`, `0.0`, empty collections/strings, and `None`; non-empty strings like `"False"` or `"0"` are `True`.')
t('out_str_repeat_3', '`777`', '`input()` returns `str`, so multiplying `"7" * 3` repeats the string three times (`"777"`) instead of computing `21`.')
t('out_str_concat_12', '`123`', 'Concatenating strings `"12" + "3"` yields `"123"` rather than numeric addition `15`.')

# --- Control flow outputs & range / loop fillers ---------------------------
t('range_stop_only', '`range(5)`', '`range(5)` yields `0, 1, 2, 3, 4` (start defaults to `0`, stop `5` is excluded).')
t('range_start_stop', '`range(1, 6)`', '`range(1, 6)` yields the five integers `1, 2, 3, 4, 5` because the stop bound is exclusive.')
t('range_step_2', '`range(2, 9, 2)`', '`range(2, 9, 2)` yields `2, 4, 6, 8`, stopping before `9`.')
t('range_countdown', '`range(5, 0, -1)`', 'A negative step counts downward from `start` while values remain strictly greater than `stop`.')
t('range_empty_step', '`range(5, 1)`', 'With default step `+1` and `start >= stop`, `range(5, 1)` produces zero iterations.')

t('out_branch_a', '`A`', 'Prints `A` because the first matching `if`/`elif` branch runs and skips all remaining `elif`/`else` clauses.')
t('out_branch_b', '`B`', 'Prints `B` when the `if` condition is `False` and the first `elif` condition is `True`.')
t('out_branch_c', '`C`', 'Prints `C` when earlier branches evaluate to `False` and execution reaches the matching clause.')
t('out_branch_d', '`D`', 'Prints `D` via the final `else` fallback when every preceding condition is `False`.')
t('out_ab', '`A B`', 'Prints `A B` when two independent `if` statements (rather than `if`/`elif`) both evaluate to `True`.')
t('out_done', '`DONE`', 'Prints `DONE` because the loop finished normally without hitting `break`, triggering its `else` suite.')
t('out_found', '`FOUND`', 'Prints `FOUND` and skips the loop `else` clause because `break` terminated the loop early.')
t('out_0_1_2', '`0 1 2`', 'Prints `0 1 2` across iterations.')
t('out_1_2_3', '`1 2 3`', 'Prints `1 2 3` across iterations.')
t('out_1_3_5', '`1 3 5`', 'Prints the odd values `1 3 5` when even iterations hit `continue`.')
t('out_2_4_6', '`2 4 6`', 'Prints `2 4 6` across the loop.')
t('out_3_2_1', '`3 2 1`', 'Prints `3 2 1` while counting down.')
t('out_nothing', 'Nothing is printed (zero iterations)', 'When the loop condition is initially `False` (or `range` is empty) and there is no `else` print, the body never runs.')

# --- Block 3: Lists, tuples, dicts, strings outputs & methods --------------
t('list_123', '`[1, 2, 3]`', 'Produces the three-element list `[1, 2, 3]`.')
t('list_321', '`[3, 2, 1]`', 'Slicing with `[::-1]` or calling `.reverse()` reverses the element order.')
t('list_2_4', '`[2, 4]`', 'Produces the filtered two-element list `[2, 4]`.')
t('list_0_4_16', '`[0, 4, 16]`', 'Squares only the even elements selected by the comprehension filter.')
t('list_1_9_25', '`[1, 9, 25]`', 'Squares only the odd elements selected by the comprehension filter.')
t('list_slice_mid', '`[20, 30]`', 'Slicing `items[1:3]` starts at index `1` and stops before index `3`.')
t('list_slice_step', '`[10, 30, 50]`', 'Slicing `[::2]` selects every second element starting at index `0`.')
t('list_alias_mutated', '`[1, 99, 3]`', 'Assigning `b = a` binds both names to the same list object, so mutating `b` mutates `a`.')
t('list_copy_unmutated', '`[1, 2, 3]` (unchanged, because `a[:]` creates a shallow copy)',
  'Slicing `a[:]` or calling `a.copy()` allocates a new outer list so reassigning an element in the copy leaves `a` untouched.')
t('list_nested_shared', '`[[9, 2], [9, 2]]`', 'Multiplying `[[1, 2]] * 2` duplicates references to the same inner list rather than cloning inner rows.')

t('meth_append', '`append()`', '`list.append(x)` adds `x` as a single element at the end of the list in place and returns `None`.')
t('meth_extend', '`extend()`', '`list.extend(iterable)` appends each element from `iterable` individually and returns `None`.')
t('meth_insert', '`insert()`', '`list.insert(i, x)` places `x` before index `i` in place and returns `None`.')
t('meth_pop', '`pop()`', '`list.pop(i=-1)` removes and returns the element at index `i` (defaulting to the last item).')
t('meth_remove', '`remove()`', '`list.remove(x)` deletes the first occurrence of value `x` and raises `ValueError` if `x` is absent.')
t('meth_index', '`index()`', '`.index(x)` returns the zero-based position of the first match and raises `ValueError` when `x` is missing.')
t('meth_sort', '`sort()`', '`list.sort()` sorts a list in place and returns `None`, whereas `sorted(seq)` returns a brand-new list.')
t('fn_sorted', '`sorted()`', '`sorted(iterable)` leaves the input untouched and returns a newly allocated sorted `list`.')
t('fn_len', '`len()`', '`len(obj)` returns the item or character count of a sequence or collection.')

t('tup_singleton_comma', '`(7,)`', 'A trailing comma is what constructs a one-element tuple; `(7)` without a comma is just the integer `7` in parentheses.')
t('tup_parens_int', '`(7)`', 'Parentheses without a comma group an arithmetic expression rather than building a tuple.')
t('tup_inner_list_ok', '`(1, [2, 99])`', 'Although a tuple cannot rebind its slots, a mutable list stored inside a tuple can still be mutated in place.')

t('dict_keys', '`keys()`', '`dict.keys()` returns a dynamic view of the dictionary keys.')
t('dict_values', '`values()`', '`dict.values()` returns a dynamic view of the dictionary values.')
t('dict_items', '`items()`', '`dict.items()` yields `(key, value)` 2-tuples suitable for two-variable `for k, v in d.items():` unpacking.')
t('dict_get', '`get()`', '`dict.get(key, default=None)` returns `default` instead of raising `KeyError` when `key` is missing.')
t('dict_pop', '`pop()` on a dictionary', '`dict.pop(key)` removes `key` and returns its associated value.')
t('dict_dup_key_last', 'Duplicate keys overwrite earlier entries, keeping the last value assigned to that key',
  'In `{"a": 1, "a": 2}`, the final binding wins so `len` is `1` and `d["a"]` is `2`.')

t('str_py', "`'py'`", "Evaluates to the two-character string `'py'`.")
t('str_thon', "`'thon'`", "Evaluates to the four-character substring `'thon'`.")
t('str_nohtyp', "`'nohtyp'`", "Slicing `'python'[::-1]` reverses the string into `'nohtyp'`.")
t('str_pto', "`'pto'`", "Slicing `'python'[::2]` picks indices `0, 2, 4`, yielding `'pto'`.")
t('str_upper_abc', "`'A-B-C'`", "Joining `'abc'.upper()` with `'-'` produces `'A-B-C'`.")
t('str_strip_clean', "`'hello'`", "`.strip()` removes leading and trailing whitespace (or specified characters) and returns a new string.")
t('str_replace_res', "`'a-b-a'`", "`str.replace(old, new, count)` returns a new string because strings are immutable; ignoring the return value leaves the original unchanged.")
t('str_join_call', "`'-'.join(parts)`", '`sep.join(iterable)` is a method on the separator string, taking an iterable of strings.')
t('str_split_call', '`line.split()`', '`str.split()` splits text into a `list` of substrings.')
t('str_find_neg1', '`-1` (returned by `str.find()` when the substring is absent)',
  '`str.find(sub)` returns `-1` on failure, whereas `str.index(sub)` raises `ValueError`.')
t('str_isdigit', '`isdigit()`', '`str.isdigit()` returns `True` when the string is non-empty and every character is a digit.')
t('str_escape_len', 'An escape sequence such as `\\n` or `\\\\` counts as a single character in `len()`',
  'In `"a\\nb"`, the backslash-`n` pair represents one newline character, so `len("a\\nb") == 3`.')

# --- Block 4: Functions, generators, recursion, scope, and exceptions ------
t('fn_def_kw', '`def`', '`def` introduces a function or generator definition.')
t('fn_pos_before_kw', 'Positional arguments must appear before any keyword arguments in a function call',
  'Passing a positional argument after a keyword argument (such as `f(a=1, 2)`) raises `SyntaxError` at parse time.')
t('fn_default_after_req', 'Parameters with default values must follow parameters without default values in `def`',
  'Defining `def f(a=1, b):` is a `SyntaxError` because a non-default parameter cannot follow a default parameter.')
t('fn_mutable_default_shared', '`[1] [1, 2]` (default list is evaluated once at `def` time and shared across calls)',
  'Default parameter expressions are evaluated once when `def` executes, so mutating a default list persists across subsequent calls.')
t('fn_mutable_default_fresh', '`[1] [2]`',
  'A fresh list per call happens only when the function uses `None` as the sentinel default and creates `[]` inside the body.')
t('fn_shadow_local', 'Assigning to a variable inside a function creates a new local name unless `global` is declared',
  'Without `global x`, an assignment `x = ...` inside a function shadows the outer `x` and leaves the module-level variable unchanged.')
t('fn_unbound_local', 'Raises `UnboundLocalError` because assigning to the name later in the function marks it local throughout the body',
  'Reading a variable before assigning to it in the same function (without `global`) raises `UnboundLocalError`, a subclass of `NameError`.')

t('exc_syntax', 'Raises `SyntaxError`',
  '`SyntaxError` is raised by the parser before execution starts when tokens violate Python grammar.')
t('exc_indentation', 'Raises `IndentationError`',
  '`IndentationError` (a subclass of `SyntaxError`) is raised when block indentation is missing or inconsistent.')
t('exc_type', 'Raises `TypeError`',
  '`TypeError` is raised when an operation or function is applied to an object of an inappropriate type, or argument counts mismatch.')
t('exc_value', 'Raises `ValueError`',
  '`ValueError` is raised when an argument has the right type (such as `str`) but an invalid content (such as `int("abc")` or `[].index(9)`).')
t('exc_zero_div', 'Raises `ZeroDivisionError`',
  '`ZeroDivisionError` (a subclass of `ArithmeticError`) is raised by `/`, `//`, or `%` when the right operand is `0` or `0.0`.')
t('exc_index', 'Raises `IndexError`',
  '`IndexError` (a subclass of `LookupError`) is raised when a sequence subscript is out of range (note that slicing out of range never raises `IndexError`).')
t('exc_key', 'Raises `KeyError`',
  '`KeyError` (a subclass of `LookupError`) is raised when `d[k]` looks up a missing dictionary key.')
t('exc_name', 'Raises `NameError`',
  '`NameError` is raised when code references an identifier that has not been bound in local, enclosing, global, or built-in scope.')
t('exc_attr', 'Raises `AttributeError`',
  '`AttributeError` is raised when accessing or calling a method that does not exist on that type (such as `tuple.append`).')
t('exc_recursion', 'Raises `RecursionError`',
  '`RecursionError` is raised when a recursive function lacks a reachable base case and exceeds the maximum call-stack depth.')
t('exc_stop_iter', 'Raises `StopIteration`',
  '`StopIteration` is raised by `next()` when a generator or iterator is exhausted.')

t('hier_base_exc', '`BaseException` sits at the root, with `SystemExit` and `KeyboardInterrupt` inheriting directly from `BaseException` rather than `Exception`',
  '`except Exception:` catches normal runtime errors while allowing `SystemExit` and `KeyboardInterrupt` to propagate cleanly.')
t('hier_lookup', '`LookupError` is the abstract parent class of both `IndexError` and `KeyError`',
  'Catching `LookupError` intercepts both out-of-range sequence subscripts (`IndexError`) and missing dictionary keys (`KeyError`).')
t('hier_arith', '`ArithmeticError` is the abstract parent class of `ZeroDivisionError` and `OverflowError`',
  '`ZeroDivisionError` inherits from `ArithmeticError`, which in turn inherits from `Exception` and `BaseException`.')
t('hier_specific_first', 'Place more specific subclass `except` clauses before broader superclass clauses such as `LookupError` or `Exception`',
  '`except` branches are tested top-to-bottom and only the first matching branch executes, so putting `Exception` first makes later subclass handlers unreachable.')
t('hier_broad_first_trap', 'Only the first matching `except` branch runs, so a leading broad superclass handler swallows subclass exceptions before later branches are checked',
  'Python executes at most one `except` suite per `try` statement, matched in source order.')
t('except_keyword', '`except`', '`except` introduces an exception-handling branch after a `try` suite (Python does not use `catch`).')
t('try_else_runs', 'The `else` branch of `try` runs only when the `try` suite finishes with no exception raised',
  'In `try ... except ... else ... finally`, `else` executes when no exception occurred and `finally` executes unconditionally.')
t('finally_always', '`finally`', '`finally` introduces cleanup code that runs whether or not an exception was raised or returned.')


# --- Additional keywords, operators, and gap-fill tokens -------------------
t('kw_for', '`for`', '`for` introduces definite iteration over any iterable sequence, dictionary, range, or generator.')
t('kw_while', '`while`', '`while` repeats its indented suite as long as its header condition evaluates to truthy.')
t('kw_else', '`else`', '`else` introduces the fallback suite on `if`, `for`, `while`, or `try` blocks.')
t('kw_try', '`try`', '`try` opens an exception-monitored suite that must be followed by at least one `except` or `finally` branch.')
t('kw_from', '`from`', '`from` is a reserved keyword used in `from module import name` and `raise ... from ...`.')
t('kw_import', '`import`', '`import` is a reserved keyword and therefore cannot be used as an ordinary variable name.')
t('kw_class', '`class`', '`class` is a reserved keyword and cannot be used as a variable identifier.')
t('kw_def_reserved', '`def` (reserved keyword)', '`def` is a reserved Python keyword and raises `SyntaxError` if used as a variable name.')

t('op_iadd', '`+=`', 'Augmented addition adds the right-hand value (moving a list in-place or rebinding immutable numbers/strings).')
t('op_isub', '`-=`', 'Augmented subtraction subtracts the right-hand expression from the target variable.')
t('op_imul', '`*=`', 'Augmented multiplication scales a number or repeats a sequence/string.')
t('op_ifloordiv', '`//=`', 'Augmented floor division replaces the variable with its floored quotient.')
t('op_imod', '`%=`', 'Augmented modulo replaces the variable with the remainder after division.')
t('op_assign_single', '`=`', 'A single `=` performs assignment rather than equality comparison (`==`), and is invalid as a plain condition in `if x = 5:`.')
t('op_gt', '`>`', 'Strictly-greater-than relational operator.')
t('op_ge', '`>=`', 'Greater-than-or-equal relational operator.')
t('op_lt', '`<`', 'Strictly-less-than relational operator.')
t('op_le', '`<=`', 'Less-than-or-equal relational operator.')
t('op_is_not', '`is not`', '`is not` evaluates to `True` when two references point to distinct objects (recommended for `x is not None`).')

# --- Additional numeric / float / string / list / dict outputs -------------
t('num_22', '`22`', 'Evaluates to the integer `22`.')
t('num_28', '`28`', 'Evaluates to the integer `28`.')
t('num_35', '`35`', 'Evaluates to the integer `35`.')
t('num_36', '`36`', 'Evaluates to the integer `36`.')
t('num_40', '`40`', 'Evaluates to the integer `40`.')
t('num_48', '`48`', 'Evaluates to the integer `48`.')
t('num_50', '`50`', 'Evaluates to the integer `50`.')
t('num_55', '`55`', 'Evaluates to the integer `55`.')
t('num_60', '`60`', 'Evaluates to the integer `60`.')
t('num_72', '`72`', 'Evaluates to the integer `72`.')
t('num_81', '`81`', 'Evaluates to the integer `81`.')
t('num_120', '`120`', 'Evaluates to the integer `120` (for example `5!`).')
t('num_125', '`125`', 'Evaluates to the integer `125`.')
t('num_neg6', '`-6`', 'Evaluates to the negative integer `-6`.')
t('num_neg7', '`-7`', 'Evaluates to the negative integer `-7`.')
t('num_neg10', '`-10`', 'Evaluates to the negative integer `-10`.')
t('num_neg27', '`-27`', 'Evaluates to `-27` (for example `-3 ** 3`, because `**` binds tighter than unary `-`).')

t('flt_7_0', '`7.0`', 'Evaluates to the floating-point value `7.0`.')
t('flt_8_0', '`8.0`', 'Evaluates to the floating-point value `8.0`.')
t('flt_9_0', '`9.0`', 'Evaluates to the floating-point value `9.0`.')
t('flt_10_0', '`10.0`', 'Evaluates to the floating-point value `10.0`.')
t('flt_12_5', '`12.5`', 'Evaluates to the floating-point value `12.5`.')
t('flt_0_25', '`0.25`', 'Evaluates to the floating-point value `0.25` (for example `2 ** -2`).')
t('flt_0_125', '`0.125`', 'Evaluates to the floating-point value `0.125` (for example `2 ** -3`).')

t('io_out_csv_semi', '`red;green;blue`', 'Passing `sep=";"` joins the three arguments with semicolons.')
t('io_out_pipe_end', '`1|2|3.`', 'Passing `sep="|"` and `end="."` formats delimiters between items and at the end of the call.')
t('io_out_star_join', '`A*B*C`', 'Passing `sep="*"` places an asterisk between consecutive `print()` positional arguments.')
t('io_out_same_line_num', '`1020`', 'Passing `end=""` suppresses the newline so two `print()` calls concatenate directly on one line.')
t('io_out_colon_pair', '`host:8080`', 'Passing `sep=":"` prints the host and port separated by a single colon.')
t('io_out_slash_date', '`2026/10/29`', 'Passing `sep="/"` formats year, month, and day separated by slashes.')

t('out_str_repeat_5', '`55`', '`input()` returns `"5"`, so `"5" * 2` repeats the string into `"55"` rather than computing `10`.')
t('out_str_repeat_4', '`444`', 'Multiplying string `"4"` by integer `3` repeats characters to produce `"444"`.')
t('out_str_aba', "`'ababab'`", "Repeating `'ab' * 3` produces the six-character string `'ababab'`.")
t('out_str_zero_mult', "`''` (multiplying a string by `0` or a negative integer returns an empty string)",
  'Repeating any string `s * n` with `n <= 0` yields `""` without raising an error.')

t('list_10_20', '`[10, 20]`', 'Produces the two-element list `[10, 20]`.')
t('list_20_30_40', '`[20, 30, 40]`', 'Produces the three-element slice `[20, 30, 40]`.')
t('list_40_30_20', '`[40, 30, 20]`', 'Negative-step slicing steps backward from the higher index toward the lower exclusive stop.')
t('list_single_nested', '`[1, 2, [3, 4]]`', '`append([3, 4])` inserts the inner list as one nested element rather than flattening its items.')
t('list_extended_flat', '`[1, 2, 3, 4]`', '`extend([3, 4])` or `+=` iterates the argument and appends each item individually.')
t('list_del_slice', '`[10, 40, 50]`', '`del items[1:3]` removes indices `1` and `2` in place, leaving `[10, 40, 50]`.')
t('list_comp_evens', '`[2, 4, 6]`', 'Selects or computes `[2, 4, 6]` via list comprehension.')
t('list_comp_lengths', '`[3, 4, 2]`', 'Maps `len()` across three short strings in a list comprehension.')
t('list_comp_upper', "`['A', 'B']`", 'Transforms filtered characters to uppercase in a list comprehension.')

t('tup_1_2_3', '`(1, 2, 3)`', 'Evaluates to the three-element tuple `(1, 2, 3)`.')
t('tup_concat_4', '`(1, 2, 3, 4)`', 'Concatenating tuples with `+` builds a new tuple `(1, 2, 3, 4)`.')
t('tup_repeat_0', '`(0, 0, 0)`', 'Repeating a single-element tuple `(0,) * 3` produces `(0, 0, 0)`.')
t('tup_unpack_swap', '`20 10`', 'Tuple assignment `a, b = b, a` evaluates the right-hand side first and swaps bindings cleanly.')

t('str_slice_mid', "`'tho'`", "Evaluates to the three-character slice `'tho'`.")
t('str_slice_tail', "`'on'`", "Negative start `[-2:]` extracts the final two characters `'on'`.")
t('str_title_res', "`'Log Error'`", "`.title()` capitalizes the first letter of each word and lowercases the rest.")
t('str_lower_res', "`'warn'`", "`.lower()` returns a new lowercase copy of the string.")
t('str_count_2', '`2` (non-overlapping occurrences counted by `str.count()`)',
  '`str.count(sub)` counts *non-overlapping* occurrences, so `"aaaa".count("aa")` is `2`, not `3`.')
t('str_startswith_fn', '`startswith()`', '`str.startswith(prefix)` checks whether a string begins with `prefix` without manual slicing.')
t('str_endswith_fn', '`endswith()`', '`str.endswith(suffix)` checks whether a string ends with `suffix`.')
t('str_isalpha_fn', '`isalpha()`', '`str.isalpha()` returns `True` only when the string is non-empty and all characters are alphabetic.')

t('gen_list_012', '`[0, 1, 2]`', 'Consuming the generator with `list(...)` collects every yielded value until exhaustion.')
t('gen_list_1_4_9', '`[1, 4, 9]`', 'Collecting yielded squares from the generator produces `[1, 4, 9]`.')
t('gen_exhausted_empty', '`[]` (a generator iterator can only be consumed once; a second `list(g)` is empty)',
  'Once a generator reaches exhaustion, subsequent iterations over the same generator object yield zero items.')

t('exc_unbound_short', 'Raises `UnboundLocalError`',
  'Assigning to a name anywhere in a function makes it local across the whole function, so reading it earlier raises `UnboundLocalError`.')
t('exc_overflow', 'Raises `OverflowError`',
  '`OverflowError` is a concrete subclass of `ArithmeticError` raised when a floating-point result exceeds representable range.')
t('exc_sys_exit_parent', '`SystemExit` inherits directly from `BaseException`, not from `Exception`',
  'Because `SystemExit` bypasses `Exception`, a standard `except Exception:` block will not accidentally trap `sys.exit()`.')
t('exc_kbd_parent', '`KeyboardInterrupt` inherits directly from `BaseException`, not from `Exception`',
  '`KeyboardInterrupt` sits directly under `BaseException` so user Ctrl-C interrupts are not swallowed by `except Exception:`.')
t('exc_val_under_exc', '`ValueError` inherits directly from `Exception` (not `LookupError` or `ArithmeticError`)',
  '`ValueError` is a sibling of `TypeError`, `LookupError`, and `ArithmeticError` under `Exception`.')
t('exc_type_under_exc', '`TypeError` inherits directly from `Exception`',
  '`TypeError` sits under `Exception` rather than under `LookupError` or `SyntaxError`.')
t('exc_index_under_lookup', '`IndexError` is a direct subclass of `LookupError`',
  '`LookupError` groups `IndexError` and `KeyError` under `Exception`.')
t('exc_key_under_lookup', '`KeyError` is a direct subclass of `LookupError`',
  'Catching `LookupError` handles `KeyError` as well as `IndexError`.')
t('exc_zero_under_arith', '`ZeroDivisionError` is a direct subclass of `ArithmeticError`',
  '`ArithmeticError` is the parent class of `ZeroDivisionError`, `OverflowError`, and `FloatingPointError`.')


# --- Multi-select expression & snippet options -----------------------------
t('str_nonempty_zero', "`'0'`", "A non-empty string `'0'` has length `1` and therefore evaluates to `True` in Boolean contexts.")
t('str_nonempty_false', "`'False'`", "Any non-empty string, including `'False'`, is truthy in Python; only `''` is a falsy string.")
t('list_with_zero', '`[0]`', 'A one-element list `[0]` has length `1` and is truthy even though its element `0` is falsy.')
t('bool_expr_chained', '`10 <= x <= 20`', 'Python supports chained comparisons equivalent to `(10 <= x) and (x <= 20)` with `x` evaluated once.')
t('bool_expr_and_range', '`(x >= 10) and (x <= 20)`', 'Combining two relational checks with `and` requires both bounds to hold.')
t('bool_expr_or_wrong', '`(x >= 10) or (x <= 20)`', 'Using `or` here is `True` for *every* number (for example `x = 99` satisfies `x >= 10`).')
t('bool_expr_bitwise_trap', '`10 <= x & x <= 20`', 'Bitwise `&` binds tighter than `<=`, so `10 <= x & x <= 20` parses as `10 <= (x & x) <= 20` rather than logical `and`.')
t('bool_expr_assign_err', '`x >= 10 and x = 20`', 'Single `=` is assignment rather than comparison and raises `SyntaxError` inside a Boolean expression.')

t('range_odd_1_6', '`range(1, 6, 2)`', '`range(1, 6, 2)` produces `1, 3, 5` (three iterations).')
t('range_three_zeros', '`range(0, 3)`', '`range(0, 3)` produces `0, 1, 2` (three iterations).')
t('range_neg_three', '`range(3, 0, -1)`', '`range(3, 0, -1)` counts down `3, 2, 1` (three iterations).')
t('range_four_inclusive_trap', '`range(1, 3)`', '`range(1, 3)` stops before `3` and yields only `1, 2` (two iterations, not three).')
t('range_wrong_dir', '`range(0, 3, -1)`', 'Starting at `0` with stop `3` and step `-1` moves away from `3` and yields zero iterations.')

t('else_runs_exhausted', 'When a `for` loop consumes every item in its iterable without hitting `break`',
  'Normal exhaustion of a `for` iterable runs the attached `else` suite.')
t('else_runs_false_cond', 'When a `while` condition initially or eventually evaluates to `False` without `break`',
  'A `while` loop whose condition turns `False` (even on the very first check) executes its `else` suite.')
t('else_skips_break', 'When `break` terminates the loop early before the condition turns `False`',
  '`break` bypasses the loop `else` suite completely.')
t('else_skips_return', 'When `return` exits the enclosing function from inside the loop body',
  'Returning out of the function exits both the loop and any attached `else` suite.')
t('else_skips_exc', 'When an unhandled exception aborts the loop body',
  'An unhandled exception unwinds the stack rather than running the loop `else` clause.')

t('copy_slice_full', '`b = a[:]`', 'Full-slice notation `a[:]` creates a new shallow copy of list `a`.')
t('copy_method_call', '`b = a.copy()`', '`list.copy()` allocates a new shallow copy of `a`.')
t('copy_list_ctor', '`b = list(a)`', 'Passing `a` to `list(a)` constructs a distinct outer list with the same element references.')
t('copy_alias_assign', '`b = a`', 'Plain assignment `b = a` creates an alias to the exact same list object rather than copying.')
t('copy_extend_self', '`b = a.sort()`', '`a.sort()` sorts `a` in place and assigns `None` to `b`.')

t('tup_lit_trailing_comma', '`t = 5,`', 'A trailing comma without parentheses packs a single-element tuple `(5,)`.')
t('tup_ctor_iterable', '`t = tuple([5])`', '`tuple([5])` converts a one-element list into the one-element tuple `(5,)`.')
t('tup_empty_call', '`t = tuple()`', '`tuple()` with no arguments returns the empty tuple `()`.')
t('tup_bad_int_call', '`t = tuple(5)`', '`tuple()` expects an iterable, so passing an integer `5` raises `TypeError`.')

t('dict_check_in', "`'host' in cfg`", 'The `in` operator on a dictionary checks membership among its *keys* in O(1) average time.')
t('dict_check_keys', "`'host' in cfg.keys()`", 'Checking membership against `cfg.keys()` tests whether the key exists without raising `KeyError`.')
t('dict_check_get_trap', "`cfg['host']` without `try`", 'Direct subscripting `cfg[k]` raises `KeyError` immediately when `k` is missing.')
t('dict_check_values_trap', "`'host' in cfg.values()`", '`cfg.values()` searches dictionary *values*, not dictionary keys.')

t('str_meth_immut_new', 'Every string transformation method returns a brand-new `str` object and leaves the original string unchanged',
  'Because `str` is immutable in Python, methods like `.upper()`, `.replace()`, and `.strip()` never mutate in place.')
t('str_slice_safe', 'Out-of-range string slice bounds such as `s[2:99]` clamp silently instead of raising `IndexError`',
  'Slicing clamps start and stop indices to valid string bounds, whereas out-of-range single-index `s[99]` raises `IndexError`.')
t('str_item_assign_err', 'Assigning `s[0] = "X"` mutates the first character of `s` in place',
  '`str` does not support item assignment; `s[0] = "X"` raises `TypeError`.')
t('str_del_char_err', 'Running `del s[0]` deletes the first character from `s` in place',
  '`str` is immutable, so `del s[0]` raises `TypeError`.')

t('call_pos_then_kw', '`calc(10, rate=2)`', 'Positional arguments precede keyword arguments and bind each parameter once.')
t('call_all_kw_swapped', '`calc(rate=2, base=10)`', 'Keyword arguments may appear in any order as long as parameter names match and none are duplicated.')
t('call_kw_before_pos_err', '`calc(base=10, 2)`', 'A positional argument after a keyword argument is a `SyntaxError`.')
t('call_dup_param_err', '`calc(10, base=5)`', 'Passing `base` both positionally and by keyword raises `TypeError: got multiple values for argument`.')
t('call_unknown_kw_err', '`calc(10, tax=2)`', 'Passing an unexpected keyword argument raises `TypeError` when the function has no `**kwargs`.')

t('ret_none_bare', 'A function executing a bare `return` statement evaluates to `None` at the call site',
  'Bare `return` exits immediately and returns the singleton `None`.')
t('ret_none_falloff', 'A function that reaches the end of its body without any `return` statement returns `None`',
  'Falling off the end of a Python function implicitly returns `None`.')
t('ret_tuple_pack', 'Writing `return a, b` returns a single `tuple` `(a, b)` that the caller can unpack',
  'Comma-separated expressions after `return` pack a `tuple` object.')
t('ret_after_yield_gen', 'Adding `yield` anywhere in a function body makes calling it return a generator object instead of running the body immediately',
  'Presence of `yield` compiles the function as a generator factory.')
t('ret_multi_runs_all', 'Multiple `return` lines in the same branch all execute sequentially and concatenate their results',
  'The first `return` executed exits the function immediately; subsequent statements in that block are unreachable.')


# --- Set 2-6 additional options --------------------------------------------
t('comp_pros_speed', 'Ahead-of-time compilation translates the entire program into native machine instructions once before execution',
  'A compiler translates the whole program ahead of time into target machine code rather than interpreting source on each run.')
t('interp_portability', 'An interpreter executes source cross-platform wherever a compatible Python runtime is installed without recompiling per CPU',
  'Interpreted Python scripts run unchanged across operating systems that provide the matching Python interpreter.')
t('comp_needs_source_user', 'Compiled native binaries require every end user to keep the original C compiler installed to launch the binary',
  'A compiled standalone executable runs directly on the target OS without shipping the compiler.')
t('interp_hides_source', 'Standard `.py` interpretation encrypts source code into irreversible machine instructions so users cannot read it',
  '`.py` files are plain text and `.pyc` bytecode can be disassembled; interpretation does not encrypt source.')

t('syntax_err_unclosed', 'Leaving an unclosed parenthesis in `print("WARN"` violates syntax and stops the file before any line runs',
  'Unbalanced delimiters break Python grammar rules during the parsing phase before line 1 executes.')
t('lexis_err_bad_token', 'Writing `@$` as an expression violates lexis because `@$` is not a valid token in Python vocabulary',
  'When characters cannot be grouped into legal Python tokens, lexical analysis rejects the source.')

t('str_err', "`'ERR'`", "Evaluates to the non-empty string `'ERR'`; `or` returns its first truthy operand directly rather than converting it to `True`.")
t('kw_assert_or_from', '`from`', '`from` is a reserved keyword used in import and exception-chaining statements.')

t('lit_sci_small', '`2.5e-2`', '`2.5e-2` is valid scientific notation representing `0.025` as a `float`.')
t('lit_oct_zero', '`0o77`', '`0o77` is a valid base-8 integer literal equal to `63` in decimal.')
t('lit_hex_bad_g', '`0x1G`', '`G` is outside hexadecimal digits `0-9` and `A-F`, so `0x1G` raises `SyntaxError`.')

t('op_neg_floordiv_res', '`-4`', '`-7 // 2` rounds `-3.5` down toward negative infinity to `-4`, not `-3`.')

t('bool_de_morgan_1', '`not (a or b)`', 'By De Morgan law, `not (a or b)` is True exactly when both `a` and `b` are falsy.')
t('bool_de_morgan_2', '`(not a) and (not b)`', 'Requiring both `not a` and `not b` is logically equivalent to `not (a or b)`.')
t('bool_de_morgan_trap_or', '`(not a) or (not b)`', '`(not a) or (not b)` is equivalent to `not (a and b)`, which still allows one operand to be truthy.')
t('bool_not_b_trap', '`not a or b`', 'Because `not` binds tighter than `or`, `not a or b` parses as `(not a) or b`.')

t('list_mut_append_none', '`items.append(x)` mutates `items` in place and evaluates to `None`',
  'In-place list mutators (`append`, `extend`, `insert`, `remove`, `sort`, `reverse`) return `None` except `pop()`.')
t('list_mut_pop_returns', '`items.pop()` removes the final element in place and returns that removed element',
  '`pop()` both mutates the list and returns the removed value so callers can inspect it.')
t('list_mut_sorted_inplace', '`sorted(items)` mutates `items` in place and returns `None`',
  '`sorted()` is a built-in function that returns a *new* sorted list without modifying `items`.')
t('list_mut_remove_all', '`items.remove(x)` deletes every occurrence of `x` across the entire list in one call',
  '`list.remove(x)` deletes only the *first* matching occurrence of `x`.')
t('list_mut_insert_tail', '`items.insert(0, x)` appends `x` after the last element of `items`',
  '`insert(0, x)` places `x` at the *front* (index `0`), shifting existing elements right.')

t('tup_immut_no_assign', 'Assigning `t[0] = 9` on a tuple raises `TypeError` because tuple slot bindings are immutable',
  'Tuples do not support item assignment or item deletion.')
t('tup_slice_returns_tuple', 'Slicing a tuple such as `t[1:3]` returns a new `tuple` containing those elements',
  'Slicing a tuple produces another tuple rather than converting it to a list.')
t('tup_append_ok_myth', 'Calling `t.append(9)` adds an element to the end of tuple `t` in place',
  '`tuple` has no `.append()` method; calling it raises `AttributeError`.')
t('tup_del_slot_myth', 'Running `del t[0]` removes the first element while keeping the same tuple object',
  '`del t[0]` raises `TypeError` because tuples are immutable; only `del t` (unbinding the whole variable) is legal.')

t('dict_iter_bare_keys', 'Iterating `for x in d:` yields each dictionary key in insertion order',
  'Iterating directly over a `dict` iterates over its keys, identical to `for x in d.keys():`.')
t('dict_iter_items_pairs', 'Iterating `for k, v in d.items():` unpacks each `(key, value)` pair cleanly',
  '`d.items()` yields 2-tuples pairing each key with its mapped value.')
t('dict_iter_bare_pairs_myth', 'Iterating `for k, v in d:` unpacks keys and values directly without calling `.items()`',
  'Iterating bare `d` yields keys alone, so `for k, v in d:` fails unless the keys themselves happen to be 2-element iterables.')
t('dict_iter_values_pairs_myth', 'Iterating `for k, v in d.values():` yields `(key, value)` tuples for every entry',
  '`d.values()` yields only the mapped values, not `(key, value)` pairs.')

t('fn_def_default_valid_1', '`def connect(host, port=5432):`', 'Required parameter `host` precedes defaulted parameter `port=5432`, which is valid Python syntax.')
t('fn_def_default_valid_2', '`def connect(host="localhost", port=5432):`', 'Every parameter may carry a default value when no non-default parameter follows.')
t('fn_def_default_bad_order', '`def connect(host="localhost", port):`', 'Placing required parameter `port` after defaulted `host="localhost"` raises `SyntaxError`.')
t('fn_def_dup_param', '`def connect(host, host=80):`', 'Duplicate parameter names in a `def` signature raise `SyntaxError`.')
t('fn_def_lit_param', '`def connect("localhost", port=80):`', 'Function parameters in `def` must be identifiers, never string literals.')

t('exc_order_zero_before_arith', 'Place `except ZeroDivisionError:` above `except ArithmeticError:` so division by zero reaches the specific handler',
  'Because `ZeroDivisionError` is a subclass of `ArithmeticError`, putting `ZeroDivisionError` first lets both handlers stay reachable.')
t('exc_order_key_before_lookup', 'Place `except KeyError:` above `except LookupError:` so missing dictionary keys hit the `KeyError` branch',
  '`KeyError` inherits from `LookupError`, so the narrower handler must appear earlier.')
t('exc_order_exc_first_trap', 'Place `except Exception:` first and `except ValueError:` second so `ValueError` overrides the general handler',
  'Putting `except Exception:` first catches `ValueError` immediately and makes the later `except ValueError:` dead code.')
t('exc_bare_before_named_trap', 'Place a bare `except:` clause above `except TypeError:` as a fallback default',
  'A bare `except:` must always be the *last* `except` clause in Python 3; placing it earlier is a `SyntaxError`.')
t('exc_runs_all_matching_trap', 'Python runs every `except` clause whose class matches the raised exception from top to bottom',
  'At most *one* `except` branch executes for a single raised exception.')


# --- Set 3-6 targeted terms ------------------------------------------------
t('lexis_syntax_pair_1', 'Lexis checks that each individual token is legal, whereas syntax checks how tokens are arranged into statements',
  'Lexical analysis validates vocabulary tokens; syntactic analysis validates statement grammar.')
t('lexis_syntax_pair_2', 'Semantics determines runtime meaning, so `10 / 0` passes lexis and syntax yet fails at runtime',
  'A statement can be lexically and syntactically valid while still failing semantically during execution.')
t('lexis_runtime_only_myth', 'Lexis runs only after the program finishes printing its output',
  'Tokenization happens before bytecode compilation and execution.')

t('num_99', '`99`', 'Evaluates to the integer `99`.')
t('list_rev_skus', '`[104, 103, 102, 101]`', 'Slicing `[::-1]` returns a reversed shallow copy of the four-element list.')

t('str_quote_double_wrap', """`"Item's price"`""",
  'Wrapping a string in double quotes lets an apostrophe appear inside without a backslash.')
t('str_quote_escaped_single', r"""`'Item\'s price'`""",
  r'Escaping the inner single quote with `\` keeps a single-quoted string literal valid.')
t('str_quote_unescaped_err', r"""`'Item's price'`""",
  'An unescaped apostrophe inside single quotes terminates the literal early and raises `SyntaxError`.')
t('str_quote_mismatch_err', r"""`"Item price'`""",
  'Opening with `"` and closing with an apostrophe leaves the string literal unterminated and raises `SyntaxError`.')
t('str_quote_trailing_bs_err', r"""`'C:\temp\'`""",
  'A trailing single backslash escapes the closing quote itself, causing `SyntaxError: unterminated string literal`.')

t('scope_mutate_list_ok', 'Mutating an element via `rates[0] = 99` inside a function modifies the global list in place without needing `global rates`',
  'Item assignment `rates[0] = ...` mutates the existing list object rather than rebinding the identifier `rates`.')
t('scope_read_outer_ok', 'Reading a module-level variable inside a function works directly as long as the function never assigns to that same name',
  'Functions look up unassigned names in enclosing and global scopes automatically (LEGB).')
t('scope_rebind_needs_global_trap', 'Rebinding `rates = []` inside a function without `global rates` clears the module-level `rates` variable for all callers',
  'Plain assignment `rates = []` binds a brand-new local variable and leaves module-level `rates` untouched.')
t('scope_param_is_global_trap', 'Function parameter names are automatically registered in module-level global scope when the function returns',
  'Parameters are local variables of the function call frame and disappear when the frame exits.')


t('list_18_24', '`[18, 24]`', 'Slicing `temps[1:4:2]` selects index `1` (`18`) and index `3` (`24`).')
t('list_10_20_30', '`[10, 20, 30]`', 'Inserting `20` at index `1` into `[10, 30]` yields `[10, 20, 30]`.')


t('num_88', '`88`', 'Evaluates to the integer `88`.')
t('list_65_70', '`[65, 70]`', 'Slicing `marks[:2]` takes indices `0` and `1`, stopping before exclusive index `2`.')
t('list_75_80_85', '`[75, 80, 85]`', 'Slicing `marks[-3:]` collects the final three elements through the end of the list.')
t('list_5_10_8', '`[5, 10, 8]`', '`scores.remove(10)` removes only the *first* matching `10` at index `0`, leaving the later `10` intact.')


t('list_9_12_15', '`[9, 12, 15]`', 'Slicing `hours[1:-1]` drops the first (`0`) and last (`-1`) elements.')
t('list_18_12_6', '`[18, 12, 6]`', 'Slicing `hours[::-2]` steps backward by `2` starting from the final element.')
t('list_12_15', '`[12, 15]`', 'Selects elements `>= 10` from `[6, 9, 12, 15]` in order.')
