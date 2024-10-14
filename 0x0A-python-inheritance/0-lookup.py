#!/usr/bin/python3
def lookup(obj):
    """

    Returns the list of the available attributes and methods of an object

    Args:
        obj: The object to inspect.

    Returns:
        A list of attributes and methods.
    """
    return dir(obj)
