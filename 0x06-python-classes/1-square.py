#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute 'size'.
"""


class Square:
    """Represents a square."""
    def __init__(self, size):
        """Initializes the square with a given size.

        Args:
            size: Size of the square (no type/value verification).
        """
        self.__size = size
