#!/usr/bin/python3
"""
Module that rotates a 2d clockwise by 90 degrees
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the matrix 90 degrees clockwise in place.


    Args:
        matrix (list of lists): the 2D matrix to be rotated.


    Returns:
        None. Modify matrix in place.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
