#!/usr/bin/python3
"""
This module provides a function to load a Python object
from a file containing a JSON representation.
"""

import json


def load_from_json_file(filename):
    """
    Loads a Python object from a file containing JSON data.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object deserialized from the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
