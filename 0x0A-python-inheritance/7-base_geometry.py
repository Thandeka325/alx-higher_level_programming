#!/usr/bin/python3
"""
This module contains the BaseGeometry class with methods from area calculated.
"""


class BaseGeometry:
    """
    A class named BaseGeometry with methods to validate integer values
    and calculate area.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented.'
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validayes the value as an integer greater than zero.

        Args:
            name (str): The name of the variable being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
