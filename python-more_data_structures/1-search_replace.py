#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element in a list with a new element.

    Args:
        my_list: The original list.
        search: The element to be replaced.
        replace: The new element to replace with.

    Returns:
        A new list with the element replaced.
    """
    return [replace if element == search else element for element in my_list]
