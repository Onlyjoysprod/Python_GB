# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

# Создаем матрицу
matrix = [[1, 0, -1, 2, 3],
          [-2, 0, 1, 4, 2],
          [2, 1, 3, 1, 5],
          [-3, 2, 4, -5, 0]]
# Создаем пустые списки, в которые положим значения столбцов и их минимальные значения.
column_numbers = []
min_numbers = []

# Запускаем цикл в пределах кол-ва столбцов. Вычисляем элементы каждого столбца и заносим в список.
for i in range(len(matrix[0])):
    column_numbers.append([])
    for i2 in range(len(matrix)):
        column_numbers[i].append(matrix[i2][i])
# Полученные элементы столбцов
print(f'Список элементов стобцов: {column_numbers}')

# Теперь вычисляем минимальные значения среди элементов каждого столбца
for num_list in column_numbers:
    min_num = num_list[0]
    for el in num_list:
        if el < min_num:
            min_num = el
    min_numbers.append(min_num)
# Список минимальных значений
print(f'Список минимальных значений: {min_numbers}')

# Находим максимальный элемент среди минимальных значений
max_num = min_numbers[0]
for num in min_numbers:
    if num > max_num:
        max_num = num

print(f'Максимальный элемент среди минимальных значений столбцов матрицы: {max_num}')
