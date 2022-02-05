1
# i = 10
# print(i)
# chek = input('введите число: ')
# print(chek)
#
# goodword = input('ведите волшебное слово: ')
# print(goodword)

2
# time_in_seconds = int(input('введите время в секундах: '))
# time_in_minuts = (time_in_seconds / 60)
# time_in_hours = (time_in_minuts / 60)
# print(f'секунды: {time_in_seconds} минуты: {time_in_minuts} часы: {time_in_hours}'

# time = int(input("enter the time in seconds: "))
# hours = time // 3600
# minuts = (time // 60) - (hours * 60)
# seconds = time % 60
# print(f"{hours:02}:{minuts:002}:{seconds:2}")


3
# n = input('введите число: ')
# print(int(n) + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))

4

# num_init = int(input('enter a positive integer: '))
# greatest_dig = 0
# num = num_init
#
# while num > 0:
#     digit = num % 10
#     if digit > greatest_dig:
#         greatest_dig = digit
#         if greatest_dig == 9:
#             break
#     num = num // 10
# print(f"the greatest figure in {num_init} is: {greatest_dig}")

5
# debet = int(input('укажите выручку: '))
# kredit = int(input('укажите издержки: '))
# if debet > kredit:
#     print('компания в прибыли')
#     rentab = (debet / kredit)
#     wokers = int(input('введите кол-во сотрудников: '))
#     print('прибыль на сотрудника равна: ', rentab / wokers)
# else:
#     print('компания в убытке')

6
# a = int(input('введите кол-во км в первый день: '))
# b = int(input('введите цель в км: '))
# c = 1
# while a < b:
#     a *= 1.1
#     c += 1
#     if a < b:
#         continue
#     print(c)
