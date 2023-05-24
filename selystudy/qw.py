while True:
    n = int(input('raqam kriting: '))
    match n:
        case 1:
            print('Barcha mahsulotlar: ')
            print('id''===''nomi''===''narxi')
            print('=' * 50)
            show_products()
            print('=' * 50)
            print(menu)
        case 2:
            add_products(input('Ismi: '), int(input('Narxi: ')), int(input('Miqdori: ')))
            print('Mahsulot qushildi')
            print('=' * 50)
            print(menu)
        case 3:
            show_products()
            m = input('mahsulot id sini kriting: ')
            delete_products(m)
            print("O'chirildi")
            print('=' * 50)
            print(menu)
        case 4:
            show_products()
            change_products(input('ID: '), input('nomi: '), input('Narxi: '), input('Miqdori: '))
            print("O'zgartirildi")
            print('=' * 50)
            print(menu)
        case 5:
            break






# import csv
#
# with open('person.csv') as file:
#     q = 0
#     for row in csv.reader(file):
#         if row[4] != 'Male' and row[4] != 'Female':
#             q += 1
#             print(row[1], " ", row[2], " ", row[4])
# print(q)
# import csv
# q = []
# with open('cars.csv') as file:
#     for row in csv.reader(file):
#         if row[-1] != 'age':
#             if int(row[-1]) >= 2000:
#                 q.append(row)
# scar = sorted(q, key=lambda x: x[-1])
# for car in scar:
#     print(*car)
# import csv
#
# m = []
# q = 0
# with open('cars.csv') as file:
#     for row in csv.reader(file):
#         if row[-1] != 'age':
#             if int(row[-1]) >= 2000 and row[2] == 'Mercedes-Benz':
#                 m.append(row)
#                 q += 1
# scar = sorted(m, key=lambda x: x[-1])
# for car in scar:
#     print(*car)
# print(q)
# import csv
#
# q = []
# w = 0
# with open('people.csv') as file:
#     for row in csv.reader(file):
#         if row[0] != 'id':
#             if int(row[-2]) <= 2005 and row[1][0] == 'A':
#                 q.append(row)
#                 w += 1
# name = sorted(q, key=lambda x: x[3])
# for nm in name:
#     print(*nm)
# print(w)
# import csv
#
# q = []
# with open('people.csv') as file:
#     for row in csv.reader(file):
#         if row[0] != 'id':
#             if 'er' in row[1] or 'er ' in row[2]:
#                 q.append(row)
# city = sorted(q, key=lambda x: x[-1])
# for cr in city:
#     print(*cr)

# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         try:
#             q = word.index(ch)
#             w = word[:q + 1]
#             return w[::-1] + word[q + 1:]
#         except Exception:
#             return word

# from array import *
#
#
# def array_list(array_num):
#     num_list = array_num.tolist()
#     print(num_list)
#
#
# array_num = array('i', [45, 34, 67])
# array_list(array_num)
# import numpy as np
#
#
# arr = np.array([[1, 2, 3], [4, 5, 6]])
#
# print(f'Matritsa:\n{arr}')

# import numpy as np
#
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# flat_list = arr.flatten().tolist()
#
# print(flat_list)

# mat = [
#     [1, 2, 3],
#     [2, 4, 5],
#     [3, 4, 6]
# ]
# l = []
# for i in mat:
#     l += i

# def longest_palindrome(words):
#     max_palindrome = ''
#     for word in words:
#         if len(word) > len(max_palindrome) and word == word[::-1]:
#             max_palindrome = word
#     return max_palindrome
#
#
# words = ['salom', 'shoxrux', 'anna', 'madam', 'wow']
# print(longest_palindrome(words))

# def sum_numbers(lst):
#     total = 0
#     for i in lst:
#         if isinstance(i, (int, float)):
#             total += i
#     return total
#
# def sum_numbers(lst):
#     return sum([item for item in lst if isinstance(item, (int, float))])
# my_list = [1, '2', 3.5, 'hello', 5]
# print(sum_numbers(my_list))

# while True:
#     user_input = input("Iltimos, istalgan matn kiriting ('stop' tugmasi bilan to'xtatish uchun): ")
#     if user_input.lower() == "stop":
#         print("Dastur tugatildi.")
#         break
#     else:
#         print("Siz kiritgan matn: ", user_input)


# text = input("Matnni kiriting: ")
# count = 0
# vowels = "aeiouAEIOU"
# for char in text:
#     if char in vowels:
#         count += 1
# print("Matnda", count, "ta unli harf bor.")
