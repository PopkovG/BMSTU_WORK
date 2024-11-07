def Q(M, N):
    # Базовые случаи
    if M == 1:
        return 1
    if N == 1:
        return 1
    if M < N:
        return Q(M, M)
    if M == N:
        return 1 + Q(M, M - 1)

    # Рекурсивный случай
    return Q(M, N - 1) + Q(M - N, N)


# Пример использования:
M = 123

N = 3
print(Q(M, N))  # Выводит количество разложений числа 5 с числами, не превышающими 3
