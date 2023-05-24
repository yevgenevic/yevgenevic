# a = [5, 7, 9, 2, 4, 5, 8, 1]
# for i in range(len(a) // 2):
#     print(a[-i - 1], a[i], end=' ')


'''
// 1
a = [5, 7, 9, 2, 4, 5, 8, 1]
s = 0
for i in a:
    s += i

print(s)'''''

'''//2
a = [5, 7, 9, 2, 4, 5, 8, 1]
s = 0
for i in a:
    s += i
print(s//len(a))

//3
a = [5, 7, 9, 2, 4, 5, 8, 1]
s = a[0]
q = 0
for i in a:
    if s > i:
        q = i

# print(q)

'''
'''

//4
a = [5, 7, 9, 2, 4, 5, 8, 1]
maximal = a[0]
for i in a:
    if maximal < i:
        maximal = i

print(maximal)'''

'''
//5
a = [5, 7, 9, 2, 15, 16, 4, 5, 8, 1, 10, 14]
maximal = a[0]
for i in a:
    if maximal < i:
        maximal = i - 1
print(maximal)'''

# c = [5, 7, 9, 2, 15, 16, 4, 5, 8, 1, 10, 14]
# a, b = input().split()
# l = list(map(int, input().split()))
# a, b = list(map(int, input().split()))
# maxx = l[0]
# while a < b:
#     b = 1
#     if maxx < b:
#         maxx = b
#     maxx += b
# print(maxx)


# a = input()
# b = 0
# for i in a:
#     b = i + b
# if (i == b):
#     print("Yes")
# else:
#     print("No")
# a = 'kiyik'
# q = len(a) // 2
# for i in range(q, len(a)-1):
#     if (q == a):
#         print('palindrome')
#     else:
#         print('not palindrome')


# a = "kiyik"
# f = len(a)//2
# for i in a:
#     f = i + f
#     if (a == f):
#         print('palindrome')
#     else:
#         print('not palindrome')

# a = str(input())
# u = 0
# q = 0
# for i in a:
#     if i in

#
# class Solution:
#     def maximumWealth(self, accounts):
#         return max([sum(arr) for arr in accounts])
#         return max([sum(arr) for arr in accounts])

# from random import randint
#
# a = randint(1, 200)
# b = randint(1, 200)
# c = int(input('{}+{} ='.format(a, b)))
# if c == (a + b):
#     print('javob tugri')
# else:
#     print('javob xato')

# s1 = set(input().split())
#
# for i in s1:
#     s1.difference(s2)
# print(s1)
#
# s = 'hello botir 12 12'
# res = set()
# for i in s:
#    if i.isdigit():
#        res.add(i)
# print(res)

# a = 1
# a = ("rost" if a else "yplgon")
# print(a)

# l = [2324, 4, 53, '324', 'jgdfas']
# q = []
# w = []
# for i in q:
#     if i not in w:
#         q.append(i)
#     else:
#         q.append(i)
# print(w)

# l = [2324, 4, 53, '324', 'jgdfas']
# q = set()
# w = set()
# rev = []
# for i in l:
#     i = str(i)
#     if i.isdigit():
#         q.add(i)
#     else:
#         w.add(i)
# print('sonlar', len(q))
# print('harflar', len(w))

# a = list(range(1, 101))
# result = [i + 1 if i % 7 == 0 else i + 2 for i in a if i % 7 == 0 or i % 2 == 0]
# print(result)

#
# a = list(range(1, 51))
# # result=[i-1 if i%5==0 else i-2 if i%7==0 for i in a if i%2==0 and i%3==0 and i%5==0 and i%7==0 ]
# result = [i - 1 if i % 5 == 0 else i - 2 if i % 7 == 0 else i - 3 for i in a if
#           i % 2 == 0 and i % 3 == 0 or i % 5 == 0 or i % 7 == 0]
# print(result)

