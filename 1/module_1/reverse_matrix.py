import LU_decomposition
import numpy as np


# обратный ход
def reverse_move(a, b):
    n = len(a)
    x = [0] * n  # вектор решения
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        summ = 0
        for j in range(i + 1, n):
            summ += a[i][j] * x[j]
        x[i] = (b[i] - summ) / a[i][i]
    x = np.around(x, 3)
    return x


# прямой ход
def straight_move(a, b):
    n = len(a)
    x = [0] * n  # вектор решения
    x[0] = b[0] / a[0][0]
    for i in range(1, n):
        summ = 0
        for j in range(i):
            summ += a[i][j] * x[j]
        x[i] = (b[i] - summ) / a[i][i]
    x = np.around(x, 3)
    return x


# обратная матрица с помощью LU разложения
def reverse_matrix(a):
    L, U = LU_decomposition.LU_decompose(a)
    n = len(a)
    X = []
    E = [[0.0] * n for i in range(n)]
    for i in range(n):
        E[i][i] = 1.0

    for i in range(n):
        y = straight_move(L, E[i])
        x = reverse_move(U, y)
        X.append(x)

    return X
