# //2
#
#
# from math import pi
#
# r1, r2, r3 = input().split()
# r1, r2, r3 = float(r1), float(r2), float(r3)
#
# r1 = pi * (r1 * r1)
# r2 = pi * (r2 * r2)
# r3 = pi * (r3 * r3)
# print(f"{r1:.2f}")
# print(f"{r2:.2f}")
# print(f"{r3:.2f}")

# 16
# from math import exp,e
#
# x, y = input().split()
# x, y = float(x), float(y)
# c1 = (x + y) / (pow(y, 2) + abs((pow(y, 2) + 2) / (x + pow(x, 3) / 5))) + exp(y + 2)
# print(f'{c1:.2f}')

# 19
# from math import log10, log, sqrt
#
# x, y = input().split()
# x, y = int(x), int(y)
# z = log10(abs(pow((x + y), 2) + sqrt(abs(y) + 2) - (x * y / (pow(x)2) / 2)))
# from math import sin, pow, cos
#
# x, y = input().split()
# x, y = float(x), float(y)
# print(f'{t11:,2f}')

# t11 = ((x * x) + 1) / ((x * x) + (x * y + (y * y)) / ((y * y) + (y + (x * y)) / abs(x * y) + 5)) + (1) / (
#         1 + cos(x) + (1) / (sin(abs(x))))

# from math import sin, sqrt, exp, log
#
# a, x, y = input().split()
# a, x, y = int(a), float(x), float(y)
# w2 = sqrt(exp(x * y) - x * sin(a * x) - pow(x, 2) + 2 / abs(x) + 5) + sqrt(log(pow(x, 2) + 2) + 5)
# print(f"{w2:.2f}")
# //3
# s, h = input().split()
# s, h = int(s), int(h)
# a = (float)(2 * s) / h
# print(f"{a:.2f}")
# //4
# from math import pi
#
# r = input()
# r = float(r)
# r = 4 * pi * (pow(r, 2))
# print(f"{r:.2f}")
# //5
# a, b, c = input().split()
# a, b, c = float(a), float(b), float(c)
# q = (a + b + c)/2
# print(f"{q:.2f}")
# //7
# from math import pi
#aAAAAAAAAAAAAAAAAA
# from math import exp
#
# x, y = input().split()
# x, y = float(x), float(y)
# c1 = (x + y) / pow(y, 2) + abs(pow(y, 2) + 2) / (x + pow(x, 3) / 5) + exp(y + 2)
# print(f"{c1:.2f}")
# //19
# from math import log, sqrt, cos
# x, y = input().split()
# x, y = int(x), int(y)
#
# z = log(abs(pow((x + y), 2) + sqrt(abs(y) + 2) - (x - x * y / (pow(x, 2) / 2 - 5)))) + cos(x + y) ** 2 / pow((x + y),
#                                                                                                              1 / 3)
#
# print(f"{z:.2f}")

# from math import log, sqrt
#
# a, x = input().split()
# a, x = int(a), float(x)
# TT = sqrt(x - 1) + sqrt(x + 2) + log(sqrt(pow(x, 2) * a) + 2) / sqrt(sqrt(x + 2) + sqrt(x + 24) + pow(x, 5))
# print(f"{TT:.2f}")
#
# from math import sqrt, pow
#
# a, b = input().split()
# a, b = float(a), float(b)
# T = (pow(a, 1 / 5)) + ((( b* (a + b)) / ((2 * b) + (a * b)))**(1/4)) * (pow(a, 2) + pow(b, 2) + 2)
# print(f"{T:.2f}")
# num = int(input('son kriting '))
# rev = 0
# while num != 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
#     print("raqam :" + str(rev))
# num=input()
# print(str(num)[::-1])
#
# x1, x2, c, d = input().split()
# x1, x2, c, d = float(x1), float(x2), int(c), int(d)
# F=abs((sin(c*x2**3+))**2/
# from math import sqrt
#
# h = input()
# h = int(h)
# g = 9.8
# a = sqrt((h * 2) / g)
# print(f"{a:.2f}")
# x = int(input())
# t = (365 * x * 24 * 3600) // 1000
# print(t)
# from math import sin, log10, cos
#
# a, x = input().split()
# a, x = int(a), float(x)
# bb1 = x * sin((x / 2) + (x / 3) + (x / 4)) + (log10(pow(x, 2) - 2) + (3 ** a)) / (cos(x + 3) * sin(x + 3) + 8)
# print(f"{bb1:.2f}")
# from math import cos
#
# a, b, c, d, x = input().split()
# a, b, c, d, x = int(a), int(b), int(c), int(d), float(x)
# y2 = ((((a * x) ** 2) + (b * x) + c) / (x * a) ** 2) + (pow(a, 2) + (pow(a, b - c))) + cos(abs(a + x) + b) / (c * x) + (d + pow(c, 2))
# print(f"{y2:.2f}")


