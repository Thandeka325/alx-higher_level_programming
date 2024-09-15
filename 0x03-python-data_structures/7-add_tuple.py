#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements (0, 0)
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Return the sum of the 1st two elements of both tuples
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
