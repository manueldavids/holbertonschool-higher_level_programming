#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divide two integers and print the result in the finally block.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of the division, or None if division fails.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
