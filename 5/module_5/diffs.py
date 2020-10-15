import numpy as np
from numpy import linalg as LA


def Euler(A, t1, t2, h0, h, y0):
    n, m = A.shape
    E = np.eye(n)
    W = E + A * h
    size = int((t2 - t1) / h) + 1
    y = [[0] * m for i in range(size)]
    y[0] = y0
    for i in np.arange(1, len(y)):
        y[i] = W.dot(y[i - 1])

    k = int(h0/h)

    res1 = [y[i][0] for i in range(0, len(y), k)]
    res2 = [y[i][1] for i in range(0, len(y), k)]
    return res1, res2


def Rev_Euler(A, t1, t2, h0, h, y0):
    n, m = A.shape
    E = np.eye(n)
    W = E - A * h
    W = LA.inv(W)

    size = int((t2 - t1) / h) + 1
    y = [[0] * m for i in range(size)]
    y[0] = y0
    for i in np.arange(1, len(y)):
        y[i] = W.dot(y[i - 1])

    k = int(h0 / h)

    res1 = [y[i][0] for i in range(0, len(y), k)]
    res2 = [y[i][1] for i in range(0, len(y), k)]
    return res1, res2


def Adams(A, t1, t2, h0, h, y0, y1):
    n, m = A.shape
    E = np.eye(n)

    size = int((t2 - t1) / h) + 1
    y = [[0] * m for i in range(size)]
    y[0] = y0
    y[1] = y1
    for i in np.arange(2, len(y)):
        y[i] = (E + 3*h*A/2).dot(y[i-1]) - (h*A/2).dot(y[i-2])

    k = int(h0 / h)

    res1 = [y[i][0] for i in range(0, len(y), k)]
    res2 = [y[i][1] for i in range(0, len(y), k)]
    return res1, res2