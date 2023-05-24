# def say_name(name):
#     def say_goodbye():
#         print('dont say me goodbye, '+ name + '!')
#
#     return say_goodbye
#
# f = say_name('Alisher')
# f2 = say_name('python')
# f()
# f2()

# def smart_divide(func):
#     def inner(a, b):
#         print('men hozir', a, 'va ', b, 'sonlarni bulaman')
#         if b == 0:
#             print('0 ga bulinmaydi')
#             return
#         return func(a, b)
#
#     return inner
#
# @smart_divide
# def divide(a, b):
#     print(a / b)
#
# divide(2,5)
# divide(2,0)

# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 15)
#         func(*args, **kwargs)
#         print("*" * 15)
#     return inner
#
#
# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 15)
#         func(*args, **kwargs)
#         print("%" * 15)
#     return inner
#
#
# @star
# @percent
# def printer(msg):
#     print(msg)
#
# printer("Hello")


# def decorator(*, upper=False, lower=False, to_type=False, reverse=False):
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
#                     print('Erorr', e)
#             if reverse:
#                 result = result[::-1]
#             return result
#
#         return wrapper
#
#     return inside
#
#
# @decorator()
# def fun(word):
#     return word
#
#
# print(fun('hello world'))

