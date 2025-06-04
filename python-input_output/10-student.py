#!/usr/bin/python3
"""
Module that defines a Student class with optional attribute filtering.
"""


class Student:
    """
    Student class with public instance attributes:
    first_name, last_name, age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to filter by.
                If None or not a list, returns all attributes.

        Returns:
            dict: Dictionary with the requested attributes.
        """
        if isinstance(attrs, list):
            # Filter only attributes present in both the instance and attrs list
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            # Return all attributes
            return self.__dict__
