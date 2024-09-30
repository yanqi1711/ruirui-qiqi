# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:   
        myHead = ListNode(-1)
        fast,slow = myHead,myHead
        myHead.next = head
        while 1:
            fast = fast.next
            n -= 1
            if n == 0:
                break
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return myHead.next