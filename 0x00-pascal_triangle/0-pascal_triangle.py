#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""
def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    new_list =[]
    if n <= 0:
        return new_list

    for x in range(n):
        new_list.append("".join(map(str, str(11**x))))
    return new_list

