# import json
#
# with open('../imthon proektlar/menu.json', 'r') as f:
#     menu = json.load(f)
# print('Menu\n====')
# for category, items in menu['menu'].items():
#     print(f'{category.title()}')
#     print('---------------------')
#     for item in items:
#         print(f'{item["name"]}: {item["description"]} - ${item["price"]}')
#     print()

# import json
#
# def calculate_menu_price(json_file_path):
#     # Load the JSON file into a Python dictionary
#     with open(json_file_path, 'r') as f:
#         menu_data = json.load(f)
#
#     # Calculate the total price of the menu items
#     total_price = 0
#     for item in menu_data['items']:
#         total_price += item['price']
#
#     # Return the total price
#     return total_price

# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         try:
#             idx = word.index(ch)
#             w = word[:idx + 1]
#             return w[::-1] + word[idx + 1:]
#         except: return word

# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         if ch not in word:
#             return word
#         ind = list(word).index(ch)
#         l = (word[:ind + 1][::-1])
#         word = list(word)
#         word[:ind + 1] = l
#         # print(word)
#
#         return ''.join(word)
#
#
# from insta import accounts
# from instabot import sub, antiban
# from time import *
# from os import *
# from instagramAPI import request
#
# account = "[insta.account/avatar/post/#]
# sub = "inputed.user.username"
# time = "time.sleep(0.3"
#
# sub = input("Please insert your usernme without the @ >")
#
# while True:
#     account.request = 1
#     sub.request = sub
#     time()
#
# # This will generate an account, follow your Instagram and loop it.
#
# while sub < 5000:
#     time.sleep("24H")
#     antiban.on
#     run.loop()
#
# # You have free antiban under 5000 followers a day. Over this its at your own risks.


