import unittest
from solution import *

class FifthHomeworkSimpleTests_ki(unittest.TestCase):
    def test_tokenize(self):
        self.assertEqual(['(', 'times', '3', '"spam"', ')'], tokenize('(times 3 "spam")'))
        self.assertEqual(['(','+','123','"eggs"',')'], tokenize('(+ 123 "eggs")'))
        self.assertEqual(
            ['(', 'foo', '(', '+','a', 'some-number', 'SOME-NUMBER', 'Some-Number', ')', '123', '#t', '"Miles Davis"', ')'], 
            tokenize('(foo (+ a some-number SOME-NUMBER Some-Number) 123 #t "Miles Davis")'))
        self.assertEqual(['(','sqrt-iter','1','x',')'],tokenize('(sqrt-iter 1 x)'))
        self.assertEqual(['(','+','(','-','a4c','bcc',')','(','*','3','r&a',')',')'],
            tokenize('(+ (- a4c bcc) (* 3 r&a))'))
        self.assertEqual(['(','+','(','-','a4c','bcc',')','(','*','3','r&a',')',')'],
            tokenize('(+ (- a4c bcc) (* 3 r&a))'))
        self.assertEqual(['a'], tokenize('a'))
        self.assertEqual(['A'], tokenize('A'))
        self.assertEqual(['aajskajsk'], tokenize('aajskajsk'))
        self.assertEqual(['a9-&94830492'], tokenize('a9-&94830492'))
        self.assertEqual(['!'], tokenize('!'))
        self.assertEqual(['$'], tokenize('$'))
        self.assertEqual(['%'], tokenize('%'))
        self.assertEqual(['&'], tokenize('&'))
        self.assertEqual(['*'], tokenize('*'))
        self.assertEqual(['+'], tokenize('+'))
        self.assertEqual(['-'], tokenize('-'))
        self.assertEqual(['.'], tokenize('.'))
        self.assertEqual(['/'], tokenize('/'))
        self.assertEqual([':'], tokenize(':'))
        self.assertEqual(['<'], tokenize('<'))
        self.assertEqual(['='], tokenize('='))
        self.assertEqual(['>'], tokenize('>'))
        self.assertEqual(['?'], tokenize('?'))
        self.assertEqual(['@'], tokenize('@'))
        self.assertEqual(['^'], tokenize('^'))
        self.assertEqual(['_'], tokenize('_'))
        self.assertEqual(['~'], tokenize('~'))
        self.assertEqual(['dkajs!jdksa'], tokenize('dkajs!jdksa'))
        self.assertEqual(['JmJmskOiskK'], tokenize('JmJmskOiskK'))
        self.assertEqual(['99292.3'], tokenize('99292.3'))
        self.assertEqual(['9.'], tokenize('9.'))
        self.assertEqual(['.93878'], tokenize('.93878'))
        self.assertEqual(['39328'], tokenize('39328'))
        self.assertEqual(['0009329'], tokenize('0009329'))
        self.assertEqual(['0.00000'], tokenize('0.00000'))
        self.assertEqual(['"skldajdslk-djksadla"'], tokenize('"skldajdslk-djksadla"'))
        self.assertEqual(['"a - b"'], tokenize('"a - b"'))
        self.assertEqual(['"90 - a"'], tokenize('"90 - a"'))
        self.assertEqual(['"#t"'], tokenize('"#t"'))
        self.assertEqual(['#t'], tokenize('#t'))
        self.assertEqual(['#f'], tokenize('#f'))
        self.assertEqual(['\''], tokenize('\''))
        self.assertEqual(['('], tokenize('('))
        self.assertEqual([')'], tokenize(')'))
        self.assertEqual(['aajskajsk', '99292.3'], tokenize('aajskajsk 99292.3 '))
        self.assertEqual(['$', '-'], tokenize('$ - '))
        self.assertEqual(['&', '#t'], tokenize('& #t '))
        self.assertEqual(['-', '_'], tokenize('- _ '))
        self.assertEqual([':', '$'], tokenize(': $ '))
        self.assertEqual(['=', '"skldajdslk-djksadla"'], tokenize('= "skldajdslk-djksadla" '))
        self.assertEqual(['@', '='], tokenize('@ = '))
        self.assertEqual(['~', 'A'], tokenize('~ A '))
        self.assertEqual(['JmJmskOiskK', '.93878'], tokenize('JmJmskOiskK .93878 '))
        self.assertEqual(['.93878', '.'], tokenize('.93878 . '))
        self.assertEqual(['0009329', '\''], tokenize('0009329 \' '))
        self.assertEqual(['"a - b"', '~'], tokenize('"a - b" ~ '))
        self.assertEqual(['#t', '&'], tokenize('#t & '))
        self.assertEqual(['\'', '"a - b"'], tokenize('\' "a - b" '))
        self.assertEqual(['a', 'A', 'aajskajsk', 'a9-&94830492', '!', '=', '.', '$', '0.00000', '?'], tokenize('a A aajskajsk a9-&94830492 ! = . $ 0.00000 ? '))
        self.assertEqual(['a', 'A', 'aajskajsk', 'a9-&94830492', '!', '9.', '?', '%', '@', '0009329'], tokenize('a A aajskajsk a9-&94830492 ! 9. ? % @ 0009329 '))
        self.assertEqual(['a', 'A', 'aajskajsk', 'a9-&94830492', '!', '#f', 'JmJmskOiskK', '&', '%', ')'], tokenize('a A aajskajsk a9-&94830492 ! #f JmJmskOiskK & % ) '))
        self.assertEqual(['a', 'A', 'aajskajsk', 'a9-&94830492', '$', '.', '"skldajdslk-djksadla"', '&', '"a - b"', '>'], tokenize('a A aajskajsk a9-&94830492 $ . "skldajdslk-djksadla" & "a - b" > '))
        self.assertEqual(['a', 'A', 'aajskajsk', 'a9-&94830492', '$', '~', '\'', '*', '^', '39328'], tokenize('a A aajskajsk a9-&94830492 $ ~ \' * ^ 39328 '))
        self.assertEqual(['a', 'A', 'aajskajsk', 'a9-&94830492', '$', '"90 - a"', '*', '-', '+', ')'], tokenize('a A aajskajsk a9-&94830492 $ "90 - a" * - + ) '))
        self.assertEqual(['a', 'A', 'aajskajsk', 'a9-&94830492', '%', '*', '=', '-', '"#t"', '?'], tokenize('a A aajskajsk a9-&94830492 % * = - "#t" ? '))
    
    def test_identifiers(self):
        self.assertEqual({'Sum', 'number'},
            identifiers(['(', 'Sum', '42', 'number', 'NUMBER', ')']))
        self.assertEqual({'+','-','*','a4c','bcc','r&a'}, 
            identifiers(['(','+','(','-','a4c','bcc',')','(','*','3','r&a',')',')']))
        self.assertEqual({'+','-','*','a4c','bcc'}, 
            identifiers(['(','+','(','-','a4c','bcc',')','(','*','3','a4C',')',')']))
        self.assertEqual({'times'}, identifiers(['(', 'times', '3', '"spam"', ')']))
        self.assertEqual({'sum_numbers','dve'}, identifiers(['(','sum_numbers','1','dve','#t',')']))
        self.assertEqual({'iden'}, identifiers(['(','"spam"','"SPAM"','#f','iden','23',')']))
        self.assertEqual({'func','&','^','~'}, identifiers(['(','func','"spam"','&','^','~',')']))
        self.assertEqual({'+','some-number'}, 
            identifiers(['(', '+', 'some-number', 'SOME-NUMBER', 'Some-Number', ')']))
        self.assertEqual({'+', 'a', 'aA', 'a123'}, 
            identifiers(['(', '+', 'a', 'aA', 'aa', '"A"', '123', 'a123', 'A']))

    def test_case_sensitive(self):
        self.assertEqual('(spam "SPAM" number number number)', 
            case_sensitive('(Spam "SPAM" Number nUmber NUMBER)', {'spam','number'}))
        self.assertEqual('(add-money more more)', 
            case_sensitive('(Add-Money more More)', {'add-money','more'}))
        self.assertEqual('(add x1 y1)', case_sensitive('(add X1 Y1)',{'x1','y1'}))
        self.assertEqual('(sum 1 number)', case_sensitive('(Sum 1 Number)', {'sum','number'}))
        self.assertEqual('(mul number1 Number2)', 
            case_sensitive('(mul NumbEr1 Number2)', {'number','number1'}))
        self.assertEqual('(mul number1 Number2 NUM3 num3)', 
            case_sensitive('(mul NumbEr1 Number2 NUM3 num3)', {'number','number1'}))
        self.assertEqual('(string "String" "stRing" "STRING" "StRiNg")', 
            case_sensitive('(String "String" "stRing" "STRING" "StRiNg")', {'string'}))
        self.assertEqual('a A aajskajsk a9-&94830492 $ . "skldajdslk-djksadla" & "a - b" > ', 
            case_sensitive('a A aajskajsk a9-&94830492 $ . "skldajdslk-djksadla" & "a - b" > ', {}))
        self.assertEqual('A A aajskajsk a9-&94830492 $ . "skldajdslk-djksadla" & "a - b" > ', 
            case_sensitive('a A aajskajsk a9-&94830492 $ . "skldajdslk-djksadla" & "a - b" > ', {'A'}))
        self.assertEqual('a a aajskajsk A9-&94830492 $ . "skldajdslk-djksadla" & "a - b" > ', 
            case_sensitive('a A aajskajsk a9-&94830492 $ . "skldajdslk-djksadla" & "a - b" > ',
                           {'a', 'A9-&94830492', 'Skldajdslk-djksadla'}))
        self.assertEqual('a a aajskajsk a9-&94830492 $ . "skldajdslk-djksadla" & "a - b" > bb bB Bb BB " A A A"', 
            case_sensitive('a A aajskajsk a9-&94830492 $ . "skldajdslk-djksadla" & "a - b" > bb bB Bb BB " A A A"',
                           {'a'}))
        self.assertEqual('"bb" "bB" "Bb" "BB" a a aajskajsk a9-&94830492 $ . "skldajdslk-djksadla" & "a - b" > bb bB Bb BB " A A A "', 
            case_sensitive('"bb" "bB" "Bb" "BB" a A aajskajsk a9-&94830492 $ . "skldajdslk-djksadla" & "a - b" > bb bB Bb BB " A A A "',
                           {'a'}))
        self.assertEqual('"bb bB && Bb BB" a a aajskajsk a9-&94830492 $ . "skldajdslk-djksadla" & "a - b" > Bb Bb Bb Bb " A A A"', 
            case_sensitive('"bb bB && Bb BB" a A aajskajsk a9-&94830492 $ . "skldajdslk-djksadla" & "a - b" > bb bB Bb BB " A A A"',
                           {'a', 'Bb'}))
if __name__ == "__main__":
    unittest.main()
