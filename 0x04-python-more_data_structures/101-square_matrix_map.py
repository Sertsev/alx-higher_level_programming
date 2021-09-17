#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if matrix == []: return 0
    return list(map(lambda x: (list(map(lambda x: x*x, x))), matrix))
