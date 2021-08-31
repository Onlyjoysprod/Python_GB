# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

num_1 = 5
num_2 = 6

# or
bit_or = num_1 | num_2
# xor
bit_xor = num_1 ^ num_2
# and
bit_and = num_1 & num_2
# сдвиг вправо на 2
shift_right = num_1 >> 2
# сдвиг влево на 2
shift_left = num_1 << 2

print(f'Побитовое or: {bin(bit_or)}')
print(f'Побитовое xor: {bin(bit_xor)}')
print(f'Побитовое and: {bin(bit_and)}')
print(f'Битовый сдвиг вправо на 2: {bin(shift_right)}')
print(f'Битовый сдвиг влево на 2: {bin(shift_left)}')
