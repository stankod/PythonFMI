import unittest
from solution import interface

class MetaclassInterfaceTest(unittest.TestCase):
    def test_interface_has_only_public_attributes(self):
        with self.assertRaises(AssertionError):
            class spam(metaclass=interface):
                def _more_spam(self): pass

        with self.assertRaises(AssertionError):
            class eggs(metaclass=interface):
                def __spam(self): pass

        class spam(metaclass=interface):
            def __call__(self, *args): pass

    def test_interface_has_only_methods(self):
        class spam(metaclass=interface):
            def a(self): pass
            b = a

        with self.assertRaises(AssertionError):
            class spam(metaclass=interface):
                def a(self): pass
                b = "a"

    def test_complain_if_pos_arg_in_different_order(self):
        class spam(metaclass=interface):
            def more_spam(self, a, b): pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def more_spam(self, b, a): pass

        @spam
        class eggs:
            def more_spam(self, a, b): pass

    def test_complain_if_wrong_number_pos_args(self):
        class spam(metaclass=interface):
            def more_spam(self, a, b, c):
                pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def more_spam(self, a, b, c, d): pass

        @spam
        class eggs:
            def more_spam(self, a, b, c): pass

    def test_complain_if_pos_args_dont_match_names(self):
        class spam(metaclass=interface):
            def more_spam(self, a, b, c):
                pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def more_spam(self, a, b, d): pass

    def test_complain_if_a_method_missing(self):
        class spam(metaclass=interface):
            def foo(self): pass
            def bar(self): pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def foo(self): pass

    def test_doesnt_complain_if_class_has_more_methods(self):
        class spam(metaclass=interface):
            def foo(self): pass

        @spam
        class eggs:
            def foo(self): pass
            def bar(self): pass

    def test_complain_if_not_taking_varargs(self):
        class spam(metaclass=interface):
            def foo(self, *args): pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def foo(self): pass
        @spam
        class eggs:
            def foo(self, *args): pass

        @spam
        class eggs:
            def foo(self, *arg): pass

    def test_complain_if_taking_varargs_but_not_defined(self):
        class more_spam(metaclass=interface):
            def foo(self): pass

        with self.assertRaises(AssertionError):
            @more_spam
            class eggs:
                def foo(self, *args): pass

    def test_complain_if_not_taking_kwargs(self):
        class spam(metaclass=interface):
            def foo(self, **kwargs): pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def foo(self): pass
        @spam
        class eggs:
            def foo(self, **kwargs): pass

        @spam
        class eggs:
            def foo(self, **kwarg): pass

    def test_complain_if_taking_kwargs_but_not_defined(self):
        class more_spam(metaclass=interface):
            def foo(self): pass

        with self.assertRaises(AssertionError):
            @more_spam
            class eggs:
                def foo(self, **kwargs): pass

    def test_methods_have_same_kwonly_args_noorder(self):
        class spam(metaclass=interface):
            def foo(self, *, a, b): pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def foo(self, *, a, c): pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def foo(self, *, a, b, c): pass

        @spam
        class eggs:
            def foo(self, *, a, b): pass

        @spam
        class eggs:
            def foo(self, *, b, a): pass

    def test_annotations_can_be_different(self):
        class spam(metaclass=interface):
            def foo(self, a: int, b: float):
                pass

        @spam
        class eggs:
            def foo(self, a: float, b:int):
                return a * b

        self.assertEqual(10, eggs().foo(2, 5))

    def test_doc_string_is_overriden(self):
        class spam(metaclass=interface):
            def more_spam(self):
                'Spam, spam and spam'

            def even_more_spam(self):
                """
                Nobody expects the Spanish Inquisition!
                """

        @spam
        class eggs:
            def more_spam(self):
                return 42

            def even_more_spam(self):
                r"Something completely different"

        self.assertEqual("Spam, spam and spam", eggs().more_spam.__doc__)
        self.assertEqual("Something completely different", eggs().even_more_spam.__doc__)

    def test_implementation_works(self):
        class spam(metaclass=interface):
            def bar(self, a): "Multiply by ten"
            def spam(self): pass

        @spam
        class eggs:
            def spam(self):
                return type(self)

            def bar(self, a):
                return a*10

        self.assertEqual(20, eggs().bar(2))
        self.assertEqual(eggs, eggs().spam())

    def test_complain_if_implementation_in_interface(self):
        with self.assertRaises(AssertionError):
            class spam(metaclass=interface):
                def foo(self):
                    return self

        with self.assertRaises(AssertionError):
            class spam(metaclass=interface):
                def foo(self):
                    return 42

        with self.assertRaises(AssertionError):
            class spam(metaclass=interface):
                def foo(self):
                    double_spam = "spam"*2

    def test_ignore_newly_implemented_methods(self):
        class spam(metaclass=interface):
            def foo(self): pass

        @spam
        class eggs:
            def a_function(self, a):
                print(a)

            def foo(self): pass
            def ultra_spam(self, *, a): pass

    def test_system_attributes_work(self):
        class spam(metaclass=interface):
            def __init__(self, value):
                pass
            def __call__(self, *args):
                pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def __init__(self, value): pass
        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def __init__(self): pass
                def __call__(self): pass
        @spam
        class eggs:
            def __init__(self, value):
                self.val = value
            def __call__(self, *args):
                return self.val
        v = 10
        egg = eggs(v)
        self.assertEqual(v, egg())

class InterfaceTest(unittest.TestCase):
    def test_add_missing_docstring(self):
        class stack(metaclass=interface):
            def pop(self):
                """Pops the stack head"""

        @stack
        class MyStack:
            def pop(self):
                pass

        self.assertEqual("Pops the stack head", MyStack.pop.__doc__)

    def test_complains_for_different_number_of_arguments(self):
        class spec(metaclass=interface):
            def foo(self, a): pass

        with self.assertRaises(AssertionError):
            @spec
            class MyStack:
                def foo(self, a, b): pass

    def test_does_not_complain_when_same_kwonly_args_but_in_different_order(self):
        class spec(metaclass=interface):
            def foo(self, *, a, b): pass

        @spec
        class MyStack:
            def foo(self, *, b, a): pass

    def test_does_not_complain_when_different_annotations(self):
        class spec(metaclass=interface):
            def foo(self, arg): pass

        @spec
        class MyStack:
            def foo(self, arg: int): pass

if __name__ == '__main__':
    unittest.main()
