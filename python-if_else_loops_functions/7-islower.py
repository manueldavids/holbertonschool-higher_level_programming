#!/usr/bin/python3

def islower(c):
    """
    Check if a character is lowercase.

    Args:
        c: A single character to check.

    Returns:
        True if c is a lowercase letter, False otherwise.
    """
    return ord(c) >= 97 and ord(c) <= 122


# Test cases
if __name__ == "__main__":
    print(islower('a'))  # True
    print(islower('z'))  # True
    print(islower('A'))  # False
    print(islower('Z'))  # False
    print(islower('1'))  # False
    print(islower('?'))  # False
