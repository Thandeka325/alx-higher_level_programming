#!/usr/bin/python3
"""
Class that defines a student by first name, last name, and age.
"""


class Student:
    """
    Defines a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the student with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance

        Args:
            attrs (list, optional): A list of attribute names to retrieve

        Returns:
            dict: A a dictionary representation of the student's attr.
        """
        if attrs is None:
            return self.__dict__

        # Create a dictionary with only the specified attributes
        return {
            attr: getattr(self, attr)
            for attr in attrs if hasattr(self, attr)
        }
