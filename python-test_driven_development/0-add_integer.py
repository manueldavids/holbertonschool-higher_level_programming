def add_integer(a, b=98):
    """
    Adds two integers or floats (converting them to integers first).

    Args:
        a (int or float): First number.
        b (int or float, optional): Second number, default is 98.

    Returns:
        int: The sum of the two numbers after conversion to integers.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):  # Check if 'a' is an integer or float
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):  # Check if 'b' is an integer or float
        raise TypeError("b must be an integer")

    return int(a) + int(b)  # Convert to int before
