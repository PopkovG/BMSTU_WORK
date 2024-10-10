# Задание 2

import numpy as np
import time
import matplotlib.pyplot as plt

matrix_A = np.random.randint(0, (10**3)*3, ((10**2)*3, (10**2)*3))  # создали случ матрицу n*n
matrix_B = np.random.randint(0, (10**3)*3, ((10**2)*3, (10**2)*3))
#matrix_A = np.random.randint(0, 5, (3, 3))  # границы допустимых значений, размер матрицы
#matrix_B = np.random.randint(0, 5, (3, 3))

def multiplication_of_mats(m1, m2):
    matrix_C = np.full((len(m1), len(m2)), 0)
    for i in range(len(m1)):
        for j in range(len(m2)):
            for k in range(len(m1)):
                matrix_C[i][j] += m1[i][k] * m2[k][j]
    return (matrix_C)

def average_t(times):
    return sum(times) / len(times)

def build_graph(time, range_):
    plt.plot(range_, time)
    plt.xlabel('Размер массива, n')
    plt.ylabel('Среднее время выполнения, sec')
    plt.title('Зависимость времени от размера массива')
    plt.show()
    plt.grid(True)

def time_measurement():
    execution_time = []  # список времени выполнения
    n_values = []  # список значений при которых выполняются измерения
    for n in range(1, (10 ** 2)*3, 30):
        single_time = []  # список 5 замеров для каждого n
        m1 = matrix_A[:n, :n]
        m2 = matrix_B[:n, :n]
        for _ in range(5):
            start_time = time.time()
            multiplication_of_mats(m1, m2)
            end_time = time.time()
            single_time.append(end_time - start_time)

        avg_time = average_t(single_time)
        execution_time.append(avg_time)
        n_values.append(n)

    build_graph(execution_time, n_values)

time_measurement()