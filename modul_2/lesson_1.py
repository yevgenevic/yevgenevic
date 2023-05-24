x# class Student:
#     def __init__(self, name, age, address, course, university):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.course = course
#         self.university = university
#
#     def __str__(self):
#         return f'{self.name}{self.age}{self.address}{self.course}{self.university}'
#
#
# students = []
# for i in range(2):
#     pass

#
# class Car:
#     def drive(self):
#         print('driving')
#
#
# class Tesla(Car):
#     def drive(self):
#         print('tezroq')
#         super().drive()
#
#
# class Audi(Car):
#     pass
#
#
# tesla = Tesla()
# tesla.drive()

#
# class String:
#     def __init__(self, value):
#         self.value = value
#
#     def reverse(self)->str:
#         return self.value[::-1]
#
#     def slicing(self, a: int, b: int):
#         return self.value[a:b + 1]
#
#     def to_list(self):
#         return list(self.value)
#
#     def count_vowels(self):
#         count = 0
#         for i in self.value:
#             if i in 'aoiueAOUIE':
#                 count += 1
#                 return count
#
#     def __str__(self) -> str:
#         return str(self.value)
#
#
# s = String('Botirjon')
# s = s.reverse()
# print(s)
# s = String("Hello")
# s = s.slicing(2, 5)
# print(s)
# s = String("Alifbo")
# s = s.count_vowels()
# print(s)
# s = String('3 4 5 6')
# s = s.to_list()
# print(s)


# class MasterString:
#     def __init__(self, value):
#         self.value = value
#
#     def reverse(self) -> str:
#         return self.value[::-1]
#
#     def slicing(self, a: int, b: int):
#         return self.value[a:b + 1]
#
#     def to_list(self) -> list:
#         return list(self.value)
#
#     def count_vowels(self):
#         return sum(i in 'aoiueAOIUE' for i in self.value)
#
#     def to_any(self, q: str):
#         if q == tuple():
#             return tuple()
#         if q == list():
#             return list()
#         if q == set():
#             return set()
#         if q == str:
#             return str
#
#
#
# s = MasterString('Botirjon')
# s = s.reverse()
# print(s)
# s = MasterString("Hello")
# s = s.slicing(2, 5)
# print(s)
# s = MasterString("Alifbo")
# s = s.count_vowels()
# print(s)
# s = MasterString('3 4 5 6')
# s = s.to_list()
# print(s)
# s = MasterString(input())
# s = s.to_any()
# print(s)

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#
# head = Node(0)
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
#
# head.next = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
#
# tmp = head.next
# l = []
# while tmp:
#     l.append(tmp.value)
#     tmp = tmp.next
# print(l)


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#
# head = Node('')
# node1 = Node('ab')
# node2 = Node('Botirjon')
# node3 = Node('phone')
# st = head.next
# l = ''
# while st:
#    l = st.value
#     l.replace('o', '')
#     st = st.next
# print(''.join(l))
#
# class A(object):
#
#     def say_hello(self) -> None:
#         print('Hello from class A')
#
#
# class B(object):
#
#     def say_hello(self) -> None:
#         print('Hello from class B')
#
#
# class C(A, B): pass
#
#
# class D(B, A): pass
#
#
# class E(C, D): pass
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
