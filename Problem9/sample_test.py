import unittest
import pdb
from solution import multidispatch
from sample_test_ek import *
from sample_test_np import *
from sample_test_pp import *

class MultiDispatchTestMY(unittest.TestCase):
    def test_single_argument_two_independant_types(self):
        class Spam(metaclass=multidispatch):
            def __init__(self, value):
                self.value = value

            def eggs(self, arg: int):
                return self.value * arg

            def eggs(self, arg: str):
                return self.value + arg
        self.assertEqual(10, Spam(2).eggs(5))
        self.assertEqual('spam!',  Spam('spam').eggs('!'))

    def test_invoking_with_a_subclass(self):
        class Spam(metaclass=multidispatch):
            def eggs(self, arg: object):
                return 'object'

        self.assertEqual('object', Spam().eggs(12))

    def test_cannot_dispatch(self):
        class Spam(metaclass=multidispatch):
            def eggs(self, arg: int): pass

        with self.assertRaises(LookupError):
            Spam().eggs('')

    def test_dispatch_methods_defined_outside(self):
        class Spam(metaclass=multidispatch):
            def eggs(self, arg: float):
                return 42.0

        def eggs(self, arg: str):
            return "42.0"

        Spam.eggs = eggs

        self.assertTrue(isinstance(Spam().eggs(12.5), float))
        self.assertTrue(isinstance(Spam().eggs("blah"), str))

if __name__ == '__main__':
    unittest.main()
