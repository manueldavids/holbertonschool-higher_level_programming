#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replace or add a key/value pair in a dictionary.

    Args:
        a_dictionary: The dictionary to update.
        key: The key to update or add (always a string).
        value: The value associated with the key.

    Returns:
        The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
