#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first integer or float.
        b: The second integer or float (defaults to 98).

    Returns:
        The sum of the two integers.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast the variables to integers if thhey are floats.
    a = int(a)
    b = int(b)

    return a + b
