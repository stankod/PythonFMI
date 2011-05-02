import unittest

from solution import *

class MyTest(unittest.TestCase):
    def test_gt(self):
        x = gt(0)
        self.assertTrue(x(10))
        self.assertFalse(x(0))
        self.assertFalse(x(-10))

    def test_lt(self):
        x = lt(0)
        self.assertFalse(x(10))
        self.assertFalse(x(0))
        self.assertTrue(x(-10))

    def test_eq(self):
        x = eq('str')
        self.assertTrue(x('str'))
        self.assertFalse(x('STR'))

    def test_oftype(self):
        x = oftype(int)
        self.assertTrue(x(10))
        self.assertFalse(x(10.0))

    def test_present(self):
        x = present()
        self.assertTrue(x(4))
        self.assertFalse(x(None))

    def test_pred(self):
        self.assertTrue(pred(lambda x: x > 2)(4))

    def test_and(self):
        pr = gt(2) & lt(4)
        self.assertTrue(pr(3))
        self.assertFalse(pr(5))
        self.assertFalse(pr(2))

    def test_and2(self):
        pr = gt(2) & (lambda x: x < 4)
        self.assertTrue(pr(3))
        self.assertFalse(pr(5))
        self.assertFalse(pr(2))
        pr = (lambda x: x> 2) & lt(4)
        self.assertTrue(pr(3))
        self.assertFalse(pr(5))
        self.assertFalse(pr(2))

    def test_or(self):
        pr = oftype(str) | gt(0)
        self.assertTrue(pr(10))
        self.assertTrue(pr('fds'))
        self.assertFalse(pr(0))

    def test_or2(self):
        pr = oftype(str) | (lambda x: x >0)
        self.assertTrue(pr(10))
        self.assertTrue(pr('fds'))
        self.assertFalse(pr(0))

        pr = (lambda x: isinstance(x, str)) | gt(0)
        self.assertTrue(pr(10))
        self.assertTrue(pr('fds'))
        self.assertFalse(pr(0))

    def test_not(self):
        pr = ~gt(0)
        self.assertTrue(pr(-10))
        self.assertTrue(pr(0))
        self.assertFalse(pr(10))

    def test_implication(self):
        pr = oftype(int) >> gt(41)
        self.assertTrue(pr(42))
        self.assertTrue(pr('fdfsd'))
        self.assertFalse(pr(41))

    def test_implication2(self):
        pr = oftype(int) >> (lambda x: x > 41)
        self.assertTrue(pr(42))
        self.assertTrue(pr('fdfsd'))
        self.assertFalse(pr(41))

        pr = (lambda x: isinstance(x, int)) >> gt(41)
        self.assertTrue(pr(42))
        self.assertTrue(pr('fdfsd'))
        self.assertFalse(pr(41))

    def test_for_any(self):
        pr1 = gt(2)
        pr2 = gt(1)
        pr3 = gt(0)
        pr = for_any(pr1, pr2, pr3)
        self.assertTrue(pr(1))
        self.assertFalse(pr(0))
        self.assertTrue(pr(100))

    def test_for_any2(self):
        pr1 = lambda x: x > 2
        pr2 = lambda x: x > 1
        pr3 = lambda x: x > 0
        pr = for_any(pr1, pr2, pr3)
        self.assertTrue(pr(1))
        self.assertFalse(pr(0))
        self.assertTrue(pr(100))

    def test_for_all(self):
        pr1 = gt(2)
        pr2 = gt(1)
        pr3 = gt(0)
        pr = for_all(pr1, pr2, pr3)
        self.assertTrue(pr(100))
        self.assertFalse(pr(2))
        self.assertFalse(pr(0))

    def test_for_all2(self):
        pr1 = lambda x: x > 2
        pr2 = lambda x: x > 1
        pr3 = lambda x: x > 0
        pr = for_all(pr1, pr2, pr3)
        self.assertTrue(pr(100))
        self.assertFalse(pr(2))
        self.assertFalse(pr(0))

if __name__ == '__main__':
    unittest.main()
