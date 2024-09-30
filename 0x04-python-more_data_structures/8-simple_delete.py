#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # If key exist in dictionary, delete it
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
