#!/usr/bin/python3
"""
This module contains the BaseGeometry class with an unimplemented area
method.
"""


class BaseGeometry:
    """
    A class named BaseGeometry with a public instance method area.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
