import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, -5), -6)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 4), -4)
        self.assertEqual(self.calc.subtract(-2, -3), 1)
        self.assertAlmostEqual(self.calc.subtract(2.5, 1.2), 1.3)
        self.assertEqual(self.calc.subtract(1000000, 500000), 500000)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertEqual(self.calc.divide(1000000, 2), 500000)

if __name__ == '__main__':
    unittest.main()