# n = int(input())
# j = 0
# for i in range(0, n):
#     i += 1
#     j += i
# print(j)
# m = int(input())
# g = 9.8
# q = m * g
# print(f"{q:.2f}")
# m, a = input().split()
# m, a = int(m), int(a)
# F = m * a
# print(F)
# //40
# x, y, z = input().split()
# x, y, z = int(x), int(y), int(z)
# if x > 0:
#     x = pow(x, 2)
# if y > 0:
#     y = pow(y, 2)
# if z > 0:
#     z = pow(z, 2)
# print(x, y, z)
# -

# x, y, z = input().split()
# x, y, z = float(x), float(y), float(z)
# if x < 1 and y < 1 and z < 1:
#     if x < y and x < z:
#         x = (y + z) / 2
#     elif y < x and y < z:
#         y = (x + z) / 2
#     else:
#         z = (x + y) / 2
#
# print(x, y, z)

# x, y, z = input().split()
# x, y, z = float(x), float(y), float(z)
# if x >= 1 and x <= 3:
#     print(x, end=" ")
# if y >= 1 and y <= 3:
#     print(y, end=" ")
# if z >= 1 and z <= 3:
#     print(z, end=" ")

# x, y, z = input().split()
# x, y, z = float(x), float(y), float(z)
# x1 = x + y + z
#
# mx = x1
# if mx < x:
#     mx = x
# if mx < y:
#     mx = y
# if mx < z:
#     mx = z
# y1 = x + y / 2
#
# mn = y1
# if mn > x:
#     mn = x
# if mn > y:
#     mn = y
# if mn > z:
#     mn = z
#
# mn = mn ** 2
#
# print(f"{mx:.2f} {mn:.2f}")

#
# from math import exp, sin, log, sqrt
#
# a, x, y = input().split()
# a, x, y = int(a), float(x), float(y)
# w2 = sqrt(exp(x * y) - x * sin(a * x) - (x ** 2 + 2) / (abs(x) + 5)) + sqrt(log(x ** 2 + 2) + 5)
# print(f"{w2:.2f}")


# from math import sin, sqrt, tan
#
# x1,x2,c,d = input().split()
# x1,x2,c,d = float(x1),float(x2), int(c), int(d)
# F = abs((sin(abs(c*x2**3+d*x1**3-c*d))**2)/(sqrt(c*x1**2+d*x2**2+7)))+tan(x1*x2**2+d**3)
#
# print(f"{F:.2f}")

# u, r = input().split()
# u, r = int(u), int(r)
# i = u / r
# print(f"{i:.3f}")
# from math import cos
#
# a, b, c, d, x = input().split()
# a, b, c, d, x = int(a), int(b), int(c), int(d), float(x)
# y2 = (((a * x) ** 2) + (b * x) + c) / ((x * a) ** 3) + (pow(a, 2)) + (pow(a, b - c)) + cos(
#     abs(a * x) + b / (c * x) + d + pow(2, c))
# print(f"{y2:.2f}")

# from math import log, sqrt, log10
#
# a, x = input().split()
# a, x = int(a), float(x)
# TT = (sqrt(x - 1)) + (sqrt(x + 2)) + log10((sqrt(a * x) ** 2) + 2) / sqrt(sqrt(x + 2) + (sqrt(x + 24) + pow(x, 5)))
# print(f"{TT:.2f}")

# from math import sqrt, tan, cos, sin
#
# x = input()
# x = float(x)
# aa = sqrt(2 * tan(x + 2) - cos(x + pow(x, 2)) / (1 + cos(x + 2) ** 2)) + sin(pow(x, 2)) / pow(x, 2) + 3
# print(f"{aa:.2f}")


# x, y = input().split()
# x, y = float(x), float(y)
# mn = y
# mx = x
# if mx < y:
#     mx = y
#
# if mn > x:
#     mn = x
# print(f"{mx:.2f} {mn:.2f}")

# x, y, z = input().split()
# x, y, z = float(x), float(y), float(z)
# mn = y
# mx = x
# if mx < y:
#     mx = y
# if mx < z:
#     mx = z
# if mn > x:
#     mn = x
# if mn > z:
#     mn = z
# print(f"{mx:.2f} {mn:.2f}")2f

# from math import cos
# a,b,c,d,x=input().split()
# a,b,c,d,x=int(a), int(b), int(c), int(d), float(x)
# y2=(a*pow(x,2)+(b*x)+c)/(x*pow(a,3)+(pow(a,2)+(pow(a,b-c))))+cos(abs(a*x+b)/(c*x+d+pow(2,c)))
# print(f'{y2:2f}')


# from math import sqrt, cos
# a,b,c,x=input().split()
# a,b,c,x=int(a),int(b),int(c),float(x)
# W1=3/4+(8.2*pow(x,2)+sqrt(abs(pow(x,3)+(3*x))+cos(x-2)))/(a/4+b/3+c/2+1)
# print(f'{W1:.2f}')

