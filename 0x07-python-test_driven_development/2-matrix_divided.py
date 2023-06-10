#!/usr/bin/python3
def matrix_divided(matrix, div):
    type_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(type_msg)
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(type_msg)
        for i in rows:
            if type(i) is not int and type(i) is not float:
                raise TypeError(type_msg)
    rowlen = len(matrix[0])
    for r in matrix:
        if rowlen != len(r):
            raise TypeError("Each row of the matrix must have the same size")
    return ([list(map(lambda n: round(n / div, 2), row)) for row in matrix])
