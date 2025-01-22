#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least two elements by appending 0s
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]

    # Add corresponding elements and return the result as a tuple
    return (a[0] + b[0], a[1] + b[1])
