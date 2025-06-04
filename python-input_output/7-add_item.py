#!/usr/bin/python3
"""
This script adds command-line arguments to a list,
then saves the list as JSON to 'add_item.json'.
"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing data only if file exists and is not empty
if os.path.exists(filename) and os.path.getsize(filename) > 0:
    items = load_from_json_file(filename)
else:
    items = []

# Append new arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
