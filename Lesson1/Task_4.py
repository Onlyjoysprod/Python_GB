# Написать программу, которая генерирует в указанных пользователем границах
# случайное целое число,
# случайное вещественное число,
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Н
# апример, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random


def randomizer(start, end):
    if type(start) == int and type(end) == int:
        result = random.randint(start, end)
    elif type(start) == float and type(end) == float:
        result = random.uniform(start, end)
    elif type(start) == str and type(end) == str:
        result = chr(random.randint(ord(start), ord(end)))
    else:
        result = 'Границы указаны неверно'
    return result


start_int_val = int(input('Укажите начало границы для целых чисел: '))
end_int_val = int(input('Укажите конец границы для целых чисел: '))

start_float_val = float(input('Укажите начало границы для вещественных чисел: '))
end_float_val = float(input('Укажите конец границы для вещественных чисел: '))

start_chr_val = input('Укажите начало границы для символов: ')
end_chr_val = input('Укажите конец границы для символов: ')

print(f'Случайное значение в границах целых чисел: {randomizer(start_int_val, end_int_val)}')
print(f'Случайное значение в границах вещественных чисел: {randomizer(start_float_val, end_float_val)}')
print(f'Случайное значение в границах символов: {randomizer(start_chr_val, end_chr_val)}')
