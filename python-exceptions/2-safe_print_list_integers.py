#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x elements of a list, only integers.

    Args:
        my_list: The list containing elements of any type.
        x: The number of elements to access in my_list.

    Returns:
        The real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            continue
    print("")  # Print a new line at the end
    return count
