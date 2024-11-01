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
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        if not current_node:
            print("Список пуст.")
            return
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def delete_from_beginning(self):
        if not self.head:
            print("Ошибка: список пуст.")
            return
        self.head = self.head.next

    def delete_from_end(self):
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


def main():
    linked_list = LinkedList()

    while True:
        print("nВыберите действие:")
        print("1. Добавить элемент в начало")
        print("2. Добавить элемент в конец")
        print("3. Просмотреть список")
        print("4. Удалить элемент из начала")
        print("5. Удалить элемент из конца")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            data = input("Введите значение элемента: ")
            linked_list.insert_at_beginning(data)
            print(f"Элемент {data} добавлен в начало списка.")

        elif choice == '2':
            data = input("Введите значение элемента: ")
            linked_list.insert_at_end(data)
            print(f"Элемент {data} добавлен в конец списка.")

        elif choice == '3':
            print("Содержимое списка:")
            linked_list.display()

        elif choice == '4':
            linked_list.delete_from_beginning()
            print("Элемент удален из начала списка.")

        elif choice == '5':
            linked_list.delete_from_end()
            print("Элемент удален из конца списка.")

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
