def check_unique_elements(arr):
    # Преобразуем массив в множество и сравниваем длину
    return len(arr) == len(set(arr))

# Пример использования
array = [1, 2, 3, 4, 5]
print(check_unique_elements(array))  # Вывод: True

array_with_duplicates = [1, 2, 3, 4, 4]
print(check_unique_elements(array_with_duplicates))  # Вывод: False
