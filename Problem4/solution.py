def make_predicate(func):
    def condition(*args, **kwargs):
        return predicate(lambda arg: func(arg, *args, **kwargs))
    return condition

class predicate:
    def __init__(self, func):
        self._condition = func

    def __call__(self, arg):
        return self._condition(arg)

    __and__ = make_predicate(lambda arg, self, other: self(arg) and other(arg))
    __or__ = make_predicate(lambda arg, self, other: self(arg) or other(arg))
    __invert__ = make_predicate(lambda arg, self: not self(arg))
    __rshift__ = make_predicate(lambda arg, self, other: other(arg) if
            self(arg) else True)

gt = make_predicate(lambda arg, condition: arg > condition)
lt = make_predicate(lambda arg, condition: arg < condition)
eq = make_predicate(lambda arg, condition: arg == condition)
oftype = make_predicate(lambda arg, _type: isinstance(arg, _type))
present = make_predicate(lambda arg: arg != None)
pred = make_predicate(lambda arg, func: func(arg))
for_any = make_predicate(lambda arg, *predicates: any((pred(arg) for pred in predicates)))
for_all = make_predicate(lambda arg, *predicates: all((pred(arg) for pred in predicates)))
