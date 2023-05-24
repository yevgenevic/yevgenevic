# // 1
# w = input()
# r = 1
# for i in w:
#     p = w.count(i)
#     if p > r:
#         r = p
#         s = i
# print(s)
# # //1,2
# def binary(d):
#     b = ''
#     q=0
#     while True:
#         if d == 0:
#             break
#         elif (d % 2) == 0:
#             d = d // 2
#
#         else:
#             d = d // 2
#             b = '1' + b
#             q+=1
#     return q
# #
# #
# i = int(input())
# print(binary(i))

# import collections
#
# line = input()
#
# bb = collections.Counter(line).most_common(1)[0][0]
# print(bb)


# //4
# a, b = list(map(int, input().split()))
# attemp = 0
# if a == b:
#     attemp += 1
# print(attemp)


# //2

#
# rows = 3
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")
#
# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")
#
#
# rows = 8
# i = 1
# while i <= rows:
#     j = i
#     while j < rows:
#         print(' ', end=' ')
#         j += 1
#     k = 1
#     while k <= i:
#         print('*', end=' ')
#         k += 1
#     print()
#     i += 1
#
# i = rows
# while i >= 1:
#     j = i
#     while j <= rows:
#         print(' ', end=' ')
#         j += 1
#     k = 1
#     while k < i:
#         print('*', end=' ')
#         k += 1
#     print('')
#     i -= 1
#
#
# rows = int(input())
# k = 0
# for i in range(1, rows + 1):
#     for space in range(1, (rows - i) + 1):
#         print(end="  ")
#     while k != (2 * i - 1):
#         print("* ", end="")
#         k += 1
#     k = 0
#     print()

# s = int(input())
# y = (2 * s) - 2
# for k in range(0, s):
#     for m in range(0, y):
#         print(end=" ")
#     y = y - 1
#     for m in range(0, k + 1):
#         print("*", end=' ')
#     print()
#
# l = []
# n = int(input())
#
# for i in range(n):
#     if i & 1:
#         l.append(i)
# l.append(n)
# l = reversed(l)
# t = 0
# for i in l:
#     print(' ' * t, '*' * i)
#     t += 1


# ///////////////////////////////
# n = int(input())
# mat = list()
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append('*')
#     mat.append(row)
#
# s: int = 0
# l: int = 0
# for i in range(n):
#     for j in range(n):
#         if i == n - 1 or i + j > n - 1:
#             print(mat[i][j], end=" ")
#         else:
#             print(" ", end=" ")
#     print()

#
# n = int(input())
#
# mat = list()
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append('*')
#     mat.append(row)
#
# s: int = 0
# l: int = 0
# for i in range(n):
#     for j in range(n):
#         if j>=i:
#             print(mat[i][j], end=" ")
#         else:
#             print(" ", end="")
#
#     print()


# //4

# //4,1
# A,B  = map(int,input().split())
# if (A==B):
#   print("=")
# elif (A<B):
#   print("<")
# else:
#   print(">")


# //5/1

# value = input()
# d = {
#     'salom': 'hello',
#     'hello': 'salom'
# }
# for i, v in d.items():
#     if value == v:
#         print(f"{value}:{i}")
#         break

# //5
# //2
# s = list(map(int, input().split()))
# for i, v in enumerate(s):
#     if i & 1 and +v & 1:
#         print(i, v)
# input()
# a = input().split()
# hi = {'A':2 , 'S':2 , 'L':1 , 'O':1 , 'M':1}
# for k , v in hi.items():
#     if a.count(k) < v:
#         print('NO')
#         break
# else:
#     print('YES')

