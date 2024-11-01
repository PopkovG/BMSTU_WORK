class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def __str__(self):
        # Сбор всех пар ключ-значение из таблицы
        all_items = [(k, v) for bucket in self.table for k, v in bucket]
        # Сортировка по значению
        sorted_items = sorted(all_items, key=lambda x: x[1])
        # Форматированный вывод отсортированных элементов
        return "{" + ", ".join(f"{k}: {v}" for k, v in sorted_items) + "}"

# Пример использования
ht = HashTable()
ht.insert("apple", 1)
ht.insert("banana", 3)
ht.insert("orange", 2)
ht.insert("cherry", 4)

print(ht.get("banana"))  # Вывод: 3
print(ht)
