# // 1
# l = input()
# l = int(l)
# print(l // 100)

# // 2
# m = input()
# m = int(m)
# print(m // 1000)

# //3
# b = input()
# b = int(b)
# print(b//1024)

# // 15
# num = input()
# print(str(num)[::-1])

# from math import sin
#
# s = 0
# n = int(input())
# for i in range(1, n + 1):
#     s += sin(i) / pow(2, i)
# print(f"{s:.2f}")
# from math import cos, sin
#
# h = 0.5
# x = 0
# s = 0
# a = int(input())
# while x <= 10:
#     s += a * cos(x) - sin(pow(x, 2))
#     x += h
# print(f"{s:.2f}")

#
# from math import cos, sin, sqrt
#
# a, b = input().split()
# a, b = int(a), int(b)
# h = 2
# x = -1
# s = 0
# while x <= 12:
#     s += pow(x, 2) + pow((a,1/5) b + sin(x) / pow(a, 3) + cos(pow(x, 3) ** 2) )
#     x += h
# print(f"{s:.2f}")

# from math import sin
#
# n = int(input())
# s = (sin(n ** n) / (2 ** n))
# print(f"{s:.2f}")

# from math import sqrt, tan, cos, sin
#
# x = float(input())
#
# AA = sqrt((2 * tan(x + 2) - cos(x + 2 ** x)) / (1 + cos(x + 2) ** 2)) + sin(x ** 2) / (x ** 2 + 3)
# print(f"{AA:.2f}")

# from math import factorial
#
# n, x = input().split()
# n, x = int(n), int(x)
#
# S = 0
#
# for i in range(1, n + 1):
#     S += x ** i / factorial(i)
#
# print(f'{S:.3f}')

# from math import cos, pi
# a = int(input())
# x = - pi / 2
# h = pi / 19
#
# S = 0
# while x <= pi:
#     S += a ** (a / 3) + x * x * cos(a * x)
#     x += h
#
# print(f'{S:.2f}')
#
# from math import log
#
# x, y, c, d = map(int, input().split())
#
# S = 0
# for k in range(1, x + 1):
#     S += (-1) ** k * (k + 1) / (k ** 3 + k ** 2 + 1)
#
# P = 1
# for i in range(1, y + 1):
#     P *= (i ** 3 + abs(i - 9)) / (log(i) + 7 * i)
#
# SP = 1
# for n in range(1, c + 1):
#     _SP = 0
#     for m in range(1, d + 1):
#         _SP += (-1) ** m * log(m + 5) / (m ** (n + 3) + n * m)
#     SP *= _SP
#
# print(f'{S:.2f} {P:.2f} {SP:.2f}')


# from math import e, sqrt
#
# x, y, c, d = map(int, input().split())
#
# s = 0
# for k in range(1, x + 1):
#     s += k ** 3 + e ** k
#
# p = 1
# for a in range(3, y + 1):
#     p *= a * x / sqrt(a ** 2 + x ** 2)
#
# sp = 0
# for i in range(1, c + 1):
#     _sp = 1
#     for j in range(1, d + 1):
#         _sp *= (i * x + j ** 2) / sqrt(i ** 2 + j * y)
#     sp += _sp
#
# print(f'{s:.2f} {p:.2f} {sp:.2f}')
# from math import cos
#
# a, b, c, d, x = input().split()
# a, b, c, d, x = int(a), int(b), int(c), int(d), float(x)
# y2 = ((a * x ** 2) + (b * x) + c) / ((x * a ** 3) + (a ** 2) + (pow(a, b - c))) + cos(
#     abs(a * x + b) / (c * x) + (d + 2 * c))
# print(f"{y2:.2f}")


# from math import  log , cos
#
# x, y, c, d = map(int, input().split())
# s = 0
# for a in range(1, x + 1):
#     s += (4 * a + 6 * log(a)) / (a * a + a)
#
# p = 1
# for a in range(1, y + 1):
#     p *= (abs(a - 6 * cos(a))) / (a * a +a**(log(a)))
#
# sp = 0
# for k in range(1, c + 1):
#     _sp = 1
#     for a in range(1, d + 1):
#         _sp *= (a * k + x) / (k * k + y * y)
#     sp += _sp
#
# print(f'{s:.2f} {p:.2f} {sp:.2f}')
#
# from math import sin, cos
#
# a, b = input().split()
# a, b = int(a), int(b)
# x = 1
# h = 2
# s = 0
# while x < 12:
#     s += a * a + pow((b + sin(x)) / (a  3 + cos(x  3) ** 2), 1 / 5)
#     x += h
# print(f'{s:.2f}')

# r1, r2, r3 = input().split()
# r1, r2, r3 = int(r1), int(r2), int(r3)
# r = 1/((1 / r1) + (1 / r2) + (1 / r3))
# print(f"{r:.2f}")
#
# x, y = map(int, input().split())
# if x > y:
#     print(f"{x * y * 4} {(x + y) / 2}")
# else:
#     print(f"{(x + y) / 2} {float(x * y * 4)}")
# from math import sin
#
# from math import factorial

# n = int(input())
# S = 0
# for i in range(1, n + 1):
#     S += pow(-1, i - 1) * sin(i ** i) / pow(2, i)
# print(f"{S:.2f}")

# n = int(input())
# s = 0
# for i in range(1, n+1):
#     s += pow(-1, i - 1) + 1 / factorial(2 * i - 1)
# print(f"{s:.4f}")

# from math import sin, cos
# a, b = input().split()
# a , b = int(a), int(b)
# x = 1
# h = 2
# s = 0
# while x < 12:
#     s += a * a + pow((b + sin(x)) / (a ** 3 + cos(x ** 3)**2),1/5)
#     x += h
# print(f'{s:.2f}')


cities = [
    {
        "name": "New York City",
        "country": "United States",
        "population": 20.14,
        "area": 1223.59
    },
    {
        "name": "Tokyo",
        "country": "Japan",
        "population": 37.47,
        "area": 2194.07,
    },
    {
        "name": "Los Angeles",
        "country": "United States",
        "population": 13.2,
        "area": 1299.01,
    },
    {
        "name": "Madrid",
        "country": "Spain",
        "population": 6.79,
        "area": 604.31,
    },
    {
        "name": "Osaka",
        "country": "Japan",
        "population": 19.3,
        "area": 5107.0,
    },
    {
        "name": "London",
        "country": "United Kingdom",
        "population": 14.26,
        "area": 8382.0,
    }
]
cities = (sorted(cities, key=lambda city: (city['country'], city['name'])))
print(*cities)
