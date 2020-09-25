# чтение матрицы из файла
# выделяем матрицу A и столбец b, если матрица расширенная

import numpy as np

def read_matrix(file_name):
    lines = []
    with open(file_name) as inf:
        for line in inf:
            line = line.strip()
            lines.append(line)
    ss = lines[0].split()
    l = len(ss)
    n = len(lines)
    if n != l:      # если матрица расширенная
        b = []
        a = []
        for i in range(len(lines)):
            s = lines[i].split()
            l = len(s)
            b.append(float(s[l - 1]))
            s = s[:-1]
            a.append([float(j) for j in s])
        return a, b
    else:  # если обычная квадратная матрица
        a = []
        for i in range(len(lines)):
            s = lines[i].split()
            a.append([float(j) for j in s])
        return a


