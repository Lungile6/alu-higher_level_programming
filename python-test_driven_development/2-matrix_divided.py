#!/usr/bin/python3
"""Define a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
        matrix: list of lists of integers or floats
        div: number (integer or float)

    Returns:
        list of lists: new matrix with elements divided by div
    """
    new_matrix = []
    mat = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
    elif len(matrix) == 1:
        for item in matrix[0]:
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
            mat.append(float("{:.2f}".format(item / div)))
        new_matrix.append(mat)
        return new_matrix
    else:
        length = len(matrix[0])
        for char in matrix:
            if not isinstance(char, list):
                raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
            if len(char) != length:
                raise TypeError("Each row of the matrix\
 must have the same size")
            for num in char:
                if type(num) not in [int, float]:
                    raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
                mat.append(float("{:.2f}".format(num / div)))
            new_matrix.append(mat)
            mat = []
        return new_matrix
