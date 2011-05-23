import unittest
from solution import interface

class CustomInterfaceTest(unittest.TestCase):
    def test_correct_interface_no_bonus(self):
        with self.assertRaises(Exception):
            class foo(metaclass=interface):
                def _foo(self): pass
        with self.assertRaises(Exception):
            class foo(metaclass=interface):
                a=0

    def test_class_implementation(self):
        class iface(metaclass=interface):
            def foo(self): pass
            def bar(self): pass

        with self.assertRaises(Exception):
            @iface
            class klass:
                def foo(self): print("lqlqlq")
                def _foo(self): print("hihihi")

    def test_same_args_same_order(self):
        class iface(metaclass=interface):
            def foo(self, a, b): pass
            def bar(self, a, b): pass

        with self.assertRaises(AssertionError):
            @iface
            class klass:
                def foo(self, b, a): print("not same args")
                def bar(self, a, b): print("same args")
            
        with self.assertRaises(AssertionError):
            @iface
            class klass:
                def foo(self, a, b): print("same args")
                def bar(self, a): print("one missing arg")

    def test_list_args(self):
        class iface(metaclass=interface):
            def foo(self, a, *args): pass
            def bar(self, a, b): pass

        with self.assertRaises(AssertionError):
            @iface
            class klass:
                def foo(self, a, b): pass
                def bar(self, a, b): pass

        with self.assertRaises(AssertionError):
            @iface
            class klass:
                def foo(self, a, *args): pass
                def bar(self, *args): pass

    def test_keyword_args(self):
        class iface(metaclass=interface):
            def foo(self, a, *args): pass
            def bar(self, a, *args, **kwargs): pass

        with self.assertRaises(AssertionError):
            @iface
            class klass:
                def foo(self, a, *args): pass
                def bar(self, a, *args): pass

        with self.assertRaises(AssertionError):
            @iface
            class klass:
                def foo(self, a, **kwargs): pass
                def bar(self, a, *args, **kwargs): pass


    def test_argument_annotations(self):
        class iface(metaclass=interface):
            def foo(self, a: int, b: str): pass
            def bar(self, a: float, b: float): pass

        @iface
        class klass:
            def foo(self, a:str, b:object): pass
            def bar(self, a:str, b:int):  pass


    def test_keyword_only_arguments(self):
        class iface(metaclass=interface):
            def foo(self, *, a, b, c): pass
            def bar(self, *, a, b): pass

        @iface
        class klass:
            def foo(self, *, b, a, c): pass
            def bar(self, *, b, a): pass

        with self.assertRaises(AssertionError):
            @iface
            class klass:
                def foo(self, *, a, b): pass
                def bar(self, *, b, a): pass
            
        with self.assertRaises(AssertionError):
            @iface
            class klass:
                def foo(self, *, a, b, c): pass
                def bar(self, a, b): pass

    def test_missing_docstring(self):
        class iface(metaclass=interface):
            def foo(self):
                """Interface method foo"""
                pass
            def bar(self):
                """Interface method bar"""
                pass

        @iface
        class klass:
            def foo(self):
                pass
            def bar(self):
                """Class method bar"""


        self.assertEqual('Interface method foo', klass.foo.__doc__)
        self.assertEqual('Class method bar', klass.bar.__doc__)
        
    def test_for_bash_maistors(self):
        with self.assertRaises(AssertionError):
            class iface(metaclass=interface):
                def foo(self, a, b):
                    return a+b

        with self.assertRaises(AssertionError):
            class iface(metaclass=interface):
                def foo(self, a, b):
                    c=a+b

        with self.assertRaises(AssertionError):
            class iface(metaclass=interface):
                def foo(self, a, b):
                    print(a)

        with self.assertRaises(AssertionError):
            class iface(metaclass=interface):
                def foo(self, a, b):
                    a>b

        class iface(metaclass=interface):
            def foo(self, a, b):
                pass

        class iface2(metaclass=interface):
            def foo(self, a, b):
                """doc"""
    
            
if __name__ == '__main__':
    unittest.main()
