# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
import timeit
import cProfile


def task_1_solution_1(from_number, to_number):
    """Алгоритм из задания 1 урока №3.
    (В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9).
    Только диапазон теперь определяется параметрами функции."""
    num_dict = {}
    for num in range(from_number, to_number):
        num_dict[num] = []
        for i in range(2, 100):
            if i % num == 0:
                num_dict[num].append(i)
        # print(f'Для числа {num} кратны: {len(num_dict[num])} чисел. Это: {num_dict[num]}')


print(f'Скорость выполнения кода при работе функции в диапазоне от 2 до 10: '
      f'{timeit.timeit("task_1_solution_1(2, 10)", globals=globals(), number=1)}')
cProfile.run('task_1_solution_1(2, 10)')

print(f'Скорость выполнения кода при работе функции в диапазоне от 2 до 100: '
      f'{timeit.timeit("task_1_solution_1(2, 100)", globals=globals(), number=1)}')
cProfile.run('task_1_solution_1(2, 100)')

print(f'Скорость выполнения кода при работе функции в диапазоне от 2 до 1000: '
      f'{timeit.timeit("task_1_solution_1(2, 1000)", globals=globals(), number=1)}')
cProfile.run('task_1_solution_1(2, 1000)')
