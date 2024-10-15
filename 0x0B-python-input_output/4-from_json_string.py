#!/usr/bin/python3
"""
This module defines a function that returns an object from JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The corresponding Python object.
    """
    return json.loads(my_str)
