# def recursion(s):
#     if s == '':
#         return s
#     elif len(s) == 0:
#         return s
#     else:
#         return recursion(s[1:]) + s[0]
#
#
# ans = []
# dicc = {}
# arr = []
#
# for i in range(len(score)):
#     arr.append(score[i][k])
#
# for j in range(len(score)):
#     dicc[arr[j]] = score[j]
#
# for kk in sorted(dicc.keys(), reverse=True):
#     ans.append(dicc[kk])
#
# return ans

# print(recursion('12345'))

# nums.sort(reverse=True)
#         print(nums)
#         return nums[0]*nums[1]-nums[-2]*nums[-1]
# a = max(nums)
# nums.remove(a)
# b = max(nums)
# nums.remove(b)
#
# c = min(nums)
# nums.remove(c)
# d = min(nums)
#
# return (a * b) - (c * d)
# score = [[10, 6, 9, 1],
#          [7, 5, 11, 2],
#          [4, 8, 3, 15]]
# k = 2
# print(sorted(score, key=lambda i: -i[k]))

# nums = [5, 6, 2, 7, 4]
#
# a = max(nums)
# nums.remove(a)
# b = max(nums)
# nums.remove(b)
# q = min(nums)
# nums.remove(q)
# w = min(nums)
# nums.remove(w)
# print((a * b) - (q * w))
# order = "cba"
# s = "abcd"
# char_dict = {char: idx for idx, char in enumerate(order)}
# sorted_s = sorted(s, key=lambda x: char_dict.get(x, len(order)))
# result = ''.join(sorted_s)
# print(result)

# order = "cba"
# s = "abcd"
# result = ''.join(sorted(s, key=lambda x: order.index(x)))
# print(result)
#


# class Solution:
#     def customSortString(self, order: str, s: str) -> str:
#         s = sorted(s, key=lambda i: (order.index(i) if i in order else ord(i)))
#         return ''.join(s)


s = "YazaAay"
q = 0
w = ''
for i in s:
    if i.lower() == i.upper():
        w += i
    print(i)

