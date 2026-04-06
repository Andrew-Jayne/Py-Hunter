#!/usr/bin/env python3
"""Test file to check what comprehension patterns are caught."""

# List comprehensions with implicit boolean filters
numbers = [1, 2, 0, 3, 0, 4]
items = ["", "hello", None, "world", False]

# These should be flagged (implicit boolean in filter)
filtered1 = [x for x in numbers if x]  # implicit: if x
filtered2 = [x for x in items if not x]  # implicit: if not x
filtered3 = [x for x in items if x and len(x) > 2]  # implicit: if x and ...

# These should NOT be flagged (explicit comparisons)
filtered4 = [x for x in numbers if x > 0]  # explicit comparison
filtered5 = [x for x in items if x is not None]  # explicit comparison
filtered6 = [x for x in items if isinstance(x, str) is True]  # explicit with is True

# Dict comprehensions
data = {"a": 1, "b": 0, "c": 3, "d": None}

# Should be flagged
dict1 = {k: v for k, v in data.items() if v}  # implicit: if v
dict2 = {k: v for k, v in data.items() if not v}  # implicit: if not v

# Should NOT be flagged
dict3 = {k: v for k, v in data.items() if v is not None}  # explicit
dict4 = {k: v for k, v in data.items() if v > 0}  # explicit comparison

# Set comprehensions
set1 = {x for x in numbers if x}  # should be flagged
set2 = {x for x in numbers if x != 0}  # should NOT be flagged

# Generator expressions
gen1 = (x for x in numbers if x)  # should be flagged
gen2 = (x for x in numbers if x > 0)  # should NOT be flagged

# Nested comprehensions
matrix = [[1, 0, 2], [0, 3, 0], [4, 0, 5]]
nested1 = [[val for val in row if val] for row in matrix]  # inner if should be flagged
nested2 = [[val for val in row if val > 0] for row in matrix]  # should NOT be flagged

# Comprehensions without filters (these are NOT checked currently)
simple_list = [x * 2 for x in numbers]  # no filter, not checked
simple_dict = {k: v * 2 for k, v in data.items()}  # no filter, not checked
simple_set = {x * 2 for x in numbers}  # no filter, not checked
