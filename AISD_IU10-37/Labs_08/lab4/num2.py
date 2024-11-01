#стек на основе связного списка
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.top.data
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return self.top is None

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

# Пример использования LinkedListStack
linked_stack = LinkedListStack()
linked_stack.push(10)
linked_stack.push(20)
linked_stack.push(30)
print(linked_stack.pop())  # Вывод: 30
print(linked_stack.peek())  # Вывод: 20
print(linked_stack.size())  # Вывод: 2
