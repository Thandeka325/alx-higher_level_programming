#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix by squaring each element of the input matrix
    return [[element ** 2 for element in row] for row in matrix]
