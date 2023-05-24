# file = open('photos.txt', 'r')
# cc = 0
# c = 0
# w = ' '
# for i in file.readlines():
#     for j in i:
#         if j in w:
#             cc += 1
#         if j.isalnum() and j not in w:
#             c += 1
#     print(cc, c, )
#     file.close()
#     c = 0
#     cc = 0
# from collections import Counter
#
#
# class Solution:
#     def reformatDate(self, date: str) -> str:
#         months = {
#             'Jan' : '01',
#             'Feb' : '02',
#             'Mar' : '03',
#             'Apr' : '04',
#             'May' : '05',
#             'Jun' : '06',
#             'Jul' : '07',
#             'Aug' : '08',
#             'Sep' : '09',
#             'Oct' : '10',
#             'Nov' : '11',
#             'Dec' : '12',
#         }
#
#         day, month, year = date.split()
#
#         day = day[ : -2 ] # remove st or nd or rd or th
#         day = '0' + day if len( day ) == 1 else day # needs to be 2 digits
#
#         return year + '-' + months[ month ] + '-' + day
# # d = Counter()

# with open('photos.txt') as f:
#     #   while data := f.read(5000):
#     data = f.read()
#     d.update(Counter(data))
#
# if d.get(' '): d.pop(' ')
# if d.get('\n'): d.pop('\n')
#
# print(*d.most_common(1))
from datetime import datetime, date

#
# class Solution:
#     def reformatDate(self, date: str) -> str:
#         oylar = {
#             'Jan': '01',
#             'Feb': '02',
#             'Mar': '03',
#             'Apr': '04',
#             'May': '05',
#             'Jun': '06',
#             'Jul': '07',
#             'Aug': '08',
#             'Sep': '09',
#             'Oct': '10',
#             'Nov': '11',
#             'Dec': '12',
#         }
#
#         kun, oy, yil = date.split()
#         kun = kun[:-2]
#         kun = '0' + kun if len(kun) == 1 else kun
#         return yil + '-' + oylar[oy] + '-' + kun
#
# if __name__ == '__main__':
#     b = "20th Feb 2052"
#     a = Solution()
#     print(a.reformatDate(b))


# def func(fun):
#     def wrapper():
#         print(8)
#
#     return wrapper()
#
#
# @func
# def add():
#     print(2)
from colorama import Style, Back, Fore
print(Back.BLACK)
print( Fore.BLUE + 'helllo')
print( Fore.LIGHTCYAN_EX+ 'helllo')
