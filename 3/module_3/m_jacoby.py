
# вычислить наибольшый наддиаг. элемент и его координаты
def maxx(A):
    mx = A[0][1]
    n = len(A)
    mx_i = 0
    mx_j = 1
    for i in range(n):
        for j in range(i, n):
            if abs(A[i][j]) > mx and i != j:
                mx = A[i][j]
                mx_i = i
                mx_j = j
    return mx, mx_i, mx_j
