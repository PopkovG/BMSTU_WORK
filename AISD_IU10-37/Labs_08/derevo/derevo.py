import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class RandomBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if not current_node:
            return Node(value)

        if random.random() < 0.5:  # Случайный выбор направления вставки
            current_node.left = self._insert_recursive(current_node.left, value)
        else:
            current_node.right = self._insert_recursive(current_node.right, value)

        return current_node

    def inorder_traversal(self):
        elements = []
        self._inorder_traversal_recursive(self.root, elements)
        return elements

    def _inorder_traversal_recursive(self, node, elements):
        if node:
            self._inorder_traversal_recursive(node.left, elements)
            elements.append(node.value)
            self._inorder_traversal_recursive(node.right, elements)

    def preorder_traversal(self):
        elements = []
        self._preorder_traversal_recursive(self.root, elements)
        return elements

    def _preorder_traversal_recursive(self, node, elements):
        if node:
            elements.append(node.value)
            self._preorder_traversal_recursive(node.left, elements)
            self._preorder_traversal_recursive(node.right, elements)

    def postorder_traversal(self):
        elements = []
        self._postorder_traversal_recursive(self.root, elements)
        return elements

    def _postorder_traversal_recursive(self, node, elements):
        if node:
            self._postorder_traversal_recursive(node.left, elements)
            self._postorder_traversal_recursive(node.right, elements)
            elements.append(node.value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        return self._search_recursive(node.left, value) or self._search_recursive(node.right, value)

    def print_tree(self):
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, level):
        if node:
            self._print_tree_recursive(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self._print_tree_recursive(node.left, level + 1)

    def is_empty(self):
        return not self.root

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if not node:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    def add_node(self, value):
        self.insert(value)

    def delete_node(self, value):
        self.root = self._delete_node_recursive(self.root, value)

    def _delete_node_recursive(self, current_node, value):
        if not current_node:
            return None
        if current_node.value == value:
            if not current_node.left:
                return current_node.right
            if not current_node.right:
                return current_node.left
            if random.random() < 0.5:
                return self._rotate_right_delete(current_node)
            else:
                return self._rotate_left_delete(current_node)
        elif value < current_node.value:
            current_node.left = self._delete_node_recursive(current_node.left, value)
        else:
            current_node.right = self._delete_node_recursive(current_node.right, value)
        return current_node

    def _rotate_right_delete(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        return x

    def _rotate_left_delete(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _find_min_value(self, node):
        while node.left:
            node = node.left
        return node.value

    def is_symmetric(self):
        return self._is_symmetric(self.root, self.root)

    def _is_symmetric(self, left, right):
        if self.height() == 0:
            return True
        if not left and not right:
            return True
        if not left or not right:
            return False
        value_symmetric = left.value == right.value
        order_symmetric = self._is_symmetric(left.left, right.right) and self._is_symmetric(left.right, right.left)
        return value_symmetric and order_symmetric

def menu(tree):
    while True:
        print("\nВыберите действие:")
        print("1. Вставить элемент")
        print("2. Удалить элемент")
        print("3. Найти элемент")
        print("4. Обход дерева")
        print("5. Проверить симметричность дерева")
        print("6. Вывести дерево")
        print("7. Проверить пустоту дерева")
        print("8. Определить высоту дерева")
        print("0. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            value = int(input("Введите значение для вставки: "))
            tree.insert(value)
        elif choice == "2":
            value = int(input("Введите значение для удаления: "))
            tree.delete_node(value)
        elif choice == "3":
            value = int(input("Введите значение для поиска: "))
            if tree.search(value):
                print("Элемент найден.")
            else:
                print("Элемент не найден.")
        elif choice == "4":
            print("Выберите тип обхода:")
            print("1. Прямой обход")
            print("2. Симметричный обход")
            print("3. Обратный обход")
            traversal_choice = input("Введите номер типа обхода: ")
            if traversal_choice == "1":
                print("Прямой обход:", tree.preorder_traversal())
            elif traversal_choice == "2":
                print("Симметричный обход:", tree.inorder_traversal())
            elif traversal_choice == "3":
                print("Обратный обход:", tree.postorder_traversal())
            else:
                print("Неверный выбор.")
        elif choice == "5":
            if tree.is_symmetric():
                print("Дерево симметрично.")
            else:
                print("Дерево не симметрично.")
        elif choice == "6":
            print("Дерево:")
            tree.print_tree()
        elif choice == "7":
            if tree.is_empty():
                print("Дерево пусто.")
            else:
                print("Дерево не пусто.")
        elif choice == "8":
            print("Высота дерева:", tree.height())
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, введите правильный номер.")

random_tree = RandomBinaryTree()
menu(random_tree)