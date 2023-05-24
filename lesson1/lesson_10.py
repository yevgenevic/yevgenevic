# // leetcode 1512

# nums = [1, 2, 3, 1, 1, 3]
# q = 0
# for i, v in enumerate(nums):
#     for j, val in enumerate(nums):
#         if nums[i] == nums[j] and i < j:
#             q += 1
# print(q)

# //letcode 1365
# nums = [8, 1, 2, 2, 3]
# print([sum(True for j in nums if i > j)for i in nums])

# //2325 leetcode#
# s.sort(key=lambda x: x[-1])
# return ' '.join(map(lambda x: x[:-1], s))

# address = '1.1.1.1'
# q = ''
# for i in address:
#     if i != '.':
#         q += i
#     else:
#         q += '[.]'
# print(q)
# address = '1.1.1.1'
# print(address.replace('.', '[.]'))


# s = "is2 sentence4 This1 a3".split()
# l = ' '.join(map(lambda i: i[:-1], sorted(s.split(), key=lambda i: i[-1])))
# print(s)
# leetcode 1218
# names = ["Mary", "John", "Emma"]
# heights = [180, 165, 170]
# print([names[heights.index(i)] for i in sorted(heights)[::-1]])

# s = "Myself2 Me1 I4 and3"
# q = ' '.join(map(lambda i: i[:-1], sorted(s.split(), key=lambda i: i[-1])))
# print(q)
# //leetcode 2011
# //v1
# operations = ["--X", "X++", "X++"]
# count = 0
# for i in operations:
#     if i == "++X" or i == "X++":
#         count += 1
#     if i == "--X" or i == "X--":
#         count -= 1
# print(count)
# //v2
# operations = ["X++","++X","--X","X--"]
# x = 0
# for i in operations:
#     if '+' in i:
#         x += 1
#     else:
#         x -= 1
# print(x)
# //v3
# a = operations.count('++X')
# b = operations.count('X++')
# d = operations.count('--X')
# c = operations.count('X--')
# return a + b - d - c


# //771 leetcode
# jewels = "aA"
# stones = "aAAbbbb"
# counter = 0
# for i in jewels:
#    for j in stones:
#         if i == j:
#             counter += 1
# print(counter)

# //1920 leetcode

# nums = [0, 2, 1, 5, 3, 4]
# ans = []
# for i in nums:
#     pass

# //1470 leetcode

# nums = [1, 2, 3, 4, 4, 3, 2, 1]
# n = 4
# q = nums[:n]
# w = nums[n:]
# e = []
# for i in range(n):
#     e.append(q[i])
#     e.append(w[i])
# return e
# for i in range(n):
#     q.append(nums[i])
#     q.append(nums[i+n])
# return q

# //1929 leetcode
# nums = [1,2,1]
# retrun nums*2

# //1480 leetcode
# nums = [1, 2, 3, 4]
# c = 0
# a = []
# for i in nums:
#     c += i
#     a.append(c)
#
# print(a)


# ///algo 151
# s = input()
# counter = 0
# for i in s:
#     if i in 'AaOoEeUuIi':
#         counter += 1
# print(counter)

# //algo 152
# s = input()
# print(str(s[::-1]))

# //algo153
# s = input().split()
# for i in s:
#     print(i, len(i))

# //algo154
# n = input()
# q = 0
# for i in str(n):
#     q += int(i)
# print(q)

# //2114 leetcode
# sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# maxx = 0
# for i in sentences:
#     if len(i.split()) > maxx:
#         maxx = len(i.split())
# print(maxx)


# //2535 leetcode

# nums = [1, 15, 6, 3]
# counter = sum(nums)
# s = sum(map(int, list(''.join(map(str, nums)))))
# print(counter - s)

# nums = [1, 15, 6, 3]
# counter = sum(nums)
# c = 0
# for i in nums:
#     i = str(i)
#     for j in i:
#         c += int(j)
# print(counter - c)

# //147 algo
# s = input()
# counter = 0
# sana = 0
# for i in s:
#     if i == 'A':
#         counter += 1
#     if i == 'Y':
#         sana += 1
# print(counter)
# print(sana)

# //148 algo
# s = input().split()
# q = 0
# for i in s:
#     if i.startswith('A'):
#         print(i)

# //154 algo
# n = int(input())
# tot = 0
# while (n > 0):
#     dig = n % 10
#     tot = tot + dig
#     n = n // 10
# print(tot)

# //155 algo
#
# str = input()
# upper = 0
# for i in range(len(str)):
#     if  str[i].isupper():
#         upper += 1
# print(upper)

# s = input()
# q = 0
# for i in s:
#     if 'a' in i and 'b' in i:
#         q += 1
# print(q)

# n = int(input())
# s = input()
# s = s.replace('$', '')
# print(s)


# class Solution:
#     def replaceDigits(self, s: str) -> str:
#         la = ''
#         for i in range(len(s)):
#             if s[i].isdigit():
#                 l = ord(s[i-1])
#                 la += chr(l+int(s[i]))
#             else:
#                 la += s[i]
#         return la

# def karraJadval():
#     for i in range(1, 10):
#         for j in range(11):
#             print(f"{i} x {j} = {j * i}")
#         print("\n")
# karraJadval()











# rows = 4
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
# rows = 4
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
