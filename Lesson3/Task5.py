# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

num_list = [7, -3, 2, 4, -1, 8, 3, 0, -4, 9]
min_num = num_list[0]
result = 0

# Сначала находим наименьшее число в массиве
for num in num_list:
    if num < min_num:
        min_num = num
# Затем находим максимальный отрицательный элемент
for num in num_list:
    if 0 > num > min_num:
        result = num

print(f'Максимальный отрицательный элемент: {result}. Индекс элемента: {num_list.index(result)}')
