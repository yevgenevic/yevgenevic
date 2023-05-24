# matrix = [
#     [1, 2, 34],
#     [4, 5, 5],
#     [7, 8, 98]
# ]
# def prime_factors(n):
#     factors = []
#     d = 2
#     while n > 1:
#         while n % d == 0:
#             factors.append(d)
#             n //= d
#         d += 1
#         if d*d > n:
#             if n > 1:
#                 factors.append(n)
#                 break
#     return factors

# sorted_matrix = sorted(matrix, key=lambda row: sum(row))
# print(sorted_matrix)
# s = "2-5g-3-J"
# k = 2
# s = s.replace('-', '').upper()
# print('-'.join(s[i:i + k] for i in range(0, len(s), k))[::-1])
#
#
# sorted_matrix = sorted(matrix, key=lambda row: sum(row))
# print(sorted_matrix)
# s = "2-5g-3-J"
# k = 2
# s = s.replace('-', '').upper()
# print('-'.join(s[i:i + k] for i in range(0, len(s), k))[::-1])

# nums = [1, 1, 0, 1, 1, 1]
# print(len(max(''.join(map(str,nums)).split('0'), key=len)))\
# from collections import Counter
# n = 1_000_000_000_000
# d = 2
# q =


# while n > 1:
#     while n % d == 0:
#         q.append(d)
#         n //= d
#         print(n)
#     d += 1
#     print(d)
#     if d * d > n:
#         if n > 1:
#             q.append(n)
#             break
# print(Counter(q))
# from itertools import groupby
#
# s = "leetcode"
# print(max(len(list(v))for i,v in groupby(s)))

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
# for i in range(m + n):
#     if i >= m:
#         nums1[i] = nums2[i - m]
# for i in range(m + n):
#     for j in range(i + 1, m + n):
#         if nums1[i] > nums1[j]:
#             nums1[i], nums1[j] = nums1[j], nums1[i]
#
# print(nums1)
for i in range(n):
    nums1[m+i]=nums2[i]
print(list(sorted(nums1)))
