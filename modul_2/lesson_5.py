#
# url = 'https://jsonplaceholder.typicode.com/posts'
# response = httpx.get(url)
# if response.status_code == 200:
#     data = response.json()
#     with open('posts.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
# url = 'https://jsonplaceholder.typicode.com/comments'
# response = httpx.get(url)
# if response.status_code == 200:
#     data = response.json()
#     with open('comments.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
# url = 'https://jsonplaceholder.typicode.com/albums'
# response = httpx.get(url)
# if response.status_code == 200:
#     data = response.json()
#     with open('albums.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
# url = 'https://jsonplaceholder.typicode.com/photos'
# response = httpx.get(url)
# if response.status_code == 200:
#     data = response.json()
#     with open('photos.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
# url = 'https://jsonplaceholder.typicode.com/todos'
# response = httpx.get(url)
# if response.status_code == 200:
#     data = response.json()
#     with open('todos.json', 'w') as f:
#         json.dump(data, f, indent=2)

# url = ['https://jsonplaceholder.typicode.com/posts', 'https://jsonplaceholder.typicode.com/comments',
#        'https://jsonplaceholder.typicode.com/albums', 'https://jsonplaceholder.typicode.com/photos',
#        'https://jsonplaceholder.typicode.com/todos']
# files = ['posts.json', 'comments.json', 'albums.json', 'photos.json', 'todos.json']
#
#
# def url(url):
#     response = httpx.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         with open('') as f:
#             json.dump(data, f, indent=2)

# import httpx
# import json
#
#
# def write_data(filename: str) -> None:
#     url = f'https://jsonplaceholder.typicode.com/{filename}'
#     response = httpx.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         with open(f'{filename}.json', 'w') as f:
#             json.dump(data, f, indent=2)
#     print(f'{filename} faylga yozildi!')
#
#
# names = ('posts', 'comments','todos','users','photos','albums','comments')
# for name in names:
#     write_data(name)

