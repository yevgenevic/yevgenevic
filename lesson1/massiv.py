# //14
# from math import sin
#
# n = input()
# l = list(map(int, input().split()))
# q = 1
# for i in l:
#     if i % 2 == 0 or i % 5 == 0:
#         q *= i
# q = sin(q)
# print(f"{q:.2f}")

# //15
#
# n = input()
# l = list(map(int, input().split()))
# k = int(input())
# summa = 0
# for i in l:
#     if i < k:
#         summa += i * i
#
# print(summa)

# //16
# from decimal import Decimal, getcontext, ROUND_HALF_UP
#
# getcontext().rounding = ROUND_HALF_UP
# input()
# l = list(map(int, input().split()))
# m = max(l)
# for i in l:
#     print(f'{Decimal(i / m):.2f}',end=" ")
'''
3 3
1 0 1
2 4 3
2 3 2
'''

#
# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for i in range(n)]
# columns = [(list(map(int, input().split())))]
# q = []
# for row in zip(n):
#     for col in zip(m):
#
#   if row[i]>col[i]

#
# n, m = map(int, input().split())
# result = []
# a = 0
# index = 0
# # matrix = [list(map(int, input().split())) for i in range(n)]
#
# for row in range(n):
#     row = str(row)
#     s = sum(map(len, input().split()))
#   if row.isdigit():
#
# print(index + 1)

#
# n,m = map(int,input().split())
# result=[]
# for i in range(n):
#     result.append(input().split())
#     index=m=0
#     for i,v in enumerate(result):
#         s=0
#         for i in v:

#
# s = 'hello worldt728538'
# count = 0
# print(len([i for i in s if i.isdigit()]))
#
#
# def separate_word(a):
#     h = ''
#     for i in a:
#         if i.isalpha():
#             h += i
#     return h
#
#
# w = input()
# print(separate_word(w))


#
#
# n, m = map(int,input().split())
# mat = list()
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(random.randint(0, 11))
#     mat.append(row)
# for row in mat:
#     print(row)
#
# for i in range(n):
#     for j in range(m):
#         if i == 0 or i == n-1 or j == 0 or j == m-1:
#             print(mat[i][j], end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n, m = map(int, input().split())
# minn = float('inf')
# maxx = float('-inf')
# result = []
#
# for i in range(n):
#     l = list(map(int, input().split()))
#     minn = min(l, minn)
#     maxx = max(l, maxx)
#     result.append(sum(l))
# print(result)
# print(maxx, minn)


# s = input()
# # a = int(input()) - 1
# # b = int(input()) - 1
# a, b = input().split()
# if a > b:
#     print(s[a:b - 1:-1])
# else:
#     print(s[a:b + 1])

# s = input()
# a = int(input()) - 1
# b = int(input()) - 1
#
# if a > b:
#     print(s[a:b - 1: -1])
# else:
#     print(s[a:b + 1])

#
# s = input()
# a = int(input()) - 1
# b = int(input()) - 1
#
# if a > b:
#     if b == 0:
#         s = s[a:: -1]
#     else:
#         s = s[a - 1:b - 1: -1]
# else:
#     s = s[a:b + 1]
# print(s)
# result = s = [s[a:: -1] if b == 0 else s[a:b + 1]]
# print(result)

#
# s = '2 3 3 4 5 6 7 8'
# l = []
# l = list(map(lambda a: int(a) % 2 == 0, float(a) % 2 == 1, s.split()))
# print(l)

# s = input()
# q = list(filter(lambda a: int(a) & 1, s.split()))
# print(q)
