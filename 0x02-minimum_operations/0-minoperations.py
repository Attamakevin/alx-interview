#!/usr/bin/python3
'''
    a funcion to dtermine the minimum operation on a given array
    of n contents
'''


def minOperations(n):
    '''minimum number of operations methods'''
    if n <= 1:
        return 0  # It's impossible to achieve less than 2 'H' characters.

    operations = 0
    clipboard = 0
    current_h = 1

    while current_h < n:
        if n % current_h == 0:
            clipboard = current_h
            operations += 1

        current_h += clipboard
        operations += 1

    if current_h == n:
        return operations
    else:
        return 0  # It's impossible to achieve exactly n 'H' characters.
