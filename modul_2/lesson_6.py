# import os
#
# exclude = ('.idea', 'venv')
# files = ''
# maxx = 0
# for i in os.listdir():
#     if i not in exclude:
#         if os.path.isdir(i):
#             s = os.listdir(i)
#             for j in s:
#                 file = open(i + '/' + j, 'r')
#                 s = file.read()
#                 if len(s) > maxx:
#                     maxx = len(s)
#                     files = j
# print(files)
# # import os
# # import json
# # from collections import defaultdict
# #
# # exclude = ('venv', '.idea')
# # a = defaultdict(list)
# # for i in os.listdir():
# #     if i not in exclude:
# #         if os.listdir():
# #             if i.endswith('json') and i.endswith('py'):
# #                 format = i.rsplit('.')
# #                 a[format[-1]].append(format[0])
# # print(r)
# # with open('task_.json', 'w') as f:
# #     json.dump(r, f, indent=2)
#
# from collections import defaultdict
#
# a = defaultdict(list)
# for i in os.listdir():
#     if not os.path.isdir(i):
#         format = i.rsplit(".")
#         a[format[-1]].append(format[0])
# with open("task_.json", 'w') as f:
#     json.dump(a, f, indent=4)


# def fun(id=None, name=None, age=None):
#     pass

#
# class List:
#     def __int__(self, value, l=list):
#         self.value = value
#         self.l = l
#
#     def slicing(self, a: int, b: int):
#         return self.value[a:b + 1]
#
#     def multiply(self, l):
#         for i in l:
#             q = l * i
#             l.append(q)
#         return l
#
#     def add(self, l):
#         for i in l:
#             q = l + i
#             l.append(q)
#         return l
#
#
# l = [2, 3, 4]
# s = List()
# s.slicing(1, 2)
# print(s)

# import json
# import os
# from collections import defaultdict
#
# data = defaultdict(list)
#
# for i in os.listdir():
#     if os.path.isfile(i):
#         name, ext = i.rsplit('.', 1)
#         data[ext].append(name)
#
# with open('data.json', 'w') as f:
#     json.dump(data, f, indent=2)

import os
import json

exclude = ('.idea', 'venv')

result = {}

for i in os.listdir():
    if i in exclude:
        continue
    d = {}
    if os.path.isdir(i):
        for j in os.listdir(i):
            if os.path.isfile(i + '/' + j):
                d[j] = 'file'

    result[i] = d if d else 'file'

with open('data.json', 'w') as f:
    json.dump(result, f, indent=2)
