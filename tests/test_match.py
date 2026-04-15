# type: ignore
value = True
count: int = 5


# ── default mode: guards checked for implicit booleans ──────────────────────

# -- implicit guard (name) --
match count:
    case _ if count:
        pass
    case _:
        pass

match count:
    case _ if count > 0:
        pass
    case _:
        pass


# -- implicit guard (not + name) --
match count:
    case _ if not count:
        pass
    case _:
        pass

match count:
    case _ if not (count > 0):
        pass
    case _:
        pass


# -- no guard --
match count:
    case _ :
        pass


# -- and --
match count:
    case _ if count and value:
        pass
    case _:
        pass

match count:
    case _ if count > 0 and count < 10:
        pass
    case _:
        pass


# ── --disallow-logic-in-match: all guards banned ─────────────────────────────
# any guard is flagged regardless of explicit vs implicit
# the right pattern is to move the condition into the case body

match count:
    case _ if count > 0:  # flagged with --disallow-logic-in-match
        pass
    case _:
        pass

match count:
    case _:
        if count > 0:  # clean: logic moved into body
            pass
