#!/usr/bin/python3
# filepath: python-data_structures/2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
