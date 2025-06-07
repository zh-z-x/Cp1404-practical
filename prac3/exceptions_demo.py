"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# Answers to questions:
# 1. When will a ValueError occur?
#    A ValueError occurs when the user enters a non-integer input (e.g., letters, symbols, or floating-point numbers)
#    for either the numerator or denominator, causing the int() conversion to fail.

# 2. When will a ZeroDivisionError occur?
#    A ZeroDivisionError occurs in the original code when the user enters 0 as the denominator,
#    as division by zero is mathematically undefined.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
#    Yes, we can check if the denominator is zero before performing the division
#    and handle it without raising an exception.

# Modified code to avoid ZeroDivisionError
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check for zero denominator to avoid ZeroDivisionError
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")