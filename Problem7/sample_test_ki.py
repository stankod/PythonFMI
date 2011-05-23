import unittest
from solution import interface

class InterfaceTestKI(unittest.TestCase):
    def test_complains_for_not_public_methods_in_interface(self):
        with self.assertRaises(AssertionError):
            class intf(metaclass=interface):
                def method1(self):
                    """Pops the stack head"""
                def _method1(self):
                    pass
                    
    def test_complains_for_defined_not_methods_in_interface(self):
        with self.assertRaises(AssertionError):
            class intf(metaclass=interface):
                def method1(self):
                    """Pops the stack head"""
                def method2(self):
                    pass
                x = 3
    def test_complains_for_defined_methods_diff_than_docstring_or_pass_in_interface(self):
        with self.assertRaises(AssertionError):
            class intf(metaclass=interface):
                def method1(self):
                    """Pops the stack head"""
                def method2(self):
                    pass
                def method3(self):
                    """printing x"""
                    print(x)
                    
    def test_not_complaining_with_correctly_defined_interface(self):
        class intf(metaclass=interface):
            def m1(self, a, b, c):
                 pass
            def m2(self):
                """docstring"""
            def m3(self):
                pass

        class intf2(metaclass=interface):
            def m1(self, a, b, c):
                pass

        class intf3(metaclass=interface):
            def m2(self):
                """docstring"""

    def test_complaining_for_not_implemented_methods(self):
        class intf(metaclass=interface):
            def m1(self, a, b, c):
                 pass
            def m2(self):
                """docstring"""
            def m3(self):
                pass

        with self.assertRaises(AssertionError):
            @intf
            class klass(metaclass=interface):
                def m1(self, a, b, c):
                    """Pops the stack head"""
                def m2(self):
                    pass

    def test_complaining_for_different_num_of_args(self):
        class intf(metaclass=interface):
            def m1(self, a, b, c):
                 pass
            def m2(self):
                """docstring"""
            def m3(self):
                pass

        with self.assertRaises(AssertionError):
            @intf
            class klass(metaclass=interface):
                def m1(self, a, b, c):
                    """Pops the stack head"""
                def m2(self):
                    pass
                def m3(self, a):
                    pass

        with self.assertRaises(AssertionError):
            @intf
            class klass2(metaclass=interface):
                def m1(self, b, c):
                    """Pops the stack head"""
                def m2(self):
                    pass
                def m3(self, a):
                    pass

    def test_complaining_for_args_with_different_names(self):
        class intf(metaclass=interface):
            def m1(self, a, b, c):
                 pass
            def m2(self, b, c):
                """docstring"""
            def m3(self):
                pass

        with self.assertRaises(AssertionError):
            @intf
            class klass(metaclass=interface):
                def m1(self, aa, b, c):
                    """Pops the stack head"""
                def m2(self, b, c):
                    pass
                def m3(self):
                    pass

        with self.assertRaises(AssertionError):
            @intf
            class klass2(metaclass=interface):
                def m1(self, a, b, c):
                    """Pops the stack head"""
                def m2(self, c, b):
                    pass
                def m3(self):
                    pass

    def test_complaining_for_not_having_list_args(self):
        class intf(metaclass=interface):
            def m1(self, a, b, c, *args):
                 pass
            def m2(self, b, c, *la):
                """docstring"""
            def m3(self):
                pass

        with self.assertRaises(AssertionError):
            @intf
            class klass(metaclass=interface):
                def m1(self, a, b, c):
                    """Pops the stack head"""
                def m2(self, b, c, *la):
                    pass
                def m3(self):
                    pass

        with self.assertRaises(AssertionError):
            @intf
            class klass2(metaclass=interface):
                def m1(self, a, b, c, *args):
                    """Pops the stack head"""
                def m2(self, c, b):
                    pass
                def m3(self):
                    pass

    def test_complaining_for_having_list_args(self):
        class intf(metaclass=interface):
            def m1(self, a, b, c):
                 pass
            def m2(self, b, c):
                """docstring"""
            def m3(self):
                pass

        with self.assertRaises(AssertionError):
            @intf
            class klass(metaclass=interface):
                def m1(self, a, b, c):
                    """Pops the stack head"""
                def m2(self, b, c, *la):
                    pass
                def m3(self):
                    pass

        with self.assertRaises(AssertionError):
            @intf
            class klass2(metaclass=interface):
                def m1(self, a, b, c, *args):
                    """Pops the stack head"""
                def m2(self, c, b):
                    pass
                def m3(self):
                    pass

    def test_complaining_for_having_list_args_with_different_names(self):
        class intf(metaclass=interface):
            def m1(self, a, b, c, *args):
                 pass
            def m2(self, b, c, *la):
                """docstring"""
            def m3(self):
                pass

        with self.assertRaises(AssertionError):
            @intf
            class klass(metaclass=interface):
                def m1(self, a, b, c, *aargs):
                    """Pops the stack head"""
                def m2(self, b, c, *la):
                    pass
                def m3(self):
                    pass

        with self.assertRaises(AssertionError):
            @intf
            class klass2(metaclass=interface):
                def m1(self, a, b, c, *args):
                    """Pops the stack head"""
                def m2(self, c, b, *al):
                    pass
                def m3(self):
                    pass

    def test_not_complaining_with_correct_list_args(self):
        class intf(metaclass=interface):
            def m1(self, a, b, c, *args):
                 pass
            def m2(self, b, c, *la):
                """docstring"""
            def m3(self):
                pass

        
        @intf
        class klass(metaclass=interface):
            def m1(self, a, b, c, *args):
                """Pops the stack head"""
            def m2(self, b, c, *la):
                pass
            def m3(self):
                    pass

    def test_complaining_for_not_having_keyword_args(self):
        class intf(metaclass=interface):
            def m1(self, a, b, c, **kwargs):
                 pass
            def m2(self, b, c, **la):
                """docstring"""
            def m3(self):
                pass

        with self.assertRaises(AssertionError):
            @intf
            class klass(metaclass=interface):
                def m1(self, a, b, c):
                    """Pops the stack head"""
                def m2(self, b, c, **la):
                    pass
                def m3(self):
                    pass

        with self.assertRaises(AssertionError):
            @intf
            class klass2(metaclass=interface):
                def m1(self, a, b, c, **kwargs):
                    """Pops the stack head"""
                def m2(self, c, b):
                    pass
                def m3(self):
                    pass

    def test_complaining_for_having_keyword_args(self):
        class intf(metaclass=interface):
            def m1(self, a, b, c):
                pass
            def m2(self, b, c):
                """docstring"""
            def m3(self):
                pass

        with self.assertRaises(AssertionError):
            @intf
            class klass(metaclass=interface):
                def m1(self, a, b, c):
                    """Pops the stack head"""
                def m2(self, b, c, **la):
                    pass
                def m3(self):
                    pass

        with self.assertRaises(AssertionError):
            @intf
            class klass2(metaclass=interface):
                def m1(self, a, b, c, **kwargs):
                    """Pops the stack head"""
                def m2(self, c, b):
                    pass
                def m3(self):
                    pass

    def test_complaining_for_having_keyword_args_with_different_names(self):
        class intf(metaclass=interface):
            def m1(self, a, b, c, **kwargs):
                pass
            def m2(self, b, c, **la):
                """docstring"""
            def m3(self):
                pass

        with self.assertRaises(AssertionError):
            @intf
            class klass(metaclass=interface):
                def m1(self, a, b, c, **aargs):
                    """Pops the stack head"""
                def m2(self, b, c, **la):
                    pass
                def m3(self):
                    pass

        with self.assertRaises(AssertionError):
            @intf
            class klass2(metaclass=interface):
                def m1(self, a, b, c, **args):
                    """Pops the stack head"""
                def m2(self, c, b, **al):
                    pass
                def m3(self):
                    pass

    def test_not_complaining_with_correct_keyword_args(self):
        class intf(metaclass=interface):
            def m1(self, a, b, c, **kwargs):
                pass
            def m2(self, b, c, **la):
                """docstring"""
            def m3(self):
                pass
        
        @intf
        class klass(metaclass=interface):
            def m1(self, a, b, c, **kwargs):
                """Pops the stack head"""
            def m2(self, b, c, **la):
                pass
            def m3(self):
                pass
                
    def test_not_complaining_for_different_annotations(self):
        class intf(metaclass=interface):
            def m1(self, a: 'anot1', b, c, **kwargs):
                pass
            def m2(self, b, c: int, **la):
                """docstring"""
            def m3(self):
                pass
        
        @intf
        class klass(metaclass=interface):
            def m1(self, a, b: 'anot2', c, **kwargs: float):
                """Pops the stack head"""
            def m2(self, b, c: float, **la):
                pass
            def m3(self):
                pass

    def test_for_complaining_different_number_of_keyword_only_arguments(self):
        class intf(metaclass=interface):
            def m1(self, a, b, *, d, e):
                pass
            def m2(self, *, b, c: int):
                """docstring"""
            def m3(self):
                pass

        with self.assertRaises(AssertionError):
            @intf
            class klass(metaclass=interface):
                def m1(self, a, b, d, e):
                    """Pops the stack head"""
                def m2(self, *, b, c: float):
                    pass
                def m3(self):
                    pass

    def test_for_complaining_for_different_names_of_keyword_only_arguments(self):
        class intf(metaclass=interface):
            def m1(self, a, b, *, d, e):
                pass
            def m2(self, *, b, c: int):
                """docstring"""
            def m3(self):
                pass

        with self.assertRaises(AssertionError):
            @intf
            class klass(metaclass=interface):
                def m1(self, a, b, *, e, f):
                    """Pops the stack head"""
                def m2(self, *, b, c: float):
                    pass
                def m3(self):
                    pass
        with self.assertRaises(AssertionError):
            @intf
            class klass(metaclass=interface):
                def m1(self, a, b, *, ee, ff):
                    """Pops the stack head"""
                def m2(self, *, b, c: float):
                    pass
                def m3(self):
                    pass
                
    def test_for_not_complaining_for_different_order_of_definition_of_keyword_only_arguments(self):
        class intf(metaclass=interface):
            def m1(self, a, b, *, d, e, f, g):
                pass
            def m2(self, *, b, c: int):
                """docstring"""
            def m3(self):
                pass

        @intf
        class klass(metaclass=interface):
            def m1(self, a, b, *, e, f, g, d):
                """Pops the stack head"""
            def m2(self, *, c, b: float):
                pass
            def m3(self):
                pass

    def test_for_taking_docstring_if_not_existing(self):
        class intf(metaclass=interface):
            def m1(self, a, b, *, d, e, f, g):
                pass
            def m2(self, *, b, c: int):
                """docstring"""
            def m3(self):
                pass

        @intf
        class klass(metaclass=interface):
            def m1(self, a, b, *, e, f, g, d):
                """Pops the stack head"""
            def m2(self, *, c, b: float):
                pass
            def m3(self):
                pass

        self.assertTrue(klass.m2.__doc__ == "docstring")
        self.assertFalse(klass.m2.__doc__ == "1234")

    def test_for_keeping_own_docstring_if_existing(self):
        class intf(metaclass=interface):
            def m1(self, a, b, *, d, e, f, g):
                pass
            def m2(self, *, b, c: int):
                """docstring"""
            def m3(self):
                pass

        @intf
        class klass(metaclass=interface):
            def m1(self, a, b, *, e, f, g, d):
                """Pops the stack head"""
            def m2(self, *, c, b: float):
                """doc2"""
            def m3(self):
                pass

        self.assertTrue(klass.m2.__doc__ == "doc2")
        self.assertFalse(klass.m2.__doc__ == "docstring")
        
    
    def test_add_missing_docstring_stefans(self):
        class stack(metaclass=interface):
            def pop(self):
                """Pops the stack head"""

        @stack
        class MyStack:
            def pop(self):
                pass

        self.assertEqual("Pops the stack head", MyStack.pop.__doc__)
   
    def test_complains_for_different_number_of_arguments_stefans(self):
        class spec(metaclass=interface):
            def foo(self, a): pass

        with self.assertRaises(AssertionError):
            @spec
            class MyStack:
                def foo(self, a, b): pass
    
    def test_does_not_complain_when_same_kwonly_args_but_in_different_order_stefans(self):
        class spec(metaclass=interface):
            def foo(self, *, a, b): pass

        @spec
        class MyStack:
            def foo(self, *, b, a): pass
   
    def test_does_not_complain_when_different_annotations_stefans(self):
        class spec(metaclass=interface):
            def foo(self, arg): pass

        @spec
        class MyStack:
            def foo(self, arg: int): pass


if __name__ == '__main__':
    unittest.main()
