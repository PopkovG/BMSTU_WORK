import random
import timeit
import functools
import matplotlib.pyplot as plt
import numpy as np
def stooge_sort(arr, l, h):
    if l >= h:
        return

    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]

    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        stooge_sort(arr, l, h - t)
        stooge_sort(arr, l + t, h)
        stooge_sort(arr, l, h - t)

average_times_stooge_sort = []

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

ndigits = 4
number_of_runs = 3

n_values = [100, 200, 500, 1000]
average_times_stooge_sort = []
@timing_decorator(ndigits, number_of_runs)
def calculate_stooge_sort(vector):
    stooge_sort(vector, 0, len(vector) - 1)

for n in n_values:
    print(n)

    average_time = calculate_stooge_sort(max_vector[:n].copy())
    average_times_stooge_sort.append(average_time)

plt.plot(n_values, average_times_stooge_sort, linestyle='-', color='g', label='Stooge Sort')
plt.title('Зависимость времени сортировки Stooge Sort от n')
plt.xlabel('n')
plt.ylabel('Среднее время выполнения (секунды)')
plt.legend()
plt.savefig('stooge_sort_time.png')