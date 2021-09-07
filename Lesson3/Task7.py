# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

num_list = [1, 2, 5, 1, 7, 4, 0, 8]

# Без сортировки списка
min_1 = num_list[1]
min_2 = num_list[0]

for num in num_list:
    if num < min_1:
        min_1 = num
    elif num < min_2 and num != num_list[num_list.index(num)]:
        min_2 = num

print(min_1)
print(min_2)
