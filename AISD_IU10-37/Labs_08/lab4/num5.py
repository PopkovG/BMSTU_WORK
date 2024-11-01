#дек на основе массива
class ArrayDeque:
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.deque.pop(0)
        raise IndexError("remove from empty deque")

    def remove_rear(self):
        if not self.is_empty():
            return self.deque.pop()
        raise IndexError("remove from empty deque")

    def is_empty(self):
        return len(self.deque) == 0

    def size(self):
        return len(self.deque)

# Пример использования ArrayDeque
deque = ArrayDeque()
deque.add_front(5)
deque.add_rear(10)
deque.add_front(1)
print(deque.remove_front())  # Вывод: 1
print(deque.remove_rear())   # Вывод: 10
print(deque.size())          # Вывод: 1
