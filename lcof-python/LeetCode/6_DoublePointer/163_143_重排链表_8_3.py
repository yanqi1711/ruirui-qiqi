# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverstList(self, head):
        if not head:
            return None
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        new_head = self.reverstList(slow.next)
        slow.next = None
        first, second = head, new_head
        while second:
            # 记录后面2个结点
            t1 = first.next
            t2 = second.next
            # 重新连接
            first.next = second
            second.next = t1
            # 重置状态
            first = t1
            second = t2
        return head