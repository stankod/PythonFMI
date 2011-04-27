# -*- coding: utf-8 -*-
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

class Test_Lazy(unittest.TestCase):
    def setUp(self):
        self.lazy1 = Lazy(5)
        self.lazy2 = Lazy(3)


    def test_forcing_lazy_number(self):
        self.assertEqual(5, self.lazy1.force())
        self.assertEqual(3, self.lazy2.force())


    def test_adding_lazy_numbers(self):
        #Two lazy numbers
        self.assertEqual(8, (self.lazy1 + self.lazy2).force())

        #Lazy number and normal number
        self.assertEqual(10, (self.lazy1 + 5).force())
        self.assertEqual(10, (5 + self.lazy1).force())

        #Something longer
        self.assertEqual(22, (self.lazy1 + self.lazy2 + 4 + 5 + self.lazy1).force())

        #In place
        lazy_num = Lazy(self.lazy1)
        lazy_num += 7
        self.assertEqual(12, lazy_num.force())
        lazy_num += Lazy(lazy_num)
        self.assertEqual(24, lazy_num.force())


    def test_substracting_lazy_numbers(self):
        #Two lazy numbers
        self.assertEqual(2, (self.lazy1 - self.lazy2).force())
        self.assertEqual(-2, (self.lazy2 - self.lazy1).force())

        #Lazy number and a normal number
        self.assertEqual(5, (self.lazy1-0).force())
        self.assertEqual(0, (self.lazy1-5).force())

        #In place
        lazy_num = Lazy(self.lazy1)
        lazy_num -= 2
        self.assertEqual(3, lazy_num.force())
        lazy_num -= Lazy(lazy_num)
        self.assertEqual(0, lazy_num.force())


    def test_multiplying_lazy_numbers(self):
        #Two lazy numbers
        self.assertEqual(15, (self.lazy1 * self.lazy2).force())

        #lazy number and a normal number
        self.assertEqual(10, (self.lazy1 * 2).force())
        self.assertEqual(9, (3 * self.lazy2).force())

        #In place
        lazy_num = Lazy(self.lazy1)
        lazy_num *= 3
        self.assertEqual(15, lazy_num.force())
        lazy_num *= Lazy(lazy_num)
        self.assertEqual(15*15, lazy_num.force())


    def test_dividing_lazy_numbers(self):
        #Two lazy numbers
        self.assertAlmostEqual(5/3, (self.lazy1 / self.lazy2).force())

        #lazy number and a normal number
        self.assertAlmostEqual(5/2, (self.lazy1 / 2).force())
        self.assertAlmostEqual(3/3, (3 / self.lazy2).force())

        #In place
        lazy_num = Lazy(30)
        lazy_num /= 6
        self.assertEqual(5, lazy_num.force())
        lazy_num /= Lazy(lazy_num)
        self.assertEqual(1, lazy_num.force())


    def test_floor_division_of_lazy_numbers(self):
        #Two lazy numbers
        self.assertEqual(5 // 3, (self.lazy1 // self.lazy2).force())

        #Lazy number and normal number
        self.assertEqual(5 // 2, (self.lazy1 // 2).force())
        self.assertEqual(17 // 5, (17 // self.lazy1).force())

        #In place
        lazy_num = Lazy(5)
        lazy_num //= 2
        self.assertEqual(2, lazy_num.force())
        lazy_num //= Lazy(lazy_num)
        self.assertEqual(1, lazy_num.force())


    def test_mod_division_of_lazy_numbers(self):
        #Two lazy numbers
        self.assertEqual(2, (self.lazy1 % self.lazy2).force())

        #Lazy number and normal number
        self.assertEqual(1, (self.lazy1 % 2).force())
        self.assertEqual(2, (17 % self.lazy2).force())

        #In place
        lazy_num = Lazy(5)
        lazy_num %= 3
        self.assertEqual(2, lazy_num.force())
        lazy_num %= Lazy(lazy_num)
        self.assertEqual(0, lazy_num.force())


    def test_negative_positive_lazy_number(self):
        self.assertEqual(-5, (-self.lazy1).force())
        self.assertEqual(5, (+self.lazy1).force())


    def test_lazy_number_conversions(self):
        self.assertTrue(isinstance(int(self.lazy2), int))
        self.assertTrue(isinstance(bool(self.lazy2), bool))
        self.assertTrue(isinstance(float(self.lazy2), float))
        self.assertTrue(isinstance(str(self.lazy2), str))


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