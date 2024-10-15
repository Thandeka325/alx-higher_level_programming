#!/usr/bin/python3
"""
This module defines a function that writes an object to a text file
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj (object): The object to be serialized.
        filename (str): The name of the file to write JSON re to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
