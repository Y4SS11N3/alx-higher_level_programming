#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        squared_row = list(map(lambda x: x ** 2, row))
        new_matrix.append(squared_row)

    return (new_matrix)
