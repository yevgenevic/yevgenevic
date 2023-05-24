# Row = int(input("Enter the number of rows:"))
# Column = int(input("Enter the number of columns:"))
#
# matrix = []
#
# for row in range(Row):
#     a = []
#
#     for column in range(Column):
#         a.append(int(input()))
#     matrix.append(a)
#
# for row in range(Row):
#     for column in range(Column):
#         print(matrix[row][column], end=" ")
#     print()
from pprint import pprint

# matrix = [
#     [1, 2, 3, 5, 3],
#     [3, 5, 6, 9, 4],
#     [3, 2, 1, 4, 6],
#     [4, 7, 5, 1, 6],
#     [4, 7, 5, 1, 6]
# ]
# l = len(matrix)
# summ = 0
# data = []
# for i in range(l):
#     for j in range(l):
#         if i & 1:
#             data.append(i)
#         if j & 1:
#             data.append(j)
# print(data)
# l = len(matrix)
# summa = 0
# for i in range(l):
#     for j in range(l):
#         q = []
#         if i != 0 and i != l - 1 and j != 0 and j != l - 1:
#             summa += matrix[i][j]
#         else:
#             matrix.append(0)
# print(summa)
# print(matrix)

# summa = sum(sum(matrix[i][1: -1]) for i in range(1, len(matrix) - 1))
# print(summa)

# sum_diagonal = sum(matrix[i][i] for i in range(len(matrix)))
# print(sum_diagonal + sum(matrix[-1]))

# matrix = [
#     [1, 2, 3, 4],
#     [6, 7, 3, 8],
#     [8, 2, 9, 9],
#     [3, 2, 3, 2],
# ]
# from itertools import chain
# from math import sqrt, ceil
#
# l = list(filter(lambda x: x % 2, chain(*matrix)))
# n = ceil(sqrt(len(l)))
# l += [0] * (n ** 2 - len(l))
#
# matrix = [l[i: i + n] for i in range(0, len(l), n)]
#
# for row in matrix:
#     print(row)
# matrix = [
#     [1, 2, 3, 4],
#     [6, 7, 3, 8],
#     [8, 2, 9, 9],
#     [3, 2, 3, 2],
# ]
#
# l = len(matrix)
# summa = 0
# for i in range(l):
#     for j in range(l):
#         if i != 0 and i != l - 1 and j != 0 and j != l - 1:
#             summa += matrix[i][j]
# print(summa)

# l = len(matrix)
# matrix = [[0] * l] + matrix + [[0] * l]
# for row in matrix:
#     row.append(0)
#     row.insert(0, 0)
#
# for i in matrix:
#     print(i)
# summ = 0
# for i in matrix:
#     print(sum(i))
# print()
# for i in zip(*matrix):
#     print(sum(i))
# from itertools import chain
# from math import sqrt, ceil
#
# l = list(filter(lambda x: x % 2, chain(*matrix)))
# n = ceil(sqrt(len(l)))
# l += [0] * (n ** 2 - len(l))
#
# matrix = [l[i: i + n] for i in range(0, len(l), n)]

# for row in matrix:
#     print(row)

# n, m = map(int, input().split())
# matrix = []
# for _ in range(n):
#     matrix.append(list(map(int, input().split())))
# sum_ = []
# max_, min_ = float('-inf'), float('inf')
# for row in matrix:
#     max_ = max(max_, max(row))
#     min_ = min(min_, min(row))
#     print(sum(row), end=' ')
# print()
# print(max_, min_)

































