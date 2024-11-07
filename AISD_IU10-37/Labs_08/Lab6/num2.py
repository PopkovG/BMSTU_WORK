def Q(M, N):

    dp = [[0] * (N + 1) for _ in range(M + 1)]

    # Заполнение базовых случаев
    for n in range(N + 1):
        dp[1][n] = 1  # Для любого N, Q(1, N) = 1

    for m in range(M + 1):
        dp[m][1] = 1  # Для любого M, Q(M, 1) = 1

    # Заполнение таблицы по рекуррентной формуле
    for m in range(2, M + 1):
        for n in range(2, N + 1):
            if m < n:
                dp[m][n] = dp[m][m]  # Если M < N, то Q(M, N) = Q(M, M)
            elif m == n:
                dp[m][n] = 1 + dp[m][m - 1]  # Если M = N, то Q(M, N) = 1 + Q(M, M-1)
            else:
                dp[m][n] = dp[m][n - 1] + dp[m - n][n]  # Если M > N, то Q(M, N) = Q(M, N-1) + Q(M-N, N)

    return dp[M][N]


# Пример использования:
M = 123
N = 3
print(Q(M, N))  # Выводит количество разложений числа 5 с числами, не превосходящими 3
