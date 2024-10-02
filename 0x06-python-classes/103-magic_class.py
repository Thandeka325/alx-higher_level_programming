#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode provided by ALX."""

import math


class MagicClass:
    """A class that replicates the behaviour of the provided bytecode"""

    def __init__(self, radius=0):
        """Initializes the radius, ensuring it is a number.

        Args:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates and returns the area of circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculates and returns the circumference of the circle."""
        return (2 * math.pi * self.__radius)
