# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
# и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.

while True:
    num1 = input('Введите первое число: ')
    num2 = input('Введите второе число: ')
    operation = input(f'Укажите какую операцию нужно выполнить ("+", "-", "*", "/") или введите 0 для выхода: ')
    if num1.isdigit() and num2.isdigit():
        if operation == '+' or operation == '-' or operation == '*' or operation == '/':
            if operation == '/' and int(num2) == 0:
                print('Нельзя делить на 0')
            else:
                result = eval(num1 + operation + num2)
                print(result)
        elif operation == '0':
            print('Выход из программы')
            break
        else:
            print('Данные введены некорректно')
    else:
        print('Данные введены некорректно')