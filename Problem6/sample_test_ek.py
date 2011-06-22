from solution import multimethod
import unittest

@multimethod
def a_func(a:int, b:int):return a**b

@a_func.multimethod
def a_func(a:float, b:float):return a/b

@a_func.multimethod
def a_func(a:str, b:int):return a*b

@a_func.multimethod
def a_func(a:str, b:str):return ' '.join([a,b])

@a_func.multimethod
def a_func(a,b):return a,b

class song:
    @multimethod
    def sing(self, a:list):
        return 'Every list is sacred'

    @sing.multimethod
    def sing(self, a:set):
        return 'Every set is great'

    @sing.multimethod
    def sing(self, a:dict):
        return 'If a dict is wasted'

    @sing.multimethod
    def sing(self, a:tuple):
        return 'God gets quite upset'


@multimethod
def da_func(a:int, b:float):pass

@da_func.multimethod
def da_func(a:float, b:int):pass

class TestMultimethods(unittest.TestCase):
    s = song()
    def test_simple(self):
        self.assertEqual(3125, a_func(5,5))
        self.assertAlmostEqual(150.13/234.52, a_func(150.13,234.52))
        self.assertEqual('babababababa', a_func('ba',6))
        self.assertEqual('e bre de bre', a_func('e bre','de bre'))
        self.assertEqual(([42],'Jeremy'), a_func([42], 'Jeremy'))

    def test_multimethod(self):
        self.assertEqual('Every list is sacred', self.s.sing([]))
        self.assertEqual('Every set is great', self.s.sing(set()))
        self.assertEqual('If a dict is wasted', self.s.sing({}))
        self.assertEqual('God gets quite upset', self.s.sing(()))

    def test_name_error(self):
        with self.assertRaises(NameError):
            @da_func.multimethod
            def larodi():pass

    def test_lookup_error(self):
        with self.assertRaises(LookupError):
            self.s.sing(17)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            @multimethod
            class something_completely_different:
                pass

#############################
#Sample test from assignment#
#############################
class MultiDispatchTest(unittest.TestCase):
    def test_single_argument_two_independant_types(self):
        class Spam:
            def __init__(self, value):
                self.value = value

            @multimethod
            def eggs(self, arg: int):
                return self.value * arg

            @eggs.multimethod
            def eggs(self, arg: str):
                return self.value + arg

        self.assertEqual(10, Spam(2).eggs(5))
        self.assertEqual('spam!',  Spam('spam').eggs('!'))

    def test_invoking_with_a_subclass(self):
        class Spam:
            @multimethod
            def eggs(self, arg: object):
                return 'object'

        self.assertEqual('object', Spam().eggs(12))

    def test_cannot_dispatch(self):
        class Spam:
            @multimethod
            def eggs(self, arg: int): pass

        with self.assertRaises(LookupError):
            Spam().eggs('')


if __name__ == '__main__':
    unittest.main()
