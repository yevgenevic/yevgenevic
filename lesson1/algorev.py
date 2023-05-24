# from math import sqrt, log, sin,exp,cos
#
# x, y, c, d = map(int, input().split())
# S, P, SP = 0, 1, 0
# for a in range(1, x + 1):
#     S += (2* a + cos(a)) ** 2
# for a in range(1, y + 1):
#     P *= (a + 6 )/ sqrt(a ** 2 + 2)
# for i in range(1, c + 1):
#     _SP = 0
#     for k in range(1, d + 1):
#         _SP += ( k ** 2 + y)/sqrt(k ** 2 + y ** 2)
#     SP += _SP
# print(f"{S: .2f} {P: .2f} {SP: .2f}")

# #
# a='Hello'
# print(a.swapcase() )


# a = str(input())
# b = ''.join((x for x in a if not x.isdigit()))
# print(b)
# a = str(input())
# b = '/start'

# if b:
#     print('true')
# else:
#     print('false')
#
# l, u, p, d = 0, 0, 0, 0
# s = str(input())
# if (len(s) >= 8):
#     for i in s:
#         if (i.islower()):
#             l += 1
#         if (i.isupper()):
#             u += 1
#
#         if (i.isdigit()):
#             d += 1
#
#         if (i == '@' or i == '$' or i == '_'):
#             p += 1
# if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(s)):
#     print("FALSE")
# else:
#     print("TRUE ")


# nums = [1, 2, 11, 15, 7]
# f = []
# for i, v in enumerate(nums):
#     if i % 2 == 1:
#         f.append(v)
# print(f)

# nums = [1, 2, 4, 11, 15, 7, 8, 10]
# f = []
# for i, v in enumerate(nums):
#     if i % 2 == 0 and v % 2 == 0:
#         f.append(v)
# print(f)


# nums = [1, 3, 2, 1]
# print(nums*2)
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
'''      95 - misol
from math import sqrt, exp
x, y, c, d = map(int, input().split())
S, P, SP = 0, 0, 0
for i in range(1, x + 1):
   S += (i ** 4 + i ** 2 + 3) / sqrt(i + exp(i))
for k in range(1, y + 1):
   P += (k + 1) / (k ** 3 + 5 * k)
for m in range(1, c + 1):
   _SP = 1
   for n in range(1, d + 1):
       _SP *= sqrt(abs(m ** n - n ** m) / (m ** n + n ** m))
   SP += _SP
print(f"{S: .2f} {P: .2f} {SP: .2f}")


 9 4 - misol
from math import sqrt, cos

x, y, c, d = map(int, input().split())
S, P, SP = 0, 1, 0
for a in range(1, x + 1):
   S += (2 * a + cos(a)) ** 2
for a in range(1, y + 1):
   P *= (a + 6) / sqrt(a ** 2 + 2)
for k in range(1, c + 1):
   _SP = 0
   for y in range(1, d + 1):
       _SP += (k ** 2 + y) / sqrt(k ** 2 + y ** 2)
   SP += _SP
print(f"{S: .2f} {P: .2f} {SP: .2f}")


97-misol
from math import sqrt, log, sin, exp

x, y, c, d = map(int, input().split())
S, P, SP = 0, 1, 0
for n in range(1, x + 1):
   S += 1 / (5 - 17 * n + n ** 3)
for m in range(1, y + 1):
   P *= sqrt(abs(m - 5) + 1) / (m ** 2 + 4 * m - 1)
for i in range(1, c + 1):
   _SP = 1
   for k in range(1, d + 1):
       _SP *= pow(-1, i) * pow(abs(sin(k) + exp(k)), 1 / 7) / (2 * abs(4 * i ** 3 - k ** 4))

   SP += _SP

print(f"{S: .2f} {P: .2f} {SP: .2f}")


from math import log, cos

x, y, a, b = map(int, input().split())

s = 0
for a in range(1, x + 1):
   s += (a ** 2 + 2 * a) / (a ** 3 + a * cos(a) ** 2 + 1)

   p = 1
   for i in range(1, y + 1):
       p *= (i ** 2 + 1) / ((i ** 3) ** (1 / i) + 2)

       sp = 0
       for i in range(1, a + 1):
           _sp = 1
           for k in range(1, b + 1):
               _sp *= log(k ** i + k ** (1 / i) / (k ** 3 + (i ** 1 / k)))
           sp += _sp
print(f'{s:.2f} {p:.2f} {sp:.2f}')


#   91 misol
from math import log
x, y, c, d = map(int, input().split())
S, P, SP = 0, 1, 0
for m in range(1, x + 1):
   S += 3 * m ** 3 + (4 * m) + 5 / m ** 3 + log(m)

for k in range(1, y + 1):
   P *= k / ((k ** 3) + (7 * k) + 5)

for i in range(1, c + 1):
   _SP = 1
   for m in range(1, d + 1):
       _SP *= log(i) + m ** i / m ** i

   SP += _SP

print(f"{S: .2f} {P: .2f} {SP: .2f}")


80- misol
from math import sin, cos
a = int(input())
s = 0
h = 0.5
x = 0
while x <= 10:
   s += a * cos(x) - sin(x * x)
   x += h
print(f"{s:.2f}")


86 - misol
from math import sqrt, sin, cos
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
s = 0
h = 0.25
x = c
while x <= b:
   s += (a*a) * cos(x) + sin(x) / 2 + b * (x * x)
   x += h

print(f"{s:.2f}")
'''
# -----------------------------------------------------

