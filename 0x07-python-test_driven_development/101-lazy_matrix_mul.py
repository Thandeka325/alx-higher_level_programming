#!/usr/bin/python3
"""
This module multiplies two matrices using NumPy.
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a: First matrix (list of lists of integers or floats)
        m_b: Second matrix (list of lists of integers or floats)

    Returns:
        A new matrix representing the product of m_a and m_b.
    """
    return np.matmul(m_a, m_b)
