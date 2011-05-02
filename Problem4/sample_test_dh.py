import unittest
from solution import gt, lt, pred, for_any,\
                        present, for_all, eq, oftype

def  even_len(str):
    if(len(str) % 2 == 0):
        return True
    return False

def even_len2(str):
    if(len(str) %2 == 0):
        return "Da"

class PredicatesTest(unittest.TestCase):
    def test_greater_than_predicate(self):
        positive=gt(0)
        self.assertTrue(positive(2))
        self.assertTrue(positive(1.5))
        self.assertFalse(positive(0))
        self.assertFalse(positive(-1))
        self.assertFalse(positive(-1.5))
    
    def test_lower_than_predicate(self):
        negative=lt(0)
        self.assertTrue(negative(-2))
        self.assertTrue(negative(-1.5))
        self.assertFalse(negative(0))
        self.assertFalse(negative(1))
        self.assertFalse(negative(1.5))
        
    def test_equal_predicate(self):
        zero=eq(0)
        self.assertTrue(zero(0))
        self.assertFalse(zero(1))
        self.assertFalse(zero(-1.5))
        
    def test_oftype_predicate(self):
        float_num=oftype(float)
        self.assertTrue(float_num(1.5))
        self.assertFalse(float_num(0))
        self.assertFalse(float_num(1+2j))
        
    def test_present_predicate(self):
        not_null=present()
        self.assertTrue(not_null(2))
        self.assertTrue(not_null('kebap4e'))
        self.assertFalse(None)
        
    def test_pred_predicate(self):
        even_length=pred(even_len)
        self.assertTrue(even_length("parjolka"))
        self.assertFalse(even_length('kebap4e'))
        
        even_length2=pred(even_len2)
        self.assertTrue(even_length2("baba"))
        self.assertFalse(even_length2("dyado"))
        
    def test_combinations_conjunction(self):
        positive_integer=gt(0) & oftype(int)
        self.assertTrue(positive_integer(5))
        self.assertFalse(positive_integer(1.5))
        self.assertFalse(positive_integer(-1))
        
        positive_even_integer=positive_integer & pred(lambda x: x % 2 == 0)
        self.assertTrue(positive_even_integer(6))
        self.assertFalse(positive_even_integer(0))
        self.assertFalse(positive_even_integer(3))
        
    def test_combination_disjunction(self):
        
        negative_or_float=lt(0) | oftype(float)
        self.assertTrue(negative_or_float(-1))
        self.assertTrue(negative_or_float(1.5))
        self.assertFalse(negative_or_float(3))
        
        neg_or_float_or_zero=negative_or_float | eq(0)
        self.assertTrue(neg_or_float_or_zero(0))
        self.assertFalse(neg_or_float_or_zero(4))
        self.assertTrue(neg_or_float_or_zero(1.5))
        
    def test_combination_negation(self):
        not_positive=~gt(0)
        self.assertTrue(not_positive(-1))
        self.assertTrue(not_positive(0))
        self.assertFalse(not_positive(1))
        
        positive=~not_positive
        self.assertTrue(positive(5))
        self.assertFalse(positive(0))
        self.assertFalse(positive(-3))
        
    def test_combination_implication(self):
        
        string_element=oftype(str)
        even_length=pred(lambda x: len(x) %2 == 0)
        
        self.assertTrue((string_element >> even_length)(2))
        self.assertFalse((string_element >> even_length)("dyado"))
        self.assertTrue((string_element >> even_length)('baba'))
    
    def test_for_any(self):
        number=for_any(oftype(int), oftype(float), oftype(complex))
        self.assertTrue(number(1))
        self.assertTrue(number(1.3))
        self.assertTrue(number(1+2j))
        self.assertFalse(number("blah"))
        
    def test_for_all(self):
        pos_even_integer=for_all(gt(0), pred(lambda x: x%2==0), oftype(int))
        self.assertTrue(pos_even_integer(6))
        self.assertFalse(pos_even_integer(1.5))
        self.assertFalse(pos_even_integer(-1))
        
    #The examples from the task page http://fmi.py-bg.net/tasks/4   
    def tests_from_task(self):
        digit = oftype(int) & gt(-1) & lt(10)
        self.assertTrue(digit(5))
        self.assertFalse(digit(-2))
        self.assertFalse(digit("a"))
        
        binary = eq(0) | eq(1)
        self.assertTrue(binary(0))
        self.assertFalse(binary(2))
        
        number = for_any(oftype(int), oftype(float), oftype(complex))
        self.assertTrue(number(10))
        self.assertTrue(number(1+2j))
        self.assertFalse(number("kiuftence"))
        
        is_the_empty_string = pred(lambda x: x is "")
        self.assertFalse(is_the_empty_string("me4ence"))
        self.assertFalse('')
        self.assertFalse("")

if __name__ == '__main__':
    unittest.main()
