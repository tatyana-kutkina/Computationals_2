import numpy as np


def f(x, y):
    val = 1 - np.sin(1.25 * x + y) - (0.1 * y) / (2 + x)
    return val

def Euler(y, x, h):
    for i in range(1, len(y)):
        val_1 = f(x[i - 1], y[i - 1])
        Y_m = y[i - 1] + h * val_1
        val_2 = f(x[i], Y_m)
        y[i] = y[i - 1] + h / 2 * (val_1 + val_2)
    return y

def Runge_Kut(y, x, h):

    for i in range(1, len(y)):
        k1 = h*f(x[i-1], y[i-1])
        k2 = h*f(x[i-1] + h/2, y[i-1] +k1/2)
        k3 = h*f(x[i-1] + h/2, y[i-1] +k2/2)
        k4 = h*f(x[i-1] + h, y[i-1] +k3)
        y[i] = y[i-1] + (k1 + 2*k2 + 2*k3 +k4)*(1/6)
    return y

def Adams_ex(y, x, h):
    for i in range(5, len(y)):
        q_4 = h*f(x[i-5], y[i-5])
        q_3 = h*f(x[i-4], y[i-4])
        q_2 = h*f(x[i-3], y[i-3])
        q_1 = h*f(x[i-2], y[i-2])
        q_0 = h*f(x[i-1], y[i-1])
        y[i] = y[i-1] + (1/720)*(1901*q_0 - 2774*q_1 + 2616*q_2 - 1274*q_3 + 251*q_4)
    return y

def Adams_in(y_ex, y, x, h):
    for i in range(4, len(y)):
        q_3 = h * f(x[i - 4], y[i - 4])
        q_2 = h * f(x[i - 3], y[i - 3])
        q_1 = h * f(x[i - 2], y[i - 2])
        q_0 = h * f(x[i - 1], y[i - 1])

        y_0 = y_ex[i]
        q_4 = h*f(x[i], y_0)
        y_1 = y[i-1] + (1/720)*(251*q_4 + 646*q_0 - 264*q_1 + 106*q_2 - 19*q_3)
        k=0
        while np.abs(y_1 - y_0) >= 0.0001 and k!=10:
            y_0 = y_1
            q_4 = h * f(x[i], y_0)
            y_1 = y[i - 1] + (1 / 720) * (251 * q_4 + 646 * q_0 - 264 * q_1 + 106 * q_2 - 19 * q_3)
            k+=1
        y[i] = y_1

    return y
