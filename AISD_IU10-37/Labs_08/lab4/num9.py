def evaluate_postfix(expression):
    stack = []

    for char in expression:
        # Если символ — число, добавляем его в стек
        if char.isdigit():
            stack.append(int(char))
        else:
            # Если символ — оператор, извлекаем два верхних элемента из стека
            b = stack.pop()
            a = stack.pop()

            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
            elif char == '^':
                stack.append(a ** b)

    return stack.pop()


# Пример использования
expression = "33*54*+9-" #(2*3) + (5*4) - 9
result = evaluate_postfix(expression)
print ("Результат: ", result)

