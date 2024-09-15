#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i < len(row) - 1:
                # Print element with space but without newline
                print("{:d}".format(num), end=" ")
            else:
                # Print element followed by newline
                print("{:d}".format(num))
        if len(row) == 0:
            print()
