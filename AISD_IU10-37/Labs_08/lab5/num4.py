def check_intersection(arr1, arr2):
    # Создаем хеш-таблицу из второго массива
    hash_table = {element: True for element in arr2}

    # Проверяем, есть ли общие элементы
    for element in arr1:
        if element in hash_table:
            return True
    return False


# Пример использования
array1 = [1, 2, 3, 4]
array2 = [5, 6, 3, 7]
print(check_intersection(array1, array2))  # Вывод: True
