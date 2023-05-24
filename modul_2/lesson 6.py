# import json
#
# with open('posts.json') as f:
#     posts: list[dict] = json.load(f)
# with open('users.json') as f:
#     users: list[dict] = json.load(f)
#
# for user in users:
#     sub_district = []
#     for post in posts:
#         if user['id'] == post['id']:
#             sub_district.append({
#                 "id": post['id'],
#                 "title": post['title'],
#                 "body": post['body']
#             }
#             )
#     user['posts'] = sub_district
# with open('task_albums.json', 'w') as f:
#     json.dump(users, f, indent=2)
# import json
#
# name = input('enter name : ')
# price = int(input('enter price : '))
# quantity = int(input('enter count : '))
#
# x = [{
#     'name': name,
#     'price': price,
#     'quantity': quantity
# }]
# with open('task_.json', 'a') as f:
#     json.dump(x, f, indent=4)
import subprocess

# import httpx
# import json
#
# url = 'https://www.boredapi.com/api/activity'
# q = httpx.get(url).json()
# sub = []
# for user in range(20):
#    sub.append(user)
# with open('task_.json', 'a') as f:
#     json.dump(, f, indent=4)
# from collections import Counter
# import json
#
# s = 'hello jhjkgjhg du 6576tibx hhgsj'
# counter = {}
# count = 0
# q = 'aioue'
# for i in s:
#     if q not in i:
#         count += 1
# with open('task_.json', 'w') as f:
#     json.dump(count, f, indent=2)
#
# import json
#
# s = 'hellodhasjg djhgasjdgh12 jge12'
# d = {}
# for i in s:
#     if i.isalpha() and i.lower() not in 'auioe':
#         if d.get(i):
#             d[i] += 1
#         else:
#             d[i] = 1
# with open('task_.json', 'w') as f:
#     json.dump(d, f, indent=2)


# from collections import defaultdict
#
# import httpx
# import json
#
# url = 'https://www.boredapi.com/api/activity'
#
# activities: dict = defaultdict(list)
# # 'recreational': [
# #     {
# #         "activity": "Start a collection",
# #         "participants": 1,
# #         "price": 0,
# #         "link": "",
# #         "key": "1718657",
# #         "accessibility": 0.5
# #     },
# #     {
# #         "activity": "Try a food you don't like",
# #         "participants": 1,
# #         "price": 0.1,
# #         "link": "",
# #         "key": "6693574",
# #         "accessibility": 0.05
# #     }
# # ],
# # 'busywork': [
# #     {
# #         "activity": "Draft your living will",
# #         "participants": 1,
# #         "price": 0,
# #         "link": "https://www.investopedia.com/terms/l/livingwill.asp",
# #         "key": "2360432",
# #         "accessibility": 0.5
# #     }
# # ]
#
#
# for _ in range(20):
#     response = httpx.get(url).json()
#     activities[response.pop('type')].append(response)
#
# data = [{'type': key, 'data': value} for key, value in activities.items()]
#
# with open('activities.json', 'w') as f:
#     json.dump(data, f, indent=2)

# import httpx
# import json
#
# url = 'https://api.first.org/data/v1/countries'
# response = httpx.get(url).json()
# c = []
# for i, v in response['data'].items():
#     c.append({
#         'country': v['country'],
#         'region': v['region']
#     })
# with open('task_.json', 'w') as f:
#     json.dump(c, f, indent=2)


# import httpx
# import json
#
# url = 'https://api.first.org/data/v1/countries'
# response = httpx.get(url).json()
# c = []
# for i, v in response['data'].items():
#     if v['region'] in v['Africa']:
#         c.append({
#             'region': v['country']
#         })
# with open('task_.json', 'w') as f:
#     json.dump(c, f, indent=2)
