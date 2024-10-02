#!/usr/bin/python3


import math


class MagicClass:
    """A class that replicates the behavior of provided bytecode."""

    def __init__(self, radius=0):
        """Initializes the radius, ensuring it is a number."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates and returns the circumference of the circle"""
        return 2 * math.pi * self.__radius
