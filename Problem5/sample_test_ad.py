import unittest
from solution import *

class LispTokenizeTests(unittest.TestCase):
    def test_tokenize(self):
        self.assertEqual(
            ['(', 'take', '2', '(', '\'', 'first', '"Eddie Vedder"',
             '1.', '0.33', ')', '#f', '^', ')'],
            tokenize('(take 2 (\'first "Eddie Vedder" 1. 0.33) #f ^)'))

    def test_identifiers(self):
        self.assertEqual(
            {'Count', 'number'},
            identifiers(['(', '"nUMber"', 'Count', 'number', 'count', '#t'
                         '13', 'COUNT', '\'', 'Number', ')']))

    def test_case_sensitive(self):
        self.assertEqual('(spam "SPAM")', case_sensitive('(Spam "SPAM")', {'spam'}))

    def test_real_scheme_code(self):
        old_code = """\
(define (software-type) 'MS-DOS)

(define (scheme-implementation-type) 'Pocket-Scheme)
(define (scheme-implementation-version) 
  (let ((v (version)))
    (string-append 
      (number->string (car v)) "." 
      (number->stRIng (cadr v)) "." 
      (number->String (caddr v)))))
(define (scheme-implementation-home-page) "http://www.mazama.net/scheme/pscheme.htm")

(define (implementation-vicinity) "\\Program Files\\Pocket Scheme\\")
(DEFINE (library-vicinity)  (in-vicinity (implementation-vicinity) "slib\\"))
(deFInE (home-vicinity)     "\\My Documents\\")
"""
        expected_code = """\
(define (software-type) 'MS-DOS)

(define (scheme-implementation-type) 'Pocket-Scheme)
(define (scheme-implementation-version) 
  (let ((v (version)))
    (string-append 
      (number->string (car v)) "." 
      (number->string (cadr v)) "." 
      (number->string (caddr v)))))
(define (scheme-implementation-home-page) "http://www.mazama.net/scheme/pscheme.htm")

(define (implementation-vicinity) "\\Program Files\\Pocket Scheme\\")
(define (library-vicinity)  (in-vicinity (implementation-vicinity) "slib\\"))
(define (home-vicinity)     "\\My Documents\\")
"""

        idents = identifiers(tokenize(old_code))

        self.assertEqual(expected_code, case_sensitive(old_code, idents))        

if __name__ == "__main__":
    unittest.main()
