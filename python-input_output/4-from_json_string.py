#!/usr/bin/python3
"""
This module provides a function to convert a JSON string
to a Python data structure (object).
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object representation of a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The corresponding Python object.
    """
    return json.loads(my_str)
