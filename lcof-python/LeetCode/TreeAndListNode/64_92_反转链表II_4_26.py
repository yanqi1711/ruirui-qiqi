# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        if right <= left:
            return head
        index = 0
        result = head
        pre = None
        cur = head
        flag = False
        while True:
            index += 1
            if index == left:
                if left != 1:
                    leftNode = pre
                else:
                    leftNode = cur
                    flag = True
            elif index == right:
                if flag:
                    leftNode.next = cur.next
                    cur.next = pre
                    return cur
                else:
                    leftNode.next.next = cur.next
                    leftNode.next = cur
                    cur.next = pre
                    return result
            # index == left 此时这个节点要指向right.next
            if index > left and index < right:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
                continue
            else:
                pre = cur
                cur = cur.next