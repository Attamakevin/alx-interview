#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    result = []
    for i in range(n):
        row = []
        C = 1
        for j in range(i + 1):
            row.append(C)
            C = C * (i - j) // (j + 1)
        result.append(row)

    return result

