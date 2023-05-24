# class Node:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
#
#
# t = [20, 45, 9, 56]
# head = Node(0)
# temp = head
# for i in t:
#     temp.next = Node(i)
#     temp = temp.next
# b: Node = head.next
# while b:
#     print(b.val, end=" ")
#     b = b.next

#
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Linkedlist:
#     def __init__(self):
#         self.head = Node(0)
#
#     def from_list(self, a: list):
#         tpm = self.head
#         for i in a:
#             tpm.next = Node(i)
#             tpm = tpm.next
#
#     def ll_print(self):
#         tpm = self.head.next
#         while tpm:
#             print(tpm.val, end=' ')
#             tpm = tpm.next
#
#
# a = [1, 2, 3, 4, 5]
# b = Linkedlist()
# b.from_list(a)
# b.ll_print()
#
#
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Linkedlist:
#     def __init__(self):
#         self.head = Node(0)
#
#     def from_list(self, a: list):
#         tpm = self.head
#         for i in a:
#             tpm.next = Node(i)
#             tpm = tpm.next
#
#     def ll_print(self):
#         tpm = self.head.next
#         while tpm:
#             print(tpm.val, end=' ')
#             tpm = tpm.next
#
#     def append(self, new):
#         new_n = Node(new)
#         tmp = self.head
#         while tmp.next:
#             tmp = tmp.next
#         tmp.next = new_n
#
#     def insert(self, index, new_val):
#         new_node = Node(new_val)
#         c = 0
#         tmp = self.head
#         while tmp.next:
#             if c == index:
#                 new_node.next = tmp.next
#                 tmp.next = new_node
#             tmp = tmp.next
#             c += 1
#
#     def pop(self, index):
#         tmp = self.head
#         c = 0
#         while tmp.next:
#
#             if c == index and tmp.next.next != None:
#                 tmp.next = tmp.next.next
#             elif c == index and tmp.next.next == None:
#                 tmp.next = None
#                 break
#             tmp = tmp.next
#             c += 1
#
#     def remove(self, qiymat):
#         pass
#
#
# a = [1, 2, 3, 4, 5]
# b = Linkedlist()
# b.from_list(a)
# b.insert(3, 90)
# b.append([3, 4])
# b.pop(4)
# b.ll_print()



