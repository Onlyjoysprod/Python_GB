# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

companies = namedtuple('Profits', ['q1', 'q2', 'q3', 'q4', 'total'])
companies_dict = {}

n = int(input('Укажите кол-во предприятий: '))

for i in range(n):
    company_name = input(f'Наименование {i+1}-го предприятия: ')
    profits = []
    total = 0
    for i2 in range(4):
        profit = float(input(f'Введите прибыль за {i2+1} квартал: '))
        profits.append(float(profit))
        total += profit
    companies_dict[company_name] = companies(q1=profits[0], q2=profits[1], q3=profits[2], q4=profits[3], total=total)

# print(companies_dict)

total_companies_profit = 0
avg_profit = 0

for name, profit in companies_dict.items():
    total_companies_profit += profit.total

avg_profit = total_companies_profit / len(companies_dict)

print(f'Общая прибыль за год: {total_companies_profit}\n'
      f'Средняя прибыль для всех компаний: {avg_profit}')

companies_list = {'avg more': [], 'avg less': []}

for name, profit in companies_dict.items():
    if profit.total >= avg_profit:
        companies_list['avg more'].append(name)
    else:
        companies_list['avg less'].append(name)

print(f'Список компаний с годовой прибылью больше либо равной среднему значению: {companies_list["avg more"]}\n'
      f'Список компаний, чья годовая прибыль ниже среднего значения: {companies_list["avg less"]}')