# https://algo.ubtuit.uz/problem/96
from math import sin, factorial, log

'''
from math import log

x, y, c, d = map(int, input().split())
S, P, SP = 0, 1, 1

for k in range(1, x + 1):
    S += pow(-1, k) * (k + 1) / (k ** 3 + k ** 2 + 1)
for i in range(1, y + 1):
    P *= (i ** 3 + abs(i - 9)) / (log(i) + 7 * i)

for n in range(1, c + 1):
    _SP = 0
    for m in range(1, d + 1):
        _SP += pow(-1, m) * log(m + 5) / (pow(m, n + 3) + n * m)
    SP *= _SP

print(f"{S:.2f} {P:.2f} {SP:.2f}")
'''

# https://algo.ubtuit.uz/problem/39

'''from math import sqrt

a , b , c = map(int , input().split())
D = b ** 2 - 4 * a * c
if D > 0 and a != 0:
    x1 = (-b-sqrt(D)) / (2 * a)
    x2 = (-b+sqrt(D)) / (2 * a)
    print(f"{x2 : .2f} {x1:.2f}")
elif D == 0 and a!=0:
    x1 = -b/(2*a)
    print(f"{x1 : .2f} {x1 : .2f}")
else:
    print('NO')'''

# https://algo.ubtuit.uz/problem/23

'''x, y = map(int, input().split())
if x > y:
    print(f"{float(x * 2 * y * 2)} {(x + y) / 2}")
else:
    print(f"{(x + y) / 2} {float(x * y * 4)}")'''

# https://algo.ubtuit.uz/problem/63
'''
n = int(input())
S = 0
for i in range(1, n + 1):
    S += pow(-1 , i - 1) / factorial(2 * i - 1)

print(f"{S : .4f}")'''

# https://algo.ubtuit.uz/problem/29

'''from math import cos, factorial, sqrt, exp, sin

a , x , y = input().split()
a , x , y = int(a) , float(x) , float(y)

TT = sqrt(y ** 2 + exp(x) + sqrt(exp(x) + a / (x ** 2 + 2)) + cos(x) ** 2 / sin(x ** 2) ) + pow(cos(x) , 3)
print(f"{TT : .2f}")'''

# https://algo.ubtuit.uz/problem/83

'''a , b , c = map(int , input().split())
h = 0.5
x = 5
S = 0
while x <= 10:
    S += (a ** 2 + b * x + x ** c) / (a ** 2 + b ** 2 + x ** 2)
    x += h
print(f"{S :.2f}")'''

# https://algo.ubtuit.uz/problem/94

'''from math import log, cos, sqrt

x, y, c, d = map(int, input().split())
S, P, SP = 0, 1, 0

for a in range(1, x + 1):
    S += pow(2 * a + cos(a) , 2)
for a in range(1, y + 1):
    P *= (a + 6) / sqrt(a ** 2 + 2)

for k in range(1, c + 1):
    _SP = 0
    for y in range(1, d + 1):
        _SP += (k ** 2 + y) / sqrt(k ** 2 + y ** 2)
    SP += _SP

print(f"{S:.2f} {P:.2f} {SP:.2f}")'''

# https://algo.ubtuit.uz/problem/94

