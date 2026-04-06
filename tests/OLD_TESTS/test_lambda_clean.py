#!/usr/bin/env python3
"""Test that clean lambdas are NOT flagged."""

# These lambdas should NOT be flagged (they're fine!)
identity = lambda x: x  # Identity function - fine
doubler = lambda x: x * 2  # Math operation - fine
upper = lambda s: s.upper()  # String method - fine
getter = lambda x: x.value  # Attribute access - fine
indexer = lambda x: x[0]  # Indexing - fine
caller = lambda x: len(x)  # Function call - fine
comparison = lambda x: x > 5  # Explicit comparison - fine

# These lambdas SHOULD be flagged (problematic patterns)
bool_and = lambda x, y: x and y  # Implicit boolean
bool_or = lambda x, y: x or y  # Implicit boolean
bool_not = lambda x: not x  # Implicit boolean
ternary_implicit = lambda x: x if x else 0  # Implicit condition in ternary
list_comp = lambda items: [x for x in items]  # Contains list comprehension
dict_comp = lambda pairs: {k: v for k, v in pairs}  # Contains dict comprehension

print("Testing clean vs problematic lambdas...")
