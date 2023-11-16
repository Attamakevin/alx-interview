#!/usr/bin/python3
"""function to rotate_2d_matrix.py
"""


def transpose_matrix(matrix, n):
    """transpose matrix method

    Args:
                    matrix (_type_): _description_
    """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """reverse matrix

    Args:
                    matrix (_type_): _description_
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix method

    Args:
                    matrix (_type_): _description_
    """
    n = len(matrix)

    """transpose matrix
    """

    transpose_matrix(matrix, n)
    """Reverse matrix
    """
    reverse_matrix(matrix)

    return matrix
