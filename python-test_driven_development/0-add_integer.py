#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first number (integer or float).
        b: The second number (integer or float), defaults to 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast to integers before addition
    a = int(a)
    b = int(b)
    return a + b
