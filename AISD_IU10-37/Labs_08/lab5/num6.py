def find_pairs_with_sum(arr, target_sum):
    seen = set()
    pairs = set()

    for number in arr:
        complement = target_sum - number
        if complement in seen:
            pairs.add((min(number, complement), max(number, complement)))
        seen.add(number)

    return pairs


# Пример использования
array = [1, 2, 3, 4, 5]
target = 5
print(find_pairs_with_sum(array, target))  # Вывод: {(2, 3), (1, 4)}
