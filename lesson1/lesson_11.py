# s = '((a)(bd))(fds(f2f(3))(f))'
# stack = []
#
# c = []
# for i in s:
#     if not i.isalpha() and not i.isdigit():
#         if i == '(':
#             c.append(i)
#         elif len(c) and c[-1] == '(':
#             c.pop()
#         else:
#             c.append(i)
#
# if len(c):
#     print("natog'ri qavs")
# else:
#     print("tog'ri qavs")


# s = '{()[]{}}'
# c = []
# for i in s:
#     if '(' and '{' and '[' in i:
#         c.append(i)
#     elif len(c) and c[-1] == '(' and '[' and '{':
#         c.pop()
#     else:
#         c.append(i)
# print(bool(c))

#


# //20. Valid Parentheses leetcode
# s = '(()[()])'
# stack = []
#
# for i in s:
#     if i in '([{':
#         stack.append(i)
#     elif len(stack) and (
#             stack[-1] == '(' and i == ')' or
#             stack[-1] == '[' and i == ']' or
#             stack[-1] == '{' and i == '}'):
#         stack.pop()
#     else:
#         stack.append(i)
#
# print(not stack)

# //1614 leetcode
# s = "(1)+((2))+(((3)))"
# c = 0
# max_ = 0
# for i in s:
#     c += (i == '(') - (i == ')')
#     max_ = max(max_, c)
# print(max_)

# //1047. Remove All Adjacent Duplicates In String  LEETCODE
# s = "azxxzy"
# stack = []
# for i in s:
#     if len(stack) and stack[-1] == i:
#         stack.pop()
#     else:
#         stack.append(i)
# print(''.join(stack))

# 1544. Make The String Great LEETCODE

# s = "((("
# stack = []
# for i in s:
#     if len(stack) and stack[-1] == '(' and i == ')':
#         stack.pop()
#     else:
#         stack.append(i)
# return len(stack)


# //155 algo
# str = input().split()
# upper = 0
# for i in str:
#     if i[0].isupper():
#         upper += 1
# print(upper)

# //160 algo

# s = input()
# print(s.swapcase())
# //algo 166
# def G(a, b):
#     return (pow(a, 2) + pow(b, 2)) / (pow(a, 2) + (2 * a * b) + (3 * b ** 2) + 4)
#
#
# t, s = map(float, input().split())
# s = G(1.2, s) + G(t, s) + G(2 * s - 1, s * t)
# print(f"{s:.2f}")

# //leetcode 1221
# s = "RLRRLLRLRL"
# counter = 0
# sana = 0
# for i in s:
#     if i == 'R':
#         counter += 1
#     if i == 'L':
#         counter -= 1
#     if counter == 0:
#         sana += 1
# print(sana)
# //557 leetcode
# s = input()
# return " ".join([word[::-1]] for word in s.split(" ")])

# sentence = "leetcode"
# if len(set(sentence))==26:
#     print(True)
# else:
#     print(False)

# sentence = "thequickbrownfoxjumpsoverthelazydog"
# counter = 0
# s = 'qwertyuioplkjhgfdsazxcvbnm'
# if  sentence in s:
#     print('true')
# else:
#     print('false')

# //1662 leetcode
# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
# s1 = ""
# s2 = ""
# for i in word1:
#     s1 += i
# for i in word2:
#     s2 += i
# print(s1 == s2)


# 1816. Truncate Sentence leetcode

# s = "Hello how are you Contestant"
# k = 4
# print(' '.join(s.split()[:k]))

# //1684 leetode
# allowed = "ab"
# words = ["ad", "bd", "aaab", "baa", "badab"]
# k = 0
# for word in words:
#     if set(word) <= set(allowed):
#         k += 1
# return k

# for i in range(5):
#     for j in range(-6, -i):
#         print(" ", end=" ")
#     for s in range(i + 1):
#         print('*', end=" ")
#     print()

# rows = int(input())
#
# k = 0
#
# for i in range(1, rows + 1):
#     for space in range(1, (rows - i) + 1):
#         print(end="  ")
#
#     while k != (2 * i - 1):
#         print("* ", end="")
#         k += 1
#
#     k = 0
#     print()

