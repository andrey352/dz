# 1
# def my_f(num_1, num_2):
#     try:
#         my_num = num_1 / num_2
#     except ZeroDivisionError:
#         return 'division by zero, enter not a zero'
#     return my_num
# print(my_f(int(input('Enter a number 1: ')), int(input('Enter a number 2: '))))

# 2
# def my_f(**kwargs):
#     return kwargs
# print(my_f(
#     name=input('name: '),
#     surname=input('surname: ')
# ))

# 3
# def my_f(num_1, num_2, num_3):
#     n = min(num_1, num_2, num_3)
#     m = sum([num_1, num_2, num_3]) - n
#     return m
# print(my_f(
#     int(input('Enter a number 1: ')),
#     int(input('Enter a number 2: ')),
#     int(input('Enter a number 3: '))
# ))

4
# def my_f():
#     try:
#       x = float(input('Enter a real positive number: '))
#       y = int(input('Enter a negative number: '))
#       res = x
#       for i in range(abs(y) - 1):
#           res *= x
#       return 1 / res
#     except ValueError:
#         return 'Check value'
# print(my_f())

5
