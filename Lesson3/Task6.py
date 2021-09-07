# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

random_list = [random.randint(0, 99) for num in range(10)]
print(random_list)

max_val = random_list[0]
min_val = random_list[0]

for num in random_list:
    if max_val < num:
        max_val = num
    if min_val > num:
        min_val = num

# Запоминаем индексы максимального и минимального значения в массиве
index_max, index_min = random_list.index(max_val), random_list.index(min_val)

# Проверяем на наличие элементов между полученными индексами и выводим результат
if index_max > index_min + 1:
    print(f'Между {min_val} и {max_val} находятся следующие значения: {random_list[index_min+1:index_max]}\n'
          f'Их сумма равна: {sum(random_list[index_min+1:index_max])}')
elif index_max < index_min - 1:
    print(f'Между {max_val} и {min_val} находятся следующие значения: {random_list[index_max+1:index_min]}\n'
          f'Их сумма равна: {sum(random_list[index_max+1:index_min])}')
else:
    print(f'Между {min_val} и {max_val} нет элементов')
