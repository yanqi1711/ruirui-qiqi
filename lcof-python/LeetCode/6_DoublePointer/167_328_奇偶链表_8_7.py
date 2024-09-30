# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        evenHead = head.next
        odd, even = head, evenHead
        #  1 2 3 4 5 -> odd:1 3 5 even: 2 4
        #  1 2 3 4   -> odd:1 3(odd在这) 4 even: 2
        # 所以只需要 odd.next = evenHead
        while even and even.next:
            # 先奇数
            odd.next = even.next
            odd = odd.next
            # 偶数
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head