# from itertools import cycle
#
# c = 0
# for i in cycle("ABC"):
#     if c > 10:
#         break
#     print(i)
#     c += 1

# 1
# import sys
# sys.argv
#
# rate_in_hour, hours, bonus = sys.argv[1:]
# def my_funk():
#     salary = int(rate_in_hour) * int(hours) + int(bonus)
#     return salary
# print(f'Salary of worker: {my_funk()} rub')

# 2
# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_list = []
# for i in range(1, len(my_list)):
#     if my_list[i-1] < my_list[i]:
#         new_list.append(my_list[i])
# print(new_list)
# print(my_list[i])

# 3
# new_list = [el for el in range(20, 240) if el % 20 == 0]
# print(new_list)

# 4
# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new_list = [i for i in my_list if my_list.count(i) == 1]
# print(new_list)

# from random import randint
# print(a := [randint(0, 20) for _ in range(10)], '\n', [i for i in a if a.count(i) == 1], sep="")

# 5
# from functools import reduce
# print(reduce(lambda x, y: x * y, range(2, 5, 2)))
#
# def mul_list(el_1, el_2):
#     return el_1 * el_2
# unic_list = [el for el in range(0, 20, 2)]
# print(f'List\n{unic_list}'\nMultiplication of numbers'\n{reduce(mul_list, unic_list)}')

6
from itertools import cycle, count
# for i in count(5):
#     print(i)
#     if i == 10:
#         break
#
# for i in cycle('abc'):
#     print(i)

# print(f'A program generate a new numbers starts by noted. For generate input integer for exit "q"')
# for i in count(int(input('Enter a number: '))):
#     print(i, end='')
#     quit = input()
#     if quit == 'q':
#         break

# my_count = count(7)
# my_cycle = cycle("ABC")
# for _ in range(5):
#     print("(my_count, my_cycle)=({},{})".format(next(my_count), next(my_cycle)))


# 7
# from itertools import count
# from math import factorial
#
# def fact_gen():
#     for el in count(1):
#         yield factorial(el)
#
# generator = fact_gen()
# x = 0
# for i in generator:
#     if x == 15:
#         break
#     else:
#         x += 1
#         print(f'Factorial {x} = {i}')




# def my_func(num = list):
#     i for i in num if count(i) == 1
# print(my_func([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))

#
# import random
# original_list = [random.randint(0, 100) for i in list(range(0, random.randint(2, 10)))]
#
# print(original_list)

# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new_list = [i for num, i in enumerate(my_list[1:]) if i > my_list[num]]
# print(new_list)
