#!/usr/bin/python3

def print_last_digit(number):
    """
    Print and return the last digit of a number.

    Args:
        number: The input number (can be positive or negative).

    Returns:
        The last digit of the input number.
    """
    # Get the absolute value of the number and compute the last digit
    last_digit = abs(number) % 10
    # Print the last digit without a newline
    print("{}".format(last_digit), end="")
    # Return the last digit
    return last_digit
