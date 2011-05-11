import unittest
from solution import *

class FifthHomeworkSimpleTests_dh(unittest.TestCase):
    def test_tokenize(self):
        self.assertEqual(
            ['(', 'foo', '(', '+','a', 'some-number', 'SOME-NUMBER', 'Some-Number', ')', '123', '#t', '"Miles Davis"', ')'], 
            tokenize('(foo (+ a some-number SOME-NUMBER Some-Number) 123 #t "Miles Davis")'))
        self.assertEqual(['(','sqrt-iter','1','x',')'],tokenize('(sqrt-iter 1 x)'))
        self.assertEqual(['(','+','(','-','a4c','bcc',')','(','*','3','r&a',')',')'], tokenize('(+ (- a4c bcc) (* 3 r&a))'))
            
    def test_tokenize_quotes(self):
        self.assertEqual(['(', 'times', '3', '"spam"', ')'], tokenize('(times 3 "spam")'))
        self.assertEqual(['(','+','123','"eggs"',')'], tokenize('(+ 123 "eggs")'))  
    @unittest.expectedFailure
    def test_tokenize_with_inner_quotes(self):
        self.assertEqual(['(','quote','(','"This is quote \""',')',')'], tokenize('(quote ("This is quote \""))'))
    
    def test_identifiers(self):
        self.assertEqual({'sum', 'number'}, identifiers(['(', 'sum', '42', 'number', 'NUMBER', ')']))
        self.assertEqual({'+','-','*','a4c','bcc','r&a'}, identifiers(['(','+','(','-','a4c','bcc',')','(','*','3','r&a',')',')']))
        self.assertEqual({'+','-','*','a4c','bcc'}, identifiers(['(','+','(','-','a4c','bcc',')','(','*','3','a4C',')',')']))
        self.assertEqual({'sum_numbers','dve'}, identifiers(['(','sum_numbers','1','dve','#t',')']))        
        self.assertEqual({'+','some-number'},  identifiers(['(', '+', 'some-number', 'SOME-NUMBER', 'Some-Number', ')']))

    def test_identifiers_with_quoted_strings(self):
        self.assertEqual({'times'}, identifiers(['(', 'times', '3', '"spam"', ')']))
        self.assertEqual({'iden'}, identifiers(['(','"spam"','"SPAM"','#f','iden','23',')']))
        self.assertEqual({'func','&','^','~'}, identifiers(['(','func','"spam"','&','^','~',')']))      
     
    def test_case_sensitive(self):
        self.assertEqual('(add-money more more)', case_sensitive('(Add-Money more More)', {'add-money','more'}))
        self.assertEqual('(add x1 y1)', case_sensitive('(add X1 Y1)',{'x1','y1'}))
        self.assertEqual('(sum 1 number)', case_sensitive('(Sum 1 Number)', {'sum','number'}))
        self.assertEqual('(mul number1 Number2)', case_sensitive('(mul NumbEr1 Number2)', {'number','number1'}))

    def test_case_sensitive_with_quotes(self):
        self.assertEqual('(string "String" "stRing" "STRING" "\"StRiNg\"")', case_sensitive('(String "String" "stRing" "STRING" "\"StRiNg\"")', {'string'}))
        self.assertEqual('(spam "SPAM" number number number)', case_sensitive('(Spam "SPAM" Number nUmber NUMBER)', {'spam','number'}))
        
        
if __name__ == "__main__":
    unittest.main()
