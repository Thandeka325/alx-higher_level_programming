#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists containing integers or floatts.
        div: The number to divide each element by(must be an integer or float).

    Returns:
        A new matrix with all elements divided by div, rounded to 2\
                decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integer/floats.
        TypeError: If rows of the matrix are not the same size
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is equal to zero.
    """

    # Check if matrix is a list of lists containing only integers or floats
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(elem, (int, float))
                    for row in matrix for elem in row)):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        "integer/floats")

    # Check if each row in the matrix is of the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of matrix must have the same size")

    # Check if div is an integer or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and rounding to two decimal places
    return [[round(elem / div, 2) for elem in row] for row in matrix]
