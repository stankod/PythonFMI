# -*- coding: utf-8 -*-
import unittest
import pdb
from solution import *
from numbers import Number
from sample_test1 import *
from sample_test_pp import *
from sample_test_ek import *

class OperatorAppliedError(Exception):
    pass

class ErrorRaisingNumber(Number):
    def __init__(self):
        pass
    def raising_operator(*args):
        raise OperatorAppliedError

    __add__ = __radd__ = raising_operator

class ThirdHomeworkSimpleTests(unittest.TestCase):
    def test_operator_is_delayed_when_applied(self):
        error_raising_number = ErrorRaisingNumber()
        lazy_number = Lazy(error_raising_number) + 8 # shouldn't raise an error
        lazy_number += Lazy(error_raising_number) # shouldn't raise an error
        lazy_number = 8 + Lazy(error_raising_number) + 8 # shouldn't raise an error

    def test_operator_is_applied_when_forced(self):
        error_raising_number = ErrorRaisingNumber()
        lazy_number = Lazy(error_raising_number) + 8
        lazy_number += Lazy(error_raising_number)
        with self.assertRaises(OperatorAppliedError):
            lazy_number.force() # should raise an error

    def test_evaluation_is_done_when_forced(self):
        number = Lazy(2) * Lazy(5)
        self.assertEqual(number.force(), 10)

    def test_operator_evaluation_works_correctly(self):
        number = Lazy(42)
        number += 8
        self.assertEqual(number.force(), 50)

    def test_lazy_addition(self):
        number = Lazy(1 + Lazy(2 + Lazy(3 + Lazy(4))))
        self.assertEqual(number.force(), 10)

    def test_lazy_subtraction(self):
        number = Lazy(1 - Lazy(2 - Lazy(3 - Lazy(4))))
        self.assertEqual(number.force(), -2)

    def test_lazy_mul_eqation(self):
        number = Lazy(5) * Lazy(10)
        self.assertEqual(number.force(), 50)

    def test_lazy_divisions_eqation(self):
        number = Lazy(5) / Lazy(10)
        self.assertEqual(number.force(), 0.5)
        number = Lazy(5) // Lazy(10)
        self.assertEqual(number.force(), 0)
        number = Lazy(5) % Lazy(10)
        self.assertEqual(number.force(), 5)

    def test_longer_equation(self):
        number = Lazy(42) + 8 - Lazy(2) + Lazy(123456) / Lazy( 2 * Lazy(3.5) )- Lazy(Lazy(Lazy(22) // Lazy(4) )) % Lazy(50)
        self.assertEqual(number.force(), (17679.571428571428))

    def test_complex_and_floats(self):
        number = Lazy(25+5j) - Lazy(10.5 + 5j) / Lazy(Lazy(150.234 - 20.3j))
        self.assertEqual(number.force(), (24.93577865898062+4.958040834813069j))

    def test_longs(self):
        number = Lazy(2 ** 37) / Lazy(2 ** 32)
        self.assertEqual(number.force(), (2 ** 5))

    def test_convertions(self):
        number = Lazy(1337)
        self.assertEqual(str(number), '1337')
        self.assertEqual(bool(number), True)
        self.assertEqual(bool(number*Lazy(0)), False)
        number = 5 / Lazy(2)
        self.assertEqual(float(number), 2.5)
        self.assertEqual(int(number), 2)

    def test_negative_positive(self):
        number = Lazy(5+10j)
        self.assertEqual((-number).force(), (-5-10j))
        self.assertEqual((+number).force(), (5+10j))

    @unittest.skip
    def test_repr(self):
        number = Lazy(Lazy(5 + 5j)) / 5
        same_number = eval(repr(number))
        self.assertEqual(same_number, number)

    def test_comparisons(self):
        five = Lazy(3) + 2
        three = 3
        another_five = Lazy(5.0)
        self.assertTrue(five > three)
        self.assertTrue(five >= three)
        self.assertTrue(three < five)
        self.assertTrue(three <= five)
        self.assertFalse(three > another_five)
        self.assertEqual(five, another_five)
        self.assertNotEqual(five, three)

if __name__ == "__main__":
    unittest.main()
