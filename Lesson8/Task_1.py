# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

from hashlib import sha1

s = input('Введите строку из латинских символов: ').lower()


def sub_counter(s):
    sub_set = set()

    for i in range(len(s) + 1):
        for j in range(i + 1, len(s) + 1):
            sub = sha1(s[i:j].encode('utf-8')).hexdigest()
            sub_set.add(sub)

    return len(sub_set)


print(f'Строка {s} содержит {sub_counter(s)} подстрок')
