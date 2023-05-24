import json

# file = open('text.txt', 'r')
# s = file.read()
# unli = []
# for i in s:
#     if 'aouie' in i:
#         print(i)

# file = open('text.txt', 'r')
# cc = 0
# c = 0
# vowels = 'uioea'
# for i in file.readlines():
#     for j in i:
#         if j in vowels:
#             cc += 1
#         if j.isalpha() and j not in vowels:
#             c += 1
#     print('undosh (', cc, ')', 'unli (', c, ')')
#     file.close()
#     c = 0
#     cc = 0

# n = int(input())
# with open('new.txt', 'w') as file:
#     for i in range(n):
#         s = '' * i
#         file.write(s + '*' + '\n')


# import os
#
#
# def current_path():
#     max_1 = 0
#     max_2 = 0
#     exclude = ('venv', '.idea')
#     for i in os.listdir():
#         if i not in exclude:
#             if os.path.isdir(i):
#                 max_1 += 1
#             elif os.path.isfile(i):
#                 max_2 += 1
#
#     print(f'p11-python  Papkalar soni  :{max_1}, Fayllar soni  :{max_2}')
#
#
# current_path()
