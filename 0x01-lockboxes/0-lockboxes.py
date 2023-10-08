#!/usr/bin/python3
"""
checks number of locked boxes that can be opened
"""


def canUnlockAll(boxes):
    """
    checks number of locked boxes that can be opened
    """

    keys = set([0])

    for box in range(len(boxes)):
        if box in keys:
            print(keys)
            keys.update(boxes[box])

    return len(keys) == len(boxes)