'''25'''
# from math import sqrt, log10
#
# a, x = input().split()
# a, x = int(a), float(x)
# TT = (sqrt(x - 1) + sqrt(x + 2) + log10(sqrt(a * pow(x, 2))+2)) / (sqrt(sqrt(x + 2) + sqrt(x + 24) + pow(x, 5)))
# print(f'{TT:.2f}')


# from math import exp,sin,sqrt,log
# a,x,y=input().split()
# a,x,y=int(a),float(x),float(y)
# W2=sqrt(exp(x*y)-x*sin(a*x)-(pow(x,2)+2)/(abs(x)+5))+sqrt(log(pow(x,2)+2)+5)
# print(f'{W2:.2f}')

#
# from math import sqrt, tan, cos, sin
#
# x = float(input())
# AA = sqrt(2 * tan(x + 2) - cos(x + pow(2, x)) / 1 + pow(cos(2 * (x + 2)))) + (sin(*pow(x, 2)) / pow(x, 2) + 3)
# print(f'AA:.2f')

'''28'''
# from math import sin,cos,log10
# a,x=input().split()
# a,x=int(a),float(x)
# BB1=x*sin(x/2+x/3+x/4)+(log10(pow(x,2)-2)+pow(3,a))/(cos(x+3)*sin(x+3)+8)
# print(f'{BB1:.2f}')

# '''29'''
# from math import sqrt, cos, sin,e
# a,x,y=input().split()
# a,x,y=int(a),float(x),float(y)
# TT=sqrt(pow(y,2)+pow(e,x)+sqrt(pow(e,x)+(a/pow(x,2)+2)+cos(x)**2)sin(x**2))+cos(x)**3

'''34'''
# a,b,c=input().split()
# a,b,c=int(a),int(b),int(c)
# if a<b and b<c:
#     print('YES')
# else:
#     print('NO')

'''35'''
# a,b,c=input().split()
# a,b,c=int(a),int(b),int(c)
# if a>=b and b>=c:
#     print ((2*a),(2*b),(2*c))
# else:
#     print (abs(a),abs(b),abs(c))

'''37'''
# a,b=input().split()
# a,b=int(a),int(b)
# if a>b:
#     print(a)
# else:
#     print(a,b)

'''37'''
# a,b=input().split()
# a,b=int(a),int(b)
# if a<=b:
#    print(0,b)
# else:
#     print(a,b)

'''38'''
# x,y,z=input().split()
# x,y,z=float(x),float(y),float(z)
# if 1<=x and x<=3:
#       print(x)
# if 1<=y and y<=3:
#       print(y)
# if 1<=z and z<=3:
#       print(z)

'''39'''
# x, y = input().split()
# x, y = int(x), int(y)
# x != y
# if x < y:
#     print(f'{(x + y) / (2):.1f}')
# else:
#     print(f'{(x + y) / (2):.1f}')
# if y < x:
#     print(f'{(x * 2) * (y * 2):.1f}')
# else:
#     print(f'{(x * 2) * (y * 2):.1f}')
#
# x , y = map(int, input().split())
# if x > y:
#     print(f"{x + y}")
# elif y > x:
#     print()


'''40'''
# x,y,z=input().split()
# x,y,z=int(x),int(y),int(z)
# if x>=0 and y<=0 and z<=0:
#       print(x*x,y,z)
# if x<=0 and y>=0 and z<=0:
#       print(x,y*y,z)
# if x<=0 and y<=0 and z>=0:
#       print(x,y,z*z)
# if x>=0 and y>=0 and z>=0:
#       print(x*x,y*y,z*z)

'''41'''
# x,y,z=input().split()
# x,y,z=float(x),float(y),float(z)
#
# if x<1 and y<1 and z<1 and x>y and y>z:
#       print(x,y,(x+y)/(2))
# if x<1 and y<1 and z<1 and x>y and z>y:
#       print(x,(x+z)/(2),z)
# if x<1 and y<1 and z<1 and y>x and z>x:
#       print((y+z)/(2),y,z)
# if x>1 and y<1 and z<1:
#       print(x,y,z)
# if x<1 and y>1 and z<1:
#       print(x,y,z)
# if x<1 and y<1 and z>1:
#       print(x,y,z)
# if x>1 and y>1 and z<1:
#       print(x,y,z)
# if x>1 and y<1 and z>1:
#       print(x,y,z)
# if x<1 and y>1 and z>1:
#       print(x,y,z)

# from math import cos, log
#
# x, y, c, d = map(int, input().split())
#
# s = 0
# for a in range(1, x + 1):
#     s += (4 * a + 6 * log(a)) / (a * a + a)
# p = 1
# for a in range(1, y + 1):
#     p *= abs(a - 6 * cos(a)) / (a * a + a * log(a))
# sp = 0
# for k in range(1, c + 1):
#     SP = 0
#     for a in range(1, d + 1):
#         SP *= (a * k + x) / (k * k + y * y)
#
#     sp += SP
#
# print(f"{s:.2f} {p:.2f} {sp:.2f}")

