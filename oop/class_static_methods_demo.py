# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers (no class or instance access required)."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Print the class attribute then return the product."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
