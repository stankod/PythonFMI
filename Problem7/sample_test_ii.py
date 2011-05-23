import unittest
from solution import interface

class InterfaceTestII(unittest.TestCase):
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

    def test_complains_for_protected_methods(self):
        with self.assertRaises(AssertionError):
            class interface_with_protected_method(metaclass=interface):
                def _protected_method(self): pass

            @interface_with_protected_method
            class MyStack:
                def _protected_method(self): pass

    def test_complains_for_code_in_interface(self):
        with self.assertRaises(AssertionError):
            class spec(metaclass=interface):
                def method_with_code(self):
                    print("This should raise Exception")

            @spec
            class MyStack:
                def method_with_code(self): pass

    def test_complain_for_missing_methods_in_implementation(self):
            class serializable(metaclass=interface):
                def serialize(self): pass
                def unserialize(self, serialized): pass

            with self.assertRaises(AssertionError):
                @serializable
                class Foo:
                    def serialize(self): pass


    def test_complains_for_using_args_only_in_interface(self):
            class IFoo(metaclass=interface):
                def bar(self, *args): pass

            with self.assertRaises(AssertionError):
                @IFoo
                class Foo:
                    def bar(self, bar, spam, eggs): pass

    def test_complains_for_using_kwargs_only_in_interface(self):
            class IFoo(metaclass=interface):
                def bar(self, **kwargs): pass

            with self.assertRaises(AssertionError):
                @IFoo
                class Foo:
                    def bar(self, bar, spam, eggs): pass

    def test_complains_for_different_order_of_positional_args(self):
            class IFoo(metaclass=interface):
                def bar(self, spam, eggs, bar): pass

            with self.assertRaises(AssertionError):
                @IFoo
                class Foo:
                    def bar(self, bar, spam, eggs): pass

if __name__ == '__main__':
    unittest.main()
