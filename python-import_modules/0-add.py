#!/usr/bin/python3

if __name__ == "__main__":
    """
    Import the function add(a, b) from add_0.py and use it to print
    the result of 1 + 2 = 3.
    """
    from add_0 import add  # Import the add function only once

    a = 1  # Define variable a
    b = 2  # Define variable b

    # Call the add function and print the result
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
