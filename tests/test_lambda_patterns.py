#!/usr/bin/env python3
"""Test lambda patterns that should be flagged."""

# ========== LAMBDAS WITH IMPLICIT BOOLEANS ==========

# Lambda with just implicit boolean (common in filter)
numbers = [0, 1, 2, 0, 3, 0]
filtered = filter(lambda x: x, numbers)  # should flag: implicit x

# Lambda with implicit boolean in map
items = [[], [1], [], [2, 3]]
lengths = map(lambda x: len(x) if x else 0, items)  # should flag: implicit x in ternary

# Lambda with boolean operations
checker = lambda x, y: x and y  # should flag: x and y are implicit

# Lambda with not
negator = lambda x: not x  # should flag: implicit not x

# ========== LAMBDAS WITH COMPREHENSIONS (EVIL!) ==========

# Lambda returning list comprehension
list_maker = lambda items: [x for x in items if x > 0]  # should flag the comprehension

# Lambda with nested comprehension
matrix_processor = lambda m: [
    [val * 2 for val in row] for row in m
]  # should flag both comprehensions

# Lambda with dict comprehension
dict_maker = lambda pairs: {
    k: v for k, v in pairs if v
}  # should flag dict comp AND implicit v

# ========== LAMBDAS THAT SHOULD BE OK ==========

# Lambda with explicit comparison
comparator = lambda x: x > 0  # OK - explicit comparison

# Lambda with isinstance check (needs is True, but that's a different issue)
type_checker = lambda x: isinstance(x, int) is True  # OK - explicit is True

# Lambda doing math (not a boolean check)
doubler = lambda x: x * 2  # OK - not a boolean context

# Lambda with explicit None check
none_checker = lambda x: x is not None  # OK - explicit comparison

print("Testing lambda patterns...")
