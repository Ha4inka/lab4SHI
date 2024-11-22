import numpy as np

def create_matrix(M, N):
    matrix = np.full((M, N), 0.5)
    for i in range(min(M, N)):
        matrix[i, i] = -1
    return matrix

M, N = 6, 6
result = create_matrix(M, N)
print(result)
print()
def get_submatrix(matrix, top_left, bottom_right):
    return matrix[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1]

top_left = [0, 1]
bottom_right = [1, 2]
submatrix = get_submatrix(result, top_left, bottom_right)
print(submatrix)