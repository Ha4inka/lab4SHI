import numpy as np

def create_diamond_matrix(size, value):
    matrix = np.zeros((size, size), dtype=int)
    mid = size // 2

    for i in range(size):
        offset = abs(mid - i)
        matrix[i, offset] = value
        matrix[i, size - offset - 1] = value

    return matrix

size = 7
value = 13
result = create_diamond_matrix(size, value)
print(result)
