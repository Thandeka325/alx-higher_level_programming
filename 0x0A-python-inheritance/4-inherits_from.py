#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of a class that inherited (directly or indirectly) from the specified
class, excluding the case where object is an instance of specified clss.
"""


def inherits_from(obj, a_class):
    """
    Returns True if `obj` is an instance of a class inherited (directly
    or indirectly) from `a_class`, exluding instance of `a_class` itself

    Args:
        obj: The object to check.
        a_class: The class to match the type `obj` against.

    Returns:
        True if `obj` is an instance of a subclass of `a_class` (not
        `a_class` itself), otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
