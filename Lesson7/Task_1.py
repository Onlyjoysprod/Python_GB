# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random

rand_list = [random.randint(-100, 100) for _ in range(10)]


def sort_bubble(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        n += 1
    return arr


print(f'Исходный массив: {rand_list}')
print(f'Отсортированный массив: {sort_bubble(rand_list)}')
