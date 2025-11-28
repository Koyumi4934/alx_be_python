import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a calculator before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition with positive, negative, zero, and floats."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertAlmostEqual(self.calc.add(2.5, 0.5), 3.0)

    def test_subtraction(self):
        """Test subtraction with positive, negative, zero, and floats."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertAlmostEqual(self.calc.subtract(2.5, 1.2), 1.3)

    def test_multiplication(self):
        """Test multiplication including by zero and negative numbers."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 999), 0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_division_normal(self):
        """Test normal division scenarios (ints and floats)."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(-9, 3), -3.0)

    def test_division_by_zero(self):
        """Division by zero should return None per implementation."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_edge_cases_large_numbers(self):
        """Test with very large numbers to ensure no unexpected behavior."""
        a = 10**12
        b = 10**6
        self.assertEqual(self.calc.multiply(a, b), a * b)
        self.assertEqual(self.calc.add(a, b), a + b)
        self.assertEqual(self.calc.subtract(a, b), a - b)
        self.assertEqual(self.calc.divide(a, b), a / b)

if __name__ == '__main__':
    unittest.main()
