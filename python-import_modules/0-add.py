#!/usr/bin/python3

if __name__ == "__main__":
    """
    Import the function add(a, b) from add_0.py and use it to print
    the result of 1 + 2 = 3.
    """
    from add_0 import add  # Import the add function only once

    # Define variables a and b in separate lines
    a = 1
    b = 2

    # Print the result using the add function
    print("{} + {} = {}".format(a, b, add(a, b)))
