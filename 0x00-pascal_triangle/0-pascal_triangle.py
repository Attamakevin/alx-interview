#!/usr/bin/python3
#implementation of paschal triangle
def pascal_triangle(n):
    new_list = []
    if n <= 0:
        return new_list
    else:
        for x in range(n):
            new_list.append("".join(map(str, str(11**x))))
        return new_list

