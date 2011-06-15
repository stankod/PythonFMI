import unittest
from solution import multimethod

class MultiDispatchTestNP(unittest.TestCase):
    def test_1(self):
        with self.assertRaises(NameError):
            class Spam:
                @multimethod
                def eggs(self, arg: int): pass

                @eggs.multimethod
                def x(self, arg:str): pass

            Spam().eggs('fsdfsd')

    def test_2(self):
        class Spam:
            @multimethod
            def eggs(self, x: int, y: str):
                return 42

        self.assertEqual(42, Spam().eggs(y='dsf',x=5))
        with self.assertRaises(LookupError):
            Spam().eggs(y=45.463, x=14.3)

    def test_3(self):
        class Spam:
            @multimethod
            def eggs(self, x:int):
                return 42

        with self.assertRaises(LookupError):
            Spam().eggs(32, 32, 45, 'fdsfsd')

if __name__ == '__main__':
    unittest.main()
