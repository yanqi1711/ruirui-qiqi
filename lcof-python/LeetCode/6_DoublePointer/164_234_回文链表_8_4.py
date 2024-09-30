# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head):
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

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return None
        slow = fast = head
        # 和143的找中点有不同 143会让slow在后面
        # 如果是奇数都可以 
        # 偶数本题 会让slow偏前
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        new = self.reverseList(slow.next)
        slow.next = None
        cur = head
        while cur and new:
            if new.val != cur.val:
                return False
            cur = cur.next
            new = new.next
        return True