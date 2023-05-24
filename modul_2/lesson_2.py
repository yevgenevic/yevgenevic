#
#
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next
#
#     def __str__(self):
#         return f"{self.value}->{self.next}"
#
#
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
# node9 = ListNode(9)
# node7 = ListNode(7)
# node8 = ListNode(8)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node8.next = node9
# node9.next = node4
# node4.next = node5
# print(node1)
# print(node8)
#
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next
#
#     def __str__(self):
#         return f"{self.value}->{self.next}"
#
#
# node1 = ListNode(2)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
#
# node6 = ListNode(3)
# node7 = ListNode(3)
# node8 = ListNode(4)
# node9 = ListNode(5)
#
# node6.next = node7
# node7.next = node8
# node8.next = node9
#
# node8 = ListNode(1)
# node9 = ListNode(2)
# node10 = ListNode(3)
# node11 = ListNode(4)
# node12 = ListNode(5)
#
# node8.next = node9
# node9.next = node10
# node10.next = node11
# node11.next = node12
#
# node8 = ListNode(8)
# node9 = ListNode(9)
# node10 = ListNode(4)
# node11 = ListNode(4)
# node12 = ListNode(5)
#
# node8.next = node9
# node9.next = node10
# node10.next = node11
# node11.next = node12
#
# node11 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
# node11.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
#
# node17 = ListNode(3)
# node18 = ListNode(6)
# node19 = ListNode(9)
# node20 = ListNode(4)
# node21 = ListNode(4)
# node22 = ListNode(5)
#
#
# node17.next = node18
# node18.next = node19
# node19.next = node20
# node20.next = node21
# node21.next = node22
#
# node23 = ListNode(8)
# node24 = ListNode(9)
# node25 = ListNode(7)
# node26 = ListNode(4)
# node27 = ListNode(4)
# node28 = ListNode(5)
#
#
# node23.next = node24
# node24.next = node25
# node25.next = node26
# node26.next = node27
# node27.next = node28
# print(node1)
# print(node6)
# print(node11)
# print(node8)
# print(node17)
# print(node23)
#
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#     def __str__(self):
#         return f"{self.val}->{self.next}"
#
#
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
# node6 = ListNode(6)
# node7 = ListNode(7)
# node8 = ListNode(8)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6
# node6.next = node7
# node7.next = node8
#
# head = node1
# tmp = head
# while tmp:
#     if not tmp.val & 1:
#         print(tmp.val, end="")
#     tmp = tmp.next
# tmp = head
# print()
#
# while tmp:
#     if tmp.val & 1:
#         print(tmp.val, end="")
#     tmp = tmp.next
# tmp = head
#
# print(head)
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#     def __str__(self) -> str:
#         return f'{self.val}->{self.next}'
#
#
# class LinkedList:
#     def __init__(self, val=0, next=None):
#         self.head = ListNode(val, next)
#
#     def from_list(self, a: list) -> None:
#         tmp = self.head  # 0->1->2->3->4->5
#         for i in a:
#             tmp.next = ListNode(i)
#             tmp = tmp.next
#
#         self.head = self.head.next
#
#     def print_ll(self) -> None:
#         tmp = self.head
#         while tmp:
#             print(tmp.val, end=' ')
#             tmp = tmp.next
#
#     def length(self) -> int:
#         q = 0
#         tmp = self.head
#         while tmp:
#             q = +1
#             tmp = tmp.next
#         return q
#
#     def example(self) -> int:
#
#         tmp = self.head
#         summa = ''
#         while tmp:
#             summa += str(tmp.val)
#             tmp = tmp.next
#         return int(summa)
#
#
# a = [1, 2, 3, 4, 5]
#
# ll = LinkedList()
# print(ll.head)
# print(ll.length())
# print(ll.example())
#
# toq = []
# juft = []
# for i in range(10):
#     if i & 1:
#         toq.append(i)
#     else:
#         juft.append(i)
# file = open('text.txt', 'a')
# file.write(f"juft - {''.join(map(str, juft))}\n")
# file.write(f"toq - {''.join(map(str, toq))}\n")
# Definition for singly-linked list.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         newList=ListNode()
#         tail=newList
#         while(list1 and list2):
#             if(list1.val<list2.val):
#                 tail.next=list1
#                 list1=list1.next
#             else:
#                 tail.next=list2
#                 list2=list2.next
#             tail=tail.next
#         tail.next = list1 or list2
#         return newList.next
#
#
# def isPalindrome(self, head: Optional[ListNode]) -> bool:
#     res = []
#     n = head
#     while (n):
#         res.append(n.val)
#         n = n.next
#     return res == res[::-1]