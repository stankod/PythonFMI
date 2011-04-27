import unittest
from solution import *

from numbers import Number

class OperatorAppliedError(Exception):
    pass

class ErrorRaisingNumber(Number):
    def __init__(self):
        pass

    def raising_operator(*args):
        raise OperatorAppliedError

    __add__ = __radd__ = raising_operator

class LazyNumbersTest(unittest.TestCase):
    def test_lazy_number(self):
        lazy = Lazy(5)
        self.assertEqual(5, lazy.force())
        self.assertNotEqual(6, lazy.force())

    def test_lazy_number_constructor(self):
        lazy1 = Lazy(2)
        lazy2 = Lazy(lazy1)
        self.assertEqual(lazy1.force(), lazy2.force())

    def test_lazy_number_addition(self):
        lazy = Lazy(5)
        lazy = lazy + 3
        self.assertEqual(8, lazy.force())
        lazy = lazy + Lazy(-2)
        self.assertEqual(6, lazy.force())
        lazy = (Lazy(2) + 5) + (Lazy(-1) + (-100))
        self.assertEqual(-94, lazy.force())

    def test_other_number_types(self):
        lazy = Lazy(12.5)
        lazy = lazy + 3.33E-5
        self.assertEqual(12.5000333, lazy.force())
        lazy = Lazy(2 + 4j)
        lazy = lazy + (-1j)
        self.assertEqual(2 + 3j, lazy.force())

    def test_right_side_operands(self):
        lazy = Lazy(17)
        lazy = 3 + lazy
        self.assertEqual(20, lazy.force())

    def test_other_operations(self):
        lazy = (Lazy(5) - 10) * 5
        self.assertEqual(-25, lazy.force())
        lazy = (Lazy(1) + 2) * (3 + Lazy(4)) - 8
        self.assertEqual(13, lazy.force())
        lazy = Lazy(5) // 3
        self.assertEqual(1, lazy.force())
        lazy = (Lazy(15.3) / 3.2) % (4 * Lazy(0.67) - 0.5)
        self.assertEqual((15.3 / 3.2) % (4 * 0.67 - 0.5), lazy.force())

    def test_inplace_operators(self):
        lazy = Lazy(45)
        lazy += 4
        lazy -= 2.22
        lazy *= 12
        lazy //= 3.3
        self.assertEqual((45 + 4 - 2.22) * 12 // 3.3, lazy.force())

    def test_operator_precedence(self):
        # just in case :)
        lazy = Lazy(3) + 4 * Lazy(4.3) // 12 + 4 - Lazy(1)
        self.assertEqual(3 + 4 * 4.3 // 12 + 4 - 1, lazy.force())

    def test_conversion_functions(self):
        lazy = Lazy(4) + 12 / Lazy(7)
        self.assertEqual(True, bool(lazy))
        self.assertEqual(5, int(lazy))
        self.assertEqual(4 + 12 / 7, float(lazy))
        self.assertEqual(str(4 + 12 / 7), str(lazy))

    def test_operator_is_delayed_when_applied(self):
        error_raising_number = ErrorRaisingNumber()
        lazy_number = Lazy(error_raising_number) + 8 # shouldn't raise an error

    def test_operator_is_applied_when_forced(self):
        error_raising_number = ErrorRaisingNumber()
        lazy_number = Lazy(error_raising_number) + 8
        with self.assertRaises(OperatorAppliedError):
            lazy_number.force() # should raise an error

if __name__ == "__main__":
    unittest.main()
