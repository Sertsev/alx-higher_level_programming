#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    _matrix = [[]] * len(matrix)
    if matrix == []:
        return 0
    _matrix = list(map(lambda x: (list(map(lambda x: x*x, x))), matrix))
    return _matrix
