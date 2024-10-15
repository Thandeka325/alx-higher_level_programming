#!/usr/bin/python3
"""
Defines a Pascal's Triangle Function.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n levels.

    Args:
        n (int): The number of levels in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
