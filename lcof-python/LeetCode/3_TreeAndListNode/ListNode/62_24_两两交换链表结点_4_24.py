# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next is None:
            return head
        left,right = head,head.next
        head = right 
        while 1:
            left.next = right.next
            right.next = left
            print(left.val, right.val)
            # 已经交换 
            if left.next is not None:
                temp = left
                left = left.next
            else:
                return head
            if left.next is None:
                return head
            else:
                right = left.next
                temp.next = right
        return head
