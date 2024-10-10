import time
import numpy as np
import matplotlib.pyplot as plt

# Генерация случайного вектора
vec = np.random.randint(1, (10**4)*3, (10**4)*3)

# Функция для суммы чисел
def sum_of_nums(vector):
    sum_v = 0
    for i in vector:
        sum_v += i
    return sum_v

# Функция для произведения чисел
def product_of_nums(vector):
    product_v = 1
    for i in vector:
        product_v *= i
    return product_v

# Функция для поиска минимального значения
def search_of_min(vector):
    min_v = vector[0]
    for i in range(1, len(vector)):
        if min_v > vector[i]:
            min_v = vector[i]
    return min_v

# Функция для вычисления полинома методом Горнера
def horner_method(coefficients, x):
    result = coefficients[0]
    for coefficient in coefficients[1:]:
        result = result * x + coefficient
    return result

# Функция для среднего времени выполнения
def average_t(times):
    return sum(times) / len(times)

# Функция для построения графика
def build_graph(time, range_):
    plt.plot(range_, time)
    plt.xlabel('Размер массива, n')
    plt.ylabel('Среднее время выполнения, sec')
    plt.title('Зависимость времени от размера массива')
    plt.grid(True)
    plt.show()

# Измерение времени выполнения функций
def time_measurement():
    execution_time_sum = []
    execution_time_product = []
    execution_time_min = []
    execution_time_horner = []
    n_values = []

    # Пример коэффициентов полинома
    coefficients = np.random.randint(1, 100, 5)  # 5 случайных коэффициентов
    x = np.random.randint(1, 50)  # Точка, в которой будем вычислять полином

    for n in range(1, (10 ** 4) * 3, 300):
        v = vec[:n]
        single_times_sum = []
        single_times_product = []
        single_times_min = []
        single_times_horner = []

        for _ in range(5):
            start_time = time.time()
            sum_of_nums(v)
            end_time = time.time()
            single_times_sum.append(end_time - start_time)

            start_time = time.time()
            product_of_nums(v)
            end_time = time.time()
            single_times_product.append(end_time - start_time)

            start_time = time.time()
            search_of_min(v)
            end_time = time.time()
            single_times_min.append(end_time - start_time)

            start_time = time.time()
            horner_method(coefficients, x)
            end_time = time.time()
            single_times_horner.append(end_time - start_time)

        avg_time_sum = average_t(single_times_sum)
        execution_time_sum.append(avg_time_sum)

        avg_time_product = average_t(single_times_product)
        execution_time_product.append(avg_time_product)

        avg_time_min = average_t(single_times_min)
        execution_time_min.append(avg_time_min)

        avg_time_horner = average_t(single_times_horner)
        execution_time_horner.append(avg_time_horner)

        n_values.append(n)

    build_graph(execution_time_sum, n_values)
    build_graph(execution_time_product, n_values)
    build_graph(execution_time_min, n_values)
    build_graph(execution_time_horner, n_values)

# Запуск измерения времени
time_measurement()
