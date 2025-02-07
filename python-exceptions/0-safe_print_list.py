#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # Counter for printed elements
    try:
        for i in range(x):  # Attempt to print x elements
            print(my_list[i], end="")  # Print without newline
            count += 1  # Increase count for each printed element
    except IndexError:  # Handle case where x is larger than the list
        pass  # Do nothing, just exit loop

    print()  # Print a new line after printing elements
    return count  # Return the number of printed elements

