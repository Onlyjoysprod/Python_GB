# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

import timeit
import cProfile
import math


def my_solution(index):
    """Поиск i-го простого числа,
    без использования алгоритма «Решето Эратосфена»"""

    num = 3
    simple_nums = [2]
    nums = [2]
    while True:
        if len(simple_nums) == index:
            return simple_nums[index-1]
        else:
            for i in nums:
                if num % i == 0:
                    nums.append(num)
                    break
            else:
                nums.append(num)
                simple_nums.append(num)
        num += 1


print(f'Результат работы без Решета Эрастофена: {my_solution(5)}')
print(timeit.timeit('my_solution(5)', globals=globals(), number=1))
cProfile.run('my_solution(5)')
print('--------------------')
print(f'Результат работы без Решета Эрастофена: {my_solution(50)}')
print(timeit.timeit('my_solution(50)', globals=globals(), number=1))
cProfile.run('my_solution(50)')
print('-------------------------------------------')


def eratosphen_solution(i):
    """Поиск i-го простого числа,
    используя алгоритм «Решето Эратосфена»"""

    i_max = i_max_count(i)
    last_prime = [el for el in range(2, i_max)]

    for number in last_prime:
        if last_prime.index(number) <= number - 1:
            for j in range(2, len(last_prime)):
                if number * j in last_prime[number:]:
                    last_prime.remove(number * j)
        else:
            break
    return last_prime[i - 1]


def i_max_count(i):
    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


print(f'Результат работы с использованием Решета Эрастофена: {eratosphen_solution(5)}')
print(timeit.timeit('eratosphen_solution(5)', globals=globals(), number=1))
cProfile.run('eratosphen_solution(5)')
print('--------------------')
print(f'Результат работы с использованием Решета Эрастофена: {eratosphen_solution(50)}')
print(timeit.timeit('eratosphen_solution(50)', globals=globals(), number=1))
cProfile.run('eratosphen_solution(50)')

# Поиск i-го простого числа без использования алгоритма "Решето Эрастофена" происходит быстрее при малом значении i.
# При более высоких значениях индекса, алгоритм с решетом работает быстрее
