import unittest
from solution import multimethod
from sample_test_ek import *
from sample_test_np import *

class MultiDispatchTest(unittest.TestCase):
    def test_single_argument_two_independant_types(self):
        class Spam:
            def __init__(self, value):
                self.value = value

            @multimethod
            def eggs(self, arg: int):
                return self.value * arg

            @eggs.multimethod
            def eggs(self, arg: str):
                return self.value + arg

        self.assertEqual(10, Spam(2).eggs(5))
        self.assertEqual('spam!',  Spam('spam').eggs('!'))

    def test_invoking_with_a_subclass(self):
        class Spam:
            @multimethod
            def eggs(self, arg: object):
                return 'object'

        self.assertEqual('object', Spam().eggs(12))

    def test_cannot_dispatch(self):
        class Spam:
            @multimethod
            def eggs(self, arg: int): pass

        with self.assertRaises(LookupError):
            Spam().eggs('')

class MyMultiDispatchTest(unittest.TestCase):
    def test_decorated_object_has_decorator(self):
        class Spam:
            @multimethod
            def eggs(self):
                return isinstance(self, Spam)

        s = Spam()
        s.eggs()

    def test_cant_decorate_with_different_name(self):
        with self.assertRaises(NameError):
            class Spam:
                @multimethod
                def eggs(self): pass

                @eggs.multimethod
                def spam(self): pass


if __name__ == '__main__':
    unittest.main()
