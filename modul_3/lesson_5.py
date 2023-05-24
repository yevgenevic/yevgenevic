# def rotate(a, b):
#     for i in range(b):
#         a.insert(0, a.pop())
#     return a

# def rotate(l, n):
#     return l[-n:] + l[:-n]
#
# a = [1, 2, 3, 4, 5, 6]
# res = rotate(a, -2)
# print(res)

# def adding(*args):
#     l = []
#     for i in args:
#             l.extend(i)
#     return l
#
#
# d = adding([2, 3, 4], [1, 2],[1,2,3,4,5,6,7,],{1,2})
# print(d)

# def adding(*args):
#     l = []
#     for i in args:
#         if isinstance(i, list):
#             l.extend(i)
#         else:
#             l.append(i)
#     return l
#
#
# d = adding([2, 3, 4], [1, 2], [1, 2, 3, 3, 4, 5, 6, 8, 8, 9, ])
# print(d)

# def adding(*args):
#     return [i for i in args for i in i]
#
#
# d = adding([2, 3, 4], [1, 2], [1, 2, 3, 3, 4, 5, 6, 8, 8, 9, ], [2, 3], [4, 5], [4, 8, 9])
# print(d)
# from itertools import zip_longest
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6, 7, 8],
#     [7, 8, 9, 2],
# ]
# for i in zip(*zip_longest(*matrix, fillvalue=max(i for i in max(matrix)))):
#     print(list(i))
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6, 7, 8],
#     [7, 8, 9, 2],
# ]
# for i in zip_longest(matrix):
#     print(i)
# def zip_longest_easy(*args, fillvalue=None):
#     max_length = max([len(l) for l in args])
#     zipped = []
#     for i in range(max_length):
#         zipped.append(tuple([l[i] if i < len(l) else fillvalue for l in args]))
#     return zipped

#
# def zip_longest(*args, fillvalue=None):
#     maxx = max(len(arg) for arg in args)
#     for i in range(maxx):
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6, 7, 8],
#     [7, 8, 9, 2],
# ]


# def zip_longest(*args, fillvalue=None):
#     maxx = max(len(i) for i in args)  # noqa
#     list_ = []
#     for i in range(maxx):  # noqa
#         q = []
#         for j in args:
#             if i < len(j):
#                 q.append(j[i])
#             else:
#                 q.append(fillvalue)
#         list_.append(q)
#     return list_
#
#
# zipped = zip_longest(*matrix)
# for i in zipped:
#     print(i)

# from math import sqrt
#
# cities = {
#     'Moscow': (550, 370),
#     'London': (510, 510),
#     'Paris': (480, 480),
# }
#
# moscow = cities['Moscow']
# london = cities['London']
#
# distance = sqrt((moscow[0]-london[0])**2 + (moscow[1]-london[1])**2)
# print(distance)

time = "0?:3?"
hour, minute = time.split(':')
if hour == '??':
    hour = '23'
elif hour[0] == '?':
    if hour[1] < 4:
        hour = '2' + hour[1]
    else:
        hour = '1' + hour[1]
elif hour[1] == '?':
    if hour[0] == '2':
        hour = hour[0] + '3'
    else:
        hour = hour[0] + '9'
if minute[0] == '?':
    minute = '5' + minute[1]
if minute[1] == '?':
    minute = minute[0] + '9'
print(hour + ':' + minute)
