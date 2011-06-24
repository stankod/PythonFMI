import unittest
from solution import multidispatch

class bahkwargs(metaclass=multidispatch):
    def __init__(self):
        self._s = 'mu'

    def setstuff(self, a:int, b:str):
        if a != 0:
            self._s = 'int:{0}'.format(a)
        elif b is not None:
            self._s = 'str:{0}'.format(b)

    def setstuff(self, a:int, b:float):
        if a != 0:
            self._s = 'int:{0}'.format(a)
        elif b is not None:
            self._s = 'float:{0}'.format(b)

    def setstuff(self, a:complex, b:str):
        if a != 0:
            self._s = 'complex:{0}'.format(a)
        elif b is not None:
            self._s = 'str:{0}'.format(b)

    def getstuff(self):
        return self._s

class TestMultiDispatchPP(unittest.TestCase):
    def test_simple(self):
        x = bahkwargs()
        x.setstuff(5, 'foo')
        self.assertEqual(x.getstuff(), 'int:5')
        x.setstuff(0, 'foo')
        self.assertEqual(x.getstuff(), 'str:foo')
        x.setstuff(6, 3.14)
        self.assertEqual(x.getstuff(), 'int:6')
        x.setstuff(0, 3.14)
        self.assertEqual(x.getstuff(), 'float:3.14')
        x.setstuff(complex(1, 2), 'bar')
        self.assertEqual(x.getstuff(), 'complex:(1+2j)')
        x.setstuff(complex(0, 0), 'bar')
        self.assertEqual(x.getstuff(), 'str:bar')

    def test_kwargs(self):
        x = bahkwargs()
        x.setstuff(5, 'foo')
        self.assertEqual(x.getstuff(), 'int:5')
        x.setstuff(0, b = 'foo')
        self.assertEqual(x.getstuff(), 'str:foo')
        x.setstuff(a = 6, b = 3.14)
        self.assertEqual(x.getstuff(), 'int:6')
        x.setstuff(b = 3.14, a = 0)
        self.assertEqual(x.getstuff(), 'float:3.14')

if __name__ == '__main__':
    unittest.main()
