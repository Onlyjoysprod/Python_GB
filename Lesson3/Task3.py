# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

random_list = [random.randint(0, 99) for num in range(10)]
print(random_list)

max_val = random_list[0]
min_val = random_list[0]

for num in random_list:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print(f'Максимально значение: {max_val}')
print(f'Минимальное значение: {min_val}')

index_max = random_list.index(max_val)
index_min = random_list.index(min_val)

random_list[index_max], random_list[index_min] = random_list[index_min], random_list[index_max]
print(random_list)
