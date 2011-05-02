import unittest
from solution import gt, lt, pred, for_any,\
                     for_all, present, eq, oftype, raising_predicate

def even(n):
    if n % 2 == 0:
        return True
    else:
        return False


class TestPredicates(unittest.TestCase):
    def test_gt(self):
        greater_than_fourty_two = gt(42)

        self.assertTrue(greater_than_fourty_two(43))
        self.assertFalse(greater_than_fourty_two(3.14))

    def test_lt(self):
        less_than_fourty_two = lt(42)

        self.assertTrue(less_than_fourty_two(3.14))
        self.assertFalse(less_than_fourty_two(43))

    def test_eq(self):
        equals_fourty_two = eq(42)

        self.assertTrue(equals_fourty_two(42))
        self.assertFalse(equals_fourty_two(3.12))

    def test_oftype(self):
        is_object = oftype(object)

        self.assertTrue(is_object('abc'))
        self.assertTrue(is_object(7))
        self.assertTrue(is_object([]))
        self.assertTrue(is_object({}))

        is_int = oftype(int)

        self.assertTrue(is_int(5))
        self.assertFalse(is_int(5.0))
        self.assertFalse(is_int('baba'))

    def test_present(self):
        is_present = present()

        self.assertTrue(is_present(5))
        self.assertFalse(is_present(None))

    def test_predicate_conjuction(self):
        between_pi_and_fourty_two = gt(3.14) & lt(42)

        self.assertTrue(between_pi_and_fourty_two(10))
        self.assertFalse(between_pi_and_fourty_two(3))
        self.assertFalse(between_pi_and_fourty_two(43))

        between_pi_and_fourty_two_except_thirteen =\
            between_pi_and_fourty_two & ~eq(13)

        self.assertTrue(between_pi_and_fourty_two_except_thirteen(5))
        self.assertTrue(between_pi_and_fourty_two_except_thirteen(15))
        self.assertFalse(between_pi_and_fourty_two_except_thirteen(13))

    def test_predicate_disjunction(self):
        lt_pi_or_gt_fourty_two = lt(3.14) | gt(42)

        self.assertTrue(lt_pi_or_gt_fourty_two(1))
        self.assertTrue(lt_pi_or_gt_fourty_two(43))
        self.assertFalse(lt_pi_or_gt_fourty_two(15))

        lt_pi_or_gt_fourty_two_and_13 = lt_pi_or_gt_fourty_two |\
            eq(13)

        self.assertTrue(lt_pi_or_gt_fourty_two_and_13(13))
        self.assertFalse(lt_pi_or_gt_fourty_two_and_13(15))

    def test_predicate_negation(self):
        ge_five = ~lt(5)

        self.assertTrue(ge_five(10))
        self.assertTrue(ge_five(5))
        self.assertFalse(ge_five(3))

    def test_predicates_implication(self):
        gt_five = gt(5)
        lt_ten = lt(10)

        self.assertTrue((gt_five >> lt_ten)(7))
        self.assertFalse((gt_five >> lt_ten)(20))
        self.assertTrue((gt_five >> lt_ten)(4))

    def test_pred(self):
        even_predicate = pred(TestPredicates.even)

        self.assertTrue(even_predicate(42))
        self.assertFalse(even_predicate(11))

    def test_for_any(self):
        some_predicate = for_any(gt(10), lt(6), eq(7.5))

        self.assertTrue(some_predicate(7.5))
        self.assertTrue(some_predicate(15))
        self.assertTrue(some_predicate(-4))
        self.assertFalse(some_predicate(6))

    def test_for_all(self):
        some_predicate = for_all(pred(even), gt(0), lt(10))

        self.assertTrue(some_predicate(4))
        self.assertTrue(some_predicate(6))
        self.assertFalse(some_predicate(3))
        self.assertFalse(some_predicate(-2))
        self.assertFalse(some_predicate(14))

    #@unittest.expectedFailure
    def test_thrifty_conunction_and_disjunction(self):
        """Ако искате да тествате за това сменете raising_predicate
        с името на вашия 'хвърлящ' клас и го добавете в import-а"""
        number = pred(lambda x: True) | raising_predicate(5)
        number(5)

        number = pred(lambda x: False) & raising_predicate(17)
        self.assertRaises(number(17))

        number = for_any(pred(lambda x: True), raising_predicate(5))
        number(5)

        number = for_all(pred(lambda x: False), raising_predicate(5))
        self.assertRaises(number(17))

    def test_for_all_and_for_any_without_arguments(self):
        empty_all = for_all()
        empty_any = for_any()

        self.assertTrue(empty_all('baba'))
        self.assertFalse(empty_any('baba'))

    #Sample tests from GitHub
    def test_simple_gt(self):
        self.assertTrue(gt(2)(4))

    def test_combining_gt_and_lt(self):
        self.assertTrue((gt(2) & lt(4))(3))

    def test_combining_lt_and_gt(self):
        self.assertTrue((lt(4) & gt(2))(3))

    def test_pred(self):
        self.assertTrue(pred(lambda x: x > 2)(4))

if __name__ == '__main__':
    unittest.main()
