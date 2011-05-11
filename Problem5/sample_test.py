import unittest
import re
from solution import *
from sample_test_dh import *
from sample_test_ad import *
from sample_test_ki import *
from sample_test_pm import *

class FifthHomeworkSimpleTests(unittest.TestCase):
    def test_tokenize(self):
        self.assertEqual(
            ['(', 'times', '3', '"spam"', ')'],
            tokenize('(times 3 "spam")'))

    def test_identifiers(self):
        self.assertEqual(
            {'sum', 'number'},
            identifiers(['(', 'sum', '42', 'number', 'NUMBER', ')']))

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
        expected = ['c*rrec7+_^', 'A1s0-c0rRecT', 'in', 'correct']
        code = '1nc0rr3c7 c*rrec7+_^ A1s0-c0rRecT in,correct'
        self.assertEqual(expected, tokenize(code))

    def test_tokenize_recognizes_dotted_numbers(self):
        code = '123 .123 1.23 12.3 123. 1.2.3'
        expected = ['123', '.123', '1.23', '12.3', '123.']
        self.assertEqual(expected, tokenize(code))

    def test_tokenize_recognizes_numbers_alone(self):
        code = '133t 13e7 1337'
        expected = ['1337']
        self.assertEqual(expected, tokenize(code))

if __name__ == "__main__":
    unittest.main()
