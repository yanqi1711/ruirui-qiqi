# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 额外内容：判断是否有环
# 1 双指针 o(n) o(1)
# 2 哈希 o(n) o(n)
# class Solution:
#     def hasCycle(self , head: ListNode) -> bool:
#         if not head:
#             return False
#         if head.next is None:
#             return False
#         slow = head
#         fast = slow
#         while fast and slow:
#             slow = slow.next
# 			# 判断是否有环 无环直接false
#             if fast.next:
#                 fast = fast.next.next
#             else:
#                 return False
#             if slow == fast:
#                 return True
# 	#   fast或者slow为None
#         return False


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow = pHead
        fast = pHead
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                fast = pHead
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None