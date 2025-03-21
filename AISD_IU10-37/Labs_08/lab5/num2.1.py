class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def hash_function(self, key):
        return hash(key) % self.size

    def probe(self, index):
        # Линейное пробирование
        return (index + 1) % self.size

    def insert(self, key, value):
        if self.count >= self.size / 2:  # Увеличиваем размер при загрузке > 50%
            self.resize()

        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = self.probe(index)

        self.table[index] = (key, value)
        self.count += 1

    def get(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = self.probe(index)
            if index == self.hash_function(key):  # Вернулись в начальную позицию
                break
        return None

    def remove(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None  # Удаляем элемент
                self.count -= 1
                return True
            index = self.probe(index)
            if index == self.hash_function(key):  # Вернулись в начальную позицию
                break
        return False

    def resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])

    def __str__(self):
        # Сбор всех пар ключ-значение из таблицы
        all_items = [(k, v) for k, v in self.table if k is not None]
        # Сортировка по значению
        sorted_items = sorted(all_items, key=lambda x: x[1])
        # Форматированный вывод отсортированных элементов
        return "{" + ", ".join(f"{k}: {v}" for k, v in sorted_items) + "}"

# Пример использования
ht = HashTable()
ht.insert("apple", 1)
ht.insert("banana", 3)
ht.insert("orange", 2)

print(ht.get("banana"))  # Вывод: 3
ht.remove("apple")
print(ht)
