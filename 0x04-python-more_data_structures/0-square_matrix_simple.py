#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cpy_matrix = matrix.copy()
    for i in range(len(matrix)):
        cpy_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return (cpy_matrix)
