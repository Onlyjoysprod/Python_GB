# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

num_dict = {}

for num in range(2, 10):
    num_dict[num] = []
    for i in range(2, 100):
        if i % num == 0:
            num_dict[num].append(i)
    print(f'Для числа {num} кратны: {len(num_dict[num])} чисел. Это: {num_dict[num]}')
