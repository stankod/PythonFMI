# -*- coding: utf-8 -*-
import unittest
from solution import *

class FirstHomeworkSimpleTests(unittest.TestCase):
    def test_make_multiset_syntax(self):
        x = make_multiset([1, 2])
        self.assertEqual(x, {1: 1, 2: 1})
        self.assertNotEqual(x, {1: 'spam', 2: 'eggs'})
        x = make_multiset(["trane", "bird", "satchmo", "bird", "trane"])
        self.assertEqual(x, {"trane": 2, "satchmo": 1, "bird": 2})
        self.assertNotEqual(x, {1: 'spam', 2: 'eggs'})

    def test_ordered_dict_syntax(self):
        x = ordered_dict({1: 'i', 2: 'ii', 3: 'iii'})
        self.assertEqual(x, [(1, 'i'), (2, 'ii'), (3, 'iii')])
        self.assertNotEqual(x, [(4, 'iv')])
        x = ordered_dict({4: 'four', 2: 'two', 3: 'three', 1: 'one'})
        self.assertEqual(x, [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')])
        self.assertNotEqual(x, [(5, 'v')])

    def test_reversed_dict_syntax(self):
        x = reversed_dict({'Nibbler': 3, 'Fillip': 2, 'Turanga': 1})
        self.assertEqual(x, {3: 'Nibbler', 2: 'Fillip', 1: 'Turanga'})
        self.assertNotEqual(x, {2: 'Amy'})
        x = reversed_dict({
            "Israel": "Jerusalem",
            "Austria": "Vienna",
            "Palestine": "Jerusalem",
            "Sweden": "Stockholm",
            })
        self.assertEqual(x, {'Jerusalem': 'Israel', 'Stockholm': 'Sweden', 'Vienna': 'Austria'})
        self.assertNotEqual(x, {2: 'Amy'})

    def test_unique_objects_syntax(self):
        x = unique_objects([1, 2, 3, 2, 1, 5, 42, None, 'asd'])
        self.assertEqual(x, 7)
        self.assertNotEqual(x, 1337)
        x = unique_objects([1, 1])
        self.assertEqual(x, 1)
        self.assertNotEqual(x, 1337)
        x = unique_objects([[], []])
        self.assertEqual(x, 2)
        self.assertNotEqual(x, 1337)
        x = unique_objects([[1], [1]])
        self.assertEqual(x, 2)
        self.assertNotEqual(x, 1337)
        b = [1, 2, []]
        a,c,f,g,h,j,k, = b,b[:],b,b[:],b,b[:],b,
        x = unique_objects([a, b, c, f, g, h, j, k, '9'*21, '9'*21])
        self.assertEqual(x, 6)
        self.assertNotEqual(x, 1337)
        x = unique_objects([1, 2, 3, [[]], [[]], []])
        self.assertEqual(x, 6)
        self.assertNotEqual(x, 1337)
        x = unique_objects([[],[[]], [] ,[[['a']]], [], []])
        self.assertEqual(x, 6)

if __name__ == "__main__":
    unittest.main()