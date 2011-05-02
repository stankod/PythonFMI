import pdb
import unittest
from solution import gt, lt, pred, for_any, for_all, present, eq, oftype
from sample_test_ek import *
from  sample_test_np import *
from sample_test_dh import *

class PredicatesTest(unittest.TestCase):
    def test_simple_gt(self):
        self.assertTrue(gt(2)(4))

    def test_combining_gt_and_lt(self):
        self.assertTrue((gt(2) & lt(4))(3))

    def test_combining_lt_and_gt(self):
        self.assertTrue((lt(4) & gt(2))(3))

    def test_pred(self):
        self.assertTrue(pred(lambda x: x > 2)(4))

    def test_gt(self):
        self.assertTrue(gt(0)(1))
        self.assertFalse(gt(0)(0))
        self.assertFalse(gt(0)(-1))
        self.assertTrue(gt(1.5)(1.6))
        self.assertFalse(gt(1.5)(1.5))

    def test_lt(self):
        self.assertFalse(lt(0)(1))
        self.assertFalse(lt(0)(0))
        self.assertTrue(lt(0)(-1))
        self.assertFalse(lt(1.5)(1.6))
        self.assertFalse(lt(1.5)(1.5))
        self.assertTrue(lt(1.5)(-1.5))

    def test_eq(self):
        self.assertTrue(eq(0)(0))
        self.assertFalse(eq(0)(1))
        self.assertTrue(eq([])([]))
        self.assertTrue(eq(None)(None))
        self.assertTrue(eq('man united champions')('man united champions'))
        self.assertFalse(eq('chelsea')('champions'))

    def test_oftype(self):
        class a: pass
        class b(a): pass
        self.assertTrue(oftype(int)(5))
        self.assertFalse(oftype(int)(5.0))
        self.assertTrue(oftype(float)(.0))
        self.assertFalse(oftype(float)(0))
        self.assertTrue(oftype(str)('5'))
        self.assertFalse(oftype(a)(b))

    def test_present(self):
        b = None
        self.assertTrue(present()(5))
        self.assertTrue(present()(-5))
        self.assertFalse(present()(None))
        self.assertFalse(present()(b))
        self.assertTrue(present()([]))

    def test_pred(self):
        def odd(x):
            return (x % 2)
        self.assertTrue(pred(odd)(1))
        self.assertTrue(pred(odd)(11))
        self.assertFalse(pred(odd)(8))
        self.assertTrue(pred(lambda x: x > 10)(11))
        self.assertFalse(pred(lambda x: x > 10)(9))
        self.assertTrue(pred(lambda x: x.lower() == x)('all lower'))
        self.assertFalse(pred(lambda x: x.lower() == x)('noT all lower'))

    def test_and(self):
        self.assertTrue((gt(0) & lt(5))(3))
        self.assertFalse((lt(5) & gt(0))(5))
        self.assertFalse((gt(0) & lt(5))(0))
        self.assertFalse((gt(0) & lt(0))(1))
        self.assertFalse((gt(0) & lt(0))(-1))
        self.assertFalse((gt(0) & lt(0))(0))
        self.assertTrue(( oftype(float) & gt(-1) & lt(10) & lt(9) & pred(lambda x: x%2) )(5.0))
        self.assertFalse(( oftype(float) & gt(-1) & lt(10) & lt(9) & pred(lambda x: x%2) )(5))
        self.assertFalse(( oftype(float) & gt(-1) & lt(10) & lt(9) & pred(lambda x: x%2) )(4.0))
        self.assertFalse(( oftype(float) & gt(-1) & lt(10) & lt(9) & pred(lambda x: x%2) )(-4.0))

    def test_and_intersection(self):
        self.assertTrue( ((lt(6) & gt(-5)) & (gt(4) & lt(10)))(5) )
        self.assertFalse( ((lt(6) & gt(-5)) & (gt(4) & lt(10)))(6) )
        self.assertFalse( ((lt(6) & gt(-5)) & (gt(4) & lt(10)))(4) )

    def test_or(self):
        self.assertTrue(( gt(0) | eq(-42) )(-42))
        self.assertFalse(( gt(0) | eq(-42) )(-43))
        self.assertTrue((gt(0) | lt(-5) | eq(-5) | oftype(float))(-3.0))
        self.assertFalse((gt(0) | lt(-5) | eq(-5) | oftype(float))(-3))
        self.assertTrue((gt(0) | lt(-5) | eq(-5) | oftype(float))(-5))
        self.assertFalse((gt(0) | lt(-5) | eq(-5) | oftype(float))(-2))
        for i in range(-5,6):
            if i == 0:
                self.assertFalse((gt(0) | lt(0))(i))
            else:
                self.assertTrue((gt(0) | lt(0))(i))

    def test_neg(self):
        negative = ~gt(0)
        positive = ~lt(0)
        negative2 = ~positive
        self.assertTrue(negative(-1))
        self.assertFalse(negative(1))
        self.assertTrue(positive(1))
        self.assertFalse(positive(-1))
        self.assertTrue(negative2(-1))
        non = ~present()
        self.assertTrue(non(None))
        not_integer = ~oftype(int)
        self.assertTrue(not_integer(1+1j))
        self.assertFalse(not_integer(1))

    def test_for_any(self):
        self.assertTrue(for_any(gt(0), lt(1))(0))
        self.assertFalse(for_any()(0))

    def test_for_all(self):
        self.assertTrue(for_all()(1))

if __name__ == '__main__':
    unittest.main()
