# Определить, какое число в массиве встречается чаще всего.

num_list = [1, 3, 3, 5, 4, 2, 1, 6, 4, 6, 2, 6, 5, 6, 5]
num_max = num_list[0]

for num in num_list:
    if num_list.count(num_max) < num_list.count(num):
        num_max = num

print(num_max)
