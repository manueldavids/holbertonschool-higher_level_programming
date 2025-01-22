#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list.

    Args:
        my_list: The list containing elements of any type.
        x: The number of elements to print.

    Returns:
        The real number of elements printed.
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print("")  # Print a newline at the end
    return count
