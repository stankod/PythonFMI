import unittest

from solution import tokenize, identifiers, case_sensitive

# identificators are strings containing :
# 1 alfa-numerical containing special symbols and starting with letter
#   - the special symbols are: ! $ % & * + - . / : < = > ? @ ^ _ ~ 
# 2 each special symbol is also an identificator

# tokens are strings which:
# 1 are identificators
# 2 sequence of symbols surrounded by double quotes aka <"...">
# 3 are numbers containing no more than one point <xy.zw>
# 4 is any of these: (, ), ', #t, #f

class IdentificatorsTest(unittest.TestCase):
    are_identifiers = ( (" Monty Python and the Holy Grail ", ['Monty', 'Python', 'and', 'the', 'Holy', 'Grail']),\
    ("ans42", ['ans42']), (" c2ho5oh a de",['c2ho5oh', 'a', 'de']),\
    (" ! $ % & * + - . / : < = > ? @ ^ _ ~ ", ['!', '$', '%', '&', '*', '+', '-', '.', '/', ':', '<', '=', '>', '?', '@', '^', '_', '~']),\
    (" a!a $  ", ['a!a', '$']),\
    )

    def test_for_identifiers(self):
        for i in self.are_identifiers:
            result = tokenize(i[0])
            self.assertEqual(i[1],result)

    are_tokens = tuple(are_identifiers[:] + (\
    ("( ) + ' #t #f",['(', ')', '+', "'", '#t', '#f']),\
    (" \" Ali Baba & \t 40-sette razboinika\"  ", ['" Ali Baba & \t 40-sette razboinika"']),\
    (" \" let's try how good are you \n \r\n \"  ", ['" let\'s try how good are you \n \r\n "']),\
    ("integers 4 8 15 16 23 42 ", ['integers', '4', '8', '15', '16', '23', '42']),\
    ("floarting point numers 3.14 333.333333 0.5", ['floarting', 'point', 'numers', '3.14', '333.333333', '0.5']),\
    ("\"did you escaped the dot ?\" 4x4", ['"did you escaped the dot ?"']),\
    ('(foo (+ some-number SOME-NUMBER Some-Number) 123 #t "Miles Davis")', ['(', 'foo', '(', '+', 'some-number', 'SOME-NUMBER', 'Some-Number', ')', '123', '#t', '"Miles Davis"', ')']),\
    (" .1 .0 0. 0.0 45 -45 +45 ",['.1', '.0', '0.', '0.0', '45', '-45', '+45'])
    ))

    def test_tokens(self):
        for i in self.are_tokens:
            result = tokenize(i[0])
            self.assertEqual(i[1],result)

    substracting_identifiers = (\
    (['(', '+', 'some-number', 'SOME-NUMBER', 'Some-Number', ')'], {'+', 'some-number'}),\
    (['(', '+', 'some-number', 'SOME-NUMBER', 'Some-Number', '"Some-Number"', ')'], {'+', 'some-number'}),\
    )
    def test_identifiers(self):
        for i in self.substracting_identifiers:
            result = identifiers(i[0])
            self.assertEqual(i[1],result)

    case_sensitivity = (\
    ('(spam "SPAM")', '(Spam "SPAM")', {'spam'}),\
    ('  ( spam "SPAM" sPam23 ! 0.1 1. .1) \t ', '  ( Spam "SPAM" sPam23 ! 0.1 1. .1) \t ', {'spam'}),\
    )
    def test_case_sensitive(self):
        for i in self.case_sensitivity:
            result = case_sensitive(i[1],i[2])
            self.assertEqual(i[0],result)

if __name__ == '__main__':
    unittest.main()
