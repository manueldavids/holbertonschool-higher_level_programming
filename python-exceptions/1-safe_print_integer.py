#!/usr/bin/python3
def safe_print_integer(value):
    """
    Print an integer using "{:d}".format().

    Args:
        value: The value to be printed.

    Returns:
        True if value was successfully printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
