#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of, or if the object is an instance of a class that inherited from, the
specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if `obj` is an instance of `a_class` or if `obj` is an
    instance of a class that inherited from `a_class`.

    Args:
        obj: The object to check.
        a_class: The class or parent class to match the type of `obj`.

    Returns:
        True if `obj` is an instance or subclass instance of 'a_class',
        otherwise False.
    """
    return isinstance(obj, a_class)