# 1844. Replace All Digits with Characters leetcode

# s = "a1c1e1"
# la = ''
# for i in range(len(s)):
#     if s[i].isdigit():
#         l = ord(s[i - 1])
#         la += chr(l + int(s[i]))
#     else:
#         la += s[i]
# print(la)

# //1967 leetcode
# patterns = ["a", "abc", "bc", "d"]
# word = "abc"
# count = 0
# for i in patterns:
#     if i in word:
#         count+=1
# return count

# words = ["abc", "car", "ada", "racecar", "cool"]
#
# for i in words:
#     if i == i[::-1]:
#         return i

# class Solution:
#     def areOccurrencesEqual(self, s: str) -> bool:
#         return len(set(Counter(s).values())) == 1
# //leetcode 1941
# from collections import Counter
#
# s = "abacbc"
# print(len(set(Counter(s).values())) == 1)

# word1 = "abc"
# word2 = "pqr"
# q = len(word1) + len(word2)
# new = []
# for i in range(len(word1)):
#     for i in range(len(word2)):
#         new.append(word1[i] + word2[i])
# print(new)

# n = list(map(int, input().split()))
# mat = sum(n) // len(n)
# w = []
# for i in n:
#     if mat > i:
#         w.append(i)
# print(*w)

# n = list(map(int, input().split()))
# mat = sum(n) // len(n)
# print([i for i in n if mat > i])

'''
1.Berilgan parametr boyicha bolib chiqilsa nechta segment bo'ladi

O'zbekistonni-     alishmasman boshqa jahonga-    O'zbeksiton tengdir-    O'zbekistonga
-
4ta
'''


# str = input()
# b = input()
# print(len(str.split(sep=b)))


# s = input().split()
# re = []
# for i in s:
#     if i.endswith('NA'):
#         re.append(i)
#
# print(len(re))
# print(*re)


# input()
# a = input().split()
# hi = {'A':2 , 'S':2 , 'L':1 , 'O':1 , 'M':1}
# for k , v in hi.items():
#     if a.count(k) < v:
#         print('NO')
#         break
# else:
#     print('YES')


# ---------  1  ----------------
# massiv = '123245467665'
#
# for i in range(3):
#     print(massiv[:4])
#     massiv = massiv[4:]

# ---------- 2 -----------------

# m = '1867345'
# l , k = map(int , input().split())
# txt = ''
# for i , v in enumerate(m):
#     if l <= i+1 and k>i+1:
#         pass
#     else:
#         txt += v

# print(txt)

# ---------- 3 --------------

# m = '1867345'
# l , k = map(int , input().split())
# print(m[l-1:k-1])

# ----------- 4 -------------
# m = "is2 this1 book3 and4 name6 my5 is7 Botirjon8".split()
# m.sort(key = lambda x : x[-1])
# print(' '.join(map(lambda x : x[:-1] , m)))

# ------------ 5 -------------

# s = "codeleet"
# indices = [4,5,6,7,0,2,1,3]
# list_ = []
# for i in range(len(s)):
#     list_.append(s[i] + str(indices[i]))
#
# print(''.join(map(lambda x : x[:-1] , sorted(list_, key=lambda x: x[-1]))))

# ----------- 6 ------------

# a = "g()()()(al)(987654)"
# # () = o

# a = a.replace('()', 'o')
# txt = ''
# for i in a:
#     if '(' == i or ')' == i:
#         pass
#     else:
#         txt += i
# print(txt)

# --------------- 7 ----------------------

# deck = [1,2,3,4,4,3,7,1]
# print(deck == deck[::-1])

# ----------------- 8 -------------------

# nums = [3,2,10,1,9]
#
# print(nums.index(max(nums)) + 1)
# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         res = 0
#         while head:
#             res = 2*res + head.val
#             head = head.next
#         return res

# def isPalindrome(s):
#     return s == s[::-1]
#
#
# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)
#
# if ans:
#     print("Yes")
# else:
#     print("No")


# def rotate_image(matrix):
#     n = len(matrix)
#     # transpose the matrix
#     for i in range(n):
#         for j in range(i, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     # reverse each row
#     for i in range(n):
#         matrix[i] = matrix[i][::-1]
#     return matrix