import unittest 
from simple_calculator import SimpleCalculator 
 
class TestSimpleCalculator(unittest.TestCase): 
    def setUp(self): 
        self.calc = SimpleCalculator() 
 
    def test_addition(self): 
        self.assertEqual(self.calc.add(2, 3), 5) 
        self.assertEqual(self.calc.add(-1, 1), 0) 
        self.assertEqual(self.calc.add(0, 0), 0) 
        self.assertAlmostEqual(self.calc.add(2.5, 1.2), 3.7) 
 
    def test_subtraction(self): 
        self.assertEqual(self.calc.subtract(5, 3), 2) 
        self.assertEqual(self.calc.subtract(0, 5), -5) 
        self.assertEqual(self.calc.subtract(-2, -3), 1) 
        self.assertAlmostEqual(self.calc.subtract(2.5, 0.5), 2.0) 
 
    def test_multiply(self): 
        self.assertEqual(self.calc.multiply(4, 5), 20) 
        self.assertEqual(self.calc.multiply(0, 999), 0) 
        self.assertEqual(self.calc.multiply(-2, 3), -6) 
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0) 
 
    def test_divide(self): 
        self.assertEqual(self.calc.divide(10, 2), 5) 
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5) 
        self.assertEqual(self.calc.divide(-9, 3), -3) 
        self.assertIsNone(self.calc.divide(5, 0)) 
        self.assertIsNone(self.calc.divide(0, 0)) 
        self.assertAlmostEqual(self.calc.divide(1, 3), 1/3) 
 
if __name__ == '__main__': 
    unittest.main() 
