#!/usr/bin/python3
"""
This module provides a function to add two integers.

It ensures that:
- The inputs are integers or floats.
- Floats are converted to integers before addition.
- Proper errors are raised for invalid inputs.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (converting them to integers first).

    Args:
        a (int or float): First number.
        b (int or float, optional): Second number, default is 98.
    
    Returns:
        int: The sum of the two numbers after conversion to integers.
    
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
