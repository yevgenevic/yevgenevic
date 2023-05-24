# address = "1.1.1.1"
# # print(address.replace('.','[.]')
# q = ''
# for i in address:
#     if i == '.':
#         q += '[.]'
#     else:
#         q += i
# print(q)

# operations = ["X++", "++X", "--X", "X--"]
# x = 0
#
# for i in operations:
#     if i == '++X' or i == 'X++':
#         x += 1
#     elif i == '--X' or i == 'X--':
#         x -= 1
# print(x)
# c = 0
# for i in operations:
#     if i[1]=='+':
#         c+=1
#     else:
#         c-=1
# print(c)
# jewels = "aA",
# stones = "aAAbbbb"
# # count = set(jewels)
# # print(sum(i in count for i in stones))
# counter = 0
# for i in stones:
#     if i in jewels:
#         counter += 1
# print(counter)

# sentences = ["please wait", "continue to fight", "continue to win"]
# print(1 + max(s.count(' ') for s in sentences))
# command = "G()(al)"
# q = ''
# print(command.replace('()', 'o').replace('(al)', 'al'))

# s = "RLRRLLRLRL"
# l = 0
# ans = l
# for c in s:
#     if c == 'L':
#         l += 1
#     else:
#         l -= 1
#     if l == 0:
#         ans += 1
# print(ans)

# s = "race a car"
# s = ''.join(filter(str.isalnum, s)).lower()
# print(s == s[::-1])
# s = "10#11#12"
# result = []
# i = 0
# while i < len(s):
#     if i < len(s) - 2 and s[i + 2] == "#":
#         num = int(s[i:i + 2])
#         result.append(chr(num + 96))
#         i += 3
#     else:
#         num = int(s[i])
#         result.append(chr(num + 96))
#         i += 1
# print("".join(result))
# word = "FlaG"
# if word.isupper() or word.islower() or word.istitle():
#     print(True)
# else:
#     print(False)
# s = "codeleet"
# indices = [4, 5, 6, 7, 0, 2, 1, 3]
# res = [''] * len(s)
# for i in range(len(s)):
#     res[indices[i]] = s[i]
# print(''.join(res))

s = "egg"
t = "add"
print([s.index(i) for i in s] == [t.index(i) for i in t])
print([s.index(i) for i in s] == [t.index(i) for i in t])
