#!/usr/bin/python3
"""
Module that defines a Student class.
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

    def to_json(self):
        """
        Returns the dictionary representation of the Student instance.

        Returns:
            dict: Dictionary with all public instance attributes.
        """
        return self.__dict__
