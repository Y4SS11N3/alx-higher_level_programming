#!/usr/bin/python3
"""
Module providing a function to divide each element of a matrix.
"""


def matrix_divided(matrix, divisor):
    """
    Divides each element of a matrix by a divisor.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        divisor (int/float): The number to divide by.

    Raises:
        TypeError: If elements in matrix are not ints or floats.
        TypeError: If rows in matrix have different sizes.
        TypeError: If divisor is not an int or float.
        ZeroDivisionError: If divisor is 0.

    Returns:
        list: New matrix with the division result, rounded to 2 decimal places.
    """
    if not isinstance(divisor, (int, float)):
        raise TypeError("div must be a number")
    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if any(not isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if any(not all(isinstance(el, (int, float)) for el in row)
           for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(element / divisor, 2) for element in row] for row in matrix]
