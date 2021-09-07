# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []

for i in range(4):
    matrix.append([])
    summ = 0
    for i2 in range(4):
        input_number = int(input(f'Введите {i2+1} элемент столбца {i+1}: '))
        summ += input_number
        matrix[i].append(input_number)
    matrix[i].append(summ)

for row in matrix:
    print(row)
