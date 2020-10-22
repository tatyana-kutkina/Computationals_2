import numpy as np


# порядок погрешности O(h)
def sweep_method_1(p, q, r, f, a1, a2, b1, b2, a, b, x_0, x_1, n):
    h = round((x_1 - x_0) / n, 3)
    xx = [round(i, 3) for i in np.arange(x_0, x_1 + h, h)]
    A, B, C, G = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)

    B[0] = -a1 - a2 / h
    C[0] = -a2 / h
    G[0] = a

    A[n] = -b2 / h
    B[n] = -b1 - b2 / h
    G[n] = b

    for i in range(1, n):
        A[i] = -p(xx[i]) / h ** 2 - q(xx[i]) / (2 * h)
        B[i] = - r(xx[i]) - 2 * p(xx[i]) / h ** 2
        C[i] = q(xx[i]) / (2 * h) - p(xx[i]) / h ** 2
        G[i] = f(xx[i])

    s, t = [0]*(n+1), [0]*(n+1)
    for i in range(n+1):
        if i == 0:
            s[i] = C[i]/B[i]
            t[i] = -G[i]/B[i]
        else:
            s[i] = C[i]/(B[i] - A[i]*s[i-1])
            t[i] = (A[i]*t[i-1] - G[i])/(B[i] - A[i]*s[i-1])
    y = [0]*(n+1)
    y[n] = t[n]
    for i in range(n-1, -1, -1):
        y[i] = s[i]*y[i+1] + t[i]
    return xx, y


# порядок погрешности O(h^2)
def sweep_method_2(p, q, r, f, a1, a2, b1, b2, a, b, x_0, x_1, n):
    h = round((x_1 - x_0) / n, 3)
    xx = [0]*(n+2)
    for i in range(n+2):
        xx[i] = round(x_0 - h/2 +i*h,3)
    A, B, C, G = [0] * (n + 2), [0] * (n + 2), [0] * (n + 2), [0] * (n + 2)

    B[0] = -a1/2 -a2/h
    C[0] = a1/2 - a2/h
    G[0] = a

    A[n+1] = b1/2 - b2/h
    B[n+1] = -b1/2 - b2/h
    G[n+1] = b

    for i in range(1, n+1):
        A[i] = -p(xx[i]) / h ** 2 - q(xx[i]) / (2 * h)
        B[i] = - r(xx[i]) - 2 * p(xx[i]) / h ** 2
        C[i] = q(xx[i]) / (2 * h) - p(xx[i]) / h ** 2
        G[i] = f(xx[i])

    s, t = [0] * (n + 2), [0] * (n + 2)
    for i in range(n + 2):
        if i == 0:
            s[i] = C[i] / B[i]
            t[i] = -G[i] / B[i]
        else:
            s[i] = C[i] / (B[i] - A[i] * s[i - 1])
            t[i] = (A[i] * t[i - 1] - G[i]) / (B[i] - A[i] * s[i - 1])
    y = [0] * (n + 2)
    y[n+1] = t[n+1]
    for i in range(n, -1, -1):
        y[i] = s[i] * y[i + 1] + t[i]
    return xx, y
