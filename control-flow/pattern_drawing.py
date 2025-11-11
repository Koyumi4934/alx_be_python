# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks in one row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    # Increase the row counter
    row += 1
