# //task1
# import json
#
# import httpx
#
# for i in range(20):
#     htp = httpx.get('https://api.chucknorris.io/jokes/random')
#     hazil = htp.json()
#     hazil_val = hazil['value']
#     hazil_id = hazil['id']
#     with open(f'{hazil_id}.json', 'w') as f:
#         json.dump(hazil, f, indent=2)
# print('succesful')

# //task3
import httpx
import psycopg2

con = psycopg2.connect(
    dbname='exam',  # noqa
    user='ali',
    password='1',
    host='localhost'
)
cur = con.cursor()


for i in range(2):
    response = httpx.get(url="https://api.chucknorris.io/jokes/random")
    data = response.json()
    joke = data["value"]
    created_at = data['created_at']
    updated_at = data['updated_at']
    url = data['url']
    categories = data['categories']
    cur.execute("INSERT INTO jokes (joke,created_at,updated_at,url,categories) VALUES (%s,%s,%s,%s,%s)", (joke,created_at,updated_at,url,categories,))
    print(joke)
con.commit()

# import json
# task3
# import os
# import httpx
#
# url = "https://api.chucknorris.io/jokes/random"
#
# for e in range(20):
#     htp = httpx.get(url)
#     joke = json.loads(htp.text)
#     create = joke['created_at'].split("T")[0]
#     year, month, day = create.split("-")
#     day1 = ''
#     for q in day.split(' ')[:-1]:
#         day1 += q
#     dir_name = f"{year}/{month}/{day1}"
#     if not os.path.exists(dir_name):
#         os.makedirs(dir_name)
# //task4
# v1
# import httpx
# from PIL import Image
# from io import BytesIO
# import os
#
# url = "https://jsonplaceholder.typicode.com/photos?_limit=20"
#
# response = httpx.get(url)
#
# if response.status_code == 200:
#     data = response.json()
#     for item in data:
#         img_url = item['url']
#         img_response = httpx.get(img_url)
#         img = Image.open(BytesIO(img_response.content))
#         img.save(f"{item['id']}.jpg")
# else:
#     print("Error: ", response.status_code)

# v2
import httpx
from PIL import Image
from io import BytesIO
import os

url = "https://jsonplaceholder.typicode.com/photos"

response = httpx.get(url)

if response.status_code == 200:
    if not os.path.exists("images"):
        os.makedirs("images")
    data = response.json()
    for item in data:
        img_url = item['url']
        img_response = httpx.get(img_url)
        img = Image.open(BytesIO(img_response.content))
        img.save(f"images/{item['id']}.jpg")
else:
    print("Error: ", response.status_code)


