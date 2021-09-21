# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

rand_list = [random.uniform(0, 50) for _ in range(10)]


def sort_merge(lst):

    def arr_half(arr):
        if len(arr) < 2:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = arr_half(left)
        right = arr_half(right)

        return arr_merge(left, right)

    def arr_merge(arr1, arr2):
        result = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        result += arr1[i:]
        result += arr2[j:]

        return result

    return arr_half(lst)


print(f'Исходный массив: {rand_list}')
print(f'Отсортированный массив: {sort_merge(rand_list)}')
