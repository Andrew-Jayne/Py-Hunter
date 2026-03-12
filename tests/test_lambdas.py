#!/usr/bin/env python3
"""Test that lambda functions themselves are flagged, not just their contents."""

# Lambda assigned to variable (should be flagged as lazy)
checker = lambda x: x > 0

# Lambda with implicit bool in body
truthy_check = lambda x: x if x else None

# Lambda in sorted() key
items = ["", "a", "bb", "ccc"]
sorted_items = sorted(items, key=lambda x: len(x))

# Multiple lambdas in one statement
operations = {
    "double": lambda x: x * 2,
    "square": lambda x: x**2,
    "check": lambda x: x if x > 0 else 0,
}

# Lambda in map/filter/reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]

mapped = map(lambda x: x * 2, numbers)
filtered = filter(lambda x: x > 2, numbers)
reduced = reduce(lambda x, y: x + y, numbers)

# IIFE (Immediately Invoked Function Expression) with lambda
result = (lambda x: x * 2)(5)

# Nested lambdas (extra evil)
nested = lambda x: lambda y: x + y

# Lambda returning lambda
curry = lambda x: lambda y: lambda z: x + y + z

print("Lambdas are just lazy one-liner functions!")
