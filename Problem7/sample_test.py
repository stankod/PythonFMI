import unittest
from solution import interface

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

class InterfaceTests(unittest.TestCase):
    def test_no_private_attributes(self):
        with self.assertRaises(NameError):
            class spam(metaclass=interface):
                def _more_spam(self): pass

        with self.assertRaises(NameError):
            class eggs(metaclass=interface):
                def __spam_end_spam(self): pass

        class ham(metaclass=interface):
            def __call__(self, *args): pass

    def test_complain_if_pos_arg_in_different_order(self):
        class spam(metaclass=interface):
            def more_spam(self, a, b): pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def more_spam(self, b, a): pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def more_spam(self, a, c): pass
        @spam
        class eggs:
            def more_spam(self, a, b): pass

    def test_complain_if_a_method_missing(self):
        class spam(metaclass=interface):
            def foo(self): pass
            def bar(self): pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def foo(self): pass

        @spam
        class more_spam:
            def foo(self): pass
            def bar(self): pass

    def test_complain_if_not_taking_varargs(self):
        class spam(metaclass=interface):
            def foo(self, *args): pass
        class more_spam(metaclass=interface):
            def foo(self): pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def foo(self): pass

        @spam
        class eggs:
            def foo(self, *args): pass

        with self.assertRaises(AssertionError):
            @more_spam
            class eggs:
                def foo(self, *args): pass

        @more_spam
        class eggs:
            def foo(self): pass

    def test_complain_if_not_taking_kwargs(self):
        class spam(metaclass=interface):
            def foo(self, **kwargs): pass
        class more_spam(metaclass=interface):
            def foo(self): pass

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def foo(self): pass

        @spam
        class eggs:
            def foo(self, **kwargs): pass

        with self.assertRaises(AssertionError):
            @more_spam
            class eggs:
                def foo(self, **kwargs): pass

        @more_spam
        class eggs:
            def foo(self): pass

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

        with self.assertRaises(AssertionError):
            @spam
            class eggs:
                def foo(self): pass

        @spam
        class eggs:
            def foo(self, *, a, b): pass

        @spam
        class eggs:
            def foo(self, *, b, a): pass

    def test_implementation_works(self):
        class spam(metaclass=interface):
            def foo(self):
                "Return 42"

            def bar(self, a):
                "Multiply by ten"

            def spam(self): pass

        @spam
        class eggs:
            def spam(self):
                return type(self)

            def foo(self):
                return 42

            def bar(self, a):
                return a*10

        self.assertEqual(42, eggs().foo())
        self.assertEqual("Return 42", eggs().foo.__doc__)
        self.assertEqual(20, eggs().bar(2))
        self.assertEqual("Multiply by ten", eggs().bar.__doc__)
        self.assertEqual(eggs, eggs().spam())

if __name__ == '__main__':
    unittest.main()
