# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('Введите трехзначное число: '))

hund = number // 100
ten = (number % 100) // 10
unit = number % 10

sum_result = hund + ten + unit
mult_result = hund * ten * unit

print(f'Сумма цифр числа {number} равна {sum_result}. Произведение рано {mult_result}')
