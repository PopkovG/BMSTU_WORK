def fibonacci_v1(n):
    """Рекурсивная реализация расчета чисел Фибоначчи"""
    print(f' Вызов fibonacci_v1({n})')
    if n == 0:
        return 0  # Базовый случай
    elif n == 1:
        return 1  # Базовый случай
    else:
        return fibonacci_v1(n - 1) + fibonacci_v1(n - 2)

fibonacci_v1(15)