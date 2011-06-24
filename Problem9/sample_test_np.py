import unittest
from solution import multidispatch

class MultiDispatchTestNP(unittest.TestCase):
    def test_2(self):
        class Spam(metaclass=multidispatch):
            def eggs(self, x: int, y: str):
                return 42

        with self.assertRaises(LookupError):
            Spam().eggs(y=45.463, x=14.3)
        self.assertEqual(42, Spam().eggs(y='dsf',x=5))

    def test_3(self):
        class Spam(metaclass=multidispatch):
            def eggs(self, x:int):
                return 42

        with self.assertRaises(LookupError):
            Spam().eggs(32, 32, 45, 'fdsfsd')

if __name__ == '__main__':
    unittest.main()
