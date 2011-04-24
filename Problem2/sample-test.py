# -*- coding: utf-8 -*-
import unittest
from solution import *
from functools import reduce

class SecondHomeworkSimpleTests(unittest.TestCase):

    def test_groupby_simple_types(self):
        expected = {'even':[2, 8, 10, 12], 'odd':[1, 3, 5, 9]}
        actual = groupby(lambda x: 'odd' if x%2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12])
        self.assertEqual(expected, actual)

    def test_iterate_start_with_identity_function(self):
        bracketisers = iterate(lambda x: '(' + x + ')') # there's no such word, really
        no_brackets = next(bracketisers)
        self.assertEqual('hello world', no_brackets('hello world'))
        no_brackets = next(bracketisers)
        self.assertEqual('(hello world)', no_brackets('hello world'))
        no_brackets = next(bracketisers)
        self.assertEqual('((hello world))', no_brackets('hello world'))

    #def test_iterate_start_with_identity_function_two_args(self):
        #bracketisers = iterate(lambda x,y: '(' + x + ')' + '[' + y + ']')
        #no_brackets = next(bracketisers)
        #self.assertEqual(('hello', 'world'), no_brackets('hello', 'world'))
        #no_brackets = next(bracketisers)
        #self.assertEqual('(hello)[world]', no_brackets('hello', 'world'))
 
    def test_iterate_ordered_calls(self):
        powers_of_two = iterate(lambda x: x*2)
        f = next(powers_of_two)
        self.assertEqual(1 * 'eggs', f('eggs'))
        f = next(powers_of_two)
        self.assertEqual(2 * 'ham', f('ham'))
        f = next(powers_of_two)
        self.assertEqual(4 * 'spam', f('spam'))
        f = next(powers_of_two)
        self.assertEqual(8 * 'spameggs', f('spameggs'))

    def test_zip_with_simple(self):
        first_names = ['Charlie', 'Dizzy']
        last_names = ['Parker', 'Gillespie']
        expected = ['CharlieParker', 'DizzyGillespie']
        actual = zip_with(str.__add__, first_names, last_names)
        self.assertEqual(expected, list(actual))
        expected = []
        actual = zip_with(str.__add__)
        self.assertEqual(expected, list(actual))

    def test_zip_with_simple2(self):
        w1 = [5, 7, 6, 10,]
        w2 = [3, 3, 2, 6,]
        w3 = [5, 7, 6, 10,]
        expected = [2**5, 4**7, 4**6, 4**10]
        actual = zip_with(lambda x,y,z: (x-y)**z, w1, w2, w3)
        self.assertEqual(expected, list(actual))
    
    def test_cache_call_is_cached(self):

        call_count = 0
        def double(x):
            nonlocal call_count
            call_count += 1
            return 2 * x
        
        cached_double = cache(double, 5)
        self.assertEqual(256, cached_double(128))
        self.assertEqual(512, cached_double(256))
        self.assertEqual(128, cached_double(64))
        self.assertEqual(256, cached_double(128))
        self.assertEqual(32, cached_double(16))
        self.assertEqual(64, cached_double(32))
        self.assertEqual(16, cached_double(8))
        self.assertEqual(256, cached_double(128))
        self.assertEqual(128, cached_double(64))
        self.assertEqual(7, call_count)
    
    def test_cache_call_more_args(self):
        
        call_count = 0
        def factorial(*args):
            nonlocal call_count
            call_count += 1
            return reduce(lambda x,y: x*y, args, 1)
        
        cached_fun = cache(factorial, -4)
        self.assertEqual(6, cached_fun(1, 2 ,3))
        self.assertEqual(24, cached_fun(1, 2 ,3, 4))
        self.assertEqual(120, cached_fun(1, 2 ,3, 4, 5))
        self.assertEqual(1, cached_fun(1))
        self.assertEqual(6, cached_fun(1, 2 ,3))
        self.assertEqual(1, cached_fun())
        self.assertEqual(6, call_count)
        
    def test_cache_call_more_args2(self):
        
        call_count = 0
        def simple_func(*args):
            nonlocal call_count
            call_count += 1
            return len(args)
        
        cached_fun = cache(simple_func, 4)
        self.assertEqual(3, cached_fun(1, 2 ,3))
        self.assertEqual(5, cached_fun(*str.split('dfkjskldjnfgsldf '*5)))
        self.assertEqual(5, cached_fun(1, 2.000 ,3.000, 4, 5))
        self.assertEqual(5, cached_fun(*str.split('dfkjskldjnfgsldf '*5)))
        self.assertEqual(1, cached_fun(1))
        self.assertEqual(3, cached_fun(1, 2 ,3))
        self.assertEqual(0, cached_fun())
        self.assertEqual(0, cached_fun())
        self.assertEqual(0, cached_fun())
        self.assertEqual(1, cached_fun(1))
        self.assertEqual(0, cached_fun())
        self.assertEqual(0, cached_fun())
        self.assertEqual(5, call_count)

if __name__ == "__main__":
    unittest.main()