# import time
#
#
# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(end - start)
#
#     return wrapper


#
# @timer
# def summa_n():
#     summa = 0
#     for i in range(10_000_000):
#         summa += i
#     print(summa)
#
#
# @timer
# def mul_n():
#     summa = 0
#     for i in range(1, 100):
#         summa *= i
#     print(summa)
#
#
# summa_n()
# mul_n()

# import random
#
#
# @timer
# def random_l():
#     summ = 0
#     s = list(i for i in range(0, 100))
#     for i in s:
#         summ += i
#     print(summ)
#
#
# @timer
# def random_t():
#     summ = 0
#     s = tuple(i for i in range(0, 100))
#     for i in s:
#         summ += i
#     print(summ)
#
#
# random_l()
# random_t()


# import time
#
#
# def timer(func):
#     def wrapper(word: str):
#         if word.isdigit():
#             word = str(int(word)) + 1
#         else:
#             word = word + '1'
#         start = time.time()
#         res = func(word)
#         end = time.time()
#         print(end - start)
#         return res
#
#     return wrapper
#
#
# @timer
# def fun(word: str) -> str:
#     return word
#
#
# word = 'hello world12'
# print(fun(word))

# def to_upper(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper

# decorator and function with params
# def upper(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs).upper()
#     return wrapper
# def lower(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs).lower()
#     return wrapper
# def reverse(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)[::-1]
#     return wrapper
#
#
#
# # @upper
# # @lower
# @reverse
# def hello():
#     return "hello, World!"
#
# print(hello())

# def decorator(*, upper=False, lower=False, to_type=None, reverse=False):
#     def inside(func):
#         def wrapper(word):
#             result = func(word)
#             if upper:
#                 result = result.upper()
#             if lower:
#                 result = result.lower()
#             if to_type:
#                 try:
#                     result = to_type(result)
#                 except Exception as e:
#                     print('Type error',e)
#             if reverse:
#                 result = result[::-1]
#             return result
#
#         return wrapper
#
#     return inside
#
#
# @decorator(upper=True,reverse=True)
# def fun(word):
#     return word
# print(fun('hello'))
#
#  if substr.isdigit() and int(substr) > max_num:
#         max_num = int(substr)


# s = 'hello|123|hjkg5758|'
# max_num = 0
#
# for i in s.split('|'):
#     if i.isdigit() and len(i) > max_num:
#         max_num = len(i)
#
# print(max_num)


