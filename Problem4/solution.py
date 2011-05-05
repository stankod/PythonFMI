def make_predicate(func):
    def condition(*args):
        return predicate(lambda arg: func(arg, *args))
    return condition

class predicate:
    def __init__(self, func):
        self._condition = func

    def __call__(self, arg):
        return self._condition(arg)

    def __and__(self, other):
        return predicate(lambda arg: self(arg) and other(arg))

    def __or__(self, other):
        return predicate(lambda arg: self(arg) or other(arg))

    def __invert__(self):
        return predicate(lambda arg: not self(arg))

    def __rshift__(self, other):
        return predicate(lambda arg: other(arg) if self(arg) else True)

gt = make_predicate(lambda arg, condition: arg > condition)
lt = make_predicate(lambda arg, condition: arg < condition)
eq = make_predicate(lambda arg, condition: arg == condition)
oftype = make_predicate(lambda arg, _type: isinstance(arg, _type))
present = make_predicate(lambda arg: arg != None)
pred = make_predicate(lambda arg, func: func(arg))
for_any = make_predicate(lambda arg, *predicates: any((pred(arg) for pred in predicates)))
for_all = make_predicate(lambda arg, *predicates: all((pred(arg) for pred in predicates)))
