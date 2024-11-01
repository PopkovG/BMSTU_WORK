#очередь на основе массива.
class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("dequeue from empty queue")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("front from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Пример использования ArrayQueue
queue = ArrayQueue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
print(queue.dequeue())  # Вывод: 'a'
print(queue.front())     # Вывод: 'b'
print(queue.size())      # Вывод: 2
