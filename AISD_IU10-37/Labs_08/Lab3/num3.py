def separate_positive_negative(L):
    L1 = []  # Список для положительных элементов
    L2 = []  # Список для отрицательных элементов

    for element in L:
        if element > 0:
            L1.append(element)  # Добавляем положительный элемент в L1
        elif element == 0:
            L1.append(element) # Я считаю, что 0 это положительный элемент
        elif element < 0:
            L2.append(element)  # Добавляем отрицательный элемент в L2

    # Добавим сортировочку, чтоб было красивее
    L1.sort()
    L2.sort()

    return L1, L2


# Пример использования
L = [10, -5, 3, -1, 0, 7, -8]
L1, L2 = separate_positive_negative(L)

print("Положительные элементы:", L1)
print("Отрицательные элементы:", L2)
