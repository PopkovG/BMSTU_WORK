def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []  # Стек для операторов
    output = []  # Список для результата (постфиксная форма)

    for char in expression:
        # Если символ — операнд (число или переменная), добавляем его в выходной список
        if char.isalnum():
            output.append(char)
        # Если символ — '(', помещаем его в стек
        elif char == '(':
            stack.append(char)
        # Если символ — ')', извлекаем из стека до '('
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Удаляем '(' из стека
        else:  # Если символ — оператор
            while (stack and precedence(stack[-1]) >= precedence(char)):
                output.append(stack.pop())
            stack.append(char)

    # Извлекаем оставшиеся операторы из стека
    while stack:
        output.append(stack.pop())

    return ''.join(output)


# Пример использования
expression = "A+B*(C/D-E)"
postfix_expression = infix_to_postfix(expression)
print("Постфиксная форма:", postfix_expression)
