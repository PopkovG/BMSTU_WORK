#очередь на основе связного списка.
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = ListNode(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.front.data
            self.front = self.front.next
            if self.front is None:  # If the queue is now empty, update rear
                self.rear = None
            return dequeued_item
        raise IndexError("dequeue from empty queue")

    def front_item(self):
        if not self.is_empty():
            return self.front.data
        raise IndexError("front from empty queue")

    def is_empty(self):
        return self.front is None

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

# Пример использования LinkedListQueue
linked_queue = LinkedListQueue()
linked_queue.enqueue(1)
linked_queue.enqueue(2)
linked_queue.enqueue(3)
print(linked_queue.dequeue())  # Вывод: 1
print(linked_queue.front_item()) # Вывод: 2
print(linked_queue.size())      # Вывод: 2
