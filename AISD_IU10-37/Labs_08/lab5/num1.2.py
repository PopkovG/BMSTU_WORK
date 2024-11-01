class HashTable:
    def __init__(self, size=2):
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

    def check_collision(self, key1, key2):
        index1 = self.hash_function(key1)
        index2 = self.hash_function(key2)
        if index1 == index2:
            # Выводим элементы в корзине, если оба ключа имеют одинаковый индекс
            collision_bucket = [f"{k}: {v}" for k, v in self.table[index1]]
            return f"Collision in Bucket {index1}: " + ", ".join(collision_bucket)
        else:
            return "No collision between the keys."

    def __str__(self):
        # Сбор всех пар ключ-значение из таблицы
        all_items = [(k, v) for bucket in self.table for k, v in bucket]
        # Сортировка по значению
        sorted_items = sorted(all_items, key=lambda x: x[1])
        # Форматированный вывод отсортированных элементов
        return "{" + ", ".join(f"{k}: {v}" for k, v in sorted_items) + "}"

# Пример использования
ht = HashTable()
ht.insert("cherry", 1)
ht.insert("banana", 3)
ht.insert("orange", 2)
ht.insert("apple", 4)

print(ht.get("banana"))  # Вывод: 3
print(ht)
print(ht.check_collision("banana", "cherry"))
