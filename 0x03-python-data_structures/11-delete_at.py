#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Check if idx is -ve or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Delete the element at index idx
    del my_list[idx]
    return my_list
