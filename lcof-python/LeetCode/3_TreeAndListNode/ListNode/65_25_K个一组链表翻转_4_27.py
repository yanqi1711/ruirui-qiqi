# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head, tail):
        #  [1 2 3 4 5] 6->prev
        prev = tail.next
        p = head
        while prev != tail:
            temp = p.next
            p.next = prev
            prev = p
            p = temp
        return tail , head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 创造头节点 这样返回就只需要返回hair.next
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                # 找到None了 直接返回
                if not tail:
                    return hair.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            pre = tail
            head = tail.next
        return hair.next