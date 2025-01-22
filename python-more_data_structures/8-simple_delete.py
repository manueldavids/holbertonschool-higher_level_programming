#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Delete a key in a dictionary if it exists.

    Args:
        a_dictionary: The dictionary to modify.
        key: The key to delete.

    Returns:
        The updated dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
