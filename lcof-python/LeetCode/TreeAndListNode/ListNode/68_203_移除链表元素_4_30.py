# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        # 创建自己头结点
        myHead = ListNode(-1)
        myHead.next = head
        cur = myHead
        while head:
            if head.val == val:
                cur.next = head.next
                head = head.next
                continue
            cur = cur.next
            head = head.next
        return myHead.next