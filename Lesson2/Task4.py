# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

n = int(input('Укажите кол-во n элементов: '))
range_number = 1
result = 0

for i in range(n):
    result += range_number
    range_number /= -2

print(result)
