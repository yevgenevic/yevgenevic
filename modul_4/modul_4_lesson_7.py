# # def decorator(func):
# #     def wrapper(*args, **kwargs):
# #         if any(map(lambda x: not isinstance(x, (float, int)), args)) or any(
# #                 map(lambda x: not isinstance(x, str) and len(str(x[1])) > 3, kwargs.items())):
# #             print('warning')
# #         return func(*args, **kwargs)
# #
# #     return wrapper
# #
# #
# # @decorator
# # def fun(*args, **kwargs):
# #     return args, kwargs
# #
# #
# # print(fun(2, 3.3, a=1234))
# import time
# from threading import Thread
#
#
# def task(n):
#     time.sleep(4)
#     print(f'Task {n} bajarildi')
#
#
# start = time.time()
#
# oqimlar = []
# for i in range(10):
#     oqimlar.append(Thread(target=task, args=(i,), daemon=True))
#
# for oqim in oqimlar:
#     oqim.start()
#
# time.sleep(6)
#
# for oqim in oqimlar:
#     oqim.join()
#
# end = time.time()
# print(int(end - start), '- seconds')

# import json
# import time
#
# import httpx
#
# start = time.time()
# response = httpx.get("https://jsonplaceholder.typicode.com/photos").json()
# response1 = httpx.get("https://jsonplaceholder.typicode.com/photos").json()
# end = time.time()
# # print(start - end, ' seconds')
# with open('photos1.json', 'w') as f:
#     json.dump(response, f, indent=2)
# print(start - end, ' seconds')
#
# with open('photos1.yaml', 'w') as f:
#     json.dump(response, f, indent=2)
# print(start - end, ' seconds')
#
#
# import os
# import fitz
#
# file_path = 'python-task.pdf'
#
# images_path = '/home/alisher/Desktop'
# pdf_file = fitz.open(file_path)
#
# page_nums = len(pdf_file)
# images_list = []
# for page_num in range(page_nums):
#     page_content = pdf_file[page_num]
#     images_list.extend(page_content.get_images())
# for i, img in enumerate(images_list, start=1):
#     xref = img[0]
#     base_image = pdf_file.extract_image(xref)
#     image_bytes = base_image['image']
#     image_ext = base_image['ext']
#     image_name = str(i) + '.' + image_ext
#     with open(os.path.join(images_path, image_name), 'wb') as image_file:
#         image_file.write(image_bytes)


#
# import re
# import fitz
#
# pdf_file = "python-task.pdf"
# url_regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=\n]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
# with fitz.open(pdf_file) as file:
#     for page in file:
#         text = page.get_text()
#         for img in page.get_images():
#             rsm = img[0]
#             image = file.extract_image(rsm)
#             with open(f"{rsm}.{image['ext']}", "wb") as f:
#                 f.write(image["image"])
#     for match in re.finditer(url_regex, text):
#         url = match.group()
#         with open('links.txt', 'a') as f:
#             f.write(url + '\n')
