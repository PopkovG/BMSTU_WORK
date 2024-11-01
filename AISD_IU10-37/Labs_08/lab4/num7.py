def check_parentheses_balance(s):
    # Инициализация стека
    stack = []

    # Словарь для соответствия открывающих и закрывающих скобок
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    # Переменная для отслеживания ошибок
    is_balanced = True

    for char in s:
        if char in matching_brackets.values():  # Если символ - открывающая скобка
            stack.append(char)
        elif char in matching_brackets.keys():  # Если символ - закрывающая скобка
            if stack and stack[-1] == matching_brackets[char]:  # Проверяем соответствие
                stack.pop()  # Убираем соответствующую открывающую скобку
            else:
                is_balanced = False  # Ошибка: несоответствие скобок
                break

    # Проверяем, остались ли незакрытые скобки в стеке
    if is_balanced and not stack:
        return True  # Скобки сбалансированы
    else:
        return False  # Скобки несбалансированы


# Пример использования
input_string = "{[)()]}"
if check_parentheses_balance(input_string):
    print("Скобки сбалансированы.")
else:
    print("Скобки несбалансированы.")
