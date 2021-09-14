# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""Примечание: не силен в таких задачах. Пришлось подглядывать в чужие решения и составлять свое на их основе"""

from collections import deque

HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
           0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
           10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def hex_sum(x, y):
    result = deque()
    transfer = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)

    while x:
        if y:
            res = HEX_NUM[x.pop()] + HEX_NUM[y.pop()] + transfer
        else:
            res = HEX_NUM[x.pop()] + transfer
        transfer = 0
        if res < 16:
            result.appendleft(HEX_NUM[res])
        else:
            result.appendleft(HEX_NUM[res - 16])
            transfer = 1

    if transfer:
        result.appendleft('1')
    return list(result)


def hex_multiply(x, y):
    result = deque()
    spam = deque([deque() for _ in range(len(y))])
    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = HEX_NUM[y.pop()]

        for i2 in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * HEX_NUM[x[i2]])

        for el in range(i):
            spam[i].append(0)

    transfer = 0

    for el in range(len(spam[-1])):
        res = transfer
        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()

        if res < 16:
            result.appendleft(HEX_NUM[res])
        else:
            result.appendleft(HEX_NUM[res % 16])
            transfer = res // 16

    if transfer:
        result.appendleft(HEX_NUM[transfer])

    return list(result)


a = list(input('Ввелите первое шестнадцатеричное число: ').upper())
b = list(input('Ввелите второе шестнадцатеричное число: ').upper())

print(f'{a} + {b} = {hex_sum(a, b)}\n'
      f'{a} * {b} = {hex_multiply(a, b)}')
