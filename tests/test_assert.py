# type: ignore
value = True
other = False
count: int = 5


class _Obj:
    attr: bool = True


obj = _Obj()


def get_value() -> bool:
    return False


# -- name --
assert value

assert value is True


# -- call --
assert get_value()

assert get_value() is True


# -- attribute --
assert obj.attr

assert obj.attr is True


# -- not + name --
assert not value

assert value is False


# -- not + compare --
assert not (count > 0)


# -- bool constants --
assert True

assert False


# -- comparisons --
assert count > 0

assert count != 0


# -- and --
assert value and other

assert count > 0 and count < 10


# -- or --
assert value or other

assert value is True or other is True