# import json
# #
# # # //d
# # # // posts
# with open('posts.json') as f:
#     posts: list[dict] = json.load(f)
# # # //r
# # //coments
# with open('comments.json') as f:
#     coments: list[dict] = json.load(f)
#
# for coment in coments:
#     sub_p = []
#     for post in posts:
#         if post['id'] == coment['id']:
#             sub_p.append({
#                 'id': post['id']
#             })
#     coment['id'] = sub_p
#
# with open('task_.json', 'w') as f:
#     json.dump(coments, f, indent=2)
'''
////////////////??/////////////////////////////////////////////         HOMEWORK       ////////////////////////////////////////////////////////////////////////////


'''
'''
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

'''
TASK 1
'''
# // 1
#  import json
#
# with open('posts.json') as f:
#     posts: list[dict] = json.load(f)
# with open('comments.json') as f:
#     comments: list[dict] = json.load(f)
# for post in posts:
#     sub_district = []
#     for coments in comments:
#         if post['id'] == coments['id']:
#             sub_district.append({
#                 'id': coments['id'],
#                 'name': coments['name'],
#                 'email': coments['email'],
#                 'body': coments['body']
#             })
#         post['comments'] = sub_district
# with open('task_posts.json', 'w') as f:
#     json.dump(posts, f, indent=2)
#
#

# // 2
# import json
#
# with open('posts.json') as f:
#     posts: list[dict] = json.load(f)
#
# with open('users.json') as f:
#     users: list[dict] = json.load(f)
# with open('albums.json') as f:
#     albums: list[dict] = json.load(f)
#
# for user in users:
#     sub_district = []
#     for post in posts:
#
#         if user['id'] == post['id']:
#             sub_district.append({
#                 'id': post['id'],
#                 'title': post['title'],
#                 'body': post['body'],
#             }
#             )
#     user['posts'] = sub_district
#     sup_district = []
#     for album in albums:
#
#         if user['id'] == album['id']:
#             sup_district.append({
#                 'id': album['id'],
#                 'title': album['title']
#             })
#     user['albums'] = sup_district
#
# with open('task_users.json', 'w') as f:
#     json.dump(users, f, indent=2)

# //3


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


'''
TASK 2
'''

# import json
#
# with open('users.json') as f:
#     users: list[dict] = json.load(f)
# with open('albums.json') as f:
#     albums: list[dict] = json.load(f)
# with open('photos.json') as f:
#     photos: list[dict] = json.load(f)
# for user in users:
#     sub_district = []
#     for album in albums:
#
#         if user['id'] == album['id']:
#             sub_district.append({
#                 'id': album['id'],
#                 'title': album['title']
#             })
#         sup_district = []
#         for album in albums:
#
#             for photo in photos:
#                 if album['id'] == photo['id']:
#                     sup_district.append({
#                         'id': photo['id'],
#                         'title': photo['title'],
#                         'url': photo['url'],
#                         'thumbnailUrl': photo['thumbnailUrl']
#                     })
#     user['albums'] = sub_district
#     user['photo'] = sup_district
#     with open('task2.users.json', 'w') as f:
#         json.dump(user, f, indent=4)

'''
TASK 3
'''
# # //1
# import httpx
# import json
#
# base_url = 'https://jsonplaceholder.typicode.com/'
# posts = httpx.get(base_url + 'posts').json()
#
#
#
# def remove_key(item):
#     item.pop('postId')
#     return item
#
#
# for post in posts[:5]:
#     post_comments = httpx.get(base_url + f'comments?postId={post["id"]}').json()
#     post['comments'] = list(map(remove_key, post_comments))
#
# with open('task_posts.json', 'w') as f:
#     json.dump(posts, f, indent=2)

# //2
import httpx
import json

# base_url = 'https://jsonplaceholder.typicode.com/'
# users = httpx.get(base_url + 'users').json()
# posts = httpx.get(base_url + 'posts').json()
#
#
# def remove_key(item):
#     item.pop('userId')
#     return item
#
#
# for user in users[:5]:
#     user_posts = httpx.get(base_url + f'posts?userId={user["id"]}').json()
#     user['posts'] = list(map(remove_key, user_posts))
#     user_posts = httpx.get(base_url + f'albums?userId ={user["id"]}').json()
#     user['albums'] = list(map(remove_key, user_posts))
#
# with open('task2_posts.json', 'w') as f:
#     json.dump(users, f, indent=2)
#
# import requests
# import json
#
# for i in range(20):
#     response = requests.get('https://api.chucknorris.io/jokes/random')
#     joke = response.json()
#
#     with open(f'joke_{i}.json', 'w') as f:
#         json.dump(joke, f)
#
# print("Barcha jokeslar fayllarga yozildi.")
import os
import httpx

url = "https://api.chucknorris.io/jokes/random"

for e in range(20):
    htp = httpx.get(url)
    joke = json.loads(htp.text)

    create = joke['created_at'].split("T")[0]
    year, month, day = create.split("-")
    day1 = ''
    for q in day.split(' ')[:-1]:
        day1 += q

    dir_name = f"{year}/{month}/{day1}"

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


# //3

#
# import httpx
# import json
#
# base_url = 'https://jsonplaceholder.typicode.com/'
# users = httpx.get(base_url + 'users').json()
#
#
# def remove_key(item):
#     item.pop('userId')
#     return item
#
#
# for user in users:
#     user_posts = httpx.get(base_url + f'posts?userId={user["id"]}').json()
#     user['posts'] = list(map(remove_key, user_posts))
# with open('task3_albums.json', 'w') as f:
#     json.dump(users, f, indent=2)


# //4
#
# import httpx
# import json
#
# base_url = 'https://jsonplaceholder.typicode.com/'
# users = httpx.get(base_url + 'users').json()
# posts = httpx.get(base_url + 'photos').json()
# albums = httpx.get(base_url + 'albums').json()
#
#
# def remove_key(item):
#     item.pop('userId')
#     return item
#
#
# for album in albums:
#     user_albums = httpx.get(base_url + f'photos?albumId = {album["id"]}').json()
#     album['photos'] = list(map(remove_key, user_albums))
# users = httpx.get(base_url + 'users').json()
# for user in users[:5]:
#     sub_district = []
#     for album in albums:
#         if user["id"] == album["userId"]:
#             sub_district.append({
#                 'id': album['id'],
#                 'title': album['title'],
#                 'photos': album['photos']
#             })
#         user['albums'] = sub_district
# with open('task2.users.json', 'w') as f:
#     json.dump(users, f, indent=2)
