#!/usr/bin/python3

def pow(a, b):
    """
    Compute a to the power of b and return the result.

    Args:
        a: The base number.
        b: The exponent.

    Returns:
        The value of a raised to the power of b.
    """
    if b == 0:  # Any number to the power of 0 is 1
        return 1
    elif b < 0:  # Handle negative exponents
        return 1 / pow(a, -b)
    else:  # Handle positive exponents
        return a * pow(a, b - 1)
