#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr = []
    for i in matrix:
        sqrr = []
        for j in i:
            j = j*j
            sqrr.append(j)
        sqr.append(sqrr)
    return sqr
