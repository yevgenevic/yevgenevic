# d = [
#     {
#         'name': 'botirjon',
#         'age': 18,
#         'address': 'Toshkent'
#     },
#     {
#         'name': 'botirjon',
#         'age': 13,
#         'address': 'Toshkent'
#     },
#     {
#         'name': 'botirjon',
#         'age': 15,
#         'address': 'Toshkent'
#     }
# ]
# for i in d:
#     if i['age'] < 16:
#         print(i)

# from pprint import pprint
#
# student = {
#     'name': 'Botirjon 2',
#     'age': 15,
#     'address': 'Toshkent viloyati'
# }
#
# d = [
#     {
#         'name': 'botirjon',
#         'age': 18,
#         'address': 'Toshkent'
#     },
#     {
#         'name': 'botirjon',
#         'age': 13,
#         'address': 'Toshkent'
#     },
#     {
#         'name': 'botirjon',
#         'age': 15,
#         'address': 'Toshkent'
#     }
# ]
# for i in d:
#     if i['age'] < 15 and i['age'] % 2 == 0:
#        i.update(student)
# pprint(d)
# s = input()
# d = {}
# for i in s:
#     if d.get(i):
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

''''exam?'''
'''exam?'''

# //4
# string1 = input()
#
# new_string = ''.join((x for x in string1 if not x.isdigit()))
#
# print(new_string)

# //7

# class Solution:
#     def hasGroupsSizeX(self, deck: List[int]) -> bool:
#         count = collections.Counter(deck)
#         val = count.values()
#         import math
#         m = math.gcd(*val)
#         if m >= 2:
#             return True
#         else:
#             return False


# //5

# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         ans = ""
#         for i in range(len(indices)):
#             ans += s[indices.index(i)]
#         return ans
#
# //8
# nums = [3, 2, 10,1, 9]
# num = nums[0]
# ind = 0
# for i, v in enumerate(nums):
#     if v > num:
#         num = v
#         ind = i + 1
# print(num, ind)
# #
# //3
# m = input()
# l, k = map(int, input().split())
# for i, v in enumerate(m):
#     if i > l - 2 and k - 1 > i:
#         print(int(v), end="")
