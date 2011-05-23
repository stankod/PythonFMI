import unittest
from solution import interface


class binary_operation(metaclass = interface):
    def set_first(self, arg1):"""Sets the first argument of the binary operation"""
    def set_second(self, arg2):"""Sets the second argument of the binary operation"""
    def calculate(self):pass
    def set_arguments(self, arg1, arg2):"""Sets the two arguments of the binary operation"""


class multi_argument_operation(metaclass = interface):
    def set_arguments(self, *args):"""Set the arguments"""
    def set_arguments_from_list(self, args):"""Set the arguemtsn from the given list"""

class something_with_kwonly(metaclass = interface):
    def a_method(a, b, c, *, kwonly1, kwonly2, kwonly3):pass

class InterfaceTestEK(unittest.TestCase):

    def test_raises_on_repositioned_arguments(self):
        with self.assertRaises(AssertionError):
            @binary_operation
            class addition:
                def set_first(self, arg1):self.arg1 = arg1
                def set_second(self, arg2):self.arg2 = arg2
                def calculate(self):return self.ar1+self.arg2
                def set_arguments(self, arg2, arg1):pass

    def test_raises_on_missing_method(self):
        with self.assertRaises(AssertionError):
            @binary_operation
            class factorial:
                def set_first(self, arg1):selfarg1 = arg1
                def calculate(self):pass

    def test_raise_if_not_agree_on_args(self):
        with self.assertRaises(AssertionError):
            @multi_argument_operation
            class avg:
                def set_arguments(self):pass
                def set_arguments_from_list(self, args):pass
        with self.assertRaises(AssertionError):
            @multi_argument_operation
            class avg:
                def set_arguments(self, *args):pass
                def set_arguments_from_list(self, args, *argsl):pass

    def test_raise_if_not_agree_on_kwargs(self):
        with self.assertRaises(AssertionError):
            @something_with_kwonly
            class something_with_other_kwargs:
                def a_method(a, b, c, *, kwonly1, kwonly2, kwonly17):pass
            

    def test_overrides_docstring(self):
        @binary_operation
        class substraction:
            def set_first(self, arg1):"""This sets the minuend"""
            def set_second(self, arg2):"""This sets the substrahend"""
            def calculate(self):pass
            def set_arguments(self, arg1, arg2):pass


        self.assertEqual("This sets the minuend", substraction.set_first.__doc__)


    def test_raise_if_nonpublic_methods(self):
        with self.assertRaises(AssertionError):
            class pvt_ifce(metaclass = interface):
                def _prot_method(self, a):pass
                def __pvt_method(self, b):pass


    def test_raise_if_nonmethods_in_interface(self):
        with self.assertRaises(AssertionError):
            class non_methods(metaclass = interface):
                var1 = 7

    #@unittest.expectedFailure
    def test_raise_if_method_has_implementaion_in_interface(self):
        with self.assertRaises(AssertionError):
            class ifce_impl(metaclass = interface):
                def a_func(self, a):
                    self.a = a


    #Tests from sample test
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
