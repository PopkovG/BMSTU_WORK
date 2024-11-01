class Node:
    """Класс для представления узла списка."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Класс для представления линейного однонаправленного списка."""

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Вставка элемента в начало списка."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Вставка элемента в конец списка."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_position(self, data, position):
        """Вставка элемента в середину списка по заданной позиции."""
        if position < 0:
            print("Ошибка: позиция не может быть отрицательной.")
            return
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None:
                print("Ошибка: позиция выходит за пределы списка.")
                return
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def display(self):
        """Просмотр элементов списка."""
        current_node = self.head
        if not current_node:
            print("Список пуст.")
            return
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def search(self, key):
        """Поиск элемента в списке."""
        current_node = self.head
        position = 0
        while current_node:
            if current_node.data == key:
                return position
            current_node = current_node.next
            position += 1
        return -1  # Элемент не найден

    def delete_from_beginning(self):
        """Удаление элемента из начала списка."""
        if not self.head:
            print("Ошибка: список пуст.")
            return
        self.head = self.head.next

    def delete_from_end(self):
        """Удаление элемента из конца списка."""
        if not self.head:
            print("Ошибка: список пуст.")
            return
        if not self.head.next:
            self.head = None
            return

        second_last_node = self.head
        while second_last_node.next.next:
            second_last_node = second_last_node.next
        second_last_node.next = None

    def delete_from_position(self, position):
        """Удаление элемента из середины списка по заданной позиции."""
        if position < 0:
            print("Ошибка: позиция не может быть отрицательной.")
            return
        if not self.head:
            print("Ошибка: список пуст.")
            return
        if position == 0:
            self.delete_from_beginning()
            return

        current_node = self.head
        for _ in range(position - 1):
            if current_node is None or current_node.next is None:
                print("Ошибка: позиция выходит за пределы списка.")
                return
            current_node = current_node.next

        current_node.next = current_node.next.next

    def reverse(self):
        """Реверс списка (переворачивание списка задом на перед)."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# Пример использования линейного однонаправленного списка
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.display()  # 10 -> 20 -> 30 -> None

    linked_list.insert_at_beginning(5)
    linked_list.display()  # 5 -> 10 -> 20 -> 30 -> None

    linked_list.insert_at_position(15, 2)
    linked_list.display()  # 5 -> 10 -> 15 -> 20 -> 30 -> None

    print("Индекс элемента 20:", linked_list.search(20))  # Индекс элемента 20: 3

    linked_list.delete_from_beginning()
    linked_list.display()  # 10 -> 15 -> 20 -> 30 -> None

    linked_list.delete_from_end()
    linked_list.display()  # 10 -> 15 -> 20 -> None

    linked_list.delete_from_position(2)
    linked_list.display()  # 10 -> 20 -> None

    linked_list.reverse()
    linked_list.display()  # 20 -> 10 -> None
