import unittest
from solution import *

class ThirdHomeworkArithmeticTests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(int(Lazy(2) + Lazy(3)), 5)
        self.assertEqual(str(Lazy(2) - Lazy(1)), '1')
        self.assertEqual(int(Lazy(2) * Lazy(3)), 6)
        self.assertEqual(int(Lazy(6) / 3), 2)
        self.assertEqual(int(Lazy(7) % Lazy(4)), 3)
        self.assertEqual(int(Lazy(7) / 4), 1)
        self.assertEqual(int(-Lazy( 3)), -3)
        self.assertEqual(int(-Lazy(-3)),  3)
        self.assertEqual(int(+Lazy( 3)),  3)
        self.assertEqual(int(+Lazy(-3)), -3)

    def test_identity(self):
        self.assertEqual(int(Lazy( 3)),  3)
        self.assertEqual(int(Lazy(-3)), -3)
        self.assertEqual(float(Lazy( 3.14)),  3.14)
        self.assertEqual(float(Lazy(-3.14)), -3.14)
        self.assertEqual(bool(Lazy(True)),  True)
        self.assertEqual(bool(Lazy(False)), False)
        self.assertEqual(str(Lazy( 3)), '3')
        self.assertEqual(str(Lazy(-3)), '-3')
        self.assertEqual(str(Lazy( 3.14)), '3.14')
        self.assertEqual(str(Lazy(-3.14)), '-3.14')

        self.assertEqual(int(Lazy( 3) + Lazy(0)),  3)
        self.assertEqual(int(Lazy(-3) + 0), -3)
        self.assertEqual(float(Lazy( 3.14) - Lazy(0.0)),  3.14)
        self.assertEqual(float(Lazy(-3.14) + 0.0), -3.14)
        self.assertEqual(str(Lazy( 3) + 0), '3')
        self.assertEqual(str(Lazy(-3) - Lazy(0)), '-3')
        self.assertEqual(str(Lazy( 3.14) + 0.0), '3.14')
        self.assertEqual(str(Lazy(-3.14) - Lazy(0.0)), '-3.14')

        self.assertEqual(int(Lazy( 3) * Lazy(1)),  3)
        self.assertEqual(int(Lazy(-3) * 1), -3)
        self.assertEqual(float(Lazy( 3.14) / Lazy(1.0)),  3.14)
        self.assertEqual(float(Lazy(-3.14) * 1.0), -3.14)
        self.assertEqual(str(Lazy( 3) * 1), '3')
        self.assertEqual(str(Lazy(-3) / 1), '-3.0')
        self.assertEqual(str(Lazy(-3) // 1), '-3')
        self.assertEqual(str(Lazy( 3.14) * 1.0), '3.14')
        self.assertEqual(str(Lazy(-3.14) / Lazy(1.0)), '-3.14')

    def test_commutative(self):
        self.assertEqual(int(Lazy(5) + Lazy(6)), int(Lazy(6) + Lazy(5)))
        self.assertEqual(int(Lazy(5) + 6), int(Lazy(6) + 5))
        self.assertEqual(5 + 6, int(Lazy(6) + Lazy(5)))
        self.assertEqual(int(Lazy(5) * Lazy(6)), int(Lazy(6) * Lazy(5)))
        self.assertEqual(int(Lazy(5) * 6), int(Lazy(6) * 5))
        self.assertEqual(5 * 6, int(Lazy(6) * Lazy(5)))

    def test_associative(self):
        self.assertEqual(int((Lazy(2) + Lazy(3)) + Lazy(4)), int(Lazy(2) + (Lazy(3) + Lazy(4))))
        self.assertEqual(float((Lazy(2) * Lazy(3)) * Lazy(4)), float(Lazy(2) * (Lazy(3) * Lazy(4))))
        self.assertEqual(int((Lazy(2) + Lazy(3)) - Lazy(4)), int(Lazy(2) + (Lazy(3) - Lazy(4))))
        self.assertEqual(float((Lazy(2) * Lazy(3)) / Lazy(4)), float(Lazy(2) * (Lazy(3) / Lazy(4))))

    def test_distributive(self):
        self.assertEqual(int(Lazy(2) * (Lazy(3) + Lazy(4))), int(Lazy(2) * Lazy(3) + Lazy(2) * Lazy(4)))
        self.assertEqual(int(Lazy(2) * (Lazy(3) - Lazy(4))), int(Lazy(2) * Lazy(3) - Lazy(2) * Lazy(4)))
        self.assertEqual(int(Lazy(2) * (Lazy(3) + Lazy(4))), int(Lazy(2) * Lazy(3) + Lazy(2) * Lazy(4)))
        self.assertEqual(int(Lazy(2) * (Lazy(3) - Lazy(4))), int(Lazy(2) * Lazy(3) - Lazy(2) * Lazy(4)))
        self.assertEqual(float(Lazy(2.0) * (Lazy(3.0) + Lazy(4.0))), float(Lazy(2.0) * Lazy(3.0) + Lazy(2.0) * Lazy(4.0)))
        self.assertEqual(float(Lazy(2.0) * (Lazy(3.0) - Lazy(4.0))), float(Lazy(2.0) * Lazy(3.0) - Lazy(2.0) * Lazy(4.0)))
        self.assertEqual(float(Lazy(2.0) * (Lazy(3.0) + Lazy(4.0))), float(Lazy(2.0) * Lazy(3.0) + Lazy(2.0) * Lazy(4.0)))
        self.assertEqual(float(Lazy(2.0) * (Lazy(3.0) - Lazy(4.0))), float(Lazy(2.0) * Lazy(3.0) - Lazy(2.0) * Lazy(4.0)))

        self.assertEqual(int(Lazy(2) * (Lazy(3) + Lazy(4))), 2 * (3 + 4))
        self.assertEqual(float(Lazy(2.0) * (Lazy(3.0) + Lazy(4.0))), 2.0 * (3.0 + 4.0))

    def test_inverse(self):
        self.assertEqual(int(Lazy(1) + Lazy(-1)), 0)
        self.assertEqual(int(Lazy(1) - Lazy(1)), 0)
        self.assertEqual(int(Lazy(1) + (-Lazy(1))), 0)
        self.assertEqual(int(Lazy(1) - (+Lazy(1))), 0)
        self.assertEqual(float(Lazy(2.0) * Lazy(0.5)), 1)
        self.assertEqual(float(Lazy(2.0) / Lazy(2.0)), 1)

class ReflectedTests(unittest.TestCase):
    def test_reflected(self):
        self.assertEqual(float(2 + Lazy(3)), float(Lazy(2) + 3))
        self.assertEqual(float(2 - Lazy(3)), float(Lazy(2) - 3))
        self.assertEqual(float(2 * Lazy(3)), float(Lazy(2) * 3))
        self.assertEqual(float(2 / Lazy(3)), float(Lazy(2) / 3))
        self.assertEqual(float(2 // Lazy(3)), float(Lazy(2) // 3))
        self.assertEqual(float(2 % Lazy(3)), float(Lazy(2) % 3))
