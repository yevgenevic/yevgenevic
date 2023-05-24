'''
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
'''
# leetcode1
# class Solution:
#     def maxDepth(self, s: str) -> int:
#         c = 0
#         max_ = 0
#         for i in s:
#             c += (i == '(') - (i == ')')
#             max_ = max(max_, c)
#         return max_

'''
https://leetcode.com/problems/remove-outermost-parentheses/
'''
# # leetcode2

# s = '(()())(())'
# stack = []
# q = ''
# for i in s:
#     if i == '(':
#         if stack:
#             q += i
#         stack.append(i)
#     elif i == ')':
#         stack.pop()
#         if stack:
#             q += i
# print(q)

'''
https://leetcode.com/problems/remove-outermost-parentheses/
'''
# leetcode3

# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         stack = []
#         for i in s:
#             if len(stack) and stack[-1] == i:
#                 stack.pop()
#             else:
#                 stack.append(i)
#         return ''.join(stack)

'''
https://leetcode.com/problems/make-the-string-great/
'''
# leetcode4


# s = "abBAcC"
# stack = []
# for i in s:
#     if stack and abs(ord(i) - ord(stack[-1])) == 32:
#         stack.pop()
#     else:
#         stack.append(i)
# print(''.join(stack))

'''
https://leetcode.com/problems/valid-parentheses/
'''
# leetcode5
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for i in s:
#             if i in '([{':
#                 stack.append(i)
#             elif len(stack) and (
#                     stack[-1] == '(' and i == ')' or
#                     stack[-1] == '[' and i == ']' or
#                     stack[-1] == '{' and i == '}'):
#                 stack.pop()
#             else:
#                 stack.append(i)
#
#         return not stack

'''
https://leetcode.com/problems/backspace-string-compare/
'''
# leetcode6
# s = "a#c"
# t = "b"
# stack = []
# stek = []
# for S in s:
#     if S == '#' and stack:
#         stack.pop()
#         continue
#     if S != '#':
#         stack.append(S)
# for T in t:
#     if T == '#' and stek:
#         stek.pop()
#         continue
#     if T != '#':
#         stek.append(T)
# print(stack == stek)

'''
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
'''
# leetcode7

# class Solution:
#     def minAddToMakeValid(self, s: str) -> int:
#         stack = []
#         for i in s:
#             if len(stack) and stack[-1] == '(' and i == ')':
#                 stack.pop()
#             else:
#                 stack.append(i)
#         return len(stack)


'''
https://leetcode.com/problems/removing-stars-from-a-string/
'''

# leetcode8


# s = "leet**cod*e"
# list_ = list(s)
# res = []
# for i in list_:
#     if i != '*':
#         res.append(i)
#     else:
#         res.pop()
# print(''.join(res))
'''
https://leetcode.com/problems/rotate-image/
'''
# leetcode11

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# n = len(matrix)
# for i in range(n):
#     for j in range(i, n):
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# for i in range(n):
#     matrix[i] = matrix[i][::-1]
# for i in matrix:
#     print(i)

'''
https://leetcode.com/problems/sort-the-students-by-their-kth-score/
'''
# leetcode13

# class Solution:
#     def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
#         return sorted(score, key=lambda i: -i[k])


'''
https://leetcode.com/problems/add-binary/
'''
# leetcode 15
# a = "11"
# b = "1"
# q = int(a, 2) + int(b, 2)
# print(bin(q)[2:])

'''

'''


# num1 = "11"
# num2 = "123"
# q = 0
# w = 0
# count = 0
# for i, v in enumerate(num1):
#     while str(count) != v:
#         count += 1
#     q += count * 10 ** (len(num1) - 1 - i)
#     count = 0
# for i, v in enumerate(num2):
#     while str(count) != v:
#         count += 1
#     w += count * 10 ** (len(num2) - 1 - i)
#     count = 0
# print(str(q+w))
# leetcode18

# grid = [[4, 3, 2, -1],
#         [3, 2, 1, -1],
#         [1, 1, -1, -2],
#         [-1, -1, -2, -3]]
# count = 0
# rows, cols = len(grid), len(grid[0])
# row, col = 0, cols - 1
# while row < rows and col >= 0:
#     if grid[row][col] < 0:
#         count += rows - row
#         col -= 1
#     else:
#         row += 1
# print(count)
