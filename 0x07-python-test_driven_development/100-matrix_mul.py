#!/usr/bin/python3
"""
This module multuplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices (m_a and m_b).

    Args:
        m_a: First matrix (list of lists of integer or floats).
        m_b: Second matrix (list of lists of integer or floats).

    Returns:
        A new matrix representing the product of m_a and m_b.

    Raises:
        TypeError: If either matrix is not a list of lists of integer or floats
        ValueError: If either matrix is empty or matrices cannt be multiplied.
    """
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Check if all elements in m_a & m_b are integers or floats
    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or float")
    for row in m_b:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check if each row in m_a and m_b is of the same size
    row_length_a = len(m_a[0])
    if not all(len(row) == row_length_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_length_b = len(m_b[0])
    if not all(len(row) == row_length_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if the number of columns in m_a is equal to the number of rows
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            element_sum = 0
            for k in range(len(m_a[0])):
                element_sum += m_a[i][k] * m_b[k][j]
            new_row.append(element_sum)
        result.append(new_row)

    return result
