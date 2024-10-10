import random
import timeit
import functools
import matplotlib.pyplot as plt
import numpy as np
def odd_even_sort(arr):
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, n-1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
        for i in range(1, n-1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

average_times_odd_even_sort = []

@functools.lru_cache(maxsize=None)
def timing_decorator(ndigits: int, number: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                number=number,
            )
            return round(usage_time / number, ndigits)

        return wrapper

    return decorator

max_n = 100001
max_vector = np.array([random.randint(1, 100) for _ in range(max_n)])

ndigits = 6
number_of_runs = 5

n_values = [100, 1000, 2000, 3500, 5000, 10000, 20000, 25000]
average_times_odd_even_sort = []
@timing_decorator(ndigits, number_of_runs)
def calculate_odd_even_sort(vector):
    odd_even_sort(vector)

for n in n_values:
    print(n)
    average_time = calculate_odd_even_sort(max_vector[:n].copy())
    average_times_odd_even_sort.append(average_time)

plt.plot(n_values, average_times_odd_even_sort, linestyle='-', color='b', label='Odd-Even Sort')
plt.title('Зависимость времени сортировки от n')
plt.xlabel('n')
plt.ylabel('Среднее время выполнения (секунды)')
plt.legend()
plt.savefig('odd_even_sort_time.png')