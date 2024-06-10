# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 0:
            return head
        length = 1
        countHead = head
        while True:
            if countHead.next is None:
                break
            countHead = countHead.next
            length+=1
        print(length , k)
        if length == 1 or (k % length == 0):
            return head
        skip = length - (k%length)
        temp = head
        for i in range(skip-1):
            temp = temp.next
        print(temp.val)
        start, end = temp.next,temp.next
        temp.next = None
        while True:
            if end is None or end.next is None: 
                break
            end = end.next
        if end is None:
            return start
        if end.next is None:
            end.next = head
        return start