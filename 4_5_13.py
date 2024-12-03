import numpy as np
def create_secondary_diag_matrix(K, N):
    matrix = np.zeros((K, K), dtype=int)
    for i in range(K):
        matrix[i, K - i - 1] = N
    return matrix

K = 4
N = 13
result = create_secondary_diag_matrix(K, N)
print(result)
