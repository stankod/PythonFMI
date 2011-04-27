#-*- coding: utf-8 -*-
from types import FunctionType
from numbers import Number
import operator

class Lazy(Number):
    """
    Implementation of a number with delayed arithmetic operations

    some_number = Lazy(10) / Lazy(2) # the operation is not applied
    print(some_number) # 5
    """
    def __init__(self, num):
        self._number = num

    @staticmethod
    def _get_value(num):
        "Extract the value of a lazy (or another) number"
        if isinstance(num, FunctionType):
            return num()
        if isinstance(num, Lazy):
            return num.force()
        return num

    def _delay_operation(operation, reflected = False):
        def lazy_operation(self, other = None):
            def computation():
                arg1 = Lazy._get_value(self)
                arg2 = Lazy._get_value(other)
                if arg2 == None:
                    return operation(arg1)
                if reflected:
                    arg1, arg2 = arg2, arg1
                return operation(arg1, arg2)
            return Lazy(computation)
        return lazy_operation

    __add__ = _delay_operation(operator.add)
    __radd__ = _delay_operation(operator.add, True)
    __sub__ = _delay_operation(operator.sub)
    __rsub__ = _delay_operation(operator.sub, True)
    __mul__ = _delay_operation(operator.mul)
    __rmul__ = _delay_operation(operator.mul, True)
    __truediv__ = _delay_operation(operator.truediv)
    __rtruediv__ = _delay_operation(operator.truediv, True)
    __floordiv__ = _delay_operation(operator.floordiv)
    __rfloordiv__ = _delay_operation(operator.floordiv, True)
    __mod__ = _delay_operation(operator.mod)
    __rmod__ = _delay_operation(operator.mod, True)
    __neg__ = _delay_operation(operator.neg)
    __pos__ = _delay_operation(operator.pos)

    def __bool__(self):
        return bool(self.force())

    def __int__(self):
        return int(self.force())

    def __float__(self):
        return float(self.force())

    def __long__(self):
        return long(self.force())

    def __complex__(self):
        return complex(self.force())

    def __str__(self):
        return str(self.force())

    def __eq__(self, other):
        return self._get_value(self) == self._get_value(other)

    def __lt__(self, other):
        return self._get_value(self) < self._get_value(other)

    def __le__(self, other):
        return self._get_value(self) <= self._get_value(other)

    def __gt__(self, other):
        return self._get_value(self) > self._get_value(other)

    def __ge__(self, other):
        return self._get_value(self) >= self._get_value(other)

    def force(self):
        self._number = self._get_value(self._number)
        return self._number
