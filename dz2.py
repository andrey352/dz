# 1
# my_list = ['str', 333, False, (9, 2)]
# for digit in my_list:
#  print(type(digit))

2
# my_list = list(input('Enter a list of values: '))

3
# mounth = int(input('Enter a number of mounth: '))
# if mounth in [1, 2, 12]:
#     print('it is a winter')
# elif mounth in [3, 4, 5]:
#     print('it is a spring')
# elif mounth in [6, 7, 8]:
#     print('it is a summer')
# elif mounth in [9, 10, 11]:
#     print('it is a autumn')

# mounth = int(input('Enter a number of mounth: '))

# 4
# my_str = list(input('Enter string: '))
# my_list =
# for ind, el in enumerate(my_str):
#     print(ind, el)

my_list = [1, 2, 3, 4, 5]
for i in range(1, len(my_list), 2):
    my_list.insert(i-1, my_list.pop(i))
    print(my_list)