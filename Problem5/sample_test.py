import unittest
import re
from solution import *
#from sample_test_dh import *
#from sample_test_ad import *

class FifthHomeworkSimpleTests(unittest.TestCase):
    @unittest.skip('not now')
    def test_tokenize(self):
        self.assertEqual(
            ['(', 'times', '3', '"spam"', ')'],
            tokenize('(times 3 "spam")'))

    @unittest.skip('not now')
    def test_identifiers(self):
        self.assertEqual(
            {'sum', 'number'},
            identifiers(['(', 'sum', '42', 'number', 'NUMBER', ')']))

    @unittest.skip('not now')
    def test_case_sensitive(self):
        self.assertEqual('(spam "SPAM")', case_sensitive('(Spam "SPAM")', {'spam'}))

    def test_tokenize_recognizes_specials(self):
        specials = '!$%&*+-./:<=>?@^_~'

        incorrect_ids = 'identifier '.join(specials)
        incorrect_ids += 'identifier'
        self.assertEqual(set(['identifier']+list(specials)),
                set(tokenize(incorrect_ids)))

        self.assertEqual(list(specials), tokenize(' '.join(specials)))

        incorrect_ids = ' identifier'.join(specials)
        self.assertEqual(len(specials), len(tokenize(incorrect_ids)))

    def test_tokenize_gets_identifiers(self):
        specials = re.escape('!$%&*+-./:<=>?@^_')
        expected = ['c*rrec7+_^', 'A1s0-c0rRecT',]
        code = '1nc0rr3c7 c*rrec7+_^ A1s0-c0rRecT incor,rect'
        self.assertEqual(expected, tokenize(code))

if __name__ == "__main__":
    unittest.main()
