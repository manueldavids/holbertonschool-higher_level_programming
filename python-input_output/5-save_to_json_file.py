#!/usr/bin/python3
"""
This module provides a function to save a Python object
to a file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using JSON representation.

    Args:
        my_obj (object): The Python object to serialize.
        filename (str): The file where the JSON will be written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
