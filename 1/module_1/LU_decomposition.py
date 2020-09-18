def LU_decompose(a):
    n = len(a)

    # создаем нулевые матрицы для L и U
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    # находим матрицу U и L
    U[0] = [a[0][j] for j in range(n)]
    for j in range(n):
        L[j][0] = a[j][0]/U[0][0]

    for i in range(1, n):

        for j in range(i, n):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = a[i][j] - s1

        for j in range(i, n):
            s2 = sum(U[k][i] * L[j][k] for k in range(i))
            L[j][i] = (a[j][i] - s2) / U[i][i]
    return L, U

