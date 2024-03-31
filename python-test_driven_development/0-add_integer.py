#!/usr/bin/python3
"""
A function that adds 2 integers.
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b.

    Args:
        a: int or float
        b: int or float, default 98

    Returns:
        int: the addition of a and b
    """
    if type(a) not in [int, float] or a is None:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b is None:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
