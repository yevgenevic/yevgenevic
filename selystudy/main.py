# l = [8, 4, 2, 9]
# l.sort()
# print(l)
#
# tuple_ = 26, 7, 4, 5
# sorted_ = tuple(sorted(tuple_))
# print(sorted_)
#
# s = {8, 32, 5, 7, 2}
# print(sorted(s))
#
# d = {6: 8, 5: 4, 3: 9, 2: 8}
# print(sorted(d.items(), key=lambda i: i[0]))
#
# s = 'hello world 51235'
# print(''.join(sorted(s)))
# a = [8, 2, 7, 7, 3, 6]
# q = []
# w = []
# for i in a:
#     if i % 2 == 1:
#         q.append(i)
#         q.sort()
#     elif i % 2 == 0:
#         w.append(i)
#         w.sort()
#
# q.extend(w)
# print(q)

# def most_frequent(List):
#     return max(set(List), key=List.count)
#
#
# List = [2, 1, 2, 2, 1, 3, 3, 3,5,3]
# print(most_frequent(List))


# l = [
#     (8, 6, 3),
#     (2, 3, 7),
#     (8, 2, 8),
#     (5, 6, 2),
#     (8, 4, 6),
#     (5, 7, 9)
# ]
# print(sorted(l),end=" ")

# a = [7, 4, 2, 5, 1, 6, 9, 3]


a.sort(key=lambda i: (not i & 1, i if i & 1 else -i))
print(a)

# l = ['hello', 'name', 'word', 'list', 'tuple', 'valijon', 'alijon', 'python']
# l.sort(key=lambda i: (sum(j in 'aeiou' for j in i), len(i)))
# print(l)

# d = {
#     'key1': 'botirjon',
#     'key2': 'valijon',
#     'key3': 'toshmat',
#     'key4': 'eshmat',
#     'key5': 'botirjon 2'
# }

# print(dict(sorted(d.items(), key=lambda i: -len(i[1]))))


# d = {
#     'key1': 'botirjon',
#     'key2': 'valijon',
#     'key3': 'toshmat',
#     'key4': 'eshmat',
#     'key5': 'botirjon 2'
# }
# print(sorted(d.items(), key=lambda a: -len(a[1])))

''''
a = [7, 4, 2, 5, 1, 6, 9, 3, 8]
6 kichiklar sonlar kamayuvchi, juft osuvchi, toq kamayuvchi
5 4 3 2 1 6 8 9 7
'''''

# a = [7, 4, 2, 5, 1, 6, 9, 3, 8]
# a.sort(key=lambda i: (-i if i < 6 else i & 1, -i if i & 1 else i))
# print(tuple(a))


s = ["h","e","l","l","o"]
print(s.reverse())

















