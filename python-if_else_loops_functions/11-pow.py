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
    result = 1  # Initialize the result to 1
    if b < 0:  # Handle negative exponents
        a = 1 / a
        b = -b
    for _ in range(b):  # Multiply a by itself b times
        result *= a
    return result
