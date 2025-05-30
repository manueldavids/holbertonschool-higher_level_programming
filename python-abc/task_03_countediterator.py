#!/usr/bin/python3
"""Module that defines CountedIterator class that counts iterated items."""


class CountedIterator:
    """Iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Returns the number of items iterated so far."""
        return self.count
