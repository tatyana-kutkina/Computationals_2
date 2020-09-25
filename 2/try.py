import matrix_funs as mf
import numpy as np
from numpy import linalg as LA
import math
import copy

eps = 10**(-5)

name = "/home/tatyana/PycharmProjects/Computationals_2/matrix_try.txt"

a_ext = np.loadtxt(name)
n, m = a_ext.shape
a = a_ext[:, 0:m-1]
b = a_ext[:,m-1 ]

E_matrix = np.eye(n)
D_matrix = np.zeros((n, n))

for i in range(n):
    D_matrix[i][i] = a[i][i]

D_inv = LA.inv(D_matrix)        # матрица обратная к D
C = D_inv.dot(a)
H_D = E_matrix - C
g_D = D_inv.dot(b)      # столбец g_D
H_norm = mf.matrix_norm(H_D)


H = H_D
H_L = np.zeros((n, n))
H_R = np.zeros((n, n))

for i in range(1, n):
    j = 0
    while j != i:
        H_L[i][j] = H[i][j]
        j += 1

for i in range(0, n):
    j = n-1
    while j >= i:
        H_R[i][j] = H[i][j]
        j -= 1

m_1 = LA.inv(E_matrix - H_L)       # матрица (E - H_L)^(-1)
m_2 = m_1.dot(H_R)

x_k = np.zeros(n)
x_k_1 = m_1.dot(g_D)
k = 1
while max(np.abs(x_k_1 - x_k)) > eps:
    x_k = copy.copy(x_k_1)
    x_k_1 = m_2.dot(x_k) + m_1.dot(g_D)
    k += 1



print("Решение, полученное методом Зейделя: ", x_k_1)
print("Потребовавшееся количество операций: ", k)
