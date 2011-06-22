import unittest
from solution import multidispatch


class multi_baba(metaclass=multidispatch):
    def __init__(self):
        self.i = 6
        self.f = 7.0
        self.s = 'baba'
        self.c = 42j
    def m(self, arg:int):
        return self.i
    def m(self, arg:float):
        return self.f
    def m(self, arg:str):
        return self.s
    def m(self, arg:complex):
        return self.c


class unanotated(metaclass=multidispatch):
    def __init__(self):pass
    def m(self, a:int):return int
    def m(self, a:float):return float
    def m(self, a:str):return str
    def m(self, a):return 'OMG!!!'


class several_multi(metaclass=multidispatch):
    def __init__(self):pass
    def m1(self, a:int): return 'm1-int'
    def m1(self, a:float): return 'm1-float'
    def m2(self, b:int): return 'm2-int'
    def m2(self, b:float): return 'm2-float'

class should_raise(metaclass=multidispatch):
    def __init__(self):pass
    def m(self, a:int):pass


class TestMultiDispatch(unittest.TestCase):
    def test_multidispatch_anotated(self):
        multi_b = multi_baba()

        self.assertIsInstance(multi_b.m(0), int)
        self.assertIsInstance(multi_b.m(12.5), float)
        self.assertIsInstance(multi_b.m(''), str)
        self.assertIsInstance(multi_b.m(2j), complex)

    def test_work_with_unanotated(self):
        unanot = unanotated()

        self.assertEqual(int, unanot.m(5))
        self.assertEqual(float, unanot.m(12.0))
        self.assertEqual(str, unanot.m('baba'))
        self.assertEqual('OMG!!!', unanot.m(1+2j))

    def test_raise_lookup_error(self):
        raises = should_raise()
        with self.assertRaises(LookupError):
            raises.m('This parrot is dead')


    def test_several_multimethods(self):
        sm = several_multi()
        self.assertEqual('m1-int', sm.m1(0))
        self.assertEqual('m1-float', sm.m1(0.0))
        self.assertEqual('m2-int', sm.m2(0))
        self.assertEqual('m2-float', sm.m2(0.0))

if __name__ == '__main__':
    unittest.main()
