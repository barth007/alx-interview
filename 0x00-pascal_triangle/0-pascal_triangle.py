#!/usr/bin/python3
"""computes a pascal triangle"""


def pascal_triangle(n):
    """
    pascal_trianle: returns a list of numbers

    Args:
        n(integer): input
    """

    pascal = []
    if n <= 0:
        return pascal
    for i in range(0, n):
        row = []
        value = 1
        for j in range(0, i + 1):
            if i == 0 or j == i:
                row.append(1)
            else:
                row.append(value)
            value = value * (i - j) // (j + 1)
        pascal.append(row)

    return pascal
