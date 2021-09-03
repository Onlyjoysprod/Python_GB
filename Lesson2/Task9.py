# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

numbers = input('Введите натуральные числа через пробел: ')
summ = 0
result_num = 0

for el in numbers.split(' '):
    local_sum = sum(map(int, el))
    if summ < local_sum:
        summ = local_sum
        result_num = el

print(f'Наибольшее число {result_num} с суммой цифр {summ}')
