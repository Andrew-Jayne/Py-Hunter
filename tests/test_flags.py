#!/usr/bin/env python3
"""Test file for --disallow-lambda and --no-if-in-match flags."""

# ========== LAMBDAS ==========
# These are all fine lambdas (unless --disallow-lambda is used)
identity = lambda x: x
doubler = lambda x: x * 2
checker = lambda x: x > 0
transform = lambda x, y: x + y

# Problematic lambdas (always flagged for implicit booleans)
bad_lambda1 = lambda x: x and y
bad_lambda2 = lambda x: not x


# ========== MATCH/CASE (Python 3.10+) ==========
def process_value(value):
    match value:
        # Guard with explicit comparison (OK normally, but not with --no-if-in-match)
        case x if x > 0:
            return f"positive: {x}"

        # Guard with implicit boolean (always bad)
        case x if x:
            return f"truthy: {x}"

        # Another explicit guard
        case [first, *rest] if len(rest) > 0:
            return f"list with multiple items"

        # Implicit guard
        case [first, *rest] if rest:
            return f"list with rest"

        # No guard (always fine)
        case None:
            return "got None"

        case _:
            return "default"


# ========== REGULAR CODE ==========
# Normal implicit boolean (always flagged)
items = []
if items:
    pass

# List comprehension (always flagged)
filtered = [x for x in range(10) if x > 5]

print("Testing flags...")