'''from math import log, cos, sqrt, exp

x, y, c, d = map(int, input().split())
S, P, SP = 0, 0, 0

for i in range(1, x + 1):
    S += (i ** 4 + i ** 2 + 3) / sqrt(i + exp(i))
for k in range(1, y + 1):
    P += (k + 1) / (k ** 3 + 5*k)

for m in range(1, c + 1):
    _SP = 1
    for n in range(1, d + 1):
        _SP *= sqrt(abs(m ** n - n ** m) / (m ** n + n ** m))
    SP += _SP

print(f"{S:.2f} {P:.2f} {SP:.2f}")'''

# from math import sqrt, cos, log
#
# x, y, c, d = map(int, input().split())
# S, P, SP = 0, 1, 0
# for a in range(1, x + 1):
#     S += (a ** 2) + (2 * a) / (a ** 3) + a * cos(a + 1) ** 2
# for i in range(1, y + 1):
#     P *= (i ** 2 + 1) / sqrt((i ** 3) + 2) ** i
# for k in range(1, c + 1):
#     _SP = 0
#     for i in range(1, d + 1):
#         _SP += log((k ** i) + sqrt(k) ** i) / (k ** 3) + sqrt(i) ** k
#     SP += _SP
# print(f"{S: .2f} {P: .2f} {SP: .2f}")

# a = [i for i in range(0, 10) if i % 2 == 0]
# print(a)
# name = ['Habibuloh', 'sulton', 'samikr', 'john']
# s = []
# for i in name:
#    if i.startswith('s'):
#     s.append(i)
# print(s)

#
# nums = [8, 1, 2, 2, 3]
# a = [sum(True for j in nums if i > j) for i in nums]
# print(a)
# nums = [0, 1, 2, 3, 4]
# index = [0, 1, 2, 2, 1]
# r=[]
# a = [i for i in range(len(nums)) : r.insert(index[i], nums[i])]

# for i in range(0, int(len(nums) / 2)):
#     k.extend(list((nums[(2 * i) + 1],)) * nums[2 * i])
# return k

# nums = [1, 2, 3, 4]
# k = []
# for i in range(0, int(len(nums) / 2)):
#     k.extend(list((nums[(2 * i) + 1],)) * nums[2 * i])
# print(k)
# //66
# from math import sin
# n, x = input().split()
# n, x = int(n), int(x)
# s = 0
# for i in range(1, n + 1):
#     s += pow((-1), (i - 1)) * 1 / i * sin(i * x)
# print(f"{s:.3f}")

# //69

# from math import factorial
#
# n, x = input().split()
# n, x = int(n), int(x)
# s = 0
# for i in range(1, n + 1):
#     s += pow(-1, i) * pow(x, i) / factorial(i)
# print(f"{s:.3f}")

# 70
# from math import factorial
#
# n, x = input().split()
# n, x = int(n), int(x)
# s = 0
# for i in range(1, n + 1):
#     s += pow((-1), (i - 1)) * pow(x, (2 * i - 1)) / factorial(2 ** i - 1)
# print(f"{s:.3f}")
# //71
# from math import factorial
#
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += pow((-1), (i - 1)) * pow(x, (2 * i - 2)) / factorial(2 * i - 2)
# print(f"{s:.3f}")

# //72
# from math import factorial
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += pow(x, (2 * i - 2)) / factorial(2 * i - 2)
# print(f"{s:.3f}")

# // 73

# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += pow(x, (2 * i - 1)) / (2 * i - 1)
# print(f"{s:.3f}")

# // 74
# fom math import factorial
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += pow(x, (2 * i - 1)) / factorial(2 * i - 1)
# print(f"{s:.3f}")

# //75
# from math import factorial
#
# n, k = map(int, input().split())
# s = 0
#
# for i in range(0, n + 1):
#     s += ((-1) ** i) * (k ** i) / factorial(i)
# print(f'{s:.3f}')


# //76

# from math import factorial, cos, sin
#
# a, b, c = map(int, input().split())
# x = a
# h = 3
# y = 0
# while x <= c:
#     y += pow((a * x + b) / (pow(b, 2) + cos(x) ** 2), 1 / 3) - (sin(x ** 2) /( a * b))
#     x += h
# print(f'{y:.2f}')

