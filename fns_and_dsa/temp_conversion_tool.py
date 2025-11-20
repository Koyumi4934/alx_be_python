# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global factor.
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    # Read and validate temperature input
    temp_str = input("Enter the temperature to convert: ").strip()
    try:
        temp = float(temp_str)
    except ValueError:
        # Required behavior: raise an error with this exact message
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Read and validate unit input
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == "F":
        result = convert_to_celsius(temp)
        print(f"{temp}°F is {result}°C")
    elif unit == "C":
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

