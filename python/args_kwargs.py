# *-operator: sequential unpack operator

def multiply_accumulate(a, b, c):
    return a+b*c

t = (1, 2, 3)

multiply_accumulate(t[0], t[1], t[2])
# > 9

multiply_accumulate(*t)
# > 9


# ---------------------------------------------------------------------------------------


def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

add(1, 2, 3, 4)
# > 10


# ---------------------------------------------------------------------------------------


def f0(c, *args):
    print(c)
    print(args)

f0(1, 2)
# > 1
# > (2,)

def f1(*args, c):
    print(args)
    print(c)


f1(1, c)
# > f1() missing 1 required keyword-only argument: 'c'

f1(1, c=2)
# > (1,)
# > 2


# ---------------------------------------------------------------------------------------


def f2(*a, *b):
  print(a)
  print(b)

# > SyntaxError: * argument may appear only once


# ---------------------------------------------------------------------------------------


def print_parameters(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}->{v}")

print_parameters(a=1, b=2, c=3)
# > a->1
# > b->2
# > c->3


# ---------------------------------------------------------------------------------------


def f3(a, b, c, *args, **kwargs)
    print(f"a->{a}")
    print(f"b->{b}")
    print(f"c->{c}")
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(f"{k}->{v}")

f3(1,2,3, 4, 6, f=5, g=7)
# > a->1
# > b->2
# > c->3
# > 4
# > 6
# > f->5
# > g->7


# ---------------------------------------------------------------------------------------


def f4(**kwargs, *args):
    ...
# > SyntaxError: arguments cannot follow var-keyword argument


# ---------------------------------------------------------------------------------------


def f5(a, b, c):
    print(a)
    print(b)
    print(c)

d = {'a':1, 'b':2, 'c':3}

f5(**d)
# > 1
# > 2
# > 3


# ---------------------------------------------------------------------------------------


def f6(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}->{v}")

d = {'a':1, 'b':2, 'c':3}

f6(**d)
# > a->1
# > b->2
# > c->3


# ---------------------------------------------------------------------------------------


def f7(a, b, **kwargs):
    print(a)
    print(b)
    for k, v in kwargs.items():
        print(f"{k}->{v}")

d = {'a':1, 'b':2, 'c':3}

f7(**d)
# > 1
# > 2
# > c->3
