'''
1108. Defanging an IP Address
'''
import math

# 1
# address = "1.1.1.1"
# print(address.replace('.','[.]'))

# 2
# address = "1.1.1.1"
# q = ''
# for i in address:
#     if i!='.':
#         q+=i
#     else:
#         q+='[.]'
# print(q)

'''
2011. Final Value of Variable After Performing Operations
# '''
# operations = ["--X", "X++", "X++"]
# x = 0
# for i in operations:
#     if i == '++X' or i == 'X++':
#         x += 1
#     elif i == '--X' or i == 'X--':
#         x -= 1
# print(x)

'''
771. Jewels and Stones
'''
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         count = 0
#         for j in jewels:
#             count += stones.count(j)
#         return count

'''
2114. Maximum Number of Words Found in Sentences
'''
# 1
# sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# mx = 0
# for i in sentences:
#     if len(i.split())>mx:
#         mx = len(i.split())
# print(mx)

# 2
# sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# print(max(sentences.count(' ')for i in sentences)+1)

# s = "luffy is still joyboy"
# l = 0
# for i in s:
#     if i==' ':
#         l = 0
#     else:
#         l+=1
# print(l)

# l = list(s.split(' '))
# print(len(l[-1])
#
#
# )

'''
1748. Sum of Unique Elements
'''
# from collections import Counter
#
# nums = [1, 2, 3, 2]
# counter = Counter(nums)
# res = 0
# for i, v in enumerate(nums):
#     if counter[v] == 1:
#         res += v
# print(res)

'''
2418. Sort the People
'''
# names = ["Mary", "John", "Emma"]
# heights = [180, 165, 170]
# print([names[heights.index(i)] for i in sorted(heights)[::-1]])

'''

'''
# nums = [1, 3, 5, 6]
# target = 7
# start = 0
# end = len(nums) - 1
# while start <= end:
#     middle = (start + end) // 2
#     if nums[middle] == target:
#         print(middle)
#     elif target > nums[middle]:
#         start = middle + 1
#     else:
#         end = middle - 1
# print(end + 1)
# nums.append(target)
# nums.sort()
# print(nums.index(target))

'''
14.Longest Common Prefix
'''
# strs = ["dog","racecar","car"]
# if not strs:
#     print('')
# elif len(strs) == 1:
#     print(strs[0])
# else:
#     strs.sort()
#     result = ''
#     for i in range(len(strs[0])):
#         if strs[0][i]==strs[-1][i]:
#             result+=strs[0][i]
#         else:
#             break
#     print(result)
from collections import Counter

'''
136. Single Number
'''
# def singleNumber(nums):
#     count = 0
#     for i in nums:
#         count = count^i
#     return count
#
# nums = [4, 1, 2, 1, 2]
# print(singleNumber(nums))
#
# nums = [4, 1, 2, 1, 2]
# a = set(nums)
# for i in a:
#     nums.remove(i)
# print(*a-set(nums))

'''
missing numbers
'''
nums = [3, 0, 1]

# maxx = nums[0]  # noqa
# for i in nums:
#     if i > maxx:
#         maxx = i
# minx = nums[0]
# for i in nums:
#     if i < minx:
#         minx = i
# q = maxx + 1
# res = []
# for i in nums:
#     maxx = maxx - 1
#     if maxx not in nums:
#         res.append(maxx)
# print(res)
# combined_array = nums + list(range(0,len(nums)+1))
# res = 0
# for i in combined_array:
#     res ^= i
# return res
# return sum(list(range(0, len(nums) + 1))) - sum(nums)

'''

'''
# n = 2
# if n==1:
#     print(1)
# if n==2:
#     print(2)
# if n==0:
#     print(0)

# x = 16
# if x>=0:
#     s = int(math.sqrt(x))
#     print((s*s)==x)
# else:
#
#     print(False)
x= 1534236469
if x < 0:
    reverse_num = int(str(x)[:0:-1]) * -1
else:
    reverse_num = int(str(x)[::-1])
print(reverse_num)
