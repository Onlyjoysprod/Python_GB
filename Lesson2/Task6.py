# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

number = random.randint(0, 100)
user_answer = None
try_count = 0
max_try = 10

print('Число сгенерировано. Игра начинается')

while try_count != max_try:
    user_answer = int(input(f'Попытка {try_count + 1}. Ваш ответ: '))
    if user_answer == number:
        print(f'Верно! Ответ: {number}')
        break
    elif user_answer < number:
        print(f'Неверно! Число больше, чем {user_answer}')
    else:
        print(f'Неверно! Число меньше, чем {user_answer}')
    try_count += 1
else:
    print(f'Вы израсходовали {max_try} попыток. Игра окончена')
