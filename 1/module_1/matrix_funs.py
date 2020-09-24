import numpy as np
import reverse_matrix as rv
import copy


# решение системы Ax = b
def Gauss(a, b):
    n = len(a)
    lines = copy.deepcopy(a)      # массив строк
    columns = []        # массив столбцов

    # массив столбцов
    for i in range(n):
        c = []
        for j in range(n):
            c.append(lines[j][i])
        columns.append(c)

    # прямой ход
    for i in range(n - 1):
        arr = columns[i][i:]
        a_max = max(arr)
        index = columns[i][i:].index(a_max) + i
        if index != i:
            lines[i], lines[index] = lines[index], lines[i]  # меняем местами строки, если нужно
            b[i], b[index] = b[index], b[i]

        for j in range(i + 1, n):
            x = lines[j][i] / lines[i][i] * (-1)
            for k in range(i, n):
                lines[j][k] += lines[i][k] * x
            b[j] += b[i] * x

    # обратный ход
    x = [0] * n  # вектор решения
    x[n - 1] = b[n - 1] / lines[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        summ = 0
        for j in range(i + 1, n):
            summ += lines[i][j] * x[j]
        x[i] = (b[i] - summ) / lines[i][i]
    x = np.around(x, 5)
    return x


# норма матрицы (по строкам)
def matrix_norm(a):
    sums = []
    for i in range(len(a)):
        arr = np.abs(a[i])
        sums.append(sum(arr))
    norm = max(sums)
    return norm


# число обсуловленности матрицы
def condition_number(a):
    a_reverse = rv.reverse_matrix(a)
    number = matrix_norm(a) * matrix_norm(a_reverse)
    return number

