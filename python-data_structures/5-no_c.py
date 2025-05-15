#!/usr/bin/python3

def no_c(my_string):
    """
    Remove all characters 'c' and 'C' from a
    string.

    Args:
        my_string (str): The original string.

    Returns:
        str: A new string with all 'c' and 'C'
        characters removed.
    """
    return ''.join([char for char in my_string if char != 'c' and char != 'C'])
