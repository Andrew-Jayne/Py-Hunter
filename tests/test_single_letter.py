# type: ignore
# -- function names --
def f():
    pass

def func():
    pass


# -- function parameters --
def func_with_args(x):
    pass

def func_with_args(param):
    pass


# -- async function --
async def g():
    pass

async def handler():
    pass


# -- class names --
class C:
    pass

class Counter:
    pass


# -- variable assignment --
x = 1

var = 1


# -- annotated assignment --
y: int = 2

count: int = 2


# -- loop variables --
for i in range(10):
    pass

for item in range(10):
    pass


# -- tuple unpacking --
a, b = 1, 2

first, second = 1, 2


# -- multiple assignment --
x = y = 0

val = result = 0


# -- exception handler --
try:
    pass
except Exception as e:
    pass

try:
    pass
except Exception as err:
    pass


# -- walrus operator --
if (n := 5) > 0:
    pass

if (result := 5) > 0:
    pass


# -- underscore excluded (standard for throwaway) --
for _ in range(10):
    pass

_ = "throwaway"
