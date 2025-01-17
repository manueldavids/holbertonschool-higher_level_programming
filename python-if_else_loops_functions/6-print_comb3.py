#!/usr/bin/python3

# Print all possible different combinations of two digits
for digit1 in range(0, 10):  # First digit
    for digit2 in range(digit1 + 1, 10):  # Second digit greater than the first
        if digit1 == 8 and digit2 == 9:  # Last combination (no trailing comma)
            print("{:d}{:d}".format(digit1, digit2))
        else:  # All other combinations with a trailing comma
            print("{:d}{:d}".format(digit1, digit2), end=", ")
