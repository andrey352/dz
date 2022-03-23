# 1
# names = input("Enter a names: ").split()
# with open("text_300.txt", "w+") as f:
#    for i in names:
#       f.write(f'{i}\n')
#    f.seek(0)
#    print(f.read())

# 2
# with open("text_300.txt") as f:
#    i = 0
#    for line in f:
#       i += 1
#       print(f'Words: {len(line.split())}')
#    print(i)

# 3
with open("sotr.txt") as f:
     for line in f:
         my_dict = {x: y for line in range()}
         # rich = [n for n, v in line if v in line]
         print(my_dict)