# //77
#
# from math import factorial, cos, sin
# a, b, c,d = map(int, input().split())
# x = c
# h = 2
# y = 0
# while x <= d:
#     y += pow((sin(a * x) + pow(b ,2 * c))/(b ** 2 + cos(x)**2),1/3) - (sin(x ** 2)/ (a * b))
#     x += h
# print(f'{y:.2f}')
# //103
# int(input())
# l = list(map(int, input().split()))
# k, i = list(map(int, input().split()))
# q = 0
# w = 0
# for n in range(k - 1, i):
#     q += 1
#     w += l[n]
# print(w/q)

#     n = int(input())
# l = list(map(int, input().split()))
# yig = sum(l) / n
# s = 0
# j = 0
# for i in l:
#     if yig > i:
#         j += 1
#         s += i
# d = s / j
#
# print(f'{d:.2f}')
# n, m = map(int, input().split())
# mins = float('inf')
# maxs = float('-inf')
# matrix = []
#
# for i in range(n):
#     l = list(map(int, input().split()))
#     maxs = max(max(l), maxs)
#     mins = min(min(l), mins)
#     matrix.append(l)
#
# summa = []
#
# for i in zip(*matrix):
#     summa.append(sum(i))
#
# print(*summa)
# print(maxs, mins)


# input()
# mat = list(map(int, input().split()))
# print(sum(map(lambda i: i * i, mat)))


# input()
# mas = list(map(int, input().split()))
# r = min(mas)
# q = []
# for i in mas:
#     print(f"{i / r:.2f}", end=" ")

# from math import log
#
# input()
# mas = list(map(int, input().split()))
# m = int(input())
# l = 1
# for i in mas:
#     if i > m:
#         l *= i
# print(f"{log(l):.2f}")
# input()
# mas = list(map(int, input().split()))
# k, m = list(map(int, input().split()))
# s = 1
# for i in mas:
#     if k == i or m == i:
#         s *= i
# print(s)

#
# input()
# mas = list(map(int, input().split()))
# m = int(input())
# q = 0
# for i in mas:
#     if m < i:
#         q += i
# print(q)
#
# print(sum(map(lambda i: m < i, mas)))

# input()
# mas = list(map(int, input().split()))
# q = 0
# sana = 0
# for i in mas:
#     if i & 1:
#         q += i
#         sana += 1
# print(f"{q / sana:.2f}", end=" ")
#
# input()
# mat = list(map(int, input().split()))
# a, b = map(int, input().split())
# s = 0
# for i in mat:
#     if i < a or i > b:
#         s += 1
# print(s)

# input()
# mat = list(map(int, input().split()))
# q = 0
# w = 0
# for i in mat:
#     q += i * i
# w = sum(mat) / len(mat)
# print(f"{q}")
# print(f"{w:.2f}")

# input()
# mas = list(map(int, input().split()))
# for i in mas:
#
# input()
# mat = list(map(int, input().split()))
# k, l = list(map(int, input().split()))
# q = 0
# w = 0
# for i in mat:
#     if k < i or i > l:
#         q += i * i * i
# input()
# mas = list(map(int, input().split()))
# r = min(mas)
# print(r)

# input()
# mas = list(map(int, input().split()))
# q = 0
# sana = 0
# for i in mas:
#     if i & 1:
#         q += i
#         sana += 1
# print(f"{q / sana:.2f}", end=" ")

# from decimal import Decimal, ROUND_HALF_UP, getcontext
#
# getcontext().rounding = ROUND_HALF_UP
# k = int(input())
# n = list(map(int, input().split()))
# nat = 0
# sanoq = 0
# for i, v in enumerate(n, 1):
#     if v % 2 == 1:
#         nat += v
#         sanoq += 1
# print(f"{Decimal(nat / sanoq):.2f}")

# import random
# n = int(input("qatorni kiriting: "))
# m = int(input("ustunni kiriting: "))
# matrix = list()
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(random.randint(-94, 92))
#     matrix.append(row)
# for row in matrix:
#     print(*row)
# l = list()
# for i in range(n):
#     summa = 0
#     for j in range(m):
#         summa += matrix[i][j]
#     l.append(summa)
# maxx = max(l)
# minn = min(l)
# print(l)
# print(maxx, minn)


# num = input()
#
# t = sum(map(lambda x: int(num[x]), range(0, len(num), 2)))
# j = sum(map(lambda x: int(num[x]), range(1, len(num) + 1, 2)))
# print(t, j)
# print('yes') if t == j else print('no')


# input()
# mas = list(map(int, input().split()))
# q = 0
# sana = 0
# for i in mas:
#     if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
#         q += i
# print(q)


