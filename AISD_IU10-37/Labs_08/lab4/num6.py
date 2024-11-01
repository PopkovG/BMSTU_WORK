#дек на основе связного списка
class DequeNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedListDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_front(self, item):
        new_node = DequeNode(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def add_rear(self, item):
        new_node = DequeNode(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def remove_front(self):
        if not self.is_empty():
            removed_item = self.front.data
            if self.front == self.rear:  # Only one element was present
                self.front = self.rear = None
            else:
                self.front = self.front.next
                self.front.prev = None
            return removed_item
        raise IndexError("remove from empty deque")

    def remove_rear(self):
        if not self.is_empty():
            removed_item = self.rear.data
            if self.front == self.rear:  # Only one element was present
                self.front = self.rear = None
            else:
                self.rear = self.rear.prev
                self.rear.next = None
            return removed_item
        raise IndexError("remove from empty deque")

    def is_empty(self):
        return self.front is None

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

# Пример использования LinkedListDeque
linked_deque = LinkedListDeque()
linked_deque.add_front('x')
linked_deque.add_rear('y')
linked_deque.add_front('z')
print(linked_deque.remove_front())  # Вывод: 'z'
print(linked_deque.remove_rear())   # Вывод: 'y'
print(linked_deque.size())           # Вывод: 0
